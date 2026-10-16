# Foundation plan

T0010 explicitly implements pinned Sentry/OTEL runtime exporters and composition wiring against mock sinks. T0005's no-op ports do not silently become production drivers; actual destination transmission is separately authorized and verified during environment release.

M0 creates a reproducible single-codebase local environment. T0001 is the smallest initial task. T0002 proves framework/test transformation and Express raw-body compatibility; T0003 proves PostgreSQL17/Kysely/pg migration and disposal/target guards. T0004 composes health/readiness and environment isolation.

T0005 adds redaction/correlation before customer-shaped data flows. T0006 supplies independently authored MA/MB fixtures, deterministic clocks and separate fake effect storage. T0007 proves same-connection pg-boss enqueue rollback/least grants before the first queue consumer. T0008 fixes recovery-record schema/coverage against a separate fake store; T1202 must qualify actual Amazon S3 before operational reliance. T0009 defines executable CI command contracts.

No compatibility test runs during Phase6. Exact package patches are intentionally unpinned until these authorized engineering tasks can obtain current evidence. An incompatibility produces an ARCHITECTURE DEVIATION PROPOSAL with failing pinned versions, minimal reproduction, impacted tasks/ADR, alternatives and required owner/engineering review; no silent stack change.

Each local task must work with synthetic data and fake providers. If Docker is unavailable, T0003 qualifies an equivalent disposable PostgreSQL17 instance; an in-memory database cannot prove RLS. Cloud provisioning is not a prerequisite for the first local slice.
