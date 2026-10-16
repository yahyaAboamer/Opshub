# OpsHub Workspace

## Durable naming rule

Gentry = legacy evidence; OpsHub = target SaaS.
Preserve Gentry in historical evidence, source names, quotations and legacy behavior; use OpsHub for future-product design.

## Operating status

- Phases 1–6 (reconstruction, domain, product, architecture, migration/validation, implementation planning) are owner-approved and closed. Their historical labels (proposed, pending, draft) remain immutable snapshots.
- Implementation is authorized only through explicitly selected Task IDs under `docs/implementation/`. One Task ID is one bounded implementation scope.
- For every task, follow `docs/implementation/START-HERE.md`, the canonical `task-manifest.yaml`, `decision-gates.yaml`, the selected task specification and its accepted predecessor contracts. The manifest owns task identity, dependencies, status, readiness and gates.
- Do not opportunistically implement neighboring tasks, unrelated fixes or work the selected task does not list.
- Local implementation permission does NOT authorize live provider calls or effects, customer or account communication, infrastructure provisioning, deployment, production shadow, controlled real actions or cutover. Each needs its own explicit gate and human authority.
- An unknown external outcome (timeout, lost response, ambiguous provider result) is never safe to blindly retry. Reconcile first.
- Approved requirements and task contracts outrank optional coding skills, plugins and their preferred conventions.

## Source and closed-material protection

Treat everything under `source/` as original evidence. Do not modify, rename, reorganize, normalize, rewrite or delete files inside `source/`.

Closed Phase 1–6 documents and evidence (`docs/reconstruction/`, `docs/domain/`, `docs/product/`, `docs/architecture/`, `docs/migration/`, `evidence/`) and the files listed in `evidence/implementation/phase6-input-baseline.json` are protected. Change them only through an explicit owner-approved amendment that is recorded, never silently. Do not recapture the protected baseline to hide drift.

## Evidence discipline

Separate conclusions into **verified fact**, **strongly supported inference** and **hypothesis / unresolved question**. Never present an inference as an established business rule. Record the evidence source for important conclusions.

When sources disagree, preserve the disagreement and record it rather than silently choosing one. Do not invent unresolved product or domain policy. Stop and record the exact blocker.

## Live Gentry application safety

Inspection of the live Gentry application, when authorized, is read-mostly. Do not delete or bulk-alter production records, trigger irreversible workflows, send real customer communications, modify production configuration, create financial consequences, bypass authentication/authorization or perform destructive security testing. If understanding something requires a consequential action, document the proposed experiment and leave it for human approval.

## Human review

Report actual results as PASS, FAIL or NOT_CHECKED. Passing local tests or task acceptance is not production, provider, shadow or cutover authorization.
