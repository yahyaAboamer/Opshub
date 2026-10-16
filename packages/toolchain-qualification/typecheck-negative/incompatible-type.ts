// T0002-TEST02 fixture. Intentionally ill-typed: DigestService.sha256 returns a string, not a number.
// `npm run typecheck:negative` must fail with exactly one error, TS2322 at line 6; the main typecheck excludes this folder.
import { DigestService } from '../src/server/digest.service';

// The next line is the intentional incompatible type.
export const digest: number = new DigestService().sha256(Buffer.from('synthetic'));
