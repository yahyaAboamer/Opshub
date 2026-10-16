# Phase 2 quality review — 14 October 2026

Status: **complete model draft reviewed and revised; pending human acceptance**. Review does not approve policies, prove current enforcement, or authorize a later phase. All work stayed in `docs/domain/` and new `evidence/domain/`; the immutable reconstruction/source/evidence baseline is verified separately.

## Method and limits

The first complete ten-document model existed before council review. The [LLM Council skill](C:/Users/AboAmer/.agents/skills/llm-council/SKILL.md) was applied as three independent lenses followed by three fresh blind peer reviewers and chairman synthesis. The default member count was adapted to available agent capacity; the unavailable skill-specific model name was not used. Agents inherited the current supported model, so this is a same-provider council, not a cross-vendor comparison. No OpenRouter calls, external communications or production actions occurred.

Usage exhaustion interrupted the initial reviewers on 13 October; the user's continuation resumed them on 14 October. All three independent reviews and three peer reviews completed. A temporary agent-capacity limit delayed the third fresh peer until a slot became available. No model edits occurred between the first complete draft and completion of blind peer review.

Review prompts covered missing entities, incorrect cardinalities, mixed grains, over/under-modeling, migration risks and unjustified assumptions; reviewers could check immutable local Phase 1 evidence. [Stage 1 responses](council-stage1-anonymized.md) and [Stage 2 peer reviews](council-stage2-blind-reviews.md) preserve the critiques. Archived first-draft line links/wording refer to that earlier draft and are not refreshed as evidence.

## Blind ranking and synthesis

| Response / original lens | Peer 1 rank | Peer 2 rank | Peer 3 rank | Mean rank |
|---|---:|---:|---:|---:|
| A — Pragmatist | 1 | 1 | 2 | 1.3333 |
| B — Red-teamer | 2 | 2 | 3 | 2.3333 |
| C — Domain rigorist | 3 | 3 | 1 | 2.3333 |

Aggregate: A first; B and C tied. Synthesis uses supported findings from all three rather than adopting one answer. All reviewers supported wallet-grain preservation and avoiding fabricated transactions/events. Peer disagreement concerned how much the draft already made intake/series distinctions explicit and whether an observed Business ID proves account identity. The chairman retained the identifier observation while keeping account/Merchant semantics unresolved, and treated summary/revision changes as clarifications, not discovered new facts.

## Findings and dispositions

| ID | Finding / evidence classification | Disposition in final draft |
|---|---|---|
| QR01 | Evidence-supported mapping gap: wallet row narrowed to fee. Retained RAW_Costs profile O:P/Q:AF/AG:AJ has COD/online payment/components/total/net/status/time/cash-out assertions; 1,381 rows, 78 distinct cash-out references | **Corrected:** named Courier Wallet Observation value object; explicit source grain, optional links/unmatched rows, fee component/aggregate views, payment/grouping assertions. No bank settlement, customer refund or net formula inferred. Catalog, identities, events, glossary, decisions PD24 and mapping revised. |
| QR02 | Missing source identifier observation; account-identity interpretation remains unresolved. RAW_Costs A Business ID populated on 1,381 rows/one distinct value | **Corrected with qualification:** preserve native binding candidate; do not declare Merchant/courier account equivalence. E04/PD20/mapping/questions distinguish available identifier from unverified boundary. No raw business identifier value copied. |
| QR03 | Proposed clarification: retry wording could erase duplicated consequences, even though unknown effects were otherwise preserved | **Corrected:** Action intent, result references and receipt observations distinct; repeat receipts can describe one result; one intent can have several evidenced duplicates. Representational cardinalities are proposals, not current behavior. E15/02/03/I18 revised, PD10 remains open. |
| QR04 | Proposed traceability clarification: native-object namespace versus artifact lineage | **Corrected:** native namespace qualified separately in Source Context; file/backup lineage is capture provenance and cannot automatically split or merge external identities. E04/02/I03/glossary/PD20/mapping revised. |
| QR05 | Evidence-supported omitted boundary: report quality eligibility differs from Operations review (BR16/BR24/L26/Phase 1 workflow) | **Corrected:** separate report-review fragment and invariant I26; stated intent/current DRAFT wording distinguished from enforcement. Revision-specific retained approval attribution explicitly proposed; no Report entity/sending workflow or historical approval events invented. |
| QR06 | Proposed precision: intake summary bundle already partly preserved but not fully named | **Clarified:** Contact Intake Summary value object retains source Date/support-attempt counter/narrative/classifications/blank fields. No synthetic Contact Events/courier attempts. Exact source counter/date roles scoped to Phase 1 instructions. |
| QR07 | Proposed precision: classification responsibility/trust versus operator assignment | **Clarified:** classification value object retains label/kind/taxonomy/source/actor/mapping version; Product/Courier/Ops/Customer/Unknown is not Membership/grant/Task assignee. |
| QR08 | Proposed precision: observation-series/result-revision contracts and optional allocation identity | **Clarified:** E18/E22/E23 distinguish stable series versus observation/result revision and changed basis. Manual weekly input and calculated export remain separate kinds. Allocation is conditional entity only with independent reconciliation/history; otherwise projection with result reference. No extra required entity introduced. |

## Required challenge checklist

| Risk from owner request | Review result / containment |
|---|---|
| Spreadsheet-driven entities | No RAW/master/dashboard sheets are commerce entities. Wallet/intake are named source-observation bundles; charge/contact events keep distinct grains. |
| UI-driven entities | Queue, chart, status, stage, tier and recommendation are classifications/projections; no entity per screen. |
| Mixed grains | Order/header/item/leg/attempt/contact/return episode/product/variant/period/stock/cost/allocation grains explicit. Wallet row versus fee and intake versus event clarified. Return/pickup episode identity remains PD18. |
| Status/event confusion | Source assertions, actual occurrences, approval/action intent and calculated projections separated. Current state does not fabricate transition history. |
| Order/shipment conflation | Multiple source legs/order preserved; courier Delivered differs from order kept. Provisional primary leg link is not enforced as source fact (PD09). |
| Product/variant conflation | Product GID, SKU label, Variant and Order Item separate; unresolved catalogue/inventory crosswalk PD13. |
| Customer identity assumptions | Phone/name nonunique; optional Customer link, independent order contact snapshot, merchant ownership; PD12 open. |
| Actor/user assumptions | Authenticated actor, free-text claim, automation and recorder/importer distinct; membership/approver policy PD11/PD19 open. |
| Merchant tenancy omissions | All 25 entity kinds evaluated; merchant-owned objects/context relationships explicit, User account scope exception exposed; no current tenancy/RBAC proof claimed. |
| Historical provenance loss | Original labels/source times/windows/blanks/unmatched links retained; native namespace versus artifact provenance clarified; revision preservation proposed without fabricated old versions. |
| Irreversible actions as status fields | Reship Request/approval and per-effect Action/results/receipts separated; refund label not transaction. Multiple/unknown consequences represented, PD10/PD24 open. |
| Derived metrics as factual events | Outcome/KPI/advice/allocation remain derived with grain/definition/input revision/as-of. E23 entity continuity conditional, never factual-event identity. |
| Open policy silently promoted to fact | All 25 register entries remain `TBD — OWNER DECISION`; invariant labels and transition qualifiers preserve historical intent/UI contracts/current observations. No conventional edge or policy inserted. |

No evidence-supported need emerged for stock movement, production batch, executed refund/payment transaction, automatic Task creation or an enforced universal lifecycle. These remain deferred. Conditional cases/attempts/ads/tasks/allocations must not be materialized by guessing.

## Final verification

[verify_domain.py](verify_domain.py) checks ten deliverables, catalog field coverage, entity/policy/invariant references, local links/heading anchors and code-fence balance; it hashes all 154 preexisting protected files against [the pre-write manifest](phase2-baseline-manifest.json). Results are in [verification.json](verification.json). These checks are not proof of business policy correctness. Mermaid diagrams were checked structurally, not rendered by a Mermaid engine.

The chairman checked every accepted critique against the retained Phase 1 profile/documents or labeled it a proposed clarification, then updated only Phase 2 documents. Independent council review covers the first complete draft; final corrections were checked by the chairman/structural verification, not a second council round. Human review remains required. Stop after the canonical domain model.
