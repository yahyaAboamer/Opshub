# OpsHub — Product Requirements Document

14 October 2026 · Phase 3 · **Accepted baseline with bounded OD08/OD09 correction for human review.** Phases 1/2 and Phase 2.5 are approved/closed. The owner accepts the prior PRD baseline and approves OD08/OD09; Phase 3 approval awaits this correction. Product requirements only: no Phase 4 architecture, technology or implementation choices.

## Product summary

OpsHub is a multi-tenant SaaS product for online-selling merchant teams to operate confirmation, delivery, returns, pickups and replacement recovery through connected commerce/courier systems, and evaluate Product/SKU performance and ROAS. Its central job remains **what needs attention now**, permitted action and evidence of completion; product analysis helps merchants understand sales, delivery/return problems and advertising economics.

Gentry is the legacy/internal reconstructed system. Its [reconstruction](../reconstruction/00-system-map.md), [canonical domain model](../domain/00-canonical-domain-overview.md) and linked evidence supply the operational knowledge. OpsHub normalizes ambiguous statuses, uncertain inputs and completion semantics rather than copying Gentry's spreadsheet structure or every historical feature. Historical evidence/names remain intact.

## Approved foundations

[Owner decisions OD01–OD07](00-owner-decisions.md) establish separate order/shipment and payment/collection truth; per-case completion; three contact attempts approximately 24 hours apart over 48 hours; explicit canonical KPI formulas; at most one outbound and zero-or-one return/pickup case per order; new linked replacement orders; and Merchant Admin-only consequential business actions. Platform authority never automatically grants merchant operational authority.

OD08 adds the integrated core loop: **source → OpsHub → Admin-authorized supported external action → returned/reconciled result**. OD09 adds Product/SKU performance, available advertising economics and canonical ROAS to MVP. Manual handling is required fallback, not normal connected-source operation; replenishment/production automation remains post-MVP.

Older domain pending-approval labels remain historical snapshots. Document00 records OD01–OD09 and the overlay; source/history is not rewritten. The correction changes these two scope priorities without reopening unrelated owner policies.

## Users and surfaces

Merchant Admin owns merchant settings/members and consequential decisions. Merchant Operator works contacts, investigations, notes and action preparation. OpsHub Platform Admin/Operator provisions and monitors merchant accounts, administrative memberships, source readiness and service/commercial state within assigned scope, without routine customer-record access or business-action execution.

One account identity can participate in both merchant and platform contexts independently. Merchant Application and Platform Control Plane have distinct authority and visible context. [02 Personas/permissions](02-personas-and-permissions.md) defines views, editing, configuration, approval, execution, exports and access recovery.

## MUST-HAVE MVP

| Capability group | Required product outcome |
|---|---|
| SaaS onboarding/access | Verified initial Admin, invitations/memberships, explicit merchant/source context, readiness and activation |
| Operational truth | Orders/items/basic SKU reference, search/filter, independent status/history and one supported outbound/return/pickup episode |
| Daily work | Confirmation/contact queue, due timing, reach/cause evidence, ownership, action-required and exhausted states; focused cleanup |
| Delivery and service recovery | Supported connected booking/cancellation/replacement under Admin authority, shipment tracking, returns/pickups, linked new order and independent per-effect result reconciliation |
| Product/SKU and advertising economics | Period orders/units/revenue, product-associated delivery/RTO/customer-return problems, available spend, canonical ROAS, comparisons, practical drill-down and justified attention |
| Analytics and trust | Six operational KPIs plus ROAS/product contracts with contributors/exclusions/as-of, pending/unknown/missing input and source freshness |
| Input and governance | Required pilot connections, mapping/coverage/readiness and repeat-safe reconciliation; safe manual imports/exports/execution fallback; minimal policies, corrections and audit |
| Platform and commercial shell | Merchant/member administration, aggregate health/support diagnostics, manual plan/subscription/service state, billing Admin contact and nondestructive suspension/reactivation |

The normal MVP supports assisted connection onboarding and an integrated daily workflow. **Shopify** supplies commerce/order/product evidence; **Bosta** supplies shipment/tracking/outcome evidence and qualified booking; **Meta** supplies applicable advertising spend. These are the Phase 1 evidenced pilot sources. [08](08-data-ingestion-and-integrations-requirements.md) defines IG01–IG08 read/action/result targets and qualification limits: Shopify cancellation/replacement/required annotation where supported, Bosta booking/tracking/results, Meta spend read and available analytical observations. UI promises are not proved execution contracts. OP01 qualifies exact account/action support, not whether connections are MVP. [03](03-mvp-feature-prioritization.md) reclassifies core integrations and Product/SKU/ROAS as MUST.

Unavailable integration, unsupported operation, incomplete onboarding or safe exception has explicit manual fallback with reason/Admin authority/evidence and later reconciliation. Unknown earlier effect blocks both re-execution and off-platform execution. Fallback cannot certify a permanently manual core as integrated readiness. No interface/sync/webhook/queue/credential design is chosen.

## Primary merchant journey

Connected order/shipment evidence enters OpsHub → work requiring attention is identified → Operator investigates/contacts customer and prepares action → Admin reviews/authorizes in OpsHub → OpsHub executes qualified connected action → external identifier/status/evidence returns for reconciliation → case closes only under OD03 → outcomes feed operational and Product/SKU/ROAS views. Routine manual copy/paste is unnecessary for the supported core; calling itself can remain external.

All ordinary contact attempts, successful or failed, count toward the three-attempt ceiling; Admin cannot bypass/reset it in MVP. Exhaustion without reach leaves the call queue as unreached; a reached case at the limit keeps unfinished action work open without another ordinary call. Paid does not prove physical courier collection or customer pickup handover; those physical events/populations are identified separately. Courier Delivered does not mean goods kept, and delivered reverse logistics is not outbound success. A replacement creates a new linked order rather than another outbound on the original. Competing execution intents and unknown earlier results block duplicate OpsHub authorization. [04 Merchant workflows](04-merchant-workflows.md) gives goals, entry, alternate paths, states, permissions, attention and acceptance for each daily job.

## Platform administration

Platform staff provision/activate accounts, support verified membership recovery, monitor input readiness/freshness and aggregate queues, maintain manual commercial/service state and inspect scoped administrative history. Support uses redacted diagnostics. Impersonation, contact-level browsing, cross-merchant operational exports and merchant-action override are excluded from MVP. Platform account suspension never destroys merchant operational data or automatically cancels/marks work complete. [05 Platform workflows](05-platform-admin-workflows.md), [09 Commercial](09-saas-commercial-requirements.md).

## Analytics and source trust

MVP delivers Confirmation Rate, Delivery Success Rate, RTO Rate, Pickup Completion Rate, Call Reach Rate and Call Action Completion Rate under OD05. Each value names numerator, denominator, included/excluded population, clock/window, source completeness and as-of with drill-down. Delivery/pickup pending populations are excluded from final-outcome denominators and shown alongside them; call reach and action completion remain distinct.

Product/SKU analytics and ROAS are MVP under OD09. Show orders/units/qualified revenue, distinct product-containing outbound delivery/RTO populations, separately evidenced customer returns, applicable direct/generic/unallocated spend and **attributed sales revenue ÷ advertising spend**. The proposed net-revenue qualification follows Gentry's verified arithmetic but remains explicit policy; incomplete revenue/spend is provisional/unavailable, never silently zero. Multi-product shipment associations overlap, so their denominators are not additive merchant totals; order-level return does not prove every SKU returned. Relevant periods/comparisons, sample counts and practical contributors are required. [06](06-analytics-and-kpis.md) defines K07/P01–P06 and OP09 qualifications.

Use available dated season/classification context only where it supports meaningful analysis; missing context does not block core analytics. Rich season creation/edit/delete/bulk assignment is SHOULD HAVE. Expose sourced stock/cost/margin observations with their own time/basis; no automated replenishment or production engine is required.

OpsHub shows missing/stale/conflicting/partial/unknown/manual/estimated/import-failed data and per-effect unknown results. Retain original references, source and available history; never manufacture events/actors from counters/tags. Corrected working views keep prior claims. Important actions identify merchant, initiating user, time, prior/new state and outcome/evidence. [08 Input/integrations](08-data-ingestion-and-integrations-requirements.md), [10 Audit/trust](10-audit-data-quality-and-trust.md).

## Configuration and commercial requirements

Only expected merchant differences become configuration: identity/connection ownership, timezone/currency, source/item/outcome/ad attribution mappings, revenue/tax/economic basis, qualified freshness and small attention thresholds/taxonomy. OD01–OD07 remain invariant; OD08/OD09 fix core/analytics MVP priority. Calling default and role boundaries are unchanged. Unapproved Gentry targets/fees/tiers do not become OpsHub policy. [07](07-configuration-and-policy.md).

Minimum commercial shell has manual plan/status/effective-period administration, designated billing Admin and visible availability/recovery. Offering/prices and optional trial are **TBD — COMMERCIAL DECISION**. No processor or pricing architecture is selected; sophisticated metering/automatic billing is deferred. Suspension preserves merchant data/history and needs an approved read/export/continuity policy.

## Deferred and excluded

Richer season management/executive briefs and extra read-only personas are SHOULD HAVE. Automated tier/replenishment recommendations, production planning, advanced inventory automation, broad provider marketplace, cost/settlement ledgers, native refunds, repeated/partial episodes, multi-store consolidation, deep BI, automated messaging and sophisticated billing remain post-MVP. Core Shopify/Bosta integrations and Product/SKU/ROAS are no longer deferred.

Multiple outbound shipments per order, arbitrary workflow/report builders, workbook mechanics and platform impersonation/action override are excluded from MVP. Unsupported historical inputs remain explicit exceptions, not silently flattened records. [12 Boundaries](12-out-of-scope-and-future.md).

## Acceptance and success

MVP readiness requires isolated merchant workspaces with qualified core connections, normal connected daily/action/result journeys without routine copying, zero unauthorized connected effects, independent truth, safe exception fallback and attributable audit. Product/SKU delivery/RTO/revenue/spend/ROAS contributors reconcile with visible incomplete inputs and compatible periods. Commercial continuity and later source/definition-qualified Gentry comparison remain required. [11](11-mvp-acceptance-criteria.md) now supplies 15 gates, including AC14 integrated round trip/fallback and AC15 product/ROAS acceptance.

This draft proposes product acceptance outcomes; no product tests have been executed because no application is being built in Phase 3. Pilot speed/volume targets require owner selection rather than invented production guarantees. Business improvement targets need a comparable measured baseline.

## Remaining review decisions and confidence

OD08 resolves manual-versus-integrated scope; OD09 resolves analytics/ROAS inclusion. Remaining OP01 is narrow Shopify/Bosta/applicable Meta account/capability qualification, and OP09 is concrete analytics attribution/revenue/tax/population policy. Unrelated tenant/recovery, consent, contact timing, pickup/finality, replacement terms, metric clocks, source authority, commercial/privacy/retention and pilot targets stay open as before. [13](13-open-product-decisions.md) records them. OD01–OD09 are not reopened.

Confidence is high in evidence-backed distinctions/named sources and approved scope, moderate in integrated/product acceptance completeness pending pilot qualification, and limited in native links/historical coverage/unobserved provider or financial effects. Review this bounded correction for Phase 3 approval; no Phase 4 work begins here.

## Supporting document index

| Document | Detail |
|---|---|
| [00 Owner decisions](00-owner-decisions.md) | Approved semantics and domain-policy overlay |
| [01 Vision/scope](01-product-vision-and-scope.md) | Problems, surfaces, preservation/normalization and boundary |
| [02 Personas/permissions](02-personas-and-permissions.md) | Role expectations and merchant/platform authority |
| [03 Prioritization](03-mvp-feature-prioritization.md) | MUST/SHOULD/LATER/EXCLUDED with reasons |
| [04 Merchant workflows](04-merchant-workflows.md) | Daily jobs and case completion |
| [05 Platform workflows](05-platform-admin-workflows.md) | Provisioning, member recovery, monitoring and service states |
| [06 Analytics/KPIs](06-analytics-and-kpis.md) | Definitions, clocks, populations, exclusions and legacy differences |
| [07 Configuration](07-configuration-and-policy.md) | Small merchant policy set and change behavior |
| [08 Input/integrations](08-data-ingestion-and-integrations-requirements.md) | Shopify/Bosta/Meta scope, connected action/result loop, safe fallback and exports |
| [09 Commercial](09-saas-commercial-requirements.md) | Minimum subscription/service availability shell |
| [10 Audit/trust](10-audit-data-quality-and-trust.md) | Attributable history and uncertainty/privacy |
| [11 Acceptance](11-mvp-acceptance-criteria.md) | Measurable product release conditions |
| [12 Future/boundaries](12-out-of-scope-and-future.md) | Deliberate deferrals/exclusions |
| [13 Open decisions](13-open-product-decisions.md) | Owner choices, evidence gaps and confidence |

Current scope review is in [OD08/OD09 quality review](../../evidence/product/od08-od09-quality-review.md); the [earlier review](../../evidence/product/quality-review.md) is retained as historical evidence. **Stop for human review after this corrected PRD.** No Phase 4 architecture, technical stack, schema, API design, infrastructure, implementation plan, code or migration implementation follows in this task.
