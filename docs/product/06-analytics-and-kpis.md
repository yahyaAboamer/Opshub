# OpsHub — analytics and KPI contracts

**Draft population/time contracts; OD05 formulas are approved.** [Gentry calculations](../reconstruction/06-calculations-and-metrics.md), [discrepancies](../reconstruction/13-live-vs-spec-discrepancies.md) and [domain projection contracts](../domain/03-events-and-projections.md) preserve legacy definitions. Do not copy a metric merely because its label matches.

## Display contract for every KPI

KPI01 — Display business meaning, numerator/denominator counts, population/grain, time basis and interval, exclusions/unknowns, source coverage, definition version and calculated/as-of time. A compact visible explanation may link to full contributing records; the value must never appear without its denominator/window qualification. Export carries the same contract.

KPI02 — Zero denominator is **N/A**, never 0% or 100%. Missing input is not zero. Distinguish zero measured activity, partial period, pending final outcome, incomplete source coverage and unresolved mapping. Ratios are computed from unrounded counts/amounts, with presentation rounding only.

KPI03 — Proposed merchant-local calendar: daily/calendar month/custom intervals and Monday–Sunday week; interval boundaries and timezone always named. A current partial week is compared only against an explicit equal-length prior interval, or against a labeled complete period with warning. This calendar/cohort choice is OP07, not part of the approved OD05 formula.

KPI04 — Cohort dates and as-of dates differ. Late outcomes/corrections can revise a cohort's rate; retained/exported summaries identify as-of and input revision. Ageing/backlog uses current merchant time rather than a stale export's last date; imported date-only/unknown-zone values retain precision uncertainty.

KPI05 — For known population with some pending outcomes, display the final-outcome ratio plus pending/unknown counts. If source completeness is unknown or unmapped records could change numerator/finality, label the known-population result **provisional** with uncovered count/unknown coverage; never call it merchant-wide performance. If the subject population or denominator cannot be reliably formed, withhold the ratio as **unavailable** and show reasons.

## Required MVP surfaces

| Surface | Required content / drill-down |
|---|---|
| Attention / daily operations | Due/overdue contact, approval waiting, reached/action incomplete, failed/unknown external results, unbooked orders, waiting pickup and data-quality work; dates do not silently remove backlog |
| Operational outcomes | Confirmation Rate, Delivery Success Rate, RTO Rate, Pickup Completion Rate; counts of eligible/confirmed, final/pending/unknown outbound and final/pending/unknown pickup |
| Contact and action | Call Reach Rate and Call Action Completion Rate separately; attempted/reached/unreached/exhausted/action-required/completed/backlog counts, distinct cases versus attempt-event counts |
| Trust / source freshness | Coverage periods and as-of by source, rejected/unmatched/conflicting rows, data age, input versus outcome completeness |
| Platform monitoring | Merchant-level readiness/freshness/issue aggregates and service state; no routine customer-level drill-down |

Product/SKU performance, advertising/product economics and ROAS are **MUST HAVE — MVP** under OD09. The merchant Product/SKU surface below complements the six operational metrics. No unapproved Gentry targets/tier algorithms become success criteria. Ingested economics/stock observations are analytical context, not profit, settlement or replenishment automation.

## K01 — Confirmation Rate (MUST)

- **Meaning:** fraction of orders participating in confirmation whose current reviewed confirmation state is affirmative at the chosen as-of.
- **Numerator:** distinct confirmed orders in the included confirmation cohort. Source-confirmed evidence is identified as source assertion; new manual confirmation records actual evidence/actor/time.
- **Denominator:** distinct orders that entered the confirmation process. One order counts once, even with multiple contacts or a reopened confirmation task.
- **Included:** valid merchant orders with an explicit or evidenced process entry; affirmative, pending, declined and exhausted participants all remain in the denominator.
- **Excluded:** orders that did not enter the process, duplicates, unresolved ownership/linkage, and historical records lacking an evidenced entry basis. Show those excluded counts separately; do not fabricate entry timestamps from placement or tag capture.
- **Time:** proposed cohort by first confirmation-process entry date; evaluated at as-of. Entry time unknown cannot join a dated cohort. A replacement is a new order and enters independently when eligible.
- **Drill-down:** participants with entry basis, confirmation evidence, attempts and any current disagreement/withdrawal. A later withdrawal changes the current affirmative numerator with retained history; it does not erase entry.
- **Gentry difference:** live 802/1,339 counts confirmer tags/all placed orders; historical coverage sometimes excludes Omar. Neither is the OpsHub process-entry denominator (D07/D08).

## K02 — Delivery Success Rate (MUST)

- **Meaning:** successful courier delivery of the outbound shipment to its intended recipient, independently of later customer return/kept-goods outcome.
- **Numerator:** distinct outbound shipments with evidenced/mapped final successful delivery.
- **Denominator:** distinct outbound shipments with a known final courier outcome, including RTO and other explicitly mapped terminal nonsuccess outcomes. Each outbound counts once under OD06.
- **Included:** matched merchant outbound shipments in the cohort with approved finality mapping. A later post-delivery customer return does not reverse the evidenced outbound delivery. It appears separately in business disposition.
- **Excluded:** pending/in-transit, unknown/unmapped/conflicting final outcomes, reverse/return/exchange legs, duplicate observations, and cancelled orders that never had an outbound shipment. A courier-cancelled actual outbound is included only when mapped as a final courier outcome; pre-booking cancellation is not a shipment. Publish excluded populations.
- **Time:** proposed cohort by outbound shipment creation date, evaluated at as-of. Missing creation basis is shown separately. Courier completion date is available as a separately labeled operational listing, not silently substituted as the cohort.
- **Drill-down:** contributing shipment, purpose, source final outcome/time/basis, order business disposition and pending population.
- **Gentry difference:** kept/finalized order outcomes (640/1,054) measure kept business outcomes; “Bosta way” includes refusal/exchange. Delivered reverse legs never enter this outbound numerator (D05/PD09).

## K03 — RTO Rate (MUST)

- **Meaning:** outbound shipments finally returned to origin without successful recipient delivery under approved mapping.
- **Numerator:** distinct outbound shipments with a final RTO outcome.
- **Denominator / population / time:** exactly K02's final-outbound population, creation cohort and as-of; identical exclusions and drill-down contract.
- **Boundary:** a completed separate reverse leg is not an additional outbound and cannot by itself prove original RTO. Preserve source linkage/purpose uncertainty. Post-receipt customer return is not RTO.
- **Qualification:** Delivery Success Rate + RTO Rate need not equal 100%; other mapped terminal outcomes can exist. Remaining final-other counts are shown. Mapping that allows two contradictory final results goes to conflict review, not double counting.
- **Gentry difference:** workbook leg-type counts and monthly “all SEND delivered” semantics cannot be reused as OpsHub final courier truth (D14/D15).

## K04 — Pickup Completion Rate (MUST)

- **Meaning:** physical collection among pickups whose pickup outcome is final, independently of payment.
- **Numerator:** distinct physically collected pickup cases with accepted collection evidence; collected-and-later-returned remains physically collected if that occurrence is evidenced.
- **Denominator:** distinct pickup cases with a known final pickup outcome: evidenced collected or explicitly final uncollected outcome under approved mapping (for example Admin-cancelled before collection or evidenced no-show).
- **Included:** single pickup case per eligible order with supported pickup/collection purpose and known final outcome; each once. Customer handover and courier collection have separately named purpose-specific populations. Neither payment nor a source label identifying the other physical event can establish collection for the selected population; OP05 supplies the mapping.
- **Excluded:** pending/waiting, historical inferred collection, ambiguous/partial/repeated episodes and unknown/conflicting final outcomes. Payment paid/refunded/voided alone never defines numerator or finality. Show pending and unknown independently.
- **Time:** proposed pickup-case entry-date cohort, evaluated at as-of; use an evidenced entry date, not inferred payment date. Ageing is an explicitly labeled placement/entry clock separate from KPI cohort.
- **Drill-down:** physical evidence, final-outcome reason, actor/source/time and separate payment state. Supported pickup type and exception mapping require OP05.
- **Gentry difference:** historical paid→Collected and live 44 collected including one refused exception are preserved legacy definitions; OpsHub requires physical evidence (D01–D03/D06).

## K05 — Call Reach Rate (MUST)

- **Meaning:** ability to reach customers on customer-contact cases, not number of successful call events.
- **Numerator:** distinct cases with at least one evidenced successful customer reach.
- **Denominator:** distinct customer-contact cases with at least one actual contact attempt.
- **Included:** confirmation, return and pickup customer-contact cases; case purpose breakdown mandatory. Failed attempts/exhausted cases with attempted contact stay included. Each case counts once, regardless of attempt count; later failed contact does not erase earlier reach.
- **Excluded:** cases without attempts, administrative-only tasks, imported summaries without evidence of attempts/reach, duplicate/uncertain case links. Do not infer reach merely from Resolved/Refunded labels. Imported explicit summary evidence may be usable only with labeled basis under approved mapping.
- **Time:** proposed cohort by first actual contact attempt date, evaluated at as-of. Unknown occurrence date appears in undated history, not a fabricated period.
- **Drill-down:** case purpose, individual evidenced attempts, successful reach basis, exhausted status and missing evidence. A contact spanning ambiguous multiple cases is held for review.
- **Gentry difference:** 59 answered/93 called deduplicated returned orders differs from 239 exported events and the 32-entry queue; OpsHub names its case population (D10/D11).

## K06 — Call Action Completion Rate (MUST)

- **Meaning:** completion of required follow-up action on customer-contact cases. It measures a different job from reaching customers.
- **Numerator:** distinct cases where every required action for that case is completed with evidence and no currently required action remains.
- **Denominator:** distinct customer-contact cases with an explicitly required action, including pending approval, failed/unknown effects and exhausted cases whose action remains required.
- **Included:** customer-contact cases whose action requirement is explicit, whether or not contact has yet been attempted or reached, evaluated as cases rather than effect/attempt events. Action-required cases are counted once even with several necessary effects.
- **Excluded:** cases that never required an action, purely administrative tasks and unsupported imported completion assertions. Removing an action requirement cannot silently erase the denominator: any correction needs Admin reason/history and a visible corrected-cohort qualification.
- **Time:** proposed cohort by first action-required date, evaluated at as-of. Later action completion updates that cohort. A separate “actions completed today” workload count uses completion date and is not this ratio.
- **Drill-down:** required actions, responsible user, approvals, each external result and incomplete reasons. A call, approval, contact label or exhausted state alone never establishes completion.
- **Gentry difference:** quick Called done/Resolved can hide actual action completion; no single generic call-performance number is carried forward (PD06/BR18).

## K07 — ROAS (MUST HAVE — MVP)

- **Meaning:** attributed sales revenue divided by advertising spend for an explicitly named merchant/product period and attribution method; not profit, collected cash or settlement.
- **Numerator:** attributed sales revenue. Proposed qualified display is **net attributed sales ROAS**, using attributed gross sales minus discounts minus recognized return/refund sales adjustments; return/refund representations of one reversal must not be subtracted twice. Gross ROAS, if later offered, is a separate definition.
- **Denominator:** advertising spend attributable to that same scope/interval, including direct and explicitly allocated generic spend once. Original generic total is not added again to its allocation portions.
- **Included:** sales/spend with compatible currency, period and evidenced attribution; net adjustment basis/attribution method is mandatory. Shopify product sales and applicable Meta spend are the named pilot inputs. Connected input is normal; disclosed fallback inputs require equivalent provenance/completeness and an exception reason.
- **Excluded:** unresolved attribution, missing spend/revenue, incompatible currencies and duplicate observations. Zero spend gives N/A, not zero. Zero revenue with positive complete spend may yield zero; a legitimate negative adjustment is labeled, not clamped away. No currency conversion policy is assumed.
- **Time:** aligned revenue-attribution and spend period with adjustment allocation basis and as-of; recent/late data can revise. Allocation collisions, zero-sales generic allocation, VAT inclusion, currency and rounding require OP09 qualification before MVP analytics release. OD09 settles priority, not these policy details.
- **Drill-down:** revenue/discount/adjustment contributors, direct/generic/unallocated spend and attribution/input revision.
- **Gentry qualification:** verified `(gross sales − discounts − returns) / (own + generic spend)` matches 14 positive-spend exported rows; six zero-spend rows blank. This supports a net-revenue qualification, not a complete attribution/tax algorithm. See [L25/profile](../../evidence/live/product-export-profile.json).

## Product/SKU performance contracts — MUST HAVE

The view supports merchant-local day/week/month/custom periods, a compatible comparison interval, product/SKU search/filter/sort and practical contributor drill-down. Distinguish Product, Variant/SKU, Order Item, Order, outbound Shipment and Return Case grain; preserve unknown mappings. Basic source season/classification context can filter/classify analysis where meaningful; current assignment is not automatically a historical assignment. Missing season is explicit and does not block analytics. Full season CRUD/bulk assignment and automated planning are not MVP dependencies.

| ID / business measure | Numerator / denominator or count population | Time, exclusions and drill-down |
|---|---|---|
| P01 Product/SKU orders, units and revenue | Orders: distinct source orders containing an evidenced matching item. Units: sum evidenced quantity under declared sales-state policy. Revenue: attributed item sales/discount/return-adjustment amounts using K07's qualified basis; never copy full order value into every SKU | Proposed placement/sales-period basis, explicitly named and evaluated at as-of. Missing item/quantity/revenue remains unknown/unmapped, not guessed from prose or zero. Source-policy cancellations/adjustments visible; carrier result never silently determines sales revenue. Drill to items/orders and money basis |
| P02 Product/SKU delivery success and RTO | K02/K03 numerator and final-outbound denominator restricted to distinct outbound shipments whose order contains the selected evidenced Product/SKU. Count each shipment once in that product population, regardless of quantity | Same outbound creation cohort/as-of/finality/exclusions as K02/K03; show pending/unknown/unmapped membership. Multi-product shipment can appear in several product views; those views overlap and are not additive merchant totals. Label shipment association, not individually delivered units or causal product fault. Drill to shipment/order/item mapping |
| P03 Product customer-return problems | Distinct product-containing orders in the stated order cohort with an evidenced post-receipt customer-return association; separate RTO, exchange and pending return work. Show item-specific returned quantities/values only where evidenced | Order placement cohort with return-observation/as-of qualified; late cases may revise. An order-level return does not prove every item was returned or caused the issue. Uncertain association displayed separately. MVP count/breakdown is required; any optional return-rate must first define its denominator/time/exclusions under OP09. Drill to case/order/reason and evidence certainty |
| P04 Product advertising spend/economics and ROAS | Direct plus explicitly allocated generic spend once, with unallocated balance and attributed sales numerator. K07 supplies ROAS denominator/zero/missing treatment. Show sourced unit cost/margin/tax basis when available as assumptions/observations, not incurred profit | Aligned Meta/commerce period/currency/tax/as-of and approved method. Name/keyword collisions, no-sale generic allocation and unknown scope remain unallocated/review unless qualified policy permits attribution. Distinguish missing from evidenced zero; incomplete result visibly provisional/unavailable. Drill to sourced spend/allocations/revenue adjustments |
| P05 Comparable periods and stock/classification context | Compare the same P01–P04 definition/grain/method and compatible period lengths; named absolute/rate differences. Current/dated inventory and source season are contextual observations with their own as-of | Zero comparison denominator gives N/A for percent change; incomplete periods/changed policy/revisions are labeled. Never substitute current stock/season for historical values. No inferred stock movement or production plan |
| P06 Product attention | Missing item/outcome/spend mapping, stale/partial input, or an evidenced comparable deterioration/approved threshold exception with sample counts | State predicate, metric/window/sample/source quality and approved threshold where used. If no threshold is approved, show observed values/rank and review reason without inventing High/Scaling labels. Attention does not change tiers, advertising budgets or order actions automatically |

For each rate/ratio tile, apply KPI01–KPI05 and K07. Counts/amounts state their contributor population and exclusions even without a mathematical denominator. Product order/shipment/return presence views overlap; financial item allocations must reconcile once to the qualified total with unmapped/unallocated balance. A product requiring attention can link to daily operational cases without implying a product-caused courier problem.

## Supporting counts and legacy comparison

Display order totals/value as **source commercial value**, not realized revenue. Queue counts measure current named predicate membership; attempt counts measure contact events/courier counters separately. Unknown dates/coverage remain counted in diagnostic totals outside incompatible dated cohorts.

Migration validation must compare the same source population, grain, definition, period and as-of. Preserve Gentry legacy figures under Gentry labels, alongside recalculated OpsHub definitions and reasoned differences. Approval of OD05 does not make legacy rates wrong or retrospectively compatible. [AC12](11-mvp-acceptance-criteria.md#ac12--legacy-comparison-readiness) defines the later comparison requirement without authorizing migration work.
