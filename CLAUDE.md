# Claude Code overlay

This file adds Claude Code working rules. [AGENTS.md](AGENTS.md) is the governing instruction file. Obey it first; nothing here relaxes it.

## Before any edit

Read, in order, and nothing broader unless an actual cited conflict requires it:

1. [docs/implementation/START-HERE.md](docs/implementation/START-HERE.md) and [execution-state.md](docs/implementation/execution-state.md).
2. [task-manifest.yaml](docs/implementation/task-manifest.yaml) and [decision-gates.yaml](docs/implementation/decision-gates.yaml) entries for the selected Task ID.
3. The selected `docs/implementation/tasks/TNNNN.md`.
4. Accepted predecessor contracts (`docs/contracts/C-TNNNN-v1.md`) on current main.
5. Only the exact specification sections the task cites.

## Scope

- Execute only Task IDs the human explicitly assigned in this chat. No assigned ID means no implementation.
- Confirm the task's START gates and dependencies are satisfied in the manifest before starting. Do not start a task whose readiness is not READY.
- Never take a Task ID, editable area or shared-change lock that another agent (Codex or another Claude session) holds. Check the manifest `execution_claim` and existing branches.
- Implement only the task's listed scope and editable areas. Record anything else you notice as a follow-up; do not fix it.

## Branches and baseline

- One branch and one worktree per Task ID (`claude/tNNNN-scope`), started from current accepted `main`.
- After a predecessor or shared-contract change merges, update or rebase onto `main` and rerun the affected tests and contract checks before requesting acceptance.

## Protected shared surfaces

Do not change shared migrations, RLS/auth/grants, shared contracts/DTOs, provider ports, action/recovery protocols, lockfiles, package roots or global config unless the selected task owns that lock and the integration owner has assigned it. Never edit `source/` or closed Phase 1–6 material.

## When blocked

If the task requires an unresolved product, domain, policy or provider decision, stop. Record the exact source locator, the missing decision, affected Task IDs and the safe completed scope. Do not invent an answer or choose a default.

## Report at the end of every task

- Files changed.
- Tests and checks run, each marked PASS, FAIL or NOT_CHECKED, with the exact command and what it proves.
- Blockers and unresolved questions.
- Contracts produced or changed.

Passing tests, a green verifier or task acceptance is never authorization for providers, infrastructure, deployment, shadow, controlled actions or cutover.
