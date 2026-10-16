export type DatabaseErrorCode =
  // Target-database identity guard (checked in a read-only transaction before any DDL).
  | 'TARGET_INVALID_EXPECTATION'
  | 'TARGET_WRONG_SERVER_MAJOR'
  | 'TARGET_WRONG_DATABASE'
  | 'TARGET_IDENTITY_MISSING'
  | 'TARGET_WRONG_ENVIRONMENT'
  | 'TARGET_WRONG_DATABASE_ID'
  // Schema owner versus runtime role separation.
  | 'ROLE_MISSING'
  | 'ROLE_MIGRATOR_IS_SUPERUSER'
  | 'ROLE_MIGRATOR_NOT_OWNER_MEMBER'
  | 'ROLE_RUNTIME_PRIVILEGED'
  // Migration files and history.
  | 'MIGRATION_BAD_FILENAME'
  | 'MIGRATION_DUPLICATE_VERSION'
  | 'MIGRATION_SEQUENCE_GAP'
  | 'MIGRATION_EMPTY'
  | 'MIGRATION_CHECKSUM_MISMATCH'
  | 'MIGRATION_NAME_MISMATCH'
  | 'MIGRATION_UNKNOWN_APPLIED'
  // Migration execution.
  | 'MIGRATION_LOCK_TIMEOUT'
  | 'MIGRATION_FAILED'
  | 'MIGRATION_TRANSACTION_ESCAPED';

/**
 * Detail carries identifiers, versions and SQLSTATEs only: never credentials, connection strings or row data.
 * A server error message can quote row values, so it stays on `cause` and is not copied into the detail.
 */
export type ErrorDetail = Record<string, string | number | boolean | null>;

export class DatabaseBoundaryError extends Error {
  override readonly name = 'DatabaseBoundaryError';

  constructor(
    readonly code: DatabaseErrorCode,
    message: string,
    readonly detail: ErrorDetail = {},
    cause?: unknown,
  ) {
    super(`${code}: ${message}`, cause === undefined ? undefined : { cause });
  }
}
