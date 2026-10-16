# Independent council review — Generalist

Verdict: **Revise before accepting the Phase 5 validation contract as sufficient.** The overall migration direction is sound and unusually explicit about uncertain evidence, non-equivalent legacy metrics, tenant ownership, irreversible effects and recovery. It does not presently prove a safe pilot, and correctly does not claim executed proof. Four bounded corrections would make the design a stronger basis for later implementation. These are document/test-contract findings, not authorization to implement or run a migration.

Reviewed all first-draft migration documents 00–17 and `evidence/migration/golden-contracts.json`, alongside approved OD01–OD09, product KPI/acceptance contracts and relevant action, analytics, privacy and recovery architecture. No other council response was read. No source/customer values were copied, design documents changed, provider experiments run or production actions performed.

## Findings

### 1. P1 — Golden quality state can certify an unmapped denominator as complete

**Evidence:** `docs/migration/06-golden-datasets.md`, GD03, explicitly calls S08's finality **unmapped**. `docs/migration/07-kpi-regression-suite.md`, baseline paragraph, calls known population/input coverage complete while distinguishing missing mappings as provisional/unavailable. The JSON KR02 and KR03 entries nevertheless set `expected_state` to `complete`. Approved `docs/product/06-analytics-and-kpis.md`, KPI05, requires a provisional known-population result when unmapped records could change numerator/finality.

**Failure:** A calculator can return the correct 3/5 and 1/5, expose S08 as unknown, and still falsely certify the result as complete. Capture completeness and interpretation completeness are being conflated at the acceptance boundary. Source conservation and exact members alone do not correct the quality claim.

**Correction:** Distinguish complete source capture from provisional interpretation explicitly. Keep the approved known-subset ratios and member sets, but expect provisional quality when finality is genuinely unmapped. Alternatively, define a separate fixture where a qualified provider observation is positively known to be pending/unknown under an approved mapping, and explain why its quality differs. Add an assertion that dashboard, contributors and export carry the same trust state. Review analogous unknown/conflict cases rather than mechanically downgrading every pending population.

### 2. P1 — False identity repair lacks a contract for already-started effect and contact reservations

**Evidence:** `02-identity-mapping.md`, IM02 and IM-T10, preserve prior links and invalidate unstarted approvals after remapping. `13-cutover-and-rollback.md`, “Corrected mapping and re-import,” requires detaching the wrong selected association. Existing EA11/RV03 recover missing objectives after restore, but no migration test combines a false accepted crosswalk, an already-started or unknown effect/contact, remapping, re-import and subsequent action eligibility. Phase 4's stable business-objective and independent-journal contracts require these reservations to survive.

**Failure:** Suppose a legacy subject was incorrectly bound to Order A, an external booking or contact may have occurred, and review later binds that evidence to Order B. Detaching A and invalidating only unstarted approvals leaves undefined whether A or B can receive a new objective or renewed contact allowance. A correct identity repair can therefore sever the suppression knowledge that prevented duplicate effects. The same issue can remain latent until restore replays the older journal descriptor.

**Correction:** Add an explicit remapping rule and adversarial contract: hold both affected scopes while tracing realized/unknown effects, issued handovers and used/uncertain contact allowance; retain immutable original dispatch scope and append a reviewed correction/supersession link that independent recovery can interpret. Never automatically transfer or reset a budget, release a reservation, or authorize a new effect because an association moved. Where true effect scope cannot be proven, quarantine the appropriate wider scope. Test new attempts on both A and B before and after re-import and restore; expected dispatch count is zero until the reviewed safety resolution.

### 3. P2 — The golden JSON is a partial expectation catalog, not yet a reproducible logical fixture contract

**Evidence:** `06-golden-datasets.md`, “Envelope and reproducibility,” says every dataset fixes scoped identities, provider/schema versions, raw assertion locators, expected facts/holds/dispositions and policies. In the JSON, policies are names rather than defined rules; MB has account names/reused aliases but no competing business observations; contact facts mostly use `attempts`, `reached` and `action_complete` summaries rather than identified event/effect evidence; Product/items/spend lack sufficient dated source assertions to reproduce their full cohort/selection logic. `required_scenarios` enumerates GD01–GD36, but many have no structured stimulus/expected output beyond the Markdown narrative.

**Failure:** A future fixture adapter can silently invent the identity, event chronology, policy or result evidence needed to make the expected totals pass. For example, constructing two events from C01's count would test an adapter's invented facts while the real importer is forbidden from synthesizing events from counters. Listing GD27 cannot demonstrate a collision if no second-merchant subject is realized. An arithmetic checker cannot establish those missing semantic inputs.

**Correction:** Without writing an importer, complete the logical specifications for the critical scenarios: explicitly identified events, requirement/effect results, native account/object bindings, source assertion locators, cohort clocks, test-policy rules, expected dispositions and collision counterparts. Alternatively, label the JSON clearly as the partial expected-value index and require a separately reviewed complete logical-fixture manifest before V2 can pass. Each required scenario must link to precise inputs, ordered variation and expected members/holds/quality state; no fixture author may fill evidence gaps by inference. Keep expected-result derivation independent of production normalization/selection code.

### 4. P2 — Final-sync coverage needs an adversarial mutable-pagination acceptance contract

**Evidence:** `03-migration-pipeline.md`, MP01/MRUN01, and `08-provider-contract-validation.md`, PC-S02/S03 and PC-B04, require complete pages, coverage and overlap. `13-cutover-and-rollback.md`, CT01-D, acknowledges ongoing external commerce and calls for a fixed coverage-bound final read with buffered post-cutoff work. CT-T03 tests changes during approval, but the listed cases do not test membership changing while pages or nested lines are being acquired, cursor expiry/restart, or an object becoming inaccessible between passes.

**Failure:** All requested pages can succeed and every acquired row can receive a disposition while an object is skipped as a mutable ordering moves it across page boundaries. A missing/deleted/inaccessible object can also be mistaken for a successful empty range. Row conservation proves conservation of received data; it does not prove that the received population is complete. An overlap statement without a qualified ordering and gap-detection contract is insufficient for the final operational handoff.

**Correction:** Add a provider-independent acceptance scenario for create/update/delete-or-inaccessibility between pages, same-timestamp updates, nested-line changes, and cursor expiry/restart. Qualification must identify the actual provider's stable snapshot or bounded watermark/overlap/catch-up mechanism and its limitations. Pass only when the expected source identity/revision set is independently reconciled, or the uncovered scope is explicitly held and blocks affected continuity. Require proof that no gap exists between the final accepted boundary and buffered incremental work. Do not invent a provider capability or numerical overlap window in Phase 5.

## Assumptions and limits

- The owner's approval of Phases 1–4 supersedes historical pending-approval prose; remaining OP/A and MD decisions are still unresolved. No finding requests changing OD formulas or removing integrated MVP scope.
- The source and provider contracts are unqualified until the future evidence stages run. This review evaluates internal sufficiency and consistency, not real account permissions, actual historical matches or deployed behavior.
- The existing design already handles many of the requested attacks well: native scoped identity, exact source-unit conservation, separate legacy/fact/interpretation records, equal-percentage/wrong-member rejection, effect unknown holds, native automatic-booking ownership, separate recovery access/egress gates and explicit privacy restrictions. The findings above should not be used to claim these safeguards are absent.
- P1 findings affect interpretation or irreversible-action safety directly. P2 findings narrow how later tests demonstrate existing requirements; they do not justify creating an engineering backlog or implementation now.

## Strongest objection

The package can become a convincing checklist whose arithmetic and document links pass while identity/event provenance and acquisition completeness remain supplied by the same implementation being tested. Its correct fail-closed prose is necessary, but insufficient without independent, fully specified adversarial evidence at those boundaries. The most dangerous concrete version is a false match corrected after an unknown effect: analytics can look repaired while duplicate-prevention knowledge has become disconnected. Resolve that case explicitly before treating the migration design as ready for implementation planning.
