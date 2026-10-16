# OpsHub — approved MVP owner decisions

Recorded 14 October 2026. **APPROVED MVP DECISIONS.** Authority: the owner's Phase 3 requests. Phase 1 — System Reconstruction and Phase 2 — Canonical Domain Model are approved and closed; Phase 2.5 — MVP Owner Decisions is approved. The existing Phase 3 PRD is accepted as the baseline; this bounded OD08/OD09 correction awaits review before Phase 3 approval. OD01–OD07 remain unchanged.

**Gentry** means the legacy/internal reconstructed system, including its live behavior and historical evidence. **OpsHub** means the future multi-tenant SaaS product. Historical artifacts, filenames, URLs and evidence labels remain unchanged.

The closed [domain overview](../domain/00-canonical-domain-overview.md) still records its earlier pending approval and uses some earlier future-product naming. This owner instruction supersedes that approval status for Phase 3. It does not rewrite historical documents or retroactively establish Gentry facts. The product package uses OpsHub for all future-product requirements.

## OD01 — Order versus shipment truth

Order/business outcome and courier/shipment outcome remain separate dimensions. Neither automatically overwrites the other. Combined dashboard projections may exist, but the underlying facts remain independent.

## OD02 — Pickup payment versus physical collection

Payment state and physical courier collection state remain separate. Payment does not prove physical collection; physical collection does not automatically determine payment state. The owner's courier-collection wording is preserved. This independence also applies to other supported pickup purposes; it does not equate courier collection with the Gentry merchant/customer Pickup channel. Purpose-specific population and evidence mapping require OP05 review without reopening OD02.

## OD03 — Meaning of resolved

“Resolved” applies to a specific operational case/task. A case is resolved when its required action has actually been completed and no further action is currently required for that case. There is no global “resolved order” status. Attempts exhausted/customer unreachable is not automatically equivalent to resolved.

## OD04 — Default calling policy

MVP default: maximum **3 contact attempts**, approximately **24 hours between attempts**, approximately **48 hours total**. Merchant configuration is later/where product scope permits.

After unsuccessful attempts are exhausted, the case leaves the normal active call queue and becomes an **unreached / attempts-exhausted** outcome. If the customer is reached and an operational action is required, the case remains open until that action is completed. These are contact attempts, not courier delivery attempts. The default covers MVP customer-contact cases, including confirmation and return follow-up.

The exact scheduling tolerance, first-attempt service target and exceptional recontact policy are draft product details in [07](07-configuration-and-policy.md), not additional approved numerical decisions.

## OD05 — MVP KPI semantics

| KPI | Approved definition |
|---|---|
| Confirmation Rate | Confirmed orders ÷ orders that entered the confirmation process |
| Delivery Success Rate | Successfully delivered outbound shipments ÷ outbound shipments with a final courier outcome |
| RTO Rate | RTO outbound shipments ÷ outbound shipments with a final courier outcome |
| Pickup Completion Rate | Physically collected pickups ÷ pickups with a final pickup outcome; pending pickups do not count as failures |
| Call Reach Rate | Customer cases successfully reached ÷ customer cases where contact was attempted |
| Call Action Completion Rate | Cases where the required action was completed ÷ cases that required an action |
| ROAS | Attributed sales revenue ÷ advertising spend |

Call reach and action completion remain separate metrics. Every displayed KPI must explicitly identify numerator, denominator, time window and exclusions. [06](06-analytics-and-kpis.md) supplies draft population, clock and qualification contracts; their unsettled details cannot change these approved formulas.

## OD06 — Order episode cardinality

For the OpsHub MVP: one order has **at most one outbound shipment**, **zero or one return case**, and **zero or one pickup case**. A shipment may contain multiple delivery attempts. A reship/replacement creates a **new order linked to the original**, rather than a second outbound shipment under the original.

An exchange may be represented as original order → return where applicable → linked replacement order → replacement shipment. Multi-shipment-per-order behavior is not introduced into the MVP. This does not erase independently evidenced historical Gentry reverse legs or manufacture individual attempts from an aggregate counter. Ambiguous or incompatible historical episodes need explicit exception treatment.

## OD07 — Consequential merchant actions

Consequential merchant business actions require **Merchant Admin authority**, including order cancellation, reship/replacement approval, shipment booking, refund where supported, and significant operational/economic settings.

Merchant Operators may investigate, prepare or request these actions; they cannot execute them unless a specific future permission model says otherwise. Platform Admin authority does **not** automatically grant merchant business-action authority. Any future platform support override must be explicit, exceptional and audited.

## OD08 — Integrated core operational MVP

OpsHub uses an **integrated MVP**. Critical integrations needed to complete the primary merchant operational workflow are **MUST HAVE — MVP**. The intended loop is **source system → OpsHub → operational decision/action → external system → resulting evidence/status back into OpsHub**.

For supported MVP sources, ingest commerce/order and courier/shipment data, keep operational state sufficiently current, execute essential supported external actions with the correct merchant authority, and receive/reconcile resulting status/evidence where the provider supports it. Phase 1 identifies **Shopify** commerce/products and **Bosta** courier operations for the initial pilot; [08](08-data-ingestion-and-integrations-requirements.md) names their required read/action/result scope and evidence limits. No unsupported provider is invented.

Manual import/export and off-platform execution remain required **fallbacks** for temporary integration unavailability, unsupported provider actions, incomplete onboarding or safe exceptions. They are not the normal workflow for an integrated source. OD07, separate truth, case completion and cardinality remain mandatory. No interface technology, sync architecture, webhook, queue or credential-handling design is selected.

## OD09 — Product performance and ROAS are MVP capabilities

**Product/SKU performance, advertising/product economics and ROAS are MUST HAVE — MVP.** OpsHub must show what products/SKUs sell, product-level sales/revenue, delivery success/RTO/return problems, advertising spend where available, canonical ROAS, relevant-period comparisons, practical underlying-record drill-down and justified attention indicators. Missing/incomplete inputs remain visible; no workbook-layout replication is required.

ROAS remains **attributed sales revenue ÷ advertising spend**, with explicit numerator, denominator, period and missing-data behavior under OD05. Phase 1 identifies **Meta** as the advertising-spend source; integration/input scope and attribution uncertainty are recorded in [08](08-data-ingestion-and-integrations-requirements.md) and [06](06-analytics-and-kpis.md).

Season support is included only as needed for meaningful analysis/classification; richer season-management workflows are **SHOULD HAVE** when basic analytics is coherent without them. Underlying inventory/product observations may be exposed with their time/provenance. Automated replenishment recommendations, production planning and advanced inventory automation remain **post-MVP**.

## Effect on the closed domain decision register

The [Phase 2 policy register](../domain/07-policy-decision-register.md) is retained as the historical question record. The following is the Phase 3 overlay, not a claim that every underlying evidence gap is closed.

| Owner decision | Domain decisions addressed | Residual limitation |
|---|---|---|
| OD01 | PD09 outcome separation | Exact source mappings, legacy summary selection and conflicting assertions still need review |
| OD02 | PD03 payment/collection separation | Accepted collection evidence, refused/partial exceptions and final-outcome mapping remain open |
| OD03 | PD06 completion meaning; PD25 work tracking | Case creation, reopening and action evidence are draft product requirements |
| OD04 | PD05 default retry ceiling/spacing | Gentry's two-NoAnswer rule remains a legacy observation; exact scheduling tolerance is open |
| OD05 | PD01 canonical KPI formulas | Time basis, finality mappings and revenue attribution qualifications still require product approval |
| OD06 | PD09/PD18 MVP cardinality; PD17 replacement order identity | Historical multiple legs/repeated or partial episodes are preserved; unsupported MVP handling is explicit |
| OD07 | PD10/PD11 approval and authority | Eligibility, safe external execution/recovery and support access remain product decisions |
| OD08 | Phase 3 OP01 manual-versus-integrated scope; intended external-action treatment | Integrated core is settled; pilot capability contracts/freshness/result evidence still need qualification, not a return to a manual-primary MVP |
| OD09 | Phase 3 analytics priority and OP09 timing | Product/SKU and ROAS MVP inclusion is settled; attribution/tax/revenue/mapping details remain open; replenishment/production remain deferred |

All other evidence gaps retain their original status. Source completeness, actual historical financial execution and native identifiers cannot be resolved by product approval alone. [13](13-open-product-decisions.md) separates remaining owner choices from evidence questions.
