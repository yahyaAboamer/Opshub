# OpsHub — jobs, reconciliation and attention

**Recommendation:** durable Postgres jobs (pg-boss), with one worker process initially and one scheduling/retry authority. Retain module-owned state only for a business invariant or useful run/checkpoint. Scheduler/worker come from the monolith release. No distributed scheduler/event bus. [ADR007](adr/ADR-007-background-jobs.md). Official [pg-boss](https://github.com/timgit/pg-boss) supports existing-transaction enqueue adapters and PostgreSQL-backed processing; external effect guarantees remain application responsibilities.

## Delivery and transactional semantics

Enqueue through the pg-boss adapter on the **same checked database transaction/connection** as the domain state/audit. Commit both or neither; do not use a separate connection that can commit the job early. A small fixed enqueue capability has only necessary queue permissions, never schema-owner grants. A08 must prove transaction enlistment, rollback and role compatibility on the pinned version. If that fails, revise ADR007 before build; do not silently fall back to an unprotected after-commit send.

pg-boss owns routine scheduling, transport claims, retry/backoff and dead letters. Ordinary safe sync/projection work does not get a parallel general `outbox_work` lifecycle. Business action intent/effect/reservations, sync checkpoint/run, export request and requested projection generation remain authoritative domain records because they explain real obligations/results. Fixed recovery sweeps may re-enqueue an eligible missing run/effect by stable domain ID; they never authorize a started/unknown mutation. Queuing success does not certify business completion. Stable job/run keys and idempotent domain writes tolerate repeated enqueue/redelivery without duplicating effects.

Assume at-least-once execution/redelivery. Each handler validates trusted type, referenced tenant/source/business record and expected revision before establishing a tenant transaction. Queue envelope contains identifiers, not contacts/intent bodies/secrets. Queue role sees only queue/administrative schedule references; tenant work uses a separate non-BYPASSRLS pool. Cross-tenant health scheduling enumerates approved metadata and dispatches separate tenant jobs; it does not query operational records globally.

Use atomic claims and leases for safe reads/projection/export work; renew bounded leases and retry idempotently. An expired mutation lease becomes unknown/reconciliation work, never a second mutation. Per-connection locks serialize cursors/token refresh; per-objective locks serialize action transition; per-tenant projection revision avoids two rebuilds publishing mixed generations. Keep DB locks short and network outside transactions. Fair bounded queues/provider budgets prevent one tenant monopolizing resources.

## Work catalog

| Work | Trigger / idempotency / failure treatment |
|---|---|
| Inbox processing | Durable authenticated receipt; unique receipt/object revision; schema/link failure → held observation/problem state |
| Initial/incremental Shopify/Bosta sync | Reviewed connection schedule/manual refresh; connection checkpoint/page identity; read retry with overlap and visible coverage |
| Meta spend report/recheck | Scheduled period+parameter series; revision comparison; report polling safely resumes; failed/incomplete spend remains unavailable/provisional |
| Result reconciliation | Started/unknown/async effects and callbacks; existing effect ID; read-only, positive/negative evidence qualification; alert overdue unknown without resending |
| Mutation dispatch | Approved exact effect ID; single ExecutionStarted CAS; no automatic write retry |
| Stale source/attention refresh | Watermark change and time tick; stable tenant/subject/predicate key; current source clock is explicit |
| KPI/product projection | Input/definition revision dirty marker; generation ID; atomically publish complete consistent result/contributors |
| Export generation | Requester/scope/input revision; reauthorization before work and download; repeat safe object/run identity |
| Cleanup/retention | Approved class policy + hold checks + deletion manifest; unavailable until owner/legal retention approval |
| Invitation/commercial state | Explicit invite request/effective state; duplicate message key/recipient check; no billing charges or automatic overdue suspension |
| Health summaries | Tenant job computes allowlisted aggregate counts; publish only safe administrative output |

Failed safe work has bounded retries/backoff, next eligible time and last error category; exhausted work enters a visible dead-letter/problem state with responsible Admin/platform diagnostic owner as appropriate. Manual redrive authorizes only safe handler replay. A generic redrive screen cannot resubmit an external mutation or reset a contact budget. All proposed cadence/freshness/reconciliation-age targets require OP08/OP13; no invented SLA is claimed.

## Operational attention: persisted versus derived

Cases persist objective, owner, required work, evidence, attempt usage/last actual time, next eligibility, closure/reopen history and version. Actions persist exact intent and results. Quality conflicts persist competing assertions/decision evidence. Queue membership is a **derived projection** with rule version/reason/clock/input revision. Stable `(merchant, subject, predicate)` keys prevent a new task for every refresh. Only embedded work/administrative incidents retain human assignment/acknowledgement; no arbitrary task builder.

The normal external-call workflow begins with a checked **Start contact** command that atomically validates membership, purpose, current due time, remaining allowance and exclusive actor reservation. One outstanding/uncertain reservation prevents another Operator or Admin from starting the same objective. Release of a clearly unused slot requires an explicit attributable no-call declaration/review under OP04; expiry, loss of a page or reassignment cannot imply no call. If a call might have occurred, hold the slot until evidence establishes the attempt/no-call status. Record real occurrence/reach separately; an unknown reservation does not become a fabricated call event. A disclosed independently made/excess call remains evidence and a policy violation, never a hidden fourth authorized start. OpsHub controls its authorized workflow and cannot physically prevent an independent off-platform call.

Issuance has explicit phases: reserve exclusively in a short DB transaction; confirm the independent contact-start descriptor outside that transaction; recheck current authority/reservation and mark issued before the UI permits the authorized call. Failure/lost response holds the reservation as uncertain; no asynchronous worker calls the customer. Evidence recording later consumes the same slot or appends an attributable known-unused disposition. This is one fixed contact protocol, not a new scheduler or telephony feature.

| Attention predicate | Basis / permitted exit |
|---|---|
| Contact due/overdue | Open customer-contact objective, usable contact, remaining budget and current next eligible time; record actual attempt or explicit policy review |
| Attempts exhausted/unreached | Three ordinary attempts used with no successful reach; outside active call queue, visible exceptions/history; never automatically resolved/cancelled |
| Reached/action required | At least one reach plus outstanding case requirement; remains open even at contact limit |
| Approval waiting | Current submitted intent lacks Admin decision; no provider effect |
| Failed known-no-effect action | Accepted negative execution evidence; Admin reviews retry/revision/fallback |
| Unknown external result | Started effect lacks reliable result; blocks repeat and manual execution; reconcile |
| Pickup waiting | Purpose-specific physical collection lacks accepted evidence; payment separately visible |
| Data-quality conflict | Competing/missing/ambiguous assertions or unsupported episode; selection/correction with attributable reason or qualified new input |
| Stale source | Last accepted/source coverage exceeds approved source-specific target; receipt alone cannot clear incomplete coverage |
| Unbooked shipment | Eligible/confirmed delivery Order without accepted outbound and without satisfied booking objective; source uncertainty may block action rather than claim unbooked certainty |
| Unresolved return/pickup/recovery | Specific required work/effects/physical evidence outstanding; only case completion predicate closes |
| Product attention | Missing SKU/spend/attribution or comparable deterioration/approved threshold with sample/window; no automated campaign/tier/production action |

Backlog is independent of dashboard date filters. Read current due predicates with database/application clock so worker delay cannot hide newly due contact. Prioritize due/overdue, then earliest eligibility and stable ID as a proposal; retain explicit filtered/excluded counts. Schedule the next allowed attempt from actual previous attempt time, approximately 24h apart, not a caught-up calendar sequence. Successful attempts count toward3; reach is sticky evidence, not reset by later NoAnswer. Case reopen preserves the same objective budget. Imported summaries never invent call chronology; uncertain consumed budget safely blocks new calls pending mapping review.

Suspension retains durable receipt and read-only already-started-effect reconciliation under the proposed OP11 continuity exception. Outages do not close attention or replace stale data with zero. [06](06-external-action-safety.md) controls unknown-result recovery; [12](12-observability-and-operations.md) makes stalled jobs/problems observable.
