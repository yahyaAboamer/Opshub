# OpsHub — system context and trust boundaries

**Proposed architecture**, governed by [OD01–OD09](../product/00-owner-decisions.md) and [permissions](../product/02-personas-and-permissions.md). Gentry is an evidence/regression source, not a runtime dependency. The diagrams describe the target system, not observed Gentry topology.

```mermaid
flowchart LR
  MU[Merchant User: Admin or Operator]
  PU[Assigned Platform Administrator]
  subgraph BROWSER[Untrusted browser boundary]
    MA[OpsHub Merchant Application]
    CP[OpsHub Platform Control Plane]
  end
  subgraph RUNTIME[OpsHub application trust boundary]
    API[Monolith: merchant and platform entry points]
    W[Worker: sync, reconciliation, projections, exports]
  end
  subgraph DATA[Private persistence boundary]
    PG[(PostgreSQL: tenant data, control data, jobs)]
    OBJ[(Private object storage)]
  end
  subgraph EXT[External provider boundaries]
    S[Shopify]
    B[Bosta]
    M[Meta: spend reads]
    IDP[Managed identity provider]
    EM[Account invitation email]
  end
  OBS[Redacted logs, metrics and traces]
  MU --> MA
  PU --> CP
  MA -->|same-origin session and REST| API
  CP -->|platform authority and REST| API
  API --> PG
  API --> OBJ
  W --> PG
  W --> OBJ
  API -->|durable work reference| PG
  W -->|qualified reads and approved effects| S
  W -->|qualified reads and approved booking| B
  W -->|report retrieval| M
  S -->|verified webhook ingress| API
  B -->|qualified callback ingress| API
  API -->|OIDC redirect and callback| IDP
  W -->|account invitations only| EM
  API --> OBS
  W --> OBS
```

## Boundary contracts

| Boundary | Trust decision and permitted information |
|---|---|
| Browser → application | Browser supplies requested context and intent, never trusted actor/tenant/role/result. Server validates session, active participation, requested scope, input and action eligibility |
| Merchant → platform surface | Separate route namespace, authorization guard, DTOs and database pool. Common account identity does not merge grants. Platform reads administrative/aggregate records, never operational customer payloads |
| API/worker → persistence | Runtime roles do not own tables or bypass RLS. Each merchant transaction establishes one checked tenant context; exports/projections obey the same boundary |
| Provider → webhook ingress | Verify provider authenticity before accepting tenant ownership. Resolve signed/verified provider account to an existing connection; never trust payload merchant ID. Persist inbox before acknowledging |
| Worker → provider | Server credentials only; exact connection/account checked. All writes enter the action coordinator. Meta has read-only capability. No provider token reaches the browser/control-plane response |
| Object store | Private buckets, environment/merchant/object prefixes plus authorized DB metadata. Keys are not permissions. Downloads reauthorize; customer-bearing exports stream through the authenticated API |
| Identity provider | Authentication establishes issuer/subject, not merchant/platform authority. Local grants and sessions govern business access |
| Observability | Allowlisted metadata/aggregates; no contact details, narrative, tokens, payload bodies, signed links or financial mutation variables |

The platform and merchant UI may be distinct bundles served by one origin. Separate UI deployments and distinct product authentication systems are unnecessary. Platform pool restrictions are a defense against accidental application queries, not containment of a fully compromised web process holding both pools. [10](10-security-threat-model.md) records this residual risk.

## Main interactions

Inbound Shopify/Bosta data becomes observations and selected working state, then refreshes attention and analytics. Meta reports become period spend revisions. Merchant users contact customers outside OpsHub and record evidence. Operators prepare requests; Admins authorize immutable intentions. Worker execution and later read/result evidence update individual effects. Case closure evaluates required effects and physical/business evidence separately.

No automatic customer communication or billing/payment processor is proposed. Invitation mail supports account onboarding, not merchant-customer outreach. Commercial state is a manual platform-admin record, independent of order payment. [02 modules](02-architecture-style-and-modules.md), [06 effects](06-external-action-safety.md) and [11 privacy](11-audit-provenance-and-privacy.md) define the detailed boundaries.
