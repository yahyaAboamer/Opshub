import { randomBytes } from 'node:crypto';
import { PostgreSqlContainer } from '@testcontainers/postgresql';

/** Official PostgreSQL 17.11 (Debian trixie) image, pinned by its multi-arch index digest. */
export const POSTGRES_IMAGE = 'postgres:17.11-trixie@sha256:2d2b8998d31037bf721cfdf764d76ba74171b4fab3431b7f72c27c56ddbdf9e3';

/** Superuser access to a disposable server. Test-only: the password is random per run and never logged. */
export interface DisposableServer {
  host: string;
  port: number;
  user: string;
  password: string;
  image: string;
}

/** Starts a throwaway PostgreSQL 17 container on an ephemeral localhost port (Docker required). */
export async function startDisposablePostgres(): Promise<{ server: DisposableServer; stop: () => Promise<void> }> {
  const user = 'opshub_admin';
  const password = randomBytes(18).toString('hex');
  const container = await new PostgreSqlContainer(POSTGRES_IMAGE)
    .withUsername(user)
    .withPassword(password)
    .withDatabase('postgres')
    .start();
  return {
    server: { host: container.getHost(), port: container.getPort(), user, password, image: POSTGRES_IMAGE },
    stop: async () => {
      await container.stop();
    },
  };
}
