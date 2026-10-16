# Two-agent execution protocol

Codex and Claude Code use the same canonical manifest, exact task/spec reading set and accepted main. An integration owner serializes manifest/status/claim/lock changes; neither agent starts by independently claiming a shared task in its own branch. No two active claims may own the same ID or overlapping editable boundary/shared lock.

After Git exists, one worktree/branch per task: codex/tNNNN-scope or claude/tNNNN-scope, based on current accepted main. Inspect existing work before editing. A task branch owns only its listed areas and one allocated migration if applicable. Shared package/lockfile/DTO/provider-port/action/recovery protocol, grants and router changes require an explicit integration-owner lock and contract review.

Predecessors must merge before a consumer starts. Freeze actual produced C-task-v1 boundary with typed interface/schema, errors, scope/transaction assumptions, fixture references and exact commands in docs/contracts. Consumer verifies that accepted artifact; it does not invent neighboring signatures. Contract change invalidates affected downstream readiness and requires current-main update/revalidation.

Parallel candidates after shared predecessors are accepted: T0306 Orders UI with T0401 Bosta read mapping; T0702 required annotation with T0703 booking adapters under frozen engine/ports; T0909 dashboard UI with T0908 ROAS computation. These are possibilities, not simultaneous scheduling instructions. [parallel-safety.json](parallel-safety.json) enumerates exact preconditions/locks. Do not parallelize core migrations/RLS/auth/action/recovery protocol or overlapping route registration.

Agent workflow: inspect claim/baseline → validate gates/dependencies → independently fix expected fixture results → implement one boundary → run relevant checks/inspect actual evidence → independent review → integration owner merges and updates canonical status/digest. Update every surviving parallel branch from main after dependency/shared-contract merge and rerun affected integration/tenant/contract checks before acceptance.

If genuinely blocked, record exact source locator, missing input/decision/environment, affected task IDs, safe completed scope and next responsible role. Keep unrelated eligible work available. No generic retry/relabel closes a safety blocker. Supersede rather than recycle task IDs. Split XL/unbounded discoveries before work.

Completion/resumption uses [execution-state](execution-state.md), which links status authority to the manifest. [single-task](agent-prompts/single-task.md) and [bounded-batch](agent-prompts/bounded-batch.md) are future prompts, not executed now. Local approval never permits provisioning, account messaging, real provider calls, deployment or cutover.
