# Calculations and metric definitions

Evidence: [workbook formulas](../../evidence/artifacts/workbooks/WORKBOOK_FINDINGS.md), [historical metric/script table](../../evidence/artifacts/text/nonworkbook-analysis.md#calculations-and-metric-definitions), [live ledger](../../evidence/live/observation-ledger.md), [product arithmetic profile](../../evidence/live/product-export-profile.json). Figures are dated examples, not permanent performance conclusions.

## Current Order Performance

| Metric | Numerator / denominator, population and missingness |
|---|---|
| Total orders/value | Selected cohort by order placement date. All-time export: 1,339 unique order names, EGP 1,893,401. Order value is not proved collected cash or recognized revenue. |
| Confirmation share | Tagged confirmer total / all selected placed orders. Current week: 21 / 32 = 65.6%. All-time: 802 / 1,339 = 59.9%, independently computed from export. Historical combined Hadeer/auto coverage excludes Omar and uses a different numerator. |
| Omar intervention | Omar / all confirmed, with a provisional 15% line in the report. The denominator is not all placed orders. Current report shows zero interventions this week and five in the comparison period. |
| Delivery dispatch | Dispatched Delivery orders / all Delivery orders. Current week: 14 / 31 = 45.2%. All-time: 1,101 / 1,215 = 90.6%. Tags or booleans can signal handoff without a matched shipment leg. |
| Delivered and kept | Kept / finalized Delivery outcomes (kept + RTO + refused + exchange). All-time: 640 / 1,054 = 60.7%. Explicit In transit outcomes and the 29 status-fallback rows are excluded. Current week: 8 / 8 = 100%, a small and recent sample. |
| Bosta way | (kept + refused + exchange) / the same finalized denominator. All-time: 715 / 1,054 = 67.8%. This includes customer-side returns and does not mean kept conversion. |
| Pickup success | Collected / (collected + cancelled): 44 / (44 + 69) = 38.9%. Eleven waiting pickups are excluded. The export has 43 `Picked up` outcomes and one pickup `Received then refused`, corresponding to the UI's 44 collected. The exception's exact meaning requires clarification. |
| Stage in transit | Broad handoff bucket of 47 orders: 18 explicit `In transit` outcomes + 19 `Cancelled` status fallbacks + 10 `Completed` status fallbacks. This differs from the explicit In transit outcome count of 18. The underlying membership predicate is unresolved. |
| Repeat returners | Orders belonging to phones with two or more returns, per UI. This is not a count of unique people; phone normalization and the returned-state definition are unresolved. |
| Pickup ageing | Waiting orders grouped by days since placement: under 3 days, 3–6 days, and 7 or more days (4 / 4 / 3 all-time). Cleanup's 10-day threshold also uses placement date, not courier return date. |
| Call coverage | Current all-time return metric cohort since 7 September: 102 returns; 93 called / 102 = 91.2%, with nine uncalled. Answered: 59 / 93 = 63.4%; No Answer: 34 / 93 = 36.6%. The queue has 32 entries. Retry eligibility and dates may explain the different population, but the complete predicate is unresolved. The 239 exported events are not this denominator. |
| Cause distribution | UI says each return counts once using the answered reason. Unknown and No Answer are kept separate. Latest-versus-first reason selection is unresolved; imported legacy values exist. |
| Report comparison | Current partial period, 12–13 October, versus the immediately preceding equal-length period, 10–11 October. This differs from comparing the last two full weeks. The trend starts weeks on Monday and includes a partial current point. |
| Confirmed delivery shipment test | Report uses a three-day age condition for confirmed Delivery orders and distinguishes booking/cancellation. The current display says there are no overdue confirmed unbooked orders. The full predicate and its enforcement are unresolved; this is not proof of a dispatch guard. |

No confirmed event timestamp or return-received timestamp was proven. Statistical correlation between tag groups and outcomes cannot establish causal effect of confirmation.

## Current Product Performance

**VERIFIED arithmetic:** `net ROAS = (gross sales − discounts − returns) / (own spend + generic share)`. All 14 positive-spend exported rows match at two decimals. Six zero-spend rows have blank ROAS, not zero. Example product: (30,400 − 0 − 6,400) / 9,915.72 = 2.4204, displayed as 2.42. The selected period's 20-product aggregate has 179 units, EGP 138,800 gross sales, EGP 24,300 returns, and EGP 30,409.77 estimated spend. These figures can revise after a Meta/Shopify rebuild.

| Metric | Definition / evidence / limit |
|---|---|
| Breakeven ROAS | 1 / gross-margin fraction. Sample: 0.35 gives 2.857, displayed as 2.86. Thresholds are multiples of breakeven, not fixed ROAS values. Zero or missing margin behavior is untested. |
| Net cash / net sales | Gross sales − discounts − returns, as seen in the weekly snapshot. This is not profit; supplier costs, courier fees and gateway charges are separate. |
| Own and generic spend | UI labels spend Meta incl VAT. Names/keywords identify own ads; generic spend is weighted by sales. UI copy says full weeks allocate per week and other periods per day. Zero-sales, collision and VAT rules remain unverified. The one-cent difference between summed components and estimated spend is consistent with rounding. |
| Assigned / suggested tier | All 20 products are assigned New. Suggestions vary between Scaling, Baseline, Underperformer and blank. Settings show Baseline at 2.8 × breakeven, Scaling at 3.8 × breakeven, and New graduation at 20 orders. ROAS alone does not explain the suggestions: some high-ROAS products with lower velocity show Baseline. A velocity condition is INFERRED; the exact algorithm is unresolved. |
| Sales velocity | Detail uses the last four full weeks; sample speed is 3.8 units per day. The dashboard's selected-period speed and store average of 1.8 per day may use a different denominator. An average over active products is a possible inference, not an established rule. |
| Days stock | Detail: 93 current units / 3.8 units per day ≈ 24.5 days, displayed as 24. Rounding, zero-speed/infinite values and incoming-stock treatment are not fully verified. |
| Sell-through | Latest weekly snapshot: 38 / (38 + 98) = 27.94%, matching 27.9% displayed. This supports units / (units + dated ending stock) for the sample, not every edge case. |
| Restock | Lead time of four weeks means 28 days; the season ends on 31 October. Expected arrival beyond the season end gives zero sellable days and the advice Enough for season. UI references current stock + incoming stock, velocity, horizon, a Scaling safety adjustment of 20%, and minimum batch. Exact rounding, order-by date and quantity rules are unknown. |
| Order counts | Selected-period orders, current all-time orders and historical snapshot cumulative orders are separate. Sample: 36 period orders / 38 units; 143 current all-time orders versus 138 in the latest weekly snapshot. New queue uses 138, so its graduation window is not proved to be all-time. |
| Time windows | Dates since 1 June with Cairo-day labels; Monday-based complete weeks. Stock now and rebuild as-of values are current even when the selected sales period is historical. Compare dated ending stock separately. |

Settings defaults needing owner confirmation are current configuration facts, not approved policy. No supplied source code implements these live product formulas.

## Historical workbook — formulas translated

Numerical examples in this section are independent reproductions from supplied inputs, not current application measurements or Excel-engine results.

| Metric / rule | Inputs and formula meaning | Inclusion, nulls, edges / locator |
|---|---|---|
| Shipment group | Type precedence: RTO, customer return, exchange; otherwise state containing deliver/cancel, else transit. | The substring “Out for delivery” would match delivered; this is an unobserved edge. `DATA_Master!I4`. |
| Outbound/RTO | SEND + RTO count; RTO / outbound. | Shipment-leg grain; customer-return and exchange legs excluded. `Config!B136:D139`. |
| Customer return rate | Customer-return legs / delivered legs. | Not RTO denominator; original cohort linkage not enforced. |
| First-time-right | (outbound − RTO − customer-return legs) / outbound. | May subtract returns from different order/shipment cohorts; exchange handling is separate. `OPS_Control!C37`. |
| Attempts excess | For numeric outbound attempts, MAX(0, attempts − 2). | This is not an incremental fee calculation. `DATA_Master!K4`. Mean attempts must specify the included shipment types. |
| Cycle days | MAX(0, completion date − created date), prefer Confirmed Delivery At and drop the time component. | Negative chronology is forced to zero. `DATA_Master!C:E`. |
| Date buckets | Saturday–Friday weeks and calendar months of shipment creation. | Different from live order-placement cohorts and Monday weeks. `DATA_Master!Q4`. |
| Product quantity/value | Four description slots of 180 characters; a trailing x with a single digit indicates quantity. Exact matched SKU price/cost × quantity. | Four-item capacity; long descriptions and multi-digit quantities are edge cases. All 569 supplied descriptions agree with newline parsing; no current parser defect was demonstrated. `DATA_Master!AR:BC`, `AD:AE`. |
| Value hierarchy | Positive numeric COD; else positive matched SKU subtotal; else measured AOV of delivered legs with positive COD; else blank. | Forty current legs use the AOV proxy. A positive source value is not proof of cash collection. `DATA_Master!AA/AF/AG`, `Config!C36`. |
| Catalogue COGS | SUM(SKU costs) / SUM(SKU prices); gross margin = 1 − that ratio. | Current catalogue ratio is 57.5596%, not sales-weighted COGS. `Config!C37:C38`. |
| Lost margin | For Returned/customer-return legs with matched COGS: MAX(0, value − COGS). Otherwise use value × blended margin. | The blended fallback is not clamped; sensitive to proxies and not audited margin. `DATA_Master!AH`. |
| Courier fee | Positive SUMIF of tracking-matched Total Fees; else a complete zone/rate/attempt model; else blank. | Current modeled sections are OUT OF USE/missing. Zero/negative actual fees are edge cases. `DATA_Master!AI/AJ`. |
| Fee total | SUM of joined shipment fees: independently reproduced EGP 55,951.05, versus EGP 134,233.55 for the entire wallet. | Excludes 812 wallet-only IDs; shipment creation and wallet completion windows differ. `OPS_Control!C50`, `Data_Quality!C19`. |
| Gateway fee | A Delivered leg with zero COD is inferred prepaid; value × 0.017. | Historical Paymob assumption, not gateway transaction evidence. `DATA_Master!AB4`, `Config!C39`, `OPS_Control!C52`. |
| Net contribution | Delivered value − matched goods COGS − all joined courier fees − presumed gateway fee, gated on inputs. | Not audited profit; recoverability, return proxies and fee scope matter. `OPS_Control!C53`. |
| Cause capture | Nonblank joined intake root cause / all Returned + Customer return + Exchange return legs. | Counts any nonblank cause, including invalid/unmapped values. Taxonomy validity is checked separately. Legacy categories and Customer refused to give reason also count as populated. Current 45 / 256 is independently reproduced. `DATA_Master!Z`. |
| Confirmation | Hadeer / auto confirmations / all placed orders; Omar / all confirmed orders. | Current 297 / 1,635 is independently reproduced Hadeer/auto coverage; historical 209 / 353 = 59.2%. Tag matching uses substring search. `Confirmation!C13:C14`. |
| Pickup no-show | Explicit No-show / (explicit No-show + explicit Collected). | Open and inferred pickups excluded; outcome inferred from payment. `Pickup_Channel!H9`. |
| Pickup age | Maximum exported order date − placed date. Call at three days, manual cancel recommendation at seven; two-day settling window. | A stale export freezes age; the clock is not TODAY. `Config!C202:C205`. |

Independent source computations have bounded support from 12 v2 cached Config outputs agreeing within 1e−9. Current/v3 have no formula caches; no original was recalculated. Source metric values must remain labelled as independent reproduction.

## Historical report pipeline divergences

The monthly extractor groups by shipment creation month, calls every SEND delivered, and averages attempts across all shipment types. Its return-fee numerator includes RTO only. It assigns full Shopify order value to each RTO leg, takes the last wallet fee per tracking number, and substitutes zero for missing fees. It gates wallet coverage at 90%, but a month without a coverage entry passes. The execution calendar month determines partialness, rather than the source watermark. Its confirmer comparison includes partial September and uses a pooled z test with Wald confidence intervals. Nonsignificance does not establish that confirmation has no effect.

The weekly chart converts missing coverage/dispatch values to zero. Optional drop-last removes the final item without checking its date. Instructions to omit partial weeks and label stale data are not fully enforced by code. Archived report inputs are absent and the output differs from the supplied builder, so exact regeneration is unverified. See TXT-D01–D32 and [discrepancies](13-live-vs-spec-discrepancies.md).
