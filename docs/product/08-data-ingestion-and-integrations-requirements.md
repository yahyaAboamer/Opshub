# OpsHub — data ingestion and integration requirements

**Product requirements, not integration architecture.** Evidence: [Gentry ingestion](../reconstruction/10-data-ingestion-and-background-jobs.md), [integration observations](../reconstruction/08-api-and-integration-observations.md), [identity rules](../domain/02-identities-and-relationships.md), [source mapping](../domain/08-reconstruction-to-canonical-mapping.md). Visible refresh and repeat-import promises do not prove backend execution contracts.

## Named pilot connections and evidence limits

Under OD08/OD09 the initial reconstructed pilot sources are **Shopify** for commerce/products, **Bosta** for courier operations and **Meta** for advertising spend where the merchant uses it. These names come from Phase 1, not a generic integration marketplace. Google Sheets CSV remains a contact-history fallback; Paymob's historical fee assumption is not a verified live payment connection.

The following distinguishes **verified recorded input/UI wording** from **OpsHub MVP requirement** and **unknown provider execution support**. A Gentry field or UI promise does not establish the provider's full action contract. OP01 qualifies the exact merchant accounts/action support; it does not reopen integrated MVP priority.

| ID / source | MUST-HAVE product capability | Evidence / support boundary |
|---|---|---|
| IG01 Shopify commerce | Connect the merchant's supported store; ingest new orders and changes, identifiers/date/channel, business/payment/fulfillment/cancellation assertions, contact/order items and available product/variant bindings; retain tags/confirmation evidence with source/time | Recorded fields, exports and changing markers: L02/L06/L14/L20. Native IDs, complete update scope and manual/tag precedence still need qualification; no fabricated consent time |
| IG02 Shopify core actions | In OpsHub, Admin authorizes supported order cancellation and new linked replacement-order creation; reconcile resulting order reference/state. Where supported and required, annotate original/replacement relationship and confirmed/attempt evidence under explicit role policy | Replacement creation/original annotation are intended UI contract L05/BR18, with four observed links; cleanup cancellation is evidenced workflow guidance L22. Direct cancellation/tag/update contracts are unverified. Required targets need provider qualification; unsupported actions use explicit fallback, never an invented effect |
| IG03 Bosta courier input | Connect supported account; ingest shipment tracking/business reference, purpose/type, current state/source dates, exceptions and reported attempt count; receive/reconcile final outbound delivery/RTO and available reverse/pickup evidence | L14–L18 and source RAW_Bosta verify observations, not all event history. A counter is not a timeline; Delivered reverse leg is not outbound kept/collection proof. Unknown link/purpose/finality stays review |
| IG04 Bosta booking | Admin-authorized supported shipment creation/booking through OpsHub, especially the replacement shipment; retain returned tracking/identifier and reconcile later courier state | L05/BR18 explicitly promise Bosta booking, but execution was not tested. Core pilot requires qualified booking/result round trip. Courier cancellation, rescheduling or return/pickup initiation is not assumed supported; use fallback until evidence establishes each action |
| IG05 Meta spend | For applicable pilot ad accounts, ingest period advertising spend and available ad/account references, names/attribution clues, currency/tax basis and as-of into OpsHub product analysis; retain direct/generic/unallocated classifications | L07/L12/L25 verify Gentry period spend/attribution copy and ROAS arithmetic; retrieval contract, native IDs, tax and collision rules are unverified. Read-spend is the MVP input target; no campaign/budget/ad writes. Unsupported/inaccessible retrieval uses disclosed fallback, not zero spend |
| IG06 Product identity and separately sourced observations | Shopify product/variant/item identity and qualified sales/adjustment/available inventory input; dated stock, cost and margin may instead come from qualified source evidence or attributed Admin-maintained product inputs. Each observation names its actual source/basis/effective or as-of time | L12 includes editable metadata/manual snapshots; L25/L27 show recorded performance/product refresh, not proved Shopify cost/margin retrieval. Cost/margin origin, native variant/line identity and inventory scope remain unverified. Do not relabel merchant inputs as Shopify facts, current stock as dated stock, or observations as a replenishment engine |
| IG07 Courier fee/cost evidence | Retain available provider fee assertions with scope/currency/source/time for context; accept supported statement import when no qualified connection provides them | Historical RAW_Costs establishes wallet/fee observations. Live fee retrieval is unverified. Fees are not a mandatory profit/settlement ledger; missing fee is not zero and component/total views cannot double-count |
| IG08 Contact / pickup evidence | Record contacts in OpsHub; retain approved history import and attributed physical-event evidence when not supplied by connected sources | Google Sheets CSV UI contract L04/L24 unexecuted. External calling is still allowed; embedded dialing/messaging deferred. Payment never proves physical collection |

IG01–IG04 form the required commerce/courier operational loop. IG05/IG06 supply the required product/ROAS capability with available-input qualifications. A pilot cannot satisfy OD08 using a permanently manual commerce/courier core while labeling it integrated. Test supported action contracts/results before release; isolate genuine unsupported operations as fallback exceptions. No current successful provider mutation is claimed by this PRD.

## Connection readiness and freshness

CON01 — Admin connects/authorizes the intended merchant source context and reviews source ownership, capability availability and mappings. Operators may inspect/refresh permitted read evidence without gaining connection configuration or consequential execution rights. Show not configured, ready, limited capability, failed/unavailable and stale/partial states with affected work.

CON02 — Connected new/changed orders, shipments and applicable spend arrive/update without routine user copy/paste. Show last successful receipt, provider as-of/coverage, recent failure and relevant time basis. Refresh/readiness targets are product acceptance values in OP08/OP13; Gentry's ten-minute UI claim is not adopted as a proved SLA or a mechanism.

CON03 — Repeated connected observations cannot create extra orders, contacts, outbound shipments or costs. Corrections preserve revisions/provenance. Source ingest/update alone cannot trigger booking/cancellation/replacement without the separately required Admin decision.

## Input lifecycle

ING01 — Select merchant and source ownership explicitly. Preserve original identifier strings, account/source scope, capture/input provenance and coverage interval. Identical order numbers/tracking/SKU labels in another merchant must never cross-link.

ING02 — Review connection mappings/coverage and preview fallback file fields, date/number/currency interpretation, object grain, likely additions/updates and duplicate/conflict/unmatched counts. Operator uses approved mappings; Merchant Admin reviews changes. Do not infer native uniqueness from a single export.

ING03 — Validate required identity/merchant/format and supported episode constraints before acceptance. Report each rejected/held row with actionable cause and safe row locator; preserve original values. Unclear phone matches cannot choose among orders/customers. Four long item descriptions or multi-digit quantities cannot be silently truncated to Gentry's historical parser limits.

ING04 — Account for every submitted input row as accepted, repeated, rejected or held/unmatched; identify whether one accepted row updates an existing object. A mixed file can accept independent safe rows only when the user sees the exact accepted/rejected scope. Invalid dependent groups are held together rather than leaving an apparently complete order with missing required parts. Failed new ingestion preserves prior accepted data.

ING05 — Re-importing an identical accepted file under the same mapping/source cannot create new orders, shipment episodes, contact attempts or external actions. A source correction is a new observed revision with before/after/provenance, not a duplicate event. Distinct genuinely evidenced contacts remain distinct even when their text/timestamps match. Ambiguous event deduplication is held for review; the MVP supported-contact-import contract needs OP13 approval.

ING06 — Keep contradictory source assertions visible. The approved source selection/manual override determines a displayed working view only for the named concept; it does not destroy alternate claims or fabricate physical/financial events. Importing a cancellation/payment/tag assertion never executes that business action externally.

ING07 — Show received/accepted time, source-reported coverage/as-of, last successful update, last failure and affected population separately. Connected-source freshness follows the qualified product target; manual fallback is labeled with its exception reason and merchant refresh dependence. Do not present fallback receipt as restored connection health.

ING08 — Source gaps, unknown statuses and multiple/repeated/partial historical episodes enter review with their original observations. OD06 remains the supported OpsHub order model; historical reverse legs retain purpose. Do not discard a second leg to satisfy the MVP or invent a replacement identity without evidence.

ING09 — Imported aggregate contact/courier counters remain summaries. No generated attempt chronology, authenticated historical actor or consent timestamp is fabricated. Seven Gentry call-before-order anomalies remain contradictions until source evidence explains them.

ING10 — A sync/file result cannot claim success for unavailable sources. Disconnecting or failing a source leaves last accepted data labeled stale/partial; it does not reset counts to zero or remove unresolved work. Data refresh should update current queue/KPI projections with a traceable new as-of.

## Integrated consequential action boundary

ACT01 — Operator prepares → Admin reviews exact intent and authorizes/initiates in OpsHub → OpsHub performs the supported external action → returned identifier/result and later status are received/reconciled → required work closes only under OD03. Track not started/pending/succeeded/failed/unknown per effect; provider acknowledgement is not physical completion. Record Admin authority and OpsHub execution origin separately from source/recording actor.

ACT02 — Only one current intent may be actionable for the same booking/recovery objective. Competing Admins, repeated submissions, delayed results and recovery cannot authorize duplicate effects. A changed intent requires reapproval. Unknown first effect blocks connected re-execution and manual fallback execution until reconciled; no blind retry/rollback claim. Successful replacement creation plus failed booking retains the known new order and pending booking, not another replacement.

ACT03 — Denial must prevent the connected external action, not merely hide a button. Platform authority never authorizes merchant execution. Reported unauthorized/duplicate effects from independently operated provider accounts remain discrepancies, not retrospectively approved. Native refunds, arbitrary payment changes and unqualified courier operations are not silently added by OD08.

## Required manual fallback

FB01 — Fallback is available for temporary integration outage, provider-unsupported action/input, incomplete onboarding or reviewed safe exception. Show reason, missing capability, current request/result knowledge and responsible actor. Operator may prepare/import approved evidence; consequential external execution and result acceptance remain Admin-controlled.

FB02 — Handover to external execution requires a known not-started intent or a reliably evidenced no-effect result under the qualified action contract. A timeout, failed refresh, missing record or unsupported absence lookup is not proof of nonexecution. Unknown earlier effect remains blocked/open. Safe handover makes the prior path nonactionable and records Admin/reason/negative-evidence basis; capture fallback provider reference/time/outcome. Missing positive result evidence stays unknown. OpsHub cannot prevent independent provider-account activity; fallback must demonstrate correct authority.

FB03 — When a connection recovers, reconcile fallback evidence with connected records without duplicates or overwriting disputes. Show connection restored separately from fallback completion. Imports/exports and off-platform work are not the normal route for an available integrated source.

Provider capability gaps, action eligibility and measurable freshness are qualification/product decisions. API technology, sync architecture, webhooks, queues, credentials handling and infrastructure remain Phase 4; none is selected here.

## Export and historical comparison

EXP01 — Export matches the requested merchant, filters, population, period and as-of. Orders, contact cases/events and shipment populations retain their named grain. Carry original source references, unknown/blank distinctions, relevant definition and caveats. Do not silently export all calls when a period subset was selected.

EXP02 — Operator exports omit direct contact details and free-text contact narratives. Admin contact-bearing export is a separate explicit choice showing affected scope, with audit. Platform exports contain scoped administration/aggregate diagnostics only. See OP12 for retention/distribution policy.

EXP03 — Preserve historical Gentry labels/definition provenance for a future comparison pack. Normalized OpsHub metrics appear alongside documented differences; no requirement to reproduce missing archived narrative inputs or workbook layout. [AC12](11-mvp-acceptance-criteria.md#ac12--legacy-comparison-readiness) defines comparison readiness.

These requirements define user-visible behavior and data trust. They select no interface technology, database, queue, schedule mechanism or implementation.
