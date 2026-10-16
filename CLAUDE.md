# Claude Code overlay

This file adds Claude Code working rules. [AGENTS.md](AGENTS.md) is the governing instruction file. Obey it first; nothing here relaxes it.

## Authority and roles

- The repository's canonical implementation files (AGENTS.md, this file, `docs/implementation/`, accepted contracts on `main`) are sufficient for normal execution. External guidance conversations are advisory only and are never a task dependency or a source of authorization.
- The human owner assigns Task IDs, accepts tasks and approves merges. No permanent separate integration owner or independent reviewer is assumed. Where repository files say "integration owner" or "independent review", see the role rule in [20-agent-execution-protocol.md](docs/implementation/20-agent-execution-protocol.md).
- A separate fresh Claude review session may be used when a task or gate explicitly requires review, or when high-risk work benefits from independent context. It never replaces a gate's named decision maker or the owner's acceptance.

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

## Branches, worktrees and sessions

- One branch and one worktree per Task ID (`claude/tNNNN-scope`), started from current accepted `main`.
- After a predecessor or shared-contract change merges, update or rebase onto `main` and rerun the affected tests and contract checks before requesting acceptance.
- A fresh Claude session per Task ID is preferred, not mandatory. The same session may take another explicitly assigned Task ID only after all of these hold: the previous task is accepted and merged; its branch and worktree are cleaned up; `main` is refreshed; the new task's reading set (above) is reread; and the session's context is still reliable. Otherwise, start a fresh session.
- Continuing in one session never merges Task-ID boundaries: separate branch, worktree, claim, evidence, brief and recap for each ID.

## Protected shared surfaces

Do not change shared migrations, RLS/auth/grants, shared contracts/DTOs, provider ports, action/recovery protocols, lockfiles, package roots or global config unless the selected task owns that lock and the human owner has assigned it. Never edit `source/` or closed Phase 1–6 material.

## When blocked

If the task requires an unresolved product, domain, policy or provider decision, stop. Record the exact source locator, the missing decision, affected Task IDs and the safe completed scope. Do not invent an answer or choose a default.

## Approved skills

Project skills live in `.claude/skills/`. They were installed once with `npx skills@1.7.2 add <source> --skill <name> --agent claude-code --copy`, recorded in `skills-lock.json`, with attributions in `.claude/skills/THIRD_PARTY_NOTICES.md`. They are advisory execution aids only: OpsHub specifications, Task IDs, contracts, gates and acceptance criteria always override them.

| Skill | Source | Select only for |
|---|---|---|
| `frontend-design` | `anthropics/skills` | Visual direction in UI tasks (the T0004 shell, `apps/web/features/`). Accepted T0004 tokens and shell override it. |
| `vercel-react-best-practices` | `vercel-labs/agent-skills` | React render, bundle and async performance in `apps/web`. Ignore its Next.js-only rules (RSC, server actions, `next/dynamic`, `after()`), and never add a dependency it suggests unless the task lists it. |
| `supabase-postgres-best-practices` | `supabase/agent-skills` | PostgreSQL schema, index, locking, pagination and RLS-performance work. OpsHub's tenancy, RLS and Auth0 design override its Supabase `auth.uid()` and role examples. |
| `differential-review` | `trailofbits/skills` | Security review of high-risk diffs (migrations, RLS/auth, provider/action/recovery protocols) or a fresh review session. Write its report to the session scratchpad, or to the task's completion record when that record calls for it; never elsewhere in the repo. |

- Select the smallest relevant set for each task, and name it in the Task Start Brief. No task loads every skill by default.
- Never install, update, remove or substitute a skill during a Task ID. `npx skills update` and any new `npx skills add` need explicit owner approval and their own branch; installed skills are never updated automatically.
- `find-skills` (installed at user level, not a project skill) is discovery-only: it may search and report, never install, update or substitute a skill. Ignore its `npx skills add … -g -y` step.
- Rejected on 2026-10-16: `web-design-guidelines` (fetches unpinned remote instructions on every use) and `spec-to-code-compliance` (needs a plugin-only multi-agent workflow and writes into the repo root).
- A user-level skill or plugin with the same name (for example the `frontend-design:frontend-design` plugin) is not the reviewed project copy; use the project skill.

## Human task briefings

### Task Start Brief

For every explicitly assigned Task ID, after validating its readiness, dependencies and gates but before the first file edit (including the claim record), send the brief as its own visible message, headed **Task Start Brief**, with all seven numbered items:

1. **Purpose:** what the task accomplishes, in plain English.
2. **Why now:** why it is dependency-ready, and which accepted predecessor work enables it.
3. **Layers involved:** only those that apply: Frontend, Backend/API, Database, Background jobs, Auth/security, External providers, Infrastructure/deployment.
4. **Technical scope:** the main systems, files and contracts expected to be touched.
5. **Expected result:** what should work or exist when the task succeeds.
6. **Reviewable output:** what the human can run, inspect or understand afterward, if applicable.
7. **Approved skills selected:** the smallest relevant set of approved skills, each with a short reason it applies, or "No specialized skill selected."

Keep it concise. Derive it from the task file (Goal, Dependencies and contracts consumed, Scope, Expected code and editable areas, Tests, Acceptance criteria), the manifest and accepted predecessor contracts; don't paste the specification. Derive layers and skills from the selected task each time; task files don't list them. A one-line summary, a status sentence ("T0002 is ready, I'll now build…") or tool-gate/hook output does not satisfy this; if any of the seven items is missing, the brief has not been given. Each item is one or two sentences.

Never select or load a skill merely because it is installed. Skills never override approved task or specification behavior, and an unavailable skill is not a blocker.

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
2. **Layers changed:** the layers actually modified (same list as the brief).
3. **Technical:** the main code, files, APIs, database objects, contracts or infrastructure changed.
4. **Result:** what is now possible that was not possible before.
5. **Validation:** the important checks and tests, each PASS, FAIL or NOT_CHECKED.
6. **Important notes:** significant decisions, limitations, risks or deferred work only.
7. **Next task:**
   - the exact Task IDs now READY according to the canonical manifest;
   - the logical recommended next Task ID;
   - one sentence on what that task will do;
   - one sentence on what the human should be able to run or review afterward.

Don't dump the task specification. The canonical manifest decides what is READY, not task-number order or Claude's judgment. Recommend the next task; never start it.

## Never auto-advance

Claude Code never moves from one Task ID to another on its own. That holds even when several Task IDs have been discussed, proposed or placed in a bounded set. A bounded batch is a scope ceiling, not permission to start successive tasks.

After each task is completed or accepted, stop and wait for an explicit human instruction that selects the next Task ID. No special wording is needed: "Implement T0002" is enough when its readiness and gates permit it.

Passing tests, a green verifier or task acceptance is never authorization for providers, infrastructure, deployment, shadow, controlled actions or cutover.
