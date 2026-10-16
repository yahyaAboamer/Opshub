# OpsHub — audit, data quality and trust

**Draft product requirements.** Evidence: Gentry [discrepancies](../reconstruction/13-live-vs-spec-discrepancies.md), [audit limits](../reconstruction/09-roles-and-permissions.md#auditability-observations), [domain assertions/provenance](../domain/03-events-and-projections.md). No claim is made that Gentry already retained the proposed history.

## Evidence labels and user-visible trust states

For source conclusions in this PRD: **Verified fact** is a scoped observation; **Strongly supported inference** is supported interpretation; **Hypothesis / unresolved question** lacks an established answer. OpsHub working data similarly distinguishes a source assertion, attributed human attestation, derived projection/estimate and unknown/conflicting input. A manual entry is evidence of what the actor recorded; it is not an independently verified financial or physical occurrence.

| Trust state | Product requirement / example |
|---|---|
| Missing | Identify missing field/source and affected action/KPI; no courier is not pickup proof |
| Stale | Display last accepted input, source coverage and expected-refresh basis; do not imply current transport truth |
| Partial / incomplete period | Show observed coverage versus requested period and provisional status; do not treat truncated history as a full month |
| Conflicting | Show competing values/source/time plus approved working selection or unresolved state; order cancellation and courier delivery can coexist as separate valid dimensions |
| Unknown status / mapping | Retain original value; exclude only from affected classified populations with visible count, not from history |
| Manual override | Identify actor/reason/effective time, prior/new working value and source assertions; keep it visible on affected results |
| Estimated / inferred | Name method/inputs; AOV proxy is not collected cash and historical inferred pickup is not collection |
| Import failed / unmatched | Row/group disposition, reason and safe locator; last valid data remains labeled; ownership uncertainty never guesses tenant |
| Pending outcome | Physically/actionally unfinished population; not a failure or unknown by default |
| External effect unknown | Requested/approved intent but no reliable result; separate reconciliation attention, no automatic success/failure |

These states can coexist. “Accepted file” does not mean complete period, “no validation errors” does not prove source truth, and a clean source input does not approve a consequential action.

## Required history

AUD01 — Consequential cancellation, booking, replacement, supported financial-action evidence and significant policy/source-authority changes retain: **what happened, when, initiating user, merchant, prior/new state where relevant, reviewed request/approval, outcome/failure/unknown and source/result evidence**. Distinguish requester, approving/initiating Merchant Admin, OpsHub connected execution origin, provider result and recording actor. New manual-fallback completion identifies Admin executor, exception reason, handover and accepted evidence; unverifiable results stay under review. Unknown historical actors/time remain unknown.

AUD02 — Audit onboarding/account/service/plan changes, invitations/membership/platform grants, source mappings, imports/repeats/rejections, exports, corrections, case closure/reopen, collection attestations and attempts-exhausted decisions. Denied consequential requests and attempted scope violations are reviewable without exposing unauthorized payloads.

AUD03 — Past available assertions and audit entries cannot be silently overwritten through ordinary editing. Correction appends attributable reason/prior/new/source/time and updates the current working view. Displayed history must explain what was known versus what changed; no fabricated older revision is required.

AUD04 — Consequential approval identifies exact reviewed intent. Result history distinguishes each required external effect: not started, succeeded, failed or unknown. “Approved” is never displayed as “completed”; duplicate/partial effects remain visible until reconciled. Material intent change requires fresh approval.

AUD05 — A source-reported caller/confirmer/payment/cash-out label remains source-reported. Authenticated recording/import user is a separate attributed actor. Fee components and aggregate are alternative views unless explicitly reconciled; source Paid does not prove bank settlement/customer refund.

AUD06 — Ordinary merchant users can inspect their operational history; Admin sees merchant administrative/action evidence. Platform sees scoped administrative audit and redacted diagnostics. Platform assignment is not permission to read customer contact payloads or execute merchant business actions.

## Quality and report use

TR01 — Quality attention explains affected record/source/rule, impact and permitted next action. Missing fields block only the capability whose prerequisite they invalidate. Missing margin/cost context does not block calling or canonical revenue/spend ROAS; incomplete attributed revenue/spend does qualify/withhold ROAS. Unresolved recipient/order identity blocks confident booking. Product/SKU/outcome/ad-allocation quality is required MVP trust, not deferred quality work.

TR02 — KPI/report exports retain completeness, unknown/excluded population and as-of. Incompatible source coverage/definitions are not compared without a visible qualification. Historical Gentry CLEAN/CAUTION/BLOCKED intent becomes user-visible complete/provisional/unavailable behavior, not a claim that its scripts enforced all gates.

TR03 — Review of a shared summary is attributable to the reviewed content/as-of. Editing it invalidates an earlier review claim. MVP sharing is a manual Admin responsibility; OpsHub does not send customer/owner communications automatically.

TR04 — Customer identifiers, raw contact exports and narratives must not leak through platform diagnostics or general summaries. Contact-bearing export is explicit Admin scope. Source originals and historical evidence names remain unchanged.

TR05 — Logical merchant isolation applies to every view, search, association, queue, metric, import, export and history. Same User or repeated phone/order number across merchants never permits cross-merchant linkage/access. Platform health overview contains only permitted aggregates/admin data, including redacted connection/analytics-input readiness.

TR06 — Retention, post-closure access, diagnostic visibility and supported security/session policy need explicit owner approval before pilot (OP12). This PRD requires authenticated access, role/scope denial, access removal and audit; it chooses no enforcement mechanism or compliance certification.

TR07 — Connected receipt success is separate from source coverage, action acknowledgement, final effect and restored health. Product/ROAS exports retain item/outcome/attribution/revenue/spend definitions and input revision; partial or unmapped data cannot be presented as complete product performance. Fallback/source reconciliation preserves earlier available claims without double-counting allocations or external effects.

Validation uses controlled synthetic cases, not real customer communications, bookings or destructive production tests. See [AC02–AC10](11-mvp-acceptance-criteria.md).
