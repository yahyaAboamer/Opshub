// T0003 — PostgreSQL 17, Kysely and explicit migration qualification. Node 24's built-in runner drives the
// isolated package's pinned binaries against a disposable Testcontainers PostgreSQL 17 (Docker must be running).
// Prepare: npm ci --prefix packages/database
// Run:     node --test "tests/tasks/T0003/*.test.mjs"
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, readdirSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const ROOT = execFileSync('git', ['-C', import.meta.dirname, 'rev-parse', '--show-toplevel'], { encoding: 'utf8' }).trim();
const PKG = join(ROOT, 'packages/database');
const readJson = (path) => JSON.parse(readFileSync(path, 'utf8'));
const manifest = readJson(join(PKG, 'package.json'));

const BIN = { tsc: 'node_modules/typescript/bin/tsc', vitest: 'node_modules/vitest/vitest.mjs' };
const run = (bin, ...args) => {
  const binPath = join(PKG, BIN[bin]);
  assert.ok(existsSync(binPath), `${bin} not installed: run npm ci --prefix packages/database`);
  return spawnSync(process.execPath, [binPath, ...args], {
    cwd: PKG,
    encoding: 'utf8',
    maxBuffer: 64 * 1024 * 1024,
    env: { ...process.env, NO_COLOR: '1', FORCE_COLOR: '0', CI: '1' },
  });
};
const output = (r) => `${r.stdout}\n${r.stderr}`;

// The qualified database stack. Every entry is pinned exactly; nothing else is a direct dependency.
// typescript, vite, vitest and @types/node reuse the C-T0002-v1 pins.
const PINS = {
  kysely: '0.29.6',
  pg: '8.23.1',
  '@testcontainers/postgresql': '12.2.1',
  '@types/node': '24.19.2',
  '@types/pg': '8.23.1',
  typescript: '7.0.2',
  vite: '8.3.4',
  vitest: '5.0.5',
};
const POSTGRES_IMAGE = 'postgres:17.11-trixie@sha256:2d2b8998d31037bf721cfdf764d76ba74171b4fab3431b7f72c27c56ddbdf9e3';

test('T0003 pins: Node 24, exact direct versions, lockfile and installed tree agree', () => {
  assert.equal(process.versions.node.split('.')[0], '24', `Node ${process.versions.node} is not Node 24`);
  assert.equal(manifest.engines?.node, '>=24 <25');
  const pins = { ...manifest.dependencies, ...manifest.devDependencies };
  assert.deepEqual(pins, PINS, 'direct dependencies differ from the qualified stack');
  assert.deepEqual(Object.keys(manifest.dependencies).sort(), ['kysely', 'pg'], 'runtime dependencies must be kysely and pg only');

  const lockPath = join(PKG, 'package-lock.json');
  assert.ok(existsSync(lockPath), 'package-lock.json missing');
  const lock = readJson(lockPath);
  assert.equal(lock.lockfileVersion, 3);
  assert.deepEqual(lock.packages[''].dependencies, manifest.dependencies, 'lockfile root dependencies drifted');
  assert.deepEqual(lock.packages[''].devDependencies, manifest.devDependencies, 'lockfile root devDependencies drifted');
  for (const [path, entry] of Object.entries(lock.packages)) {
    if (path === '' || entry.link) continue;
    assert.match(entry.resolved ?? '', /^https:\/\/registry\.npmjs\.org\//, `${path} is not resolved from registry.npmjs.org`);
  }
  for (const [name, version] of Object.entries(PINS)) {
    assert.equal(lock.packages[`node_modules/${name}`]?.version, version, `lockfile resolves ${name} differently`);
    const installed = join(PKG, 'node_modules', name, 'package.json');
    assert.ok(existsSync(installed), `${name} not installed: run npm ci --prefix packages/database`);
    assert.equal(readJson(installed).version, version, `installed ${name} differs from the pin`);
  }
  const disposable = readFileSync(join(PKG, 'src/testing/disposable-postgres.ts'), 'utf8');
  assert.ok(disposable.includes(`'${POSTGRES_IMAGE}'`), 'disposable PostgreSQL image is not the digest-pinned 17.11 image');
});

test('T0003 migration allocation: only the reviewed 0001 file, LF-only, no down migration', () => {
  const dir = join(PKG, 'migrations');
  assert.deepEqual(readdirSync(dir), ['0001_opshub_schema_baseline.sql'], 'unexpected migration allocation');
  const sql = readFileSync(join(dir, '0001_opshub_schema_baseline.sql'), 'utf8');
  assert.ok(!sql.includes('\r'), 'migration file contains CR; its checksum would differ by checkout');
  assert.doesNotMatch(sql, /\bcreate\s+table\b/i, '0001 must not create tenant or domain tables');
});

test('T0003 typecheck: tsc reports 0 errors with skipLibCheck false', () => {
  const r = run('tsc', '-p', 'tsconfig.json', '--noEmit');
  assert.equal(r.status, 0, `main typecheck failed:\n${output(r)}`);
});

let vitestStatus;
const vitestResults = () => {
  if (vitestStatus) return vitestStatus;
  const docker = spawnSync('docker', ['info', '--format', '{{.ServerVersion}}'], { encoding: 'utf8' });
  assert.equal(docker.status, 0, `Docker engine not reachable (start Docker Desktop):\n${output(docker)}`);
  const dir = mkdtempSync(join(tmpdir(), 't0003-vitest-'));
  try {
    const report = join(dir, 'report.json');
    const r = run('vitest', 'run', '--reporter=json', `--outputFile=${report}`);
    assert.ok(existsSync(report), `vitest produced no report:\n${output(r)}`);
    const results = readJson(report).testResults.flatMap((f) => f.assertionResults);
    vitestStatus = { exit: r.status, log: output(r), status: Object.fromEntries(results.map((a) => [a.fullName, a.status])) };
    return vitestStatus;
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
};
const expectPassed = (prefix, names) => {
  const { exit, log, status } = vitestResults();
  const group = Object.fromEntries(Object.entries(status).filter(([name]) => name.startsWith(prefix)));
  assert.deepEqual(group, Object.fromEntries(names.map((n) => [`${prefix} ${n}`, 'passed'])), `vitest results:\n${log}`);
  assert.equal(exit, 0, `vitest failed:\n${log}`);
};

test('T0003-TEST01: wrong database/environment rejected before DDL', () => {
  expectPassed('T0003-TEST01 target identity guard', [
    'accepts facts that match the expected target',
    'rejects each mismatch with its own error code',
    'against a disposable PostgreSQL 17 database rejects a wrong environment before any DDL',
    'against a disposable PostgreSQL 17 database rejects a wrong database name before any DDL',
    'against a disposable PostgreSQL 17 database rejects a wrong database id before any DDL',
    'against a disposable PostgreSQL 17 database rejects a database without an identity marker before any DDL',
    'against a disposable PostgreSQL 17 database ignores a session-level identity spoof and reads the database-level marker',
    'against a disposable PostgreSQL 17 database rejects a superuser migrator before any DDL',
    'against a disposable PostgreSQL 17 database rejects a runtime role that holds schema-owner membership before any DDL',
    'against a disposable PostgreSQL 17 database rejects a runtime login that can reach an elevated role before any DDL',
    'against a disposable PostgreSQL 17 database rejects a migrator that can reach a superuser role before any DDL',
    'against a disposable PostgreSQL 17 database positive control: the matching target migrates and trips the DDL tripwire',
  ]);
});

test('T0003-TEST02: clean apply and second no-op with concurrent migration lock', () => {
  expectPassed('T0003-TEST02 serialized ordered SQL migrations', [
    'applies the repository migrations to a clean database',
    'second run is a no-op that issues no DDL',
    'concurrent runners serialize on the advisory lock and apply each migration exactly once',
    'gives up with MIGRATION_LOCK_TIMEOUT while another runner holds the lock',
  ]);
});

test('T0003-TEST03: rollback a Kysely unit of work and verify no persisted rows', () => {
  expectPassed('T0003-TEST03 Kysely unit of work', [
    'commits a successful unit of work',
    'rolls back a unit of work that throws and persists no rows',
    'rolls back a unit of work that hits a constraint violation and persists no rows',
  ]);
});

test('T0003 protocol: ordering, immutability, forward repair, and owner versus runtime roles', () => {
  expectPassed('T0003 migration protocol', [
    'loadMigrations accepts only contiguous NNNN_slug.sql files',
    'refuses an applied migration whose file changed',
    'refuses history that is ahead of the migration files',
    'a failed migration rolls back completely and is repaired forward',
    'pins search_path so a connection option cannot redirect unqualified names',
    'detects a migration that escapes its transaction',
  ]);
  expectPassed('T0003 schema owner versus runtime role', [
    'runtime role can use the app schema but cannot create objects or read migration history',
    'the migrator login has no owner privileges until it sets the owner role',
  ]);
  const { status } = vitestResults();
  assert.equal(Object.keys(status).length, 27, 'unexpected number of vitest tests');
});
