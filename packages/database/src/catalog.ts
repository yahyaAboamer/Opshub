import { fileURLToPath } from 'node:url';

/** The only PostgreSQL major this boundary is qualified on (ADR-003, 15-technology-selection). */
export const SUPPORTED_SERVER_MAJOR = 17;

/**
 * Grant catalog, v1. Stable NOLOGIN group roles that migrations GRANT to; environment-specific LOGIN roles join them.
 * - The schema owner owns every migrated object. A migrator login is a member WITH INHERIT FALSE, SET TRUE and acts
 *   as the owner only after the runner's SET ROLE.
 * - The runtime role receives only explicit per-object grants from reviewed migrations. It and its members are never
 *   superuser, BYPASSRLS, CREATEROLE, CREATEDB or members of the schema owner.
 * Later roles (control plane, worker, queue transport, retention) extend this catalog under its lock.
 */
export const SCHEMA_OWNER_ROLE = 'opshub_schema_owner';
export const RUNTIME_ROLE = 'opshub_runtime';

/** Application schema created by migration 0001, and the runner-owned migration history schema. */
export const APP_SCHEMA = 'opshub';
export const MIGRATION_SCHEMA = 'opshub_migration';
export const MIGRATION_TABLE = 'applied_migrations';

/** Session advisory lock serializing migration runners within one database: int4 pair 'OPSH', 'MIGR'. */
export const MIGRATION_LOCK_KEY = [0x4f505348, 0x4d494752] as const;

/**
 * Target identity marker: database-level settings written by the provisioning step (ALTER DATABASE … SET), never by
 * migrations. The guard reads them from pg_db_role_setting, so a session-level SET or connection option cannot spoof them.
 */
export const IDENTITY_SETTING_ENVIRONMENT = 'opshub.environment';
export const IDENTITY_SETTING_DATABASE_ID = 'opshub.database_id';

/** The repository's reviewed, ordered migration files. */
export const REPOSITORY_MIGRATIONS_DIR = fileURLToPath(new URL('../migrations', import.meta.url));
