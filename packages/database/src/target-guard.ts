import type pg from 'pg';
import {
  IDENTITY_SETTING_DATABASE_ID,
  IDENTITY_SETTING_ENVIRONMENT,
  RUNTIME_ROLE,
  SCHEMA_OWNER_ROLE,
  SUPPORTED_SERVER_MAJOR,
} from './catalog';
import { DatabaseBoundaryError } from './errors';

/** What the caller (migration job configuration) asserts about the database it intends to change. */
export interface ExpectedTarget {
  /** Exact current_database() name. */
  database: string;
  /** Environment label, e.g. 'local-synthetic', 'ci-synthetic', 'staging', 'production'. */
  environment: string;
  /** UUID assigned to this database at provisioning time. */
  databaseId: string;
}

/** What the connected server reports. Read in one read-only transaction; see readTargetFacts. */
export interface TargetFacts {
  serverVersionNum: number;
  database: string;
  environment: string | null;
  databaseId: string | null;
  sessionUser: string;
  /** session_user is a superuser or can reach a superuser role through membership. */
  sessionUserIsSuperuser: boolean;
  ownerRoleExists: boolean;
  runtimeRoleExists: boolean;
  /** session_user may SET ROLE to the schema owner. */
  sessionUserCanSetOwner: boolean;
  /** The runtime role or any (transitive) member can reach an elevated role or the schema owner. */
  runtimeRolePrivileged: boolean;
}

const ENVIRONMENT = /^[a-z][a-z0-9-]{0,62}$/;
const DATABASE = /^[a-z_][a-z0-9_$]{0,62}$/;
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/;

// Membership is followed in both directions. Downward: every login that is (transitively) a member of the runtime
// role. Upward: every role those logins, and the session user, can reach, since any reachable role can be assumed
// with SET ROLE. Elevated means superuser, BYPASSRLS, CREATEROLE, CREATEDB, a server file/program role, or (for
// runtime) the schema owner.
const FACTS_SQL = `
with recursive
  owner_role as (select to_regrole($1) as oid),
  runtime_role as (select to_regrole($2) as oid),
  runtime_members(oid) as (
    select oid from runtime_role where oid is not null
    union
    select m.member from pg_auth_members m join runtime_members r on m.roleid = r.oid
  ),
  runtime_reach(oid) as (
    select oid from runtime_members
    union
    select m.roleid from pg_auth_members m join runtime_reach r on m.member = r.oid
  ),
  session_reach(oid) as (
    select oid from pg_roles where rolname = session_user
    union
    select m.roleid from pg_auth_members m join session_reach s on m.member = s.oid
  ),
  elevated(oid) as (
    select oid from pg_roles
    where rolsuper or rolbypassrls or rolcreaterole or rolcreatedb
       or rolname in ('pg_execute_server_program', 'pg_read_server_files', 'pg_write_server_files')
  )
select
  current_setting('server_version_num')::int as server_version_num,
  current_database() as database,
  session_user::text as session_user,
  exists (select 1 from session_reach s join pg_roles r on r.oid = s.oid where r.rolsuper) as session_user_is_superuser,
  coalesce((select setconfig from pg_db_role_setting
            where setrole = 0 and setdatabase = (select oid from pg_database where datname = current_database())),
           '{}'::text[]) as database_settings,
  (select oid is not null from owner_role) as owner_role_exists,
  (select oid is not null from runtime_role) as runtime_role_exists,
  coalesce((select pg_has_role(session_user, oid, 'SET') from owner_role where oid is not null), false)
    as session_user_can_set_owner,
  exists (
    select 1 from runtime_reach rr
    where rr.oid in (select oid from elevated) or rr.oid = (select oid from owner_role)
  ) as runtime_role_privileged`;

const setting = (settings: string[], name: string): string | null => {
  const prefix = `${name}=`;
  const entry = settings.find((s) => s.startsWith(prefix));
  return entry === undefined ? null : entry.slice(prefix.length);
};

/**
 * Reads the target facts inside a READ ONLY transaction, so the guard itself cannot change the database.
 * Identity comes from the database-level settings catalog, not current_setting(): session SETs and connection
 * options cannot override it.
 */
export async function readTargetFacts(client: pg.ClientBase): Promise<TargetFacts> {
  await client.query('begin transaction read only');
  try {
    const { rows } = await client.query(FACTS_SQL, [SCHEMA_OWNER_ROLE, RUNTIME_ROLE]);
    const row = rows[0];
    const settings: string[] = row.database_settings;
    return {
      serverVersionNum: row.server_version_num,
      database: row.database,
      environment: setting(settings, IDENTITY_SETTING_ENVIRONMENT),
      databaseId: setting(settings, IDENTITY_SETTING_DATABASE_ID),
      sessionUser: row.session_user,
      sessionUserIsSuperuser: row.session_user_is_superuser,
      ownerRoleExists: row.owner_role_exists,
      runtimeRoleExists: row.runtime_role_exists,
      sessionUserCanSetOwner: row.session_user_can_set_owner,
      runtimeRolePrivileged: row.runtime_role_privileged,
    };
  } finally {
    await client.query('commit');
  }
}

/** Pure check. Throws the first violation in this fixed order; returns only when every check passes. */
export function assertTarget(expected: ExpectedTarget, facts: TargetFacts): void {
  if (!DATABASE.test(expected.database) || !ENVIRONMENT.test(expected.environment) || !UUID.test(expected.databaseId)) {
    throw new DatabaseBoundaryError('TARGET_INVALID_EXPECTATION', 'expected database, environment or database id is malformed');
  }
  const major = Math.floor(facts.serverVersionNum / 10_000);
  if (major !== SUPPORTED_SERVER_MAJOR) {
    throw new DatabaseBoundaryError('TARGET_WRONG_SERVER_MAJOR', `server major ${major} is not ${SUPPORTED_SERVER_MAJOR}`, {
      serverVersionNum: facts.serverVersionNum,
    });
  }
  if (facts.database !== expected.database) {
    throw new DatabaseBoundaryError('TARGET_WRONG_DATABASE', 'connected database is not the expected database', {
      expected: expected.database,
      actual: facts.database,
    });
  }
  if (facts.environment === null || facts.databaseId === null) {
    throw new DatabaseBoundaryError('TARGET_IDENTITY_MISSING', 'database has no provisioned identity marker', {
      database: facts.database,
      environmentPresent: facts.environment !== null,
      databaseIdPresent: facts.databaseId !== null,
    });
  }
  if (facts.environment !== expected.environment) {
    throw new DatabaseBoundaryError('TARGET_WRONG_ENVIRONMENT', 'database belongs to another environment', {
      expected: expected.environment,
      actual: facts.environment,
    });
  }
  if (facts.databaseId !== expected.databaseId) {
    throw new DatabaseBoundaryError('TARGET_WRONG_DATABASE_ID', 'database identity differs from the expected database id', {
      expected: expected.databaseId,
      actual: facts.databaseId,
    });
  }
  if (!facts.ownerRoleExists || !facts.runtimeRoleExists) {
    throw new DatabaseBoundaryError('ROLE_MISSING', 'schema owner or runtime group role is not provisioned', {
      ownerRoleExists: facts.ownerRoleExists,
      runtimeRoleExists: facts.runtimeRoleExists,
    });
  }
  if (facts.sessionUserIsSuperuser) {
    throw new DatabaseBoundaryError('ROLE_MIGRATOR_IS_SUPERUSER', 'migrations must not run as a superuser', {
      sessionUser: facts.sessionUser,
    });
  }
  if (!facts.sessionUserCanSetOwner) {
    throw new DatabaseBoundaryError('ROLE_MIGRATOR_NOT_OWNER_MEMBER', `session user cannot SET ROLE ${SCHEMA_OWNER_ROLE}`, {
      sessionUser: facts.sessionUser,
    });
  }
  if (facts.runtimeRolePrivileged) {
    throw new DatabaseBoundaryError(
      'ROLE_RUNTIME_PRIVILEGED',
      `${RUNTIME_ROLE} or a member holds schema-owner membership or an elevated role attribute`,
    );
  }
}
