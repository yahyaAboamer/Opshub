# OpsHub — merchant workflows

**Accepted baseline with bounded correction**, governed by [OD01–OD09](00-owner-decisions.md). [Gentry workflow evidence](../reconstruction/04-workflows-and-state-machines.md) and [domain states](../domain/04-state-machines.md) inform the jobs; proposed transitions describe OpsHub, not verified Gentry enforcement. The normal supported-source path is integrated; manual handling is a labeled fallback. Acceptance IDs resolve to [11](11-mvp-acceptance-criteria.md).

## Shared daily experience and case rules

A merchant user enters their own workspace and sees due contact, pending approval, action waiting, failed/unknown external result and data-quality attention. Each entry explains **why it is here**, subject/source, responsible user, relevant clock, next permitted step and completion evidence. Dashboard date filters cannot silently hide the operational backlog. Explicit queue filters show excluded/backlog counts.

Cases/tasks track specific work, not a global order lifecycle. MVP work is embedded in confirmation, return/pickup follow-up, cleanup and action requests; there is no general-purpose task builder.

| Work state | Meaning / permitted exit |
|---|---|
| Ready / due | Eligible work with a clear next action and responsible merchant team |
| Waiting for next contact | Unsuccessful attempt recorded; next eligible attempt displayed |
| Waiting for approval | Prepared consequential intent awaits Merchant Admin decision |
| Action required / waiting for external result | Customer reached or issue identified; action still outstanding; approval alone cannot close it |
| Result failed / unknown | A required effect failed or lacks evidence; visible reconciliation work; no blind retry |
| Resolved | Required work completed with evidence and no further action currently required, per OD03 |
| Unreached / attempts exhausted | Three ordinary contact attempts used without successful reach; leaves ordinary active call queue, remains visible in exceptions/history; not Resolved |
| Contact limit reached / action required | Customer was reached but all three ordinary attempts are used; no further ordinary call is due, while unfinished action remains open |
| Reopened | New evidence or failed completion invalidates closure; reason and next responsibility retained |

Work state is independent of order, courier, payment and physical collection. Every actual ordinary contact attempt, successful or unsuccessful, counts toward the same case objective's three-attempt ceiling. Reach never resets that count. Later NoAnswer does not erase a previous successful reach; it can create new attention without claiming the customer was never reached. An unsuccessful attempt is distinct from a refused business request. A resolved contact-only case can coexist with an open return or failed booking case. Do not multiply contact cases merely to reset the ceiling.

Proposed queue order: due/overdue first, then earliest due time and stable identity. First attempt at case entry, second near +24 hours and third near +48 hours; actual attempt times drive the next due time. A delay never triggers catch-up calls close together. Timing tolerance and urgent attention are OP04; no automatic cancellation at exhaustion. Reopening retains history and does not reset used attempts for the same objective. A fourth contact for that objective is blocked in MVP, including for Admin. Any future increased limit requires an explicit owner-approved change to OD04, with retained reach/exhaustion history.

In-app attention is MUST. Automatic customer messaging, email alerts and embedded dialing are deferred. Calls may be performed externally and recorded by the responsible merchant user.

## WF01 — Onboard and reach first useful work

- **Goal / entry:** a legitimate merchant representative wants a usable workspace; platform provisioning and initial Admin verification are available.
- **Primary flow:** create merchant/workspace → verify initial Admin → confirm source ownership, timezone/currency/defaults → invite Operators → connect pilot Shopify/Bosta and applicable Meta inputs → review capabilities/mappings/coverage and first received data → inspect source freshness/quality → reach first usable queue and product/operational dashboards.
- **Alternate paths:** incomplete/unavailable connection allows labeled onboarding import fallback but does not establish integrated readiness. Missing courier coverage remains unknown; a genuinely pickup-only merchant may declare that source not applicable without waiving the Shopify/Bosta operational pilot gate. Missing Meta/spend gives an explained unavailable/provisional ROAS state. Existing identifiers/mappings cannot be guessed. Mapping conflict or no Admin blocks affected readiness; commercial state stays explicit.
- **Result / permissions:** Admin confirms readiness; platform provisions/activates the account but does not choose merchant operational rules. Members have only their offered merchant role.
- **Attention:** checklist distinguishes account created, data configured, first data received, quality incomplete and ready. No empty dashboard implies zero activity when inputs are missing.
- **Success / acceptance:** Admin connects qualified pilot sources and reaches usable work/analytics; connection failures have recoverable fallback and do not lose accepted data. AC01/AC02/AC08/AC11/AC14/AC15.

## WF02 — Ingest or refresh operational data

- **Goal / entry:** Admin-approved source ownership/mapping exists and supported connections provide new/changed evidence; an authorized user can inspect permitted refresh/results.
- **Primary flow:** connected source supplies scoped observations → apply reviewed mapping/validation → account for accepted/repeated/rejected/unmatched updates → retain changed-source revisions → route conflicts/unknown links to attention → update queues and operational/Product-SKU/ROAS views with explicit coverage/as-of. Routine manual copy/paste is unnecessary.
- **Alternate paths:** exact repeat is a reported no-op; a revised source snapshot is a reviewed correction, not an extra event. Ambiguous phone/SKU/order matching stays unresolved. Missing courier history is not evidence of pickup. Unsafe or incompatible rows are held with a reason; no silent second outbound/return/pickup creation.
- **Result / permissions:** Operator investigates permitted read updates or uses an approved fallback mapping; Admin approves connection ownership, changed mappings and authoritative overrides. Ingestion never executes a consequential action as a side effect.
- **Attention:** connection/capability state, coverage/as-of, failed/stale/partial updates, conflicts and recovery guidance. For fallback files, preview and account for rows using08's ING rules; keep exception reason visible. Old valid evidence remains distinct from failed refresh.
- **Success / acceptance:** connected and fallback updates reconcile without duplicates/lost revisions; routine daily ingestion needs no copy/paste. AC04/AC08/AC09/AC14/AC15.

## WF03 — Confirm an order and contact the customer

- **Goal / entry:** a valid order explicitly enters the confirmation process, creating one confirmation work objective with entry time/basis. Imported uncertain history is not assigned a fabricated entry time.
- **Primary flow:** open due case → inspect connected order/items/contact/source → contact externally → record timestamp/actor/reach/customer decision in OpsHub → record affirmative consent evidence → where qualified and required, apply the merchant's mapped confirmation/attempt annotation through the commerce connection and reconcile its result → complete contact-only work or retain remaining action until finished. Calling remains external; connected source annotation is not embedded telephony.
- **Alternate paths:** failed reach schedules the next eligible attempt within the total OD04 budget; three attempts with no reach go to unreached. A reached case at its three-attempt limit retains action work without another ordinary call. Customer declines or asks to change/cancel → prepare Admin request. Confirmed source tag with unknown actor/time remains imported confirmation evidence; it does not become a retrospective call. Contradictory or withdrawn confirmation requires review and retained earlier assertion.
- **Result / permissions:** Operator records reach/consent/notes; Admin handles consequential change. Reached is not automatically confirmed. Exhaustion is not cancellation. A contact-only confirmation case closes only when the stated objective is complete and no follow-up remains.
- **Attention:** next contact due, unusable contact, ambiguous consent, required source-annotation failure/unknown result, approval waiting and confirmed-but-unbooked work. OP03 qualifies tag/dispatch policy; no consequential action is authorized merely by ingested confirmation.
- **Success / acceptance:** three attempts near the approved intervals; consent evidence and process-entry population support Confirmation Rate; reached-but-unfinished work remains visible. AC05/AC06/AC07.

## WF04 — Book and monitor an outbound shipment

- **Goal / entry:** a Delivery order has a prepared dispatch request, valid recipient/items and no already-associated outbound shipment. Booking eligibility and any confirmation exception need Admin review.
- **Primary flow:** Operator prepares request from connected order evidence → Admin reviews/initiates supported booking in OpsHub → OpsHub executes qualified Bosta booking → receive/reconcile returned tracking/result → reconcile subsequent courier status with that order → monitor physical outcome, exceptions and freshness. Booking success is separate from shipment delivery.
- **Alternate paths:** existing booking or another actionable pending/approved booking intent blocks competing execution. One responsible Admin holds the current executable intent; transfer/supersession makes the earlier intent nonactionable and is recorded. Supersession is unavailable while earlier execution/result is unknown; reconcile first. Failed/unknown result creates visible reconciliation work. A provider reply with only a count does not manufacture attempt history. Tag-only handoff and no matching consignment display disagreement. A second outbound proposal is rejected under OD06; replacement uses WF08. Reverse legs retain purpose. If an external duplicate nevertheless occurs, retain both observations as a violation/reconciliation exception, not a silently dropped second consignment.
- **Result / permissions:** Admin authorizes connected execution; Operator prepares/investigates. If booking capability is unavailable/unsupported, show reason and use08's safe Admin fallback only after the connected result is known not to have occurred; unknown effect blocks both paths. Booking is not handoff/delivery. Order cancellation/customer return can coexist with courier Delivered, per OD01.
- **Attention:** confirmed/unbooked, expected update missing, courier exception, disputed mapping and failed/unknown effect. Age is labeled by its actual origin; stale courier data cannot be called a verified delay.
- **Success / acceptance:** one outbound at most, separate order/courier truth, no duplicate booking during recovery, and final-outcome KPI drill-down. AC03/AC06/AC07/AC08.

## WF05 — Follow up a return

- **Goal / entry:** explicitly evidenced RTO, post-receipt return or exchange-related disposition links to the order's single return case; uncertain classification becomes review work.
- **Primary flow:** reconcile connected courier/order disposition separately from reverse-logistics state → investigate reason/exception → contact under unchanged retry rules → record explanation/cause/recovery intent → prepare supported connected cancellation/replacement or separately evidenced financial follow-up → obtain Admin decision and reconcile each required result before closure. Unqualified reverse booking/reschedule/refund uses explicit fallback, not assumed automation.
- **Alternate paths:** customer unreachable becomes attempts-exhausted; unknown cause stays unknown. Courier-reported cause is not a customer's explanation. “Refunded” or “Re-shipped” from an old contact field stays a reported claim until an external result is evidenced. Repeated/partial episodes cannot create a second return case or silently overwrite the first; hold exceptional source observations for review. Stock restoration is outside MVP.
- **Result / permissions:** Operator can investigate/contact/request; Admin accepts consequential result and closes consequential action work. Physical return receipt, customer contact, service action and financial assertion remain separate.
- **Attention:** uncalled, retry due, reached/action incomplete, disputed classification, reverse transport unknown and external result waiting.
- **Success / acceptance:** a completed reverse consignment never proves original delivery kept/refund done; failed reach never closes required service action. AC05/AC06/AC07/AC08.

## WF06 — Manage a pickup

- **Goal / entry:** an explicitly identified pickup/collection purpose has zero or one pickup case per order under OD06. Preserve Gentry merchant/customer Pickup-channel work. Also preserve OD02's separate payment versus physical courier collection truth wherever courier collection is present, including return follow-up. Customer handover and courier collection are different events; purpose is mandatory and their populations cannot be silently mixed. OP05 approves pilot purpose/evidence/finality mapping, not whether payment may stand for physical collection.
- **Primary flow:** reconcile available connected pickup/reverse evidence with explicit purpose and separate payment → record source-evidenced courier collection or witnessed customer handover with event kind/actor/time/basis → contact about overdue waiting → prepare supported Admin cancellation in OpsHub where needed → classify final outcome within approved purpose mapping. Missing provider physical evidence requires attestation/review; payment still cannot substitute.
- **Alternate paths:** paid remains waiting without physical evidence; missing courier does not create collection. Collected then refused/returned retains physical collection plus later disposition; it is not relabeled as never collected. Pending remains outside final denominator. No-show needs explicit evidence/mapping, not payment void/refund inference. Partial collection/repeated pickup episode becomes review exception.
- **Result / permissions:** Operator can attest physical collection under the approved evidence policy; Admin decides cancellation/payment corrections. Collection does not automatically change payment. Payment does not automatically close pickup work.
- **Attention:** aged waiting, missing evidence, payment/collection disagreement and requested cancellation. Thresholds are proposals in [07](07-configuration-and-policy.md), never an automatic cancellation rule.
- **Success / acceptance:** physical evidence controls collection; final outcomes and excluded pending/unknown records are visible. AC06/AC07/AC08.

## WF07 — Work cleanup and correct data

- **Goal / entry:** a named quality/operational predicate flags missing booking, returned-still-sale disagreement, stale courier state, old waiting pickup or inconsistent financial/business assertions.
- **Primary flow:** inspect predicate/clocks/connected assertions → distinguish missing/stale input from real work → refresh/investigate or prepare specific action → Admin authorizes supported cancellation/other qualified action in OpsHub → reconcile external result → recompute issue membership with history. Unsupported archive/payment/refund operation uses explicit fallback; a cleanup label is not evidence of provider support.
- **Alternate paths:** missing source blocks confident classification; no financial action is inferred from a cleanup label. A view is tidy/archive-only rather than an operational failure when appropriate. Hiding/archive acknowledgement cannot make unknown input complete or suppress KPI exclusions.
- **Result / permissions:** Operators investigate; authoritative corrections and consequential cancellation remain Admin-reviewed. Archive/acknowledge is a display/history action, not financial resolution or deletion.
- **Attention:** separate data-quality review, action waiting and optional tidy work. Each age says placement, booking, contact or input-watermark basis.
- **Success / acceptance:** issue clearance reflects its predicate/evidenced action, not a generic Resolved order checkbox; corrections retain before/after/source/reason. AC06/AC08/AC09.

## WF08 — Approve and complete a replacement/reship

- **Goal / entry:** customer-service recovery needs a new order linked to the original; Operator prepares recipient/items, reason, proposed commercial amount/payment basis and any return dependency.
- **Primary flow:** Admin reviews exact intent/eligibility in OpsHub → approves/initiates qualified Shopify new replacement order → OpsHub obtains/reconciles its identity and original link → Admin-authorized qualified Bosta booking creates its sole outbound → reconcile tracking/status and any required original annotation independently → close required work only after completed effects/no remaining action. Normal supported operation requires no copying between provider screens.
- **Alternate paths:** changed recipient/items/value invalidates approval. Competing requests for the same recovery objective cannot both remain independently executable; retain the reviewed current intent and reconcile any earlier unknown result first. New order exists but booking failed/unknown → keep that order and reconciliation work; do not create another replacement on blind retry. Gentry same-original-COD wording is preserved as legacy evidence, not the OpsHub universal pricing rule. Exchange can link original → return where applicable → replacement. Rejected intent remains decision history; it does not silently claim another pending action complete.
- **Result / permissions:** Admin approves and executes; Operators prepare/submit evidence. Approval, creation, booking and any required original-order annotation each have independent outcomes. No second outbound is attached to the original.
- **Attention:** pending decision, unavailable capability, failed/unknown effect, possible duplicate and created order waiting booking. Provider-unsupported/unavailable effects have safe Admin fallback with explicit handover; never fallback-execute an unknown effect. Native refunds and automatic rollback remain deferred.
- **Success / acceptance:** linked new order with at most one outbound; no false all-effects success; no operator/platform execution; approved commercial treatment OP06. AC03/AC06/AC07/AC09.

## WF09 — Review outcomes and export a scoped summary

- **Goal / entry:** user needs current attention and period performance from accepted merchant inputs.
- **Primary flow:** choose named period/cohort → read canonical operational KPIs with counts, exclusions and data watermark → drill into contributing records and unknown/pending populations → export the same filters/time basis with definitions and caveats → Admin reviews any externally shared summary.
- **Alternate paths:** zero denominator gives N/A; incomplete source makes value provisional or unavailable under [06](06-analytics-and-kpis.md), not zero. Recent unfinalized outbound/pickup populations stay visible beside final-outcome metrics. Historical Gentry comparison uses its own definitions plus documented reconciliation.
- **Result / permissions:** scoped merchant view/export per [02](02-personas-and-permissions.md); Operator export is contact-free. No automatic report forwarding.
- **Attention:** freshness, incomplete periods, excluded unknowns and incompatible comparison warning.
- **Success / acceptance:** exported contributors reproduce displayed metrics, scope does not change silently, and no unrelated merchant/contact data leaks. AC07/AC08/AC10/AC12.

## WF10 — Manage merchant users and policies

- **Goal / entry:** Merchant Admin maintains the team and approved operational scope.
- **Primary flow:** invite named recipient with role → acceptance creates only that merchant membership → Admin changes/suspends membership or edits permitted merchant configuration with reason/effective time → review changed access and policy effect on work.
- **Alternate paths:** revoked/expired invite, suspended member, last-Admin removal and source-ownership ambiguity are explicit blocks. Shared User identity across merchants grants no additional membership. Suspend membership without deleting authored history; transferred cases remain visible/unassigned for Admin attention.
- **Result / permissions:** Merchant Admin manages merchant users/settings; Platform uses PF02 administrative recovery, never self-grant or merchant settings authority.
- **Attention:** pending invitations, no responsible active user, readiness changed and policy changes affecting existing cases.
- **Success / acceptance:** two merchant teams remain isolated and attributable; significant settings are Admin-only. AC01/AC02/AC03/AC09.

## WF11 — Inspect Product/SKU performance and ROAS

- **Goal / entry:** merchant wants to know what sells, what delivers/returns and where advertising inputs support decisions; product/order/courier and applicable spend observations are connected or explicitly labeled fallback.
- **Primary flow:** select product/SKU and compatible period/comparison → inspect order/unit/revenue population → inspect outbound delivery/RTO plus separately classified customer returns → inspect direct/generic/unallocated spend and qualified ROAS → drill into contributing items/orders/shipments/adjustments/spend → review justified product attention and source gaps. Use season/classification context when available/necessary, not a required planning engine.
- **Alternate paths:** unknown item/variant link, pending outcome, stale input, missing spend/revenue or currency/attribution conflict remains visible; unavailable ROAS is not zero. Multi-product shipments appear once per product-containing population, never as independent unit deliveries. Later return does not erase outbound delivery. Current stock/season is not substituted for dated historical observations.
- **Result / permissions:** Admin/Operator view own merchant analytics; significant attribution/economic/mapping settings stay Admin-only. No automated replenishment, production order, campaign-budget change or financial transaction results from attention/advice.
- **Attention:** unresolved SKU/outcome linkage, missing/incomplete spend, comparable deterioration or approved threshold exception with sample/definition; no unapproved Gentry tier thresholds copied.
- **Success / acceptance:** practical sales/outcome/spend drill-down and canonical, qualified ROAS; source trust/merchant isolation unchanged. AC07/AC08/AC10/AC15; definitions P01–P06 in06.

## Primary daily journey

Connected orders/shipment evidence enter OpsHub → attention identifies due work → Operator investigates/contacts and prepares action → Admin authorizes/initiates in OpsHub → OpsHub performs the supported provider action → reconcile returned identifiers/status/evidence → close only completed case work → feed operational/Product-SKU/ROAS dashboards. Failed/unsupported/incomplete-onboarding exceptions use labeled manual fallback, never the default connected path. Review product attention with the same source-trust principles.
