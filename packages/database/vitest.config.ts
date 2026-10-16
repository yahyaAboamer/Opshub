import { defineConfig } from 'vitest/config';

// One disposable PostgreSQL 17 container per run (globalSetup); each spec provisions its own databases.
// Files run serially because the group roles opshub_schema_owner/opshub_runtime are cluster-wide and some
// specs change role memberships to prove the guard. fsModuleCache is off per C-T0002-v1.
export default defineConfig({
  test: {
    include: ['src/**/*.spec.ts'],
    environment: 'node',
    globalSetup: ['src/testing/global-setup.ts'],
    fileParallelism: false,
    testTimeout: 60_000,
    hookTimeout: 180_000,
    fsModuleCache: false,
  },
});
