# Data model observations

No live database schema was available. These are observed file schemas, exported contracts and inferred relationships, not target tables.

## Supplied raw schemas and grain

Exact complete column/type/completeness profiles: [workbook evidence](../../evidence/artifacts/workbooks/WORKBOOK_FINDINGS.md) and adjacent `.data_profiles.json` files.

| Dataset / schema locator | Grain, key and current supplied population |
|---|---|
| `RAW_Bosta!A2:AC2` | One shipment leg per row. A is tracking number as text; J is business order reference. 569 distinct tracking keys, 534 distinct nonblank references, and four missing references. Twenty-eight references occur on multiple legs. Types: 313 SEND, 210 RTO, 26 CUSTOMER_RETURN_PICKUP, 20 EXCHANGE_return. All supplied shipment states are terminal. |
| `RAW_Costs!A2:AJ2` | One wallet/cash-cycle row. C, Order Id, means Bosta tracking number; AF is Total Fees. 1,381 unique keys. Values reach row 1383 although the declared XML dimension ends at row 1239. Completion dates span 30 April–7 September. |
| `RAW_Intake!A2:T2` | One tracking-keyed return/contact record; D is tracking number. 75 keys: 45 Reached, 23 No Answer, seven blank call states. Return type, size detail, refund and recoverability are blank on all 75 rows. Thirty root causes are blank; 28 use legacy fit/quality categories. Schema presence does not prove adoption. |
| `RAW_SKU!A2:E2` | Variant label, product, size, price and COGS; 60 unique variants / 19 product labels. Joins the parsed description. Forty unmatched item slots occur in 39 shipment legs. SKU audit flags check only slots 1–2, while valuation uses four slots. |
| `RAW_Shopify!A2:CC2` | 79 Shopify export columns plus helpers; 2,082 line items / 1,635 order headers. A nonblank Financial Status in C identifies the header. Order names repeat across line items; a raw row is not an order. Dates span 1 April–8 September. |
| `DATA_Master!A2:BC2` | 55 derived columns per shipment leg, with 2,000 slots in `A4:BC2003`. Derives contact, cost, SKU, date, group, owner, proxy value, audit flags and parsed items. |
| `Orders_Master!A3:X3` | 24 derived columns per order, with 2,000 slots in `A4:X2003`. Sequence lookup from financial-status headers; joins matching Bosta references and derives confirmation, channel, cancellation and pickup fields. |

The current supplied history has unequal windows: Bosta creation dates span 20 May–6 September; Shopify order dates span 1 April–8 September; wallet completion dates span 30 April–7 September. The 75-row intake is unchanged across all three system workbooks. Staged datasets have separate provenance; the package cannot be described as uniformly updated.

## Capacities and parsing

Current Shopify named ranges use rows 3:5002 and the CC helper spans 5,000 rows; v3 uses rows 3:2002. Both masters retain 2,000 entity slots. All 1,635 order headers fit despite 2,082 source line items. Bosta/cost names span rows 3:2002; SKU names span rows 3:402. Larger inputs can exceed a named range or master capacity. No dynamic structured tables were found. Reading must not be bounded by stale OOXML dimensions.

Bosta descriptions use four fixed slots of 180 characters and a single-digit quantity suffix. All 569 supplied rows match newline parsing; more than four items, multi-digit quantities and long labels remain unobserved edge cases. Variant spelling affects joins; Excel MATCH is case-insensitive. Intake takes the first MATCH and allows numeric fallback, creating possible text/numeric ambiguity. Current wallet keys are unique, but SUMIF permits multiple fee lines per tracking number. A zero or negative actual fee sum is not accepted as the actual cost by the master formula.

## Live CSV contracts

| Export | Fields / grain / observations |
|---|---|
| Orders — [profile](../../evidence/live/order-export-profile.json) | 15 columns, 1,339 unique order rows. Statuses: 37 Pending, 480 Cancelled, 822 Completed. Twenty-nine Outcome values are blank. Customer, phone and item values were intentionally not retained. |
| Calls — [profile](../../evidence/live/call-export-profile.json) | 11 columns, 239 events / 224 distinct order names. Event dates span 11 June–8 October; seven matched call dates precede the exported order date. Historical values extend beyond current form dropdowns. |
| Products — [profile](../../evidence/live/product-export-profile.json) | 28 columns, 20 product-period rows, all assigned New. Period: 5–11 October. Current stock and all-time order fields use a different time basis from selected-period sales. |

Exact CSV headers, preserving spelling and spaces:

- Orders: `Order`, `Date`, `Customer`, `Phone`, `Channel`, `Confirmed by`, `Outcome`, `Status`, `City`, `Bosta state`, `Attempts`, `Items`, `Value (EGP)`, `Returns by this phone`, `Last call`.
- Calls: `Called at`, `Order`, `Customer`, `Phone`, `Call status`, `Reason`, `Resolution`, `Refund issued`, `Recoverable`, `Called by`, `Notes`.
- Products: `Product`, `Period`, `From`, `To`, `Tier`, `Gross margin %`, `Breakeven ROAS`, `Unit cost (EGP)`, `Lead time (weeks)`, `Units sold`, `Gross sales (EGP)`, `Discounts (EGP)`, `Returns (EGP)`, `Ad spend est. (EGP)`, `Ad spend: own ads (EGP)`, `Ad spend: generic share (EGP)`, `Net ROAS`, `Own ads (count)`, `Own ads`, `Stock left (now)`, `Days of stock`, `Orders (period)`, `Orders (all-time)`, `Suggested tier`, `Ad advice`, `Restock advice`, `Restock qty`, `Order by`.

These export contracts are not proved database columns. Live detail internal IDs differ from Shopify order names and Product GIDs. Hidden server-action fields were not treated as business data. No credentials were retained.

## Source-to-live reconciliation

The reconciliation uses exact trimmed external order names, not fuzzy customer or phone matching:

| Source | Shared / source-only / live-only | Date comparison |
|---|---|---|
| Current 1,635 vs live 1,339 | 768 / 867 / 571 | Zero shared placement-date differences. Source-only dates span 1 April–1 June; live-only dates span 8 September–13 October. |
| v3 backup 353 vs live 1,339 | 353 / 0 / 986 | All 353 shared placement dates agree. |

Overlap supports related identities and different windows, not complete migration success. The live minimum is 7 May, while source-only records extend into June. Neither all-source-before-live-start nor a simple date cutoff explains every omission. Import scope and omission reasons require authorized read-only backend/import-log evidence.

## Data-quality implications

- A missing shipment match may mean a different export window, legitimate pickup, failed sync or missing record. It does not prove physical collection.
- Call taxonomy includes old labels (`Fit - size not specified`, `Quality - not specified`, `Not recoverable`, `Reshipped`, `Exchange completed`, `Pending`) absent from the current form. Preserve their original meaning before proposing mappings.
- Customer phone as a repeat key has no proved normalization. One person may have multiple numbers; multiple people may share one number.
- Call dates before order dates may reflect backfilled times, bad linkage, timestamp format or import logic. The seven matched comparisons are verified; their cause is UNRESOLVED.
- Amounts are EGP in the current UI. No currency entity or exchange-rate handling was verified. Historical zero/blank COD may trigger proxy valuation.
- No Excel data-validation rules, structured tables, pivots or external connection files establish enforcement. The current system workbook has three charts and conditional formatting as presentation controls.
- Live deletion, retention, audit and update semantics; shipment selection and outcome projection; manual snapshot overwrite; and caller identity require further inspection.
