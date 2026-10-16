# Independent Council review — domain rigor and technical correctness

Verdict: **REVISE WITH BOUNDED AMENDMENTS before treating the Phase 5 validation contract as complete.** The design is substantially sound and suitable for continuing human review. It does not yet prove a safe pilot: implementation, provider, migration and recovery tests are explicitly not executed. I found no reason to reopen OD01–OD09 or replace the architecture. The amendments below close specific proof gaps; they do not authorize implementation or cutover.

Reviewed all migration documents 00–17 and `evidence/migration/golden-contracts.json`, plus approved owner decisions and architecture data, analytics, external-action and recovery contracts. I did not read other Council reviews or modify design files. Evidence below is document or synthetic-fixture evidence, not an observation of application behavior.

## Findings, in priority order

### 1. P1 — False-match repair needs an explicit contact/effect reservation continuity contract

**Evidence:** `02-identity-mapping.md`, “Collision and replay rules,” IM02 and IM-T10; `03-migration-pipeline.md`, “Failure, rollback and re-import”; `13-cutover-and-rollback.md`, “Corrected mapping and re-import.” These require retained old links/history, recomputation and invalidation of **unstarted** dependent approvals. Architecture `06-external-action-safety.md` reserves stable business objectives; architecture `13-deployment-and-environments.md` rebuilds holds from native/business descriptors. The migration test catalog does not compose these rules when the identity correction itself changes which canonical Order/case owns the native subject.

**Failure to test:** A false crosswalk attaches a native subject to synthetic Order OA; an actual or uncertain call/booking consumes or reserves its scope. A reviewed repair detaches that association and binds the native subject to OB. Re-import creates OB's apparently unused case/objective, or a later restore reconstructs only the old OA hold. Keeping the historic record and invalidating future approvals does not, by itself, prove that OB cannot obtain another allowance or executable objective. Conversely, blindly moving the completed result can falsely certify work on a different actual recipient/subject.

**Correction:** Add an explicit remap barrier and adversarial IM/EA/RV contract covering started, succeeded, unknown and manual-handover effects plus consumed/uncertain contact allowances. Preserve immutable execution-time native scope and intent; identify every affected old/new objective; block affected starts while continuity is ambiguous; reconcile current reservations and independent recovery descriptors without rewriting history. Test repair, replay and restore after repair. Expected result: no new allowance or duplicate effect merely because a canonical association changed, and no transfer of completion without evidence. If continuity cannot be established, quarantine the union of affected scopes. This is a missing proof obligation, not a claim that the intended implementation necessarily loses holds.

### 2. P2 — Some claimed contributor-level golden results still contain only scalar expectations

**Evidence:** `07-kpi-regression-suite.md`, “Result assertion envelope,” requires exact member IDs and amounts. Its KR16 row states prior sales 15,000, units 4 and delivery 3/4, but supplies no prior contributor identities or amounts. `06-golden-datasets.md` GD31 and JSON `partial_attribution` specify attributed 15,000/unattributed 5,000, but do not define which item amounts received that attribution. JSON `spend_revision` similarly specifies aggregate revised allocation rather than a full revised contributor result. The baseline has much stronger item and shipment sets.

**Failure to test:** Wrong prior shipments can yield the required 3/4, and two different item attribution assignments can both yield 15,000 and ROAS 3.0. A test author must invent the missing expected assignments or derive them from implementation output, weakening the independent oracle exactly where the suite rejects scalar-only equality.

**Correction:** Specify synthetic prior-period Orders/items/shipments, amount/basis per contributor, exact exclusion sets and complete current/prior comparison envelopes. For GD31, name each item's attributed/unattributed amounts and test-only eligibility basis. For GD30, spell out selected revision/portion contributors and retained prior results. These may remain logical JSON/document contracts; no executable importer or production policy decision is needed. Verify a same-total/wrong-item or wrong-prior-shipment mutation fails.

### 3. P2 — The temporal oracle does not distinguish the competing clocks it says must remain separate

**Evidence:** `06-golden-datasets.md`, “Envelope and reproducibility,” places baseline qualified dates on 18–20 August within a single window. JSON contact facts give first-attempt and first-action dates on the same date for all cases that have both. Confirmation and pickup entry dates and shipment creation also sit inside that window. `07-kpi-regression-suite.md`, “Cohorts,” requires exclusive-end, undated and timezone checks, but gives no concrete cross-clock expected sets. The architecture deliberately distinguishes occurred/effective/source-updated/observed/ingested/calculated clocks.

**Failure to test:** Using observation date for confirmation entry, order date for shipment-created cohorts, or first-attempt date for action-required cohorts can pass the present baseline. A generic exclusive-end test can also pass while evaluating the wrong field. This matters to shadow comparison because later-arriving evidence can silently rebucket historical work.

**Correction:** Add small synthetic cases where relevant clocks lie on opposite sides of a window boundary, including action required before the first attempt, shipment creation after order placement, late observation of earlier occurrence, and later correction with an earlier effective date. Declare exact members for each KPI and old/new generation. Include a named timezone-offset transition and an ambiguous local timestamp with the expected hold/qualification. State the test-only clock selection concretely rather than relying only on the `TEST-POLICY-v1` label. Production clock decisions remain MD06.

### 4. P2 — Pagination completeness needs an adversarial changing-population acceptance test

**Evidence:** `03-migration-pipeline.md` MP01 demands proof of all pages/coverage; `08-provider-contract-validation.md` PC-S02/S03 and PC-B04 require complete reads and overlapping incremental recovery; `13-cutover-and-rollback.md` CT01-D records bounded final reads, source skew and buffered work. CT-T03 covers changes during approval, but no named contract demonstrates discovery completeness when the source population changes during pagination itself.

**Failure to test:** A traversal can exhaust every returned cursor while an object moves across the already-read boundary, a late-visible update retains an earlier source timestamp, or a nested line connection changes between pages. Every acquired object can have a disposition and every checkpoint can be consistent while a required object was never acquired. Row conservation alone cannot detect this omission.

**Correction:** Extend provider/migration contracts with insert, update, delete/unavailability and nested-child changes between controlled page barriers. Require a provider-qualified snapshot/high-water/overlap/reconciliation method, declared limitations and exact expected identity/revision sets. When the provider cannot support a completeness claim, preserve explicit coverage uncertainty and block continuity-dependent activation rather than equating exhausted pagination with complete discovery. This does not assume any particular provider has the defect; it ensures the future qualification can detect it.

## What is already strong

Native tenant/account/kind identity precedes alias matching; source rows, canonical facts, derived interpretations and legacy outputs remain distinct. Disposition conservation explicitly handles unknown file remainders. Baseline KPI tests use exact contributor sets and reject equal percentages with different membership. Shadow mode disables contact starts as well as provider writes. Per-class authority switching includes native automations, old senders and manual executors. Restore gates independently protect effects, contact allowance, privacy and current grants. Rollback correctly preserves irreversible external facts. These protections address the requested attack categories directly; unresolved OP/A/MD decisions are not disguised as approvals.

## Assumptions and limits

- Human approval of Phases 1–4 supersedes their historical pending-review wording. Residual OP/A/MD policies and account capabilities remain unresolved.
- Logical fixtures are intentionally not provider payloads or implemented tests. Findings 2–3 ask for independent expected semantics, not premature implementation.
- No production rows, customer identifiers, credentials, live mutations or provider experiments were used. No execution readiness is inferred from documentation consistency.
- P1 denotes a safety-critical validation-contract gap that must be closed before affected migration/action activation; it is not an observed exploit or proven current software bug.

## Strongest objection to this position

The general invariants already demand stable reservation scope, exact contributors, correct clocks and truthful acquisition coverage. A competent Phase 6 engineer could derive all four amendments while realizing the contracts, and the numerous fail-closed gates may prevent an unsafe launch even without naming these combinations. That is a strong argument for approving Phase 5 with explicit conditions rather than rejecting it outright. My narrower concern is that a validation plan should name these falsifiable cases before the implementation supplies its own interpretation: otherwise its most important safety claims can pass tests that never exercise the failure.
