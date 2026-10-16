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

## Human task briefings

### Task Start Brief

For every explicitly assigned Task ID, after validating its readiness, dependencies and gates but before the first file edit (including the claim record), send the brief as its own visible message, headed **Task Start Brief**, with all five numbered items:

1. **Purpose:** what the task accomplishes, in plain English.
2. **Why now:** why it is dependency-ready, and which accepted predecessor work enables it.
3. **Technical scope:** the main systems, files and contracts expected to be touched.
4. **Expected result:** what should work or exist when the task succeeds.
5. **Reviewable output:** what the human can run, inspect or understand afterward, if applicable.

Keep it concise. Derive it from the task file (Goal, Dependencies and contracts consumed, Scope, Expected code and editable areas, Tests, Acceptance criteria), the manifest and accepted predecessor contracts; don't paste the specification. A one-line summary, a status sentence ("T0002 is ready, I'll now build…") or tool-gate/hook output does not satisfy this; if any of the five items is missing, the brief has not been given. Each item is one or two sentences.

If the human already explicitly assigned a READY Task ID, the brief needs no second confirmation: give it, then begin that task. If the Task ID was not explicitly assigned, is not READY, lacks a required START gate, or conflicts with an active claim or shared lock, don't implement it. Say why instead.

### Implementation handoff (before acceptance)

When the task's work is done and submitted for review, report:

- Files changed.
- Tests and checks run, each marked PASS, FAIL or NOT_CHECKED, with the exact command and what it proves.
- Blockers and unresolved questions.
- Contracts produced or changed.

This handoff keeps every technical evidence requirement of the task and of the completion record. It is not the recap below.

### Accepted Task Recap

Only after the task is actually recorded as ACCEPTED in the manifest, give a concise recap:

1. **Plain English:** what was accomplished and why it matters.
2. **Technical:** the main code, files, APIs, database objects, contracts or infrastructure changed.
3. **Result:** what is now possible that was not possible before.
4. **Validation:** the important checks and tests, each PASS, FAIL or NOT_CHECKED.
5. **Important notes:** significant decisions, limitations, risks or deferred work only.
6. **Next task:**
   - the exact Task IDs now READY according to the canonical manifest;
   - the logical recommended next Task ID;
   - one sentence on what that task will do;
   - one sentence on what the human should be able to run or review afterward.

Don't dump the task specification. The canonical manifest decides what is READY, not task-number order or Claude's judgment. Recommend the next task; never start it.

## Never auto-advance

Claude Code never moves from one Task ID to another on its own. That holds even when several Task IDs have been discussed, proposed or placed in a bounded set. A bounded batch is a scope ceiling, not permission to start successive tasks.

After each task is completed or accepted, stop and wait for an explicit human instruction that selects the next Task ID. No special wording is needed: "Implement T0002" is enough when its readiness and gates permit it.

Passing tests, a green verifier or task acceptance is never authorization for providers, infrastructure, deployment, shadow, controlled actions or cutover.
