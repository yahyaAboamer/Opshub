# Cutover, rollback and re-import design


## Cutover approval envelope and inherited restrictions

MD11–MD13/MD15 approve an exact base generation/cutoff, buffered catch-up classes, material changes that invalidate sign-off, maximum held-start window tied to merchant operational deadlines, backlog handling owner and abort/escalation path. Bounded nonmaterial deltas may use explicit reviewed delta-validation against that base; changes to identity, authority, physical/consent prerequisite, unknown-result scope, privacy, policy/version or source closure require renewed affected approval.

Rehearse continuous new orders/updates during approval, cutoff timestamp ties, catch-up backlog and exceeded hold budget. Safe abort can remain a controlled hold if return-to-incumbent authority cannot be proven; it never turns Gentry on automatically. Do not invent a universal hold duration.

Before CT01-H, verify independently durable migration-safety-seed/repair coverage, current privacy suppression, acquisition closure through buffered incremental boundary, and exclusive authority for each connected **conflict group**/eligible scope. A per-class switch cannot leave conflicting booking/cancellation/replacement active in the other system. Authority rollback follows the same matrix/holds and carries inherited restrictions.

**CT-T09:** incumbent cancellation versus target booking across flags. **CT-T10:** continuous-traffic deadline/abort. **CT-T11:** restore before migration with only inherited seed. **CT-T12:** false-match repair after may-executed effect plus re-import/restore. Expected single compatible coordinator or held gap, zero new disputed starts, no forgotten allowance, no resurrected privacy fields.
**Future sequence; no cutover is performed.** Cutover switches authority as well as application use. Application rollback cannot reverse a sent booking, created Order, cancellation, manual action or customer contact. [Phase 4 protocol](../architecture/06-external-action-safety.md) and [recovery](11-recovery-validation.md) apply.

## Preconditions

Approved migration manifest/source scope and all blocking MD/policy choices; validated inactive generation and exact reconciliation; shadow exit; action/provider qualification and restore drills; verified current Admin/access/service state/privacy; trained accountable operator; private evidence/independent coverage; per-class authority ledger including native/manual automation and emergency disable. User-facing communication/access arrangements are planned, not sent here.

## Ordered checkpoint sequence — CT01

| Step | Operation to be authorized later / gate |
|---|---|
| CT01-A freeze/checkpoint | Freeze source mapping/configuration/definition/action-eligibility revisions and deployment protocol versions, record canonical/source/generation cutoffs. External commerce may continue; configuration freeze is not proof of data freeze |
| CT01-B hold starts | Enter ALL_MUTATIONS_HELD for switching class, including Gentry/manual/native automation. Hold contact starts during budget handoff. Record effect/job/request reservations and independent descriptors; deny new starts |
| CT01-C drain and settle | Stop/drain old senders; identify every in-flight/may-have-sent request/handover/contact. Reconcile qualified native results and negative evidence; timeout alone does not settle |
| CT01-D final source sync | Fixed coverage-bound initial/incremental overlap read, all pages/receipts/checkpoints; ingest late changes. Report source skew/coverage and retain post-cutoff buffered work; unread evidence is not presumed absent |
| CT01-E unresolved inventory | Every unmatched/conflicting/unknown effect/old contact budget/partial case/extra shipment has scope, evidence, responsible owner and activation hold. Block unresolved day-one continuity/action prerequisites |
| CT01-F queue reconciliation | Compare incumbent/current operational members with OpsHub cases/objectives, action/contact holds and budgets, required work and native bookings. Imported task/approval label never triggers execution |
| CT01-G read activation/access | Publish exact validated generation with current Admin manifest sign-off; confirm grant/service/privacy gates, role tests, identical contributor export, files and source freshness. Actions still held |
| CT01-H authority switch | Verify old/Gentry/native/manual path nonexecuting for selected class and old process containment. Sign authority ledger, then enable qualified OpsHub capability/limits. Serialize ledger/configuration revision; a deliberate no-authority gap is safer than overlapping starts |
| CT01-I monitor and expand | Limited eligible scope first; native result counts/case closure/queue/source reconciliation, immediate disable on correctness breach. Later classes require independent pass/sign-off |

Initial migration facts and final-sync facts share identity bindings with retained observations/revisions. Real sources are not atomically frozen together; declare exact cutoffs/skew and the read catch-up protocol. Concurrent current state/configuration changes invalidate stale activation approval and require validation of the delta.

## Abort and disable conditions

Abort before switch on missing ownership/coverage, unexpected identity/member/money delta, required dependency omission, uncertain in-flight action/contact, authority overlap, stale source beyond approved target, untrained Admin or failed privacy/recovery gates. After switch, correctness breach disables new starts for affected class/connection/merchant and preserves reads/reconciliation only where safe. No arbitrary number of duplicate/leak incidents is tolerable.

Source outage/performance degradation uses approved MD13 operational thresholds; stale values stay visible. Disable does not mark sent effects failed or silently hand them back to Gentry. Retain all holds and reconcile before alternate authority.

## Rollback types

| Type | Permitted recovery | Forbidden assumption |
|---|---|---|
| Application rollback | Compatible previously reviewed image/read generation; retain schema/evidence/current holds/epoch/privacy; verify old protocol understands new records | Prior UI/DB state means prior business world |
| Staging/import rollback | Withdraw inactive selection; retain immutable snapshot/dispositions; isolate failed child bundle/run | Delete source/evidence and pretend run never happened |
| Interpretation rollback | Select prior valid interpretation only with explicit changed-source/policy/correction review and new visible generation | Hide real later result/correction/privacy state to match old metrics |
| Authority rollback | Disable OpsHub starts, drain/settle/reconcile, transfer exact still-eligible scopes to one incumbent authority with signed ledger/handover | Turn Gentry back on immediately while OpsHub result is unknown |
| Business-action remediation | Separately reviewed Admin/provider-supported corrective action with its own scope/effects/side effects | Automatic cancellation/refund/deletion/compensation of prior action |

External actions already performed remain facts even if undesirable or irreversible. Returning read service to Gentry never erases new replacement native Order or consignment. If old process cannot represent the new hold/link/contact budget, retain a responsible controlled reconciliation path and block affected operations rather than force a rollback.

## Corrected mapping and re-import

Create a new mapping/run/generation against preserved snapshot and current facts. Preview affected identities, every old→new link, field interpretations, KPI contributors/amounts and invalidated unstarted approvals. Preserve prior evidence, run manifests and exported generations. False match repair must detach incorrect selected association with attributable history; never delete a real provider object.

Re-run identical source preserves native/canonical identity and produces no duplicate active objects. Production activation is a separate current signed boundary; fixing a parser does not automatically publish. Later backfill cannot authorize old tasks/effects or reset contact allowance. Privacy/retention holds apply to both old and new run evidence.

## Cutover experiment proof

CT-T01 switching while worker paused after may-send marker; CT-T02 native automatic booking on replacement; CT-T03 final sync source changes during approval; CT-T04 crash after read pointer publish/before capability switch; CT-T05 imported unknown effect with missing native link; CT-T06 post-switch application rollback; CT-T07 return-to-incumbent with new native Order; CT-T08 privacy change during staged activation.

For each, assert one normal mutation authority or deliberate held gap, zero blind repeated request, stable canonical/native scope, full queue/row accounting, current authorization and reproducible validated generation. Capability flags/ledger state alone are insufficient if independent provider automation still executes. [14](14-reconciliation-and-signoff.md) signs exact evidence, not intent to test.
