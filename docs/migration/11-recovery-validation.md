# Restore and recovery validation contracts


## RV19–RV21 — Migration-specific recovery composition

**RV19:** backup before migration; import legacy unknown sole-outbound scope and consumed/uncertain three-contact allowance; persist migration-safety-seed; execute zero new OpsHub effects/contacts; restore backup. Enumerate seed independently and reconstitute restrictions before fresh discovery/access/egress. No dispatch-journal-only completeness claim; missing seed/coverage quarantines affected connection/merchant.

**RV20:** false native binding OA→OB repaired after may-executed action/contact. Restore before repair, replay native evidence and minimal independent repair descriptor. Both disputed scopes remain held until reviewed native/business continuity resolution; old native intent/result/allowance history unchanged.

**RV21:** completed privacy disposition survives not only DB restore but old snapshot re-import, changed parser/mapping, late receipt and retained generation download. Current suppression/approved holds apply before data access/publication. Missing disposition coverage blocks affected access.

RV-G3 now explicitly includes migration-seed and repair descriptor enumeration/versions/coverage as well as ordinary dispatch/handover/contact markers. RV-G2 includes current suppression on replayed data. A fully enumerated empty OpsHub journal does not prove no inherited legacy restrictions existed.
Turn [Phase 4 recovery](../architecture/13-deployment-and-environments.md) into future executable experiments. A restored database is not an operationally safe system. Synthetic/redacted drills use a new isolated DB, independently surviving provider/mock effect store, private journal/privacy manifests and runtime recovery epoch. **No restore or infrastructure work is executed here.**

## Experiment protocol

For each RV case: capture backup at T0; make named change/effect at T1; preserve independent records; restore T0 into isolated environment at T2 with all user access and mutation/contact egress denied; terminate/drain old senders; establish a new independently configured recovery epoch; enumerate/reconcile surviving records and privacy/grants; assert before/after gates and record measured RPO/RTO under approved targets. Keep failure injection/time checkpoints deterministic.

Backup includes app jobs but their delivery is not authorization to repeat effects. Restore ordinary records, grants/RLS/FKs/file hashes/interpretation generations and secret-key availability; unknown effects need held scopes rather than historic status replay.

## Recovery test matrix

| ID/experiment | Post-backup change / restore fault | Expected outcome and required proof |
|---|---|---|
| RV01 ordinary restore | Orders/items/cases/assertions/corrections/generations from backup | Integrity/count/digest and real-role RLS pass; jobs held; new epoch invalidates sessions/invites; current authority/privacy review precedes access |
| RV02 recent provider effect | Booking/replacement executes after T0; DB loses result | Independent pre-dispatch/result descriptor rebuilds reservation/native match. No send from restored Approved job; positively reconcile once |
| RV03 missing whole objective | Order/connection/objective created after T0 then effect happens | Descriptor includes account/native subject/business scope/dependencies; rediscovery stays same held scope. Missing reliable binding quarantines whole affected merchant/connection |
| RV04 revoked membership/session | Admin/Operator/platform grant revoked after T0, session still unexpired at backup | Restored session denied; fresh OIDC login identity only. Independent verified current grant/recovery procedure prevents resurrected access/approval |
| RV05 consumed invitation | Invitation consumed/revoked after T0 | New epoch invalidates all restored tokens; no duplicate acceptance/escalation. Newly issued verified invitation required |
| RV06 privacy/deletion | Redaction authorized/completed/partial after T0 across DB/projections/objects | Independent manifest replay before any reads/exports; partial authorization reconciled idempotently under policy; no resurrected customer data |
| RV07 manual handover | Handover issued and off-platform booking after T0 | Independent handover survives, both connected/manual repeat denied; native result attaches to same business scope. Missing DB handover cannot mint a new one |
| RV08 missing journal coverage | Missing page/prefix/version/coverage checkpoint/unreadable newer schema | Complete paginated enumeration and coverage cannot be proven → affected merchant/connection egress remains quarantined; no timer release |
| RV09 connection credential rotation | Token/key pair rotated/revoked/account ownership changed after T0 | Restored old credential never assumed valid. Confirm current ownership/capability/version and protected decrypt keys, reauthorize/reconnect/rotate as required; unknown effects remain held |
| RV10 lost contact allowance | Actual/uncertain contact-start after T0, budget three | Independent contact markers reconstruct held ordinal/case/purpose; no fourth ordinary start or fabricated occurrence/spacing. Missing scope/coverage blocks affected contact workflow |
| RV11 stale worker | Old sender survives while restored worker claims job | Old process stopped/drained and request lifetime settled; new runtime fenced. Local CAS cannot prevent old network send; no releasing its scope on lease expiry |
| RV12 missing privacy coverage | Manifest interval/prefix/object unavailable or tombstone unreadable | Affected data remains inaccessible, including exports and platform/customer support; no “DB restored” access waiver |
| RV13 lost approved authority | Backup approval names Admin grant with no current independent revalidation | Old approval remains historical only; unstarted effects require current legitimate authority/reapproval; no platform self-grant |
| RV14 encryption/object failure | Backup restored but necessary journal/evidence/credential decrypt key missing | Recovery incomplete; preserve data, block relevant access/effects. No discard of encrypted unknown reservations |
| RV15 provider-only discrepancy | Provider effect has no corresponding approval/journal | Retain source-reported result/discrepancy; not retroactively authorized. Expand quarantine/investigate scope; no automatic compensation |
| RV16 application rollback | Restore older app image against compatible schema/current evidence | Preserve current effects/holds/privacy/epoch/grants; verify old version understands new protocol. Incompatible journal/state means egress disabled/forward fix |
| RV17 contact no-call uncertainty | Contact issuance marker exists but no actual call record | Marker means may-have-started; allowance/spacing held until reliable no-call/current policy resolution; not inferred successful reach |
| RV18 retention gap | Allowed backup older than surviving reservation/privacy coverage | Backup outside safety coverage not reopened as ordinary service; retain/quarantine/escalate. Retention must cover every restorable horizon plus unresolved holds |

## Separate access and egress gates

**RV-G1 infrastructure:** isolated restore verified; old runtime cannot dispatch; recovery epoch outside DB active; runtime grants/RLS/FKs/files/decrypt material valid; version compatibility proven.

**RV-G2 user access:** independently verified current merchant/platform grants, source ownership/service state and privacy coverage/replay pass. Restored grants cannot certify themselves; fresh login alone does not pass. Deny reads/export/download until this gate per merchant is signed by the authorized recovery procedure.

**RV-G3 contact/action egress:** complete dispatch/handover/contact journal enumeration and independent coverage; reconstruct every possibly missing hold; qualified positive/no-effect evidence and old-path containment; capabilities/current Admin/dependencies checked; outstanding unknown scopes visibly blocked. Unreadable/unbound missing records quarantine the whole affected connection/merchant.

Operational reads may resume after G1/G2 while specific effect/contact holds remain. Egress can resume only for proven unaffected scopes and qualified action classes after G3 review; journal-wide uncertainty blocks affected connection as a whole. “No pending rows in restored DB” is never a coverage test.

## Evidence and targets

Record backup/source cutoffs, independent coverage bounds/page totals/descriptor digests, missing/held/recovered scope inventory, current grant verifications, privacy replay counts/status, credential versions (never secrets), old-process termination and protocol-version evidence, actual provider requests/effects during recovery, user-access probes and signed gate decisions.

Require zero unauthorized restored access, revived invitation privilege, resurrected privacy data in reopened access or blind duplicate effect/contact starts. RPO/RTO, retention horizon and escalation time remain A05/A06/MD12–MD14 owner targets, measured in future drills. Recovery journal protects minimum business reservation knowledge; it does not justify retaining unlimited customer payload.
