# Independent council review — Red-teamer

**Verdict: AMEND before Phase 6 handoff.** The design has strong safety boundaries and is suitable for bounded correction. It does not yet prove that a controlled Gentry pilot can migrate safely or that OpsHub interprets its inputs correctly; the package accurately identifies execution evidence as future work. I am not recommending implementation, provider experiments, production activation or cutover now.

I read migration documents 00–17, `evidence/migration/golden-contracts.json`, approved owner decisions, and the relevant architecture data, external-action, analytics, privacy and recovery contracts. I did not read other council responses. Phases 1–4 approval is accepted; residual OP/A/MD choices remain unresolved. Findings concern missing or ambiguous **validation contracts**, rather than a demand to implement them in Phase 5.

The strongest existing protections are native scoped identity, preserved conflicting evidence, exact contributor comparisons, no blind retry after uncertain effects, separate physical/payment truth, and recovery access gates. I found no basis to claim that the package deliberately promotes legacy formula results into canonical truth. The remaining risk is that broad safety requirements can pass a review without testing the transitions below.

## Prioritized findings

### 1. P1 — Exclusive authority per action class does not exclude incompatible actions across classes

**Evidence:** `docs/migration/12-shadow-and-parallel-run.md`, “Controlled action pilot ordering” and “Parallel run authority”; `13-cutover-and-rollback.md`, CT01-B/H. The ledger switches one class at a time. The explicit coupling example is replacement creation triggering native booking. Architecture `06-external-action-safety.md`, “Execution protocol and concurrent Admins,” recognizes cancellation-versus-booking/replacement conflicts, but its local reservations cannot serialize an incumbent action.

**Failure:** OpsHub owns booking while Gentry/manual processes still own cancellation or replacement. Each class has exactly one authority, yet both systems can act on the same order using stale evidence. The signed per-class ledger remains correct while an incompatible pair of effects occurs. A later discrepancy cannot undo cancellation or physical dispatch.

**Correction:** Add a cross-class conflict/dependency matrix to the authority ledger. Transfer conflicting classes together, or explicitly hold the incumbent conflicting scope until the target operation is settled. Require a CT/EA test racing incumbent cancellation against OpsHub booking, and incumbent replacement against OpsHub cancellation. State how the shared prohibition is enforced when Gentry cannot consume OpsHub reservations; if enforcement is unavailable, the conflicting class stays held. This need not introduce a shared distributed lock service.

### 2. P1 — Inherited legacy holds and contact usage need an explicit independent recovery seed

**Evidence:** `03-migration-pipeline.md`, “Inbound does not replay history”; `11-recovery-validation.md`, RV03/RV10 and RV-G3; `13-cutover-and-rollback.md`, CT01-B/E/F. Architecture `13-deployment-and-environments.md` writes independent records before OpsHub dispatch, handover or contact issuance. The migration design preserves imported unknown effects and historical allowances, but does not explicitly require independently surviving records for every inherited restriction before enabling actions.

**Failure:** A legacy unknown booking or used contact allowance is imported, no new OpsHub effect/contact is issued, and a later restore predates the migration. The ordinary OpsHub dispatch journal can have complete coverage while containing no record of that inherited restriction. Reacquired provider data may not reconstruct an uncertain legacy call or missing-native-reference effect. A new case/objective then appears eligible.

**Correction:** Define a signed, minimal migration safety manifest covering inherited unknown effects, handovers, consumed/uncertain contact allowances, unsupported live episodes and their native/business scopes. Independently retain it before authority transfer, and include its enumeration/coverage in RV-G3. Add a restore-before-migration experiment with **zero post-migration OpsHub dispatch markers**. Missing seed coverage must quarantine the affected scope. CT01's generic descriptor requirement may intend this already; make that obligation and its test explicit.

### 3. P1 — Completed privacy dispositions must constrain future imports, not only restores

**Evidence:** `15-privacy-and-test-data.md`, “Cleanup and retention decisions” and PV07–PV09; `03-migration-pipeline.md`, replay/new-run rules and MP-T09; `13-cutover-and-rollback.md`, “Corrected mapping and re-import.” Architecture privacy/recovery contracts explicitly replay dispositions after database restore. They do not explicitly specify how an old snapshot, changed-parser run or delayed source receipt is prevented from reintroducing previously redacted data into ordinary access.

**Failure:** Redaction completes correctly across current data. A later approved re-import reads an earlier immutable capture and creates a fresh observation or generation with the removed fields. No database restore occurs, and the existing privacy-during-staging test need not exercise a disposition that predates the new run.

**Correction:** Require acquisition/intake, normalization and publication to consult the current source-scoped privacy disposition, including late arrivals and superseded files. Define authorized evidence-hold exceptions and minimized suppression identifiers under MD14; do not assume all source data may be retained or all must be deleted. Add tests for same-snapshot replay, a changed importer/mapping version, late callback, and old-generation export after a completed disposition. Expected results must separately cover restricted intake, canonical fields, projections and downloads.

### 4. P1 — Identity repair after execution starts needs a two-sided effect quarantine

**Evidence:** `02-identity-mapping.md`, IM02/IM-T10; `13-cutover-and-rollback.md`, “Corrected mapping and re-import.” Both preserve old associations and invalidate **unstarted** dependent approvals. EA14 tests edited intent, but there is no named experiment for correcting a false native/canonical association after an effect may have been sent.

**Failure:** An incorrectly crosswalked shipment/action is attached to order A; its effect is unknown or successful. A reviewed repair moves the selected association to B. A now appears to lack a shipment or completed objective, while its original dispatch scope still has consequences. Preserving historical links alone does not specify which identities remain nonactionable, and a newly derived objective can bypass the old reservation.

**Correction:** State that identity repair never rekeys or releases a started/unknown effect's original reservation. Quarantine both affected subjects and linked objectives until independent native/business-scope reconciliation establishes which actions remain permissible. Carry contact allowances conservatively through disputed case remaps. Add an IM/EA/CT experiment: false match → accepted/lost-response effect → remap → new request on each side. Assert zero additional mutation/contact starts until the affected scopes are resolved, with both histories retained.

### 5. P2 — “All pages plus overlap” is not yet a proof of a closed capture boundary

**Evidence:** `03-migration-pipeline.md`, MP01 and MRUN01; `08-provider-contract-validation.md`, PC-S02/S03 and PC-B04; `13-cutover-and-rollback.md`, CT01-D. The package correctly rejects a fictitious globally atomic snapshot and requires fixed coverage, overlap and post-cutoff buffered work. It does not specify the acceptance proof when records move during pagination, updates share a cutoff timestamp, or a previously captured child/object disappears.

**Failure:** All requested pages succeed, every captured unit has a disposition, and counts reconcile. An object moved across the pagination boundary was never captured, or a removed order line remains selected indefinitely. Conservation of captured rows cannot detect either problem. A configurable overlap is not a completeness guarantee without a qualified delay/order bound or an independent reconciliation process.

**Correction:** Require provider-specific capture-closure evidence: ordering/cursor and boundary semantics, inclusive overlap/dedup behavior, buffering/reconciliation across initial-to-incremental handoff, and explicit withdrawal/deletion treatment that distinguishes missing data from authoritative removal. Add mutations between page reads, equal-boundary updates, late receipt outside the initial overlap, and removed child-item scenarios. Where the provider cannot establish a bound, require repeated inventory reconciliation and an explicit incomplete/held scope rather than a complete flag. Preserve historical assertions while correcting current membership.

### 6. P2 — Golden contracts do not yet fix enough input semantics to prevent circular validation

**Evidence:** `06-golden-datasets.md`, “Envelope and reproducibility” and GD27/GD28/GD34; `07-kpi-regression-suite.md`, “Result assertion envelope”; `evidence/migration/golden-contracts.json`, `merchants`, `facts`, `policies`, `required_scenarios`. The JSON declares MB and reused aliases, but supplies no MB business objects that collide with MA. Several fact groups lack explicit tenant/account, cohort clocks or reporting-window inputs. Contact facts mostly provide aggregate attempts/reached/action booleans. `TEST-POLICY-v1` names policies without defining the relevant clock/selection rules in the JSON. Many scenarios are listed rather than supplied as input/expected-output pairs.

**Failure:** Future fixture realization can fill those gaps from the implementation's own defaults, directly seed already-interpreted booleans, and compare resulting contributor sets to the same assumptions. The KPI arithmetic passes while raw-to-canonical identity, event continuity, period selection or tenant binding is wrong. Exact member comparisons are necessary, but only test the members represented by independently specified inputs.

**Correction:** Keep the current JSON explicitly a partial semantic expected-value catalog. Before treating the golden contract as complete, specify a minimal independent source-to-canonical fixture layer: actual MA/MB collisions, distinct repeated item IDs, contact events versus summaries, declared clocks/precision, source-account bindings, reporting parameters and expected dispositions/bindings. Define test-policy rules and intentional omissions without selecting production OP policies. No importer implementation is requested. Require future realization to preserve that approved input/expected mapping and prove that deliberately wrong parsers/mappers fail.

## Assumptions and limits

- These are foreseeable failure paths inferred from contract gaps, not observed production incidents.
- No live provider behavior, customer record, application implementation, RLS deployment, recovery drill or actual migration was inspected or executed.
- Existing broad fail-closed requirements remain binding. An unresolved policy cannot be replaced with a test default at launch.
- Recommendations preserve OD01–OD09 and the approved architecture. They add bounded proof obligations, not a new product scope or an engineering backlog.

## Strongest objection to this position

The package repeatedly requires complete holds, current privacy rules, safe source coverage and zero unexplained errors. A careful implementation team could derive all six corrections from those requirements, and Phase 5 intentionally defers fixture realization and provider qualification. Requiring every experiment now risks duplicating Phase 6 work.

That objection is strongest for findings 5 and 6. It is weaker for findings 1–4: the existing named tests can pass while these specific cross-boundary failures remain untested. A short amendment naming the invariant, protected scope and failing experiment is enough; implementation is unnecessary. With those amendments and explicit preservation of unresolved owner/provider gates, I would support approving Phase 5 as a validation design—not as evidence that migration or cutover is safe to execute.

<oai-mem-citation>
<citation_entries>
MEMORY.md:3-4|note=[Used prior workspace evidence and unresolved-policy boundaries; current documents govern review]
</citation_entries>
<rollout_ids>
01a1365c-3467-7632-b95d-63db866d071b
</rollout_ids>
</oai-mem-citation>
