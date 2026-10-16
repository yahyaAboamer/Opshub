# Gentry spreadsheet reconstruction evidence

Inspected 13 October 2026. Scope: every `.xlsx` and `.csv` under `source/`, plus the owner-authorized live order export downloaded by the root investigator to `D:\Downloads\orders-2026-10-13.csv`. All sources were read only. Customer names, emails, phones, addresses and raw transaction identifiers are omitted from generated evidence.

## Evidence status and method

- **Verified artifact facts** below come from OOXML worksheet cells, defined names, formulas, validation/format rules, cached results and complete input-row inspection. Each workbook has a SHA-256 in `workbook_inventory.json` and a `.structure.json`.
- OOXML was inspected directly, including expansion of Excel shared formulas in v2. This matters because some declared worksheet dimensions are stale and because a shared formula is present in many cells with its text stored only once.
- Current and v3 have **no cached values for any formula**. Their dashboards cannot be treated as measured results merely by opening the files with a data-only library. Independent Python reproduction of inspected formula semantics is recorded separately in `reconciliation.json`, without editing or recalculating any original workbook.
- A numerical crosscheck against v2 caches is recorded in `additional_checks.json`. This is bounded validation of the independently reproduced rules, not a complete Excel recalculation or validation of current live metrics.
- Twelve selected v2 cached outputs agree within 1e-9 with the independent reconstruction: Config C34, C36:C38, C40, C166:C172. The historical Shopify CSV matches v3 across all 495 line rows and all 79 export columns. The staged Shopify subset has equal within-order line counts (664 rows across 476 refs), with four orders having later differences in financial state, refund, payment references, notes or cancellation timestamp. Current fixed-width product parsing agrees with newline splitting on all 569 supplied descriptions; its edge limits remain unobserved.
- **Strongly supported inference:** these files describe the historical spreadsheet operations model that preceded or informed the live application. No workbook is automatically the authority for current live behavior.

## File roles and evidence relationships

| Source | Verified content and grain | Status |
|---|---|---|
| `02_Gentry_Delivery_Performance_System.xlsx` | 22 sheets; 167,678 formula cells. Shopify 2,082 line rows / 1,635 order headers; Bosta 569 shipment legs; wallet 1,381 cost rows; intake 75 tracking-keyed records; SKU 60 variants. | Most expanded supplied spreadsheet snapshot, with mixed input periods; current live authority not established. |
| `02_Gentry_Delivery_Performance_System_v3.0_BACKUP_2026-09-08.xlsx` | 22 sheets; 164,678 formula cells. 495 Shopify lines / 353 orders; 237 Bosta legs; 237 wallet rows; same 75 intake rows; 51 variants. | Historical v3 backup. Its Bosta and wallet history is still 18 Jun–17 Aug, despite the backup filename date. |
| `02_Gentry_Delivery_Performance_System_v2.0_BACKUP_2026-08-28.xlsx` | 18 sheets; 114,293 formula cells including shared formulas. 237 Bosta legs, 237 wallet rows, 75 intake records, 51 variants. No Shopify order funnel. | Historical v2 model; contains cached results useful for crosschecking. |
| `2026-08-28_Shopify_orders_18Jun-17Aug.csv` | 79 export columns; 495 line rows / 353 unique orders. Order header is identified by nonblank `Financial Status`. | Raw historical export used by v3. Full within-order line-sequence equivalence is checked separately. |
| `2026-09-08_RAW_Bosta_STAGED_20May-06Sep.xlsx` | `RAW_Bosta_PASTE`, 29 columns, 569 legs. | All 569 rows match current `RAW_Bosta` by tracking key and all input values. Incorporated staging data. |
| `2026-09-08_RAW_Shopify_STAGED_18Jun-08Sep.xlsx` | `RAW_Shopify_PASTE`, 664 line rows / 476 order references. Export columns plus a staged helper. | All 476 references exist in current; complete line sequences are compared in `additional_checks.json`. Current also contains older orders absent from this stage. |
| `2026-09-08_RAW_SKU_ADDITIONS.xlsx` | `RAW_SKU_ADDITIONS`, 22 nonblank variant keys; prices, costs and source notes. | Nine keys are incorporated unchanged into current; 13 are absent. Do not assume all staged additions were applied. |
| `2026-09-08_Hadeer_CallQueue_TopUp_27rows.xlsx` | `READ_ME` and `PASTE_AT_A102`; 27 contact/identity rows with tracking IDs, names, phones and items. | None of its 27 IDs occurs in supplied `RAW_Intake`. The README proposes pasting into the external call sheet; that action was not performed. |
| `01_Hadeer_Sheet_Upgrade_Pack.xlsx` | Four sheets: Setup guide; Paste into Lists; Migration formulas; Your weekly paste. Seven migration formulas. | Supporting migration procedure and taxonomy, not transaction history. |
| `~$02_Gentry_Delivery_Performance_System.xlsx` | 165-byte Excel owner/lock file. | Temporary application metadata, not a meaningful workbook; not parsed as transaction evidence. |

## Current workbook sheet map

| Sheet | Verified purpose / grain |
|---|---|
| START | Instructions and source refresh sequence. |
| EXEC_Brand | Executive reporting and three charts, with helper series. |
| OPS_Control | Latest complete Saturday–Friday week versus previous week, period totals and an operational action queue. |
| Weekly | Shipment creation-week aggregates, up to 52 week rows. |
| Monthly | Shipment creation-month aggregates, up to 24 month rows. |
| Returns_Channels | Separates failed delivery, customer return after delivery and exchange return; root cause counts and economic aggregates. |
| Failure_Analysis | Root cause ownership and carrier exception reliability. |
| Product_Size | Product/variant and size analysis from parsed Bosta Description slots and the SKU reference. |
| Geo_Courier | Zone/city and courier scorecards. Rates get a red flag only with at least five outbound observations. |
| Customer_Recovery | Contact reach, root-cause capture, resolution and repeat returners by literal trimmed phone. |
| Data_Quality | Input completeness, joins, duplicates, taxonomies, unknown SKU keys and proxy valuations. |
| Config | Named assumptions, mappings, taxonomy, thresholds and computed source status. |
| DATA_Master | One formula row per Bosta shipment leg, joined to intake, wallet and SKU inputs. 55 columns. |
| RAW_Bosta | Carrier shipment-leg export, 29 populated header columns in current. |
| RAW_Costs | Bosta cash-cycle/wallet row keyed by carrier tracking ID, 36 columns. |
| RAW_Intake | Return contact record keyed by Bosta tracking ID; legacy and new call columns coexist. |
| RAW_SKU | One variant key as Bosta writes it, with product, size, price and COGS. |
| Change_Log | Human-readable historical changes and approvals claimed by the artifact. |
| RAW_Shopify | Shopify line-item export with order-header fields and helper sequence in CC. |
| Orders_Master | One Shopify order per financial-status header, 24 derived columns. |
| Confirmation | Order-grain confirmation funnel, confirmer segments, Whappi failures and recent 12-week trend. |
| Pickup_Channel | Explicit office pickups, no-show calculation, overdue queue and separately labelled inferred pickups. |

Schema locators: `DATA_Master!A2:BC2`; `RAW_Bosta!A2:AC2`; `RAW_Costs!A2:AJ2`; `RAW_Intake!A2:T2`; `RAW_SKU!A2:E2`; `RAW_Shopify!A2:CC2`; `Orders_Master!A3:X3`. Complete cell-located schemas and per-column completeness/type statistics are in each `.data_profiles.json`.

## Identifiers, joins and capacities

1. `RAW_Bosta!A` is carrier tracking number; `RAW_Bosta!J` is Shopify/business order reference. Current has 569 distinct tracking numbers and 534 distinct nonblank business references. Twenty-eight references occur on multiple legs; four legs have no business reference. A Shopify order and a shipment leg are different grains.
2. `RAW_Costs!C` is carrier `Order Id`, matched to tracking number, not Shopify reference. `DATA_Master!AI4` uses `SUMIF(cost_id,$A4,cost_total)`; actual `Total Fees` is column AF. Current wallet IDs are all unique, but the formula allows summing several cost lines for the same tracking ID. It accepts the actual sum only if positive. Zero/negative actual fee behavior is a formula edge requiring live reconciliation.
3. `RAW_Intake!D` is also tracking number. `DATA_Master!AL4` first tries an exact text MATCH then numeric conversion MATCH. The intake join returns the first match. Customer name and phone do not own this join.
4. `RAW_SKU!A` matches the parsed Bosta variant description. Exact spelling, punctuation and spacing matter; Excel MATCH is case-insensitive.
5. `RAW_Shopify!A` is Shopify order reference; `Financial Status` in C is present only on the header row. CC3 is `IF($C3="","",COUNTA($C$3:$C3))`, filled through CC5002. `Orders_Master!A4` uses `INDEX(shop_name,MATCH(ROW()-3,shop_seq,0))`. It is a sequence lookup, **not** a raw-row-aligned copy. All 1,635 current order headers fit 2,000 output slots despite 2,082 source line rows.
6. Current `shop_*` names span RAW_Shopify rows 3:5002; v3 spans 3:2002. Current versus v3 formula samples are unchanged; 12 Shopify named ranges were expanded and 3,000 helper formulas added. `DATA_Master!A4:BC2003` and `Orders_Master!A4:X2003` each hold 2,000 entity slots. Current cost and Bosta named ranges use rows 3:2002; SKU names use rows 3:402.
7. Some OOXML dimensions are stale: RAW_Costs declares AJ1239 although values reach row 1383; RAW_Shopify declares CC2002 although inputs reach row 2084 and helper formulas reach 5002; RAW_Bosta declares Y despite populated Z:AC columns. Reconstruction used actual cells and defined ranges. A reader relying only on the declared dimensions could truncate evidence.

## Verified spreadsheet rules and calculations

| Rule | Exact evidence / implication |
|---|---|
| Delivery denominator | Config B136:D139: SEND and RTO are Outbound; CUSTOMER_RETURN_PICKUP and EXCHANGE_return are excluded. Shipment legs, not distinct Shopify orders. |
| Group precedence | DATA_Master I4: RTO → Returned; CUSTOMER_RETURN_PICKUP → Customer return; EXCHANGE_return → Exchange return; otherwise state containing `deliver` → Delivered, containing `cancel` → Cancelled, else In transit. These supplied exports contain only terminal states. `Out for delivery` would match `deliver`, an unobserved edge. |
| Shipment dates | DATA_Master C:E parse carrier month-day-year strings or Excel serials, drop times, and prefer Confirmed Delivery At over Delivered at. Cycle days are `MAX(0, completed-created)`. |
| Weekly cohort | DATA_Master Q4 uses `created_at-WEEKDAY(created_at,16)+1`: Saturday starts. Monthly uses EOMONTH of shipment creation date. |
| Attempts | DATA_Master K4: for numeric outbound attempts, `MAX(0,attempts-2)`. This is a derived excess-attempt count, not actual incremental cost. |
| Description parser | DATA_Master AR:AU replace each newline with 180 spaces and read four 180-character windows. AV:BC strip a trailing `x` plus a single digit and infer quantity; AD:AE sum matched price/COGS times quantity. It does not parse an unlimited line array or multi-digit quantities. |
| Value hierarchy | DATA_Master AA/AF/AG: positive numeric COD amount → COD value; otherwise positive matched SKU subtotal → SKU list; otherwise Config C36 measured delivered-positive-COD AOV → AOV proxy; else blank. Proxy is explicitly flagged. |
| Prepaid heuristic | DATA_Master AB4 calls a Delivered leg with zero COD `Yes` for prepaid. This is an artifact heuristic, not verified payment-gateway evidence. OPS_Control C52 charges 1.7% against those values. |
| Margin | Config C37: SUM of variant COGS / SUM of variant prices; a catalogue ratio, not sales-weighted COGS. C38 is 1 minus that ratio. DATA_Master AH computes lost margin only for Returned and Customer return, using matched COGS or the blended margin fallback. |
| Fee source | DATA_Master AI/AJ: positive sum of actual wallet Total Fees wins; otherwise complete zone delivery/RTO/extra-attempt rate-card inputs model the fee; otherwise blank/none. Config sections 2 and 3 are marked OUT OF USE and contain `[MISSING]`. |
| Fee scope | OPS_Control C50 and Returns_Channels C52 SUM `dm_fee`; they do not sum every wallet row. Data_Quality C19 explicitly flags wallet rows without a shipment match. |
| First-time-right | OPS_Control C37 subtracts RTO and customer-return leg counts from outbound count. It is a count-derived measure; independently aligned outbound/customer-return cohorts are not enforced by this formula. |
| Net contribution | OPS_Control C53: delivered value − delivered matched SKU COGS − all joined shipment fees − presumed prepaid gateway charges, gated on inputs. Do not label it audited financial profit. |
| Root cause | DATA_Master U/V join governed intake root cause to Config owner taxonomy. No source root cause remains blank; carrier exception reason is separate and assigned a trust class in Config. |
| Reason capture | Return groups are Returned + Customer return + Exchange return. DATA_Master Z tests whether root cause is nonblank. Customer refused to give reason and legacy categories count as populated root cause. |
| Repeat returners | DATA_Master AP/AQ and Customer_Recovery: literal trimmed phone identity, combining RTO and customer returns; formatting differences can split a customer. No canonical customer ID was evidenced in the workbook. |
| Confirmation | Config B180:D191 and Orders_Master L:O: substring searches for literal tag strings. `confirmed omar` has priority, then `Confirmed`; confirmer is Omar or combined Hadeer / auto. Attempt tags 3/3, 2/3, 1/3 give max attempt stage. |
| Confirmation KPI | Confirmation C13: Hadeer / auto confirmed orders divided by ALL orders placed. C14: Omar confirmations / ALL confirmations. Whappi failures have separate segments and never adjust Hadeer's numerator or denominator. |
| Cancel stage | Orders_Master G/P/S: Shopify Cancelled at determines cancellation; any matched Bosta ref means Post-dispatch, otherwise Pre-dispatch. The Cancelled tag is informational. |
| Order outcome | Orders_Master R4: any related Returned to origin wins over any Delivered; otherwise In transit / other. No chronological latest-event or outbound-leg restriction is used. |
| Fulfillment channel | Orders_Master J4: shipping method `90 Office` first; any Bosta join next; otherwise paid, not cancelled, positive value, old enough → Pickup - unrecorded; otherwise Not fulfilled. The inferred channel is explicitly separate. |
| Pickup status | Orders_Master T4: explicit pickup paid → Collected; voided/refunded → No-show; pending → Open; other financial states → Other. An inferred pickup is Collected (inferred). |
| Pickup ageing | Config C202=3 flag days; C203=7 kill days; C205=2 settling days. C204 is MAX exported order date, not TODAY. Orders_Master U/V/X ages and ranks open pickups oldest first, with ties resolved by row position. `KILL` is a suggested action label in a spreadsheet, not evidence of automated cancellation. |
| No-show rate | Pickup_Channel H9: explicit No-show / (explicit No-show + explicit Collected). Open and inferred pickups are excluded. |

All formula patterns, representative cells, counts and named ranges are retained in `.structure.json`. No source workbook data-validation rules were found, including Config/intake. Spreadsheet setup instructions describe validations to install in the external Google Sheet; they do not prove those validations were active. There are no Excel structured tables, pivots or external connection files in the current system workbook. It has three chart XML files and bounded conditional formatting rules. The upgrade pack's migration examples contain external `[1]lists!` references, which are template/migration evidence, not a production integration.

## Controls and evidence limits

- Config C39 contains `0.017` for Paymob, with an artifact note claiming owner confirmation on 19 August. A current real Paymob integration/fee schedule was not verified by this worker.
- Config C44:E53 gives internal targets: RTO 10% green / 15% amber; customer return 5% / 8%; attempts 2 / 2.5; reason capture 90% / 75%; reach 70% / 55%; recovery 25% / 15%; cycle 6 / 8 days; queue age 2 / 3 days; unmapped cities and unpriced SKUs zero. These are labelled owner targets and explicitly not external industry benchmarks.
- Config B93:E117 gives 25 root-cause categories and owners Product / Courier / Ops / Customer / Unknown, including two Legacy categories. Current intake has only five populated categories, with 28 legacy fit/quality records.
- Config C223:C225 are **not approved targets**: confirmation coverage 60%, Omar intervention 15%, pickup no-show 30%. The surrounding rows explicitly say `[CONFIRM]`, proposed by the build, not yet set by the owner.
- Current `RAW_Intake` has 75 records, 45 Reached, 23 No Answer and seven blank call states. All 75 return types, size details, refunds and recoverable fields are blank. New columns existing in the schema do not demonstrate that users adopted them.
- Current SKU reference has 60 priced/costed variants across 19 product labels, but independently parsed shipment descriptions still contain 40 unmatched slots across 39 shipments. DATA_Master's SKU flags cover only slot 1 and slot 2 even though values use four slots.
- v2's 189 cached `#N/A` cells are intentional EXEC_Brand chart suppression, e.g. AF5 `IF(Monthly!B9="",NA(),Monthly!E9)`. They are not evidence of broken operational calculations.

## Independent artifact aggregates

These are reproduction results from supplied inputs, not values displayed by the current live application.

| Metric | Current inputs | v2 / v3 shipment inputs |
|---|---:|---:|
| Shipment legs | 569 | 237 |
| Outbound legs | 523 | 212 |
| Delivered legs | 313 | 133 |
| RTO legs | 210 | 79 |
| Customer-return legs | 26 | 15 |
| Exchange-return legs | 20 | 10 |
| Joined positive wallet fees | EGP 55,951.05 | EGP 23,710.11 |
| Wallet rows absent from shipment export | 812 | 0 |
| Return-group legs with root cause | 45 / 256 | 37 / 104 |
| AOV proxy-valued legs | 40 | 14 |
| Measured delivered-positive-COD AOV | EGP 1,404.5806 | EGP 1,517.3966 |
| Catalogue COGS ratio | 57.5596% | 57.7514% |

The current wallet's entire Total Fees sum is EGP 134,233.55, covering completed dates 30 Apr–7 Sep; only matched legs contribute EGP 55,951.05. Current Bosta creation dates span 20 May–6 Sep, and completion dates 13 Jun–8 Sep. Shopify spans 1 Apr–8 Sep. Those are different populations.

Literal current Orders_Master logic produces 534 Bosta-channel orders, 69 explicit office pickups, **547 inferred pickups**, and 485 Not fulfilled. Confirmation is 297 Hadeer / auto, 37 Omar and 1,301 not confirmed. These figures must not be represented as live operational measurements or as proof that 547 customers collected in-store. The inference depends on absent carrier evidence and mismatched input coverage. v3's corresponding order history is only 353 orders from 18 Jun–17 Aug.

## Live export reconciliation

Live export is a read-only UI download supplied by the root investigator, with 1,339 rows and distinct order refs; date range 7 May–13 Oct 2026. Exact trimmed `Order` versus source Shopify `Name` strings were matched. No customer/phone matching or numeric-ID assumption was used.

| Comparison | Exact shared refs | Source-only refs | Live-only refs | Placement-date differences among shared |
|---|---:|---:|---:|---:|
| Current source 1,635 orders vs live 1,339 | 768 | 867 | 571 | 0 / 768 |
| v3 source 353 orders vs live 1,339 | 353 | 0 | 986 | 0 / 353 |

Current-source-only refs are dated 1 Apr–1 Jun. Live-only refs are dated 8 Sep–13 Oct. Shared current refs span 7 May–8 Sep. This strongly supports related order identities and different cohorts, not identical snapshots or completeness of either historical import.

Live export channels are Delivery 1,215 and Pickup 124. Its outcomes include Delivered & kept 640, Never received (RTO) 339, Received then refused 41, Exchange return 35, In transit 18, Picked up 43, Cancelled before dispatch 85, Cancelled 69, Not shipped yet 29, Pickup - not yet collected 11, and blank 29. The current source's formula outcomes are coarser and based on a narrower carrier export. Forty-one live export refused outcomes may differ from a dashboard's settled-delivery count of 40 because the export population/state rules differ; do not silently reconcile the discrepancy.

Live separates Hadeer 670, Whapi (auto) 41, Omar 91 and Not confirmed 537. The workbook combines Hadeer and automatic confirmation and cannot supply that split. Live export Bosta state strings include Processing, Created and Terminated, unlike the supplied terminal-only carrier input. Route-level investigation determines their current meaning.

## Contradictions, unknowns and next evidence

1. **Artifact/live terminology differs:** workbook customer-return legs and live Received then refused are not proven to be the same event/entity or date cohort. Live definitive outcome logic should take precedence for current behavior.
2. **Unequal source windows:** current Shopify history starts 1 Apr; Bosta starts 20 May and contains only 569 terminal legs; wallet includes 1,381 rows. This materially affects inferred pickups, confirmation coverage, fee completeness and rates. A full matched-period reconstruction would require authoritative export/import scope, not guessing missing records.
3. **Staged application is partial:** Bosta stage is fully applied; only nine of 22 staged SKU additions appear; top-up 27 IDs are absent from supplied call intake. The external Google Sheet may differ from this workbook and needs direct authorized inspection if considered current truth.
4. **Blank new fields:** the upgraded intake schema includes return type, size detail, refund and recoverable but has no populated values in these snapshots. Intended schema adoption and current live fields must be reconciled separately.
5. **Spreadsheet controls versus app validation:** no data-validation constraints in these files prove what the Google Sheet or live UI enforced. Observe current UI safely; do not invent mandatory rules from column labels.
6. **Formula edges:** zero/negative wallet sums, multi-digit quantities, fixed description windows, more than four products, substring tag matching, and precedence of old return versus later delivered legs need explicit classification as formula behavior or unobserved edge, not invented live defects.
7. **No current merchant tenancy evidence in spreadsheets:** a Business Name exists in wallet rows and Config has one courier. This does not establish live permissions, tenants, isolation or multi-merchant business behavior.

Confidence is high for artifact schemas, exact source overlap, formula text, capacities and explicit controls. Numerical reconstruction has bounded support from matching v2 caches and transparent code. Confidence is limited for current live business rules until root route/network inspection reconciles each rule, and low for physical-pickup conclusions inferred from absent shipment rows.

Supporting machine evidence: `workbook_inventory.json`, all `.structure.json`, `.controls.json`, `.data_profiles.json`, `reconciliation.json`, and `additional_checks.json`. Analysis scripts are preserved in this evidence directory for reproducibility and never write to `source/`.
