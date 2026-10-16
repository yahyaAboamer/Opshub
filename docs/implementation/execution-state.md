# Execution state and handoff

Plan: **P6-r2**. Manifest [task-manifest.yaml](task-manifest.yaml) is authoritative; this handoff does not maintain a second status list. Current plan digest is in that manifest and [task-order.json](task-order.json); the verifier checks agreement.

Baseline: evidence/implementation/phase6-input-baseline.json; 298 protected inputs, captured before any Git repository existed. Owner scope: Phases1–6 approved/closed; G-P6 SATISFIED 2026-10-16 for LOCAL implementation of explicitly selected Task IDs only ([approval record](../../evidence/implementation/phase6-owner-approval.json)). No other gate is satisfied.

Accepted tasks: none. T0001 is IN_REVIEW on `claude/t0001-workspace-boundary` ([claim](claims/T0001.md), [completion evidence](completion/T0001.md)); acceptance is the owner's decision. All other tasks NOT_STARTED. Readiness: T0001 READY; every other task WAITING_DEPENDENCIES. Later independent/release gates remain unresolved at their scoped boundaries.

Observed at approval (2026-10-16), for T0001 to inspect: a Git repository now exists. Commit a18ce19 on `main` was made by the owner and is mirrored at `origin`. On 2026-10-16 the owner had `source/` removed from Git and its entire history (rewritten `main` 42bedba; `/source/` is now ignored). The originals stay only on disk in the primary workspace, so a fresh clone fails the verifier's PROTECTED_INPUT check for those 38 files by design; verify against the primary workspace. GitHub's read-only `refs/pull/1/head` still pins the pre-rewrite commits until GitHub Support purges it. With `core.autocrlf=true`, Git stored 119 originally CRLF or mixed-EOL protected files as LF, so a Git checkout does not reproduce the baseline bytes. The on-disk originals in the primary workspace still match all 298 baseline digests. T0001 owns the resolution (trackable allowlist, private custody, line-ending policy). This handoff did not change it.

Exact next eligible tasks after T0001 is ACCEPTED: **T0002** and **T0003** (each requires explicit human selection). Next conservative runway: T0002, T0003, T0004, T0005, T0006, T0007, T0008, T0009, T0101, T0102. Each waits its exact accepted contracts; no task starts based only on this list.

Resume:
1. Inspect current AGENTS.md, START-HERE and canonical manifest; run the planning verifier and inspect existing user work.
2. Confirm current direct/recorded authorization. An explicit later human request to implement a selected local task is valid evidence; record its scope rather than demanding a special phrase.
3. Integration owner claims the selected eligible ID/locks on current main (or establishes Git in T0001), assigns Codex or Claude Code, records branch/worktree/base revision and marks IN_PROGRESS.
4. Agent reads selected task/specs/produced predecessor boundaries, implements only that scope and submits actual evidence.
5. Independent review/integration owner accepts or records exact blocker, merges in dependency order, updates canonical status/readiness/digest and refreshes derived views. Keep unrelated work intact.
6. Record the exact next eligible IDs and evidence links here at each real handoff. Do not mark operational tasks accepted based on local coding.

Planning evidence: [baseline](../../evidence/implementation/phase6-input-baseline.json), [independent source inventory](../../evidence/implementation/source-inventory.json), [verification](../../evidence/implementation/verification.json), [review and walkthrough](../../evidence/implementation/quality-review.md), [input issues](../../evidence/implementation/input-issues.md). The AGENTS phase-status amendment proposed in evidence/implementation/proposed-agents-update.md was adopted on 2026-10-16 as a recorded protected amendment; root CLAUDE.md adds the Claude Code overlay.
