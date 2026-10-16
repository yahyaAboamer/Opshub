import { createHash } from 'node:crypto';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import pg from 'pg';
import { MIGRATION_LOCK_KEY, MIGRATION_SCHEMA, MIGRATION_TABLE, REPOSITORY_MIGRATIONS_DIR, SCHEMA_OWNER_ROLE } from './catalog';
import { DatabaseBoundaryError } from './errors';
import { assertTarget, readTargetFacts, type ExpectedTarget } from './target-guard';

export interface MigrationFile {
  version: number;
  name: string;
  fileName: string;
  /** SHA-256 of the file's exact bytes (the checkout is LF-only per .gitattributes). */
  sha256: string;
  sql: string;
}

export interface AppliedMigration {
  version: number;
  name: string;
  sha256: string;
}

export interface MigrationRunResult {
  /** Migrations this run applied, in order. */
  applied: AppliedMigration[];
  /** Migrations already recorded in history before this run. */
  alreadyApplied: number;
}

export interface MigrateOptions {
  /** Migrator LOGIN role: not superuser, member of the schema owner WITH SET TRUE. */
  connection: pg.ClientConfig;
  expected: ExpectedTarget;
  /** Defaults to the repository's reviewed migrations. */
  migrationsDir?: string;
  /** Maximum wait for another runner's migration lock. Default 30 s. */
  lockTimeoutMs?: number;
}

/** NNNN_slug.sql: four-digit version, lowercase snake_case slug. There are no down migrations. */
const FILE_NAME = /^(\d{4})_([a-z0-9]+(?:_[a-z0-9]+)*)\.sql$/;
const HISTORY = `${MIGRATION_SCHEMA}.${MIGRATION_TABLE}`;

const hasStatement = (sql: string) =>
  sql
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/--[^\n]*/g, '')
    .trim().length > 0;

/** Loads and validates a migrations directory: every entry is a NNNN_slug.sql file, versions run 1..N without gaps. */
export async function loadMigrations(dir: string): Promise<MigrationFile[]> {
  const entries = (await readdir(dir, { withFileTypes: true })).sort((a, b) => a.name.localeCompare(b.name));
  const files: MigrationFile[] = [];
  for (const entry of entries) {
    const match = FILE_NAME.exec(entry.name);
    if (!entry.isFile() || !match) {
      throw new DatabaseBoundaryError('MIGRATION_BAD_FILENAME', `${entry.name} is not a NNNN_slug.sql migration file`, {
        fileName: entry.name,
      });
    }
    const bytes = await readFile(join(dir, entry.name));
    const sql = bytes.toString('utf8');
    if (!hasStatement(sql)) {
      throw new DatabaseBoundaryError('MIGRATION_EMPTY', `${entry.name} contains no statement`, { fileName: entry.name });
    }
    files.push({
      version: Number(match[1]),
      name: match[2] as string,
      fileName: entry.name,
      sha256: createHash('sha256').update(bytes).digest('hex'),
      sql,
    });
  }
  files.sort((a, b) => a.version - b.version);
  files.forEach((file, index) => {
    if (index > 0 && files[index - 1]?.version === file.version) {
      throw new DatabaseBoundaryError('MIGRATION_DUPLICATE_VERSION', `version ${file.version} appears more than once`, {
        version: file.version,
      });
    }
    if (file.version !== index + 1) {
      throw new DatabaseBoundaryError('MIGRATION_SEQUENCE_GAP', `expected version ${index + 1}, found ${file.version}`, {
        expected: index + 1,
        found: file.version,
      });
    }
  });
  return files;
}

async function acquireMigrationLock(client: pg.Client, timeoutMs: number) {
  if (!Number.isInteger(timeoutMs) || timeoutMs <= 0) throw new RangeError('lockTimeoutMs must be a positive integer');
  await client.query(`set lock_timeout = ${timeoutMs}`);
  try {
    await client.query('select pg_advisory_lock($1, $2)', [...MIGRATION_LOCK_KEY]);
  } catch (error) {
    if ((error as { code?: string }).code === '55P03') {
      throw new DatabaseBoundaryError('MIGRATION_LOCK_TIMEOUT', 'another migration runner holds the migration lock', { timeoutMs }, error);
    }
    throw error;
  } finally {
    await client.query('reset lock_timeout');
  }
}

/** Creates the history table on first use only, so a run with nothing pending issues no DDL. */
async function ensureHistory(client: pg.Client) {
  const { rows } = await client.query('select to_regclass($1) is not null as present', [HISTORY]);
  if (rows[0].present) return;
  await client.query('begin');
  try {
    await client.query(`create schema if not exists ${MIGRATION_SCHEMA}`);
    await client.query(`revoke all on schema ${MIGRATION_SCHEMA} from public`);
    await client.query(`create table ${HISTORY} (
      version integer primary key check (version > 0),
      name text not null check (name ~ '^[a-z0-9]+(_[a-z0-9]+)*$'),
      sha256 char(64) not null check (sha256 ~ '^[0-9a-f]{64}$'),
      applied_at timestamptz not null default now(),
      applied_by text not null default session_user
    )`);
    await client.query(`revoke all on ${HISTORY} from public`);
    await client.query('commit');
  } catch (error) {
    await client.query('rollback');
    throw error;
  }
}

/** Applied history must be exactly the files' prefix: same versions, names and bytes. */
function verifyHistory(files: MigrationFile[], applied: AppliedMigration[]) {
  applied.forEach((row, index) => {
    const file = files[index];
    if (row.version !== index + 1 || file === undefined) {
      throw new DatabaseBoundaryError('MIGRATION_UNKNOWN_APPLIED', `history records version ${row.version} with no matching file`, {
        version: row.version,
      });
    }
    if (row.name !== file.name) {
      throw new DatabaseBoundaryError('MIGRATION_NAME_MISMATCH', `applied version ${row.version} was named ${row.name}`, {
        version: row.version,
        applied: row.name,
        file: file.name,
      });
    }
    if (row.sha256 !== file.sha256) {
      throw new DatabaseBoundaryError('MIGRATION_CHECKSUM_MISMATCH', `applied ${file.fileName} has changed; add a new migration instead`, {
        version: row.version,
        applied: row.sha256,
        file: file.sha256,
      });
    }
  });
}

const currentXid = async (client: pg.Client) => (await client.query('select pg_current_xact_id()::text as xid')).rows[0].xid as string;

/** One migration, one transaction: its statements and its history row commit together or not at all. */
async function applyMigration(client: pg.Client, file: MigrationFile) {
  await client.query('begin');
  try {
    const xid = await currentXid(client);
    try {
      await client.query(file.sql);
    } catch (error) {
      throw new DatabaseBoundaryError(
        'MIGRATION_FAILED',
        `${file.fileName} failed and was rolled back`,
        { version: file.version, name: file.name, sqlState: (error as { code?: string }).code ?? null },
        error,
      );
    }
    if ((await currentXid(client)) !== xid) {
      throw new DatabaseBoundaryError(
        'MIGRATION_TRANSACTION_ESCAPED',
        `${file.fileName} ended the runner's transaction; migrations must not contain transaction control`,
        { version: file.version, name: file.name },
      );
    }
    await client.query(`insert into ${HISTORY} (version, name, sha256) values ($1, $2, $3)`, [file.version, file.name, file.sha256]);
    await client.query('commit');
  } catch (error) {
    await client.query('rollback');
    throw error;
  }
}

/**
 * Applies pending migrations in order. Sequence: validate files, guard the target (read-only), take the migration
 * advisory lock, SET ROLE to the schema owner, verify history, apply each pending file in its own transaction.
 * A failure stops the run with earlier migrations committed; repair is always forward (fix the unapplied file or add a
 * new one), never a down migration or an edit to an applied file.
 */
export async function migrate(options: MigrateOptions): Promise<MigrationRunResult> {
  const files = await loadMigrations(options.migrationsDir ?? REPOSITORY_MIGRATIONS_DIR);
  const client = new pg.Client({ application_name: 'opshub-migrator', ...options.connection });
  await client.connect();
  try {
    assertTarget(options.expected, await readTargetFacts(client));
    await acquireMigrationLock(client, options.lockTimeoutMs ?? 30_000);
    // The session advisory lock is released when the connection closes below, including after any failure.
    await client.query(`set role ${SCHEMA_OWNER_ROLE}`);
    // Empty search_path: a connection option cannot redirect names, and every migrated object must be schema-qualified.
    await client.query(`set search_path = ''`);
    await ensureHistory(client);
    const { rows } = await client.query<AppliedMigration>(`select version, name, sha256 from ${HISTORY} order by version`);
    verifyHistory(files, rows);
    const applied: AppliedMigration[] = [];
    for (const file of files.slice(rows.length)) {
      await applyMigration(client, file);
      applied.push({ version: file.version, name: file.name, sha256: file.sha256 });
    }
    return { applied, alreadyApplied: rows.length };
  } finally {
    await client.end();
  }
}
