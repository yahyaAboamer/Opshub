# OpsHub — cost and complexity review

**Qualitative MVP assessment.** No actual pilot volumes, hosting plan or measured bill was supplied; precise monthly prices/totals are intentionally not fabricated. Compare current vendor plans/region/retention after owner chooses A06/OP13's envelope. [Technology recommendations](15-technology-selection.md) and [deployment](13-deployment-and-environments.md) are proposals.

| Driver | Expected qualitative behavior / control |
|---|---|
| Paid web/worker/database and staging | Main fixed baseline; database backup capability is worth paying for. One shared DB and worker avoid a service fleet; staging/preview duplication can materially add cost |
| Database storage/IO | Source revisions, contacts, contributor history and job retention grow; bounded raw payload/history, indexes and job cleanup limit cost. Never erase unknown actions as cost cleanup |
| Provider integration reads | Frequent broad polling/backfills consume quota/compute; callbacks plus incremental overlap/targeted reconciliation and account budgets reduce load |
| Objects/backups/egress | Small files/journal markers are likely modest at a small pilot, but raw payloads/exports and retained backups dominate growth; expiry and explicit download scope matter |
| Managed identity/MFA | Plan/user/security-feature gating can dominate early fixed costs; verify chosen package before build |
| Hosted observability/email | Low ordinary invitation volume; verbose traces/error loops can raise ingestion/mail cost. Sample traces/group failures and avoid sending product customer messages |
| Engineering/support | Provider qualification, unknown-result resolution and source/attribution mapping can exceed infrastructure cost; safe diagnostic/admin tools reduce investigation time |

Likely low-cost choices at small scale: no Redis, no warehouse/event bus, static UI from web service, one Postgres queue, manual commercial shell and small named provider set. The pre-dispatch journal is an intentional additional storage request/availability dependency per effect; it protects recovery across DB rollback, not speculative scale. Database relations/evidence tables add implementation work because the PRD demands trustworthy provenance and independent truth, not because every entity requires a service.

## Measured change triggers

| Observed pressure | Simplest next response / later extraction condition |
|---|---|
| Projection/export query duration threatens agreed operational latency | Inspect plans/indexes, bounded filters, incremental recomputation and worker capacity; consider read replica only after consistency/watermark review |
| Queue/reads consume DB capacity needed for commands | Fair limits/pool sizing/retention, separate workers. Replace queue transport if isolated queue load dominates; domain work/effect truth stays relational |
| Evidence tables exceed tested restore/maintenance budget | Approved retention, size-aware partitioning/archive minimal evidence; verify restore and old contributor explanation before change |
| Provider quota/failure isolation dominates work | More provider-specific worker concurrency/budgets; extract connector deployment only when measurable independent operation warrants it |
| Analytics workloads need independent historical exploration beyond MVP | Separate analytical replica/store with explicit tenant/security/input watermark contract; warehouse only for approved need |
| Tenant contractual isolation/large noisy tenant/independent recovery requirement | Reevaluate database-per-tenant or selective isolated tenant DB, with explicit routing and migration design in a separately authorized phase |
| Team needs independent module release ownership | Extract through existing ports/work IDs with new consistency/operations ADR; module count alone is not justification |

Thresholds are **agreed workload/latency/restore targets and measured symptoms**, not invented order-count ceilings. OP13 must supply expected merchants/orders/contacts/shipment/spend history/export sizes and source freshness/reconciliation expectations. No premature massive-scale plan is introduced.

Deferred complexity: Kubernetes, microservices, distributed saga platform, event bus/CDC, warehouse, always-on cache, multi-region active-active, generic provider marketplace/workflow engine, advanced inventory/replenishment, native finance/refunds, billing metering/processor and rich seasons. Deferred functionality is not secretly implemented through technical module names.
