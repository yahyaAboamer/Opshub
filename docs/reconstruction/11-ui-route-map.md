# UI route and navigation map

Verified through visible navigation, links, rendered forms and existing records on 13 October 2026. Base URL: https://gentry-ops-production.up.railway.app. Evidence: [live ledger](../../evidence/live/observation-ledger.md). Dynamic paths are templates for observed records; they are not authorization to probe arbitrary IDs.

## Navigation

Global: Gentry Ops, current user Omar, Logout, **Order Performance**, **Product Performance**. Desktop and mobile representations showed the same two areas. Home / showed navigation only.

| Route | Entry / content / coverage |
|---|---|
| `/` | Home inspected; no additional feature panels in current state. |
| `/orders` | Order section dashboard, filters/chart drilldowns/table/export/brief. This-week and all-time inspected. |
| `/orders?…&bucket=…#orders` | Observed cards/stage/outcome/confirmer/age drilldown links. Broad in-transit 47 rows checked. |
| `/orders/lookup` | Lookup navigation; blank and no-match states inspected. |
| `/orders/{internalId}` | Existing record links; four contrasting samples. Order form/call/history/reship fields inspected. |
| `/orders/calls` | Calls navigation; week/all metric views and invariant queue, import/export. |
| `/orders/cleanup` | Cleanup navigation; early/later queues, month view and optional low=1 checked. |
| `/orders/reships` | Reship navigation; empty pending state and four historical links. |
| `/orders/new` | Add order navigation; entire native form read, not submitted. |
| `/reports/delivery?period=…` | Dashboard Delivery brief PDF link; printable HTML with draft/metric/narrative controls. |
| `/export/orders?period=all` | Visible CSV link; downloaded and aggregate-profiled. |
| `/export/calls` | Calls export link; event CSV downloaded/profiled. |
| `/export/cleanup` | Cleanup export href observed; content not downloaded. |
| `/products` | Product section dashboard, filters/date controls/cards/advice/export. |
| `/products/{internalId}` | Existing product links; one full detail, metadata/restock/ads/snapshot/history. |
| `/products/new-tier` | New-Tier Products navigation; all 20 New queue. |
| `/products/seasons` | Seasons navigation; existing/future/All-year states, add/edit/delete controls. |
| `/products/seasons?tag={seasonId}#tag` | Choose its products link; 20 checkboxes/18 assigned. |
| `/products/new` | Add Product navigation; required/optional inputs read. |
| `/products/settings` | Settings navigation; four parameter defaults and approval caveat. |
| `/export/products` | Product export link; selected 5–11 Oct CSV downloaded/profiled; Phase 1B September period also verified. |
| `/reports/products?period=last-month` | Phase 1B: observed Product brief href opened successfully; printable HTML, GET period selector and browser PrintButton. |

## Filter and display behavior

Order period controls: This week, This month, Last month, last 7 days, last 30 days, custom, all; date bounds, channel, confirmer, outcome, city, q and repeat flag. Table max 100 newest records in large cohort; no ordinary page-next/page-number controls observed. Separate Shopify batch search links cover 50 orders each, including 27 batches for 1,339 orders. Their purpose is external Shopify work, not table pagination.

Product periods include daily shortcuts, full-week/month shortcuts, custom weeks/dates and Since June. Dates use Cairo-day labels and minimum 1 June. Filters tier/ROAS-vs-breakeven/stock plus q; sort defaults sales and supports units/net ROAS/days of stock/name. 20 cards, no pagination needed in observed dataset.

Calls period controls affect metrics, not queue. Cleanup month filters and optional tidy toggle change visible categories; export href lacks optional query. Printable brief period selector is narrower than dashboard's. Detailed parameter/date semantics need care when comparing routes.

## Phase 1B delivered-feature discovery

Evidence: [technical ledger](../../evidence/live/phase1b/technical-ledger.md), [browser contracts](../../evidence/live/phase1b/browser-contracts.json), [client chunks](../../evidence/live/phase1b/static-analysis.md).

**VERIFIED:** delivered modules include shared Logo/SideNav/TabNav/ThemeToggle, DateRangePicker (16340), CallSheetUpload (4773) and PrintButton (44026). The upload wrapper names uploadCallSheet; DateRangePicker submits its enclosing form; PrintButton calls browser printing. These identify existing client behaviors, not replacement features.

**VERIFIED metadata:** order tabs carry orders.view / orders.calls / orders.reship / orders.edit as described in [09](09-roles-and-permissions.md). The retained navigation functions render supplied props without a client role filter. No additional Production/admin/business route or meaningful business feature flag was established by these assets. Framework fallbacks, icon names, ARIA roles, library URLs and bot-detection strings were excluded from the business route inventory. Other-role/server coverage remains unresolved.

| Newly discovered destination | Evidence / access classification |
|---|---|
| /reports/products?period=last-month | Access verified through an observed authenticated product-brief link. |
| /login?from=%2Forders | Server redirect from an independent unauthenticated /orders GET. **DISCOVERED, NOT ACCESS-VERIFIED**; destination not visited. |

The original user tab was returned to /orders/cleanup after this pass. No unlinked business routes or arbitrary IDs were probed.

## Empty/error/hidden navigation pass

- Lookup synthetic no-match verified.
- Pending reship approvals empty; upcoming season has no products.
- Paid-pending/unshipped cleanup categories empty in observed snapshot.
- No warn/error console records in bounded inspected window; no global error guarantee.
- Production mentioned in product restock copy but no visible link; its route/access remains unresolved.
- No merchant/user/courier admin, wallet/contribution, audit log or report action history route exposed in current role.
- No route guessing or inaccessible-ID probing occurred. Other-role feature coverage remains open.

Agent-created printable-report tab was temporary; original user tab was preserved. No tab with raw customer output was saved as evidence.
