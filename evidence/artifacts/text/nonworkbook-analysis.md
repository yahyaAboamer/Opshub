# Gentry non workbook artifact reconstruction

Inspection date: 13 October 2026. Scope: every meaningful non-workbook file under `source/`, excluding the Shopify CSV assigned to dataset inspection. Sources were read only. No original script, macro or Apps Script was run; no source file was altered. This is artifact reconstruction, not evidence of the current web application's implementation.

`VERIFIED` below means a claim about the inspected artifact or statically visible code has direct evidence. A statement that an old document calls something live does not independently verify today's production behavior. Intended historical rules and observed current behavior must remain separate.

## Evidence locators and coverage

- Markdown, Python and Apps Script citations use one-based original source line numbers.
- DOCX citations use `P<n>` for a top-level body paragraph and `T<n>R<n>` for a top-level body table row, in OOXML document order. This is a reproducible structural locator, not a guessed page. Ordered sanitized blocks are retained beside this report.
- Report PDF page numbers were verified by rendering all four existing pages with bundled Poppler and inspecting them. PDF extraction and the DOCX extraction show the same material report tables, findings and notes. No layout claims are made for unrendered SOP DOCX files; all body text and tables were inspected structurally, and they contain no embedded images.
- `nonworkbook-manifest.json` contains size, SHA-256, line/block counts, document metadata and PYC headers for all 28 files. It establishes file identity, not business authority.
- The three superseded SOPs contain empty `word/comments.xml` parts, not substantive comments. All seven DOCX files have no tracked insertions/deletions. Current SOP/report core dates are generic 2013 `python-docx` template dates and cannot establish document chronology. Visible version/date labels are more useful.

## Artifact authority and provenance

| Artifact | Meaning and authority | Relationships and limits |
|---|---|---|
| `00_Delivery_Performance_System_Architecture.md` | Historical architecture specification v3.0, 28 Aug 2026, supersedes v2.0 19 Aug. Main workbook schema/domain intent. | Handover explicitly calls it the spec. Operating rhythm defers to current Operations SOP. Base sections contain stale v2 assumptions while §13 adds corrections and fourth channel. This is not the web application's source code. |
| `HANDOVER_README.md` | Developer handover dated 4 Sep 2026, version 3.0. Explicit authority and warning guide. | Calls the main workbook the system, 22 sheets; old plan/kickoff historical; older SOPs superseded. Its 18 Jun–17 Aug data-staleness statement predates 8 Sep refresh/report. |
| `03_SOP_Customer_Support_Calls.docx` | Current supplied role SOP v2.0 28 Aug; intended daily confirmation and return calling. | Supersedes named-person 19 Aug version. Calls/tagging and return taxonomy workflow, not server permissions. |
| `04_SOP_Operations_Weekly_Routine.docx` | Current supplied Operations SOP v3.0 28 Aug. Explicitly wins over spec for weekly routine. | Adds Shopify refresh, daily pickup age queue, confirmation review. Prescriptive human routine, not evidence of a scheduler. |
| `05_Executive_Brief_How_To_Read_It.docx` | Current supplied Brand Owner guide v2.0 28 Aug. | Defines decision authority, display interpretation, contribution economics and caveats. Some threshold/coverage wording contradicts provisional flagging elsewhere. |
| `06_v3.0_PreDispatch_Confirmation_Layer_PLAN.md` | Plan dated 22 Aug, explicitly `plan, not built`. Historical hypotheses. | Wrong intervention-tag string, assumed cancel reason/Whappi decline source, undecided denominator and grain. Handover lines 29 makes §13 supersede it. |
| `06.1_v3.0_Kickoff_Prompt.md` | Historical execution prompt for v2→v3. | Requests proof of joins, contains placeholders and older tag vocabulary. Its instruction to follow the plan is historical evidence, not a present task instruction. |
| `2026-08-22_Config_Audit.md` | Point-in-time analysis, not final policy. | Explicitly says numbers have not been written into Config; proposals need owner choices. Some recommendations were later adopted according to architecture §12; others remain unresolved. |
| `01.1_Gentry_ReturnType_Dependent_Dropdown.gs` | Container-bound Google Sheets validation automation source, 111 lines. | Intended `Sheet1!J→M` dependency, lists in `Lists!N/O/P`; setup instruction. Presence does not establish whether deployed script/validation still exists today. |
| `_superseded/03_SOP_Hadeer_Returns_Calls.docx` | Old Support SOP v1.0 19 Aug. | Returns only; old approximate taxonomy selection and duplicate handling help explain later drift. Not current authority. |
| `_superseded/04_SOP_Omar_Weekly_Routine.docx` | Old Operations SOP v2.0 19 Aug. | Four source workflow, explicit top-up field mapping, priority `P0` blocks; no pre-dispatch layer. |
| `_superseded/05_Hassan_How_To_Read_Your_Page.docx` | Old executive guide dated 19 Aug. | Courier-only page and eight decision families; later guide adds confirmation and store collection. |
| `reports/2026-09-08_Delivery_Operations_Review_Jul-Sep.docx` | Generated, edited narrative review as at 8 Sep. Supporting output, not canonical facts. | Four-page PDF counterpart. Jul/Aug comparison; Sep 1–6 partial. Contradicts older June completeness account and confirmation-value interpretation. Raw `metrics.json`/`narrative.json` inputs absent. |
| `reports/2026-09-08_Delivery_Operations_Review_Jul-Sep.pdf` | Four-page rendition of same review. | Visually checked all pages. Same tables and notes. Tables cross page boundaries, but no missing content was found. |
| `skills/gentry-weekly-report/SKILL.md` | Historical report-author workflow definition, not an instruction invoked for this investigation. | Two brief types, gates, action carry-over, partial-week rules, draft approval boundary. Implements agent/human judgments outside Python, not an autonomous job. |
| `skills/gentry-weekly-report/references/report_structure.md` | Supporting template for CEO/Ops briefs and action sidecar. | Specifies ordering, no customer data, one owner decision, action IDs/owner/due/effort/refs/success. |
| `skills/gentry-weekly-report/references/writing_rules.md` | Supporting attribution and interpretation rules. | No invented benchmarks; provisional targets, channel and small-sample caveats. |
| `skills/gentry-weekly-report/evals/evals.json` | Two qualitative example prompts with expected outcomes. | Not executed tests, no test results, both have empty `files`; no proof of report correctness. |
| `skills/gentry-weekly-report/scripts/extract_metrics.py` | Workbook→JSON KPI/worklist extraction, static inspection only. | Cached recalculation copy; fixed sheet/cell coordinates, 2,000-row worklists. Includes a customer field contrary to its privacy declaration. |
| `skills/gentry-weekly-report/scripts/actions.py` | Read/write action JSON sidecars. | Loads lexicographically latest `*_actions.json`, optional earlier-date cutoff; saves payload. Does not validate status/schema or independently decide completion. |
| `skills/gentry-weekly-report/scripts/make_chart.py` | Trend chart renderer from confirmation JSON. | Optional `--drop-last`, coverage/dispatch, provisional target line. Null plot values become zero. No actual partial-week detection. |
| `skills/gentry-weekly-report/scripts/report_kit.py` | DOCX presentation helper library. | Rendering/colour/format helpers, not extraction logic. Exactly identical SHA-256 to delivery-report copy. |
| `skills/gentry-weekly-report/scripts/__pycache__/report_kit.cpython-310.pyc` | Generated Python 3.10 bytecode cache metadata. | Timestamp header 4 Sep 2026 22:17:55 UTC; source size 10,766. Not loaded/executed or used as business authority. |
| `skills/gentry-delivery-report/scripts/extract.py` | Later monthly delivery/operations metrics extractor. | Recomputes much logic from raw sources instead of using workbook dashboards; gates coverage and current calendar month. Several differences from spec/weekly extractor. |
| `skills/gentry-delivery-report/scripts/build_report.py` | Review DOCX assembler from metrics + externally authored narrative. | Nine required narrative slots; outputs report/chart, does not update report state despite state comment. No source SKILL.md for this report family exists. |
| `skills/gentry-delivery-report/scripts/report_kit.py` | Duplicate presentation library. | Byte-identical to weekly kit, SHA-256 `5246fc773f7f5f602b517de57529309e6c208ccae429e8aa51c34bfc9e6b73b3`. |
| `skills/gentry-delivery-report/scripts/__pycache__/report_kit.cpython-310.pyc` | Generated bytecode cache metadata. | Timestamp header 8 Sep 2026 15:03:37 UTC; source size 10,766. Different cache bytes can reflect embedded compilation location; no business version inferred. |
| `skills/gentry-delivery-report/state.json` | Report history/next-period sidecar, supporting state. | One 8 Sep history entry, next period `2026-09-01`, June missing-page account. Historical commentary; not a current production scheduler. |

Source-protection instructions override historical handover comments suggesting deletion of superseded files/backups. No deletion occurred.

## System and domain reconstructed from these artifacts

The historical system is a single apparel merchant operation, GENTRY, combining Shopify orders/tags, Bosta deliveries and wallet fees, a Google Sheets returns call log, and a SKU price/cost list in Excel. No supplied non-workbook artifact establishes tenancy, merchant-specific configuration partitions, application login roles, API handlers, database tables, actual web-service technology or cloud background jobs.

| Concept | Identity, grain and relationships | Exact evidence |
|---|---|---|
| Merchant/business | One named business GENTRY. Owner is Hassan; Operations Manager is Omar; Support is Hadeer as historical holders, not immutable identities. | Handover 12; architecture 184–195; current SOP P4. |
| Shopify order | Unique `Name`/order reference `#NNNN`. Shopify export is line-item grain; `Orders_Master` is one row per order, 24 columns. | Architecture 281–285, 372–373; handover 47–48, 87–89. |
| Bosta shipment/leg | Tracking number as text. One order can generate multiple legs; shipment master 55 columns. `SEND`, `RTO`, `CUSTOMER_RETURN_PICKUP`, `EXCHANGE_return` are distinct types. | Architecture 89–98, 135–144, 285; handover 87–89. |
| Order→shipment | Shopify Name matches Bosta Business Reference Number, not tracking. Historical 227/234 match claim; misses before Shopify export window. These rows were not reverified here. | Architecture 281–285; handover 111. |
| Return/call-log intake | Return log `order ID` means Bosta tracking number, not Shopify order reference. A row retains free-text customer reason, contact outcome, attempt count, root cause, fit detail, resolution. | Architecture 110–123, 282; Support T15. |
| Customer | Legacy repeat-customer identity keyed by phone; two numbers can appear as two customers. Customer identity is not proved globally unique. | Architecture 218. |
| Contact attempt | Return attempts stored as a number; confirmation attempts encoded by `1/3`, `2/3`, `3/3` tags, replace previous tag. No event timestamps or attempt entities established. | Architecture 157, 305; Support T6R1. |
| Root cause and owner | Separate from courier reason and call reach status. One root-cause category maps to Product, Customer, Courier, Ops or Unknown. | Architecture 150–159; Support T17/T18. |
| Variant/SKU | Variant label must match Bosta Description exactly; source Shopify price/cost, 51 historical variants. Parses at most four item slots in original shipment master. | Architecture 96, 125–127. |
| Fee line/cost ledger | RAW_Costs Order Id joins tracking; multiple fee lines should sum; actual fee overrides modeled rate card. | Architecture 100–102. |
| Financial outcome | COD amount may be zero on returned legs; valued via SKU price then measured AOV proxy. Shopify paid/voided/refunded used to infer pickup outcome. | Architecture 219, 404; Owner T8/T12. |
| Pickup | Recorded shipping method `90 Office`; inferred unrecorded pickup has paid, not cancelled, no Bosta row, not office method, beyond 2-day settling window. | Architecture 313–318. |
| Operational action | Weekly report sidecar action has ID, action, owner, due, effort, optional refs and success condition. Human/agent determines DONE/OPEN/SLIPPED/DROPPED. | Weekly structure 120–136, kit 134–152; actions.py 17–40. |

The artifacts describe manual joins and classification, not a separately proved shipment parent/child foreign-key implementation. Distinguish shipment legs from unique order outcomes; never count order confirmation once per shipment.

## Intended historical business rules and workflows

### Confirmation

Support SOP T4–T8 prescribes calling every new order before dispatch. After actually reaching a customer who says yes, apply exactly `Confirmed` in Shopify. Tag attempts `1/3`, then replace with `2/3`, then `3/3`. After three failed attempts, stop, leave unconfirmed, and flag to Operations (T23R7). A confirmed tag must never mean merely tried/reachable. This is an intended manual transition from unconfirmed to confirmed after a successful conversation, not proof of a production dispatch-blocking validator.

The plan originally proposed `confirmed by omar`. Final architecture says the observed exact tag is `confirmed omar`; it takes precedence (289–305). Final confirmed-by categories include `Hadeer / auto`, `Omar`, `n/a`; the human-versus-automation distinction inside `Confirmed` remains ambiguous.

Architecture 340–342 fixes Hadeer coverage denominator as all placed orders, excludes Omar from her numerator, and says Whappi is its own segment. The documented 59.2% is 209/353 Hadeer-or-auto orders. Intervention 9.9% is 23/(209+23), not 23/353, as Support T21R3 explains. The later monthly extractor instead calls all tagged Hadeer-plus-Omar orders confirmed coverage. These are different metrics despite the common label.

No `confirmed_at` source was found in supplied final specs; time-to-confirm was only a historical plan field. Whappi cannot be assumed to record decline: architecture says the export contains failure-to-reach/error tags but no Whappi-cancelled tag, and no `Cancel Reason` column.

### Fulfilment and cancellations

The final intended four-way order classification is Bosta courier, recorded office pickup, inferred unrecorded office pickup, never fulfilled (handover 109, architecture 313–318). Recorded pickup is identified by `90 Office`; inferred pickup relies on payment/no cancellation/no Bosta and a 2-day settling exclusion. These are historical inference rules, not proof that such orders physically reached the customer.

Pre-dispatch cancellation remains separate from post-dispatch RTO. The first avoids courier costs; the second carries freight waste (architecture 21, handover 108–110). `bosta_sync_failed` does not by itself mean actionable courier failure: architecture 304 says 12/17 such tags were office pickup, where non-sync was correct.

The source lists outbound and return types but does not enumerate every allowed shipment state transition or triggering event. `SEND` means normal outbound attempt in the spec; no evidence authorizes assuming all SEND rows are completed delivery.

### Return contact and resolution

Support routine T10–T14: locate uncalled returns, oldest first by column A, call column C, fill K–O and preserve customer's meaning in free-text F. J is Operations-owned return type. K is contact outcome; L attempt count. M may be populated only when K = Reached; N supplies fit direction when relevant; O records resolution.

Contact values: Reached, No Answer, Phone Off, Wrong Number, Refused to Talk, Number Unreachable (Support T16). Resolution values: Pending, Exchange requested, Exchange completed, Refund issued, Reshipped, Customer lost, Not recoverable (Support T19). These are field values, not a proven enforced graph of allowed transitions. Recording Refund issued is not evidence the workbook issues a payment. Exchange completed is defined by the SOP as replacement gone out, not delivery completed.

The SOP explicitly forbids editing A–E, deleting a return row, or guessing M when not reached (T18/T20). Current version escalates new taxonomy needs instead of the old version's instruction to choose nearest existing cause and explain in F. Customer free-text reason is kept unrestricted. Categories are extended in Config and mirrored to Lists under Operations control and logged in Change_Log (architecture 150; old Operations T16R2).

Two human confirmations remain required in historical evidence: two genuine legacy resolved returns need a chosen exchange/refund/reship resolution; three apparently delivered-and-kept records lack a Kept/not-return taxonomy value (audit 54–68; architecture 249). Their tracking identifiers/customer text are deliberately omitted here.

### Pickup shelf

Operations SOP P6–P8 and architecture 334 prescribe daily inspection: after 3 days call the unclaimed pickup; at 7 days recommend/manual cancel to release stock. Source describes amber/red action recommendations, not automatic cancellation. No-show financial inference is paid→collected, voided/refunded→no-show (architecture 404). Open pickups are excluded from resolved no-show denominator. Inferred unrecorded pickups must stay outside that recorded no-show denominator.

### Weekly ingestion and quality gate

Operations SOP T2–T11 prescribes all-status Bosta delivery export, values-only RAW_Bosta A3 paste; Cash Cycles wallet→RAW_Costs; Shopify orders including cancelled→RAW_Shopify A3; top-up new returns in call log; duplicate check S; notify support; download and paste intake; add new SKU variants; full Ctrl+Alt+F9 recalculation. The original named-person SOP additionally provides top-up mapping Created At→A, customer name→B, phone→C, tracking→D, Description→E, return type→J (old Operations T5).

The report eligibility gate is BLOCKED→fix missing core inputs and withhold CEO report; USABLE WITH CAUTION→report with explicit gaps; CLEAN→normal report. If Config channel reconciliation is not YES, stop reporting v3 metrics (Operations T12; weekly SKILL 58–66). These are instructed behaviors; extractors themselves still write JSON and do not implement a complete hard stop for every gate.

Read Data_Quality before Ops dashboards. Monthly update SKU prices/costs and verify unrecorded pickups near zero; quarterly review taxonomy/change log/city map/tag vocabulary. New source tag spellings can silently zero a KPI. Historical workbook master limits are 2,000 rows per refresh; formulas must be extended rather than assumed dynamically unbounded (Operations T20R10).

### Decision authority and escalation

Operational ownership is historical, not verified web authorization. Support works calls/tagging, Operations owns Config/paste zones/taxonomy and prepares briefs, Brand Owner makes product, supplier, payment policy, COD restrictions, courier negotiations and staffing decisions. Brand Owner is not supposed to receive raw rows (architecture 184–195; Owner T11–T13).

Escalation triggers: two consecutive red RTO weeks, product return >50% on meaningful volume, returns/gross-margin movement >5 points, courier case, reason capture <75%, confirmation coverage <60% for month, unrecorded pickups reappearing (Operations T21). Support flags repeat third return, courier never-called claims, recurring product faults, damaged items, repeated taxonomy misses, failed three-attempt confirmations, or office collection request (Support T23). COD/prepaid switching and financial claims are proposals requiring owner decision, not automatic actions found in artifacts.

## Calculations and metric definitions

| Metric | Inputs and meaning | Missing/period caveat and evidence |
|---|---|---|
| Outbound volume | SEND + RTO types constitute outbound denominator; post-delivery pickup and exchange legs excluded. | Do not merge order and shipment grain; architecture 135–144. |
| RTO rate | RTO count / outbound count. | Null if zero denominator; architecture 142; delivery extract 123–130. |
| Customer return rate | Post-delivery customer returns / delivered orders. | Different denominator from RTO; architecture 143. |
| First-time-right/kept | (outbound − RTO − customer-return count) / outbound. | Product-return legs can belong to different original order dates; source does not prove cohort matching. Architecture 144; delivery extract 131. |
| Hadeer coverage | Hadeer-or-auto-confirmed count / all orders placed. | Omar excluded from numerator; Whappi said separate; architecture 340–344. |
| Monthly total confirmation coverage | (order count − confirmed_by n/a) / order count. | Includes Omar; not comparable without naming definition. Delivery extract 143–148. |
| Omar intervention | Omar / all confirmed (Hadeer-or-auto + Omar). | Historical 23/232=9.9%, Support T21R3. |
| Pickup no-show | Recorded no-shows / (collected + no-show). | Open and inferred unrecorded excluded. Historical 10/24=41.7%, CI 24.5–61.2 stated spec 332. |
| Reason capture and reach | Historical 37/104 returns with known cause/reached in audit. | Conditional reasons-of-reached 100% is a different denominator; audit 25–26 vs Support T21. |
| Return value | SKU pricing, fallback measured AOV when Bosta zero COD. | Proxy must be flagged; architecture 219. Monthly script instead uses Shopify order-value lookup only and skips unmatched values. |
| Net contribution | Revenue paid-and-kept − supplier goods cost − all courier fees − Paymob fees on prepaid. | 1.7% comparison in Owner T12R2 is historical stated payment fee, not current verified pricing. Owner T8. |
| Monthly coverage gate | Count wallet tracking IDs with Bosta row / count wallet tracking IDs, grouped by wallet completed month. | Fixed >=90% threshold; missing month coverage is not rejected. Delivery extract 96–116. |
| Monthly delivery rates | Group Bosta rows by Created At month; count SEND as delivered, RTO returned. | Uses types, ignores loaded Delivery State; future/stale partial-month handling weak. Delivery extract 118–133. |
| Average attempts | Mean numeric Number Of attempts over every monthly Bosta type. | Includes customer-return/exchange legs, not just outbound. extract 127–133; difference from spec needs workbook comparison. |
| Confirmation outcome test | Bosta orders with outbound outcome Delivered/RTO grouped by confirmer; compare failure proportions using pooled z test. | Current script uses Wald 95% CI clipped to [0,1], not Wilson/Fisher. September partial included in sample. extract 41–52, 149–168. No causal claim supported. |
| Product return rate | Aggregate parsed Bosta line units: shipped SEND+RTO; back RTO+customer-return+exchange; only products shipped >=10 in comparable months. | Filters size suffix, ignores blank Description, does not link returns to original shipment cohort, repeated legs may double-count units. extract 170–189. |
| Most ordered products | Shopify line units grouped by source order creation month and size stripped. | All qualifying Shopify line items included; cancelled orders not excluded in this script. extract 170–177. |
| Monthly courier spend | Sum looked-up fee for each Bosta row in creation month. | Does not include wallet-only shipments; repeated wallet lines last-wins instead of sum; missing fee→0. extract 86, 192–205. |
| Spend on returns/share wasted | Fees on RTO rows / fees on all Bosta rows. | Customer-return/exchange fee excluded from numerator although label says returns broadly. extract 199–205. |
| Monthly value not converted | Sum full Shopify order-value for each RTO row with matched order reference. | Duplicate RTO legs can repeat order value; unmatched/no numeric value contributes nothing and is not marked missing. extract 193–205. |

Weekly buckets are intended Saturday-start. Skill says compare last two complete weeks and remove partial tail, mark stale (>about ten days) report at top (weekly SKILL 68–74). Monthly report says September 1–6 is incomplete and not comparable. The source scripts do not enforce these intentions completely; details below.

Historical Config thresholds from audit lines 22–31: RTO green .10/amber .15; customer return .05/.08; average attempts 2/2.5; reason capture .90/.75; reach .70/.55; recovery .25/.15; cycle days 6/8; queue age 2/3; unmapped cities 0; unpriced SKU 0. These are internal targets, not external benchmarks. Three later v3 thresholds are explicitly `[CONFIRM]` (coverage 60%, intervention 15%, pickup no-show 30% in SOP guidance); setting/approval remains unresolved in the documents.

## Static automation reconstruction

### Google Sheets dependent dropdown

`01.1...gs` lines 25–38 configures Sheet1, Lists, J10, M13, first row2. Return-type label mapping is hardcoded to column letters: Failed delivery (RTO)→N, Returned after delivery→O, Exchange return leg→P. Cause values are configurable in Lists N2:N100/O2:O100/P2:P100; fallback full cause list A2:A26. Thus values are sheet-driven, but type→column routing and limits are code-driven.

`onEdit` lines 40–55 only responds to manual edits touching J on Sheet1, including UI multi-row paste. It applies M validation per touched row. Any error is swallowed so typing is not blocked. API import will not fire onEdit per its setup comments; `backfillAllRows` must be manually run afterward. Bulk routine lines 79–110 preloads lists, determines last true data row from D rather than formula-padded sheet row1001, then batch sets validations M2:last.

`setAllowInvalid(false)` rejects future off-list input. The script never clears/reclassifies an existing M value when J changes, never inspects K call status, and does not enforce the only-Reached root-cause rule. Actual Spreadsheet permissions/protection are outside this code. No evidence this script performs refund, shipment creation or customer communications.

### Weekly report family

`extract_metrics.py` searches parents for one non-BACKUP/non-lock workbook, fails on ambiguous candidates (51–71), copies it to temp then invokes LibreOffice and reads recalculated cache (22–37, 74–75). It does not write original workbook. It maps fixed coordinates across Data_Quality, EXEC_Brand, Config, Confirmation and Pickup_Channel. `_missing` records None/absent sheet for g() reads, but direct accesses are not consistently checked. It does not delete its temp directory.

Working lists read only master rows4–2003: unknown-cause returns sorted oldest by shipment Created date, high attempts by `HIGH-ATTEMPTS`, unconfirmed/not-dispatched excluding cancellation and both pickup channels, unrecorded pickups, and order audit flags (219–293). Unknown-cause return age is time since shipment creation, not proven return-received age or time since last contact.

`actions.py` saves/loads a JSON sidecar and creates reports directory even on load (24). Latest file chosen by filename, optional before-date. Completion logic is specified for report author but not computed by script. No action sidecars are present in source inventory, so first-run behavior/history cannot be reconstructed beyond these instructions.

`make_chart.py --drop-last` removes final array item if there are >1 items, without checking its date/partial status (25–26). It converts missing coverage/dispatch to 0 (31–32), colours provisional coverage threshold as target (38–40), and skips <2 weeks. Report_kit only formats content; it does not send messages. `message_block` creates draft text inside a document, not an integration.

### Monthly delivery review family

`extract.py` recalculates a copy, loads Bosta, wallet, Orders_Master and Shopify. It reads report state to choose period start (67–70). It parses Bosta MM-DD-YYYY strings, wallet date objects, and fixed raw column offsets rather than header-driven RAW schemas. It gates wallet-completed-month coverage below 90%, except no coverage entry passes. Months considered come from Bosta creation dates, and current execution calendar month alone is labeled partial (104–116).

`build_report.py` requires nine narrative slots, no comparable months→exit, takes quantitative inputs from JSON and authored prose from narrative. Fixed numeric assumptions remain outside Config: delivery row red at >30%, product RAG .25/.35, product >=10 threshold and coverage .90 in extractor. It writes DOCX plus trend PNG; no PDF conversion, state update, scheduler, email or other messaging is implemented. Narrative can contain typed numbers; code does not verify prose against metrics.

The builder's delivered-and-kept/rate language and chart use raw-script definitions, not necessarily the workbook definitions. All displayed report observations must be attributed to the 8 Sep output and not generalized to today's product.

## Contradictions, limitations and reconciliation candidates

| ID | Finding | Evidence and present classification |
|---|---|---|
| TXT-D01 | June completeness explanation reverses. Older spec says Bosta is complete and June absence is office collection/onboarding; September review says partial paginated export and only 43% coverage, re-pull/restatement pending. | Architecture 358–366; report P40/PDFp4; state history. `UNRESOLVED`, preserve both rather than pick later narrative without dataset verification. Period windows changed and may contribute. |
| TXT-D02 | Confirmation's stated business value differs. Spec/SOP says conversion to dispatch, not lower RTO; review dismisses the control as changing nothing because RTO difference is not significant. | Architecture 346–356; Support T1/T3; report P7, P24–25/T11. `UNRESOLVED interpretation`: no causal experiment, and conversion benefit was not recomputed by monthly script. |
| TXT-D03 | Same confirmation-coverage label uses Hadeer-only vs Hadeer+Omar numerator. Owner guide even says someone called. | Architecture 340–344; Support T21; Owner T4R2; delivery extract 143–148. `VERIFIED artifact metric-definition conflict`. |
| TXT-D04 | `Confirmed` is human-only in Support SOP, but master spec and script aggregate `Hadeer / auto`; Whappi should be separate yet attribution cannot be separated by this field. | Support T5/T8; architecture 266/293/340–342; extract 156. `UNRESOLVED attribution`. |
| TXT-D05 | Privacy promise contradicts weekly extraction of customer name from pickup queue. | Handover141, skill38, weekly extractor181 versus215–218/290–292. `VERIFIED static code conflict`; actual presence of names depends on workbook cell. No customer values extracted by this investigation. |
| TXT-D06 | Multiple wallet fee lines should sum but monthly extractor overwrites per ID, last value wins. | Architecture102; extract86. `VERIFIED static discrepancy`; extent of monetary error requires duplicate-line inspection. |
| TXT-D07 | Monthly extractor calls every SEND delivered; spec uses Delivery State for delivered/returned classification. | Architecture91/137; extract79 reads state but123–131 never uses it. `VERIFIED static discrepancy`; live outstanding SEND population unresolved. |
| TXT-D08 | Missing monetary inputs become zero or disappear in monthly extract, versus missing-as-missing contract. | Handover107; extract86/199–203. `VERIFIED static discrepancy`. All-wallet/complete-order lookup may mask it on one snapshot. |
| TXT-D09 | Monthly script gates partialness by today's month, not source watermark; rerunning September snapshot in October can call September comparable. | extract107–116. `VERIFIED static behavior`; no rerun executed. |
| TXT-D10 | Monthly confirmation statistical groups include partial September although stated not comparable. | extract149–168 uses comparable+shown; report P43/PDFp4. `VERIFIED analysis-window discrepancy`; effect sample mixes Jul–Sep. |
| TXT-D11 | State says builder reads and writes state after success; builder has no state reference/read/write. | state `_comment`; extract67–70; builder58–169. `VERIFIED documentation-code mismatch`. |
| TXT-D12 | Queue age said actively measured in SOP but audit says no return-received/called timestamps and no computed metric. Weekly list age uses shipment Created date. | Support T21R6; audit29; weekly extract237/243. `UNRESOLVED operational clock`. |
| TXT-D13 | Uncalled queue changed from empty K to K–O empty, potentially excluding partially populated rows. | Old Support T3 versus current Support T10. `UNRESOLVED exact queue filter`. |
| TXT-D14 | Root-cause-only-when-Reached is human instruction, not enforced by supplied dependent-dropdown code; J changes preserve old cause. | Support T18; gs40–71. `VERIFIED static gap`, actual Sheets formulas/other validators not inspected here. |
| TXT-D15 | Architecture says Support writes J–Q, but its schema/SOP reserve J to Operations and P/Q optional. | Architecture114/120/191; Support T15R2. `VERIFIED role-boundary inconsistency`; current SOP narrower. |
| TXT-D16 | Target agreement ambiguity: three Config17 targets `[CONFIRM]`, while executive guide presents 60%/30% as firm worry lines and Operations escalation hardcodes 60%. | Architecture408; Owner T4; Operations T21R7; Support T21 includes flags. `UNRESOLVED target authority`, do not treat as approved policy. |
| TXT-D17 | Base spec says three fulfilment channels; final addendum/handover establish four with inferred pickup separate. | Architecture20/270–273 vs313–318, handover109. `Historical supersession`, keep fourth channel explicitly marked inferred. |
| TXT-D18 | Base spec's missing descriptions are presented as preventable entry error; audit says all twelve are structural customer-return pickups. | Architecture221; audit84. `UNRESOLVED discrepancy`, source dataset can verify distribution, Bosta source behavior needs live/source confirmation. |
| TXT-D19 | Low reach explanation drifts from queue not entered/not called to wrong checkout numbers as asserted fact. | Old Support T14/T15; audit26; current Support T21/T22. `UNRESOLVED cause`, low reach does not prove wrong numbers. |
| TXT-D20 | Absolute lack-of-effect prose is stronger than statistical evidence. P>=.05 with n=30 unconfirmed does not establish no effect; observational selection confounds personal comparisons. | Report P24–25; builder126–129; extract41–52/149–168; spec356. `Inference risk`, preserve nonsignificant result with sample/CI rather than causal certainty. |
| TXT-D21 | Product back numerator combines RTO/customer-return/exchange legs and no cohort linking; can include repeat physical units. | extract178–189; report T8/P29. `VERIFIED metric grain`, unique physical-return rate unresolved. |
| TXT-D22 | Average attempts in later review includes all shipment types, whereas base architecture/effective headline is outbound operational metric. | extract127; audit24 distribution. `UNRESOLVED denominator equivalence` needs workbook formulas. |
| TXT-D23 | Fees reported as spent on orders that came back count RTO only, contrary to broadly labeled return spend. | extract199–205; report T10/P34; architecture distinguishes return channels. `VERIFIED metric meaning`, compare separately to total all-return economics. |
| TXT-D24 | Handover says both scripts already drop trailing week; chart requires explicit flag and extractor merely dumps all weeks. | Handover147; weekly extract155–163; make_chart21–26. `VERIFIED prose overstatement`. Last item need not be partial. |
| TXT-D25 | Report claims source includes call log, but monthly extractor never reads RAW_Intake/root-cause fields; body admits minority called then action asks to call all 86 with no cause. | report P3/T4/T12R4; extract76–94/135–138. `VERIFIED source/action support gap`, actual uncalled population must come from call log. |
| TXT-D26 | Latest report and supplied builder are not exact reproducibility pair. Report's reason table has interpretive fourth column, September labels explicit 1–6, custom narrative and multi-action ask; builder produces three-column reason table and generic partial labels. Metrics/narrative JSON inputs absent. | Report T3/T2/T12; builder94–119/155–165. `VERIFIED output/code divergence`, manual or older/newer generator version possible. |
| TXT-D27 | Hardcoded report thresholds conflict with every assumption in Config intent. | Architecture17/handover106; extract17/189; builder99/142. `VERIFIED historical implementation variance`, not authorized to change now. |
| TXT-D28 | 48 inferred pickups called true pickup total in older spec overstates certainty of physical outcome. | Architecture315 marked INFERRED vs330 says true. `Inference wording risk`, maintain inferred channel label. |
| TXT-D29 | Absence of cancel reason/Whappi-decline source supersedes plan's proposed cancel-reason field. | Plan§3/§5 vs architecture300–303. `Historical corrected assumption`, no software feature can be presumed from plan. |
| TXT-D30 | Source global `one join key tracking` principle is stale for Shopify layer, which needs order reference, plus line-item/order/shipment grains. | Architecture16 vs281–285, handover111. `Historical corrected statement`, preserve two bridges. |
| TXT-D31 | Return calling priority differs: current supplied SOP says oldest first; generated 8 Sep report assigns failed delivery callbacks newest first. | Support T11R1; report T12R4/PDFp4. `UNRESOLVED queue-policy change`, the report does not explicitly amend SOP. |
| TXT-D32 | The return SOP does not specify a maximum No Answer retry count; the three-attempt ceiling belongs to pre-dispatch confirmation. | Support T6/T7/T23R7 versus return T16/P31/T20. `VERIFIED document scope`; any live two-NoAnswer terminal rule is a separate live-only rule until corroborated. |

Other observed document differences are dates/snapshots rather than automatically contradictory facts: 212 historical outbound shipments versus 213 unique Shopify orders with any Bosta reference, 237 shipments versus 220 order references, older 353 order export versus later review order counts. They use different populations and dates. Do not reconcile them by equating numbers.

## Current-app verification checklist guided by artifacts

1. Verify whether live order and shipment identities preserve Shopify reference and Bosta tracking bridges, and whether imports reject/coerce numeric tracking values.
2. Inspect confirmation status/attribution, attempt tags/events, and dispatch guards without sending messages or changing consequential records.
3. Inspect live return contact fields, allowed root cause conditional validation, existing invalid data, resolution semantics and whether financial actions are separate from mere records.
4. Inspect pickup financial inference versus explicit outcome, ageing reference timestamp, thresholds and action side effects; cancellation requires authorized consequential experiment if not otherwise observable.
5. Trace live cost joins, fee line aggregation, missing-input suppression, refund/payment metrics, and unique order/leg denominators.
6. Verify import and scheduled job behavior, export windows/status filters/pagination, rate-card overrides, tagging integration errors, duplicate handling and source provenance.
7. Inspect actual live user roles/access and audit events. The three historical role names do not establish authentication or permission enforcement.
8. Compare live metric populations to the source's Hadeer-only/total confirmation distinction and SEND/delivered ambiguity; require explicit date windows and statuses.
9. Confirm June completeness using current historical wallet/delivery populations and importer pagination; do not promote either contradictory account uncritically.

## Confidence

High confidence in supplied artifact identity, historical intended workflows, direct static script logic, report text and contradictions listed above. Medium confidence that these artifacts describe the historical workbook business meaning consistently, because several definitions diverge across versions. No claim of current web behavior, current integration installation, agreed thresholds, live financial truth or causal performance effects is made from these files alone. A final SHA-256 check confirms all 28 inspected source files match their initial read; static parsing of all seven supplied Python files passed without execution. Supplementary OOXML inspection found no header/footer/footnote/endnote text, nested tables or textboxes omitted from the extracted SOP/report evidence.
