import { Kysely, PostgresDialect, type Transaction } from 'kysely';
import pg from 'pg';

/**
 * Runtime query builder over a pg pool. Connect as a runtime LOGIN role (member of opshub_runtime), never the
 * migrator or a superuser. DB is the consuming module's typed table interface; this boundary defines none.
 */
export function createRuntimeDb<DB>(config: pg.PoolConfig): Kysely<DB> {
  return new Kysely<DB>({
    dialect: new PostgresDialect({ pool: new pg.Pool({ application_name: 'opshub-runtime', ...config }) }),
  });
}

/**
 * One unit of work = one database transaction. Commits when `work` resolves; rolls back and rethrows the original
 * error when it rejects, so nothing it wrote persists. Never perform provider or object-store I/O inside `work`
 * (04-data-architecture: no external I/O while holding a database transaction).
 */
export function withUnitOfWork<DB, T>(db: Kysely<DB>, work: (trx: Transaction<DB>) => Promise<T>): Promise<T> {
  return db.transaction().execute(work);
}
