# OpsHub — API and consistency boundaries

**Recommendation:** same-origin REST/JSON application API, internal typed module calls, provider-specific protocols inside adapters. [ADR011](adr/ADR-011-application-interface.md). An external Shopify GraphQL adapter does not require a GraphQL product API.

## Interface alternatives

| Approach | Evaluation |
|---|---|
| Server-rendered actions | Simple for forms, but session/action routing and cache invalidation can hide durable action semantics; no SEO/SSR need in authenticated pilot |
| REST | Explicit resources/commands, ordinary HTTP/session controls, durable202 operation/status and straightforward contract tests; recommended |
| GraphQL | Flexible selection, but field-level authorization/query complexity and mutation semantics add burden without demonstrated client need |
| Type-safe RPC | Good local TypeScript ergonomics; can obscure durable domain operation/versioning boundaries; use typed internal calls and generated REST DTO/client types rather than a second public interface |

One API authority boundary serves both surfaces through distinct `/api/v1/merchants/{merchant}/...` and `/api/v1/platform/...` namespaces. Webhook/OIDC callback endpoints have their own authenticity protocol, not ordinary browser session grants. No general provider proxy or arbitrary SQL/report endpoint. Persist external action status resources rather than holding a browser request open for all provider effects.

## Request contract

Authenticate → build checked authority/context → apply service/capability rule → validate input/ownership → load current subject/version → execute module transaction → append audit/durable work → return result. DTO schemas reject unknown sensitive fields, invalid quantities/currency/IDs and overlong input; compile-time TypeScript does not validate network input. Actor/tenant/approval/provider-success fields are derived server-side. Server authorization covers reads, filters, imports, exports, direct IDs, action requests, result acceptance and worker execution.

Consequential requests include client idempotency key, subject/intent expected version and explicit side-effect flags. Identical key/payload replays existing operation; mismatched payload or competing objective returns conflict. Approval references exact intent version/hash. The command response is202 plus operation ID/status when provider work remains pending;200 for accepted local read/update. No200 promise of completed booking merely because a request was queued.

Errors use stable code, safe explanation, correlation ID, permitted field errors, current accessible version and retry classification. Suggested codes: `UNAUTHENTICATED`, `FORBIDDEN`, `NOT_FOUND`, `VALIDATION_FAILED`, `VERSION_CONFLICT`, `OBJECTIVE_RESERVED`, `OUTCOME_UNKNOWN`, `CAPABILITY_UNAVAILABLE`, `SOURCE_INCOMPLETE`, `RATE_DEFERRED`. HTTP401/403/404/409/422/429/503 map to appropriate application categories. Avoid provider raw body/contact disclosure. `retryable` means the indicated **safe operation**, never generic permission to replay a mutation.

Use cursor pagination with stable `(sort_value,id)` order, max page/interval/complexity bounds, validated filter enums and tenant indexes. Search is tenant-scoped; free-text narratives are rendered as text. Responses identify current input/projection version and freshness. API v1 allows additive changes; breaking changes use explicit version/transition and reviewed contract fixtures. No complete OpenAPI schema is generated here; a later build can derive client types/spec from the same validated DTOs.

## Exports

Export request persists tenant, requester/membership, contact-free versus Admin contact-bearing scope, exact filters/grain/window, definition and requested as-of/input revision. Freeze contributors/field interpretation versions before queued generation; reconstruct from retained immutable revisions or an authorized private snapshot. Unsupported historical as-of requests fail explicitly; workers cannot substitute current state. A generated export lists the same scope/counts/nulls/caveats as its result/drill-down. Recheck current requester/membership/service/export permission at generation and download; suspended/revoked privilege blocks delivery even if the file exists.

Private file reference is a run identity, not permission. Customer-bearing downloads stream through an authenticated endpoint with `no-store`, attachment disposition and no loggable signed URL. Contact-free downloads can use short-lived authorized URLs only after current checks. Formula-injection escaping and sensitivity validation apply to every CSV field, including imported narrative and leading whitespace/control characters. Files are bounded/expire per approved policy; failed generation leaves no public partial export. [11](11-audit-provenance-and-privacy.md).

## Concurrency matrix

| Situation | Boundary / control |
|---|---|
| Two Admin approvals/new keys | Lock stable objective, unique current-intent/effect reservation, expected intent version; one executable result |
| Membership/service suspension during action | Serialize dispatch transition with authority/service versions; changes before ExecutionStarted block. After dispatch, preserve in-flight result and stop later unstarted effects |
| Duplicate webhook/repeated provider event | Unique receipt plus object/version interpretation dedup; page/inbox commit atomic; no generated extra object/contact/effect |
| Late event/competing source assertions | Append observation; compare provider version/effective time under reviewed concept policy; current selection can remain unchanged/conflicted; not arrival-order wins |
| User correction during sync | Expected field/entity revision; append correction; sync retains competing assertion. Interpretation transaction recomputes under OP10 policy; unstarted effect approvals invalidate on material changes |
| Replacement creation succeeds/booking fails | Per-effect durable boundary; persist linked new Order before dependent booking. Resume/review existing booking objective, never repeat creation |
| Job retries | Handler identity/version/claim, idempotent safe work. Started write becomes read reconciliation; lease expiry cannot resend |
| Stale browser read before consequential action | Require expected versions; re-read source freshness/dependencies at approval and dispatch; changed recipient/items/payment/eligibility requires review |
| Contact concurrency/reopen | Atomic pre-call Start contact reserves one eligible actor/slot; held/unknown slot cannot expire into extra allowance. Separate evidence endpoint records actual/violating calls without authorizing them; same case/objective on reopen |
| Last active Admin removal | Lock merchant admin root and membership state; retain/recover a verified Admin before change commits |
| Projection/drill/export versus concurrent sync | Snapshot tenant revision/definition/policy/evidence; publish generation atomically; result and contributors belong to same generation |

Use optimistic version checks for ordinary edits and short row locks for scarce reservations/counters/last-Admin. Deadlocks/serialization conflicts may retry **local transactions before external dispatch** under stable operation identity. Database locks are not held across provider I/O. Multi-effect workflows have durable local steps and reconciled external results, not distributed transactions or automatic compensation.
