# OpsHub — platform administration workflows

**NEW SAAS draft product requirements.** Gentry did not expose a verified platform control plane. The [domain E26/I27 boundary](../domain/05-domain-invariants.md) and [OD07](00-owner-decisions.md) require separate platform authority. [02](02-personas-and-permissions.md) defines the permitted scope; [09](09-saas-commercial-requirements.md) defines commercial status. Platform staff do not run merchant booking, cancellation, replacement or refund work.

## Platform view

Show merchant identity, designated Admin/billing contact, activation/commercial status, readiness, active members, commerce/courier/applicable advertising connection capability/coverage/freshness, rejected/unmatched inputs, aggregate queue/approval ageing and incidents. Drill-down remains redacted administration, not contacts/call narratives/order exports. Service standing, operational readiness, analytics-input completeness and connection freshness are separate dimensions; platform gets no merchant-action authority.

## PF01 — Provision and activate a merchant

- **Goal / entry:** verified merchant representative requests an account in the approved pilot/commercial offering.
- **Primary flow:** platform checks merchant identity/source-boundary intent → creates workspace administrative record → invites verified initial Admin → records plan/commercial state → monitors merchant-led WF01 readiness → authorizes account activation with reason.
- **Alternates:** duplicate name does not establish duplicate business; unresolved ownership is reviewed. Account exists but no Admin/data/configuration is not operationally ready. Merchant operational thresholds/mappings need Merchant Admin decision.
- **Result / permissions:** platform account is provisioned/active; merchant can finish onboarding. Only assigned platform staff may provision/activate.
- **Attention / success:** incomplete onboarding has reason and responsible party; no usable dashboard falsely reports zero. AC01/AC11.

## PF02 — Administer memberships and recover access

- **Goal / entry:** merchant needs initial Admin recovery, invitation diagnosis or suspension of compromised/inactive membership.
- **Primary flow:** inspect membership administration and current verified Admin → verify legitimate merchant authorization → propose exact recipient/role change → record authorizing party, reason and effective result → inform merchant through an approved human support process → retain earlier authorship.
- **Alternates:** cannot remove last active Admin without a verified recovery path; wrong/expired/revoked invite cannot be reused. Platform actor cannot self-grant membership or silently become an Admin. A user with two merchant memberships has independently administered rights; suspending one does not silently suspend the other.
- **Result / permissions:** scoped membership/invitation change only; no business-record edits. Granting platform authority is a separately restricted platform administrative action, not a merchant role change.
- **Attention / success:** unresolved verification or orphaned work remains visible; access changes and denied self-elevation auditable. Verification policy OP02 is a launch gate. AC02/AC03/AC09/AC11.

## PF03 — Monitor merchant operational readiness and source health

- **Goal / entry:** active merchant has failed, stale, incomplete or conflicting input, or an unusually old work backlog.
- **Primary flow:** review aggregate status/as-of/coverage → distinguish source failure from merchant work delay → inspect redacted error category and affected scope → assign administrative support follow-up → guide Merchant Admin to refresh/review → confirm new input health or leave issue open.
- **Alternates:** platform cannot call customers, resolve merchant work or execute provider actions from aggregates. Successful connection/file receipt without coverage is not healthy input. Label manual fallback reason and last receipt separately from integrated capability/health; fallback completion is not connection restoration. Missing applicable spend cannot be presented as zero or healthy ROAS.
- **Result / permissions:** administrative incident status and guidance recorded; merchant operational truth remains owned by merchant users/sources.
- **Attention / success:** actionable current failure, partialness and no recent input visible; no unchanged-status notification requirement. AC08/AC11.

## PF04 — Manage service/commercial availability

- **Goal / entry:** approved activation, renewal, suspension or reactivation decision exists.
- **Primary flow:** inspect separate plan/commercial/service states → review affected merchant and reason → confirm permitted service-state change → record actor/time/prior/new/reason → present clear merchant-facing availability/recovery notice.
- **Alternates:** billing overdue is not automatically suspension absent approved policy. Suspension never deletes orders/cases/audit; reactivation retains history and refreshes due work without immediate clustered calls. Commercial update does not mark cases resolved or execute merchant actions.
- **Result / permissions:** platform administers access/commercial state, Merchant Admin owns billing contact and operational response. Proposed read/export access while suspended requires OP11 approval.
- **Attention / success:** reason, effective state and recovery route visible; preservation and resumability verified. AC11.

## PF05 — Investigate support and platform administrative history

- **Goal / entry:** merchant reports an incident or administrator needs to explain a platform change.
- **Primary flow:** locate merchant administrative context → read authorized audit/health summaries → correlate import receipt/failure timing and administrative changes → document finding/next owner without customer payload → verify support case outcome.
- **Alternates:** insufficient redacted evidence remains unresolved or Merchant Admin supplies a redacted diagnostic. No impersonation, contact-level access, merchant-action override or production experiment is implied by a support case.
- **Result / permissions:** support findings and administrative follow-up only; platform support task resolution is separate from merchant operational-case resolution.
- **Attention / success:** actor/merchant/time/prior/new/result explain important changes. Denied/out-of-scope access has no effects. AC03/AC09/AC10/AC11.

Automated billing, global customer search, cross-merchant operational exports and platform execution of merchant business actions are outside MVP. Exact pilot plan, status policy, staff authority and verification procedure are [open product decisions](13-open-product-decisions.md).
