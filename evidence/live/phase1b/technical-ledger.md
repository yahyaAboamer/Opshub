# Phase 1B technical observation ledger

Focused read-only pass on 13 October 2026. The accepted reconstruction remains the baseline.

Evidence: [browser contracts](browser-contracts.json), [public HTTP observations](public-http-observations.json), [delivered-client analysis and byte locators](static-analysis.md), [structured static analysis](static-analysis.json), [product export profile](product-export-profile.json), [partial REA summary](rea-partial-summary.json).

## Collection and limits

**VERIFIED:** authenticated UI/DOM observations covered Order Performance and its Last month filter, an existing order, Calls, Cleanup, Product Performance and its Last month preset, an existing product, Seasons and a product printable report. A September product CSV downloaded successfully. The original tab was restored to Cleanup.

Inline Flight import rows and public server-reference identities were read from already-delivered documents. Only control names/types, validation attributes, navigation metadata and function identities were retained. No customer field values, dynamic record IDs, raw Flight trees or bound arguments were saved.

Independent HTTP GETs without browser credentials covered 14 exact DOM-observed chunk URLs: 13 successful JS bodies totaling 607,054 bytes, and one 404 with body discarded. These are separate public HTTP observations, not an authenticated browser request trace. A single unauthenticated GET of the already-known /orders returned 307, Location /login?from=%2Forders, without Set-Cookie. Its body was discarded; login was not visited.

**UNRESOLVED:** authenticated request methods/headers/statuses/bodies, navigation versus prefetch traffic, server responses to writes, upstream integrations and background requests.

The CUA browser exposes DOM and console observation but no request/response listener or explicit CDP endpoint. Read-only DOM evaluation did not expose performance resource entries. REA browser inspection requires an explicit supported loopback CDP endpoint, absent here; no guessed ports or alternate sessions were used. REA static analysis was attempted once on the initial nine assets and timed out with retained partial evidence. Its summary was recovered once, covering six parsed scripts and an incomplete graph. This REA snapshot predates the four later retained assets; independent static review covers all 13 retained files.

T01–T05 lack precise capture times; their chronological order is preserved. T06–T13 have UTC times. Displayed Cairo sync/rebuild markers are data timestamps, not capture timestamps.

## Read contracts

For every UI row below, HTTP status is unknown. Native form methods and hrefs establish rendered intent, not packet capture. All navigation results were checked in the authenticated UI.

| Observation | Trigger / path | Method and query evidence | Response or output shape |
|---|---|---|---|
| T01–T02 | Original Cleanup; visible Order Performance link → /orders | Navigation method uncaptured; filter form GET. | Dashboard, markers and chunks. Initial Flight present; inline imports absent immediately after client navigation. This does not prove no RSC request occurred. |
| T03 | Last month + Apply → /orders?period=last-month&from=&to=&channel=&confirmedBy=&outcome=&city=&q= | Native GET; repeat also a control. Empty values preserved; unchecked repeat absent. Expected body: none. | September dashboard, inline Flight and changed marker. |
| T04 | Existing linked order → /orders/{recordId} | Navigation method uncaptured; no ID enumeration. | Detail/history and bound action forms. |
| T05/T12 | Calls → /orders/calls | GET period; GET /orders/lookup with q. | Metrics/queue, upload, 32 pairs of Called done/No answer POST forms. |
| T11 | Revisit /orders/cleanup | GET month form; /export/cleanup link. | Categories and Shopify links; external cleanup untouched. |
| T06/T07 | Products; Last month → /products?period=last-month&tier=&roas=&stock=&q=&sort= | Enclosing GET form; DateRangePicker requestSubmit. Preset disables from/to inputs and supplies period. | September dates/cards; CSV/report hrefs carry period=last-month. |
| T08 | Existing linked product → /products/{recordId} | Navigation method uncaptured. | Advice/history and edit/snapshot POST forms. |
| T09 | /products/seasons | Navigation method uncaptured. | Season lists and add/edit/delete POST forms. |
| T10 | Observed /reports/products?period=last-month | Show GET form with period. | Printable HTML, grey edit areas and PrintButton; printing not invoked. |
| T13 | Filtered export → /export/products?period=last-month | GET link intent; actual method/headers/status uncaptured. | CSV: 20 rows, 28 columns, 1–30 September, 385 units and 297,500 EGP gross sales. Other filters untested. |

## Unsubmitted action wiring

**VERIFIED rendered/static structure:** native POST forms have empty action attributes and React $ACTION_ID_* or $ACTION_REF_* / $ACTION_*:* marker names. Flight references identify public functions and whether bound arguments exist. Bound values were not extracted or retained. Source names are unknown except uploadCallSheet.

| Form / component | Field or broad argument shape | Apparent public reference |
|---|---|---|
| Order Save | channel, customerName, customerPhone, fulfillmentStatus, cancelledAt, confirmedBy, tags, bostaSynced, bostaType, bostaDeliveryState | T04: 6077f8cd4a3a403054c5762369de64a6a2f701a1d1; bound. |
| Save call | callStatus, reasonCategory, resolution, refundIssued, recoverable, calledBy, notes | T04: 60e75825357fc55459ab9d0109f6cd5d54173eb2de; bound. refundIssued does not prove financial execution. |
| Request reship | receiverName, phone, city, firstLine, secondLine, note, items | T04: 604efdb47f9a439868c48ee98735f0663376361d3b; bound. receiverName/phone/city/firstLine/items native required. |
| Called done / No answer | No editable fields; record/status context apparently bound | T05: same 70e2ace4747fb7a1f777530fe2f0b9c4242afb539b for both; bound contents unknown. |
| Import calls | useActionState prior state + FormData with file | T12 + APP10/S42: 603a2551faaf2a276b438c3b70de362ad8e990c011, symbol uploadCallSheet. No import. |
| Product Save / Save snapshot | Metadata versus weekly numbers; fields in JSON | T08 bound pair 60aa4fe61835ec8da955b94805046baf2898e4dc1b and 60860b997290d55d5ed87e563a8ec545e8feb3944f; mapping to individual forms unresolved. |
| Add / Save season | name, startDate, endDate, all native required | T09 add 405e415dc9cd0ab95ebd1ddb45defee9ce3e3da313 unbound; edit 609e1aeac17bb0343a895afec5756de5c720feb164 bound. |
| Delete season | No editable fields; season context bound | T09 extra bound 40233347097e60f56c578aca763951656b0038ebd4; group correspondence supported, button-child mapping not fully resolved. |
| Sync now / Logout | No editable fields; unbound references | IDs vary across observations/pages; examples in JSON. No clicks or effects observed. |

**VERIFIED client expectation, not actual response:** CallSheetUpload displays optional error and result with added, alreadyThere, noCallStatus and unmatched. Preview caps unmatched at 15; Import disables while pending. No client CSV parser/schema/size validator found in this component. Its .csv,text/csv accept attribute is a chooser hint. Server validation, matching and deduplication remain unverified.

## Framework, routes and permissions

**VERIFIED shipped code:** Next App Router declaration window.next={version:"16.3.5",appDir:!0}; React/DOM 19.3.0-canary-cbb046ab-20260731. These are delivered declarations, not a backend lockfile or deployment inventory.

Generic code supports Flight GET (rsc, next-router-state-tree, _rsc) and enhanced action POST to current canonical URL (next-action, encoded arguments, router-state metadata). Response branches handle text/x-component, action/Flight data, redirects and revalidation. These are static capabilities, not observed authenticated requests/status guarantees. No stable REST or Gentry JSON API was reconstructed.

**VERIFIED metadata:** /orders and /orders/cleanup carry orders.view; Calls orders.calls; Reships orders.reship; Add Order orders.edit. Lookup and sampled product links lack a permission value. Shared client navigation renders supplied items without a role predicate. Server authorization is unknown; missing metadata does not make a route public.

New access-verified route relative to baseline map: /reports/products?period=last-month, from an observed link. **DISCOVERED, NOT ACCESS-VERIFIED:** /login?from=%2Forders, from the unauthenticated redirect. No additional Production/admin/business route was established. Framework fallbacks, ARIA roles, icons, bot strings and library URLs were excluded.

## Background and discrepancies

Order marker changed 19:15→19:47; products 19:15→19:56; product dashboard rebuild stayed 18:39 before report showed 19:57. No manual Sync now. The UI still claims ten-minute refresh while section open.

Retained Gentry navigation/date/print/upload functions contain no recurring setInterval or integration request. Generic router refresh/revalidation exists; PrintButton's 400 ms timeout is one-shot printing. **UNRESOLVED:** polling, lazy/render-triggered sync, scheduler, webhooks, integration polling, locks/retries and cache freshness. Bounded client absence does not rule out server/unseen code.

Earlier Calls referenced 1kudf3dkhdpbd.js; its exact public GET returned 404. One fresh Calls navigation referenced 1t_el1w5uiobt.js, which returned 200. Shared chunks/action IDs also differed across observations. Cause is unresolved; deployment chronology is not established. These function IDs/assets are snapshot evidence, not durable integration contracts.

## Closure assessment

The technical gap is partially closed: framework/protocol, DOM contracts, named importer/expected feedback, permission metadata, one unauthenticated route guard and one nondefault export now have evidence. Authenticated traffic, backend execution and upstream behavior remain unverified.

Read-only investigation is substantially exhausted for the current role/tools. Further useful closure needs authorized backend/log evidence, a redacted authenticated capture on a supported developer surface, another legitimate role or separately approved nonproduction experiments. No PRD, target architecture, technology selection or implementation follows.

