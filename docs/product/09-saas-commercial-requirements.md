# OpsHub — minimum SaaS commercial requirements

**NEW SAAS, draft for owner review.** Gentry did not provide a complete billing layer, and the [domain boundary](../domain/00-canonical-domain-overview.md#platform-administration-and-deferred-product-boundary) deliberately deferred it. These requirements introduce only the commercial shell needed to operate a merchant pilot.

## Minimum offering

COM01 — Each merchant has an explicit assigned plan/tier concept and commercial status, with current effective dates, authorizing platform actor and history. MVP can use one manually assigned pilot offering. Plan names/packaging and exact prices remain **TBD — COMMERCIAL DECISION**. No price, payment processor, invoice/payment entities or billing architecture is selected.

COM02 — A designated Merchant Admin is the billing owner/contact. Other Operators see availability/service notices without unrestricted commercial or contact details. Platform staff can administer the offering/status without obtaining merchant operational authority.

COM03 — Proposed commercial states: evaluation/trial (only if offered), active, overdue/review-required, suspended and closed. Service activation, onboarding readiness and commercial standing are displayed separately. A merchant can be commercially active yet have incomplete input readiness.

COM04 — Proposed state changes are manually authorized in MVP. Overdue does not automatically suspend; trial expiry, grace period, charges and exact transitions require OP11 approval. Trial is optional, with duration **TBD — COMMERCIAL DECISION**; no hidden default trial or automatic charge.

COM05 — Subscription/plan status shows what is permitted, effective period and how the Admin can request renewal/reactivation. Failed commercial administration does not mark merchant operations completed or discard data.

## Suspension and data preservation

COM06 — Suspension **must not destroy** merchant operational data, relationships, imported evidence or audit/history. Proposed behavior is read-only access for active Merchant Admins, existing-record exports and clear recovery notice; block new operational writes/ingestion/consequential requests until reactivation. Operator visibility and emergency continuity need OP11 approval before pilot.

COM07 — Pending requests/actions remain identifiable with their last evidence and responsible party. No automatic cancellation/refund/booking is caused by suspension or closure. Any external action already initiated is retained as succeeded/failed/unknown according to evidence, never relabeled as undone.

COM08 — Reactivation restores permitted access and preserved history, recomputes current attention with explicit freshness and prevents catch-up contact attempts from being scheduled tightly together. It does not fabricate input updates from the suspended period.

COM09 — Administrative closure is not destructive deletion. Retention/export/recovery policy requires OP12 approval. Account closure cannot authorize deletion without a separately approved product/legal retention policy.

## Entitlements and billing deliberately limited

COM10 — Entitlements may identify supported modules/member/input volume limits only when approved commercial packaging actually requires them. No detailed usage meter, overage billing or invented order quota is required for MVP. A limit must be visible before the user performs affected work; reaching it cannot silently drop data or deny access to retained history.

COM11 — A human billing/support process may maintain commercial records; OpsHub need not process payments in MVP. It must not present “paid invoice” or verified settlement without evidence. Subscription status is not a customer-order payment assertion.

Launch depends on approved pilot offering, commercial authority, availability/grace policy and data continuity (OP11/OP12), not exact final public pricing. [AC11](11-mvp-acceptance-criteria.md#ac11--platform-and-commercial-continuity) tests the approved behavior.
