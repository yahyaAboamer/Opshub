// T0001 — versioned workspace boundary checks. Node 24 built-in test runner and git only; no dependencies.
// Run: npm run test:t0001   (optionally OPSHUB_CUSTODY_ROOT=<primary workspace> to check private originals)
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync, mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const git = (cwd, ...args) => execFileSync('git', ['-C', cwd, ...args], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
const ROOT = git(import.meta.dirname, 'rev-parse', '--show-toplevel').trim();
const readJson = (base, path) => JSON.parse(readFileSync(join(base, path), 'utf8'));
const sha256 = (buf) => createHash('sha256').update(buf).digest('hex');
const lfSha256 = (buf) => sha256(Buffer.from(buf.toString('latin1').replaceAll('\r\n', '\n'), 'latin1'));

const inventory = readJson(ROOT, 'docs/development/workspace-inventory.json');
const baseline = readJson(ROOT, inventory.baseline.path);
const approval = readJson(ROOT, 'evidence/implementation/phase6-owner-approval.json');
const amended = new Map(approval.authorized_protected_amendments.map((a) => [a.path, a]));
const privateRules = inventory.private_custody_rules.map((r) => new RegExp(r.regex));
const isPrivate = (p) => privateRules.some((rx) => rx.test(p));
const SECRET = [/(^|\/)\.env(\.(?!example$)[^/]*)?$/, /\.(pem|key|p12|pfx|keystore|jks)$/i, /(^|\/)id_(rsa|ed25519|ecdsa)(\.pub)?$/, /(^|\/)\.npmrc$/, /(^|\/)secrets?\//i, /\.pyc$/];
const isSecretOrGenerated = (p) => SECRET.some((rx) => rx.test(p));
const isTrackablePath = (p) =>
  inventory.trackable_root_files.includes(p) || inventory.trackable_root_dirs.some((d) => p.startsWith(d));
const matchesBaseline = (record, buf) =>
  sha256(buf) === record.sha256 || (amended.has(record.path) && lfSha256(buf) === amended.get(record.path).amended_sha256_lf);

test('T0001 inventory classifies every protected file exactly once, with baseline digests', () => {
  assert.equal(sha256(readFileSync(join(ROOT, inventory.baseline.path))), inventory.baseline.sha256, 'baseline file drift');
  const byPath = new Map(baseline.protected_files.map((r) => [r.path, r.sha256]));
  const listed = [...inventory.private_custody, ...inventory.excluded_generated];
  assert.equal(new Set(listed.map((x) => x.path)).size, listed.length, 'duplicate custody entry');
  for (const x of listed) assert.equal(x.sha256, byPath.get(x.path), `custody digest differs from baseline: ${x.path}`);
  for (const x of inventory.private_custody) assert.ok(isPrivate(x.path), `custody entry outside the approved rules: ${x.path}`);
  const c = inventory.counts;
  assert.equal(c.protected_trackable + c.private_custody + c.excluded_generated, baseline.protected_files.length);
  assert.equal(c.private_custody, inventory.private_custody.length);
});

test('T0001-TEST01a: protected originals in custody are unchanged on disk', (t) => {
  const custodyRoot = process.env.OPSHUB_CUSTODY_ROOT || ROOT;
  const missing = baseline.protected_files.filter((r) => !existsSync(join(custodyRoot, r.path)));
  if (missing.length) {
    t.skip(`NOT_CHECKED: ${missing.length} protected files are not present under ${custodyRoot}; set OPSHUB_CUSTODY_ROOT to the primary workspace`);
    return;
  }
  const drift = baseline.protected_files.filter((r) => !matchesBaseline(r, readFileSync(join(custodyRoot, r.path))));
  assert.deepEqual(drift.map((r) => r.path), [], 'protected original changed');
});

test('T0001-TEST01b: a fresh clone holds only the approved trackable inventory, byte-exact', (t) => {
  const branch = git(ROOT, 'rev-parse', '--abbrev-ref', 'HEAD').trim();
  const dir = mkdtempSync(join(tmpdir(), 't0001-clone-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  const clone = join(dir, 'repo');
  execFileSync('git', ['clone', '--quiet', '--no-local', ...(branch === 'HEAD' ? [] : ['--branch', branch]), ROOT, clone]);

  const tracked = git(clone, 'ls-files', '-z').split('\0').filter(Boolean);
  assert.deepEqual(tracked.filter((p) => !isTrackablePath(p)), [], 'tracked file outside approved trackable roots');
  assert.deepEqual(tracked.filter(isPrivate), [], 'private-custody file tracked');
  assert.deepEqual(tracked.filter(isSecretOrGenerated), [], 'secret-like or generated file tracked');

  const historyPaths = git(clone, 'rev-list', '--objects', '--all').split('\n').map((l) => l.slice(41)).filter(Boolean);
  assert.deepEqual([...new Set(historyPaths.filter((p) => isPrivate(p) || p.endsWith('.pyc')))], [], 'private or generated path present in history');

  const custody = new Set([...inventory.private_custody, ...inventory.excluded_generated].map((x) => x.path));
  const notExact = [];
  for (const r of baseline.protected_files) {
    const p = join(clone, r.path);
    if (custody.has(r.path)) assert.ok(!existsSync(p), `custody file present in clone: ${r.path}`);
    else if (!existsSync(p) || !matchesBaseline(r, readFileSync(p))) notExact.push(r.path);
  }
  assert.deepEqual(notExact, [], 'trackable protected file missing or not byte-identical to baseline in clone');
});

test('T0001-TEST02: ignore rules reject secret/private paths and keep synthetic fixtures', () => {
  const ignored = (p) => {
    try { execFileSync('git', ['-C', ROOT, 'check-ignore', '-q', '--no-index', p]); return true; }
    catch (e) { if (e.status === 1) return false; throw e; }
  };
  const mustIgnore = [
    '.env', '.env.local', 'apps/api/.env.production', '.npmrc', 'ops/keys/deploy.pem', 'server.key', 'certs/client.p12',
    'id_rsa', 'secrets/provider.json', 'tests/fixtures/private/real-orders.json', 'tests/fixtures/shared/customer.private.json',
    'source/new-workbook.xlsx', 'source/reports/x.md', 'evidence/artifacts/text/new_sop.extracted.txt',
    'evidence/artifacts/text/new_sop.blocks.json', 'evidence/artifacts/text/review-page-9.png',
    'evidence/live/phase1b/assets/abc.js', 'evidence/implementation/__pycache__/x.cpython-314.pyc',
    'node_modules/x/index.js', 'apps/web/dist/index.html', 'coverage/lcov.info', 'playwright-report/index.html', 'test-results/a.png',
  ];
  const mustKeep = [
    '.env.example', 'apps/api/.env.example', 'tests/fixtures/shared/merchant-ma.json', 'tests/fixtures/synthetic/orders.json',
    'tests/tasks/T0001/workspace-boundary.test.mjs', 'docs/development/workspace-boundary.md',
    'evidence/artifacts/text/nonworkbook-analysis.md', 'evidence/live/phase1b/static-analysis.md', 'apps/web/src/main.tsx',
    'package.json', 'package-lock.json',
  ];
  assert.deepEqual(mustIgnore.filter((p) => !ignored(p)), [], 'secret/private path not ignored');
  assert.deepEqual(mustKeep.filter(ignored), [], 'approved trackable path wrongly ignored');
});
