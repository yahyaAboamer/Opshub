# Open questions and next evidence

This is the human review agenda. It does not authorize production experiments. See [discrepancies](13-live-vs-spec-discrepancies.md) and [evidence ledger](../../evidence/live/observation-ledger.md).

## Owner and Operations decisions

| Priority / question | Needed clarification |
|---|---|
| P0: Which metric definitions govern current reports? | Coverage numerator, intervention denominator, kept/Bosta-way/physical pickup, leg versus order, calendar and partial-period comparison. |
| P0: Is June courier history complete? | Pagination/import scope, office evidence and matched creation/completion-date exports. Resolve before interpreting inferred pickups. |
| P0: What makes a pickup collected, cancelled or a no-show? | Explicit collection evidence and payment/refund/return precedence. |
| P0: Which thresholds are approved? | Confirmation 60%, Omar 15%, pickup 30%; current product defaults 2.8/3.8/20/.15. Record approval/date/definition. |
| P1: What is current return-call policy? | Retry ceiling, priority, 48-hour clock and later answered/NoAnswer precedence. |
| P1: What does resolved mean? | Called done, reached with cause, service action completed and financial refund are distinct. |
| P1: Were top-ups and SKU additions ingested? | Locate the current external call Sheet/catalogue; explain intentional exclusions. |
| P1: Are manual records/snapshots active? | Operational use, sync versus manual authority and overwrite behavior. |
| P1: Where is Production? | Incoming stock/minimum batch lifecycle, owner and available role. |
| P2: Which historical economics remain active? | Actual versus modeled fees, gateway heuristic, AOV proxies, catalogue margin and recoverability. |

## Phase 1B closure and remaining technical gap

Evidence: [technical ledger](../../evidence/live/phase1b/technical-ledger.md). This pass is complete; it does not authorize another production experiment or design work.

| Question | Current evidence / status |
|---|---|
| Which delivered frontend/protocol is present? | **Resolved within client evidence:** Next App Router declaration 16.3.5, React/DOM canary, inline Flight and React server-action machinery. Backend dependency inventory remains unknown. |
| How do product presets and PDF controls act? | **Resolved within client/DOM evidence:** enclosing GET form submission, preset period/date-input handling; printable HTML and browser window.print. No server PDF action observed. |
| Is there a named call-import interface? | **Partially resolved:** uploadCallSheet public reference, file/action state and expected added/alreadyThere/noCallStatus/unmatched feedback. Actual request/response, CSV rules/deduplication/transactions unknown. |
| Does any auth/permission structure appear? | **Partially resolved:** unauthenticated /orders → server 307 login redirect; order navigation permission labels. Session mechanism, grants, server actions, exports and record/merchant authorization unverified. |
| Are there extra routes/features? | Product printable report now access-verified; login redirect destination **DISCOVERED, NOT ACCESS-VERIFIED**. No additional Production/admin route established in retained assets. Other legitimate roles remain needed. |
| Does a nondefault product period export correctly? | **Resolved for one sample:** September CSV 20 rows/28 columns, matching interval and aggregate UI totals. Other filters, cleanup output and transport headers/status unknown. |
| What drives automatic synchronization? | **Unresolved:** changing markers without manual sync; no recurring Gentry timer/integration request in inspected client functions. Polling/render-triggered sync/scheduler/webhook/cache behavior still not distinguishable. |
| Is the authenticated backend/API gap closed? | **No, partially closed only:** DOM and shipped-code contracts plus public HTTP responses now exist; no authenticated network trace or backend execution evidence. |

Read-only reconstruction is **substantially exhausted for this session, role and available tools**. Another ordinary UI pass is unlikely to close these technical unknowns. Useful next evidence is authorized backend/source/log material, a redacted authenticated capture from a supported developer surface, another legitimate role and separately approved nonproduction transition tests. REA browser tooling lacked an explicit CDP connection; its single static attempt produced a retained partial summary, without repeated troubleshooting.

## Additional read-only investigation

| Area | Focused evidence needed |
|---|---|
| Integrations | Authorized sync/import logs, cursor/page limits, cutoffs, watermarks, tag-only handoff and late updates; no secrets. |
| Outcomes | Current implementation or authoritative contract for multi-leg selection, chronological precedence, fallback status and pickup return inclusion. |
| Calls | Seven date anomalies, old-value mapping, event dedup/link keys, phone fallback, reason selection and chart cutoff. |
| Product calculations | Meta matching/collisions/zero sales/VAT/currency, daily/full-week boundary, tier velocity/graduation window, inactive progress, restock rounding and minimum batch. |
| Background jobs | Browser versus server triggers, interval, locks/retries/failures and concurrent users. |
| Roles/audit | Support and Owner access, export scope, actor stamping, approval separation and retention; merchant partition if present. |
| Hidden areas | Genuine navigation in other roles for Production, administration, quality, audit and finances. |
| Exports | Cleanup schema and filters; nondefault product/order filter propagation, nulls, encoding and size limits. |

## Controlled experiments left for authorization

An appropriate nonproduction environment is preferred. Any consequential production action requires explicit human authorization.

1. Synthetic confirmation/tag combinations and manual confirmer values: check attribution, timestamps and dispatch guards without customer contact.
2. Synthetic outbound/return/exchange legs in different chronological orders: verify outcome, stage and export parity.
3. Synthetic call imports and first/second NoAnswer followed by answered contact: check deduplication, date parsing, queue membership and actor identity.
4. Sandbox reship approval/rejection and duplicate/failed bookings: verify external effects, eligibility, approval separation and compensation.
5. Synthetic pickup/cleanup payment, collection, cancellation, refund and archive combinations: verify clocks and number impact.
6. Product zero/missing inputs, matching collisions, season boundaries, incoming stock and snapshot overwrite: verify formulas, meaningful validation and audit.
7. Same synthetic operations under Support/Operations/Owner: verify server denial and recorded actors without authorization bypass.

The package substantially covers supplied artifacts and accessible read-only UI. End-to-end confidence requires P0 decisions, integration/backend/other-role evidence and controlled transition tests. Review and correct this reconstruction before a replacement PRD, architecture, technology selection or implementation.
