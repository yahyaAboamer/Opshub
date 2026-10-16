# Future migration risks identified by reconstruction

These are preservation risks and evidence gaps, not a target design or implementation plan. Human reconstruction review comes first.

| Risk | Evidence and potential distortion | Evidence required before migration |
|---|---|---|
| Identity and grain collapse | Order reference, tracking, variant label, product GID and internal ID differ; multiple legs/order and calls/event grain. | Authoritative crosswalk and normalization constraints. |
| Historical incompleteness | Unequal windows, 812 wallet-only IDs, 867 source-only orders, June contradiction and 547 inferred pickups. | Cohort provenance, import scope and explicit exclusions. |
| Financial misstatement | Value proxies, catalogue COGS, inferred prepaid, joined-only fees, missing-to-zero/last-fee rules. | Approved economics, transaction provenance and uncertainty flags. |
| State reinterpretation | Delivered return leg differs from kept order; cancellation can coexist with RTO; handoff differs from booking; blank outcomes. | Current projection and chronological precedence contract. |
| Lost call history | 239 events/224 orders, legacy labels and seven dates before matching order dates. | Preserve vocabulary/time/actor/link provenance and resolve ambiguity. |
| Confirmation misattribution | Hadeer/auto versus Whapi, exact tags/manual values, no confirmation timestamp. | Attribution precedence and event evidence; avoid causal claims. |
| Pickup inference treated as fact | Historical paid/no-courier classification versus live paid waiting. | Explicit physical collection and no-show definitions. |
| Duplicate external consequences | Reship promises Shopify and Bosta writes plus original tag; retries/failures unknown. | Sandbox idempotency, partial-failure and approval tests. |
| Product/stock mismatch | Variant label versus product ID; current versus dated stock; incoming/minimum batch inaccessible. | Crosswalk, inventory source and manual/sync ownership. |
| Incomparable metrics | Shipment-created/Saturday versus placed-order/Monday; differing numerators and partial intervals. | Definition, date basis, denominator and as-of provenance. |
| Unapproved advice/config | Suggested versus assigned tier, graduation window, active defaults needing confirmation. | Owner decisions and exact algorithms including null/edge behavior. |
| Ad allocation drift | Name/keyword matching, generic allocation, VAT and recent revisions. | Collision/zero-sales/currency rules and rebuild watermarks. |
| Access/tenant assumptions | One merchant/session, permission vocabulary and one server redirect but no verified role enforcement or tenancy. | Authorized role/action/export/access/isolation/audit evidence. |
| Client contract mistaken for backend API | Phase 1B verifies Flight/action transport and public function IDs; chunk/action identities varied and one old referenced chunk returned 404. Expected importer feedback was never produced by a test. | Authorized backend/network contracts, importer validation/deduplication and actual response/error evidence. Public function hashes are not stable migration interfaces. |
| Privacy propagation | Historical report script reads a customer name contrary to its promise; exports contain contacts. | Review generated-report inputs and data retention/sharing before use. |
| Capacity/parsing limits | Bounded masters/ranges, four 180-character slots, single-digit quantity and partial SKU flags. | Preserve known scope and test unobserved edges. |
| Time and refresh loss | Export watermark ageing, stripped times, current stock with historical sales, changing rebuild results. | Retain event/source/rebuild times and timezone provenance. |
| Audit/reproduction gaps | Snapshot overwrite, missing narrative inputs, unsupported state update, no immutable audit verified. | Revision and actor provenance; date historical outputs. |
| Operational process loss | Manual quality gates, escalation, review and external Sheets duties may be outside the app. | Current ownership and procedural controls. |
| Missing feature coverage | Product management/reship/cleanup exceed source spec; Production/admin/financial access unknown. | Other-role and controlled workflow inspection. |

Recorded facts, inferred outcomes and missing evidence must stay distinguishable. Historical taxonomy should not be silently replaced by current dropdown values. A recorded resolution/refund is not proof of an executed financial or shipment action. Historical outputs require their date basis and calculation definition.

These findings do not select a schema or improve existing workflows. The next step is human correction and approval of the reconstruction, followed by separately authorized design work.

Phase 1B permission properties and the /orders login redirect narrow the access evidence gap but do not prove server authorization or isolation. Generic refresh/revalidation capability and changing watermarks do not establish a scheduler. Preserve these qualifications when reviewing future migration scope; the technical read-only pass is complete without any implementation.
