# OpsHub — architecture style and modules

**Recommendation:** modular monolith with one shared relational persistence system and two runtime process roles. [ADR001](adr/ADR-001-architecture-style.md) records this proposal. The approved [PRD](../product/14-prd.md) needs consistent authority, cases, effects, evidence and analytics; module names are not permission to introduce excluded features.

## Alternatives

| Criterion | Modular monolith | Service-oriented/microservice alternative |
|---|---|---|
| MVP/small AI-assisted team | One dependency graph, code review and local environment; explicit module ownership restrains agent edits | Several deployments/contracts/operational owners before workload justifies them |
| Transactions and invariants | Approval, intent reservation, audit and durable work commit together | Cross-service coordination and eventual consistency around safety-critical invariants |
| Integration workloads | Worker isolates latency; per-provider limits and queues isolate work | Independent scaling/failure domains, but network failures add coordination burden |
| Analytics | Typed queries/projections over reviewed module read models in the same database | Replication/CDC and additional consistency/watermark design |
| Operations | One release, web/worker processes, Postgres restore and object storage | Service discovery, distributed tracing, multiple migrations/on-call paths |
| Future extraction | Ports, owned tables and durable internal notifications provide measured extraction points | Premature extraction is costly to reverse and weakens transactional boundaries |

The service alternative would split integrations/analytics/operations with separate databases and message transport. It is rejected for MVP. Later extraction requires a measured bottleneck or independent security/operational need, not an entity count. Web/worker can scale separately while sharing one release. No network calls between internal modules.

## Module contracts

Commands are in-process typed application calls; notifications describe committed internal changes, not claimed provider occurrences. Durable work uses the same transaction as the relevant state. Consumers cannot edit another module's tables directly. Cross-module business transactions use a coordinator and one checked unit of work; avoid cyclic service injection. Read-only projections consume explicit read contracts. The table gives owned data, capabilities, dependencies and forbidden responsibilities together.

| Module | Responsibility / owned data | Exposed capabilities; commands/notifications | Dependencies and forbidden responsibilities |
|---|---|---|---|
| Identity & Access | User/external identity, server sessions, invitations, membership and platform assignments | Authenticate, select context, grant/suspend member; `ParticipationChanged` | Tenant admin state; cannot derive business rights from IdP claims, email or platform assignment |
| Tenant & Commercial Administration | Workspace/admin metadata, service/readiness, manual plan/subscription assignment, recovery record | Provision/activate/suspend/reactivate; `ServiceStateChanged` | Identity; cannot change merchant policies, browse contacts, charge cards or resolve merchant cases |
| Orders | Order, items, contact snapshots, commercial/payment/confirmation working dimensions and typed order links | Ingest accepted order interpretation, search, confirmation entry/evidence; `OrderInterpretationChanged` | Provenance, catalog binding; cannot select courier truth or initiate external mutation from sync |
| Case & Contact Operations | Confirmation/return/pickup work, objective identity, attempts, reach, required work, collection attestations and case history | Claim/assign/contact, prepare action, request closure; `CaseWorkChanged` | Orders, logistics read contracts, actions results; cannot reset three-attempt budget, globally resolve order or certify payment as collection |
| Logistics | Accepted shipment associations, purpose/state, reported counters and independently evidenced attempts | Apply mapped courier observations, tracking, finality/collection evidence; `ShipmentInterpretationChanged` | Provenance, Orders, Actions; cannot book on its own, fabricate attempt events or discard duplicate consignment evidence |
| External Actions | Immutable action intent, approval, objective/effect reservation, execution attempts/results/reconciliation and handover | Request/review/start/reconcile/handover; `EffectEvidenceChanged` | Access, service policy, Orders/Cases/Logistics snapshots, integration adapter ports; cannot retry unknown writes, auto-refund/compensate or bypass Admin authority |
| Catalog & Product Context | Product/variant bindings, dated stock/economic/classification observations and aliases | Catalog lookup/mapping, inspect dated context; `CatalogInterpretationChanged` | Provenance/integrations; no inventory ledger, season CRUD suite, tier/replenishment/production automation |
| Advertising Inputs | Ad references, spend series/revisions and approved attribution input mappings | Accept Meta/fallback spend, map direct/generic/unallocated scopes; `SpendObservationChanged` | Provenance/catalog; no ad/campaign/budget writes or invented SKU attribution |
| Integration & Transfer | Connections, encrypted credential versions, provider capabilities, inbox receipts, sync checkpoints, import/export runs/files | Verify connection, sync, safe adapter request, preview/accept/import/export; `ObservationsAccepted` | Access/provenance and target module ports; cannot decide source authority, execute arbitrary mutations or mark business cases complete |
| Trust & Audit | Observations/assertions, interpretation references, corrections/conflicts, policy revisions and append-only audit | Explain belief, review correction, append attributable history; `InterpretationSelected` | Checked context; no generic event-sourcing framework, payload dumping, unapproved destructive retention |
| Read Projections | Attention membership, KPI/product result revisions, contributor indexes and redacted health summaries | Recompute/query/drill/export with version/coverage; `ProjectionPublished` | Reviewed module read contracts; no business writes, generic task manager or warehouse |

Policy definitions are owned by their business module and registered/versioned through Trust. Platform staff see redacted health projections and administrative history via Tenant Administration; this is a capability boundary rather than another duplicate business module. Return and pickup subtype records belong to Case Operations, while carrier consignments belong to Logistics.

## Every MUST-HAVE has a home

| PRD ID | Architectural home / relevant chapters | Acceptance gate |
|---|---|---|
| MR01 | Tenant Administration + Access + connection readiness;03/05 | AC01/AC11 |
| MR02 | Access sessions/invitations/memberships/context;03 | AC02/AC03 |
| MR03 | Orders/items/bindings plus independent Logistics/Cases;04/08 | AC02/AC04/AC06 |
| MR04 | Trust conflicts/corrections + attention projection;07/11 | AC06/AC08 |
| MR05 | Orders confirmation entry/evidence + contact objective;04/07 | AC05/AC07 |
| MR06 | Case/contact attempt budget, reach and required actions;04/07 | AC05/AC06 |
| MR07 | Logistics one-outbound association + Admin action coordinator;05/06 | AC03/AC06/AC14 |
| MR08 | Return subtype + disposition/transport/contact/effect evidence;04/07 | AC06/AC13 |
| MR09 | Pickup subtype + purpose/physical attestation/payment separation;04/09 | AC06/AC07 |
| MR10 | Replacement objective/actions + linked new Order;06 | AC03/AC09/AC14 |
| MR11 | Attention and six operational metrics + Product/ROAS views/export;07/09 | AC07/AC10/AC15 |
| MR12 | Shopify/Bosta/applicable Meta connectors + safe transfer/reconciliation;05/18 | AC04/AC08/AC14 |
| MR13 | Module-owned effective policy/mapping revisions;04/11 | AC03/AC09 |
| MR14 | Trust/Audit observation/correction/history;11 | AC04/AC08/AC09 |
| MR15 | Restricted platform administrative capabilities/health;03/12 | AC02/AC03/AC11 |
| MR16 | Manual commercial/service shell and preserved data;03/13 | AC11 |
| MR17 | Case ownership/due state + derived attention;07 | AC05/AC09/AC13 |
| F18 | Catalog/product/variant/item bindings;04 | AC04/AC15 |
| F19 | Product/SKU sales/revenue/outbound/return contributor projections;09 | AC15 |
| F20 | Advertising inputs + method-versioned allocation/ROAS;05/09 | AC07/AC15 |
| F21 | Dated source season/classification context only;04/09 | AC15 |
| F24 | Integration adapter ports + safe action/result loop;05/06/18 | AC03/AC14 |
| F25 | Scoped revision-preserving summary/export;08/09/11 | AC07/AC10 |

## Deliberate exclusions

F31 has no multi-outbound feature; duplicate observations are exception evidence, not an accepted second outbound. F32 has no arbitrary reports/workflow builder. F33 has no platform impersonation, contact browsing or action override. F36 has no workbook-layout replication or named-employee role logic. Deferred F22/F23/F27/F29/F30/F34/F35 do not acquire financial ledgers, native refunds, messaging, advanced episodes, checkout, mobile apps, broad provider marketplace or deep BI through these modules. SHOULDS such as rich seasons/executive briefs are not MVP dependencies. The existence of a canonical entity or provider endpoint does not change this scope.
