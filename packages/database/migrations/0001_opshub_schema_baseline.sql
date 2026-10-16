-- 0001 opshub_schema_baseline (T0003, C-T0003-v1).
-- Runs as opshub_schema_owner (the runner SETs ROLE first), so the schema is owned by the owner role, not a login.
-- No tenant or domain tables: each owning task adds its own reviewed migration with explicit per-object grants.
create schema opshub;
revoke all on schema opshub from public;
-- The runtime role may resolve names in the schema; table privileges come only from later explicit grants.
grant usage on schema opshub to opshub_runtime;
