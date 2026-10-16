# Discrepancies and reconciliation

A verified disagreement does not establish its cause. Sources: [live ledger](../../evidence/live/observation-ledger.md), [workbook findings](../../evidence/artifacts/workbooks/WORKBOOK_FINDINGS.md), [32 source-specific findings](../../evidence/artifacts/text/nonworkbook-analysis.md#contradictions-limitations-and-reconciliation-candidates).

| ID / priority | Evidence and classification | Meaning / required resolution |
|---|---|---|
| D01 High: June completeness | Architecture 358–366/handover versus report P40/state; contradictory artifacts. | Earlier complete/onboarding-office account versus incomplete paginated Bosta export/43% coverage. Obtain matched export scope and pagination evidence; do not select a narrative by date alone. |
| D02 High: inferred pickups | WB current 547 inferred; unequal input windows; inference. | Absence of courier evidence is not collection proof. Shopify begins 1 April, Bosta 20 May. Resolve coverage first. |
| D03 High: pickup completion | Source paid→Collected versus L18 paid pickup waiting 21 days; contradictory. | Confirm explicit physical collection and payment/refund precedence. |
| D04 High: dispatch without courier | L15 handoff flag true versus courier card “not dispatched”; ambiguous dimensions. | Distinguish tag signal from matched booking and inspect its provenance. |
| D05 High: stage/outcome/export | L14/L20: broad transit 47 = 18 transit + 19 Cancelled + 10 Completed; 29 CSV outcomes blank. | Define outcome, status fallback and operational stage; make export interpretation explicit. |
| D06 Medium: pickup exception | UI 44 collected versus CSV 43 Picked up + one pickup Refused. | Potentially physical collection followed by return; inclusion needs confirmation. Delivery refused 40 versus export 41 is reconciled by channel. |
| D07 High: coverage definition | Source Hadeer/auto excludes Omar; monthly/current total-confirmed includes Omar. | Same label, different numerator. Historical comparison requires comparable definitions. |
| D08 High: attribution/time | Source Hadeer/auto conflated; current Whapi from tags; no confirmed_at. | Tags do not prove actor or chronology. Manual confirmer precedence remains unknown. |
| D09 Medium: retries/priority | Source no return retry cap/oldest first; live two-NoAnswer/newest first; review also newest first. | Confirm current policy. Source three-attempt limit belongs to confirmation. |
| D10 High: call chronology/taxonomy | L24: seven call dates precede matching order dates; legacy values absent current forms. | Verified date comparison, cause unknown. Inspect importer linkage/timezone and preserve original vocabulary. |
| D11 Medium: call populations | 102 metric returns, 93 called, queue 32, export 239 events. | Different grains/windows; not automatically incorrect. Export lacks period query; July chart under September order cutoff needs clarification. |
| D12 Medium: cleanup age/export | L22: “10+ with courier/delivered” age uses placed date; export drops low=1. | Clarify age origin and export filter behavior; actual cleanup CSV not verified. |
| D13 High: fees/missingness | Master SUMIF versus monthly last-wins; missing fee→0 versus blank contract. | Static variance; current unique wallet keys mask duplicate-fee issue. Zero/negative actual sums also fall through. |
| D14 High: SEND/partialness | Monthly every SEND delivered; execution-month partialness; partial September in statistics. | Current terminal SEND inputs mask state issue; a later rerun can misclassify stale partial data. No rerun executed. |
| D15 Medium: economic labels | Monthly RTO-only return fees, full order value per RTO leg, all-type attempt mean. | Definitions differ from workbook; do not conflate order/leg/unit rates or financial totals. |
| D16 Medium: target authority | Config [CONFIRM] targets versus firm guide wording; current settings ask owner confirmation. | Configured/proposed is not approved policy. Confirm values, dates and denominators. |
| D17 Medium: weeks/cohorts | Historical Saturday shipment-created versus current Monday placed-order; equal-length partial comparison. | Specify calendar and cohort before performance comparisons. |
| D18 Medium: schema adoption | Stage Bosta incorporated; 13 SKU additions absent; 27 top-ups absent intake; new intake fields blank. | Preparation/schema presence is not adoption evidence. External Sheet may differ. |
| D19 Medium: report reproducibility | Builder does not update state; input JSON absent; archived structure differs. | Exact automated regeneration unverified; preserve output provenance. |
| D20 High: report privacy | Weekly extractor 181 reads pickup customer name despite privacy declarations. | Verified static conflict; this investigation omits contacts from evidence. |
| D21 Medium: product algorithms | Live-only Meta/seasons/tiers/restock. | ROAS arithmetic verified; tier/quantity/allocation algorithms incompletely specified. |
| D22 Medium: progress window | New progress 138 versus all-time 143; inactive cards zero despite historical orders. | Weekly cutoff may explain first; window/conditional display unresolved. |
| D23 Medium: stale copy/navigation | Add order says sync unwired despite markers; Production referenced but no route; START still v2. | Stale text or role/feature gap; current behavior outranks label. |
| D24 Medium: access/audit | Historical duties versus one Omar session, editable caller text, approver named in UI; Phase 1B finds order permission properties and one server login redirect. | Permission vocabulary/one route guard now evidenced; actual RBAC, action/export authorization, audit and tenant isolation remain unresolved. |
| D25 Medium: technical snapshot changes | Phase 1B earlier Calls references 1kudf3dkhdpbd.js, exact public GET 404; fresh Calls references 1t_el1w5uiobt.js, GET 200. Shared assets/public action IDs also vary across observations. | Verified time-scoped mismatch/change; deployment/cache cause unresolved. Do not treat action IDs or chunk URLs as durable API contracts. [Technical evidence](../../evidence/live/phase1b/technical-ledger.md). |

## Reconciled distinctions, not demonstrated defects

- Source 1,635 versus live 1,339 orders have different windows and 768 shared matching dates. All 353 v3 orders match live. Source-only orders span 1 April–1 June, interleaving the live window from 7 May; a simple cutoff is insufficient. No current master overflow exists.
- Product 175 units/136,100 sales became 179/138,800 after the rebuild watermark changed from 13:24 to 18:39. Later UI matches export.
- Current stock 93 versus historical ending stock 98, and all-time orders 143 versus weekly cumulative 138, have different time bases. Graduation's selected basis remains open.
- Historical 212 outbound legs versus 213 orders with any Bosta reference, and 237 legs versus 220 references, are different grains.
- v2's 189 cached #N/A cells suppress empty chart points; no operational formula failure was demonstrated.
- Current fixed item parser matches all present 569 description splits. Length/item/quantity limitations remain unobserved edges.
- Monthly fee overwrite is a static semantic discrepancy; current 1,381 wallet IDs are unique, so current duplicate-fee loss was not demonstrated.

The source-specific register preserves additional role, taxonomy, description and statistical caveats. No discrepancy was silently settled through industry conventions.

Phase 1B resolves the earlier frontend inference to verified delivered Next App Router/React and server-action machinery. It also establishes a product printable HTML route and browser-print implementation. Generic router refresh code does not explain the observed integration watermarks; expected importer feedback does not verify deduplication. The remaining backend/network/refresh gaps are preserved explicitly in [08](08-api-and-integration-observations.md), [10](10-data-ingestion-and-background-jobs.md) and [14](14-open-questions.md).
