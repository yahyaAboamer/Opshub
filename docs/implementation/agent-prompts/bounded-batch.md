# Future bounded-batch implementation prompt

Replace TASK_ID_SET with an explicit finite set. This prompt is not executed during Phase6.

```text
Authorized Task ID set: TASK_ID_SET
Authorized scope: implement only this explicit bounded set locally. Dependencies outside it must already be accepted; do not expand the batch to implement missing predecessors. Nonlocal task effects still require their own explicit authorization and accountable role.

You are implementing OpsHub under the approved Phase6 plan in a fresh chat. Gentry is legacy evidence; OpsHub is the target SaaS.

Before any edit:
- Read current repository AGENTS.md, docs/implementation/START-HERE.md and execution-state.md, then task-manifest.yaml and decision-gates.yaml for the selected Task IDs.
- Read each selected task Markdown, its exact relevant spec sections and its accepted predecessor C-task-v1 contract records. Do not read every Phase1–6 document by default. Broaden only to investigate an actual cited ambiguity.
- Inspect the existing repository, actual Git/worktree/base-main revisions, current user changes and previously completed work. Never overwrite or redo unrelated work. T0001 may establish Git if still absent; other tasks require the accepted repository.
- Confirm the current direct or recorded human authorization covers local implementation of the selected scope; record it. Phase6 planning alone does not authorize coding. Do not demand repeated permission when the human has already explicitly authorized that scope.
- Validate accepted predecessor contracts merged on current main, fixture inputs, effective START/current-stage gates and environment readiness. A future SHADOW/ACTION_ENABLEMENT/CUTOVER gate does not block unrelated synthetic code. A missing required start gate does.
- Claim one Task ID/branch/worktree and all editable-area/shared locks through the integration owner. Codex and Claude Code never concurrently own the same ID or overlapping write/lock boundary. Do not edit the canonical manifest concurrently; the integration owner owns status/claims/acceptance.
- Follow listed permitted environments/effects and filesystem/tool permissions. Local approval does not permit provisioning services, sending account/customer messages, calling real provider APIs, controlled real effects, deployment, production shadow or cutover; those need their own explicit envelope and current authority.

During the task:
- For a user-facing task (an `apps/web/features/` area): write the journey client contract against accepted producer ports before components; build UI with its listed read adapter as one vertical slice; reuse the T0004 shell, tokens and state primitives; represent loading/empty/validation-error/forbidden/stale/pending/unknown/partial-source/success states; prove the journey in the browser against the running web/API/PostgreSQL (worker if asynchronous) with fake providers at narrow and desktop viewports with keyboard/focus/label review. API-only evidence cannot accept it. A missing producer field/state stops the task with a bounded contract amendment request.
- Skill routing: use specialized skills only when relevant to the selected task (UI tasks: approved frontend-design/web-design/React skills; PostgreSQL/RLS: approved Postgres skill; high-risk security/recovery: approved review skills). Tests and approved acceptance criteria remain authoritative; never load unrelated skill packs because they are installed; an unavailable skill is not a blocker.
- Use the approved architecture and actual accepted boundary contracts. Resolve concrete file allocation inside the listed areas; do not invent neighboring interfaces or silently change a shared protocol.
- Fix independent synthetic expected inputs/results before evaluation. Implement the bounded actor/data/workflow behavior and named negative tests, including UI navigation/loading/empty/error/stale/permission/accessibility where specified.
- Keep source/, Phases1–5 and existing evidence unchanged. No raw customer/secret data in code, fixtures, prompts or output. Separate facts, selection/interpretation and unknown evidence.
- Never treat timeout/lease/empty search as no-effect, reset contact budgets, hide real duplicate results, infer collection from payment or close a case from approval alone.
- After any dependent/shared merge update from current main and rerun affected deterministic/tenant/contract checks before acceptance.
- On source contradiction, record exact locators, affected IDs, consequence and bounded proposed resolution; stop the affected task rather than inventing business policy. Continue only independently eligible tasks within the authorized set.
- Unexpected XL/broad scope must split with new stable IDs before execution; no ID recycling.

Completion:
- Provide actual base/head/main revisions, exact commands/environment/tool versions, independent fixture/policy/source digests, actual pass/fail/not-checked output and what each proves; request/effect/start counts and fault barriers for safety; synthetic browser journey evidence for UI against the running stack, with viewport and accessibility results.
- All command names in the plan are PLANNED until the repository defines them. Do not fabricate scripts/results or mark not-executed tests PASS.
- Update the produced C-task-v1 record and actual completion-evidence links; independent reviewer/integration owner decides acceptance and merge. Update canonical status/readiness/digest and generated views through that owner; preserve unrelated changes.
- A qualification dossier can be complete while its capability is unavailable; required core qualification remains blocked until its required actual verdict. Local completion does not imply real integrated MVP readiness or production approval.

Choose only eligible tasks from the named set in dependency/lock order. Work one claimed task at a time unless two independent agents have explicit nonoverlapping assignments. Stop when all named tasks are accepted or all remaining named tasks are genuinely blocked. Record accepted evidence, exact remaining blockers and resumption IDs. Do not proceed to the next milestone, real provider calls, messages, deploy or cutover by implication.
```
