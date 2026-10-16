# OpsHub — analytics, contributors and revisions

**Recommendation:** indexed PostgreSQL transactional queries for fresh detail/backlog, plus tenant-keyed revisioned projection tables for metric/product results and reproducible contributor drill-down. No warehouse for MVP. [ADR008](adr/ADR-008-analytics.md). [OD05](../product/00-owner-decisions.md) formulas and [K01–K07/P01–P06](../product/06-analytics-and-kpis.md) are authoritative. Proposed clocks/mappings/methods remain OP07/OP09 launch choices, not changed formulas.

## Alternatives and publication

| Option | Decision |
|---|---|
| Transactional queries only | Adequate for details/small cohorts; expensive repeated joins and historical-as-of export need retained interpretation versions |
| Projections/materialized views | Recommended relational projection **tables** with generation/contributor identity and RLS. Ordinary materialized views do not automatically provide safe tenant access or retained history; use reviewed invoker views over protected projection tables |
| Analytical store/warehouse | Deferred; replication/CDC, security, cost and cross-store freshness outweigh unmeasured pilot benefit |

Each ingestion/correction changes monotonic `tenant_revision` and records material working interpretation revisions. Worker reads a consistent revision/definition/policy snapshot, calculates results and contributor records, and atomically publishes a generation. Do not update ratios before their contributors. A query reports `as_of`, input revision, generation, coverage and computation time separately. Later evidence makes a new revision, leaving retained exports/selected snapshots explainable. Generation data includes scalar state/amount/basis and evidence references needed to reproduce it; current-state drill-down cannot replace old contributors.

Direct operational queues evaluate current time so delayed projection jobs cannot hide due work. Read models never execute domain commands. Dirty-subject/cohort recomputation is sufficient; no streaming engine is needed. Initially retain requested/exported generations plus bounded recent operational results under 11; do not store every minute indefinitely.

## Operational KPI calculations

| KPI | Numerator / denominator, grain and proposed cohort | Required exclusions and preserved populations |
|---|---|---|
| Confirmation Rate | Distinct currently affirmative Orders / distinct Orders with evidenced confirmation-process entry; first entry cohort | Never-entered, unknown entry/date, duplicates/unmatched separate; pending/declined/exhausted participants remain denominator. Withdrawal revises affirmative interpretation without erasing entry |
| Delivery Success Rate | Distinct accepted outbound shipments with mapped final recipient delivery / distinct accepted outbound shipments with known final courier outcome; shipment-created cohort | Pending, unknown/conflicting/unmapped and reverse legs separate; cancelled-before-booking Order is not a shipment. Later customer return cannot erase courier delivery |
| RTO Rate | Final RTO outbound / **same final-outbound denominator/cohort** as delivery | Separate reverse delivery alone cannot prove original RTO; final-other count means delivery+RTO need not sum100% |
| Pickup Completion Rate | Physically collected pickup cases / pickup cases with known final pickup outcome; case-entry cohort | Name purpose population (customer handover/courier collection); pending/unknown/partial/repeated/inferred separate. Payment never defines collection/finality |
| Call Reach Rate | Distinct customer-contact cases with evidenced reach / distinct cases with actual contact attempted; first-attempt cohort | Confirmation/return/pickup purpose breakdown; no-attempt/admin-only/uncertain summary separate. Repeat attempts do not inflate cases; later failure does not erase reach |
| Call Action Completion Rate | Distinct contact cases with all required actions/evidence complete and no remaining action / distinct cases explicitly requiring action; first-action-required cohort | Pending approval/unknown/failed/exhausted/unattempted action-required cases remain denominator. Removing obligation requires attributable correction/cohort qualification |

Persist member flags/reasons per contributor rather than a hidden denominator. Different clocks are displayed in listings rather than silently substituted for cohorts. Missing dates enter an undated diagnostic population. OD04 contact-attempt usage is different from courier attempt counters and different from case denominators.

Call contributors use the canonical confirmation/return/pickup case identity in 04. Each contact case has at most one objective; reopening, repeated attempts, imported labels and derived attention entries cannot create another case denominator. A pre-call reservation is authorization/held budget, not evidence of an actual attempt or reach. Ambiguous imported case links are diagnostic exclusions. These identity rules preserve K05/K06 without redefining their approved formulas.

## Product/SKU analytical grain

P01 sales: distinct product-containing Orders, sum evidenced line quantities, and qualified **item** sales/discount/reversal values. Order totals are not copied onto every item/product. Repeated same-variant lines remain distinct. Product presence counts are distinct at Product level, not sum of SKU presence counts. Item amounts/units add across known nonoverlapping lines with explicit unmapped balance.

P02 delivery/RTO: restrict K02/K03's distinct outbound membership to Orders with evidenced Product/SKU items. A shipment containing A+B belongs once in each respective Product cohort; product rates overlap and are not additive merchant totals or individually delivered units. Unknown item membership remains diagnostic. P03 customer returns are separately evidenced case/order associations; an order-level return cannot establish each SKU's returned quantity or causal blame. Item return quantities only appear where evidenced. No return-rate label is added without OP09 denominator policy.

P04 advertising economics: use compatible period/currency/tax/source basis, direct allocations and approved generic portions plus visible unallocated remainder. Account/ad/campaign totals are alternative aggregation levels; select one nonoverlapping source grain, not their sum. Product spend is not copied to each SKU. SKU ROAS is unavailable absent qualified SKU spend attribution. Sourced costs/margins are dated assumptions/context, not incurred profit or settlement.

P05 comparisons require compatible definition/grain/method/currency/timezone, equal-length or clearly qualified intervals, retained input revision and completeness. Report absolute changes/percentage points/count denominators; zero comparison denominator → N/A. Current stock/season cannot fill dated historical context. Minimal sourced season/classification context filters analysis when available; no rich season workflow/production planning dependency. P06 attention names predicate/period/sample/approved threshold; without threshold, show values/quality/rank for review without fabricated High/Scaling labels or causal claims.

## Canonical ROAS

ROAS is **attributed sales revenue / advertising spend**. Proposed named qualification is net attributed sales: item gross less assigned discounts and recognized return/refund sales reversals, counting one evidenced reversal once. This is not Meta's reported purchase-ROAS field, cash collected, profit or courier COD. Use Shopify revenue evidence and applicable Meta spend, with explicit approved attribution mapping; name/keyword matching is at most a candidate, not a definitive native product link.

Every allocation run fixes source spend revision, method/version, target period/product, currency/tax basis, weights and portions. Sum direct+generic allocated portions+unallocated balance equals selected source amount at declared precision; deterministic remainder handling is OP09. Do not add generic parent total to its own portions. Collision/zero-sales/unknown product cases remain unallocated unless an approved method governs them. Negative evidenced sales adjustments stay labeled; no FX conversion, VAT uplift or last-year fee constant is invented.

**Revenue attribution is a separate contributor selection contract.** For each qualified item/order revenue amount, retain the approved method/version, eligibility basis/source references, attributed amount/target and unattributed balance. Product membership or ad-to-product spend mapping alone does not make all sales attributed. OP09 may approve a supported product-period or source-linked attribution method, with its meaning visibly named; it does not imply click-level attribution. Attributed plus unattributed amounts reconcile to the selected eligible revenue base; reversals follow the same approved recognition/allocation basis once. Missing/unapproved revenue eligibility leaves K07 provisional/unavailable, even when spend allocation is complete. Reuse `metric_contributors` where sufficient; no generic attribution engine is required.

Preserve provider account timezone and reporting grain. If daily provider aggregates cannot express a requested merchant-local interval exactly, choose an approved compatible window or qualify/withhold the comparison; never apportion days or shift dates silently. Exact policy remains OP07/OP09.

Recent report windows are repeatedly read under a **proposed** bounded lookback configurable to qualified reporting behavior; no Meta finality/maximum revision horizon was verified. Closed-period refresh is supported on demand and on agreed reconciliation schedule. Each refresh appends changed spend/revenue interpretation; finalized-looking periods can become provisional on new conflicting/late inputs.18 distinguishes documented report fields from account/attribution uncertainty.

## Display and reproducibility contract

Every metric result includes definition/version, subject/grain/cohort/window/timezone, as-of/input revisions, numerator/denominator or monetary/count contributors, exclusions by reason, pending/unknown counts, coverage and complete/provisional/unavailable/N/A state. Zero denominator/spend → N/A; missing input → unknown, not zero. Complete positive spend with evidenced zero revenue can yield0; unknown subject/denominator produces unavailable; calculable known subset is provisional. Export preserves the identical generation and precision-before-rounding result.

Architectural test oracles from AC07/AC15: confirmation6/10=60%; delivery3/5=60%, RTO1/5=20% with pending2/unknown1; collection2/4=50%; reach3/5=60%; action completion1/5=20%; qualified revenue 20,000/spend 5,000=4.0. S1(A+B delivered), S2(A RTO), S3(B delivered) produce A: 1/2 delivery, B: 2/2 and merchant 3 shipments, not summed 4. Product A two-SKU presence remains 2 Orders/shipments while evidenced units 6 and item revenue 20,000 add. These are planned fixtures, not executed application tests. [14](14-testing-strategy.md).
