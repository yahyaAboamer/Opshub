# Start here — OpsHub implementation

Phase6 plan revision **P6-r2**, 15 October 2026. **Owner-approved 16 October 2026 (G-P6 SATISFIED): LOCAL implementation is authorized only for explicitly selected Task IDs.** Phases1–6 are approved and closed; the approval is recorded at [phase6-owner-approval.json](../../evidence/implementation/phase6-owner-approval.json). No provider, shadow, external-effect, production or cutover gate is satisfied. Preserve historical labels and source evidence.

Read current repository AGENTS.md, this file, [task-manifest.yaml](task-manifest.yaml), the selected task file and only its exact spec reading set/accepted predecessor contracts. Do not reread all Phase1–6 documents by default. A source conflict requires the broader cited material and a bounded issue record, not invention.

The manifest is the authority for task identity, dependencies, execution status, readiness, gates and coverage. [execution-state](execution-state.md) is a resumption pointer. Task Markdown/roadmap are generated views. [decision-gates](decision-gates.yaml) records exact stage/environment/evidence/decision maker. [task-order](task-order.json) gives one complete valid order; it is not a demand to serialize independent work.

Baseline: [298 protected files](../../evidence/implementation/phase6-input-baseline.json), SHA-256 inventory, **captured before any Git repository existed**; the owner has since committed a baseline to Git (see [execution-state](execution-state.md)). Current plan digest is the manifest's plan_digest, verified over canonical sorted JSON excluding that field. Static check command is `python evidence/implementation/verify_plan.py` from the workspace root. Do not recapture the protected baseline to hide drift.

Current state (the manifest is authoritative): **T0001 ACCEPTED** (2026-10-16); **T0002 ACCEPTED** (2026-10-16); in-progress claims: none; **T0003** is READY and starts only when a human explicitly selects it. T0006 waits on gate A08-NEST (reviewer verdict pending). Then use the manifest's first_runway and accepted-dependency/gate checks. Not all launch policies need answering before local coding.

One Task ID, one claiming owner and isolated branch/worktree; integration owner serializes manifest and lock changes. T0001 creates Git only if still absent. Thereafter accepted integration baseline is main; no commit is invented now. Two agents never share a Task ID or overlapping edit/lock boundary. Update/revalidate parallel branches after relevant merges.

Actual implementation evidence, deployment, provider/account emails, controlled live reads/effects, infrastructure, production shadow/action/contact authority and cutover are distinct scopes. A prompt authorizing local implementation does not grant the latter. Use [single-task](agent-prompts/single-task.md) or [bounded-batch](agent-prompts/bounded-batch.md) only in a later authorized chat.
