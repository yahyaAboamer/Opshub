# Open domain questions, confidence and owner review

The [decision register](07-policy-decision-register.md) preserves policy choices. This document separates conceptual identity blockers from remaining evidence gaps. It does not reopen Phase 1 or authorize further production experiments.

The owner accepts the existing model subject to the bounded platform-operator distinction. E26 Platform Operator Assignment now supplies that NEW SAAS boundary. The unresolved questions below are preserved records, not a request to reopen unrelated Phase 2 decisions.

## Five highest-risk unresolved questions

1. **Which KPI definitions are authoritative, and from when?** PD01. Confirmation/courier/pickup/call metrics differ in grain, population, calendar and numerator. Wrong normalization could make historically incomparable results appear equivalent.
2. **Is June courier history complete, and which omissions are intentional?** PD02. The contradictory coverage narratives plus mismatched source windows can create false inferred pickups and incomplete costs. Completeness requires evidence; no owner preference can establish missing physical events.
3. **What proves physical pickup collection or a no-show?** PD03. Paid+waiting and the refused-pickup exception make payment-derived completion unsafe. Clarify partial collection, return-after-collection, cancellation/refund precedence and age clock.
4. **Which source wins for each concept, and how do manual overrides/corrections affect history?** PD08. Without this, normalized tags, snapshots, product economics and financial inputs can lose valid conflicting history or claim a false current truth.
5. **How do multiple shipments, returns and pickups form distinct business episodes and outcomes?** PD09/PD18. Current summaries/legs/calls do not prove case identity, partial item flows, chronological precedence or consolidated shipment cardinality. This affects entity identity, not just UI labels.

## Identity/grain blockers versus containable policy

| Question | What remains blocked | What can be modeled now |
|---|---|---|
| Return/pickup episode partition / partial quantities (PD18) | Automatic case creation/merging and definitive item allocations for ambiguous history | Independent Orders/Legs/Contacts/source assertions and proposed case vocabulary; retain unresolved links. |
| One primary order per consignment / consolidated multi-order flow (PD09) | Enforcing provisional Leg→Order cardinality on unproven cases | All consignment identities and observed business refs; association can remain unresolved. |
| Merchant/source namespace (PD20) | Cross-merchant source binding/account sharing/multi-workspace identity | Single Gentry ownership context; first-class merchant model proposal. |
| Customer/variant/call event crosswalk (PD12/PD13/PD16) | Irreversible merge, invented variant mapping, definitive import dedup/linking | Merchant-local unknown links, original labels/row locators/contact snapshots/summary history. |
| KPI/retry/threshold/economic/advice policy | Selecting approved current projection results/enforcement | Separate facts/projections, named legacy/current definitions, input provenance and owner-decision placeholders. |
| External action/financial evidence (PD10/PD24) | Claiming execution/atomic success, monetary transaction identity or approved retry recovery | Intent, approval, known result identities and unknown per-effect consequences. |

Unknown entity instance identity does not invalidate the distinction between business concepts. It does prevent inventing instances from convenient spreadsheet/UI groupings. No SQL/key/constraint implementation is proposed to settle these choices.

## Evidence questions beyond owner preference

| Area / question | Evidence needed / limit | Model references |
|---|---|---|
| External IDs and memberships | Authorized native store/customer/variant/ad/call IDs and legitimate role/account metadata; RAW_Costs Business ID observation already exists, but its account/Merchant boundary is unverified; current baseline only one operator session | PD11–PD13/PD16/PD20; E02–E05/E07/E17/E21 |
| Multi-leg state selection | Authoritative outcome/link policy or approved nonproduction chronological/split cases; current samples do not establish every branch | PD09/PD18; E08/E12/E13 |
| Actual contact/time/import behavior | Redacted source rows/import rules for seven date anomalies, dedup, legacy mapping and caller provenance | PD05/PD16/PD19; E10/E11 |
| Pickup physical evidence | Collection record/event and exceptional/partial examples; paid and no-courier assertions insufficient | PD02/PD03/PD18 |
| Reship/financial effects | Approved nonproduction request/approval/duplicate/partial-failure results and finance receipts; no production booking/refund/cancel test authorized here | PD10/PD17/PD24; E14/E15/E24 |
| Courier wallet semantics | Existing monetary/payment/cash-out fields are retained, but their actual settlement/net/component/reuse contract needs authoritative clarification; 78 IDs do not prove 78 payments | PD07/PD20/PD24; Courier Wallet Observation/E24 |
| Product/ad/stock inputs | Native stock/ad scopes, matching/zero-sales/VAT/currency methods, incoming/minimum-batch source and revision/as-of contract | PD13/PD14/PD21/PD23; E16–E23 |
| Source authority/history | Current override/update/retention contract, old economics validity, explicit cohort exclusions and temporal policy approvals | PD01/PD02/PD07/PD08/PD21/PD22 |
| Independent work records | Current task/exception-case material or concrete authored sidecars; queues are insufficient | PD25; E25 |

Prefer owner-provided authoritative materials, approved read-only source/log evidence and legitimate additional-role inspection. Any future materially consequential experiment must be separately authorized; Phase 2 performs none.

## Confidence assessment

| Area | Confidence in this model / practical limit |
|---|---|
| Order/line/leg/contact/product-period grain separation | **High**: direct source schemas/counts, multiple legs and event export; entity distinctions firmly supported. |
| Facts/assertions/projections/actor/currency/time distinctions | **High** as canonical preservation principles; not evidence that current application enforces/retains all provenance. |
| Proposed canonical entities and tenant boundary | **Moderate**: coherent merchant model and normalization grounded in evidence; Source Context units/native account crosswalks and case identities remain documented questions. E26 platform authority is an owner-required NEW SAAS distinction, not a verified current-system feature. |
| Customer/variant/native identity and relationship crosswalks | **Limited**: native keys/uniqueness/link rules not reconstructed; safe unknowns preserve gaps. |
| Return/pickup case partition and partial quantity flows | **Limited**: first-class concepts justified, actual episode grain/materialization unresolved. |
| State transitions, retry/closure/approval and financial execution | **Limited**: historical intent/current UI contracts plus sample histories, no executed transitions/current backend truth. |
| Product/ad allocation/replenishment policies and source finality | **Limited** beyond verified ROAS arithmetic and UI inputs; algorithms/authority/edge cases unresolved. |
| Historical mapping/provenance preservation | **High** for documented sources/grains/known disagreements, including wallet/intake observation bundles; **limited** for unretained events/revisions and unavailable native identity crosswalks/backend evidence. |

No numerical confidence score implies measured probability. Evidence-backed distinctions can be high-confidence while a proposed lifecycle/cardinality is unresolved.

## Deferred platform and commercial boundary

The canonical identity distinction is explicit: User/Operator is the account concept; Merchant Membership represents authority in one merchant; Platform Operator Assignment represents authority in the SaaS control plane. Neither context implies the other. Platform operators may administer/observe Merchant and Membership records under separately defined authority without becoming members of every tenant. Identity alone never permits cross-merchant access.

Exact platform roles/permissions, super-admin capabilities, support impersonation, delegated access and access-control implementation are deferred to PRD/architecture. Provisioning, invitation, suspension, merchant onboarding, deletion and support-access workflows are deferred to the PRD; none is an added Phase 2 lifecycle.

Subscription, Plan, Invoice and SaaS Payment entities are not introduced. SaaS commercial/billing concepts lie outside reconstructed Gentry merchant operations and will be evaluated during the PRD/product-boundary phase. Their absence here does not decide that billing will be absent from the product.

## Review request and completion boundary

Review is limited to the E26 addition and its identity/authority distinction in [01](01-entity-catalog.md), [02](02-identities-and-relationships.md) and I27 in [05](05-domain-invariants.md). The accepted model and existing policy questions otherwise retain their prior semantics. Phase 2 approval is not assumed from this correction.

[Quality review](../../evidence/domain/quality-review.md) records the earlier council review, which predates E26. The current [verification](../../evidence/domain/verification.json) checks the corrected document set/counts and unchanged Phase 1 baseline. Stop here: no PRD, target architecture, technology, schema, API, frontend/backend, or migration implementation is authorized.
