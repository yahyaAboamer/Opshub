# OpsHub OD08/OD09 — bounded correction review

14 October 2026. The owner accepts the current PRD baseline, approves OD08/OD09 and requires their incorporation before Phase 3 approval. This record covers that correction only. [Current PRD](../../docs/product/14-prd.md) remains for human review; Phase 4 is not begun.

## Changed product documents

All 15 existing product documents were reviewed. 14 changed; document 09 commercial requirements remains unchanged against the [accepted pre-correction baseline](od08-od09-baseline-manifest.json).

| File | Material reason for correction |
|---|---|
| [00 Owner decisions](../../docs/product/00-owner-decisions.md) | Approved OD08/OD09 and baseline status; existing OD01–OD07 sections retained |
| [01 Vision/scope](../../docs/product/01-product-vision-and-scope.md) | Integrated normal loop and analytical MVP |
| [02 Personas/permissions](../../docs/product/02-personas-and-permissions.md) | Connected Admin execution, product view and significant analytics/connection configuration authority |
| [03 Prioritization](../../docs/product/03-mvp-feature-prioritization.md) | Core connections/Product-SKU/ROAS MUST; analytical versus richer season scope |
| [04 Merchant workflows](../../docs/product/04-merchant-workflows.md) | Connected onboarding/input/action/result, safe fallback and WF11 analytics |
| [05 Platform workflows](../../docs/product/05-platform-admin-workflows.md) | Connection/capability and analytics-input health, same redacted authority |
| [06 Metrics](../../docs/product/06-analytics-and-kpis.md) | K07 MVP and P01–P06 product population/time/provenance contracts |
| [07 Configuration](../../docs/product/07-configuration-and-policy.md) | Applicable integrated freshness/analytics policy, source season context; no automated planning |
| [08 Connections](../../docs/product/08-data-ingestion-and-integrations-requirements.md) | Named Shopify/Bosta/Meta capabilities, evidence limits, connected action and safe fallback |
| [10 Trust/audit](../../docs/product/10-audit-data-quality-and-trust.md) | Admin initiation versus OpsHub/provider execution, fallback and required analytics trust |
| [11 Acceptance](../../docs/product/11-mvp-acceptance-criteria.md) | Integrated normal jobs, AC14 round-trip/fallback, AC15 product/SKU/ROAS/period fixtures |
| [12 Future scope](../../docs/product/12-out-of-scope-and-future.md) | Remove obsolete core/analytics deferrals; retain advanced/financial boundaries |
| [13 Decisions](../../docs/product/13-open-product-decisions.md) | Resolve manual-vs-integrated and analytics priority; narrow OP01/OP09, preserve unrelated choices |
| [14 PRD](../../docs/product/14-prd.md) | Cohesive integrated/product MVP summary and current review status |

The documentation verifier was extended for nine decisions, 11 merchant workflows, 15 acceptance gates and OD08/OD09 classification/provider/contract checks. This is analysis tooling, not application code. Original source, reconstruction/domain and linked pre-existing evidence remain protected by the original 170-file baseline.

## Provider and product boundary

Phase1 evidence names Shopify commerce/products, Bosta shipment state/booking intent and Meta spend. IG01–IG08 distinguish recorded observations/UI promises from intended OpsHub targets and unverified support. Required core connects order updates → Admin-supported action → resulting order/tracking/status evidence. Normal integrated operation needs no repeated copy/paste; exact unsupported actions use recorded exception fallback.

No claim is made that Gentry mutations or provider contracts were tested. Native refund/settlement, arbitrary payment changes, unqualified courier initiation/rescheduling and campaign/budget control are not silently promised. Meta spend applies where used/available. Cost/margin/snapshots identify actual provider or merchant-maintained origin, not assumed Shopify retrieval.

Product/SKU orders/units/qualified revenue, shipment-associated delivery/RTO, customer-return association, spend/ROAS and comparisons/attention are MUST. Product-presence populations overlap; item revenue is additive only through evidenced allocation. Missing/incomplete revenue/spend remains unavailable/provisional with caveat. Basic analytical season context is conditional MVP; rich management SHOULD. Automated replenishment/production remains post-MVP.

## Targeted council and incorporated findings

Three independent reviewers and two fresh blind peer reviewers challenged only OD08/OD09 consistency. [Independent findings](od08-od09-council-stage1.md), [peer ranking/synthesis](od08-od09-council-stage2.md). Same inherited model; no cross-vendor/provider call. Both peer rankings C>B>A; average1/2/3. All reported no blocker; existing release qualifications remain meaningful unknowns.

| Finding | Bounded disposition |
|---|---|
| IG06 could imply Shopify cost/margin retrieval was verified | Distinguish connected identity/item/qualified inventory from actual-source/attributed merchant economic/snapshot input |
| Fallback negative evidence too implicit | FB02/AC14 require known not-started or qualified reliable no-effect; timeout/absence/failed refresh never proves nonexecution |
| SKU aggregation/comparison acceptance too implicit | AC15 adds shared-SKU distinct order/shipment counts, additive unit/revenue, no copied product spend, complete-period differences and incomplete/method-change caveats |
| Prior quality review described obsolete manual scope | Marked it explicitly historical; current correction has this review and current verification |

No unrelated owner decision, role, contact policy, episode cardinality, commercial choice or architectural mechanism was reopened. Unresolved provider/action support, attribution/revenue/tax/mapping/freshness and existing pilot/privacy/commercial choices remain in13.

## Consistency and verification

Targeted search and manual review covered all15 documents for deferred-core integration/product/ROAS statements, primary off-platform execution, accidental default fallback and selected architecture. Remaining SHOULD/LATER statements concern rich seasons, advanced planning/finance/BI/marketplace, messaging and billing, or clearly preserved historical evidence. No language/framework/database/cloud/API/webhook/queue/credential design was chosen.

The existing [verifier](verify_documents.py) passed after correction: **15 product documents, 102 valid product links/anchors, no Markdown/naming errors, all OD08/OD09 checks passed, document 09 unchanged and all 170 original protected files unchanged**. [Latest results](verification.json) include corrected document hashes/list. These are document/provenance checks, not executed product/provider tests.

Stop after the corrected PRD for human review. No architecture, implementation plan, application code, migration or live external effect is part of this task.
