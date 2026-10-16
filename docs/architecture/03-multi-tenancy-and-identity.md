# OpsHub — multi-tenancy, identity and authorization

**Recommendation:** shared database/shared schema with mandatory tenant ownership, application scope checks, composite foreign keys and forced PostgreSQL RLS. [ADR002](adr/ADR-002-tenancy.md), [ADR004](adr/ADR-004-authentication-and-authorization.md). Authority derives from [OD07/PER01–PER07](../product/02-personas-and-permissions.md), not Gentry's unverified grants.

## Tenant strategy alternatives

| Strategy | Benefits | MVP costs / decision |
|---|---|---|
| Shared database/schema, `merchant_id` keys | One migration/backup, transactional invariants and economical small pilot | Requires disciplined RLS/relations/jobs/exports; recommended with isolation tests |
| Schema per tenant | Namespace separation | Repeated migrations/search-path risk, pool complexity and weak protection if one role sees all schemas; reject for MVP |
| Database per tenant | Stronger credential/failure boundary; independent restores | Provisioning/connection/upgrade/backup fleet, awkward platform health and small-team overhead; defer until contractual isolation or measured operational need |

One Merchant/Workspace is the tenant root; workspace is an alias, not a nested unit. One operational Shopify store/Bosta account and applicable Meta account are explicitly bound to it for the pilot. Multi-store consolidation/shared provider-account allocation is deferred under OP02. Enforce a verified provider-account binding to at most one active merchant in an environment; disconnect/rebind requires ownership review and retains the old namespace/history.

## Ownership and context propagation

Every merchant-scoped table, observation, action, job business record, projection and file metadata has nonnull `merchant_id`. Primary IDs are opaque canonical UUIDs, but UUIDs alone do not provide isolation. Parent/child references use `(merchant_id, id)` foreign keys, including items, cases, effects, contributors and evidence links. External IDs are qualified by verified source namespace/object kind; phone/order number/SKU text are never global keys.

Request context is built server-side: authenticated User + current active Membership + explicit route merchant + permitted capability + current service state. Switching merchant rechecks membership; the browser selector does not change a global process variable. Use one immutable context per request/job and transaction-local database settings on that transaction's checked connection. Missing context fails closed. All reads/writes use that transaction; returning a pooled connection cannot leave tenant settings behind. No asynchronous global tenant variable or mixed-tenant transaction.

RLS applies to reads and write checks; runtime roles are nonowners, nonsuperusers, without `BYPASSRLS` or schema-altering grants. Force RLS on tenant tables. Use invoker-security views and inspect grants for every added table/projection. Constraints are scoped to tenant and generic error messages prevent revealing another tenant's existence. PostgreSQL owners/superusers and referential checks have special behavior; RLS is a defense against omitted filters, not a defense against an attacker executing arbitrary SQL with a runtime credential. [Official RLS behavior](https://www.postgresql.org/docs/17/ddl-rowsecurity.html), [invoker views](https://www.postgresql.org/about/featurematrix/detail/security-invoker-views/).

| Surface | Required isolation |
|---|---|
| Query/search/direct ID | Checked route context, tenant predicates, RLS and same-tenant relationships; inaccessible IDs return nonenumerating result |
| Jobs | PII-free queue envelope with tenant/connection/action IDs; checked business record and trusted job type determine context; separate restricted tenant-data pool |
| Cache/browser state | No shared server cache initially. Query keys include context, subject/filter/permission and revision. Clear merchant data on context/logout/suspension; no persistent offline PII cache |
| Export | Persist requested scope/requester/membership/version; reauthorize at generation and each download; tenant file metadata plus scoped storage key |
| Files | Private environment/merchant prefix, unguessable object ID, authenticated metadata lookup; no public listing or key-based access |
| Analytics | Tenant keys/FKs/RLS on projections and contributors. Platform only gets allowlisted aggregate health table |
| Logs/support | Tenant pseudonym/incident/correlation IDs and safe categories; no contacts/narrative/raw payload. Scoped platform assignment validates each administrative target |

## Shared identities, separate authority

`users` and external IdP subject bindings are platform-scoped identity data. `merchant_memberships` belongs to one merchant and offers Admin or Operator; `platform_operator_assignments` has separately enumerated administrative capabilities and explicit target scope. A user may hold both; neither creates the other. No platform superuser flag is accepted by merchant command guards.

Use separate merchant and platform route namespaces/guards/DTOs. A restricted control-plane DB pool can access approved workspace/member/commercial records and precomputed redacted health only; it has no SELECT on orders/contact/payload/effects or merchant write grants. Tenant runtime and worker pools have different grants from control-plane/admin/migration/queue pools. Platform recovery uses a narrow audited administration operation, not generic merchant repository access. Platform grant provisioning must be controlled out of band initially and subsequently by a specifically authorized platform grant capability; no bootstrap endpoint available to ordinary users.

| Operation | Server authority |
|---|---|
| Operational reads, record contacts/ordinary evidence, prepare action | Active Merchant Admin or Operator; role-specific evidence policy |
| Significant corrections/mappings/economics, connection ownership, approve/start booking/cancel/replacement, accept consequential result | Active Merchant Admin in that merchant |
| Operator imports/refresh/export | Approved mappings/read capabilities; contact-free export; no mutation side effects |
| Platform provision/recover/suspend/monitor | Active scoped platform assignment; recovery verification and no self-grant; no customer business capabilities |
| Worker provider mutation | Recorded exact Admin authorization plus current membership/service/capability/dependency check; automation origin is not a new authority grant |

## Authentication, sessions and invitations

Managed OIDC hosted authentication handles account login/password recovery/MFA. Prefer authorization-code flow with PKCE, validated state/nonce/issuer/audience/redirect and code exchange on the server. Local User binding uses `(issuer, subject)`, never unverified email or display-name equality. [Auth0 PKCE reference](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow-with-pkce/add-login-using-the-authorization-code-flow-with-pkce).

OpsHub stores opaque, hashed server-session tokens in PostgreSQL. Browser cookie is Secure, HttpOnly, SameSite=Lax and host-only; rotate on login/reauth and privilege change. Mutating same-origin requests require CSRF token and Origin validation. Session rows retain authentication time, expiry/revocation and current context; grants are read live for privileged actions, not frozen in an IdP JWT. Membership suspension takes effect on the next request and on unstarted worker effects; existing authorship remains. An already transmitted provider request cannot be undone by session revocation. Other tenant memberships remain independent.

Invitations bind tenant, intended verified email/IdP recipient, offered role, inviter, expiry and a hashed single-use token. Acceptance requires authenticated verified recipient, current invitation validity and one transaction updating invitation/membership/audit. Rate-limit guessing/resends; accepting does not grant platform authority. Initial Admin and recovery require OP02's legitimate merchant verification. Concurrent last-Admin changes serialize on the merchant administration row and cannot orphan the workspace. Platform staff cannot use recovery to grant themselves membership; record independent merchant authorizer and target verification. Legitimate dual-context participation is created through the authorized merchant path.

Step-up authentication is justified for platform grants/recovery, major connection ownership/credential replacement and contact-bearing exports. Routine contacts and every ordinary booking need an explicit intent confirmation, not compulsory repeated MFA. Proposed session duration and step-up freshness are policy gate A04/OP12; there is no approved security timeout hidden in this design. Unattended IdP token refresh does not count as recent user reauthentication.

## Service state and emergency continuity

Database restoration invalidates restored sessions/invitations through an independently enforced recovery epoch. Restored local grants are provisional until verified; fresh login cannot resurrect a revoked membership or platform assignment. 13 gates customer reads/exports as well as mutations until independent privacy replay and audited current-authority revalidation pass.

Manual commercial standing, operational readiness and service availability are independent. Proposed suspension blocks new business writes/normal sync/mutation starts; preserves active Admin read/export and allows **bounded read-only reconciliation of already-started effects and durable callback receipt** so suspension cannot hide an unknown consequence. Operators' suspended access and this continuity exception need OP11 approval before launch. It never books/cancels/refunds. Reactivation recomputes due work and source coverage, without clustered catch-up calls. [17 gates](17-open-architecture-decisions.md).
