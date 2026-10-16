// T0002 — toolchain qualification. Node 24 built-in test runner drives the isolated package's pinned binaries.
// Prepare: npm ci --prefix packages/toolchain-qualification
// Run:     node --test "tests/tasks/T0002/*.test.mjs"
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const ROOT = execFileSync('git', ['-C', import.meta.dirname, 'rev-parse', '--show-toplevel'], { encoding: 'utf8' }).trim();
const PKG = join(ROOT, 'packages/toolchain-qualification');
const readJson = (path) => JSON.parse(readFileSync(path, 'utf8'));
const manifest = readJson(join(PKG, 'package.json'));

const BIN = {
  tsc: 'node_modules/typescript/bin/tsc',
  vitest: 'node_modules/vitest/vitest.mjs',
  vite: 'node_modules/vite/bin/vite.js',
};
const run = (bin, ...args) => {
  const binPath = join(PKG, BIN[bin]);
  assert.ok(existsSync(binPath), `${bin} not installed: run npm ci --prefix packages/toolchain-qualification`);
  return spawnSync(process.execPath, [binPath, ...args], {
    cwd: PKG,
    encoding: 'utf8',
    maxBuffer: 64 * 1024 * 1024,
    env: { ...process.env, NO_COLOR: '1', FORCE_COLOR: '0', CI: '1' },
  });
};
const output = (r) => `${r.stdout}\n${r.stderr}`;
const tempDir = (t, prefix) => {
  const dir = mkdtempSync(join(tmpdir(), prefix));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  return dir;
};

// The qualified stack. Every entry must be pinned exactly; nothing else is a direct dependency.
const STACK = [
  '@nestjs/common', '@nestjs/core', '@nestjs/platform-express', '@nestjs/testing', 'reflect-metadata', 'rxjs',
  'typescript', 'vite', 'vitest', '@vitejs/plugin-react', 'react', 'react-dom', 'jsdom',
  '@types/node', '@types/express', '@types/react', '@types/react-dom',
];

test('T0002 pins: Node 24, exact direct versions, lockfile and installed tree agree', () => {
  assert.equal(process.versions.node.split('.')[0], '24', `Node ${process.versions.node} is not Node 24`);
  assert.equal(manifest.engines?.node, '>=24 <25');
  const pins = { ...manifest.dependencies, ...manifest.devDependencies };
  assert.deepEqual(Object.keys(pins).sort(), [...STACK].sort(), 'direct dependencies differ from the qualified stack');
  for (const [name, version] of Object.entries(pins)) {
    assert.match(version, /^\d+\.\d+\.\d+$/, `${name} is not pinned to an exact version`);
  }

  const lockPath = join(PKG, 'package-lock.json');
  assert.ok(existsSync(lockPath), 'package-lock.json missing');
  const lock = readJson(lockPath);
  assert.equal(lock.lockfileVersion, 3);
  assert.deepEqual(lock.packages[''].dependencies, manifest.dependencies, 'lockfile root dependencies drifted');
  assert.deepEqual(lock.packages[''].devDependencies, manifest.devDependencies, 'lockfile root devDependencies drifted');
  for (const [name, version] of Object.entries(pins)) {
    assert.equal(lock.packages[`node_modules/${name}`]?.version, version, `lockfile resolves ${name} differently`);
    const installed = join(PKG, 'node_modules', name, 'package.json');
    assert.ok(existsSync(installed), `${name} not installed: run npm ci --prefix packages/toolchain-qualification`);
    assert.equal(readJson(installed).version, version, `installed ${name} differs from the pin`);
  }
});

test('T0002-TEST01: decorator injection and Express raw-body middleware pass under Vitest on the pinned versions', (t) => {
  const report = join(tempDir(t, 't0002-vitest-'), 'report.json');
  const r = run('vitest', 'run', '--reporter=json', `--outputFile=${report}`);
  assert.equal(r.status, 0, `vitest failed:\n${output(r)}`);
  const results = readJson(report).testResults.flatMap((f) => f.assertionResults);
  const status = Object.fromEntries(results.map((a) => [a.fullName, a.status]));
  assert.deepEqual(status, {
    'T0002 Nest DI and controller contract emits design:paramtypes so constructor injection resolves by type': 'passed',
    'T0002 Nest DI and controller contract exposes the exact received bytes through the Express raw-body middleware': 'passed',
    'T0002 Nest DI and controller contract rejects with 400 when the raw-body middleware is not enabled': 'passed',
    'T0002 React client contract renders typed props and updates state on click': 'passed',
  });
});

test('T0002-TEST02: the separate typecheck catches the intentional incompatible type', () => {
  const clean = run('tsc', '-p', 'tsconfig.json', '--noEmit', '--pretty', 'false');
  assert.equal(clean.status, 0, `main typecheck failed:\n${output(clean)}`);

  const negative = run('tsc', '-p', 'tsconfig.negative.json', '--noEmit', '--pretty', 'false');
  assert.notEqual(negative.status, 0, 'typecheck accepted the intentional incompatible type');
  const errors = output(negative).split(/\r?\n/).filter((line) => /error TS\d+/.test(line));
  assert.equal(errors.length, 1, `expected exactly one type error:\n${errors.join('\n')}`);
  assert.match(errors[0], /typecheck-negative[\\/]incompatible-type\.ts\(6,\d+\): error TS2322\b/);

  // Same ill-typed module under Vitest: transpile-only, so it runs. Type safety needs the separate check.
  const transpiled = run('vitest', 'run', '--config', 'vitest.negative.config.ts');
  assert.equal(transpiled.status, 0, `transpile-only run failed:\n${output(transpiled)}`);
});

test('T0002 client build: Vite emits a static React bundle', (t) => {
  const outDir = join(tempDir(t, 't0002-vite-'), 'dist');
  const r = run('vite', 'build', '--outDir', outDir, '--emptyOutDir');
  assert.equal(r.status, 0, `vite build failed:\n${output(r)}`);
  const html = readFileSync(join(outDir, 'index.html'), 'utf8');
  const script = html.match(/<script[^>]+src="\/(assets\/[^"]+\.js)"/);
  assert.ok(script, 'index.html does not reference a built script');
  assert.ok(existsSync(join(outDir, script[1])), `missing bundle ${script[1]}`);
});
