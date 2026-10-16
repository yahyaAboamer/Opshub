# Milestone roadmap

Numbers group outcomes; use the task DAG for order. Each local demonstration below uses synthetic data/fake adapters and is **PLANNED**, not executed. A milestone containing controlled qualification or an operational task is not Done merely because its local demo passes.

## M0 — Engineering foundation

Actor: **Engineer**. Included **10 tasks**: [T0001](tasks/T0001.md), [T0002](tasks/T0002.md), [T0003](tasks/T0003.md), [T0004](tasks/T0004.md), [T0005](tasks/T0005.md), [T0006](tasks/T0006.md), [T0007](tasks/T0007.md), [T0008](tasks/T0008.md), [T0009](tasks/T0009.md), [T0010](tasks/T0010.md).

Local entry: accepted no predecessor contracts for T0001, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: none.

Demonstration: Initialize a synthetic checkout, run the qualified toolchain/DB/queue harness, start web/API and worker with fake services.

Expected visible/test result: Health/readiness and redacted correlation are visible; wrong DB and failed atomic enqueue are rejected; no business capability exists.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local foundation; patches/runtime availability and later purchased services remain qualifications.

## M1 — Tenant identity and authorization

Actor: **Merchant Admin, Operator and scoped platform user**. Included **11 tasks**: [T0101](tasks/T0101.md), [T0102](tasks/T0102.md), [T0103](tasks/T0103.md), [T0104](tasks/T0104.md), [T0105](tasks/T0105.md), [T0106](tasks/T0106.md), [T0107](tasks/T0107.md), [T0108](tasks/T0108.md), [T0109](tasks/T0109.md), [T0110](tasks/T0110.md), [T0111](tasks/T0111.md).

Local entry: accepted T0003, T0004 contracts for T0101, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0003, T0004, T0005, T0007.

Demonstration: Use synthetic OIDC; verify initial Admin, accept invitation, change/suspend a member, switch MA Admin to MB Operator and attempt a foreign record.

Expected visible/test result: Accessible access/member/context views work; foreign data and platform business commands are denied; last Admin preserved.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local identity journey; actual Auth0/Resend, representative/session/suspension policies remain gated.

## M2 — Evidence provenance and immutable intake

Actor: **Merchant Operator and Admin**. Included **10 tasks**: [T0201](tasks/T0201.md), [T0202](tasks/T0202.md), [T0203](tasks/T0203.md), [T0204](tasks/T0204.md), [T0205](tasks/T0205.md), [T0206](tasks/T0206.md), [T0207](tasks/T0207.md), [T0208](tasks/T0208.md), [T0209](tasks/T0209.md), [T0210](tasks/T0210.md).

Local entry: accepted T0109 contracts for T0201, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0006, T0007, T0008, T0103, T0105, T0108, T0109.

Demonstration: Preview an invalid/repeated synthetic intake, inspect each disposition/provenance, submit/approve a correction, replay a suppressed snapshot and repair an ambiguous native binding.

Expected visible/test result: Exact accounting and selected-versus-source history visible; missing coverage/inherited hold blocks relevant work.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local evidence slice; actual private S3/retention/legal/source-selection choices remain gated.

## M3 — Read-only commerce slice

Actor: **Merchant Operator and Admin**. Included **9 tasks**: [T0301](tasks/T0301.md), [T0302](tasks/T0302.md), [T0303](tasks/T0303.md), [T0304](tasks/T0304.md), [T0305](tasks/T0305.md), [T0306](tasks/T0306.md), [T0307](tasks/T0307.md), [T0308](tasks/T0308.md), [T0309](tasks/T0309.md).

Local entry: accepted T0201, T0105, T0005 contracts for T0301, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0005, T0007, T0105, T0201, T0204, T0205, T0206, T0207, T0208, T1204.

Demonstration: Connect fake Shopify, receive order with repeated native line contents and catalog bindings, search Order/items, inspect evidence; simulate missing scope and fallback import.

Expected visible/test result: Own Orders/catalog/source-readiness journey usable, incomplete inputs explicit; mutations0.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local normal read loop plus separately authorized actual read qualification; no provider account required for demo.

## M4 — Read-only courier slice

Actor: **Merchant Operator**. Included **6 tasks**: [T0401](tasks/T0401.md), [T0402](tasks/T0402.md), [T0403](tasks/T0403.md), [T0404](tasks/T0404.md), [T0405](tasks/T0405.md), [T0406](tasks/T0406.md).

Local entry: accepted T0302, T0303 contracts for T0401, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0207, T0301, T0302, T0303, T0305, T0306, T1204.

Demonstration: Attach fake Bosta shipment, deliver duplicate/out-of-order callback and reverse Delivered evidence, inspect shipment detail/source conflict.

Expected visible/test result: One accepted outbound, real extra consignment retained as discrepancy, counter is not timeline; separate business/courier truth.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local courier journey plus separately authorized actual account/callback/read proof; no booking.

## M5 — Operational contact slice with synthetic starts

Actor: **Merchant Operator and Admin**. Included **7 tasks**: [T0501](tasks/T0501.md), [T0502](tasks/T0502.md), [T0503](tasks/T0503.md), [T0504](tasks/T0504.md), [T0505](tasks/T0505.md), [T0506](tasks/T0506.md), [T0507](tasks/T0507.md).

Local entry: accepted T0303, T0401, T0209 contracts for T0501, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0006, T0008, T0105, T0202, T0205, T0207, T0209, T0303, T0401, T0403.

Demonstration: Enter confirmation; reserve/start a fake external-call slot, record failed→reached→failed near approved test spacing, reopen and request fourth; inspect reached action work.

Expected visible/test result: Only three ordinary authorized slots; fourth denied for both roles; reach retained and unfinished action visible; backlog unaffected by dashboard dates.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Synthetic contact starts only. Production timing/history and actual S3/recovery/exclusive authority precede T1303.

## M6 — External action safety and recovery

Actor: **Merchant Operator and Admin with deterministic worker harness**. Included **9 tasks**: [T0601](tasks/T0601.md), [T0602](tasks/T0602.md), [T0603](tasks/T0603.md), [T0604](tasks/T0604.md), [T0605](tasks/T0605.md), [T0606](tasks/T0606.md), [T0607](tasks/T0607.md), [T0608](tasks/T0608.md), [T0609](tasks/T0609.md).

Local entry: accepted T0501, T0105, T0202 contracts for T0601, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0007, T0008, T0103, T0105, T0202, T0206, T0208, T0209, T0301, T0402, T0501, T0504, T0506, T0507.

Demonstration: Prepare/approve same fake booking twice; race workers, lose response after effect, attempt fallback, then recover positive native result; restore before objective.

Expected visible/test result: At most one controlled dispatch, unknown holds both paths, native result reconciles once; restored access/privacy/authority gates distinct from egress.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local safety engine and fault proof. No actual provider write, real contact or cloud restore qualified yet.

## M7 — Qualified per-class consequential actions

Actor: **Merchant Admin; qualified account operator and owner for later evidence**. Included **14 tasks**: [T0701](tasks/T0701.md), [T0702](tasks/T0702.md), [T0703](tasks/T0703.md), [T0704](tasks/T0704.md), [T0705](tasks/T0705.md), [T0706](tasks/T0706.md), [T0707](tasks/T0707.md), [T0708](tasks/T0708.md), [T0709](tasks/T0709.md), [T0710](tasks/T0710.md), [T0711](tasks/T0711.md), [T0712](tasks/T0712.md), [T0713](tasks/T0713.md), [T0714](tasks/T0714.md).

Local entry: accepted T0608, T0305 contracts for T0702, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0305, T0308, T0309, T0404, T0405, T0406, T0608, T1205.

Demonstration: With fakes compare annotation triggers, booking, replacement creation and cancellation; exercise result/unknown path for each; inspect capability dossier.

Expected visible/test result: Each class has independent evidence/state, no automatic first class, unsupported capability visibly unavailable.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local class adapters plus separately authorized actual qualification. T0701 owner selection uses actual evidence; no pilot class enabled.

## M8 — Returns pickups replacement and cleanup

Actor: **Merchant Operator and Admin**. Included **6 tasks**: [T0801](tasks/T0801.md), [T0802](tasks/T0802.md), [T0803](tasks/T0803.md), [T0804](tasks/T0804.md), [T0805](tasks/T0805.md), [T0806](tasks/T0806.md).

Local entry: accepted T0505, T0404 contracts for T0801, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0205, T0404, T0505, T0605, T0607, T0702, T0703, T0704.

Demonstration: Inspect unpaid-collected versus paid-pending pickup, separate RTO/post-receipt return, request linked replacement, fail booking after create, investigate cleanup predicate.

Expected visible/test result: Independent physical/payment/return truth, one new linked Order retained, incomplete effects remain open; cleanup explains actual predicate.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local end-to-end recovery/cleanup. Exact commercial/consent/physical policy and per-class real effects remain gated.

## M9 — Product performance Meta ROAS and exports

Actor: **Merchant Operator and Admin**. Included **15 tasks**: [T0901](tasks/T0901.md), [T0902](tasks/T0902.md), [T0903](tasks/T0903.md), [T0904](tasks/T0904.md), [T0905](tasks/T0905.md), [T0906](tasks/T0906.md), [T0907](tasks/T0907.md), [T0908](tasks/T0908.md), [T0909](tasks/T0909.md), [T0910](tasks/T0910.md), [T0911](tasks/T0911.md), [T0912](tasks/T0912.md), [T0913](tasks/T0913.md), [T0914](tasks/T0914.md), [T0915](tasks/T0915.md).

Local entry: accepted T0202, T0304, T0404, T0507, T0007 contracts for T0901, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0006, T0007, T0202, T0206, T0207, T0208, T0301, T0302, T0303, T0304, T0404, T0502, T0506, T0507, T0609, T0801, T0802, T0805, T1204.

Demonstration: Use fixed cohort, inspect six KPIs; open A/B Product/SKU and ROAS contributors; revise spend, compare prior period, export same generation then revoke permission.

Expected visible/test result: 6/10,3/5,1/5,2/4,3/5,1/5 and ROAS4.0 reproduce; A/B overlap not additive; partial/revised/missing states match exports; download revoked.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local analytics journey plus actual Meta input qualification; production MD06/MD07 definitions still gated.

## M10 — Platform control plane and commercial shell

Actor: **Scoped Platform Admin and Merchant Admin**. Included **5 tasks**: [T1001](tasks/T1001.md), [T1002](tasks/T1002.md), [T1003](tasks/T1003.md), [T1004](tasks/T1004.md), [T1005](tasks/T1005.md).

Local entry: accepted T0108, T0109, T0307 contracts for T1001, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0005, T0106, T0108, T0109, T0205, T0307, T0606, T0901, T0910, T0911.

Demonstration: Provision MA within assigned scope, inspect safe health; suspend/reactivate $0 offering, try customer drill-down/self-grant; merchant reviews settings/service notices.

Expected visible/test result: Separate readiness/service/commercial history; preserved data and bounded reconciliation; customer/merchant business access denied to platform.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local control-plane/commercial journeys; actual access/grace/retention policy and service procurement remain gated.

## M11 — Migration realization and private rehearsal

Actor: **Merchant Admin and authorized data/reconciliation reviewer**. Included **8 tasks**: [T1101](tasks/T1101.md), [T1102](tasks/T1102.md), [T1103](tasks/T1103.md), [T1104](tasks/T1104.md), [T1105](tasks/T1105.md), [T1106](tasks/T1106.md), [T1107](tasks/T1107.md), [T1108](tasks/T1108.md).

Local entry: accepted T0308, T0405, T0914, T0206 contracts for T1101, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0203, T0204, T0205, T0206, T0209, T0304, T0308, T0405, T0505, T0609, T0901, T0913, T0914, T1005, T1205.

Demonstration: Parse synthetic mixed groups into inactive run, crash/replay, inspect all dispositions, exact/explained/untrusted oracle differences, seed/repair/privacy holds and drifted read approval.

Expected visible/test result: Usable run report and one validated read generation only; missing closure/continuity blocks publication; external action/contact counts0.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Local migration tools plus separately authorized private census/rehearsal. No production activation/cutover implied.

## M12 — Read shadow and pilot readiness

Actor: **Authorized operations/recovery lead and Merchant Admin**. Included **11 tasks**: [T1201](tasks/T1201.md), [T1202](tasks/T1202.md), [T1203](tasks/T1203.md), [T1204](tasks/T1204.md), [T1205](tasks/T1205.md), [T1206](tasks/T1206.md), [T1207](tasks/T1207.md), [T1208](tasks/T1208.md), [T1209](tasks/T1209.md), [T1210](tasks/T1210.md), [T1211](tasks/T1211.md).

Local entry: accepted T0004, T0005, T0009 contracts for T1201, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0004, T0005, T0008, T0009, T0010, T0107, T0109, T0111, T0208, T0209, T0210, T0307, T0308, T0309, T0404, T0405, T0406, T0609, T0706, T0711, T0712, T0713, T0714, T0913, T0914, T0915, T1005, T1106, T1107, T1108.

Demonstration: Against synthetic staging/mock source run disabled shadow comparison, isolated restore and key/coverage/revocation failure probes; inspect readiness report.

Expected visible/test result: Current grant/privacy checks precede access; separate egress holds reconstructed; source/KPI/queue discrepancies actionable and calls/mutations disabled.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Actual provisioning/deployment/read shadow require separate permission, measured targets and real source qualification. Local demo is not real shadow completion.

## M13 — Controlled actions contact and cutover readiness

Actor: **Owner/current Merchant Admin and authorized operations lead**. Included **6 tasks**: [T1301](tasks/T1301.md), [T1302](tasks/T1302.md), [T1303](tasks/T1303.md), [T1304](tasks/T1304.md), [T1305](tasks/T1305.md), [T1306](tasks/T1306.md).

Local entry: accepted T1207, T0701, T0805, T0608, T1205 contracts for T1301, appropriate synthetic environment and human local implementation permission. Each other task starts only on its exact predecessors. Whole-milestone external contracts needed before all tasks can exit: T0507, T0606, T0608, T0701, T0707, T0708, T0709, T0710, T0804, T0805, T1108, T1202, T1205, T1207.

Demonstration: In synthetic rehearsal hold incumbent starts, drain paused sender, select one class, preserve contact budget, apply continuous-traffic delta and exceed approved held-start window.

Expected visible/test result: One compatible authority or safe held gap; material drift invalidates signoff; abort never blindly enables incumbent; existing business effects preserved.

Exit evidence: all included tasks accepted in their declared scopes; produced boundaries/actual test and review evidence; relevant browser journey and tenant/security/golden assertions; stage-applicable decisions and rollback/disable proof. Readiness for separately authorized first/additional class, contact and exact cutover operations. No production operation occurs in Phase6.
