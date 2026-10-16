import { defineConfig } from 'vitest/config';

// T0002-TEST02 companion: runs the intentionally ill-typed fixture to show Vitest transpiles without type-checking.
export default defineConfig({
  test: {
    include: ['typecheck-negative/**/*.spec.ts'],
    environment: 'node',
    fsModuleCache: false,
  },
});
