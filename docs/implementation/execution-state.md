# Execution state and handoff

Plan: **P6-r2**. Manifest [task-manifest.yaml](task-manifest.yaml) is authoritative; this handoff does not maintain a second status list. Current plan digest is in that manifest and [task-order.json](task-order.json); the verifier checks agreement.

Baseline: evidence/implementation/phase6-input-baseline.json; 298 protected inputs, no Git repository, no commit. Owner scope: Phases1–5 approved/closed; Phase6 planning only. Do not execute generated prompts during Phase6.

Accepted tasks: none. In-progress claims: none. Actual completion evidence: none. All unexecuted tasks NOT_STARTED; G-P6 makes current readiness WAITING_AUTHORIZATION. Later independent/release gates remain unresolved at their scoped boundaries.

Exact next candidate after explicit local implementation approval: **T0001**. Next conservative runway: T0002, T0003, T0004, T0005, T0006, T0007, T0008, T0009, T0101, T0102. Each waits its exact accepted contracts; no task starts based only on this list.

Resume:
1. Inspect current AGENTS.md, START-HERE and canonical manifest; run the planning verifier and inspect existing user work.
2. Confirm current direct/recorded authorization. An explicit later human request to implement a selected local task is valid evidence; record its scope rather than demanding a special phrase.
3. Integration owner claims the selected eligible ID/locks on current main (or establishes Git in T0001), assigns Codex or Claude Code, records branch/worktree/base revision and marks IN_PROGRESS.
4. Agent reads selected task/specs/produced predecessor boundaries, implements only that scope and submits actual evidence.
5. Independent review/integration owner accepts or records exact blocker, merges in dependency order, updates canonical status/readiness/digest and refreshes derived views. Keep unrelated work intact.
6. Record the exact next eligible IDs and evidence links here at each real handoff. Do not mark operational tasks accepted based on local coding.

Planning evidence: [baseline](../../evidence/implementation/phase6-input-baseline.json), [independent source inventory](../../evidence/implementation/source-inventory.json), [verification](../../evidence/implementation/verification.json), [review and walkthrough](../../evidence/implementation/quality-review.md), [input issues](../../evidence/implementation/input-issues.md). The proposed AGENTS phase-status amendment is separate and unadopted.
