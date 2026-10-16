# Adversarial external-action safety validation


## EA23–EA26 — Cross-boundary safety

**EA23:** Gentry/incumbent cancellation races OpsHub booking, or incumbent replacement races OpsHub cancellation on overlapping Order/objective. Enforce [cross-class authority matrix](12-shadow-and-parallel-run.md#cross-class-authority-conflicts). Same-class exclusivity alone fails. If incumbent cannot obey verified shared hold/coordination, keep target conflicting scope disabled.

**EA24:** may-executed booking/contact on falsely matched OA, repair to OB, re-import and restore. Immutable original dispatch scope retained; both affected scopes hold new starts pending native/business reconciliation. No automatic rekey/release/result transfer.

**EA25:** restore before migration with inherited uncertain legacy action/contact allowance but no post-migration OpsHub dispatch marker. Independent migration seed restores holds; missing seed coverage quarantines, zero new starts.

**EA26:** privacy disposition after intake, followed by old snapshot/changed parser/late receipt. No restored accessible customer fields or old-generation download; minimized suppression/effect knowledge retained under approved policy.
Authority: [Phase 4 effect protocol](../architecture/06-external-action-safety.md), [independent recovery journal](../architecture/13-deployment-and-environments.md), OD03/OD06/OD07/OD08. **Future tests only.** Test local serialization and provider behavior separately; local locks do not provide exactly-once effects at an unqualified provider.

## Harness and assertions

Use deterministic barriers at approval/claim/ExecutionStarted commit/journal write/send/provider acceptance/local result commit. Instrument outgoing request count, provider-native effect count/results, local objective/intent/effect/reservation IDs, journal descriptors, durable audit, queue redelivery and current authority. Disable generic HTTP/SDK mutation retries. Preserve mock provider effect store separately from DB restore so forgotten effects are observable.

Expected safety has three parts: no unapproved dispatch, no blind repeat while outcome may exist, and no hidden independently evidenced duplicate result. A transport acknowledgement is not physical fulfillment or all-action completion. Newest intent/worker lease cannot erase an earlier sent request.

## Adversarial matrix

| ID/fault | Setup / stimulus | Expected safe outcome and proof |
|---|---|---|
| EA01 double-click approval | Same client key/exact payload twice; then changed payload same key | Original intent/result returned for exact repeat; changed payload conflict; one approval scope/effect reservation, at most one dispatch |
| EA02 two Admins | Different keys approve same booking/replacement objective concurrently | Stable business-objective lock chooses one current intent/reservation; scoped existing/conflict response; at most one dispatch |
| EA03 duplicate worker delivery | Deliver same effect job twice/race claims | One ExecutionStarted transition; redelivery reads/reconciles existing state, no second provider mutation |
| EA04 crash before request | Crash after ExecutionStarted commit, before journal/send; separately crash before state commit | After commit remains conservative unknown/held, provider requests0; before commit safe unstarted work may resume only after checks. No lease-based inference that a started effect was not sent |
| EA05 crash after send | Provider accepts; worker dies before local result save | One provider effect, local unknown/reservation held; recover positive native identity through qualified read; no connected/manual repeat |
| EA06 timeout unknown | Request may execute, response lost/stale search empty | Unknown + read-only reconciliation/escalation; no provider resend, no no-effect conclusion from absence |
| EA07 known rejection | Exact qualified provider terminal no-effect response | Store reliable negative evidence. Only reviewed retry/reapproval after old execution path terminated/drained and request lifetime settled; no automatic generic retry |
| EA08 success/lost callback | Provider success/result stored or recoverable; callback never arrives | Qualified poll/read reconciles same effect; delayed callback attaches receipt; never rerun create |
| EA09 duplicate result | Same receipt twice; separately two independently real provider result IDs | One receipt/result association for replay; real two effects both retained, invariant breach and Admin/provider investigation; no auto compensation/deletion |
| EA10 manual fallback unknown | Admin attempts handover while original OutcomeUnknown | Denied; integrated and human repeat remain blocked; show exact held objective/native scope |
| EA11 restore forgets effect | DB restored before effect/Order/connection existed; provider and journal survive | Rebuild hold from native/business scope; rediscovery cannot mint executable new objective; missing binding/coverage quarantines affected merchant/connection |
| EA12 stale worker resumes | Old paused sender resumes after timeout/new worker or handover | No reservation release/handover while old path may still send; terminate/drain old path and settle request lifetime before no-effect retry. Local write fencing blocks stale persistence, cannot retract sent request |
| EA13 authority revoked | Admin suspended after approval, before each unstarted effect | Zero new dispatch; reapproval by current authorized Admin required. Already-transmitted effect remains under read-only reconciliation, not retroactively undone |
| EA14 intent edit | Recipient/items/COD/side-effect/dependency version changes after approval | Prior unstarted approval invalid; exact changed intent requires review; no quiet execution of stale intent |
| EA15 replacement partial | New Shopify Order succeeds; booking fails/unknown; annotation incomplete | Retain one new linked Order. Retry only qualified no-effect booking/annotation under same scope; unknown blocked; no recreate/no premature case closure |
| EA16 handover race | Known unstarted/no-effect state; queue worker races Admin handover | One exclusive reservation/path; independently durable handover before release to human; old connected path nonactionable. Issuance/journal uncertainty holds both |
| EA17 native auto-booking | Shopify replacement triggers independent Bosta connector | Capability fails until one booking authority configured/verified; detect existing consignment and reconcile, do not book again |
| EA18 journal unavailable | Pre-dispatch conditional marker write fails or is uncertain | Zero provider send; reservation held; no “best effort” marker skip |
| EA19 service/account changes | Merchant suspended, account rebound, capability disabled, credential rotated after approval | Current dependency/ownership/service check before each effect; deny stale dispatch, preserve approval and evidence |
| EA20 false completion | Approval/call/source Resolved label present but required effect unknown | Case remains action-required/incomplete; contributes to K06 denominator only |
| EA21 cross-merchant result | Callback/native result from MB attached to MA effect | Reject/hold binding without disclosing MB data; no effect success/relationship contamination |
| EA22 recovery redrive | Restore started queue job, manually redrive dead letter, or clear unknown by timer | Only safe reconciliation scheduled; queue state never releases business reservation or resets held contact/action scope |

## Recovery evidence and release

Reliable no-effect requires an exact qualified terminal negative contract plus old execution-path containment. Provider search incompleteness, 5xx, connection timeout, lease expiry and silence cannot establish it. A provider-supported idempotent operation must be tested for exact operation/key/payload/account/lifetime semantics; MVP default holds unknown until resolved, even if another operation documents idempotency.

One provider attempt may itself reveal duplicate effects; retain all independently evidenced identities and flag qualification failure. The zero-tolerance gate applies to OpsHub blind duplicates/unauthorized requests and to activating a capability without demonstrated provider-safe behavior. Do not promise control over independent external actors.

Every test records attempted and actual requests/effects, unknown/positive/negative evidence, all reservations, final case state and audit. Run races with barriers, not just sleeps; repeat alternate ordering and DB rollback boundaries. All applicable EA cases must pass for an enabled action class. A successful happy path cannot waive EA05/EA06/EA11/EA12/EA16. No test here has been executed against an application/provider.
