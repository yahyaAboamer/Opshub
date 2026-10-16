# OpsHub — MVP acceptance and release criteria

**Proposed product acceptance gates for human review.** They do not assert a product exists or authorize architecture, implementation, migration or live consequential experiments. Requirement references: MRxx [scope](03-mvp-feature-prioritization.md), WFxx [merchant work](04-merchant-workflows.md), PFxx [platform work](05-platform-admin-workflows.md), Kxx [metrics](06-analytics-and-kpis.md), ING/EXP [ingestion/export](08-data-ingestion-and-integrations-requirements.md), AUD/TR [trust](10-audit-data-quality-and-trust.md).

All applicable MUST gates must pass in a controlled environment before MVP release. AC12 requires comparison readiness for every release; executing a historical Gentry baseline comparison applies to a pilot ingesting Gentry history or replacing Gentry, not an unrelated fresh-input merchant. Tests use synthetic/redacted records, at least **two separate merchant workspaces**, Admin/Operator/platform identities, reused human-readable identifiers across merchants and both complete/incomplete inputs. Product behavior is measured from results/history/export, not only from visible labels or disabled buttons.

## AC01 — Merchant can be onboarded

**MR01/MR02/MR12/MR13/F19/F20/F24; WF01/WF10/PF01.** A verified initial Admin establishes membership, invites Operator, confirms merchant/source settings and connects qualified Shopify/Bosta plus applicable Meta input. First orders/shipments and product/spend observations produce usable queues and analytics. Missing connection/data/mapping has a checklist/limited state, not false zero or false integrated readiness; onboarding fallback is explicit. Service/commercial state remains separate.

**Pass:** both pilot workspaces complete the agreed assisted path with no undisclosed technical/manual prerequisites; all required checklist items have a result or explicit not-applicable reason. Time-to-first-use is recorded against the owner-approved OP13 target.

## AC02 — Merchant isolation and membership work

**MR02/MR03/MR11/MR12/MR14/MR15; PER01–PER05/TR05.** Reuse order numbers, tracking, phones and SKU labels in both merchants; verify view/search, direct-record access, queues, links, imports, exports, KPI contributors and history remain scoped. A User with membership in both deliberately changes context; one membership supplies no authority in the other. Expired/revoked/wrong-recipient invites and suspended memberships are denied; removing last Admin is blocked or follows approved verified recovery.

**Pass:** zero cross-merchant operational disclosures/associations and zero unauthorized effects in the agreed scenarios. Existing authorship survives suspension; no platform self-grant of merchant Admin.

## AC03 — Consequential authority is effective

**MR07/MR10/MR13/MR15/F24; OD07/OD08/PER02/PER06.** Operator prepares but cannot invoke supported connected cancellation/booking/replacement or approve fallback execution. Platform cannot invoke merchant actions. Admin reviews/initiates exact intent in OpsHub; source-returned identifiers/status reconcile to it. Changed scope requires reapproval. Test every supported action path, including unavailable/fallback handover, not only control visibility.

**Pass:** zero unauthorized connected effects, approvals or result acceptance through OpsHub; each supported action identifies Admin initiation, exact approved intent, OpsHub execution origin and provider result. Safe manual exceptions identify Admin executor/reason/handover. OpsHub does not control independent provider-account activity; unverifiable/unauthorized reported results remain reviewed discrepancies. Refunded contact labels never execute refunds.

## AC04 — Merchant data enters safely and repeatably

**MR03/MR12/F18/F24; ING01–ING06/WF02.** Accept qualified connected updates and preview fallback files; reconcile every observation/input disposition. Repeated source observation/file yields no extra objects/contacts/effects. Correction preserves prior assertion. Distinct evidenced contacts remain distinct; uncertain event identity is held. Unmatched provider/variant/order references and conflicting times stay reviewable; long/multiple items/quantities are not silently truncated.

**Pass:** 100% of input rows accounted for with safe locator/disposition; accepted objects/counts reconcile; no lost prior accepted data or unintended external actions. Pilot mapping/dedup contract OP13 is approved and verified.

## AC05 — Due contact work follows OD04

**MR05/MR06/MR17; WF03/WF05/WF06.** Cases due now appear independently of dashboard period. All ordinary contacts, successful or failed, count toward the three-attempt total. When another contact is needed and budget remains, next eligibility uses approximately 24 hours spacing. Three attempts without reach leave the active call queue as unreached/exhausted; a reached case at the limit retains unfinished action without another ordinary call. Test failed→successful→failed and reached→failed→failed: both use three attempts, retain successful reach and block a fourth, including an Admin trying to reset through reopening. Use delayed attempts to verify no clustered catch-up. Also test missing contacts, no action required and refusal.

**Pass:** all eligible due cases are reachable; maximum three total ordinary contact attempts per objective; next-due behavior matches approved OP04 tolerance; zero exhaustion automatically marked Resolved/cancelled. Reopening does not reset the ceiling; any future higher limit needs owner-approved policy change. Imported cumulative counters do not create fabricated attempts.

## AC06 — Truth and action completion are separate

**MR03/MR04/MR07–MR10/MR14/MR17; OD01–OD03.** Test paid/waiting pickup; collected/unpaid pickup; payment recorded with no physical courier collection; courier collection with separate customer handover still unknown; customer handover that cannot prove courier collection; Delivered reverse leg with RTO/customer-return order disposition; cancelled business order with delivered outbound evidence; approval with incomplete external effects; tag-only handoff without matched consignment; and a contact-only resolved case beside unresolved action work.

**Pass:** all source dimensions remain explainable and independent. Only a specific completed case is Resolved; payment/courier label/call/approval/queue disappearance cannot falsely close another case. Physically collected requires accepted evidence; unknown external effect stays visible until reconciled.

## AC07 — Canonical KPI arithmetic is reproducible

**MR11/F19/F20; K01–K07/KPI01–KPI05/OD05/OD09.** Use the following complete synthetic cohort, with date/source mapping explicit:

| Metric fixture | Expected result |
|---|---|
| 10 confirmation participants, 6 confirmed; another 2 orders never entered | Confirmation Rate 6/10 = 60%; 2 nonparticipants outside denominator |
| 5 final outbound: 3 delivered, 1 RTO, 1 mapped final other; 2 pending and 1 unknown | Delivery Success Rate 3/5 = 60%; RTO Rate 1/5 = 20%; pending 2 / unknown 1 separately shown |
| 4 final pickups: 2 evidenced collected, 1 final uncollected cancellation, 1 evidenced final no-show; 2 pending, 1 unknown | Pickup Completion Rate 2/4 = 50%; pending 2 / unknown 1 excluded and visible |
| 5 contact cases attempted, 3 reached, with repeated attempts on the same cases | Call Reach Rate 3/5 = 60%; repeats do not inflate case counts |
| 5 contact cases require action, 1 completed; others approval-waiting/unknown/exhausted/unattempted with action outstanding | Call Action Completion Rate 1/5 = 20%; unattempted required-action case enters completion denominator but not Call Reach Rate |
| Qualified product net attributed sales 20,000; direct spend 3,000 + allocated generic 2,000; same period/currency and complete inputs | ROAS 20,000 / 5,000 = 4.0; source generic total is not added again |

Test zero denominator/spend, missing revenue/spend, partial interval, unknown mapping, late revision and contradictory outcomes now for MVP, including K07. Missing required spend is unavailable, not zero; a calculable partial population is visibly provisional with limitation. Pickup fixtures separate customer handover/courier collection/payment. Withdrawals/corrections retain history; later return preserves outbound delivery. Discounts/return-refund adjustments and generic spend are counted once.

**Pass:** every MVP KPI count/value can be exactly reproduced from its exported contributors before display rounding; 100% carry definition, population, exclusions, window and as-of. Zero-denominator is N/A; unreliably formed population is unavailable; partial known population is clearly provisional. No pending pickup is classified as failure.

## AC08 — Data-quality and freshness gaps are visible

**MR04/MR11–MR15; ING07–ING10/TR01–TR02/PF03.** Simulate absent/stale courier file, incomplete source period, unknown status, competing assertions, import failure and manual override. Show source coverage/as-of, affected capability/KPI, responsible review and recovery route. Last accepted data remains labeled; missing source does not imply pickup/zero fees/complete history.

**Pass:** 100% of the agreed gap cases produce an understandable trust state and impact; dashboard/export/platform aggregate agree on that state. Source receipt success cannot mask incomplete coverage. Thresholds/time basis match OP08.

## AC09 — Important history is attributable and preserved

**MR10/MR13–MR17/F24; AUD01–AUD05.** Review connected initiation/result, failed/unknown effects, fallback handover, request edits, attribution/input correction, export, closure and reopen. Verify Admin authority versus OpsHub/provider/source/recording actor, times/merchant/prior-new/result and unknowns. Creation-success/booking-failed retains known new order; ordinary edits cannot erase history.

Also test two Admins preparing/approving booking for the same order before any result is recorded. Only one intent may be actionable; safe reassignment/supersession makes the earlier one nonactionable. Delayed or unknown first result blocks new execution until reconciliation. Test the same recovery objective with competing replacement requests. If a provider duplicate is discovered despite external controls, both observed results remain visible as a violation; rejecting the second association cannot erase it.

**Pass:** 100% of specified important actions have the required fields or explicitly justified historical unknowns; zero competing OpsHub-authorized execution for the same intent; no approved request masquerades as completed multi-effect work; no invented historical actor/event/revision.

## AC10 — Exports and privacy match the product scope

**MR11/MR14/MR15; EXP01–EXP03/PER04/AUD06.** Select filters, period and as-of; compare dashboard/drill-down/export counts and nulls. Operator operational export excludes direct contacts/free narratives. Admin explicitly selects contact-bearing export, with scope preview and audit. Platform report contains only allowed administration/aggregate diagnostics. Report revision/as-of caveats survive sharing.

**Pass:** exact scope/population agreement; zero unauthorized contact/cross-merchant disclosure; no hidden export-all-calls behavior. Privacy/retention policy OP12 approved.

## AC11 — Platform and commercial continuity

**MR15/MR16; PF01–PF05/COM01–COM11.** Platform provisions and monitors both merchants, handles verified membership recovery, records manual plan/status and service changes, suspends/reactivates under approved policy. Retain all original merchant record relationships, evidence, cases and audit; commercial state changes cause no bookings/refunds/cancellation/case resolution. Read/export behavior and notices match OP11. Reactivation shows fresh/stale inputs and safe current contact eligibility.

**Pass:** 100% tested accounts observable within assigned platform scope; zero automatic merchant business authority; suspension causes zero operational-data destruction and reactivation preserves continuity. Trial/prices/limits are explicit approved values or visibly TBD where not launch-dependent.

## AC12 — Legacy comparison readiness

**MR11/MR12/MR14; EXP03 and closed Phases 1/2 mapping.** A later authorized migration review can choose a bounded Gentry baseline and identify each source observation/reference, original definition/window/as-of, OpsHub mapping, unsupported episodes/exclusions and expected normalized differences. Cover paid-inferred pickup, outbound/reverse Delivered, two-versus-three call policy, confirmation numerator, blank outcomes and missing-to-zero costs. Do not require numerical equality for deliberately different definitions.

**Pass:** product supports the named comparison metadata and sample distinctions, with no silent dropped leg or invented event. For a Gentry-ingesting/replacement pilot, every sampled baseline difference is reproducible or explicitly unresolved with source locator/reason. A fresh-input merchant need not run a historical Gentry migration to pass release; AC04/AC07 remain mandatory. This is a product acceptance condition, not a migration implementation deliverable in Phase 3.

## AC13 — Operational usability and bounded scope

**All MUST modules; primary journey in04/WF11.** Operator works connected orders/shipments → contact/action request → Admin initiates supported connected effect → reconciled result → justified case closure → operational/Product-SKU/ROAS review. Platform uses redacted readiness diagnostics. Include return, pickup, failed/unknown effect and source exception; integrated normal jobs require no routine copy/paste. Native refunds, replenishment and advanced BI remain unnecessary.

**Pass:** agreed connected daily/product jobs finish without routine provider-screen copying or undocumented workaround; freshness/action-reconciliation/analytics/export durations and volume meet OP08/OP13 targets. Labeled unsupported/unavailable exceptions pass fallback safely. Measure usability against owner targets, not invented production benchmarks.

## AC14 — Integrated pilot round trip and fallback

**OD08; IG01–IG08/CON01–CON03/ACT01–ACT03/FB01–FB03.** In controlled qualified pilot provider contexts, connect the supported Shopify store/Bosta account and applicable Meta input with explicit merchant ownership. Receive new/changed commerce/payment/item/product/tag evidence and shipment tracking/purpose/attempt-count/final-outcome evidence into OpsHub. Demonstrate one qualified Admin-supported Bosta booking and Shopify replacement-order result with linked tracking/status returned; also test cancellation/required annotation where the capability contract supports them. Record any genuinely unsupported action as an exact unavailable capability and test its approved fallback.

Test temporary unavailable input/execution, incomplete onboarding, unsupported action, repeated submission, uncertain result and creation-success/booking-failed. Contrast known not-started/reliably evidenced no-effect (fallback permitted after handover) with timeout/failed refresh/no visible result/late result (unknown; connected/manual repeat blocked). Missing provider absence-lookup capability is not negative evidence. Handover records earlier nonactionable path/Admin/reason/evidence; recovery reconciles identifiers without duplicates/false health. Do not assume unqualified event/fee/collection response fields.

**Pass:** core supported daily loop completes through OpsHub without routine manual copy/paste; updates/results arrive within qualified targets with attributable source/coverage/as-of. Unauthorized Operator/platform invocation causes zero connected effects. Safe fallback succeeds under its declared condition and rejoins connected truth without duplicate order/shipment/action. Entirely manual core cannot certify integrated readiness. Provider contract/required action support is qualified before release; this document performs no real bookings or connections.

## AC15 — Product/SKU performance and trustworthy ROAS

**OD09; F19/F20/F21; WF11; K07/P01–P06.** Inspect product/SKU orders/units/qualified revenue, outbound delivery/RTO and separately associated customer returns for selected/comparable periods. Synthetic finals: S1 contains A+B and is delivered; S2 contains A and is RTO; S3 contains B and is delivered. A has delivery1/2=50%, RTO1/2=50%; B delivery2/2=100%, RTO0/2. Merchant has3 shipments, not4 summed product associations. Pending/unknown/unmapped shipments remain separately visible. A post-receipt return on S1 does not erase its courier success or prove every SKU was returned.

Trace item revenue/adjustments and Meta direct/generic spend to contributors; qualified A revenue20,000/spend5,000 gives4.0. Verify complete zero-spend=N/A, missing required input=unavailable, meaningful partial input=visible provisional limitation, incompatible currency/unresolved attribution=no unqualified ratio, and no double-count of return/refund or generic total plus allocations. Source revision changes as-of/caveats, not historical evidence.

For aggregation, S1 contains A's SKUs A1(quantity1) and A2(quantity2); S2 contains A1(quantity3). Product A has2 distinct orders/shipments, not3 summed SKU-presence counts; units4+2=6 and net item revenue12,000+8,000=20,000 add correctly. Unmapped items remain a separate balance. Product ad spend5,000 is not copied into each SKU; SKU ROAS is unavailable without qualified SKU spend attribution.

For a compatible complete comparison interval, prior A revenue15,000/units4 versus current20,000/units6 gives +5,000 revenue (+33.3% rounded) and +2 units (+50%). Prior delivered3/4=75% versus current1/2=50% gives -25 percentage points, with both denominators visible; no causal claim. Repeat with incomplete prior coverage/changed method: visible qualification or withheld incomparable difference, not an unqualified improvement/deterioration. Current stock/season never fills missing historical context.

**Pass:** both merchant roles inspect own product analytics with practical drill-down and consistent exports; product/SKU/outcome populations and all numerator/denominator/period/quality details are reproducible. Attention has justified predicate/sample. Analytics works with absent season context as explicit unknown and with available dated season context; it does not need rich season management, replenishment or production automation. Same trust/isolation principles apply to every operational and product view.

## Human review and launch gates

Owner review of this bounded correction is required before Phase 3 approval/any Phase 4 work. OD08/OD09 settle integrated core and Product/SKU/ROAS MVP inclusion. OP01/OP09 now qualify narrower provider/analytics contracts, alongside unchanged unrelated launch choices. Supported normal round trips and product analytics must pass; exact unsupported/unavailable operations may use a bounded fallback, not a primarily manual core. OP14 retains only future scope. Evidence gaps are not resolved by owner preference.

Functional targets here are deliberately deterministic: no unauthorized effects/leaks/data destruction; full accounting for accepted inputs and important audit; exact metric contributor reconciliation. Merchant business improvements (higher delivery/reach or lower RTO) need a measured comparable baseline; no fabricated uplift target is claimed.
