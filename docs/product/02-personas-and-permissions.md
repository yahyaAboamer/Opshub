# OpsHub — personas and permissions

**Draft requirements.** [OD07](00-owner-decisions.md#od07--consequential-merchant-actions) is mandatory. [Gentry responsibilities](../reconstruction/09-roles-and-permissions.md) justify administration versus daily operations; they do not establish current enforced permissions. The [domain participation boundary](../domain/02-identities-and-relationships.md) separates User, Merchant Membership and Platform Operator Assignment.

## Personas

| Persona | Goal / visible work | Limits |
|---|---|---|
| Merchant Admin | Own merchant readiness, members, policies and consequential decisions; see queues, outcomes, sources and audit; resolve approval/reconciliation work | Acts only in merchant contexts where they hold Admin membership |
| Merchant Operator | Confirm/contact customers, investigate orders, maintain permitted operational notes, prepare action requests and work assigned cases | No cancellation, booking, replacement approval, refund execution or significant settings authority |
| OpsHub Platform Admin / Operator | Monitor and administer merchants, onboarding, memberships, platform diagnostics and commercial standing | Platform assignment supplies no customer-operation rights or general access to merchant contacts |

MVP uses two merchant roles and one bounded platform capability set. Splitting Platform Admin from Platform Operator into distinct permission sets is LATER unless the pilot owner requires it. Historical Support and Operations jobs can both fit Merchant Operator, with consequential work allocated to Admin. Brand Owner can hold Merchant Admin; a separate executive/read-only role is SHOULD HAVE. Customer, courier and advertising-provider portals are not personas in the MVP. A billing contact is an Admin responsibility, not a fourth operational role.

## Product permission matrix

“Prepare” means a draft/request without external business effects. “Record evidence” never grants permission to initiate the corresponding action. Platform entries apply only to assigned administrative scope.

| Capability | Merchant Admin | Merchant Operator | Platform Admin / Operator |
|---|---|---|---|
| View/search own merchant orders, contacts, items, shipment/case history | Yes | Yes for operational work | No routine customer-record access |
| View canonical dashboard and quality drill-down | Yes | Yes | Merchant-level health/quality aggregates only |
| View own merchant Product/SKU performance, spend/ROAS and source-qualified stock/season context | Yes | Yes | Source readiness/quality aggregates only; no routine operational analytics access |
| Configure connected-source ownership/capabilities and significant attribution/economic mappings | Yes | Inspect/refresh permitted read evidence; request changes | Administrative diagnostics only; no merchant policy/execution authority |
| Record contact attempt, consent evidence, reason and operational notes | Yes | Yes, attributed to current actor | No |
| Prepare cancellation/booking/replacement request | Yes | Yes | No |
| Approve and execute those consequential actions | Yes | No | No |
| Record reported external result | Yes; accepts result for consequential closure | May submit evidence for review; no implied execution/approval | No |
| Physically mark pickup collected | Yes | May attest collection with evidence under approved policy | No |
| Change order payment, business cancellation or authoritative source selection | Admin-reviewed correction with reason | Propose correction | No |
| Import approved operational files | Yes | Yes within Admin-approved mapping/scope; consequential state conflicts require review | Diagnostics/onboarding guidance; no operational import execution |
| Configure source ownership, mappings, policies, economics | Yes | No; can investigate/request | No merchant economic/operational settings |
| Assign/reassign ordinary operational cases | Yes | Claim/work own cases; request reassignment | No |
| Review consequential-case closure/reopen exceptional outreach | Yes | Prepare; ordinary contact-only closure allowed with evidence | No |
| Export | Own merchant operational export; contact-bearing export requires Admin | Contact-free scoped operational export; detailed contact export deferred | Scoped control-plane report without customer payloads |
| Invite/change/suspend merchant memberships | Yes; cannot leave merchant without an Admin | No | Administrative recovery with verification/audit; cannot self-grant membership |
| View commercial state / change billing contact | Yes | Service availability notice only | View/update commercial state under platform authority |
| Provision/activate/suspend merchant account | Request/read state | Read service notice | Yes with reason and affected-state confirmation |
| Assign platform authority | No | No | Restricted authorized platform administrator; no self-elevation |
| View audit | Own merchant relevant history | Own merchant operational history; administrative details restricted | Platform administrative audit and permitted diagnostics |

## Required behavior

PER01 — Always make the current merchant or platform context visible. A user holding both relationships exercises each separately. Changing context does not import rights from the previous context.

PER02 — Deny unauthorized actions consistently regardless of how the action is reached. Disabling a visible control alone is insufficient. Denied attempts do not cause external effects and remain reviewable without exposing another merchant's data.

PER03 — Merchant membership invitations identify merchant, recipient and offered role. Expired/revoked/wrong-recipient invitations cannot be accepted. An Admin must remain available; recovery is explicit and audited.

PER04 — Platform support can inspect merchant identity, member administration, freshness/error summaries and aggregate queue health. Redacted diagnostic information is the MVP support path. Impersonation, contact-level support browsing and merchant-action overrides are EXCLUDED from MVP.

PER05 — An invitation or support request cannot let platform staff silently add themselves as Merchant Admin. Recovery of an Admin membership requires verification of the legitimate merchant representative, records the authorizing party and blocks self-grant. Verification method is OP02, a launch decision.

PER08 — Exceptional outreach after the same contact objective's three attempts is not an Admin permission in MVP. Admin can review unfinished work and request a future policy change; higher contact limits need explicit owner approval changing OD04.

PER06 — Each consequential request records the acting Merchant Admin and exact reviewed intent. For supported connected actions, Admin authorizes/initiates in OpsHub and OpsHub executes/reconciles the external result; Operator/platform authority cannot invoke that effect. Manual execution is an attributed fallback exception. Admin may approve their own request; mandatory dual approval remains deferred. Material recipient/items/value/action-scope edits invalidate approval and require a new Admin decision.

PER07 — Uncertain imported callers/confirmers remain source claims, separate from authenticated recording/importing users. Never relabel historical free text as verified actor identity.

Acceptance: see AC02/AC03/AC06/AC10 in [11](11-mvp-acceptance-criteria.md). Export privacy and retention details awaiting approval are OP12 in [13](13-open-product-decisions.md).
