import type { TestProject } from 'vitest/node';
import { startDisposablePostgres, type DisposableServer } from './disposable-postgres';
import { provisionClusterRoles } from './provision';

declare module 'vitest' {
  export interface ProvidedContext {
    postgres: DisposableServer;
  }
}

/** One disposable PostgreSQL 17 container per Vitest run, with the grant catalog's group roles; removed at teardown. */
export default async function setup(project: TestProject) {
  const { server, stop } = await startDisposablePostgres();
  try {
    await provisionClusterRoles(server);
  } catch (error) {
    await stop();
    throw error;
  }
  project.provide('postgres', server);
  return stop;
}
