Phases 1–5 are approved and closed. This instruction authorizes Phase 6 planning only.

The earlier phase-status and stop-before-next-phase wording in historical documents and AGENTS.md does not require repeating approved phases. All source-protection, evidence, scope and production-safety rules remain in force. Approval of a phase does not automatically resolve its OP/A/MD decisions or prove provider capabilities.

Gentry = legacy evidence; OpsHub = target SaaS.

We are now beginning:

# Phase 6 — OpsHub Implementation Plan

This is the final planning phase before application implementation begins.

Do NOT build OpsHub in this phase.

Do NOT install application dependencies, scaffold the production application, create migrations, call live providers, deploy infrastructure, or modify production systems.

Your job is to transform the approved product, architecture and validation contracts into an **implementation-ready engineering roadmap suitable for AI coding agents working in bounded sessions**.

Use as authoritative inputs:

- `docs/reconstruction/`
- `docs/domain/`
- `docs/product/`
- `docs/architecture/`
- `docs/migration/`
- approved owner decisions
- existing ADRs and evidence

Priority when documents conflict:

1. approved owner decisions
2. approved Product PRD
3. approved canonical domain model
4. approved architecture
5. approved migration/validation contracts
6. reconstructed Gentry behavior/evidence

Never silently resolve a contradiction.

---

# Preflight, Baseline and Planning Boundaries

Before drafting:

1. Read applicable AGENTS.md instructions and inventory current files. Inspect any existing docs/implementation/ package before creating a competing plan. Preserve unrelated changes. If Phase 6 already exists, assess and improve it rather than duplicating it.
2. Read the current Phase 3 PRD, owner decisions, priority/acceptance/decision registers; Phase 4 architecture, ADRs and review; Phase 5 validation handoff, decision register, review amendments and linked synthetic evidence. Use reconstruction/domain references for the meanings they establish.
3. Record the exact baseline in evidence/implementation/phase6-input-baseline.json: source paths, content digests, available revision information and owner approval scope. Do not assume Git exists or invent a commit. Historical "proposed" labels do not negate this owner's phase approval, but unresolved decisions remain unresolved.
4. Record missing inputs, factual contradictions and materially ambiguous requirements with exact source locators. Continue independent planning; mark only affected tasks blocked. Do not demand all launch decisions before planning or local coding.
5. Identify outdated repository instructions. Draft a narrow phase-status amendment in evidence/implementation/proposed-agents-update.md for the later handoff. Do not silently rewrite active instructions or closed documents.

Allowed outputs in this phase: planning documents under docs/implementation/, and baseline/review/static-verification artifacts under evidence/implementation/. You may create and run small local documentation-verification scripts using available tooling. These are not application code, provider experiments or executable migration tooling.

Protect source/, Phases 1–5 documents and existing evidence from modification. Verify their content digests remain unchanged. Do not copy customer-level source data into task specifications, review prompts or public artifacts.

Public official documentation may be consulted for a specific compatibility uncertainty; record date and scope. It cannot qualify the actual pilot account. Do not install dependencies or perform compatibility prototypes in this planning phase; schedule those as future engineering tasks.

## Authority and conflicts

The priority list above governs approved intent, but is not permission to discard a lower-level validation or safety obligation. Compatible contracts are cumulative. Preserve Phase 5 amendments and safeguards.

For a genuine conflict, record the sources, affected task IDs, consequence and bounded proposed resolution. Do not silently invent business policy or weaken zero-tolerance gates. Owner decisions require the owner; engineering compatibility questions require evidence.

# Primary Goal

Create a plan where an AI coding agent can take **one task at a time**, understand:

- why the task exists
- prerequisites
- exact bounded scope
- expected behavior
- architectural constraints
- files/modules likely involved
- tests required
- acceptance criteria
- decisions that must already be resolved
- things explicitly not to do

and complete it without needing to redesign OpsHub.

The implementation process must be incremental and continuously testable.

Design the plan for two independent coding agents, Codex and Claude Code. Every task must define branch isolation, editable areas, shared-change locks, parallel-safety classification, predecessor contracts, and required merge order. Two agents must never concurrently own the same Task ID or overlapping shared-write boundary. main is the accepted integration baseline; after any dependent merge, parallel branches must update from current main and revalidate before acceptance.

Do NOT create giant tasks such as:

> Build the Orders module.

Break work into coherent, verifiable units.

---

# Implementation Philosophy

Optimize for:

1. vertical working slices
2. correctness before breadth
3. deterministic tests
4. tenant isolation from the beginning
5. source provenance from the beginning
6. auditability from the beginning
7. external-action safety before provider mutations
8. read paths before write paths
9. provider qualification before relying on provider effects
10. simple operations
11. reversible implementation steps
12. AI-agent comprehensibility

Avoid:

- “build frontend first, then backend”
- “build all database tables first”
- giant cross-system rewrites
- speculative abstractions
- premature microservices
- implementing every future feature because an entity exists

A milestone should preferably result in a usable/testable vertical capability.

Build the pilots as production tenants on a $0 pilot offering. Do not implement the pilots as a temporary single-tenant/demo architecture. Billing/payment processing is explicitly deferred until commercialization, but commercial-state primitives must exist from the beginning.

---

# Approved Architecture Baseline

Plan implementation against the approved Phase 4 architecture unless a verified incompatibility is discovered.

Current baseline includes:

- React, TypeScript and Vite
- NestJS on the Phase 4 Node baseline, standard Express adapter
- PostgreSQL 17
- Kysely + pg, with reviewed explicit SQL migrations
- Auth0 OIDC with OpsHub-owned server sessions and authorization
- pg-boss with qualified same-transaction enqueue semantics
- private Amazon S3, including independently retained protected recovery records
- paid Render web/API, worker and PostgreSQL deployment
- structured redacted logs, Sentry and selected OpenTelemetry correlation
- Resend for invitations/account support only, not customer outreach
- Vitest, real PostgreSQL/Testcontainers, a mock provider server and Playwright
- modular monolith
- separate web/API and worker processes from one codebase
- PostgreSQL-backed MVP analytics projections
- shared-schema multi-tenancy with tenant keys + forced RLS
- no Redis for MVP
- no warehouse for MVP
- no microservices for MVP

The complete authority is docs/architecture/15-technology-selection.md and the approved ADRs, not this abbreviated list. Do not silently generalize Amazon S3 to any "S3-compatible" store, change session ownership, omit account invitations, or weaken transaction/recovery requirements.

Do not casually reopen technology selection. Exact supported patches and tool compatibility must be verified and pinned in later authorized engineering work. A08/MD16 qualification tasks must precede the first implementation that relies on the affected behavior, not merely appear as a final release check.

If implementation research proves a material incompatibility, document it as:

`ARCHITECTURE DEVIATION PROPOSAL`

with evidence before changing the plan.

---

# First Deliverable — Implementation Dependency Graph

Construct the dependency graph before detailed tasks.

Identify foundational capabilities such as:

- repository/toolchain
- environment configuration
- CI
- database access
- migration tooling
- Merchant identity
- User identity
- Membership
- Platform assignment
- RLS
- authorization
- audit primitives
- source observations
- external identity mapping
- job infrastructure
- provider connection primitives
- action/effect primitives
- test fixture infrastructure

Then identify which product capabilities depend on them.

Use this graph to determine implementation order.

Do not implement an arbitrary module ordering based on document order.

---

# Sequencing Rules and Milestone Outcomes

Milestone numbers are a proposed organization, not automatic dependency order. Distinguish:

- implementation with synthetic inputs and fake adapters;
- qualified integration in controlled nonproduction environments;
- separately authorized real read-only shadow;
- individually authorized action/contact enablement;
- cutover.

A locally testable vertical slice must not require a live provider account. A fake-backed demo is not qualified integrated MVP completion.

Schedule bounded compatibility tasks for Nest/test tooling, real PostgreSQL and migration tooling, pg-boss transactional enqueue/rollback and least-privilege grants, provider SDK retry controls, and independent S3 recovery-record semantics before dependent capabilities rely on them.

Introduce verified initial-Admin onboarding, minimal platform provisioning, source ownership, service/capability checks and invitation prerequisites early enough for M1–M3. M10 completes the control plane/commercial shell; it must not conceal foundational prerequisites.

Introduce fixture realization, immutable intake/run identity, replay/dispositions and migration-safety requirements with the first capabilities that need them. M11 completes migration tooling and rehearsals; it is not the first time these contracts receive implementation tasks.

A contact workflow can authorize a real-world effect even when the telephone call happens outside OpsHub. Before any real contact start, require applicable contact reservation/budget, concurrency, independent recovery-marker, inherited-history and single-authority proofs. M5 cannot bypass safety simply because the generic provider action engine is scheduled at M6. Local synthetic contact work may precede real enablement.

For each milestone specify:
- the actor and end-to-end workflow that becomes demonstrable;
- entry prerequisites, exact included task IDs and exit evidence;
- local synthetic demonstration steps and expected visible results;
- remaining policy/provider/release limitations;
- whether it yields local functionality, qualified integration, or readiness for a separate operational approval.

Include user-facing list/detail/workflow behavior, loading/empty/error/stale/permission states, navigation and relevant accessibility checks in capability tasks. API success alone is not evidence of a usable merchant journey. Do not introduce a new product redesign.

# Recommended Milestone Shape

Evaluate and refine the following sequence rather than accepting it blindly.

## M0 — Engineering Foundation

Potential scope:

- monorepo/repository structure
- TypeScript configuration
- application packages/process boundaries
- linting/formatting
- test infrastructure
- environment configuration
- CI
- local development
- database development setup
- migration framework
- basic health/readiness
- logging foundation

No real business capability yet.

---

## M1 — Tenant, Identity and Authorization Foundation

Potential first vertical capability:

A signed-in user can enter the correct OpsHub merchant context and cannot access another merchant.

Include:

- Merchant/Workspace
- User
- Membership
- Merchant Admin
- Merchant Operator
- Platform Operator Assignment
- Auth0 integration
- server-side authorization
- tenant context
- PostgreSQL RLS
- tenant-safe repository/query patterns
- invitations and verified initial-Admin provisioning; if delivery comes later, name the prerequisite tasks and keep real onboarding gated
- audit identity
- tenant-isolation tests

Do not postpone tenant isolation until later.

---

## M2 — Canonical Evidence / Provenance Foundation

Implement the primitives required to explain:

> Why does OpsHub believe this?

Potential scope:

- Source Context
- external/native identity
- source observation
- interpretation
- manual correction
- provenance
- freshness/completeness
- import/run identity
- disposition
- immutable evidence references
- basic audit events

Begin realizing the Phase 5 logical golden contracts as independently reviewed executable fixtures immediately. The existing golden-contracts.json is an expected-value index; golden-logical-fixtures.json is a logical input supplement. Neither proves the complete provider-shaped fixture suite already exists.

---

## M3 — Read-Only Commerce Vertical Slice

Target:

A pilot merchant can connect/import qualified Shopify evidence and see trustworthy Orders/Items/Products in OpsHub without external mutations.

Potential scope:

- provider connection abstraction
- Shopify read authentication
- order ingestion
- product/variant ingestion
- initial sync
- incremental sync/webhooks where qualified
- identity mapping
- data-quality states
- order list/detail
- basic source provenance UI
- import/manual fallback

Provider contract qualification is a gate.

---

## M4 — Read-Only Courier Vertical Slice

Target:

OpsHub connects commerce Orders to Bosta shipment evidence and exposes operational delivery truth.

Potential scope:

- Bosta connection/read path
- shipment identity
- tracking
- status observations
- delivery attempts
- delivery/RTO outcome
- source conflicts
- freshness
- shipment detail
- preliminary delivery KPI projections
- duplicate callback/read handling

Still no consequential external actions.

---

## M5 — Operational Work / Contact Vertical Slice

Target:

Merchant teams can work the daily confirmation/calling queue safely.

Potential scope:

- confirmation entry/evidence
- contact cases
- contact events
- maximum-three-attempt policy
- due/overdue contact
- unreached/attempts exhausted
- action-required cases
- case-level resolved semantics
- attention queue
- Operator/Admin permissions
- audit
- call KPI projections

Use deterministic clock fixtures from Phase 5.

---

## M6 — External Action Safety Engine

Implement the safety mechanism before integrating consequential mutations.

Potential scope:

- action intent
- approval
- immutable request identity
- authorization snapshot/current authorization check
- execution reservation
- concurrency control
- idempotency
- execution states
- known failure
- unknown outcome
- reconciliation required
- provider result evidence
- manual handover
- recovery journal
- audit

Prove:

- double click
- two Admin race
- worker duplication
- crash before request
- crash after request
- timeout after possible provider effect
- stale worker
- revoked authority

No provider action should be enabled until these generic safety contracts pass.

---

## M7 — First Integrated Consequential Action

Choose the lowest-risk/high-value qualified action based on provider evidence.

Do not preselect Bosta booking. Evaluate the Phase 5 candidate ordering, including supported annotation, booking, replacement and eligible cancellation, against actual qualification and user value. Even an annotation can trigger downstream automation; include its side effects. Record why the selected first action has a bounded effect and qualified recovery path.

Implement only one action class first.

Requirements:

- qualification contract passed
- Admin authority
- action engine integration
- provider identity/correlation
- ambiguous result recovery
- duplicate suppression
- reconciliation
- manual fallback
- audit
- capability flag
- emergency disable

Then expand action classes individually. Name explicit later tasks for every approved MVP action/result contract, including supported cancellation, replacement and any required annotation. "Expand later" is not sufficient coverage of OD08 or the PRD's integrated MVP.

---

## M8 — Returns, Pickups and Replacement Workflow

Potential scope:

- Return Case
- Pickup Case
- independent payment/physical collection
- pickup evidence
- replacement request
- linked new replacement Order
- approval
- applicable integrated actions
- original/replacement relationship
- operational queues
- audit

Preserve OD06 cardinality.

---

## M9 — Product Performance + Meta + ROAS

Target:

Merchant can evaluate product/SKU operational and advertising performance.

Potential scope:

- product/SKU performance projections
- revenue contributors
- delivery/RTO/return behavior
- Meta connection
- spend observations
- spend allocation
- unallocated spend
- missing spend
- revisions
- ROAS
- period comparisons
- contributor drill-down
- data completeness/coverage

Do not invent attribution when evidence is missing.

MD06/MD07 decisions gate the final production definitions.

---

## M10 — OpsHub Platform Control Plane + Commercial Shell

Potential scope:

- merchant administration
- membership administration
- integration/readiness health
- safe platform diagnostics
- activation/suspension
- basic subscription/commercial status
- entitlement shell if required

Do not give Platform Admin merchant business authority.

Avoid customer-level PII in platform monitoring by default.

---

## M11 — Migration Tooling and Regression Harness

Implement Phase 5 contracts:

- immutable intake
- Migration Run
- parsing
- normalization
- identity resolution
- dispositions
- inactive candidate generation
- reconciliation
- legacy oracle comparison
- contributor comparison
- golden fixtures
- re-import/idempotency
- privacy suppression
- migration report

This may begin earlier where infrastructure is needed, but production migration activation remains later.

---

## M12 — Shadow Mode and Pilot Readiness

Prepare:

- real read-only pilot synchronization
- mutation/contact egress disabled
- queue comparison
- KPI comparison
- source coverage/freshness
- discrepancy reporting
- operational metrics
- provider qualification evidence
- recovery drill readiness
- tenant/security gates

No cutover merely because the application “looks correct.”

---

## M13 — Controlled Actions and Cutover Readiness

Gradually qualify and enable approved action classes.

Prepare Phase 5 cutover contracts:

- single mutation authority
- conflict-group holds
- incumbent drain
- final synchronization
- queue reconciliation
- action authority transfer
- rollback/disable
- recovery validation
- sign-off report

Do not perform production cutover in Phase 6 planning.

---

# Task Granularity

Convert milestones into bounded coding tasks.

Each task should normally be completable by one AI coding agent in one focused implementation session without needing broad redesign.

Prefer tasks like:

> Implement merchant-scoped Order list query with RLS integration tests.

rather than:

> Build Orders.

Prefer:

> Add ActionIntent persistence and duplicate-request uniqueness contract.

rather than:

> Implement external actions.

Do not create thousands of microscopic tasks either.

Use engineering judgment.

---

# Task Contract

Every implementation task must contain the fields below. Tasks must have stable IDs that are never silently recycled.

Separate execution status from readiness:
- execution status: NOT_STARTED, IN_PROGRESS, IN_REVIEW, ACCEPTED, BLOCKED, SUPERSEDED;
- readiness: READY, WAITING_DEPENDENCIES, WAITING_DECISION, WAITING_ENVIRONMENT, WAITING_AUTHORIZATION.

Initialize all unexecuted tasks as NOT_STARTED, with a derived readiness and explicit blockers. A future unresolved release gate does not block local implementation unless the task actually depends on it.

Distinguish ENGINEERING, QUALIFICATION, VALIDATION, DOCUMENTATION, OWNER_DECISION and OPERATIONAL_RELEASE work. Do not assign an owner approval or real cutover to a coding agent as if it were ordinary implementation. Give each task an accountable role and permitted environment/effects.

## Identity

- Task ID
- Milestone
- Title
- Execution status: NOT_STARTED; readiness and blockers separately
- Type
- Risk level

## Goal

One concise outcome.

## Why

PRD/domain/architecture requirement being satisfied.

## Dependencies

Exact predecessor Task IDs and decision gates, with the artifact/interface/evidence consumed from each predecessor. Avoid vague "foundation complete" dependencies.

## Definition of Ready

Minimum specs, accepted interfaces, fixture inputs, resolved start gates and environment prerequisites required to begin. Identify the smallest reading set; do not require every agent to reread the entire project.

## Contracts Produced and Consumed

Name the application/provider/data boundaries, relevant behavior and versioned outputs used by downstream tasks. Specify semantics from approved architecture without inventing final filenames or prebuilding the schema/API. Interface-definition work must precede consumers where contracts are not yet concrete.

## Scope

What to build.

## Explicit Non-Scope

What must not be built during this task.

## Relevant Specifications

Links to exact approved documents/sections.

## Expected Code Areas

Expected modules/packages/files or architectural boundaries.

Do not prescribe exact filenames when they cannot reasonably be known yet.

## Data Changes

Tables/entities/indexes/migrations expected.

## Security / Tenancy Requirements

Where applicable.

## Failure / Edge Cases

Important negative behavior.

## Tests Required

Specific test categories and important scenarios.

## Acceptance Criteria

Objective pass/fail criteria.

## Completion Evidence

Commands/test output/artifacts that the implementation agent must provide. State the environment and what each check proves. Mark proposed commands as PLANNED until the repository defines them; do not fabricate existing scripts or results.

For UI tasks, include the demonstrated user journey and visual/E2E evidence as appropriate. For safety tasks, include deterministic fault barriers and observed request/effect counts.

## Change and Recovery Boundary

Expected editable areas, shared-file/migration ownership, local rollback or forward-repair approach, and explicit stop/escalation conditions. Application rollback must never be described as undoing an external business effect.

## Decision Gates

Any OP/A/MD/provider qualification decision required before starting or completing the task.

## Parallelism

- SAFE TO PARALLELIZE
- PARALLEL WITH RESTRICTIONS
- SERIAL

and why.

---

# Machine-Readable Task Manifest

In addition to human-readable documents, create:

`docs/implementation/task-manifest.yaml`

Each task must include at least:

- id
- milestone
- title
- status
- type
- risk
- dependencies
- decision_gates
- spec_refs
- test_requirements
- acceptance_summary
- parallelism

Also include:
- schema_version and plan/input-baseline digest at manifest level;
- task_spec path;
- requirement_ids and validation_contract_ids;
- complexity;
- accountable_role;
- readiness and blockers;
- permitted_environment and effect_class;
- produced_contracts and consumed_contracts;
- editable_areas/shared_change_locks;
- completion_evidence_refs (empty until actually executed).

Use structured gate references: gate ID, blocking stage (START, COMPLETION, SHADOW, ACTION_ENABLEMENT or CUTOVER), and the applicable capability/environment. Define gate acceptance evidence and responsible decision maker in a canonical decision-gate register. Unresolved gates must not be represented as false task dependencies or ambiguous prose strings.

Define a small explicit manifest schema and validate against it with available tooling. Do not build an orchestration service.

The YAML is the canonical task index, dependency/status/coverage metadata and links. Individual Markdown task files hold the detailed contract. Roadmaps and chapter summaries are derived views; do not maintain three independent task/status lists. Check every intentionally duplicated value for agreement.

task-manifest.yaml is authoritative for task identity, dependency, status, readiness, gates and coverage metadata. If a roadmap/chapter summary conflicts with the manifest, treat the manifest as authoritative and repair the derived document.

The YAML is for future AI orchestration.

It must agree with the Markdown roadmap.

Do not put secrets or environment values in it.

---

# Decision Gate Mapping

Map all unresolved:

- Product OP decisions
- Architecture A decisions
- Migration MD decisions

to the exact implementation milestone/task where they become blocking.

Classify each:

### MUST DECIDE BEFORE TASK START

Implementation meaning cannot be known without it.

### MUST DECIDE BEFORE TASK COMPLETION

Scaffolding can start, production semantics cannot finish.

### MUST DECIDE BEFORE PILOT

Does not block code construction.

### MUST DECIDE BEFORE ACTION ENABLEMENT

Read-only implementation can proceed.

### MUST DECIDE BEFORE CUTOVER

Only operational launch is blocked.

This prevents us from unnecessarily answering all open questions before coding.

Map inherited domain PD questions to their superseding OD/OP/A/MD decisions where applicable; do not reopen settled decisions or lose an unresolved one. Separate owner-policy decisions, technical proofs, provider-account qualification and operational authorizations.

Use Phase 5's existing shadow/action/cutover gate requirements as the baseline. Do not move a gate later merely to make an earlier milestone appear ready. A test-only policy permits deterministic synthetic tests; it does not approve that policy for production. Gate satisfaction must reference actual evidence/approval and scope.

---

# Provider Qualification Spikes

Provider unknowns should become explicit bounded qualification tasks.

A qualification task is NOT:

> explore Shopify.

It should be:

- exact capability/question
- exact account/environment required
- safe test method
- expected evidence
- prohibited effects
- decision produced
- implementation tasks that depend on it

Plan qualification work for Shopify, Bosta and Meta.

Do not call live providers during Phase 6.

---

# Database Implementation Order

Plan database work incrementally.

Avoid one giant migration containing the entire future schema.

Foundational migrations should establish:

- tenant anchors
- identity
- RLS mechanism
- audit/provenance primitives

Domain tables should arrive with the capability that actually uses them.

Every merchant-scoped table must explicitly address:

- merchant ownership
- RLS
- FK/tenant consistency
- uniqueness
- source identity where applicable
- audit/provenance requirements

Plan database invariant tests alongside each migration.

---

# Testing Must Be Implementation Work, Not a Final Phase

Every task should ship its tests.

Do not schedule:

> Build app
> Then write tests.

The roadmap must continuously introduce:

- unit tests
- database/invariant tests
- RLS tests
- authorization tests
- provider contract tests
- integration tests
- golden fixture tests
- concurrency tests
- E2E tests

Add broader suites only when the underlying capability exists.

---

# Golden Dataset Integration

The Phase 5 golden datasets must become executable tests throughout implementation.

Inventory the current complete scenario catalogs, including council amendments, rather than assuming earlier counts are exhaustive. Map every GD/KR scenario to the fixture-realization task, the first task/milestone where it becomes executable, the expected assertion, and the release gate it supports.

Plan separately reviewed raw synthetic input realizations, deterministic IDs/clocks and expected contributor/disposition/hold sets. Cover test-policy versus production-policy separation and tests showing intentionally wrong identity, parser, clock, member-set or quality-state implementations fail. Golden expected values must not be edited merely to match current output.

Map the other applicable Phase 5 contract families too: MI/IM/CL, MP/MRUN, OR, PC, EA, TI/AU, RV, SH/CT/RE/PV, including embedded and subsequently added contract IDs. A prose mention of "recovery" or "golden tests" is not a traceable implementation assignment.

A milestone cannot claim semantic completion when its relevant golden contracts remain unimplemented.

Do not create expected results using the same production logic being tested.

---

# External Mutation Rule

Carry forward as a non-negotiable engineering invariant:

> UNKNOWN EXTERNAL OUTCOME ≠ SAFE TO RETRY

No implementation task may introduce generic mutation retry behavior that violates this.

Retries are allowed only when the action protocol can establish that no external effect occurred or when provider-supported idempotency/reconciliation makes the operation safe under the approved contract.

Generic HTTP retry middleware must not blindly wrap consequential provider mutations.

---

# Repository Structure

Propose the concrete repository structure for implementation.

Keep it understandable by humans and AI agents.

Show likely boundaries for:

- web
- API
- worker
- domain/application modules
- database
- integrations
- shared contracts
- tests
- fixtures
- scripts/tooling

Do not over-fragment into dozens of packages without reason.

---

# Branch / Change Protocol for AI Agents

Define a recommended implementation workflow.

Prefer:

1. select one Task ID
2. read referenced specs
3. inspect existing implementation
4. produce short execution plan
5. implement only task scope
6. run required tests
7. run broader regression appropriate to change
8. summarize changed files
9. report test evidence
10. update task status only after acceptance

Agents should not opportunistically implement adjacent backlog items.

Define acceptance authority by task risk: ordinary verified changes may use the agreed review workflow; security, authorization, external effects, recovery and operational release require their named stronger review/gates. An implementing agent reports IN_REVIEW until the defined acceptance process completes. Tests passing never imply production authorization.

A failed test, interrupted session or missing environment must be reported as such. Record what was attempted, changed, verified, not verified and what remains. Never mark a task accepted based on files existing or an agent's narrative.

Use one writer per shared working directory; concurrent writers require isolated worktrees/checkouts and stable interfaces. Serialize shared migrations, lockfiles and global contracts through a named integration owner. Plan parallelism only after accounting for shared writable areas and integration/regression work.

## Fresh-Chat Execution and Resumption

Create docs/implementation/START-HERE.md plus an execution-state/handoff file. It must identify plan revision, current baseline, accepted/in-progress tasks, blockers, evidence links, exact next eligible Task IDs and how to resume. The manifest remains authoritative for status; the handoff links to it.

Produce two copy-paste agent prompts:
1. a single-task implementation prompt accepting one Task ID;
2. a bounded-batch prompt accepting an explicit set of Task IDs, stopping when those tasks are accepted or genuinely blocked.

Both prompts must require the new agent to read current repository instructions, START-HERE, the manifest, the selected task and its exact specs; inspect existing work before editing; honor environment/permission boundaries; validate dependencies; preserve unrelated changes; and record actual completion evidence. They must distinguish approval to implement locally from permission to provision, send messages, call real providers, deploy or cut over.

The generated implementation prompts must never instruct a new agent to read all Phase 1–6 documentation by default. Each task must specify the smallest sufficient reading set. Broader documents are consulted only when the selected task requires them.

Do not start either execution prompt in Phase 6. Do not assume a new chat inherits this conversation or hidden memory.

If a task exposes a spec contradiction, stop and record it rather than inventing a product decision.

---

# Code Review Expectations

Define review requirements for:

- ordinary changes
- security/tenancy changes
- schema migrations
- external provider mutations
- authorization
- recovery logic
- analytics definitions

High-risk changes require stronger review/test evidence.

LLM Council may review plans or high-risk changes, but cannot substitute for deterministic tests.

---

# CI Quality Gates

Plan progressive CI gates such as:

- formatting/linting
- typechecking
- unit tests
- database tests
- migration validation
- RLS/authorization suite
- integration contract suite
- golden semantics
- build
- dependency/security checks
- E2E subset where appropriate

Keep CI practical for a small team.

Separate fast PR gates from heavier scheduled/pre-release suites where appropriate.

---

# Environments and Deployment Sequence

Plan implementation of:

- local
- CI/test
- staging
- production

Do not make production the first integrated environment.

Define when Render, Auth0, Postgres, object storage and provider credentials become necessary.

Use fake/sandbox adapters before real credentials where possible.

Secrets never belong in repository files/prompts.

---

# Observability Implementation Order

Add observability alongside capabilities.

Plan:

- correlation/request IDs
- tenant-safe logs
- job visibility
- provider sync health
- external action state
- unknown-effect alerts
- freshness
- migration-run diagnostics
- platform-safe merchant health

Do not wait until launch to add diagnostics.

---

# Definition of Done

Define both:

## Task Done

and

## Milestone Done

Task completion requires deterministic evidence, not an agent saying “implemented.”

Milestone completion should require:

- all included tasks accepted
- relevant golden tests passing
- no unresolved severity-blocking defects
- security/tenant tests passing where applicable
- documentation updated
- applicable decision gates resolved
- rollback/disable behavior where appropriate

---

# Pilot Release Gates

Translate Phases 3–5 into a final set of gates before:

### Read-only shadow

### First consequential action

### Broader controlled action pilot

### Cutover

Do not conflate these gates.

---

# Effort / Complexity

Do not provide false precision such as:

> Task will take exactly 4.5 hours.

Instead label relative implementation complexity:

- XS
- S
- M
- L
- XL

Any XL task should be challenged and split where practical.

Any task rated XL must either be split before implementation or contain a written justification explaining why splitting would create a less safe or less coherent implementation boundary. AI agents must not begin an unjustified XL task.

Also classify risk independently:

- LOW
- MEDIUM
- HIGH
- CRITICAL

---

# Parallel Execution Strategy

Because multiple AI agents may eventually work simultaneously, identify which tasks can safely run in parallel.

Be conservative around:

- foundational schema
- RLS
- auth
- shared action engine
- database migration ordering
- provider interfaces
- global contracts

Parallelize independent UI/read-model/test/adapter work only when interfaces are stable.

Provide a dependency DAG.

Do not recommend maximum parallelism merely because agents are available.

---

# Recommended First Coding Task

At the end, identify exactly what the **first coding task** should be after Phase 6 approval.

It should be small, foundational and independently verifiable.

Do not execute it.

Also list the next 5–10 tasks in recommended order so the project has a clear starting runway.

---

# Review

After the first implementation plan is complete, use LLM Council or an independent reviewer if available within authorized tooling. Review the actual task files, manifest, coverage and dependency graph, not just the summary. Use only necessary sanitized planning material.

If independent review is unavailable, record that limitation and perform a structured self-review; never label self-review as independent. Do not install a review tool or transmit original source/customer data to obtain it.

Ask reviewers to attack:

- tasks too large for bounded AI sessions
- missing dependencies
- unsafe parallelism
- architecture violations
- tests deferred too late
- provider assumptions
- hidden migration work
- missing tenant/security gates
- sequence that enables mutations too early
- product features with no implementation home
- implementation work with no PRD requirement
- critical decisions not mapped to gates

Incorporate justified critiques and record each material finding, disposition, changed task/contract and verification result.

Include a fresh-context handoff check: attempt to understand and execute on paper one early foundation task, one workflow task, and one high-risk action/recovery task using only their stated reading sets. Report hidden decisions, undefined inputs and missing dependencies, then repair the task specifications. This is a planning walkthrough, not code execution.

---

# Deliverables

Create:

`docs/implementation/00-implementation-summary.md`

`docs/implementation/01-execution-principles.md`

`docs/implementation/02-dependency-graph.md`

`docs/implementation/03-milestone-roadmap.md`

`docs/implementation/04-repository-structure.md`

`docs/implementation/05-foundation-plan.md`

`docs/implementation/06-identity-tenancy-security-plan.md`

`docs/implementation/07-data-and-provenance-plan.md`

`docs/implementation/08-integrations-plan.md`

`docs/implementation/09-external-action-plan.md`

`docs/implementation/10-operational-workflows-plan.md`

`docs/implementation/11-analytics-plan.md`

`docs/implementation/12-platform-control-plane-plan.md`

`docs/implementation/13-migration-shadow-cutover-plan.md`

`docs/implementation/14-testing-and-ci-plan.md`

`docs/implementation/15-observability-and-deployment-plan.md`

`docs/implementation/16-provider-qualification-plan.md`

`docs/implementation/17-decision-gate-map.md`

`docs/implementation/18-risk-register.md`

`docs/implementation/19-definition-of-done.md`

`docs/implementation/20-agent-execution-protocol.md`

`docs/implementation/21-release-gates.md`

`docs/implementation/22-first-coding-runway.md`

Create:

`docs/implementation/tasks/`

with one bounded Markdown specification per implementation task.

Create:

`docs/implementation/task-manifest.yaml`

as the machine-readable task index.

Create:

`docs/implementation/adr-impact-map.md`

mapping approved ADRs to implementation milestones/tasks.

Also create:
- docs/implementation/START-HERE.md
- docs/implementation/execution-state.md
- docs/implementation/agent-prompts/single-task.md
- docs/implementation/agent-prompts/bounded-batch.md
- docs/implementation/requirements-coverage.yaml
- docs/implementation/task-manifest.schema.json
- evidence/implementation/verification.json
- evidence/implementation/quality-review.md
- evidence/implementation/phase6-input-baseline.json
- evidence/implementation/proposed-agents-update.md, if instruction drift exists
- the small reproducible static verifier under evidence/implementation/.

Keep the chapter documents concise views of the task contracts, rationale and cross-cutting constraints. Do not pad 23 documents with repeated background or copy complete task lists into every chapter.

Use Mermaid diagrams for the dependency DAG and milestone relationships where helpful. Provide a topological task order as data/text as well; a diagram alone is insufficient.

---

# Coverage Verification

Before finishing, prove that:

1. every `MUST HAVE — MVP` capability in the approved PRD maps to implementation task(s)
2. every architecture module required for MVP maps to task(s)
3. every approved owner decision OD01–OD09 maps to implementation behavior/tests
4. every applicable architecture ADR maps to implementation task(s)
5. every Phase 5 zero-tolerance correctness gate maps to automated/manual validation work
6. every GD/KR golden scenario maps to a task/milestone
7. every unresolved OP/A/MD decision maps to a specific blocking gate
8. every consequential provider action is preceded by qualification + safety-engine work
9. no deferred feature has accidentally entered the MVP roadmap
10. no production cutover is implied merely by implementation completion

Run a reproducible static consistency/coverage check, not only keyword counts.

Derive the requirement and validation inventories from the protected approved inputs independently of the task manifest. Map each source requirement/contract ID to task IDs, acceptance criteria/tests and release gates. Where a critical requirement has no ID, assign a local traceability ID with an exact source path/section; do not modify the approved source.

Check at minimum:
- schema validity, unique IDs, existing task files and resolvable spec references;
- no dangling dependencies, self-dependencies or dependency cycles;
- complete topological order, predecessor-before-consumer scheduling and valid first runway;
- every inventoried MVP/OD/ADR/validation requirement covered, or explicitly unresolved with a blocking gate;
- every task justified by a requirement, invariant or necessary engineering/operational dependency;
- no deferred/excluded feature introduced by an ambiguous task;
- gate references valid; start/completion/shadow/action/cutover boundaries respected;
- each real action/contact enablement depends transitively on its required qualification, safety, authority and recovery proof;
- golden realization and assertion tasks assigned, without treating logical datasets as already executed tests;
- safe parallelism consistent with dependencies, interface readiness and shared-change locks;
- manifest, task files, milestone totals and runway agree;
- protected input digests unchanged.

Use negative controls to demonstrate that the verifier rejects, for example, a dangling dependency, cycle and missing coverage mapping. Do not mutate protected files to test it.

Static checks prove structure and declared traceability, not semantic correctness, provider behavior or application security. Pair them with reviewer inspection of whether mapped tasks/tests actually satisfy the cited requirement. Report PASS/FAIL/NOT_CHECKED with scope; never claim future application tests ran.

---

# Planning Completion and Context Budget

Complete task contracts for the full approved MVP, not only M0/M1. Early runway tasks should be immediately actionable; later tasks must still state exact outcomes, dependencies, tests and gates without guessing unresolved policies.

Use staged work internally: inventory and graph, milestone/task drafting, cross-cutting/coverage mapping, review, then verification. Do not stop after an outline merely because the document set is large.

If a session limit interrupts work, save a truthful planning checkpoint under evidence/implementation/ with completed artifacts, remaining work, unresolved findings and exact resumption instructions. Do not label a partial package implementation-ready, invent a final task count, or imply Phase 6 is approved.

Phase 6 is complete only when the full task catalog, coverage, gate mapping, execution handoff, review disposition and static checks are present. Human approval of the plan remains separate.

# Stop Condition

Stop after the Phase 6 Implementation Plan.

Do NOT:

- scaffold the application
- install production dependencies
- create application code
- create database migrations
- provision infrastructure
- connect provider accounts
- call provider APIs
- deploy anything
- modify production data

At completion return:

1. milestone count and sequence
2. task count
3. first recommended coding task
4. next 5–10 tasks
5. critical-path tasks
6. safe parallel work
7. decisions that block early implementation
8. decisions safely deferred until pilot/action/cutover
9. major implementation risks
10. coverage verification result

Then wait for human approval before implementation begins.