# OpsHub — Phase 4 technical architecture

14 October 2026. **Proposed architecture for human review.** The owner's current instruction approves and closes Phases 1–3 and authorizes this phase. Older pending-approval text in those documents is a historical snapshot. This package designs the system; it supplies no application, production migration, integration implementation, deployment or implementation backlog.

## Recommendation

Use a **modular monolith**, delivered as a web/API process and a background worker from one versioned codebase/image. Keep business transactions, evidence, action coordination and MVP analytics in **PostgreSQL**. Use a shared database/shared schema with mandatory tenant keys, composite relationships and row-level security (RLS). Separate platform administration from merchant operations in application capabilities and database grants. A worker is a deployment process, not an independently owned microservice.

The technology-independent design in 01–14 precedes the selection in 15. Recommended stack: React/TypeScript/Vite; NestJS/TypeScript on Node LTS using the standard Express adapter; PostgreSQL 17 with Kysely and reviewed SQL; managed Auth0 OIDC authentication with OpsHub-owned server sessions and authorization; pg-boss for durable jobs; private Amazon S3 storage; paid Render web/worker/Postgres; Sentry plus structured logs and selected OpenTelemetry spans; Resend for account invitations only; Vitest, real-Postgres/Testcontainers and Playwright. Exact package patches are selected and pinned during a later authorized build. No Redis, warehouse, Kubernetes, event bus, payment processor or embedded telephony is needed for MVP.

## Authoritative inputs and evidence classes

The [PRD](../product/14-prd.md), [OD01–OD09](../product/00-owner-decisions.md), [MVP priorities](../product/03-mvp-feature-prioritization.md), [acceptance gates](../product/11-mvp-acceptance-criteria.md), [canonical catalog](../domain/01-entity-catalog.md) and [domain invariants](../domain/05-domain-invariants.md) govern this proposal. [Reconstruction](../reconstruction/00-system-map.md) and its linked evidence explain legacy knowledge and limitations.

**Verified fact** means a scoped project observation or accessible official provider contract. **Strongly supported inference** is explicitly identified. **Hypothesis/unresolved** includes account-specific provider behavior and launch policy choices. Architecture decisions are **recommendations**, not facts about Gentry. OD01–OD09 override older domain proposals where they settle cardinality, formulas, authority or MVP inclusion. OP02–OP13's narrower policy/evidence choices remain launch gates; they do not reopen OD08/OD09.

## Nonnegotiable technical properties

- An order, item, outbound shipment, reverse consignment, case, contact attempt and provider effect each retain their own identity and grain. Only cases resolve. Payment cannot establish collection; courier delivery cannot establish goods kept.
- The normalized MVP permits one outbound per order and at most one return/pickup case. Unsupported and independently evidenced duplicate provider objects remain observable exceptions outside the accepted association; constraints never destroy their evidence. Replacement produces a linked new order.
- Merchant Admin approval covers immutable intent and exact effect scope. Platform grants and UI visibility are insufficient. Execution rechecks current Admin membership, service/capability state and reviewed dependencies.
- Local deduplication suppresses repeated requests and concurrent Admin intent. **Outcome unknown blocks another mutation and manual execution**. Queue delivery is not exactly-once external execution; timeouts and absence of a search result are not no-effect evidence.
- Inbound evidence never triggers merchant business mutations. Corrections preserve previous assertions and provenance. No universal newest/manual/provider-wins rule is introduced.
- Metrics carry versioned definition, cohort/window/as-of, numerator, denominator, exclusions, pending/unknown populations, coverage and reproducible contributors. Product associations overlap; monetary allocations conserve one declared total.

## Review map

| Concern | Design |
|---|---|
| Context and trust boundaries | [01](01-system-context.md) |
| Style, modules and PRD coverage | [02](02-architecture-style-and-modules.md) |
| Tenancy, identity, server authorization | [03](03-multi-tenancy-and-identity.md) |
| Persistence and invariants | [04](04-data-architecture.md) |
| Provider synchronization | [05](05-integrations.md), [18 capability evidence](18-provider-capability-review.md) |
| External effects and concurrent approvals | [06](06-external-action-safety.md) |
| Jobs, recovery and operational attention | [07](07-background-jobs-and-reconciliation.md) |
| Interfaces and transaction boundaries | [08](08-api-and-application-boundaries.md) |
| KPIs/Product/SKU/ROAS | [09](09-analytics-architecture.md) |
| Threats, audit, provenance and privacy | [10](10-security-threat-model.md), [11](11-audit-provenance-and-privacy.md) |
| Monitoring, deployment and restore | [12](12-observability-and-operations.md), [13](13-deployment-and-environments.md) |
| Architectural test strategy | [14](14-testing-strategy.md) |
| Stack and alternatives | [15](15-technology-selection.md) |
| Cost and extraction thresholds | [16](16-cost-and-scale-review.md) |
| Unresolved choices and release gates | [17](17-open-architecture-decisions.md) |
| Independent challenge and quality gate | [19](19-architecture-review.md) |

Significant proposals are recorded in [ADRs](adr/ADR-001-architecture-style.md). Naming-only corrections are recorded in [Step 0 review](../../evidence/architecture/naming-consistency-review.md). The [input baseline](../../evidence/architecture/phase4-input-baseline.json) protects original files and closed evidence.

## Biggest risks and review boundary

Provider-account qualification, reliable identification of an uncertain create result, Shopify cancellation side effects, commerce/courier automatic activity outside OpsHub, Meta spend attribution/time/currency, tenant-context leaks and restoration of stale action state are the largest risks. [17](17-open-architecture-decisions.md) names the evidence/owner gates and containment for each. A documented API is not proof that the pilot can execute safely.

Review this architecture, ADRs, provider qualifications and residual policy gates before Phase 5. Phase 4 ends here; no subsequent implementation or migration work is authorized by this package.
