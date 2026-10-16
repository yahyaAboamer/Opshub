# Planned repository and ownership boundaries

These are future boundaries, not scaffolded directories. T0001 establishes version control/workspace protections; T0002/T0003 qualify tooling before T0004 composes the runtime.

| Planned area | Responsibility |
|---|---|
| apps/web | React/Vite merchant and separately guarded platform views; feature-owned routes/components |
| apps/api | Nest Express HTTP composition root and shared in-process business modules |
| apps/api/modules | Identity/tenant, Orders, Cases, Logistics, Actions, Catalog, Advertising, Integrations/Transfer, Trust and Projections |
| apps/worker | Worker composition root plus provider adapters/job handlers; imports the same business modules without starting HTTP |
| packages/database | Kysely/pg unit of work, roles/RLS and serialized reviewed SQL migrations |
| packages/jobs, packages/recovery | Qualified single pg-boss transport and bounded independent-record protocols |
| packages/config, packages/observability | Validated environment and redacted correlation primitives |
| tests | Synthetic reviewed fixtures, independent expectations, real DB, mocks/barriers, browser and qualification evidence |
| docs/contracts | Versioned accepted task boundaries with actual typed interfaces/schema/errors/commands |
| ops | Explicit later environment/release/recovery artifacts |
| docs/implementation | Canonical task/status/coverage index and generated views |

One immutable release serves built web plus API on the paid Render web service; worker is a separate process from that codebase. There are no internal network services or duplicated worker business rules. HTTP/provider/storage ports are narrow boundaries.

Task editable areas are ownership contracts. Exact implementation filenames are discovered and frozen by predecessor tasks. If accepted structure differs, record a bounded ownership-map amendment before editing, preserving semantics. Shared package/lockfile/interface/router/migration edits require integration-owner allocation; an adapter/UI task cannot silently widen into those files.

Original source/ and Phase1–5 docs/evidence remain immutable. Real customer intake, credentials and private test evidence stay out of Git/AI prompts. Synthetic fixtures and redacted aggregate evidence can be reviewed.
