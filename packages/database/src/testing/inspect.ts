import assert from 'node:assert/strict';
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { MIGRATION_LOCK_KEY } from '../catalog';
import { DatabaseBoundaryError, type DatabaseErrorCode } from '../errors';
import { withClient, type ProvisionedDatabase } from './provision';

/**
 * DDL tripwire: an event trigger that advances a sequence on every ddl_command_start. Sequence advances are not
 * transactional, so the count survives a rolled-back transaction: 0 proves no DDL statement was even attempted.
 */
export async function installDdlTripwire(db: ProvisionedDatabase): Promise<void> {
  await withClient(db.admin, async (c) => {
    await c.query('create schema t0003_tripwire');
    await c.query('create sequence t0003_tripwire.ddl_seen');
    await c.query(`create function t0003_tripwire.count_ddl() returns event_trigger language plpgsql
                   security definer set search_path = pg_catalog
                   as $$ begin perform nextval('t0003_tripwire.ddl_seen'); end $$`);
    await c.query('create event trigger t0003_ddl_tripwire on ddl_command_start execute function t0003_tripwire.count_ddl()');
    await c.query("select setval('t0003_tripwire.ddl_seen', 1, false)");
  });
}

export async function ddlCount(db: ProvisionedDatabase): Promise<number> {
  return withClient(db.admin, async (c) => {
    const { rows } = await c.query('select last_value, is_called from t0003_tripwire.ddl_seen');
    return rows[0].is_called ? Number(rows[0].last_value) : 0;
  });
}

export async function schemaExists(db: ProvisionedDatabase, schema: string): Promise<boolean> {
  return withClient(db.admin, async (c) => (await c.query('select to_regnamespace($1) is not null as present', [schema])).rows[0].present);
}

export async function relationExists(db: ProvisionedDatabase, relation: string): Promise<boolean> {
  return withClient(db.admin, async (c) => (await c.query('select to_regclass($1) is not null as present', [relation])).rows[0].present);
}

export interface HistoryRow {
  version: number;
  name: string;
  sha256: string;
  applied_by: string;
}

export async function appliedHistory(db: ProvisionedDatabase): Promise<HistoryRow[]> {
  if (!(await relationExists(db, 'opshub_migration.applied_migrations'))) return [];
  return withClient(db.admin, async (c) =>
    (await c.query<HistoryRow>('select version, name, sha256, applied_by from opshub_migration.applied_migrations order by version')).rows,
  );
}

/** Sessions waiting (not granted) on this database's migration advisory lock. */
export async function advisoryLockWaiters(db: ProvisionedDatabase): Promise<number> {
  return withClient(db.admin, async (c) => {
    const { rows } = await c.query(
      `select count(*)::int as n from pg_locks l join pg_database d on d.oid = l.database
       where l.locktype = 'advisory' and not l.granted and d.datname = $1
         and l.classid = $2 and l.objid = $3 and l.objsubid = 2`,
      [db.name, ...MIGRATION_LOCK_KEY],
    );
    return rows[0].n;
  });
}

export async function waitFor(condition: () => Promise<boolean>, label: string, timeoutMs = 20_000): Promise<void> {
  const deadline = Date.now() + timeoutMs;
  while (!(await condition())) {
    if (Date.now() > deadline) throw new Error(`timed out waiting for: ${label}`);
    await new Promise((resolve) => setTimeout(resolve, 50));
  }
}

const checkError = (error: unknown, code: DatabaseErrorCode, label?: string): DatabaseBoundaryError => {
  const where = label ? ` (${label})` : '';
  assert.ok(error instanceof DatabaseBoundaryError, `expected DatabaseBoundaryError ${code}${where}, got ${String(error)}`);
  assert.equal(error.code, code, `wrong error code${where}: ${error.message}`);
  return error;
};

/** Asserts a synchronous call or a promise fails with the given boundary error code, and returns the error. */
export function expectBoundaryError(run: () => unknown, code: DatabaseErrorCode, label?: string): DatabaseBoundaryError;
export function expectBoundaryError(run: Promise<unknown>, code: DatabaseErrorCode, label?: string): Promise<DatabaseBoundaryError>;
export function expectBoundaryError(
  run: (() => unknown) | Promise<unknown>,
  code: DatabaseErrorCode,
  label?: string,
): DatabaseBoundaryError | Promise<DatabaseBoundaryError> {
  if (typeof run === 'function') {
    try {
      run();
    } catch (error) {
      return checkError(error, code, label);
    }
    assert.fail(`expected ${code}${label ? ` (${label})` : ''}, but the call succeeded`);
  }
  return run.then(
    () => assert.fail(`expected ${code}${label ? ` (${label})` : ''}, but the operation succeeded`),
    (error: unknown) => checkError(error, code, label),
  );
}

const tempDirs: string[] = [];

/** Writes synthetic migration files to a fresh temporary directory. */
export function writeMigrationsDir(files: Record<string, string>): string {
  const dir = mkdtempSync(join(tmpdir(), 't0003-migrations-'));
  tempDirs.push(dir);
  for (const [fileName, sql] of Object.entries(files)) writeFileSync(join(dir, fileName), sql);
  return dir;
}

export function removeMigrationsDirs(): void {
  for (const dir of tempDirs.splice(0)) rmSync(dir, { recursive: true, force: true });
}
