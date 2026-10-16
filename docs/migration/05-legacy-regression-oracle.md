# Legacy Gentry regression oracle


## OR-INDEP01 — Avoid circular expected results

The report names how each expected source set, binding and value was established, including shared parser/mapping/selector dependencies. Fix expected sets before evaluating implementation output. Intake conservation uses independently enumerated raw units; capture closure uses an independently known source inventory; semantic proof uses reviewed source observations/crosswalks and deterministic golden facts. A validator that reuses the importer's selected objects cannot alone prove the selection correct.

Review every critical open obligation/unknown-effect/contact hold and an owner-approved evidence sample of closed history, without claiming statistical certainty from a small sample. A discovered false rule/match expands review to that rule's affected source group. Current Admin selection is a decision, not independent proof that a historical occurrence/identity was correct. This does not require a second production migration engine.
**Oracle scope:** the reconstructed source/workbook/system is a comparison reference, not canonical truth. Preserve [D01–D25](../reconstruction/13-live-vs-spec-discrepancies.md) and [formula evidence](../reconstruction/06-calculations-and-metrics.md). Never tune OpsHub to reproduce a known mistake.

## Comparison envelope

Each OR comparison fixes artifact hash/version, source/sheet/formula/row-group or route/profile, acquisition date, grain, namespace/mapping, cohort/timezone/interval/as-of, coverage, input revisions, legacy algorithm/version, OpsHub definition/policy version and expected relationship. Store **migrated fact**, **recomputed OpsHub interpretation**, **legacy Gentry result** separately, plus contributor differences and explanation/decision. Legacy observed UI, cached formula and independent reconstruction are different oracle methods.

Comparison readiness is universal under AC12. Execution of this historical oracle is applicable to the Gentry migration pilot; a new merchant does not inherit historical Gentry data.

## Catalog

| ID/comparison | Qualified legacy baseline / locator | Expected relationship and pass condition |
|---|---|---|
| OR01 raw commerce units | Main RAW_Shopify: 2,082 data lines / 1,635 nonblank Financial Status headers; v3/CSV 495 / 353 | **EXACT MATCH EXPECTED** for accounted source row/header sets before identity interpretation. Canonical accepted Orders may differ with explained collisions/exclusions; do not require 1,635 active Orders |
| OR02 raw courier population | Main/staged RAW_Bosta: 569 unique tracking rows, types SEND313/RTO210/customer-return26/exchange20; four blank business references | **EXACT MATCH EXPECTED** for retained assertion/disposition sets. Multiple captures do not double canonical shipments; 28 repeated business references are preserved |
| OR03 cross-snapshot overlap | Staged Bosta all 569 rows match; CSV/v3 all 495 lines/79 columns match; staged Shopify 476 references/664 lines with four revised orders | **EXACT MATCH EXPECTED** for equivalence/revision classifications under the frozen evidence, not “last file wins” |
| OR04 wallet/intake/catalog | Main 1,381 wallet rows, 75 intake summaries, 60 SKU aliases/19 products; 812 wallet-only IDs | **EXACT MATCH EXPECTED** for source sets and missing-link accounting. Canonical Customer/Variant/event counts are not inferred from these totals |
| OR05 final delivery counts | DATA_Master I / Orders_Master R; live640 kept of1,054 finalized business outcomes; Delivered courier export includes reverse legs | **EXPLAINED DIFFERENCE EXPECTED**: OD01/OD05 outbound courier result versus business kept result. Compare matched members/purpose/finality, never use kept count as delivery numerator |
| OR06 RTO | Config B136:D139 / DATA_Master group; monthly extractor every SEND delivered | **EXPLAINED DIFFERENCE EXPECTED** for source leg/group versus qualified outbound finality. **LEGACY RESULT NOT TRUSTED** when monthly SEND assumption or unknown original/reverse link governs |
| OR07 confirmation | Confirmation C13: current297/1,635 Hadeer/auto; v3 209/353; live802/1,339 all confirmed/all placed | **EXPLAINED DIFFERENCE EXPECTED**: OD05 process-entry denominator and independent actors. Unknown entry/consent time stays excluded from dated cohort, never manufactured to force equality |
| OR08 contact populations | L24 239 exported events/224 order names; dashboard59 answered/93 called and queue32 | **EXACT MATCH EXPECTED** for retained export event-row observations; **EXPLAINED DIFFERENCE EXPECTED** for canonical case reach/action ratios. Seven pre-order dates held/qualified; no invented importer fix |
| OR09 pickup | Orders_Master T / Pickup_Channel H9 paid→Collected; 547 inferred pickups; live44 collected vs43 Picked up + one Refused | **EXPLAINED DIFFERENCE EXPECTED** for OD02 physical-evidence population; **LEGACY RESULT NOT TRUSTED** as physical collection oracle where paid/inferred/refused semantics are unresolved |
| OR10 Product/SKU sales | RAW_Shopify items; live product period rows; historical parser four 180-char slots/single-digit quantity | **EXACT MATCH EXPECTED** on the same independently evidenced item contributors/amount basis; **EXPLAINED DIFFERENCE EXPECTED** if parser limitations/alias mapping/missing lines affect legacy output |
| OR11 Product/SKU delivery/returns | Product_Size description association and live product outcomes | **EXPLAINED DIFFERENCE EXPECTED**: distinct outbound association, overlapping product presence, post-receipt return separately. No item return/causal claim from order-only return |
| OR12 native versus product spend | Live own/generic allocations, 20 product rows; native Meta report not supplied | **LEGACY RESULT NOT TRUSTED** as exhaustive native spend/attribution oracle; compare displayed components as archived outputs only. Require independently qualified report and conservation |
| OR13 ROAS arithmetic | L25 fourteen positive-spend rows satisfy (gross-discounts-returns)/(own+generic); six zero-spend blanks | **EXACT MATCH EXPECTED** for arithmetic on those identical frozen inputs, method and rounding. **EXPLAINED DIFFERENCE EXPECTED** for qualified OpsHub revenue eligibility/reversal/period/spend basis; equality cannot certify attribution |
| OR14 fees/economics | DATA_Master AI/AJ; independently reproduced joined fees55,951.05 EGP vs all-wallet134,233.55 EGP | **EXACT MATCH EXPECTED** for matching input-scope sums; **EXPLAINED DIFFERENCE EXPECTED** for excluded/missing fee basis; **LEGACY RESULT NOT TRUSTED** for last-wallet-wins/missing→0/proxy profit |
| OR15 calendar/age | Saturday shipment-created weeks vs live Monday order-placed; max-export-date pickup ageing | **EXPLAINED DIFFERENCE EXPECTED** under approved cohort/current-clock semantics. Separate calendar-only rebucketing from changed population |
| OR16 v2 bounded cached checks | Twelve Config cached outputs C34,C36:C38,C40,C166:C172 agree with independent reconstruction within1e-9 | **EXACT MATCH EXPECTED** only for replay of those same inputs/formulas. This tolerance is a historical numerical check, not a production money/contributor tolerance |
| OR17 current/v3 formula outputs | No cached formula results; 167,678 current formula cells | **LEGACY RESULT NOT TRUSTED** as observed calculated values. Independent reproduced results are labeled as such; no source recalculation/macro execution |
| OR18 authored report/tier/replenishment | Report input JSON absent; builder/archived structure differ; tier/stock/Meta allocation algorithms incomplete | **LEGACY RESULT NOT TRUSTED** for exact regeneration or operational decision oracle. Preserve context, do not implement these future/deferred algorithms |
| OR19 staged adoption | Nine of22 SKU additions present; 13 absent; all27 top-up keys absent intake | **EXACT MATCH EXPECTED** for artifact overlap sets; no migration of “proposed” as “performed” |
| OR20 replacement/extra episodes | Four observed original/new links; 28 repeated courier references | **EXACT MATCH EXPECTED** for retained evidence links when unambiguous; **EXPLAINED DIFFERENCE EXPECTED** for incompatible OD06 active cardinality; unknown duplicates remain holds |

## Difference adjudication

An EXACT comparison fails on a different member set even if totals agree. Compare sorted scoped identities/locators and field bases; report added/removed/changed/unknown members and monetary reconciliation. A diff is “explained” only with evidence locator, rule/definition difference, affected members, quantified effect and accountable review—not a free-text excuse.

An unknown relationship or missing source gives **comparison blocked/unresolved**, not a fourth success class. Legacy-not-trusted does not exempt OpsHub from golden/domain/source conservation tests. Historical source can still be informative for individual observations even when its ratio is not trustworthy.

No canonical KPI has a scalar error tolerance merely because a workbook used floats. Exact counts/member sets are integer/set equal; monetary comparisons use declared decimal/currency/rounding and identified residual allocation, never an unexplained percentage tolerance.

## Oracle capture and privacy

Future comparisons read approved private frozen copies. Preserve source/ hashes and original formulas; do not run original report skills/scripts, recalculate originals, send customer reports or expose PII in diff output. Public/documentation evidence contains only safe locators, aggregates and synthetic examples. Full contributor identity diff stays in authorized private evidence; scoped digests support sign-off. [15](15-privacy-and-test-data.md).

Current Phase 5 verifies this catalog and the underlying prior evidence; it has not executed an OpsHub-versus-Gentry regression.
