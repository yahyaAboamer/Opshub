# OpsHub — architectural testing strategy

**Phase 5 test design only.** No application/provider tests are executed in Phase 4. Requirements map to [AC01–AC15](../product/11-mvp-acceptance-criteria.md); fixtures use at least two merchants, Admin/Operator/platform/dual-context accounts, reused human-readable references and complete/incomplete inputs. No test may use production bookings, destructive writes or real customer communication without separately explicit authorization.

| Layer | Architectural proof |
|---|---|
| Domain/unit | OD01–OD07 dimensions, case-only resolution, stable objective/3 total attempt budget, consent/physical evidence, fixed KPI formula and policy-version behavior |
| Module/application service | Commands obey ownership/forbidden responsibilities; ingestion cannot send mutation; exact intent edit invalidates approval; case closure checks all requirements |
| Database/invariants | Real PostgreSQL nonowner roles; RLS read/write fail closed, composite FKs, one accepted outbound/return/pickup, uniqueness/last-Admin/objective reservations and decimal conservation |
| Authentication/authorization | Wrong/suspended membership, independent merchant/platform participation, direct command/API/worker denial, verified invitation recipient/single-use/expiry, no recovery self-grant |
| Tenant isolation | Every endpoint/filter/search/link/cache/job/file/export/contributor/audit; two tenants reuse phones/SKUs/tracking/order names; no cross-association or disclosures |
| Provider contract | Versioned official contract fixtures for auth/scopes/IDs/pagination/errors/async result/side effects and missing fields; no unqualified default provider behavior |
| Provider mock/sandbox | Simulate create acknowledgement, documented rejection, timeout before/after effect, truncated history, rate limit, auth revocation, callback/schema drift; controlled pilot qualification only after future approval |
| Webhook/replay | Raw-body signature validation, wrong account/merchant, repeated delivery/event, out-of-order update, late correction and full-page checkpoint rollback |
| Privacy provider requests | Forged/wrong-account/duplicate data-request and redaction receipt, source-identity scope, approved minimal tombstones, disclosure denial and deletion-manifest replay after restore |
| Action idempotency/concurrency | Two Admins/two keys, stale approval/subject/auth, queue redelivery, worker crash before send/after send/before local commit, unknown blocks both execution paths and stale worker quarantine |
| Partial effect/fallback | Creation known/booking failed or unknown/annotation incomplete; keep new order; safe handover makes old path nonactionable; recovered connection attaches same identity |
| Analytics regression | AC07/AC15 exact contributors and unrounded arithmetic; unknown versus zero, pending finals, overlapping product counts, once-only reversals/spend, SKU unavailable, compatible comparisons and late revision |
| Import/export | All rows/group dispositions, repeat accepted file, distinct real same-text contacts, ambiguous link held; malicious formulas/control characters/oversized input; scope/as-of/privacy/download revocation |
| Operations/recovery | Transactional enqueue rollback/duplicate, job starvation, membership/service suspension, token rotation crash, restore gap/journal hold/deletion manifests/old jobs and compatible rollback |
| End-to-end | AC01 onboarding → connected input → Operator contact/request → Admin action → returned evidence → justified closure → operational/Product/ROAS drill/export; platform restricted administration |

Recommended tools: Vitest for TypeScript domain/UI/API service tests, PostgreSQL/Testcontainers for invariant/RLS/concurrency checks, deterministic mock HTTP provider server with barriers/fault injection, and Playwright for browser/direct API flows. Typecheck separately because runtime test transpilation is not type verification. [Vitest](https://vitest.dev/guide/), [Postgres Testcontainers](https://node.testcontainers.org/modules/postgresql/), [Playwright API testing](https://playwright.dev/docs/api-testing). Nest decorator/DI test compatibility is verified on the selected pinned toolchain before relying on it; no second parallel test framework is necessary by default.

Use controlled transaction barriers to reproduce races, not timing sleeps alone. Assert **provider request/effect counts** and durable records after failure, not just UI labels. Sentinel tokens/phones/addresses verify diagnostics/log/export redaction. Real PostgreSQL covers invoker views, roles and transaction-local context reuse; an in-memory DB cannot prove RLS. Separate DB tests/connection pools avoid workspace or production DB selection mistakes.

## Council-driven adversarial fixtures

- Restore a point **before** an Order/connection/objective was locally created, while independent descriptor and provider effect survive. Rediscover native records: the same business scope remains held, with no new booking/replacement. Unreconstructable identity/coverage quarantines the merchant/connection.
- Handover, then manual booking after backup, then rollback. Independent handover survives; neither execution path resumes or creates a second effect without qualified reconciliation.
- Revoke a still-unexpired Admin/Operator/platform grant, consume/revoke an invitation, suspend service and complete customer redaction **after backup**, then restore. Old sessions/invites and fresh IdP login cannot obtain reads/exports/business authority before new-epoch revalidation; independent privacy manifests remove resurrected data before opening access.
- Two Operators race to Start contact for one due objective. Only one pre-call reservation is issued. Lost/abandoned/uncertain result cannot release allowance by lease expiry. Report an independently made fourth call: retain it as violating evidence and deny another authorized start. After restore, surviving contact-start markers prevent forgotten allowance/spacing from authorizing a fourth call.
- Reopen the same confirmation/return/pickup case and repeat imported labels: stable case/objective IDs and K05/K06 contributors remain unchanged; ambiguous legacy case identity is held rather than multiplied.
- Same SKU has qualified net sales 20,000, of which an **approved** revenue method attributes 15,000 and leaves 5,000 unattributed; spend 5,000 gives that method's ROAS 3.0. Without approved revenue eligibility, no unqualified ratio; spend mapping alone does not attribute all sales.
- Queue enqueue on the same domain transaction rolls back with it; no worker sees an uncommitted intent. Prove actual pg-boss adapter/grant compatibility, and safe repeated enqueue/sweep without a duplicate generic scheduler.

These are proposed test oracles, not completed application tests. They make recovery/authority/contact contracts reviewable without expanding into migration execution or telephony.

## Gentry regression oracle boundary

Phase 5 may use immutable workbook/system evidence for **source-qualified regression comparison**: named artifact/version/sheet/formula/locator, grain, period/calendar/as-of, source coverage and expected OpsHub normalization. It does not automatically execute original scripts/macros or alter `source/`. Preserve D01–D24 contradictions and unsupported historical episodes. Compare paid-inferred pickup versus physical evidence, outbound/reverse Delivered, legacy2-NoAnswer versus approved3 attempts, confirmed/all-placed versus process-entry denominator, missing-to-zero money, unmatched native keys and seven call-before-order anomalies.

Numerical equality is required only for the same approved definition/population; deliberately changed semantics require explained differences. No synthesized chronology/customer identity/case episode fixes an oracle discrepancy. AC12 comparison readiness is universal; historical comparison execution applies to a Gentry-ingesting/replacement pilot. This chapter plans a validation oracle, not migration design/execution or an implementation backlog.

Before release every applicable MUST gate passes in a controlled environment with qualified OP01/OP09 and other launch choices. Phase 4 verification checks documentation/integrity/review coverage only; it cannot certify application security, provider success, performance, cost or restore time.
