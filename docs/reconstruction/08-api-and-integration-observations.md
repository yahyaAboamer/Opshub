# API and integration observations

Evidence: [live ledger](../../evidence/live/observation-ledger.md), [Phase 1B technical ledger](../../evidence/live/phase1b/technical-ledger.md), [sanitized browser contracts](../../evidence/live/phase1b/browser-contracts.json), [delivered-client analysis](../../evidence/live/phase1b/static-analysis.md), [source static script map](../../evidence/artifacts/text/static-script-map.json), [source script analysis](../../evidence/artifacts/text/nonworkbook-analysis.md).

## Inspection boundary

Navigation, safe filters, rendered forms, inline Flight metadata, already-delivered client modules and CSV outputs were inspected. Phase 1B adds independent unauthenticated HTTP observations of exact observed public asset URLs and one known protected route. No authenticated browser request/response trace or verified backend execution contract was captured. The browser exposed no network listener or explicit CDP endpoint; REA browser tools require that endpoint. REA static inspection returned retained partial evidence, recovered once; independent static review covered all 13 saved assets. No guessed endpoints/ports, arbitrary IDs, session extraction or authentication bypass were attempted.

**VERIFIED delivered implementation:** inline self.__next_f.push data, module imports, React server references and the shipped Next App Router declaration (16.3.5); React/DOM declare 19.3.0-canary-cbb046ab-20260731. These are declarations in captured client bytes, not a backend lockfile, database, deployment topology or stable public API. Native POST/action markers do not establish REST endpoints.

## Observed read interfaces

Base: https://gentry-ops-production.up.railway.app.

| Interface | Observed contract / parameters / limits |
|---|---|
| `/orders` | GET period, from, to, channel, confirmedBy, outcome, city, q, repeat and bucket filters observed in controls/links. Bucket examples stage/outcome/confirmer and ageing drilldowns; fragment #orders directs table. Exact parameter values should be taken from current controls rather than invented. |
| `/orders/lookup` | GET q search accepts order number, phone or name. No-match state verified. |
| `/orders/calls` | Period changes metric cohort; queue remains separate. Export link carries no period query. |
| `/orders/cleanup` | Month view and low=1 optional category. Export link omits low=1; content equivalence unverified. |
| `/products` | Date/period, tier, ROAS, stock, q and sort controls. Last month preset submits the enclosing native GET form; resulting URL period=last-month with empty tier/roas/stock/q/sort. Client disables from/to inputs for preset submission. Default previous-week and September export periods verified; other filter propagation untested. |
| `/products/seasons?tag={id}#tag` | Opens membership chooser for observed season internal ID. Read-only inspection confirmed 20 checkboxes. |
| `/reports/delivery?period=this-week` | Printable HTML rather than direct PDF response. Save-as-PDF action exposed; not executed. |
| `/reports/products?period=last-month` | Product-brief link opened successfully; printable HTML, GET period selector and client PrintButton. Delivered button calls window.print; browser PDF save was not invoked. |
| `/export/orders?period=all` | Successful CSV: 15 columns, 1,339 rows. Current outcome blanks/status fallbacks differ from dashboard. |
| `/export/calls` | Successful CSV: 11 columns, 239 event rows. No selected dashboard period in href. |
| `/export/products` | Successful CSV: 28 columns, 20 rows for 5–11 Oct; Phase 1B period=last-month also returns 20 rows for 1–30 Sept (385 units/297,500 EGP gross sales). Estimated-spend terminology differs from page's Meta incl VAT wording. |
| `/export/cleanup` | Link observed only; download/output schema not verified. |

Exports were obtained through visible UI, then profiled locally without retaining raw contacts in evidence. This is verified output behavior at inspection time, not proof of API versioning, authentication policy or stable serialization guarantees.

## Observed write interfaces — not executed

Order add/edit/contact/reship, season add/edit/delete/assign, product add/edit/snapshot, settings, call import, quick Called done and Sync now expose POST forms. Required and optional field sets are recorded in [feature inventory](02-feature-inventory.md). No server response/error, transaction boundary, retry policy, CSRF validation, validation error shape or mutation permission was observed.

The UI promises these external effects:

| Integration | Verified statement / observation | Unresolved implementation |
|---|---|---|
| Shopify orders | Orders/tags/payment/fulfilment fields; external search links; changing sync timestamps/counters. | Webhook versus polling, pagination, import cutoff, tag/manual-field precedence, cancellation/refund/archival propagation and credentials. |
| Bosta | Order summary state/type/attempts/exception; sync match count; request-approval shipment promise. | Multi-leg matching, newest/terminal precedence, pagination, retry/failure handling, booking idempotency and status mapping. |
| Shopify products | Product GID, current stock and 20 updated marker. | Variant stock aggregation, manual metadata preservation, deletion/renaming and cost/margin origin. |
| Meta ads | Page attribution says spend incl VAT, name/keyword match and generic allocation; recent revisions. | API scope, VAT rate, attribution/collision, currency, daily versus weekly consistency and late adjustments. |
| Google Sheets calls | CSV import matches tracking in order ID or phone; entire-file repeat-safety claim. | Actual deployed Sheet script, importer schema mapping/dedup key, caller/time migration and order linkage. |
| Paymob | Historical Config 1.7% assumption and inferred prepaid cost. | No current live gateway integration/transaction data or pricing verified. |
| Railway | Application is served at Railway hostname. | No account/service/configuration access or backend infrastructure inspection performed. |

## Phase 1B transport and action evidence

The following categories must remain separate. Full path/query/trigger/action/field evidence is in the [technical ledger](../../evidence/live/phase1b/technical-ledger.md) and [browser JSON](../../evidence/live/phase1b/browser-contracts.json).

| Evidence class | Verified structure / broad shape | Limit |
|---|---|---|
| Actual independent HTTP | 14 GETs of exact observed chunk paths: 13 returned 200 JavaScript with public immutable cache headers; one earlier CallSheetUpload asset returned 404 text/plain, body discarded. No payload/authentication copied. | Separate from authenticated browser traffic. Later fresh Calls exposed a different chunk, fetched 200. Cause unresolved. |
| Actual unauthenticated route response | GET /orders, no payload → 307 Location /login?from=%2Forders; no Set-Cookie, body discarded. | Proves protection of this request only. Login not visited; session mechanism/RBAC unknown. |
| Rendered GET intent | Orders/products safe filters, Calls period/lookup, Cleanup month and report period forms; results visibly verified. Bodies expected absent for native GET; output is rendered UI or downloaded CSV. | Actual browser method/status/headers not captured. Inline Flight rows do not substitute for a network trace. |
| Shipped Flight machinery | Generic GET support with rsc, next-router-state-tree and _rsc; text/x-component codec and navigation/cache logic. | Static capability; no evidence which requests were prefetch/navigation/revalidation. |
| Shipped action machinery | Generic enhanced POST to current canonical URL with next-action and router-state metadata; encoded argument sequence. Response code handles action result/Flight, redirect and revalidation indicators. | Neither a durable endpoint nor an observed Gentry request/response. Native form fallback and enhanced submission may encode differently. |
| Unsubmitted bound forms | Order Save, Save call, Request reship, quick Called done/No answer, product edit/snapshot and season actions have public reference IDs and bound metadata. Field names/validation captured; bound values omitted. | No writes, response/error schemas, enforcement, transaction/retry or external effects verified. Product's two bound IDs were not individually mapped to its two forms. |

**VERIFIED client-specific action:** CallSheetUpload creates the public reference 603a2551faaf2a276b438c3b70de362ad8e990c011 under symbol uploadCallSheet. It uses useActionState with an initial empty state and a file FormData field. Client feedback expects optional error/result; result uses added, alreadyThere, noCallStatus and unmatched, displaying at most 15 unmatched entries. This is an expected client feedback shape, not an observed successful import response. The Import button disables while pending; .csv,text/csv is a chooser hint. Server CSV validation, matching, deduplication, atomicity and authorization remain unknown.

Action reference IDs are public function identities, not credentials, and varied across sampled pages/renders. They were not invoked or replayed. No integration connector endpoint or upstream authenticated payload was found in retained application functions. Permission props and route discovery are recorded in [09](09-roles-and-permissions.md) and [11](11-ui-route-map.md).

## Historical script interfaces

- Weekly extractor finds one main nonbackup/nonlock workbook, copies to temporary location, recalculates with LibreOffice, then reads fixed sheet coordinates into JSON. No original write.
- Monthly extractor similarly recalculates a copy, reads raw columns and report state, emits metrics. Builder combines metrics and nine authored narrative slots into DOCX/chart.
- Actions helper writes JSON sidecars; presentation helpers generate documents, not communications.
- Apps Script manual onEdit/backfill adjusts return-cause dropdowns only. It does not book shipments, refund money or send customer messages.

No HTTP client, deployed job/API handler, integration secret, tenancy partition or live authorization implementation was established from these supplied scripts.
