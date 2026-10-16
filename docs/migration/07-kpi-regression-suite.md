# Deterministic KPI and Product/SKU regression suite


## KR18–KR21 — Explicit clocks, prior contributors and quality

KR16 prior contributors now fixed in the logical supplement: PI01/PI02/PI03=4,000 each, PI04=3,000; four units on PO01–PO04; delivered PS01/PS02/PS03, denominator PS01–PS04, prior [10Aug,17Aug), same definition/as-of/currency and no exclusions. Wrong PS99 replacing PS04 must fail despite the same3/4. GD31 attribution is OA-A1 4,000, OA-A2 8,000, OB-A1 3,000 with OB-A1 unattributed5,000; altered per-item assignment with the same15,000 fails. GD30 selects SP01@r1/A3,000 and SP02@r2/A2,080, unallocated520; old r1 portions remain independently reproducible.

**KR18:** TC01 shipment-created current / order-placed prior, TC02 valid order placement before confirmation-entry prior / observed current, TC03 pickup entry current / physical occurrence after interval, TC04 action-required prior / first attempt current; TC09 order placement prior / confirmation entry current. Expected current/prior members are supplied, not inferred from ingestion or placement dates.

**KR19:** TC05 exact exclusive end (21:00Z = next Cairo midnight) excluded; TC06 date-only allowed for the declared calendar cohort but spacing held; TC07 explicit -04/-05 instants differ, unoffset repeated local hour held. Record future timezone database version.

**KR20:** TC08 late correction changes selected numerator in new generation/as-of while old generation retains original contributors. Effective/source/recorded/cohort clocks stay distinct.

**KR21:** complete acquisition + unmapped finality/physical/summary coverage yields provisional known-subset result. Assert identical state/reason/coverage on tile, contributor detail and export. Positively mapped pending is a separate fixture and can leave the known-population metric complete; unknown denominator that cannot be formed yields unavailable. Golden JSON now distinguishes these states instead of labeling every source-complete fixture complete.
Authority: [OD05](../product/00-owner-decisions.md), [K01–K07/P01–P06](../product/06-analytics-and-kpis.md), [architecture analytics](../architecture/09-analytics-architecture.md), AC07/AC15. Golden inputs: [06](06-golden-datasets.md) and [expected values](../../evidence/migration/golden-contracts.json). Production clocks/finality/revenue/attribution remain OP07/OP09/MD06/MD07 until approved.

## Result assertion envelope

Every expected result specifies merchant, definition/version, grain/purpose, cohort/window/timezone, as-of, input/policy/mapping revisions and projection generation; **exact numerator member IDs and amounts**, **exact denominator IDs and amounts**, exclusions/reasons, pending/unknown/undated/unmapped populations, source coverage by source/interval, stale/partial flags, state complete/provisional/unavailable/N/A and exact unrounded value. Ratios round only for display. Contributor detail/export must reference the same generation, not current-state approximations.

Matching percentage with different members is a failed test. Assert set identity/uniqueness before arithmetic; assert amount/basis per member before sum; numerator is a subset of count denominator. Monetary numerator/denominator contributors are independently reconciled, not the same subject set.

## Baseline expected members

| Contract | Numerator | Denominator | Exclusions / exact result |
|---|---|---|---|
| KR01 Confirmation Rate / K01 | CF01,CF02,CF03,CF04,CF05,CF06 | CF01–CF10 | CF11/12 never entered; pending CF07/08, declined CF09, exhausted CF10 remain included;6/10=60% |
| KR02 Delivery Success / K02 | S01,S03,S04 | S01,S02,S03,S04,S05 | Pending S06/S07; unknown S08; reverse legs and prebooking cancellation excluded separately;3/5=60% |
| KR03 RTO / K03 | S02 | **Exactly KR02 denominator** | Same clocks/as-of/unknowns;1/5=20%; S05 final-other explains remaining20% |
| KR04 Pickup Completion / K04 | P01,P02 | P01,P02,P03,P04 | Customer-handover purpose; pending P05/P06 and unknown P07 excluded/visible;2/4=50%. Separate CP01/CP02 courier population1/1, pending1 |
| KR05 Call Reach / K05 | C01,C02,C03 | C01,C02,C03,C04,C05 | C06 no attempt; C07 summary/ambiguous basis excluded. Eight events still five cases;3/5=60% |
| KR06 Call Action Completion / K06 | C01 | C01,C02,C03,C04,C06 | C05 no required action; C02 approval waiting/C03 unknown/C04 exhausted/C06 unattempted all denominator;1/5=20% |
| KR07 ROAS / K07 | A attributed item net: OA-A1=4,000,OA-A2=8,000,OB-A1=8,000 | SP01 A3,000 + SP02-A2,000 | Net20,000/spend5,000=4.0; SP02-unallocated500 visible; generic parent not added; SKU spend absent |

Baseline source capture is complete under TEST-POLICY-v1. Unmapped S08/P07 and unqualified C07 summary history can affect finality/case population, so KR02–KR06 carry a **provisional known-subset interpretation** despite exact counts. CF entries are known and KR01 is complete. Positively mapped pending alone does not mean source or interpretation coverage is partial. Unknown denominator that cannot support a valid subset makes the result unavailable.

## Product/SKU fixtures

| Contract | Expected contributors / values |
|---|---|
| KR08 A sales | Order set OA,OB; item quantities1+2+3=6; net4,000+8,000+8,000=20,000 |
| KR09 A variants | A1 Order set OA,OB/units4/net12,000; A2 OA/units2/net8,000. Product Orders2, not variant Orders sum3 |
| KR10 A delivery/RTO | final set S01,S02; delivered S01=1/2, RTO S02=1/2 |
| KR11 B sales/delivery | Orders OA,OC; units1+2=3; net6,000+3,000=9,000; final S01,S03; delivery2/2,RTO0/2 |
| KR12 overlap | AC15 subset merchant final set S01,S02,S03 count3. Product presence {A:S01,S02;B:S01,S03} count4, overlap S01 explicit |
| KR13 customer returns | R01 post-receipt return associated with OA; S01 still delivered. Order-level product association qualified; no fabricated variant returned quantities/causal reason |
| KR14 spend/revenue conservation | Native spend5,500=product portions5,000+unallocated500; qualified eligible A revenue20,000=attributed20,000+unattributed0. Distinct source grains/reversal identity once |
| KR15 SKU ROAS | A1/A2 sales known; product spend not SKU spend. Ratio unavailable without qualified SKU allocation, never product5,000 copied twice |
| KR16 comparison | Prior A net15,000/units4/delivery3/4; current20,000/units6/delivery1/2. +5,000/+33.333…% sales, +2/+50% units,−25 percentage points delivery, denominator sets explicit |
| KR17 dated context/attention | Current stock/season separately dated; absent historical season stays unknown. Attention reports predicate/sample/approved threshold, no automatic tier/budget/action |

## Required perturbation assertions

- **Empty:** every rate zero denominator → N/A, empty sets and displayed counts; no NaN/Infinity/0%.
- **Money:** spend0 → N/A; missing spend/revenue/attribution/currency/window basis → unavailable; complete revenue0 with positive spend →0; negative legitimate net stays labeled.
- **Conflict/correction:** GD16 changes exact final membership to S02–S05: delivery S03/S04=2/4, RTO S02=1/4; unknown S01/S08. GD17 independently adds S08 final-other:3/6 and1/6. Never compose these deltas implicitly.
- **Confirmation:** GD33 removes CF01 from numerator only,5/10. GD34 wrong member set fails even with60%.
- **Revision:** GD30 selects only SP02 revision2, spend5,080/ROAS500/127 and unallocated520; old generation and old4.0 export remain reproducible.
- **Eligibility:** GD31 A attributed15,000/unattributed5,000 gives3.0, not4.0; no approved eligibility → unavailable despite complete spend mapping.
- **Partial/stale:** a reliable known subset yields provisional with explicit uncovered population; unknown denominator/coverage with no valid subset → unavailable. Stale accepted values remain labeled, not zeroed. Export carries exact source coverage/reasons.
- **Cohorts:** date-only/undated source cannot silently enter instant-based cohort; boundary at exclusive end excluded; merchant/provider timezone mismatch qualified or withheld. Cancellation before shipment not denominator; delivery followed by return still success.
- **Case identity:** reopening/repeated labels/extra contact events cannot multiply C01–C06 case denominators; “attempts exhausted” never completes required action.
- **Purpose:** courier collection/customer handover never mixed by payment status or label; finality mapping revision changes only qualified generation.

## Future execution evidence

For each KR test record input fixture digest, actual ordered contributor export/digest, set diff, expected/actual counts/amounts, exact ratio and display result, exclusions/coverage/versions, retained-generation check and pass/fail. Store private real contributor diffs under [15](15-privacy-and-test-data.md); synthetic fixtures can enter Git/prompts.

Acceptance requires all applicable KR contracts and invariant perturbations pass. No average pass rate or tolerated member mismatch. Phase 5's arithmetic checker checks only these **expected specifications**, not an OpsHub engine.
