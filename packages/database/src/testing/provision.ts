import { randomBytes, randomUUID } from 'node:crypto';
import pg from 'pg';
import { IDENTITY_SETTING_DATABASE_ID, IDENTITY_SETTING_ENVIRONMENT, RUNTIME_ROLE, SCHEMA_OWNER_ROLE } from '../catalog';
import type { ExpectedTarget } from '../target-guard';
import type { DisposableServer } from './disposable-postgres';

/**
 * Local provisioning for disposable databases: the privileged step a real environment performs outside migrations
 * (roles, database, identity marker, database-level grants). Synthetic and test-only; not a production procedure.
 */
export interface ProvisionedDatabase {
  name: string;
  expected: ExpectedTarget;
  /** Superuser connected to this database (fixtures and inspection only). */
  admin: pg.ClientConfig;
  /** Migrator LOGIN: member of the schema owner WITH INHERIT FALSE, SET TRUE. */
  migrator: pg.ClientConfig;
  /** Runtime LOGIN: member of the runtime role. */
  runtime: pg.ClientConfig;
  migratorLogin: string;
  runtimeLogin: string;
  server: DisposableServer;
}

const IDENTIFIER = /^[a-z][a-z0-9_]{0,40}$/;
const ENVIRONMENT = /^[a-z][a-z0-9-]{0,62}$/;

const connection = (server: DisposableServer, database: string, user = server.user, password = server.password): pg.ClientConfig => ({
  host: server.host,
  port: server.port,
  database,
  user,
  password,
});

export async function openClient(config: pg.ClientConfig): Promise<pg.Client> {
  const client = new pg.Client(config);
  await client.connect();
  return client;
}

export async function withClient<T>(config: pg.ClientConfig, work: (client: pg.Client) => Promise<T>): Promise<T> {
  const client = await openClient(config);
  try {
    return await work(client);
  } finally {
    await client.end();
  }
}

/** Cluster-wide NOLOGIN group roles of grant catalog v1. Run once per disposable server. */
export async function provisionClusterRoles(server: DisposableServer): Promise<void> {
  await withClient(connection(server, 'postgres'), async (c) => {
    await c.query(`create role ${SCHEMA_OWNER_ROLE} nologin nosuperuser nocreatedb nocreaterole noinherit nobypassrls`);
    await c.query(`create role ${RUNTIME_ROLE} nologin nosuperuser nocreatedb nocreaterole nobypassrls`);
  });
}

export async function provisionDatabase(
  server: DisposableServer,
  options: { environment?: string; identity?: null } = {},
): Promise<ProvisionedDatabase> {
  const name = `t0003_${randomBytes(4).toString('hex')}`;
  const environment = options.environment ?? 'local-synthetic';
  if (!IDENTIFIER.test(name) || !ENVIRONMENT.test(environment)) throw new Error('invalid synthetic provisioning input');
  const expected: ExpectedTarget = { database: name, environment, databaseId: randomUUID() };
  const migratorLogin = `${name}_migrator`;
  const runtimeLogin = `${name}_app`;
  const migratorPassword = randomBytes(18).toString('hex');
  const runtimePassword = randomBytes(18).toString('hex');

  await withClient(connection(server, 'postgres'), async (c) => {
    await c.query(`create database ${name}`);
    if (options.identity !== null) {
      await c.query(`alter database ${name} set ${IDENTITY_SETTING_ENVIRONMENT} = '${expected.environment}'`);
      await c.query(`alter database ${name} set ${IDENTITY_SETTING_DATABASE_ID} = '${expected.databaseId}'`);
    }
    await c.query(`revoke all on database ${name} from public`);
    await c.query(`grant connect, temporary on database ${name} to ${RUNTIME_ROLE}`);
    await c.query(`grant create on database ${name} to ${SCHEMA_OWNER_ROLE}`);
    await c.query(`create role ${migratorLogin} login password '${migratorPassword}'`);
    await c.query(`grant connect on database ${name} to ${migratorLogin}`);
    await c.query(`grant ${SCHEMA_OWNER_ROLE} to ${migratorLogin} with inherit false, set true`);
    await c.query(`create role ${runtimeLogin} login password '${runtimePassword}'`);
    await c.query(`grant ${RUNTIME_ROLE} to ${runtimeLogin}`);
  });

  return {
    name,
    expected,
    admin: connection(server, name),
    migrator: connection(server, name, migratorLogin, migratorPassword),
    runtime: connection(server, name, runtimeLogin, runtimePassword),
    migratorLogin,
    runtimeLogin,
    server,
  };
}

export async function dropDatabase(db: ProvisionedDatabase | undefined): Promise<void> {
  if (!db) return;
  await withClient(connection(db.server, 'postgres'), async (c) => {
    await c.query(`drop database if exists ${db.name} with (force)`);
    await c.query(`drop role if exists ${db.migratorLogin}, ${db.runtimeLogin}`);
  });
}
