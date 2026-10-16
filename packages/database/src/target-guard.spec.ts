import { randomUUID } from 'node:crypto';
import { afterAll, beforeAll, describe, expect, inject, it } from 'vitest';
import { assertTarget, migrate, type DatabaseErrorCode, type ExpectedTarget, type TargetFacts } from './index';
import {
  ddlCount,
  dropDatabase,
  expectBoundaryError,
  installDdlTripwire,
  provisionDatabase,
  schemaExists,
  withClient,
  type ProvisionedDatabase,
} from './testing';

const EXPECTED: ExpectedTarget = {
  database: 'opshub_t0003',
  environment: 'local-synthetic',
  databaseId: '6f1c2a3e-0000-4000-8000-000000000003',
};
const MATCHING: TargetFacts = {
  serverVersionNum: 170011,
  database: 'opshub_t0003',
  environment: 'local-synthetic',
  databaseId: '6f1c2a3e-0000-4000-8000-000000000003',
  sessionUser: 'opshub_t0003_migrator',
  sessionUserIsSuperuser: false,
  ownerRoleExists: true,
  runtimeRoleExists: true,
  sessionUserCanSetOwner: true,
  runtimeRolePrivileged: false,
};

const MISMATCHES: Array<[string, Partial<TargetFacts>, DatabaseErrorCode]> = [
  ['PostgreSQL 18 server', { serverVersionNum: 180000 }, 'TARGET_WRONG_SERVER_MAJOR'],
  ['PostgreSQL 16 server', { serverVersionNum: 160004 }, 'TARGET_WRONG_SERVER_MAJOR'],
  ['other database name', { database: 'opshub_production' }, 'TARGET_WRONG_DATABASE'],
  ['no environment marker', { environment: null }, 'TARGET_IDENTITY_MISSING'],
  ['no database id marker', { databaseId: null }, 'TARGET_IDENTITY_MISSING'],
  ['other environment', { environment: 'production' }, 'TARGET_WRONG_ENVIRONMENT'],
  ['other database id', { databaseId: '6f1c2a3e-0000-4000-8000-000000000099' }, 'TARGET_WRONG_DATABASE_ID'],
  ['schema owner role absent', { ownerRoleExists: false }, 'ROLE_MISSING'],
  ['runtime role absent', { runtimeRoleExists: false }, 'ROLE_MISSING'],
  ['superuser session', { sessionUserIsSuperuser: true }, 'ROLE_MIGRATOR_IS_SUPERUSER'],
  ['session cannot SET ROLE to the owner', { sessionUserCanSetOwner: false }, 'ROLE_MIGRATOR_NOT_OWNER_MEMBER'],
  ['runtime role holds owner or elevated attributes', { runtimeRolePrivileged: true }, 'ROLE_RUNTIME_PRIVILEGED'],
  ['several mismatches report the first in check order', { database: 'x', environment: 'production' }, 'TARGET_WRONG_DATABASE'],
];

describe('T0003-TEST01 target identity guard', () => {
  it('accepts facts that match the expected target', () => {
    expect(() => assertTarget(EXPECTED, MATCHING)).not.toThrow();
  });

  it('rejects each mismatch with its own error code', () => {
    for (const [label, override, code] of MISMATCHES) {
      expectBoundaryError(() => assertTarget(EXPECTED, { ...MATCHING, ...override }), code, label);
    }
    expectBoundaryError(
      () => assertTarget({ ...EXPECTED, databaseId: 'not-a-uuid' }, MATCHING),
      'TARGET_INVALID_EXPECTATION',
      'malformed expected database id',
    );
  });

  describe('against a disposable PostgreSQL 17 database', () => {
    let db: ProvisionedDatabase;
    let unmarked: ProvisionedDatabase;

    beforeAll(async () => {
      const server = inject('postgres');
      db = await provisionDatabase(server);
      unmarked = await provisionDatabase(server, { identity: null });
      await installDdlTripwire(db);
      await installDdlTripwire(unmarked);
    });
    afterAll(async () => {
      await dropDatabase(db);
      await dropDatabase(unmarked);
    });

    const expectRejectedBeforeDdl = async (target: ProvisionedDatabase, run: Promise<unknown>, code: DatabaseErrorCode) => {
      await expectBoundaryError(run, code);
      expect(await ddlCount(target)).toBe(0);
      expect(await schemaExists(target, 'opshub_migration')).toBe(false);
      expect(await schemaExists(target, 'opshub')).toBe(false);
    };

    it('rejects a wrong environment before any DDL', async () => {
      await expectRejectedBeforeDdl(
        db,
        migrate({ connection: db.migrator, expected: { ...db.expected, environment: 'staging' } }),
        'TARGET_WRONG_ENVIRONMENT',
      );
    });

    it('rejects a wrong database name before any DDL', async () => {
      await expectRejectedBeforeDdl(
        db,
        migrate({ connection: db.migrator, expected: { ...db.expected, database: 'opshub_elsewhere' } }),
        'TARGET_WRONG_DATABASE',
      );
    });

    it('rejects a wrong database id before any DDL', async () => {
      await expectRejectedBeforeDdl(
        db,
        migrate({ connection: db.migrator, expected: { ...db.expected, databaseId: randomUUID() } }),
        'TARGET_WRONG_DATABASE_ID',
      );
    });

    it('rejects a database without an identity marker before any DDL', async () => {
      await expectRejectedBeforeDdl(
        unmarked,
        migrate({ connection: unmarked.migrator, expected: { ...db.expected, database: unmarked.name } }),
        'TARGET_IDENTITY_MISSING',
      );
    });

    it('ignores a session-level identity spoof and reads the database-level marker', async () => {
      const spoof = { environment: 'staging', databaseId: randomUUID() };
      await expectRejectedBeforeDdl(
        db,
        migrate({
          connection: { ...db.migrator, options: `-c opshub.environment=${spoof.environment} -c opshub.database_id=${spoof.databaseId}` },
          expected: { ...db.expected, ...spoof },
        }),
        'TARGET_WRONG_ENVIRONMENT',
      );
    });

    it('rejects a superuser migrator before any DDL', async () => {
      await expectRejectedBeforeDdl(db, migrate({ connection: db.admin, expected: db.expected }), 'ROLE_MIGRATOR_IS_SUPERUSER');
    });

    it('rejects a runtime role that holds schema-owner membership before any DDL', async () => {
      await withClient(db.admin, (c) => c.query(`GRANT opshub_schema_owner TO "${db.runtimeLogin}"`));
      try {
        await expectRejectedBeforeDdl(db, migrate({ connection: db.migrator, expected: db.expected }), 'ROLE_RUNTIME_PRIVILEGED');
      } finally {
        await withClient(db.admin, (c) => c.query(`REVOKE opshub_schema_owner FROM "${db.runtimeLogin}"`));
      }
    });

    it('rejects a runtime login that can reach an elevated role before any DDL', async () => {
      const elevated = `${db.name}_elevated`;
      await withClient(db.admin, async (c) => {
        await c.query(`create role ${elevated} nologin bypassrls`);
        await c.query(`grant ${elevated} to "${db.runtimeLogin}"`);
      });
      try {
        await expectRejectedBeforeDdl(db, migrate({ connection: db.migrator, expected: db.expected }), 'ROLE_RUNTIME_PRIVILEGED');
      } finally {
        await withClient(db.admin, (c) => c.query(`drop role ${elevated}`));
      }
    });

    it('rejects a migrator that can reach a superuser role before any DDL', async () => {
      await withClient(db.admin, (c) => c.query(`grant "${db.server.user}" to "${db.migratorLogin}"`));
      try {
        await expectRejectedBeforeDdl(db, migrate({ connection: db.migrator, expected: db.expected }), 'ROLE_MIGRATOR_IS_SUPERUSER');
      } finally {
        await withClient(db.admin, (c) => c.query(`revoke "${db.server.user}" from "${db.migratorLogin}"`));
      }
    });

    it('positive control: the matching target migrates and trips the DDL tripwire', async () => {
      const result = await migrate({ connection: db.migrator, expected: db.expected });
      expect(result.applied.map((m) => m.version)).toEqual([1]);
      expect(await ddlCount(db)).toBeGreaterThan(0);
      expect(await schemaExists(db, 'opshub')).toBe(true);
    });
  });
});
