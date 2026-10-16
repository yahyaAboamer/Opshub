import { createHash } from 'node:crypto';
import { mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { afterAll, beforeAll, describe, expect, inject, it } from 'vitest';
import { loadMigrations, migrate, MIGRATION_LOCK_KEY, REPOSITORY_MIGRATIONS_DIR } from './index';
import {
  advisoryLockWaiters,
  appliedHistory,
  ddlCount,
  dropDatabase,
  expectBoundaryError,
  installDdlTripwire,
  openClient,
  provisionDatabase,
  relationExists,
  removeMigrationsDirs,
  schemaExists,
  waitFor,
  withClient,
  writeMigrationsDir,
  type ProvisionedDatabase,
} from './testing';

const created: ProvisionedDatabase[] = [];
const fresh = async () => {
  const db = await provisionDatabase(inject('postgres'));
  created.push(db);
  return db;
};
afterAll(async () => {
  for (const db of created) await dropDatabase(db);
  removeMigrationsDirs();
});

describe('T0003-TEST02 serialized ordered SQL migrations', () => {
  it('applies the repository migrations to a clean database', async () => {
    const db = await fresh();
    const result = await migrate({ connection: db.migrator, expected: db.expected });
    expect(result).toMatchObject({ alreadyApplied: 0 });
    expect(result.applied.map((m) => `${m.version}:${m.name}`)).toEqual(['1:opshub_schema_baseline']);
    const history = await appliedHistory(db);
    expect(history.map((h) => [h.version, h.name, h.sha256])).toEqual([
      [1, 'opshub_schema_baseline', result.applied[0]?.sha256],
    ]);
    expect(history[0]?.applied_by).toBe(db.migratorLogin);
    const owners = await withClient(db.admin, async (c) =>
      (
        await c.query(`select n.nspname, pg_get_userbyid(n.nspowner) as owner from pg_namespace n
                       where n.nspname in ('opshub', 'opshub_migration') order by 1`)
      ).rows,
    );
    expect(owners).toEqual([
      { nspname: 'opshub', owner: 'opshub_schema_owner' },
      { nspname: 'opshub_migration', owner: 'opshub_schema_owner' },
    ]);
  });

  it('second run is a no-op that issues no DDL', async () => {
    const db = await fresh();
    await migrate({ connection: db.migrator, expected: db.expected });
    await installDdlTripwire(db);
    const second = await migrate({ connection: db.migrator, expected: db.expected });
    expect(second).toEqual({ applied: [], alreadyApplied: 1 });
    expect(await ddlCount(db)).toBe(0);
    expect((await appliedHistory(db)).length).toBe(1);
  });

  it('concurrent runners serialize on the advisory lock and apply each migration exactly once', async () => {
    const db = await fresh();
    const holder = await openClient(db.admin);
    try {
      await holder.query('select pg_advisory_lock($1, $2)', [...MIGRATION_LOCK_KEY]);
      const runners = Promise.allSettled([
        migrate({ connection: db.migrator, expected: db.expected, lockTimeoutMs: 60_000 }),
        migrate({ connection: db.migrator, expected: db.expected, lockTimeoutMs: 60_000 }),
      ]);
      // Barrier: both runners have passed the guard and are queued on the migration lock before it is released.
      await waitFor(async () => (await advisoryLockWaiters(db)) === 2, 'two runners waiting on the migration lock');
      expect(await schemaExists(db, 'opshub_migration')).toBe(false);
      await holder.query('select pg_advisory_unlock($1, $2)', [...MIGRATION_LOCK_KEY]);
      const settled = await runners;
      const results = settled.map((s) => {
        if (s.status === 'rejected') throw s.reason;
        return s.value;
      });
      expect(results.map((r) => [r.applied.length, r.alreadyApplied]).sort()).toEqual([
        [0, 1],
        [1, 0],
      ]);
      expect((await appliedHistory(db)).map((h) => h.version)).toEqual([1]);
    } finally {
      await holder.end();
    }
  });

  it('gives up with MIGRATION_LOCK_TIMEOUT while another runner holds the lock', async () => {
    const db = await fresh();
    const holder = await openClient(db.admin);
    try {
      await holder.query('select pg_advisory_lock($1, $2)', [...MIGRATION_LOCK_KEY]);
      await expectBoundaryError(
        migrate({ connection: db.migrator, expected: db.expected, lockTimeoutMs: 300 }),
        'MIGRATION_LOCK_TIMEOUT',
      );
      expect(await schemaExists(db, 'opshub_migration')).toBe(false);
    } finally {
      await holder.end();
    }
  });
});

describe('T0003 migration protocol', () => {
  it('loadMigrations accepts only contiguous NNNN_slug.sql files', async () => {
    const good = writeMigrationsDir({ '0001_first.sql': 'select 1;\n', '0002_second_step.sql': 'select 2;\n' });
    const loaded = await loadMigrations(good);
    expect(loaded.map((m) => [m.version, m.name, m.fileName])).toEqual([
      [1, 'first', '0001_first.sql'],
      [2, 'second_step', '0002_second_step.sql'],
    ]);
    expect(loaded[0]?.sha256).toBe(createHash('sha256').update('select 1;\n').digest('hex'));
    expect(await loadMigrations(writeMigrationsDir({}))).toEqual([]);

    const repository = await loadMigrations(REPOSITORY_MIGRATIONS_DIR);
    expect(repository.map((m) => m.fileName)).toEqual(['0001_opshub_schema_baseline.sql']);

    const rejects: Array<[Record<string, string>, Parameters<typeof expectBoundaryError>[1]]> = [
      [{ '0001_init.down.sql': 'drop schema x;' }, 'MIGRATION_BAD_FILENAME'],
      [{ '0001_init.sql': 'select 1;', 'README.md': 'notes' }, 'MIGRATION_BAD_FILENAME'],
      [{ '1_init.sql': 'select 1;' }, 'MIGRATION_BAD_FILENAME'],
      [{ '0001_Init.sql': 'select 1;' }, 'MIGRATION_BAD_FILENAME'],
      [{ '0001_a.sql': 'select 1;', '0003_c.sql': 'select 3;' }, 'MIGRATION_SEQUENCE_GAP'],
      [{ '0002_b.sql': 'select 2;' }, 'MIGRATION_SEQUENCE_GAP'],
      [{ '0001_a.sql': 'select 1;', '0001_b.sql': 'select 1;' }, 'MIGRATION_DUPLICATE_VERSION'],
      [{ '0001_a.sql': '  \n-- only a comment\n' }, 'MIGRATION_EMPTY'],
    ];
    for (const [files, code] of rejects) {
      await expectBoundaryError(loadMigrations(writeMigrationsDir(files)), code, Object.keys(files).join(','));
    }
    const withSubdir = writeMigrationsDir({ '0001_a.sql': 'select 1;' });
    mkdirSync(join(withSubdir, '0002_dir.sql'));
    await expectBoundaryError(loadMigrations(withSubdir), 'MIGRATION_BAD_FILENAME', 'subdirectory');
  });

  it('refuses an applied migration whose file changed', async () => {
    const db = await fresh();
    const original = { '0001_fx_base.sql': 'create schema fx;\n' };
    await migrate({ connection: db.migrator, expected: db.expected, migrationsDir: writeMigrationsDir(original) });
    const run = (files: Record<string, string>) =>
      migrate({ connection: db.migrator, expected: db.expected, migrationsDir: writeMigrationsDir(files) });
    await expectBoundaryError(run({ '0001_fx_base.sql': 'create schema fx; -- edited\n' }), 'MIGRATION_CHECKSUM_MISMATCH');
    await expectBoundaryError(run({ '0001_fx_renamed.sql': 'create schema fx;\n' }), 'MIGRATION_NAME_MISMATCH');
    await expectBoundaryError(
      run({ '0001_fx_base.sql': 'create schema fx; -- edited\n', '0002_fx_more.sql': 'create table fx.t(id int);\n' }),
      'MIGRATION_CHECKSUM_MISMATCH',
    );
    expect(await relationExists(db, 'fx.t')).toBe(false);
    expect((await appliedHistory(db)).map((h) => h.version)).toEqual([1]);
  });

  it('refuses history that is ahead of the migration files', async () => {
    const db = await fresh();
    const files = { '0001_fx_base.sql': 'create schema fx;\n', '0002_fx_t.sql': 'create table fx.t(id int);\n' };
    await migrate({ connection: db.migrator, expected: db.expected, migrationsDir: writeMigrationsDir(files) });
    await expectBoundaryError(
      migrate({ connection: db.migrator, expected: db.expected, migrationsDir: writeMigrationsDir({ '0001_fx_base.sql': files['0001_fx_base.sql'] }) }),
      'MIGRATION_UNKNOWN_APPLIED',
    );
  });

  it('a failed migration rolls back completely and is repaired forward', async () => {
    const db = await fresh();
    const base = 'create schema fx;\n';
    const broken = 'create table fx.items(id int primary key);\ninsert into fx.missing values (1);\n';
    const fixed = 'create table fx.items(id int primary key);\n';
    const failure = await expectBoundaryError(
      migrate({ connection: db.migrator, expected: db.expected, migrationsDir: writeMigrationsDir({ '0001_fx_base.sql': base, '0002_fx_items.sql': broken }) }),
      'MIGRATION_FAILED',
    );
    expect(failure.detail).toMatchObject({ version: 2, name: 'fx_items', sqlState: '42P01' });
    expect((await appliedHistory(db)).map((h) => h.version)).toEqual([1]);
    expect(await relationExists(db, 'fx.items')).toBe(false);

    const repaired = await migrate({
      connection: db.migrator,
      expected: db.expected,
      migrationsDir: writeMigrationsDir({ '0001_fx_base.sql': base, '0002_fx_items.sql': fixed }),
    });
    expect(repaired.applied.map((m) => m.version)).toEqual([2]);

    const forward = await migrate({
      connection: db.migrator,
      expected: db.expected,
      migrationsDir: writeMigrationsDir({
        '0001_fx_base.sql': base,
        '0002_fx_items.sql': fixed,
        '0003_fx_items_label.sql': 'alter table fx.items add column label text;\n',
      }),
    });
    expect(forward).toMatchObject({ alreadyApplied: 2 });
    expect(forward.applied.map((m) => m.version)).toEqual([3]);
    expect((await appliedHistory(db)).map((h) => h.version)).toEqual([1, 2, 3]);
  });

  it('pins search_path so a connection option cannot redirect unqualified names', async () => {
    const db = await fresh();
    const failure = await expectBoundaryError(
      migrate({
        connection: { ...db.migrator, options: '-c search_path=opshub_migration' },
        expected: db.expected,
        migrationsDir: writeMigrationsDir({ '0001_unqualified.sql': 'create table unqualified_t(id int);\n' }),
      }),
      'MIGRATION_FAILED',
    );
    expect(failure.detail).toMatchObject({ version: 1, sqlState: '3F000' });
    expect(await relationExists(db, 'opshub_migration.unqualified_t')).toBe(false);
  });

  it('detects a migration that escapes its transaction', async () => {
    const db = await fresh();
    await expectBoundaryError(
      migrate({
        connection: db.migrator,
        expected: db.expected,
        migrationsDir: writeMigrationsDir({ '0001_escape.sql': 'create schema esc;\ncommit;\ncreate table esc.t(id int);\n' }),
      }),
      'MIGRATION_TRANSACTION_ESCAPED',
    );
    expect(await appliedHistory(db)).toEqual([]);
  });
});

describe('T0003 schema owner versus runtime role', () => {
  let db: ProvisionedDatabase;
  beforeAll(async () => {
    db = await fresh();
    await migrate({ connection: db.migrator, expected: db.expected });
  });

  it('runtime role can use the app schema but cannot create objects or read migration history', async () => {
    const privileges = await withClient(db.admin, async (c) =>
      (
        await c.query(`select has_schema_privilege('opshub_runtime', 'opshub', 'USAGE') as usage,
                              has_schema_privilege('opshub_runtime', 'opshub', 'CREATE') as create,
                              has_schema_privilege('opshub_runtime', 'opshub_migration', 'USAGE') as history_usage`)
      ).rows[0],
    );
    expect(privileges).toEqual({ usage: true, create: false, history_usage: false });
    await withClient(db.runtime, async (c) => {
      await expect(c.query('create table opshub.runtime_ddl(id int)')).rejects.toMatchObject({ code: '42501' });
      await expect(c.query('select * from opshub_migration.applied_migrations')).rejects.toMatchObject({ code: '42501' });
    });
  });

  it('the migrator login has no owner privileges until it sets the owner role', async () => {
    await withClient(db.migrator, async (c) => {
      await expect(c.query('create table opshub.login_ddl(id int)')).rejects.toMatchObject({ code: '42501' });
      await c.query('set role opshub_schema_owner');
      await c.query('create table opshub.login_ddl(id int)');
      await c.query('drop table opshub.login_ddl');
    });
  });
});
