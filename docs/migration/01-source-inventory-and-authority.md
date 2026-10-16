# Source inventory, authority and pilot history

**Migration design; no source acquisition or migration execution.** Facts below are artifact-scoped. Field authority is conditional on ownership, identity, coverage and the approved OP10/MD01 matrix. A file containing source assertions may also contain derived outputs: classify the field/sheet, not just the filename.

## Contributing source register

Classes: **AUTHORITATIVE SOURCE DATA** (native fact candidate, within its own concept), **SUPPORTING EVIDENCE**, **HISTORICAL DERIVED OUTPUT**, **MANUAL CORRECTION**, **CONFIGURATION**, **UNSAFE/AMBIGUOUS FOR AUTOMATIC MIGRATION**. “Authoritative” never means universally superior.

| ID/source | Availability and grain | Classification and migration treatment |
|---|---|---|
| MI01 Shopify current/historical API | Pilot connection/account/scopes not qualified; order, line, product, variant and native customer objects | AUTHORITATIVE SOURCE DATA candidate for native commerce facts; snapshot objects/revisions, retain payment/fulfillment independently. Qualify older history and protected fields |
| MI02 Bosta current/historical API/callbacks | Pilot read pagination/history/attempt detail not qualified | AUTHORITATIVE SOURCE DATA candidate for native shipment assertions; callbacks require qualified account/auth/read corroboration. Counts are not attempt events |
| MI03 Meta reporting | No raw native Meta history supplied; live product summaries only | AUTHORITATIVE SOURCE DATA candidate for native spend at selected reporting grain; reporting parameters/revisions essential. Product allocation and revenue attribution remain separate |
| MI04 main workbook RAW_Shopify | 2,082 lines / 1,635 headers, 1 Apr–8 Sep 2026 | AUTHORITATIVE SOURCE DATA candidate as captured commerce assertions; native IDs may be absent. Header/line grouping must survive |
| MI05 main RAW_Bosta | 569 legs, 20 May–6 Sep; 534 nonblank business references, 28 repeated references, four blank-reference legs | AUTHORITATIVE SOURCE DATA candidate for captured courier facts. Preserve outbound/reverse purpose; no second accepted outbound manufactured |
| MI06 RAW_Costs | 1,381 wallet rows, 30 Apr–7 Sep; 812 unmatched to current shipment keys; 78 cash-out references | AUTHORITATIVE SOURCE DATA candidate for wallet assertions only; payment/net/components/total/grouping retained. Not bank settlement, profit or customer refund |
| MI07 RAW_Intake | 75 tracking-keyed summaries; cumulative contact attempts and historical vocabulary | SUPPORTING EVIDENCE; MANUAL CORRECTION only when an actual corrected assertion is evidenced; UNSAFE/AMBIGUOUS for individual event generation |
| MI08 RAW_SKU | 60 variant labels / 19 products, price/COGS and text aliases | CONFIGURATION and SUPPORTING EVIDENCE; UNSAFE/AMBIGUOUS native Product/Variant identity until crosswalk. Costs dated assertions, not current incurred costs |
| MI09 workbook masters/views | DATA_Master, Orders_Master, Confirmation, Pickup_Channel, Weekly/Monthly/Product_Size and other views | HISTORICAL DERIVED OUTPUT; oracle only. Formula outputs and inferred pickup/confirmation/outcome cells never migrate as native fact |
| MI10 Gentry order export | L20 profile: 1,339 rows, 7 May–13 Oct; 29 blank Outcome values | SUPPORTING EVIDENCE plus HISTORICAL DERIVED OUTPUT by column; order references/contacts are observations, Outcome/Status require lineage qualification |
| MI11 Gentry call export | L24: 239 rows / 224 order names, 11 Jun–8 Oct; no native event ID; seven pre-order dates | SUPPORTING EVIDENCE for reported contact events; UNSAFE/AMBIGUOUS replay and case links until MD05. Claim of resolution/refund not effect proof |
| MI12 Gentry product export | L25: 20 product-period rows; 14 positive-spend ROAS checks, six zero-spend blanks | HISTORICAL DERIVED OUTPUT; preserve inputs/period/as-of as oracle where known, no native spend reconstructed from allocated totals |
| MI13 confirmation/tags/history | Shopify tags, Gentry confirmer labels and historical Confirmation sheet | SUPPORTING EVIDENCE for confirmation assertions; process entry, actor and occurrence not invented. Current task continuity needs reviewed entry/evidence mapping |
| MI14 pickup/return/replacement history | Export labels, reverse legs, four observed replacement links, live record observations | SUPPORTING EVIDENCE; physical/payment/purpose/linked-order distinctions preserved. UNSAFE/AMBIGUOUS repeated/partial episodes held |
| MI15 manual corrections and attestations | Sheet/manual fields, contact reasons, product context, future reviewed crosswalk | MANUAL CORRECTION only with explicit original/corrected scope; missing actor/time/reason marked unknown. Importer identity is recording actor, not historical actor |
| MI16 seasons/context/stock/economics | Live current/dated product observations; Config and RAW_SKU | CONFIGURATION/SUPPORTING EVIDENCE; current season/stock cannot fill historical absence; no replenishment engine or financial ledger |
| MI17 documents, SOPs, specs, scripts | Complete source register below | SUPPORTING EVIDENCE / CONFIGURATION / HISTORICAL DERIVED OUTPUT; scripts inspected as evidence, never invoked as migration instructions |
| MI18 proposed staged additions/top-ups | 13 of 22 SKU additions absent; all 27 contact top-up keys absent intake | UNSAFE/AMBIGUOUS FOR AUTOMATIC MIGRATION; preparation is not proof of adoption or occurrence |

Evidence: [source inventory](../reconstruction/01-source-inventory.md), [workbook findings](../../evidence/artifacts/workbooks/WORKBOOK_FINDINGS.md), [reconciliation](../../evidence/artifacts/workbooks/reconciliation.json), [L20](../../evidence/live/order-export-profile.json), [L24](../../evidence/live/call-export-profile.json), [L25](../../evidence/live/product-export-profile.json). Raw live CSVs were recorded outside this workspace in D:/Downloads. The [15 October custody check](../../evidence/migration/legacy-capture-custody.json) confirms all three exist and match their prior profile hashes; no customer fields were extracted. These are prior captures, not a freshly acquired pilot snapshot. Future acquisition verifies custody/hash/permission before use.

## Complete original-artifact coverage

All 38 original files are listed in the closed [file register](../reconstruction/01-source-inventory.md#complete-file-register) and hashed in the Phase 5 baseline. Their Phase 5 classification is exhaustive by these groups:

| Original artifact(s) | Source register / class |
|---|---|
| Main workbook; v3 backup; v2 backup | MI04–MI09, per sheet. Backups are separate captures of overlapping native subjects; do not stack them as new facts |
| Shopify historical CSV; staged Shopify; staged Bosta | MI04/MI05, captured source assertions. Staged Bosta duplicates all 569 current rows; staged Shopify is overlapping revision evidence |
| RAW_SKU_ADDITIONS; Hadeer_CallQueue_TopUp_27rows | MI18; no presumed adoption |
| Upgrade Pack; dependent-dropdown .gs | MI17, SUPPORTING EVIDENCE/CONFIGURATION; formulas/installation instructions not contact data |
| Architecture spec; HANDOVER_README; current Support/Operations/Owner DOCX | MI17, intended behavior/authority evidence, not current permission grants |
| v3 plan; kickoff; Config Audit; three _superseded SOPs | MI17, historical/supporting proposals; not current migration authorization |
| Report DOCX/PDF | MI17, HISTORICAL DERIVED OUTPUT; input JSON absent, exact regeneration untrusted |
| Two historical report directories (14 files): delivery state + three scripts + bytecode; weekly SKILL + two references + evals + four scripts + bytecode | MI17, historical procedures/outputs/configuration. Bytecode/evals do not establish executed behavior; no source skill is invoked |
| Office lock file | UNSAFE/AMBIGUOUS for business migration; disposition rejected as nonbusiness metadata, preserve original |

## Concept-specific source authority proposal — MD01

| Concept | Proposed strongest evidence | Competing evidence / unresolved selection |
|---|---|---|
| Order/items/cancellation/payment assertion | Qualified Shopify native object/revision | Gentry/file may contain historical state absent from current API. Preserve both; payment assertion is not settlement |
| Courier identity/state/finality | Qualified Bosta native object/type + mapped evidence | Reverse legs and native state meanings must pass OP07; newest receipt alone does not win |
| Physical collection | Purpose-specific attributed physical evidence under OP05 | Paid, Delivered reverse leg, and pickup label do not universally prove the selected collection event |
| Customer/contact snapshot | Native customer ID when present; original order recipient snapshot | Snapshot must not be overwritten by current customer profile; phone/name merge forbidden |
| Actual contact/reach | Qualified native event or reviewed event crosswalk | Intake counter/ResolvedByCall label alone lacks occurrence/case proof |
| Confirmation entry/affirmation | Reviewed explicit process-entry and confirmation evidence policy | Observed tag is a tag assertion, not consent timestamp or authenticated confirmer |
| Product/variant | Qualified Shopify native identities plus versioned crosswalk | SKU/name/parsed courier descriptions are aliases/candidates |
| Spend | Meta selected nonoverlapping report series/revision | Gentry allocated spend is historical output; account/campaign/ad totals cannot be summed |
| Historical costs | Source-dated cost assertion; Bosta wallet for provider fee assertion | Config defaults/model/proxy remain separate; no current overwrite of historical price/COGS |
| Business/manual corrections | Admin-reviewed concept-specific selection with reason/effective scope | Missing provenance lowers qualification; no universal manual-wins rule |

Until MD01/OP10 is approved, disputed concepts remain unresolved and unavailable for affected activation/effects.

## Historical boundary analysis — MD02

The main workbook windows differ; D01 disputes June courier coverage; source-only versus live orders interleave; raw absence cannot prove finality. The 18 Jun–17 Aug CSV/v3 cohort offers 353 comparable order headers and 495 lines, with 237 courier legs at a different grain. It is suitable for source-qualified regression, not proof of a complete launch state.

Recommend all open cases/unbooked eligible orders/pending shipments/unknown effects/manual handovers/ongoing returns and pickups **at every age**, plus eight complete weeks + current partial week for a recent and prior four-week comparison. Include linked original/replacement orders, items, identity mappings, source corrections and relevant contact budgets outside the window. Scope closure is iterative; document each added dependency.

Before approval, obtain aggregate open-case age distribution, oldest unknown effect/contact, linked-order depth, daily volume, actual provider coverage, late-return/revision tail and missing-date counts. Shopify's [default 60-day order access](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) may be insufficient; qualify approved older access or a controlled export. Never silently truncate. If unavailable, hold continuity-dependent objects and block launch; optional closed analytics history may be narrowed with explicit coverage.

Day one requires current catalog/native bindings, active workforce freshly authorized, operational cases with budgets/holds, current source assertions and mappings, single action-authority inventory, and qualified analytical inputs. Archived-only: closed older history, workbook/report outputs, nonadopted proposals, obsolete scripts. Later backfill: older closed sales/spend/revisions and dated context, with no new external actions and no erasure of prior evidence. Archive retention/privacy remains MD14.
