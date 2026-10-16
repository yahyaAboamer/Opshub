import { defineConfig } from 'vitest/config';

// Server specs run in Node; client specs opt into jsdom with a `@vitest-environment jsdom` docblock.
// fsModuleCache is off: Vitest 5 reuses cached transforms after a tsconfig change (for example dropping
// emitDecoratorMetadata), which reported stale passes during T0002 qualification.
export default defineConfig({
  test: {
    include: ['src/**/*.spec.{ts,tsx}'],
    environment: 'node',
    fsModuleCache: false,
  },
});
