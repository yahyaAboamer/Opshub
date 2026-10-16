# OpsHub — product vision and scope

14 October 2026 · Phase 3 · **Accepted baseline with bounded correction for review.** [OD01–OD09](00-owner-decisions.md) are approved. Requirements describe OpsHub product behavior, not implemented capabilities or verified Gentry enforcement.

## Product and problem

OpsHub helps an online-selling merchant operate orders from ingestion through confirmation, delivery/pickup, return follow-up and linked replacement. Its daily question is **“What needs my attention now, who can act, and what proves the action finished?”** Reliable operational truth, explicit authority and trustworthy metrics take precedence over replicating every Gentry report.

Gentry evidence shows useful daily order lookup, call and cleanup queues, shipment summaries and replacement links. It also shows disconnected payment/physical states, mixed status meanings, uncertain source coverage and contact labels that do not prove action completion. See [features](../reconstruction/02-feature-inventory.md), [workflows](../reconstruction/04-workflows-and-state-machines.md), [discrepancies](../reconstruction/13-live-vs-spec-discrepancies.md) and the [domain model](../domain/00-canonical-domain-overview.md). These are evidence-backed needs; the SaaS shell is a new product requirement.

## Two surfaces

| Surface | User job | Product boundary |
|---|---|---|
| OpsHub Merchant Application | Work the merchant's daily operations, inspect history, request/approve actions, review outcomes and data quality | Explicit merchant context; operational data belongs to that merchant |
| OpsHub Platform Control Plane | Provision and monitor merchant accounts, memberships, readiness, service issues and commercial standing | Platform authority permits the defined administration/diagnostics; it does not confer merchant business-action authority |

## Smallest coherent MVP

The MVP is an integrated operational product under OD08. For the initial Shopify/Bosta pilot, source data enters OpsHub, users work attention and authorize supported actions, OpsHub executes through the connected provider, and resulting identifiers/status/evidence return for reconciliation. Assisted onboarding and manual import/export/off-platform execution are safe fallback paths when connection/action capability is unavailable; routine copying is not the intended connected-source workflow. Approval or a provider request acknowledgement cannot substitute for completed action evidence.

Merchant users need orders/items and trustworthy source links; a confirmation/contact queue; outbound tracking and exceptions; return and pickup cases; integrated supported booking/cancellation/replacement with Admin authority; focused cleanup; operational and Product/SKU dashboards; advertising-spend/economics and ROAS; scoped exports, history and small merchant configuration. Platform users retain account/member administration, source readiness/freshness monitoring and manual commercial state. See [03](03-mvp-feature-prioritization.md).

Under OD09, Product/SKU performance and ROAS are MVP decision tools: sales/revenue, product delivery/RTO/return behavior, available spend, period comparison, practical drill-down and data-quality attention. Shopify product/order evidence, Bosta outcomes and Meta spend are the named pilot inputs. Basic source season/classification context is used when needed for analysis; missing season does not block core analytics. Rich season management is SHOULD HAVE. Automated replenishment/production planning remains post-MVP.

## Preserved versus normalized

| Gentry evidence | OpsHub treatment | Source / certainty |
|---|---|---|
| Order lookup, filter/drill-down, call history and focused cleanup | PRESERVED daily jobs; complete scoped access to the relevant population | Verified UI, L02–L04/L14/L22–L24 in [ledger](../../evidence/live/observation-ledger.md) |
| Commercial status, courier type/state, handoff and customer disposition coexist | NORMALIZED independent dimensions and named projections under OD01 | Verified examples L15–L18; [domain states](../domain/04-state-machines.md) |
| Paid/no-courier historical pickup inference | Preserve as labeled historical inference; never physical collection truth under OD02 | Verified contradiction D01–D03; collection cause remains unresolved |
| Called done / two NoAnswer removal | Normalize to per-case reach, work completion and three-attempt OD03/OD04 | Verified UI contract, unexecuted; not a proven closure mechanism |
| Replacement original→new-order links | Preserve linked new order; Admin decision and separate action results | L05/BR18 is observed history and UI promise; external enforcement unverified |
| Fixed workbook ranges, named staff, inconsistent metric formulas | EXCLUDED as product constraints; retain historical semantics for comparison | [mapping](../domain/08-reconstruction-to-canonical-mapping.md), D07/D13–D17 |
| Human report quality gates and review before forwarding | Preserve data caveats and reviewed summaries; automated sending deferred | BR16/BR24 historical intent/current wording, not proved enforcement |
| One Gentry operation; no verified tenant/control plane | NEW SAAS merchant isolation, memberships and separate platform administration | [domain I01/I27](../domain/05-domain-invariants.md); not a legacy feature claim |

## Assumptions and limits

The MVP addresses one coherent order episode under OD06. It does not need multi-store consolidation, partial return execution, repeated pickup episodes or logistics routing to be usable. Those flows cannot be silently flattened when encountered in imports. Proposed commercial and onboarding boundaries require owner review before release.

Source-specific identity, final-outcome and product/spend mappings must be approved for the pilot. Historical missing coverage and actual Gentry mutation behavior remain evidence questions. [08](08-data-ingestion-and-integrations-requirements.md) distinguishes evidenced input, intended action targets and unsupported/unknown provider capability. Integration readiness must demonstrate the supported round trip before release; an unverified action remains unavailable/under review with a safe fallback, never a silently promised automation. Manual fallback records Admin authority, exception reason and usable result evidence.

## Success and review boundary

Two isolated pilot merchants must be able to connect supported sources, work due cases, authorize/execute supported actions in OpsHub, reconcile external results, use safe fallback during exceptions and reproduce operational/Product-SKU/ROAS results from their contributing populations. Detailed gates are in [11](11-mvp-acceptance-criteria.md); remaining pilot/policy choices are in [13](13-open-product-decisions.md).

This phase stops at the product PRD. It chooses no technology, implementation architecture, schema, interface technology, infrastructure or implementation plan.
