// T0002-TEST02 companion: Vitest only transpiles, so the ill-typed fixture runs and this passes.
// This is why the separate typecheck is required.
import { expect, it } from 'vitest';
import { digest } from './incompatible-type';

it('runs ill-typed code because Vitest does not type-check', () => {
  expect(typeof digest).toBe('string');
});
