// T0002-TEST01 (server): Nest constructor injection and Express raw-body middleware on the pinned toolchain.
import 'reflect-metadata';
import { createHash } from 'node:crypto';
import { Test, type TestingModule } from '@nestjs/testing';
import type { NestExpressApplication } from '@nestjs/platform-express';
import { afterEach, describe, expect, it } from 'vitest';
import { AppModule } from './app.module';
import { DigestService } from './digest.service';
import { WebhookController } from './webhook.controller';

// Synthetic payload. The irregular spacing and trailing newline are lost by JSON.parse + JSON.stringify,
// so only the exact received bytes reproduce RAW_SHA256.
const RAW = '{"event":"synthetic.ping",  "n":1}\n';
const RAW_SHA256 = createHash('sha256').update(RAW).digest('hex');
const REPARSED_SHA256 = createHash('sha256').update(JSON.stringify(JSON.parse(RAW))).digest('hex');

const apps: NestExpressApplication[] = [];
afterEach(async () => {
  await Promise.all(apps.splice(0).map((app) => app.close()));
});

async function compile(): Promise<TestingModule> {
  return Test.createTestingModule({ imports: [AppModule] }).compile();
}

async function start(options: { rawBody: boolean }): Promise<string> {
  const app = (await compile()).createNestApplication<NestExpressApplication>(options);
  apps.push(app);
  await app.listen(0, '127.0.0.1');
  return `${await app.getUrl()}/webhooks/synthetic`;
}

function post(url: string): Promise<Response> {
  return fetch(url, { method: 'POST', headers: { 'content-type': 'application/json' }, body: RAW });
}

describe('T0002 Nest DI and controller contract', () => {
  it('emits design:paramtypes so constructor injection resolves by type', async () => {
    expect(Reflect.getMetadata('design:paramtypes', WebhookController)).toEqual([DigestService]);
    const moduleRef = await compile();
    const controller = moduleRef.get(WebhookController);
    expect(controller.digests).toBeInstanceOf(DigestService);
    expect(controller.digests).toBe(moduleRef.get(DigestService));
  });

  it('exposes the exact received bytes through the Express raw-body middleware', async () => {
    expect(RAW_SHA256).not.toBe(REPARSED_SHA256);
    const res = await post(await start({ rawBody: true }));
    expect(res.status).toBe(200);
    expect(await res.json()).toEqual({ sha256: RAW_SHA256, bytes: Buffer.byteLength(RAW), event: 'synthetic.ping' });
  });

  it('rejects with 400 when the raw-body middleware is not enabled', async () => {
    const res = await post(await start({ rawBody: false }));
    expect(res.status).toBe(400);
    expect(await res.json()).toMatchObject({ statusCode: 400, message: 'raw body unavailable' });
  });
});
