# Feature inventory

Evidence IDs below link to the [live ledger](../../evidence/live/observation-ledger.md). “Action visible” does not mean executed. Source-only features are separately scoped.

## Current Order Performance

| Feature / purpose | Inputs, output, interaction and limits |
|---|---|
| Order dashboard, `/orders` — L02, L14 | Placed-date cohort; period/from/to/channel/confirmer/outcome/city/q/repeat filters via GET. Cards and stage/outcome/confirmation charts drill into bucketed records. Table includes order/date/customer/channel/confirmation/outcome/city/value, newest first, max 100 observed; no further table pagination. Search accepts number/name/phone. Bulk Shopify matching links divide50 order names per batch. CSV export and printable brief links. Filters modify view, not data. |
| Lookup, `/orders/lookup` — L03, L19 | Dedicated q search; initial blank, safe no-match empty state verified. Matching-detail path exists from dashboard records. Search permission only observed for current session. |
| Order detail, `/orders/{id}` — L15–L18 | Header placed date/channel/status; tags/confirmation; courier type/state/attempts/exception; customer/contact/address/items present but not retained. Order editing fields, return-contact form, call history and reship request. Samples span RTO, customer return, cancelled dispatch-tag-only, waiting paid pickup. Raw status, operational stage and derived outcome differ. No save or financial operation tested. |
| Calls, `/orders/calls` — L04, L23 | Period controls affect returns/called/reached/reasons/daily chart, not32-entry queue. Queue newest first, orders since 7 Sep, two-NoAnswer removal UI contract. Quick Called done; detail for reasons. Import CSV file picker and button; export calls href independent of period. Current all metric cohort102returns versus 239 exported events. |
| Cleanup, `/orders/cleanup` — L01, L21, L22 | Month filter and optional low-priority view. Queues returned-but-still-sale, stuck courier, paid-pending, unshipped, old pickup, finished-not-archived. Category guidance links to Shopify; archive exposed as tidy operation. Numbers refresh during investigation. Age10+ uses placed date. Export href omits low query; actual exported content not verified. No cleanup action executed. |
| Reships, `/orders/reships` — L05 | Pending approval empty; four historical relationships visible. UI claims approve creates Shopify payment-pending replacement+Bosta booking and original tag. Recipient/items requested on detail; approval eligibility, rejection, duplicate prevention, rollback and finances unknown. |
| Add order, `/orders/new` — L06 | Manual name/date/channel required. Optional value/contact/items/fulfilment/cancellation/confirmer/tags/Bosta boolean, type, state. No items/line entity selector observed. Native required fields verified; uniqueness, type consistency and server validation untested. Form copy says sync not wired despite sync markers. |
| Delivery brief, `/reports/delivery` — L26 | Printable HTML labelled PDF, periods this/last week, this/last month/all. Comparison is preceding equal-length interval in current partial-week example. Draft label, metrics/trend/operational tests, four editable narrative slots, Save as PDF. Printing and narrative persistence unverified. No communications sent. |
| Sync status, section chrome — L14 | New/updated/Bosta-match counters, as-of timestamp, Sync now. Copy says refresh every 10 minutes while section open. Markers changed spontaneously; network/job mechanism and sync-now write behavior not inspected. |

Detail return inputs: contact status NotCalledYet/ResolvedByCall/NoAnswer; conditional reason taxonomy; resolution blank/Refunded/Re-shipped/Rescheduled delivery/Closed-no-resolution; refund blank/Yes/No/Partial; recoverable boolean; caller text; notes. Current dropdown lacks historical EscalatedToOmar and several imported reasons/resolutions. A recording field named Refunded does not prove a payment is issued.

Reship request required recipient name, phone, city, first address line and items; optional note. Existing address/items populate it. UI says COD equals original and Operations approval is required. The form is also visible for a pickup sample; server eligibility remains unresolved.

## Current Product Performance

| Feature / purpose | Inputs, output, interaction and limits |
|---|---|
| Product dashboard, `/products` — L07, L25 | Default previous Monday–Sunday week. Daily/week/month/custom windows since 1 Jun, Cairo-day labels. Tier/ROAS-vs-breakeven/stock filters, name search, sort sales/units/ROAS/stock-days/name.20 products. Cards show units/sales/returns/spend split/net ROAS/ads/stock/advice/order counts. Export28-column CSV. Counts changed with rebuild watermark; later UI agrees export. |
| Product detail, `/products/{id}` — L12 | Internal ID plus Shopify GID; name, assigned tier, margin0–1, lead weeks, unit cost, optional season, ad keyword text. Restock/advice/own ads/weekly history. Edit/save and manually add weekly snapshot; same-week overwrite stated. Current stock is distinct from dated ending stock. One full detail inspected; other product rows checked through dashboard/export. |
| New-tier queue, `/products/new-tier` — L10 |20alphabetic New products; progression against20 order graduation threshold. Suggestions guide manual editing; no automatic tier transition observed. Progress window differs from all-time/display on inactive cards. |
| Seasons, `/products/seasons` — L09, L27 | Name/start/end required; date-driven Now/Upcoming; membership counts and All year remainder. Edit/delete, checkbox assignment view reached by tag query. Untick→All year; tick assigned elsewhere→move. No save/delete. Future season empty state verified. |
| Add product, `/products/new` — L11 | Shopify product ID/name required; tier, margin, lead time, unit cost. Native bounds inspected; duplication, negative lead/cost and GID validation untested. |
| Settings, `/products/settings` — L08 | Baseline 2.8/scaling 3.8 breakeven multipliers, New 20 order threshold, Baseline spend ratio .15. UI explicitly asks owner confirmation of defaults. Saving/influence on recomputation untested. |
| Shopify product sync — L27 |0new/20updated at18:53, earlier marker differs. Product section advertises10-minute refresh while open. Inventory provenance/incoming-stock update job unresolved. |
| Production reference — L12 | Incoming stock/minimum-batch copy mentions Production; no route/nav in available session. Feature existence/access is UNRESOLVED, not declared absent. |

Product manual snapshot fields: required weekStart, unitsSold, grossSales, endingStock, adSpend; optional discounts, refunds, cumulativeOrderCount. Displayed history computes net cash, sell-through and net ROAS. Input names describe a contract; negative/missing-value enforcement and overwrites were not tested.

## Historical artifact-only feature families

| Family | Source evidence / live coverage |
|---|---|
| Financial contribution / wallet cost joins / gateway charge | DATA_Master, Config, Owner SOP; no corresponding live wallet/contribution page exposed. |
| Data-quality report eligibility | Data_Quality + Ops SOP + weekly skill; no equivalent live CLEAN/CAUTION/BLOCKED gate visible. |
| Product-size, city-zone, cause-owner, recovery and attempts analysis | Historical workbook sheets; current Order UI has some cause/city/attempt observations but not full equivalent matrices. |
| Rate-card scenarios / COD-prepaid comparison | Config and audit; dormant OUT OF USE model where actual fees exist; no live scenario controls found. |
| Google Sheets taxonomy migration and dependent validation | Upgrade pack + Apps Script; current CSV import exposes a bridge, deployment of Sheets code unverified. |
| Action carry-over briefs and sidecars | Weekly skill/references/actions.py; no action JSON files supplied or equivalent persistent live task entity observed. |
| Monthly DOCX review pipeline | Delivery extract/build_report/state + archived report; not the current HTML delivery brief implementation. |

No visible merchant management, user administration, audit-log page, courier setup or general import configuration was found in this role. That is a coverage limit, not proof those features cannot exist.
