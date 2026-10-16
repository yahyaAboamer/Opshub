# Gentry Reconstruction Workspace

## Durable naming rule

Gentry = legacy evidence; OpsHub = target SaaS.
Preserve Gentry in historical evidence, source names, quotations and legacy behavior; use OpsHub for future-product design.

## Mission

This repository is currently in the **system reconstruction phase**.

The purpose of this phase is to accurately understand the existing Gentry operations system from:

- source artifacts in `source/`
- the authorized live Gentry application
- observed application behavior
- available datasets, spreadsheets, documents, specifications, scripts, and SOPs

Do not build the replacement SaaS yet.

Do not prematurely choose its technology stack, architecture, database, UI system, or implementation framework.

First reconstruct what exists.

---

## Source Protection

Treat everything under `source/` as original evidence.

Do not modify, rename, reorganize, normalize, rewrite, or delete files inside `source/`.

Generated work belongs under:

- `docs/reconstruction/`
- `evidence/`

If temporary analysis scripts are required, place them outside `source/`.

---

## Evidence Discipline

Separate conclusions into:

- **Verified fact**
- **Strongly supported inference**
- **Hypothesis / unresolved question**

Never present an inference as an established business rule.

For important conclusions, record their evidence source where practical:

- live application
- route/page
- workbook
- sheet
- formula
- document
- SOP
- specification
- script
- dataset
- observed API/network behavior
- inference

When two sources disagree, preserve the disagreement instead of silently choosing one.

Prefer current verified live behavior for describing what the current application does.

Prefer authoritative specification artifacts when determining intended behavior.

Record discrepancies explicitly.

---

## Reconstruction Before Design

During this phase, do not redesign Gentry.

Do not improve workflows merely because another design appears cleaner.

Do not substitute industry best practices for observed Gentry behavior.

Do not allow UI/design skills or architectural preferences to influence the description of the existing system.

We need to understand the existing system before deciding what should replace it.

---

## Live Application Safety

The owner has authorized inspection of the Gentry application.

Treat the production application as read-mostly.

You may:

- navigate
- search
- filter
- inspect records
- inspect UI state
- inspect browser/network behavior when authorized
- observe validation behavior where safe
- document workflows

Do not intentionally:

- delete production records
- alter large numbers of records
- trigger irreversible workflows
- send real customer communications
- modify production configuration
- create financial consequences
- bypass authentication or authorization
- perform destructive security testing

If understanding a workflow requires an irreversible or materially consequential action, document the proposed experiment and leave it unresolved for human approval.

---

## Investigation Style

Investigate systematically.

Do not rely only on screenshots or visible labels.

Trace important workflows across:

UI → state transition → business rule → data → calculation → downstream consequence.

Pay particular attention to:

- domain entities
- identifiers
- relationships
- statuses
- state transitions
- operational queues
- calculations
- derived metrics
- business rules
- exception handling
- validation
- data-quality rules
- imports
- exports
- scheduled/background operations
- integrations
- user roles
- permissions
- auditability
- merchant-specific behavior

---

## Skills

Skills are supporting procedures, not sources of truth.

When a trusted reverse-engineering skill is available, it may be used during investigation.

Do not allow a skill's preferred architecture, design system, coding conventions, or assumptions to override evidence from Gentry.

Do not invoke UI/design-oriented skills during reconstruction.

An LLM-council/reviewer skill may be used later to challenge the completed reconstruction, not to invent facts about the system.

---

## Deliverables

Maintain reconstruction documents under:

`docs/reconstruction/`

Prefer updating the existing reconstruction documents as understanding improves rather than producing many duplicate versions.

Maintain unresolved contradictions and questions explicitly.

The reconstruction must become understandable by a senior engineer who has never seen Gentry.

---

## Human Review Gates

Do not begin:

- replacement PRD
- target SaaS architecture
- technology selection
- database implementation
- frontend implementation
- backend implementation
- migration implementation

until the reconstruction phase has been reviewed and approved by the human owner.

When reconstruction reaches a stable point, stop and present:

1. what has been verified
2. important contradictions
3. open questions
4. areas still requiring live-system inspection
5. confidence assessment
6. recommended next review step