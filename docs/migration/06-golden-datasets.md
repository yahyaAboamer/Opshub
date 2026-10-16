# Versioned golden datasets


## Reviewed logical input supplement and coverage limit

[golden-logical-fixtures.json](../../evidence/migration/golden-logical-fixtures.json) supplies explicit test-policy clock/finality/selection rules, MA/MB colliding business observations, repeated identical line contents with distinct native IDs, eight independently identified contact events, action requirement/result states, prior-period item/shipment members, per-item partial attribution, revised spend portions and temporal boundary cases.

GD01–GD36 remain logical scenarios, not all complete provider-shaped input files. The arithmetic JSON is an **expected-value index**. Before V2 passes, every scenario requires a separately reviewed fixture realization manifest fixing raw synthetic observations/locators/native scope/clocks, ordered stimulus and exact expected bindings/dispositions/holds/generations. No realization may invent missing event/actor/clock evidence or derive expected inputs/results from production normalization code. Prove intentionally wrong identity/parser/clock/quality/member implementations fail.

| ID / additional scenario | Input and expected canonical facts | Expected KPI/safety contribution |
|---|---|---|
| GD37 cross-clock cohorts | TC01–TC06/TC09 shipment/confirmation/pickup/action dates straddle window separately from observation/placement | Exact current/prior member sets in supplement; valid chronology and wrong clock must FAIL |
| GD38 offset/late correction | TC07 repeated offset hour and TC08 late-recorded earlier-effective correction | FOLD01 included/FOLD02 excluded/unoffset held; old/new TS01 numerator changes without rebucketing creation cohort |
| GD39 changing capture | N02 moves page/revises, N03 exact cutoff, N04 late visible, parent line removed | Exact qualified current source set or coverage Held; no missing→deleted assumption |
| GD40 inherited restore | Migration seed holds legacy booking/three-call allowance, then restore before migration with zero new OpsHub markers | Zero new contact/effect starts; seed gap quarantines |
| GD41 repair after effect | False native OA binding, may-executed effect/allowance, repair to OB, replay/restore | Original native execution immutable, both disputed scopes held; no budget/result transfer by assumption |
| GD42 privacy re-import | Completed disposition followed by old snapshot/changed parser/late receipt/old export | No accessible redacted fields resurrected; accounted suppressed units and minimal justified holds |
| GD43 cross-class race | Incumbent cancellation vs OpsHub booking/replacement under differing class flags | Conflicting scopes held or under one coordinator; no overlapping incompatible dispatch |

Baseline source capture may be complete while KR02/KR03 (unmapped S08), KR04 (unknown P07) and contact summary-affected KR05/KR06 remain **provisional**. CF entry states are known and K01 remains complete. Product A/B membership/finality is fully evidenced for its scoped fixture, while unknown C-shipment finality qualifies C. Positive pending alone does not automatically downgrade a metric. Trust state is an asserted output alongside members.
**GD-v2, synthetic specification only; first-draft v1 retained in the Council snapshot.** [golden-contracts.json](../../evidence/migration/golden-contracts.json) is a machine-readable expected-value index; it is not an importer, complete provider payload, application test or production dataset. Future engineering realizes these independently specified logical facts as separately reviewed versioned provider/DB fixtures under Phase 6.

## Envelope and reproducibility

Every dataset fixes dataset ID/version/digest, two synthetic merchants MA/MB, separate account namespaces, symbolic subject→deterministic test UUID mapping, provider/schema version, policy/source-authority/identity/finality/revenue-attribution/allocation versions, interval/timezone/precision, as-of, raw assertion locators, expected accepted facts/holds/dispositions, KPI member sets and exclusions. Symbols below refer only to synthetic identities. Same display aliases/phone sentinel/SKU/order name can be reused in MB with no shared tenant-owned subject.

Baseline window: merchant-local [2026-08-17,2026-08-24), Africa/Cairo; as-of2026-08-24T12:00:00Z. Qualified fixture occurrence dates are18–20 August. Fixture-specific clock choices/finality/revenue eligibility/allocation rules are **TEST-POLICY-v1**, deliberately explicit and not approval of OP07/OP09/OP10 production choices. Date-only/unknown-zone variants never inherit the baseline instant.

## Baseline facts

- **G-CF:** CF01–CF10 entered confirmation once; CF01–CF06 affirmative, CF07/08 pending, CF09 declined, CF10 exhausted/unreached. CF11/12 never entered. All included entry dates evidenced. Result6/10.
- **G-SHIP:** S01/S03/S04 final delivered; S02 final RTO; S05 mapped final-other; S06/S07 pending; S08 unknown. One distinct Order/outbound each; two individually identified delivery attempts under S01. Final denominator S01–S05; no attempt inflation.
- **G-PICK:** customer-handover population P01/P02 collected (paid/unpaid); P03 final cancelled uncollected (paid); P04 final no-show uncollected (unpaid); P05/P06 pending (paid/unpaid); P07 unknown. Final2/4, pending2, unknown1. Separate courier-collection fixture CP01 collected, CP02 paid pending yields1/1 with pending1; never combined with handover population.
- **G-CALL:** C01–C05 attempted; C01–C03 reached. C01 requires action and completes every requirement; C02 awaits approval; C03 has unknown external result; C04 has three actual unsuccessful attempts at18/19/20 Aug09:00+03:00, exhausted with action outstanding; C05 has one unsuccessful attempt and no action requirement. C06 has no attempt and action required. Events counts2/1/1/3/1 =8; reach3/5; action1/5 on C01,C02,C03,C04,C06. Reopening uses same case/objective/budget. C07 is only an imported summary and cannot contribute as an event/case without reviewed mapping.
- **G-PROD shares S01/S02/S03:** S01 Order OA has A1 qty1 net4,000, A2 qty2 net8,000 and B1 qty1 net6,000; S02 Order OB has A1 qty3 net8,000; S03 Order OC has B1 qty2 net3,000. Product A:2 orders,6 units,20,000 net, delivery1/2,RTO1/2; A1:2 orders/4 units/12,000; A2:1 order/2 units/8,000. Product B:2 orders/3 units/9,000,delivery2/2,RTO0/2. Product order/shipment presence overlaps and is not additive.
- **G-MONEY for A:** first A1 line gross8,000−discount2,000−REV01 sales reversal2,000 =4,000; other A lines net8,000 each. Qualified net20,000. Return and refund references to REV01 describe one reversal, deducted once. Fixture revenue method attributes20,000; variant G31 attributes15,000 and leaves5,000 unattributed.
- **G-SPEND:** native SP01 direct A3,000; SP02 generic2,500, approved fixture portion A2,000 plus unallocated500. Source total5,500 = allocated5,000 + unallocated500. A spend5,000 → ROAS4.0. Campaign/account rollups of the same report are alternate views, not additional money. SKU spend attribution absent → SKU ROAS unavailable.

Shipment fixture G-SHIP has five final outbounds. The smaller AC15 product fixture is explicitly the S01–S03 subset, with three merchant shipments, four product presence memberships. It is not silently compared to the five-final merchant baseline.

## Scenario catalog

Each scenario is an isolated baseline variation unless explicitly composed. Its delta applies only to named subjects; all unmentioned baseline member sets remain unchanged.

| ID / scenario | Input and expected canonical facts | Expected KPI contribution |
|---|---|---|
| GD01 successful delivery | S01 final delivered with native binding | Delivery numerator+denominator; Product A/B once each |
| GD02 RTO | S02 qualified final original outbound RTO | RTO numerator+final denominator; no customer-return inference |
| GD03 pending/unknown | S06/S07 pending; S08 unmapped finality | Excluded final denominator; pending2/unknown1 visible |
| GD04 multiple delivery attempts | S01 attempt DA01/DA02 native occurrences | Two attempts, one shipment contributor; count-only variant creates zero events |
| GD05 confirmation states | CF01 affirmative/CF07 pending/CF09 declined with entry | All denominator, only affirmative numerator; CF11 no entry excluded |
| GD06 three contact attempts | C04 three actual calls near0/24/48h | One attempted case; exhausted not reached; required action remains denominator |
| GD07 reached/action required | C02 reached and incomplete action | Reach numerator; no action-completion numerator |
| GD08 exhausted/unresolved | C04 after third failure/reopen | Same case/budget; no automatic resolved/action completion |
| GD09 pickup paid/uncollected | P05 paid pending | Neither final denominator nor collected numerator; pending visible |
| GD10 physical collection | P02 unpaid collected with physical evidence | Collected+final once; payment unaffected |
| GD11 return | Post-receipt Return R01 on OA; item scope unknown | S01 stays delivered; Product A/B order-return association qualified, no every-item quantity or blame |
| GD12 linked replacement | New Order OR with original OA relation and its own S09 pending | Separate Order/own outbound; S01 unchanged; pending+1, no duplicate original shipment |
| GD13 unresolved external action | C03 effect OutcomeUnknown | Action denominator only; hold both connected and manual retry |
| GD14 duplicate webhook | Same authenticated delivery receipt twice | One logical observation/version, no KPI change or effect dispatch |
| GD15 duplicate provider object | Same scoped native Order/Shipment in API/file | Stable canonical IDs, extra evidence lineage only; no KPI change |
| GD16 source conflict | S01 positive delivered versus competing final RTO with unresolved selection | S01 removed from both final numerators/denominator; remaining delivery2/4, RTO1/4, unknown2; Product A1/2 baseline becomes0/1; B2/2 becomes1/1 |
| GD17 manual correction | Admin selects evidenced S08 final-other under test source policy | Append correction/prior assertion; final denominator6, delivery3/6,RTO1/6, unknown0 |
| GD18 multiple variants | A1/A2 on OA plus A1 on OB | Product distinct Orders2, not summed SKU presence3; units6/revenue20,000 |
| GD19 multi-product order | OA contains A+B | S01 once in each product cohort; subset merchant count3, product memberships4 |
| GD20 product spend | SP01+SP02 qualified A portions | A5,000; no copy into A1/A2 |
| GD21 unallocated spend | SP02 remaining500 | Source conserved5,500; A5,000 only; unallocated visible |
| GD22 missing spend | Remove required SP01 source without completeness evidence | A ROAS unavailable; missing does not become zero |
| GD23 ROAS / reversal | G-MONEY+G-SPEND; duplicate return/refund REV01 evidence |20,000/5,000=4.0; no repeated reversal or generic parent |
| GD24 stale source | Fixed known accepted generation, source beyond approved test freshness bound | Facts/rates retained with stale qualification; no automatic failure/zero; action eligibility held as policy requires |
| GD25 zero denominator | Empty eligible population | N/A with empty numerator/denominator, never0/100% |
| GD26 zero spend/zero revenue | Evidenced spend0 → N/A; complete revenue0 and spend5,000 →0 | Missing revenue → unavailable; negative evidenced adjustment labeled |
| GD27 ambiguous identity | MA/MB same aliases; two native variants same SKU; phone shared | No tenant/customer/variant merge; unresolved candidates excluded where required |
| GD28 summary/no event ID | C07 summary3 and two same-text event rows without native IDs | Preserve source observations; no synthetic three events/case budget; exact snapshot replay no-op, cross-snapshot continuity unresolved |
| GD29 historical cardinality | Second outbound native result linked to OA | Retain independently real result/discrepancy; one accepted outbound; no dropped evidence or auto replacement |
| GD30 late spend revision | SP02 revision2 amount2,600; A80%=2,080/unallocated520 under fixture method | Source5,600=5,080+520; new ROAS20,000/5,080=500/127; old generation4.0 retained |
| GD31 partial revenue attribution | Qualified net20,000; approved fixture attributes15,000/unattributed5,000 | ROAS3.0, qualified method named; absent approved eligibility → unavailable |
| GD32 currency/window mismatch | Revenue EGP vs spend USD, or daily source cannot represent requested timezone window | No silent FX/day apportionment; affected ROAS/comparison unavailable |
| GD33 confirmation withdrawal | CF01 affirmative evidence withdrawn, entry retained | Numerator CF02–06=5; denominator10;50%, history preserved |
| GD34 equal percentage/wrong members | Swap confirmed CF06 for CF07 while returning60% | Scalar equal; contributor set differs; regression FAIL |
| GD35 concurrent/reopened contact | Two Operators reserve C04 after reopen/third call | Zero new authorized starts; same canonical case/budget and exhausted state |
| GD36 privacy/restore | Redaction/grant revocation after backup plus missing journal interval | Deny restored access/egress; no KPI export before replay/authority gates; [11](11-recovery-validation.md) |

Coverage includes all required Phase 5 scenarios. Fault/concurrency/provider scenarios use [08](08-provider-contract-validation.md)–[11](11-recovery-validation.md) for barriers and effect-count assertions.

## Version changes and expected outputs

A fixture change produces a new dataset version/digest with rationale, changed source facts, expected members/exclusions and impacted contracts. Do not update expected values merely to make implementation pass. Golden truth comes from approved formulas plus explicit synthetic facts; disputed production policy remains MD decision. Future tests store typed snapshots/sets and pre-rounding decimal arithmetic, current and retained generation lineage. [07](07-kpi-regression-suite.md) defines the assertion format.
