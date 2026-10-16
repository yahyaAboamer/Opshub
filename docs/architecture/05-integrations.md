# OpsHub — integration architecture

**Proposed integration framework**, implementing OD08/OD09 and [IG01–IG08/CON/ING/FB](../product/08-data-ingestion-and-integrations-requirements.md). Official capability verification and account limitations are in [18](18-provider-capability-review.md). Endpoint existence is not pilot readiness. [ADR005](adr/ADR-005-integration-pattern.md).

## Separate three lanes

| Lane | Contract |
|---|---|
| Inbound synchronization | Qualified provider reads/events → durable receipt/observation → mapped assertions/current interpretation → projections; never sends business mutations |
| Outbound actions | Exact Admin-authorized immutable effect → current connection/eligibility check → one controlled request → independent result evidence; only06's coordinator may call mutating adapters |
| Result reconciliation | Safe reads/callbacks/approved manual evidence → matching existing intent/result and conflict review; never turns missing result into automatic mutation retry |

Adapters expose typed reads, mapped observation envelopes, qualified mutation descriptors and reconciliation probes. Each capability has API/schema version, enabled state, required scope, accepted positive/negative evidence, request correlation support and retry class. Business modules own consent/finality/source-authority decisions, not adapters. Unknown fields/states are retained as assertions and placed under review; provider vocabulary does not become a universal OpsHub lifecycle.

## Provider mechanisms

| Source | Normal inbound path | Reconciliation / outbound / fallback |
|---|---|---|
| Shopify | Initial paginated scoped order/product/variant reads; subscribed order/product and relevant cancellation/refund changes via verified HTTPS webhooks | Scheduled overlapping updated-time read sweep and targeted reads. Admin-qualified cancellation/new order/annotation effects. Historical read coverage restricted by actual scopes. Approved file/off-platform fallback only for stated exception |
| Bosta | Initial/periodic authenticated shipment retrieval qualified for the account; callbacks as low-latency hints | Callback authenticity and current-object read corroboration; polling open/unknown objects and periodic account reconciliation where supported. Admin booking only after pilot contract qualification. Cancellation/return initiation/business pickup are individually gated, not assumed mandatory automation |
| Meta | Scheduled account/ad period Insights reads; async report retrieval where qualified volume needs it | Re-fetch recent windows and requested closed periods with revision history; no spend-finality SLA assumed. Admin-approved direct/generic/unallocated mapping; no advertising writes. Disclosed spend import if access temporarily unavailable/unqualified |
| Manual files/attestations | Reviewed source scope, mapping, preview and accept | Retain raw locator/actor, row/group disposition and exception reason; reconcile back into the same provider namespace where identity is established |

Shopify webhooks are unordered and reconciliation is recommended in official documentation; OpsHub therefore persists receipts and performs read sweeps rather than relying on an event-only feed. [Official webhook guidance](https://shopify.dev/docs/apps/build/webhooks). Qualify distribution-specific mandatory privacy topics and app-uninstall behavior alongside ordinary sync topics. Verified privacy receipts enter the bounded data-request/redaction workflow in 11; uninstall revokes/blocks new connector work while existing uncertain effects remain under reconciliation. Bosta status callbacks are documented; their account delivery/authentication reliability is qualified separately in 18. No provider may set the tenant from an untrusted payload.

## Connection, ownership and credential boundaries

Persist connection state: not configured, authorization pending, validating, ready, limited, degraded, expired/revoked, disabled. Track readiness by capability and source coverage separately from overall connection status. `ready` never means complete history, confirmed final outcome or authorized execution. Member Admin verifies ownership/native account binding; platform sees redacted administrative readiness only.

Tokens/API keys are encrypted, versioned and referenced in `credential_versions`; never placed in jobs/browser/logs/docs. Use established envelope/sealed-box encryption: web connection setup can encrypt with a public key, worker alone receives the protected decryption key. Store connection/merchant/version binding inside authenticated encrypted contents and verify after decryption. Inbound signature/auth verification keys have a separate restricted ingress boundary. Keys live in environment secret management with documented rotation/recovery; old decrypt keys stay available only while needed to rotate or reconcile. Platform APIs cannot decrypt secrets. [Sealed-box primitive](https://doc.libsodium.org/public-key_cryptography/sealed_boxes) supports recipient public-key encryption; this is an implementation recommendation, not homemade cryptography.

Use least provider privilege: Bosta read key for ingestion and read/write for booking where feasible; no Full key by default. Shopify granted scopes separate from OpsHub authority; offline worker access is required for relevant order creation. Meta authorization is read-only under the account/app's qualified permission process. Token renewal serializes per connection and atomically saves the pair/version; expired/revoked state blocks affected work and requests Admin reconnection. An IdP session is not a provider credential.

## Inbox, checkpoint and replay

Authenticate ingress before durable tenant receipt. Unique provider delivery identity where available deduplicates receipts; retain separate transport delivery and logical provider event identities. Without a guaranteed event ID, compare source object/version/basis to deduplicate a repeated observation, not all identical real events. Bosta callbacks with unknown ordering/auth support cause targeted safe reads; they cannot alone authorize effects or close physical collection.

Each sync run stores connection, requested/observed coverage, page cursor, mapping/schema version, started/completed times, dispositions and failure. Commit an accepted page/group and durable projection work before checkpoint advancement. Use a fixed upper-bound timestamp plus overlap/lookback for updated-time sweeps; do not advance to wall clock merely because one page succeeded. Repetition is safe by native object binding/revision identity. Unknown absence/deletion in incomplete listings is not deletion or zero activity. Metadata-only unsupported observations remain reviewable.

Replay of verified inbound observations is permitted under the recorded mapping revision or a new reviewed mapping run; it cannot recreate contacts from counters, execute effects or erase manual corrections. Parser/schema changes require versioned fixtures and compatibility review. Snapshot source data is not an event timeline. Selected working interpretations follow OP10's concept-source policy, not arrival order.

## Rates, retries and outages

Per-account/provider budgets coordinate all worker calls in Postgres so multiple workers cannot each spend a full quota. Reserve capacity for reconciliation before large backfills. Shopify uses returned calculated-cost/throttle information; Bosta/Meta limits and headers require account qualification, so initial concurrency/poll intervals are conservative configurable proposals, not asserted quotas. [Shopify rate documentation](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits).

Reads: bounded exponential backoff with jitter, provider retry advice when available, and cursor-safe resume; exhausted/auth/schema errors become visible problem work. Mutations: adapter error classification enters06; generic SDK/HTTP automatic write retries must be disabled. A429/5xx is not automatically no-effect unless the exact response contract establishes it. Circuit-open state defers new dispatch; unstarted approved actions are revalidated later. Already-started effects retain unknown/succeeded/no-effect evidence, not outage-derived failure.

Show last receipt, accepted/source-as-of/coverage, last successful sync and latest problem separately. Preserve last accepted values while stale/partial. Manual receipt does not restore connection health. Daily budgets/rate adaptation prevent one tenant's large backfill starving ordinary reads of another. Dead letters contain safe IDs/category/revision, not raw secrets/customer payloads.

## Integration qualification before pilot

Verify Shopify/Bosta account ownership, native IDs, supported scopes/response/error/pagination, callback authentication, exact create result identity and mutation side effects in controlled nonproduction contexts. Inspect whether an existing Shopify↔Bosta connector automatically books newly created orders; choose **one normal booking authority** before enabling OpsHub booking. Disable or exclude competing auto-booking under an authorized future account setup, and reconcile already-created consignments. OpsHub cannot prevent independent manual/provider-system activity. Do not present local locks as a guarantee over those actors.

Qualify Meta period/currency/tax/timezone/reporting parameters and real product links. If the required operational core cannot pass AC14, pilot integrated readiness is blocked; fallback cannot disguise a permanently manual core. No provider connection or experiment is executed in Phase 4.
