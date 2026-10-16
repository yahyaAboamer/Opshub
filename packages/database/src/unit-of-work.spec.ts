import { randomUUID } from 'node:crypto';
import type { Kysely } from 'kysely';
import { afterAll, beforeAll, describe, expect, inject, it } from 'vitest';
import { createRuntimeDb, migrate, withUnitOfWork } from './index';
import { dropDatabase, provisionDatabase, withClient, type ProvisionedDatabase } from './testing';

// Synthetic fixture table, created by the schema owner in test setup only (not a repository migration).
interface ProbeDatabase {
  'opshub.t0003_probe': { id: string; label: string };
}

describe('T0003-TEST03 Kysely unit of work', () => {
  let db: ProvisionedDatabase;
  let runtime: Kysely<ProbeDatabase>;

  // Counts through a separate runtime connection, so only committed rows are visible.
  const committedRows = (labelPrefix: string) =>
    withClient(db.runtime, async (c) =>
      Number((await c.query('select count(*) as n from opshub.t0003_probe where label like $1', [`${labelPrefix}%`])).rows[0].n),
    );

  beforeAll(async () => {
    db = await provisionDatabase(inject('postgres'));
    await migrate({ connection: db.migrator, expected: db.expected });
    await withClient(db.migrator, async (c) => {
      await c.query('set role opshub_schema_owner');
      await c.query('create table opshub.t0003_probe (id uuid primary key, label text not null)');
      await c.query('grant select, insert on opshub.t0003_probe to opshub_runtime');
    });
    runtime = createRuntimeDb<ProbeDatabase>({ ...db.runtime, max: 2 });
  });
  afterAll(async () => {
    await runtime?.destroy();
    await dropDatabase(db);
  });

  it('commits a successful unit of work', async () => {
    await withUnitOfWork(runtime, (trx) =>
      trx.insertInto('opshub.t0003_probe').values({ id: randomUUID(), label: 'synthetic-commit-1' }).execute(),
    );
    expect(await committedRows('synthetic-commit')).toBe(1);
  });

  it('rolls back a unit of work that throws and persists no rows', async () => {
    let seenInside = -1;
    await expect(
      withUnitOfWork(runtime, async (trx) => {
        await trx
          .insertInto('opshub.t0003_probe')
          .values([
            { id: randomUUID(), label: 'synthetic-rollback-1' },
            { id: randomUUID(), label: 'synthetic-rollback-2' },
          ])
          .execute();
        const inside = await trx
          .selectFrom('opshub.t0003_probe')
          .select((eb) => eb.fn.countAll<string>().as('n'))
          .where('label', 'like', 'synthetic-rollback%')
          .executeTakeFirstOrThrow();
        seenInside = Number(inside.n);
        throw new Error('synthetic failure after writes');
      }),
    ).rejects.toThrow('synthetic failure after writes');
    expect(seenInside).toBe(2);
    expect(await committedRows('synthetic-rollback')).toBe(0);
  });

  it('rolls back a unit of work that hits a constraint violation and persists no rows', async () => {
    const id = randomUUID();
    await expect(
      withUnitOfWork(runtime, async (trx) => {
        await trx.insertInto('opshub.t0003_probe').values({ id, label: 'synthetic-duplicate-1' }).execute();
        await trx.insertInto('opshub.t0003_probe').values({ id, label: 'synthetic-duplicate-2' }).execute();
      }),
    ).rejects.toMatchObject({ code: '23505' });
    expect(await committedRows('synthetic-duplicate')).toBe(0);
  });
});
