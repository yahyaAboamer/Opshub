# Canonical glossary

This vocabulary separates current labels from business meanings. It is a proposed canonical glossary, not a change to immutable Phase 1 terminology. Sources: [domain](../reconstruction/03-domain-model.md), [workflows](../reconstruction/04-workflows-and-state-machines.md), [metrics](../reconstruction/06-calculations-and-metrics.md), [discrepancies](../reconstruction/13-live-vs-spec-discrepancies.md). Entity and policy references resolve to [01](01-entity-catalog.md) and [07](07-policy-decision-register.md).

| Term | Canonical meaning | Existing mapping / ambiguity preserved |
|---|---|---|
| Merchant / Workspace | One explicit merchant-domain ownership boundary (E01) | One Gentry business observed; Workspace is an alias here. Multi-workspace/legal-merchant relationship PD20. |
| User / Operator | Common canonical human/operator account identity (E02), separate from authority context | Merchant participation through E03 and platform participation through E26 can coexist; identity alone grants neither. Historical labels/native account matching remain evidence questions. |
| Merchant Membership / Membership | Operator participation/authority within exactly one merchant (E03) | NEW SAAS; does not imply platform administration or another merchant's authority. Current metadata/duties do not establish an enforced grant matrix. |
| Platform Operator Assignment | Explicit platform-scoped participation/authority assignment to a User (E26) | NEW SAAS; control-plane context, not Merchant Membership. It does not grant unrestricted access by itself; exact platform capabilities/scopes are deferred to PRD/architecture. |
| SaaS control plane | Platform administrative/observational context for Merchant/Workspace records and merchant memberships | Authority distinct from merchant operations; no separate Platform entity or provisioning/onboarding/support lifecycle is introduced. |
| SaaS commercial/billing boundary | Product-boundary concern outside reconstructed Gentry merchant operations | Subscription, Plan, Invoice and SaaS Payment entities are not added here; billing will be evaluated during PRD. Omission is not a no-billing decision. |
| Actor attribution | Independently recorded actual actor, asserted label, recorder/importer and automation origin | `Called by`, manual confirmer and tags can be claims/free text; PD11. |
| Customer | Merchant-local evidenced customer party (E05) | Contacts/phones are observations; repeat-phone indicator does not prove distinct people. PD12. |
| Order | One commercial order identity (E06) | Shopify Name/live internal ID/header; independent of courier tracking and raw line row. |
| Order item | One commercial line within an order (E07) | Shopify lines; live Items summary/Bosta description do not prove line identities/quantities. |
| Shipment / Shipment leg | One independently identified courier consignment (E08) | Bosta tracking. “Leg” preserves transport grain; not invented physical route segments. |
| Delivery | Specify either outbound transport activity, customer receipt, or Delivery order channel | Existing `Delivered` can describe return-leg completion. Never use bare delivery to mean kept conversion. |
| Courier state | Provider's reported consignment state | Delivered/Created/Processing/Terminated etc.; distinct from order outcome. |
| Shipment purpose/type | Provider's consignment classification | SEND/RTO/CUSTOMER_RETURN_PICKUP/EXCHANGE_return; type and state independent. |
| Delivery attempt | One evidenced courier attempt event (E09) | Attempts counter is separately named Reported attempt count; no event chronology proved. |
| Handoff signal | Recorded tag/checkbox assertion that order was handed/booked with courier | `bosta_synced` may exist without matched leg; distinct from Verified booking evidence/physical dispatch. |
| Booking evidence | Evidence identifying an external courier consignment/result | A UI promise, sync flag or approval is not a booking receipt. |
| Return case | One distinguishable return/failure-of-receipt episode (E12), identity partition unresolved | Source labels/legs and current outcomes; not automatically one per order/leg/call. PD18. |
| RTO / never received | Failed outbound receipt/return-to-origin disposition classification | Live Never received (RTO); provider RTO consignment may itself be Delivered. Complete physical chronology PD09. |
| Post-receipt customer return | Customer-side return after receipt under current UI wording | `Received then refused` / historical Customer return. Their exact episode/quantity/cohort equivalence is unproved. |
| Refused | Ambiguous legacy term; use Outbound refusal reason or Post-receipt return outcome explicitly | Courier refusal exception can occur on RTO; current Received then refused denotes post-receipt per UI. A pickup refused exception exists. |
| Exchange return | Exchange-related reverse-goods classification, separate from replacement sale | Historical EXCHANGE_return/live Exchange return; outbound replacement/financial linkage PD17/PD18. |
| Kept | Derived finalized order disposition indicating delivered and retained under named rule | Delivered & kept. Not identical to Bosta Delivered or Bosta-way metric. |
| Pickup | Customer-collection fulfillment process/episode (E13) | Explicit Pickup/90 Office separate from historical inferred no-courier classification. |
| Collected | Physical customer collection **only when appropriately evidenced**; otherwise label source assertion/inference | Historical paid→Collected and Collected(inferred) do not prove physical collection. Live paid/waiting; PD03. |
| Waiting pickup | Pickup collection not established under current selected policy | Payment can be paid. Waiting age is placed-date based in observed live queues. |
| No-show | Governed pickup noncollection disposition, definition unresolved | Workbook voided/refunded classification differs from physical absence. PD03. |
| Contact / call event | One recorded support contact/attempt/assertion (E10) with purpose and provenance | Current contact history/export, quick Called done. Not courier attempt or confirmation failure tag. |
| Contact Intake Summary | One tracking-subject source-row summary of contact state, cumulative support attempts and narrative/classifications | RAW_Intake summary is not Contact Event; Date is not a reconstructed call timestamp. Preserve native counter and legacy/new fields/blanks. |
| Responsibility / trust classification | Governed mapping of cause/exception to a responsibility or reliability category | Product/Courier/Ops/Customer/Unknown or courier trust category; not operator identity, assignee or permission. Preserve original and mapping version. |
| Contact purpose | Reason for contact: predispatch confirmation, return recovery, pickup follow-up or unknown | Current return-contact fields and historical duties; do not assign purpose to ambiguous historical rows by guess. |
| Reached / answered | Source contact-reach assertion under a named definition | Historical Reached versus current ResolvedByCall/Resolved; equivalence is not approved. |
| Call retry eligibility | Projection of contact history and current retry policy | Current two-NoAnswer contract differs from confirmation's three failures; PD05. |
| Last call | Selected contact-history projection | Export value is not the entire event history; selection/chronology policy unresolved. |
| Confirmation | Evidence of intended customer consent to order fulfillment, distinguished from tag-based attribution | Historical consent rule; current tags/manual field. Actual occurrence time and current dispatch guards PD19. |
| Confirmation evidence | One tag/manual assertion observation or separately evidenced consent event (E11) | Never convert tags into invented actual contact/timestamp. |
| Confirmed by | Derived/recorded attribution category | Omar priority; Confirmed+Confirmation Sent→Whapi; other Confirmed→Hadeer. Does not prove actual human/automation action. |
| Resolution | Recorded intended/apparent service disposition, with specific completion domain | Refunded/Re-shipped/Rescheduled delivery/Closed-no-resolution; not universal order/service/financial closure. PD06. |
| Resolved | Ambiguous current/legacy contact label; use Contact completion assertion, Service-action completion, Financial effect, or Issue clearance | These are separate. PD06 must decide each governing predicate. |
| Refund assertion | Recorded claim about refund status | Call Yes/No/Partial or Refunded; amount/payment execution absent. |
| Refund action / transaction | Separately evidenced financial intent/effect; transaction model deferred | E15 can represent action evidence; real monetary transaction identities not reconstructed. PD24. |
| Reship request | Request for linked new commercial order and courier action (E14) | Current form and approval promise; not simply changing original order status. |
| Replacement order | A distinct Order linked to original by typed relationship | Four reship histories. Reship-of/replacement-of/exchange semantics PD17. |
| Reattempt / rescheduled delivery | Continued delivery activity/action potentially on existing order/consignment | Recorded resolution is not proof of a new order or booked consignment. PD17. |
| External business action | One materially consequential intent with independent decision/effect evidence (E15) | Shopify creation, Bosta booking, tag, cancellation/archive/refund effects; no inferred atomic completion. |
| Outcome | Named business disposition projection, with grain and policy | Order outcome differs from source commercial status/consignment state. Null and fallback labels are preserved. |
| Status | Qualified recorded state assertion; always name its dimension/source | Pending/Cancelled/Completed order display, courier state, contact status and financial status are not one machine. |
| Stage | Operational grouping/projection for work progress | With Bosta in transit broad stage contains 29 status-fallback rows beyond 18 transit outcomes. It is not proof of physical location. |
| Product | Merchant merchandising identity (E16) | Shopify Product GID/internal ID versus historical product label. |
| Variant / SKU | Sellable option identity (E17); SKU text is a scoped alias when supported | RAW_SKU variant text/product/size versus uninspected native variant IDs; SKU reuse/uniqueness PD13. |
| Tier | Assigned product classification | New/Scaling/Baseline/Underperformer/Clearance. Suggested tier is a separate recommendation, not auto-assignment. |
| Product-period snapshot | Dated, sourced observation/revision of a product's period data (E18) | Weekly manual row/live CSV aggregate; stock now and rebuild time remain separate. |
| Snapshot revision | Another observation/calculation version of the same logical subject-period/basis | Proposed preservation of overwrite provenance; no fabricated old versions. |
| Logical observation series | Continuity of subject, period, source/basis and measure definition across revisions | Changed definition/period/source scope or manual-versus-calculated kind creates a different series; a same-basis revision is a distinct observation/result. |
| Inventory observation | Quantity assertion with subject/scope/as-of (E19) | Current stock/ending stock/incoming; not stock movement or production batch. |
| Season | Merchant-defined named date horizon (E20) | Summer dates; Now/Upcoming derived; All year is unassigned fallback. |
| Advertisement | Stable external ad identity when evidenced (E21) | Own ads names/keywords alone are not stable IDs. |
| Spend observation | Source measure of spend for specified scope/interval (E22) | Meta incl VAT assertion; native identities/rate/currency unresolved. Not invoice/payment proof. |
| Spend allocation | Derived attribution portion to Product/period (E23) | Own versus generic sales-weighted estimates; collision/zero-sales/daily-week methods PD14. |
| Cost / fee record | One observed/assessed/modeled charge entry with subject/source (E24) | RAW_Costs carrier Order Id means tracking; positive sum selection is historical calculation, not global charge rule. |
| Courier Wallet Observation | Provider cash-cycle/financial-row assertion bundle | COD, online payment, fees/credits/VAT, total/net, payment status/time and cash-out reference retained separately from charges/settled transactions. |
| Cash-out grouping | Source-reported reference grouping financial-row observations | 78 distinct supplied Cash-out IDs; native uniqueness/payment meaning unknown. Not proof of 78 bank payouts or customer refunds. |
| Courier payment status assertion | Provider's recorded Paid/Not Paid label in cash-cycle evidence | Separate from Shopify order payment and customer refund; actual settlement meaning/execution PD24. |
| Unit cost / catalogue margin | Economics input/observation at Product/Variant grain | Catalogue ratio and live product margin differ; not cost already incurred, sales-weighted margin or audited profit. |
| Order value / COD / cash collected | Distinct commercial valuation, courier due-at-delivery amount and actual monetary receipt | A positive number or paid assertion cannot prove collected cash/recognized revenue. |
| Net sales / net cash label | Product-period gross less discounts and return/refund amounts under source definition | Live Net cash is not profit/free cash flow or bank cash. |
| ROAS / breakeven ROAS | Defined spend-return ratio / reciprocal margin input where supported | Current net-sales/allocated-spend arithmetic verified; denominator zero yields blank in sample; policies/edges PD14. |
| Operational exception / issue | Original exception assertion or calculated predicate failure | Courier exception/data-quality/cleanup category; not automatically independently tracked Case/Task. |
| Operational task | Independently authored human work commitment (E25) | Historical action sidecar intent; queues do not prove task creation/history. |
| Queue | Derived membership list under a named predicate/time scope | Calls, Cleanup, New tier; entity identity persists independently of view membership. |
| Source Context | Merchant-scoped source origin with independently qualified native-object namespace (E04) | Evidence artifact/lineage is capture provenance, not automatically native scope. Observed Business ID is a candidate binding, not Merchant/account equivalence. No credentials/infrastructure. |
| Policy / metric definition | Governed rule/version with authority, grain, population, calendar, null handling | Current setting is a configured fact, not owner-approved policy. |
| Bosta way | Existing finalized-order metric `(kept + refused + exchange) / finalized` | 67.8% all-time observed; includes post-receipt returns, not kept conversion. |
| Confirmation coverage | Must name numerator/denominator definition | Historical Hadeer/auto-only versus current all-confirmed; preserve both labels/definitions until PD01. |
| As-of / watermark | Time/boundary describing observation, source completeness or calculation | Sync/rebuild/capture times are distinct; maximum export order date is historical age clock, not TODAY. |

Use these qualified names in future owner decisions. Do not relabel old evidence to imply that a current dropdown, source formula or proposed policy always governed it.
