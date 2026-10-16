# Canonical entity catalog

Use the [evidence/treatment labels](00-canonical-domain-overview.md#evidence-and-semantic-labels). All canonical identities and lifecycles below are semantic proposals unless explicitly identified as scoped historical/current evidence. Identity means a stable business reference, not a SQL type or key implementation. Unresolved fields are not mandatory migration prerequisites; retain missingness. Relationship cardinalities and evidence limits are authoritative in [02](02-identities-and-relationships.md); invariants Ixx resolve to [05](05-domain-invariants.md); PDxx to [07](07-policy-decision-register.md).

## Shared entity contract

Every merchant-owned entity carries its Merchant/Workspace identity, canonical identity, source identity references where present, and evidence provenance. Preserve source-native names/values, effective or occurred time if known, observation/capture time, precision/timezone, origin and uncertainty. Imported facts may have no known actor or event time. Unknown and zero are distinct. A relation can be unresolved without creating a fictitious target. Canonical identity is not recreated when a mutable label changes. Source assertions do not acquire higher certainty by being normalized (I07–I12).

User/Operator identity and E26 Platform Operator Assignment are not forced into merchant ownership. E03 participation belongs to a specific Merchant; E26 participation belongs to the OpsHub SaaS control-plane context. No separate Platform entity, authentication architecture or permission engine is introduced.

Lifecycle descriptions state the **supported extent**, not a fully verified transition machine. Canonical historical correction/supersession preserves earlier evidence (I13); retention/deletion policy remains PD22.

## E01 — Merchant / Workspace

- **Purpose / treatment:** tenant boundary for one merchant's business records; NEW SAAS. “Workspace” is an alias for this boundary here, not a second nested tenant entity.
- **Grain / identity:** one merchant operational workspace; stable canonical Merchant identity. Whether a legal merchant can have multiple workspaces is PD20.
- **Ownership:** root owner of merchant-local concepts; no parent tenant is modeled.
- **Attributes:** business/display name, operational calendar/timezone policy reference, default currency context if approved. A default never replaces transaction currency evidence.
- **Relationships:** Memberships, Source Contexts and all owned business records. Merchant-side User participation is through Membership. Platform assignments provide the distinct authority context for administration/observation of Merchant and Membership records; this does not change operational ownership or create merchant memberships for platform operators.
- **Lifecycle:** active business context evidenced only for Gentry. Provisioning, invitation, suspension, onboarding, deletion, support access, closure and transfer workflows are deferred to the PRD; no additional merchant lifecycle is defined.
- **Invariants:** I01–I03; merchant assignment of imported evidence must be explicit.
- **Sources / historical-current map:** named Gentry operation; workbook Config/business labels; live single operation. No tenant ID/selector proved. Never infer identity from Bosta wallet Business Name alone.
- **Questions:** PD20 workspace/store/legal-business boundary; cross-merchant business links are not authorized by this proposal.

## E02 — User / Operator

- **Purpose / treatment:** identify a human/operator account separately from Customer, historical actor labels and its authority contexts; NORMALIZED/NEW SAAS participation semantics. E02 remains the common canonical account concept for both merchant-side and platform-side participation.
- **Grain / identity:** one canonical operator account identity, independent of display name, Merchant Membership or Platform Operator Assignment. One resolved User may have either, both or neither participation relationship. Native account matching remains PD11/PD20; a shared name or human claim does not automatically merge accounts.
- **Ownership:** account identity is separate from participation ownership: E03 is merchant-owned and E26 is platform-scoped. User identity alone grants no merchant, platform or cross-merchant access; profile sharing and authentication implementation are not specified.
- **Attributes:** account identity, current display name and evidenced prior labels. A name alone is not a trusted identity match.
- **Relationships:** zero or more Merchant Memberships, zero or more Platform Operator Assignments, and attributed events/actions. Authority must identify the relevant participation context; unresolved imported labels use Actor Attribution value objects.
- **Lifecycle:** one Omar authenticated session observed; account invitation, deactivation, role transitions and identity merging unverified.
- **Invariants:** I02/I09/I27; attribution, account identity and authority context remain distinct. Merchant membership does not imply platform administration; platform assignment does not imply merchant membership.
- **Sources / map:** authenticated display name, historical Support/Operations/Owner duties; free-text `calledBy`/`Called by` is not an account ID.
- **Questions:** PD11 actor matching and approval responsibilities; PD20 account scope; PD22 retention of attribution.

## E03 — Merchant Membership

- **Purpose / treatment:** participation and authority within exactly one Merchant/Workspace; NEW SAAS. It does not represent platform administration or prove existing RBAC.
- **Grain / identity:** one association of an operator with a merchant, with its own canonical Membership identity and historical participation evidence. Duplicate active-membership policy is PD11.
- **Ownership:** exactly one Merchant; one identified User.
- **Attributes:** responsibilities/grants as approved, effective period if known, authority and provenance. Historical role names are descriptive until adopted.
- **Relationships:** Merchant, User, optional trusted event/action actor attribution. A User may separately have E26 assignments; neither relationship creates or substitutes for the other.
- **Lifecycle:** historical duties and one session only; membership states and change controls remain unspecified.
- **Invariants:** I01–I03/I09/I27; a named Omar approver must not hardcode a person's display name as a universal SaaS role. No platform authority is inferred from membership.
- **Sources / map:** SOP duty matrix; Phase 1B navigation permission vocabulary `orders.view`, `orders.calls`, `orders.reship`, `orders.edit`; actual grant/enforcement matrix unknown.
- **Questions:** PD11 current grants, separation of request/approval, multiple duties and membership identity history.

## E04 — Source Context

- **Purpose / treatment:** describe a merchant's external/source origin and its evidenced native-object namespace; NORMALIZED/NEW SAAS. This is domain provenance, not credentials or connector infrastructure.
- **Grain / identity:** one merchant source context, such as a particular Shopify store, courier business/account context or manual source. Native-object namespace is independently qualified within that context; it may be unresolved. Workbook/export lineage and individual file revisions are Evidence References, not automatically a new provider identity namespace.
- **Ownership:** exactly one Merchant; source account spanning merchants is PD20 and must not silently share identities.
- **Attributes:** source kind, candidate native business/account/store identifiers, namespace semantics/confidence, evidence lineage references, observed coverage windows and authority references. Coverage belongs to each source observation/import, not a permanent completeness claim. Several exports can observe one namespace; identical labels in unrelated sources do not establish one namespace.
- **Relationships:** source identity bindings and provenance on every imported entity/event/projection.
- **Lifecycle:** observed exports, imports and sync/rebuild markers; trigger and refresh schedules remain unknown. Revisions preserve earlier origins.
- **Invariants:** I03/I07/I12/I19; source label is not stable external identity; public client action IDs are not business source IDs.
- **Sources / map:** Shopify, Bosta, Meta, Google Sheets, workbook/backups/stages, manual live entry. The immutable workbook profile records `RAW_Costs!A2` Business ID on all 1,381 rows, with one distinct value. Preserve this identifier observation as a binding candidate; its equivalence to courier account or Merchant is unverified. Native Shopify/Meta account crosswalks remain unknown.
- **Questions:** PD02 completeness; PD08 authority; PD14 ad origin; PD20 source-account mapping; PD21 refresh watermarks.

## E05 — Customer

- **Purpose / treatment:** merchant-local party placing/receiving orders when identity is sufficiently established; NORMALIZED. Customer does not mean phone.
- **Grain / identity:** one evidenced customer identity within a merchant; stable canonical Customer identity. Person, household, payer and recipient equivalence is unresolved.
- **Ownership:** exactly one Merchant; no cross-merchant person profile or automatic sharing.
- **Attributes:** evidenced names and contact observations with provenance, optional native customer ID if later supplied, identity confidence/ambiguities. Keep order-specific contact/address snapshots on Order.
- **Relationships:** zero or more Orders; Order may have no resolved Customer. Payer/recipient separation is not asserted from current evidence.
- **Lifecycle:** recurring phone associations observed; deduplication, identity correction and merges require PD12.
- **Invariants:** I01/I08; phones/names are nonunique descriptive evidence and must not overwrite historical order contacts.
- **Sources / map:** Shopify/Bosta contacts, live customer labels and repeat-phone indicator; no native customer ID/canonical customer table verified.
- **Questions:** PD12 matching, shared/recycled numbers, format normalization and recipient identity; PD22 retention.

## E06 — Order

- **Purpose / treatment:** merchant commercial order, independent of shipment and fulfillment channel; PRESERVED/NORMALIZED.
- **Grain / identity:** one order header/commercial request; canonical Order identity, with source-scoped Shopify name/reference and live internal ID bindings where known. A replacement is another Order, linked by meaning.
- **Ownership:** exactly one Merchant.
- **Attributes:** placed time/date, external references, channel assertion, value with provenance/currency, source payment/fulfillment/cancellation/archive assertions, tags, contact snapshot, unresolved item summary. Status/outcome/stage are separate dimensions.
- **Relationships:** optional Customer; Order Items, linked Shipment Legs, Contact Events, Confirmation Evidence, Return/Pickup Cases, Reship Requests, related orders and actions. Unmatched legs/events stay unmatched.
- **Lifecycle:** Pending/Cancelled/Completed source/display vocabulary and separate outcomes observed; no single allowed-transition graph proved. [04](04-state-machines.md#order).
- **Invariants:** I04–I07/I10/I14/I16; no full order-value duplication across legs/items.
- **Sources / map:** `RAW_Shopify` header helper → `Orders_Master`; live `/orders/{id}`, export `Order`; Bosta business reference is a link, not tracking ID. Exact trimmed references supported 768 shared current/live and all 353 backup/live orders.
- **Questions:** PD01 metrics; PD08 source/manual authority; PD09 outcome precedence; PD17 reship relationships; PD20 identifier namespaces.

## E07 — Order Item

- **Purpose / treatment:** one line of ordered goods/quantity/commercial description; PRESERVED/NORMALIZED, not Product or Shipment Item.
- **Grain / identity:** one evidenced order line within one Order; stable canonical Item identity. Repeated same-variant lines need distinct line identities. Source line ID is not currently established; artifact file+row/line sequence is a locator, not a universal business key.
- **Ownership:** same Merchant as Order.
- **Attributes:** ordered quantity if known, source product/variant labels, commercial price/discount/value observations if available, ordered description snapshot. Free-text item summary may remain unresolved rather than being parsed into invented lines.
- **Relationships:** exactly one Order; optional matched Variant/Product; quantity allocations to legs/returns only with evidence.
- **Lifecycle:** historical Shopify line rows verified; line edits, partial fulfillment/cancellation/return transitions unverified.
- **Invariants:** I04/I05/I14; repeated order-header amounts are not independent line values.
- **Sources / map:** 2,082 Shopify raw line rows / 1,635 headers, line-item exports. Bosta four-slot parser gives shipment description observations, not proof of order-line identities. Live `Items` is summary text.
- **Questions:** PD13 crosswalk, source line keys and unidentified summaries; PD18 partial-item allocations.

## E08 — Shipment Leg

- **Purpose / treatment:** one independently identified courier consignment/transport leg; PRESERVED/NORMALIZED. “Leg” denotes the evidenced courier record, not an invented route segment.
- **Grain / identity:** one courier tracking identity within its source context, with canonical Leg identity. RTO may be a source consignment classification; no separate physical segment is invented from its name.
- **Ownership:** exactly one Merchant.
- **Attributes:** tracking text, business reference, type/purpose assertion, courier state, created/completed timestamps with precision, COD observation, exception text, reported attempt count, description. Purpose/type and state are independent.
- **Relationships:** optional resolved Order; Delivery Attempts if individually evidenced; Cost/Fee Records; optional return/action links. Leg-to-order sharing and related-leg pairing remain PD09/PD18.
- **Lifecycle:** terminal historical records and additional live state strings observed; allowed transitions, chronology and selected-leg precedence unverified. A return leg can be Delivered without order kept.
- **Invariants:** I04/I06/I07/I11/I14; original tracking representation and unmatched references retained.
- **Sources / map:** `RAW_Bosta!A` tracking / `J` business reference; 569 distinct tracking keys, four blank references; live selected courier card, reship tracking links.
- **Questions:** PD02 coverage; PD09 consolidation/split/shared shipment and outcome rules; PD18 return episode linkage.

## E09 — Delivery Attempt

- **Purpose / treatment:** individually evidenced courier delivery/contact attempt, separate from a cumulative attempt count; NORMALIZED, conditionally materializable.
- **Grain / identity:** one attempt event on exactly one Leg; canonical Attempt identity plus provider event ID if supplied. Counts do not provide event IDs.
- **Ownership:** same Merchant as Leg.
- **Attributes:** occurrence time/precision, source result/reason, actor evidence, source event reference; only if available. Do not assume a full timeline or consecutive attempt numbers.
- **Relationships:** exactly one Shipment Leg, indirectly its resolved Order; provider count remains a leg observation.
- **Lifecycle:** attempt count 0–7 observed, **no event-grain timeline reconstructed**. Corrections remain evidence revisions; result transitions are not invented.
- **Invariants:** I06/I11/I13; no synthetic event per counter increment or reverse-engineered timestamp.
- **Sources / map:** Bosta/export `Attempts`, `DATA_Master!K4` excess-attempt projection; no current source identity for individual attempts.
- **Questions:** PD15 availability, event key and count semantics; whether counts include non-delivery activity.

## E10 — Contact Event

- **Purpose / treatment:** one recorded support contact/attempt/quick completion assertion, retaining contact purpose and source semantics; PRESERVED/NORMALIZED.
- **Grain / identity:** one independently recorded contact event, normally concerning one Order; canonical Event identity. Historical intake summary is not a collection of invented events.
- **Ownership:** exactly one Merchant.
- **Attributes:** recorded/occurred times separately if known, contact purpose, source contact status, customer narrative, reason/taxonomy reference, recorded resolution, refund assertion, recoverability, actor attribution, notes and source locator.
- **Relationships:** optional resolved Order or Return Case/Leg reference when evidence supports it; actual external action/confirmation evidence may be linked separately. Unmatched import events are permitted.
- **Lifecycle:** 239 exported events across 224 orders; current/legacy values differ. Two-NoAnswer queue behavior is UI contract, not event-state mutation. Preserve all history rather than replacing with Last call.
- **Invariants:** I07/I09/I11/I13/I16; `ResolvedByCall`/`Refunded` is a recorded assertion, not an executed refund or universal closure.
- **Sources / map:** live call CSV/history; `RAW_Intake!D` tracking + cumulative attempts/contact fields maps to the named Contact Intake Summary below, not to invented Contact Events. Seven live call dates precede matched order dates; cause unresolved.
- **Questions:** PD05 retry/event precedence, PD06 resolved, PD11 actors, PD16 importer matching/dedup/time; PD18 return-case link.

## E11 — Confirmation Evidence

- **Purpose / treatment:** retain evidence about order confirmation or attempts without manufacturing actual consent history; PRESERVED/NORMALIZED.
- **Grain / identity:** one observed confirmation assertion, tag observation or separately evidenced confirmation event concerning an Order; canonical Evidence identity with origin. Distinguish snapshot observation from event occurrence.
- **Ownership:** same Merchant as Order.
- **Attributes:** assertion kind, original tags/manual value, observed time, actual occurrence time only if known, consent/content only if independently evidenced, asserted confirmer, trusted actor if known and confidence.
- **Relationships:** exactly one Order when resolved; optional Contact Event, Actor Attribution, source identity. Multiple observations may yield one confirmer projection.
- **Lifecycle:** historical intended three failed attempts and consent rule; current Omar/Hadeer/Whapi attribution from tags. No proved confirmation timestamp; no automatic revocation/cancellation rule.
- **Invariants:** I09/I11/I17; failed attempt is not consent, tags are not authenticated actor proof.
- **Sources / map:** `Orders_Master!L:O`, Shopify tags `Confirmed`, `Confirmation Sent`, `confirmed omar`, attempt tags; live `confirmedBy` direct field/current attribution. Manual versus tags is unresolved.
- **Questions:** PD04 confirmation targets, PD08 authority, PD11 attribution, PD19 current consent/dispatch policy and superseding evidence.

## E12 — Return Case

- **Purpose / treatment:** one distinguishable goods-return/failure-of-receipt business episode, independent of courier legs/contact/actions; NORMALIZED identity proposed, not a verified persisted entity.
- **Grain / identity:** one evidenced episode tied to an original Order when known. RTO, post-receipt return and exchange-return remain distinct classifications. **Episode partition and item scope are PD18; do not create one case per label, leg or call.**
- **Ownership:** exactly one Merchant.
- **Attributes:** original order reference, reason evidence, receipt/disposition assertions, return kind, item quantities only if known, occurred/observed dates, links and provenance. Return date is not inferred from placed date.
- **Relationships:** optional resolved original Order; related Legs, Contact Events, item allocations, Tasks and External Actions. Multiplicity of physical return legs per episode unknown.
- **Lifecycle:** current outcomes RTO/refused/exchange plus historical groups; no request/approval/receipt/refund transition graph proved. Financial closure is a separate dimension.
- **Invariants:** I04/I06/I11/I14/I16; leg state Delivered does not establish kept outbound order or returned inventory availability.
- **Sources / map:** shipment types RTO/CUSTOMER_RETURN_PICKUP/EXCHANGE_return, `DATA_Master` groups, tracking intake and live order outcomes/contact forms. These are candidates for episode linkage, not authoritative case IDs.
- **Questions:** PD09 outcome chronology; PD18 episode identity/partial returns/exchanges; PD06 closure; PD07 economic recovery.

## E13 — Pickup Case

- **Purpose / treatment:** distinguish customer collection process from order payment and courier absence; NORMALIZED, no separate live case identity verified.
- **Grain / identity:** one evidenced pickup arrangement/episode for an Order; canonical Pickup identity. One case per order versus split/partial arrangements is PD18.
- **Ownership:** same Merchant as Order.
- **Attributes:** pickup channel evidence, collection assertion/evidence/time if known, waiting/cancel/no-show classification with policy, contact/task links, location only if supplied. Order payment remains a separate assertion.
- **Relationships:** owning Order when resolved, optional item allocations/contact/actions; no Bosta leg is required for a pickup.
- **Lifecycle:** current waiting/collected/cancelled/refused exception; historical paid/void/refund projections are preserved separately. Physical completion trigger and no-show precedence are PD03.
- **Invariants:** I10/I11/I16; neither paid nor missing carrier proves collection.
- **Sources / map:** `90 Office`, explicit/inferred workbook channel and `Pickup_Channel`; live Pickup and age queues; paid 21-day waiting sample (L18).
- **Questions:** PD03 completion/refused exception/no-show; PD02 historical inferred cases; PD18 partial collection identity; PD01 denominator/clock.

## E14 — Reship Request

- **Purpose / treatment:** independently tracked request for a linked replacement order/shipment, including approval evidence; PRESERVED/NORMALIZED. Rescheduling an existing leg is a different action kind.
- **Grain / identity:** one request concerning an original Order, canonical Request identity; supplied source request key unknown. Repeated requests cannot be deduplicated by original order alone.
- **Ownership:** same Merchant as original Order.
- **Attributes:** requested recipient/address/items snapshot, note, original COD assertion, requesting/approving actor evidence and times if known, observed request/approval/result evidence.
- **Relationships:** original Order; zero or more evidenced External Business Actions/results and related replacement Orders. Exact fulfillment cardinality/eligibility is PD10/PD17.
- **Lifecycle:** submission→pending approval is UI contract; four completed original→replacement histories observed. Approval/rejection/execution/failure transitions not tested.
- **Invariants:** I09/I16/I18; request/approval/history tag is not proof that every promised external effect succeeded.
- **Sources / map:** `/orders/{id}` request, `/orders/reships`, replacement `Reship of`/original `Reshipped` tags. UI same COD and named Omar approver are current scoped contracts, not universal SaaS policy.
- **Questions:** PD10 duplicate/partial effects and approval; PD17 reship versus replacement/exchange/reattempt and original financial treatment.

## E15 — External Business Action

- **Purpose / treatment:** retain identity and evidence of a materially consequential action such as replacement creation, courier booking, refund, cancellation or archival; NORMALIZED. No background job/transport design is implied.
- **Grain / identity:** one business intent targeting one kind of external effect; canonical Action identity. A reship request may entail several distinct intents. Retry/receipt observations alone do not establish another consequence, but one intent can have zero, one or several independently evidenced results, including unintended duplicates. Intent matching remains PD10.
- **Ownership:** exactly one Merchant; target source context belongs to that Merchant.
- **Attributes:** action kind, target/reference, approved/requested parameters, decision/actor evidence, externally identified result references, receipt/execution observations, known/unknown effect state and provenance. Requested, approved and externally confirmed are distinct assertions. Several receipts may describe the same result; missing receipts do not prove zero results.
- **Relationships:** optional Order/Leg/Reship/Return/Pickup/Task; zero or more independently evidenced effect results, each with zero or more receipt observations. Actual result multiplicity and completeness remain unresolved; this is representational capacity, not a claim about Gentry behavior. No actual refund transaction is inferred from call form fields.
- **Lifecycle:** UI promises and existing related-order histories only; no submission/retry/rollback graph proved. Proposed distinctions record incomplete/unknown effects without promising automatic compensation.
- **Invariants:** I16/I18; external consequence must not be represented solely by an order status or contact-resolution string.
- **Sources / map:** reship approval promise, cleanup Shopify links and recorded refund/cancel/archive assertions; execution receipt, dedup identity and audit source unverified.
- **Questions:** PD10 business idempotency/partial execution; PD06 actual resolution; PD08 authority; PD11 approval/actor; PD22 retention.

## E16 — Product

- **Purpose / treatment:** merchant merchandising product, grouping variants and product-level management; PRESERVED/NORMALIZED.
- **Grain / identity:** one product independent of labels/tier/season; canonical Product identity with scoped Shopify Product GID/current internal ID if evidenced.
- **Ownership:** exactly one Merchant; matching products across merchants are not shared automatically.
- **Attributes:** name, assigned tier, economics observations (margin/unit cost with currency/basis), lead time, ad keywords, season-assignment history and provenance. Advice/suggested tier are projections.
- **Relationships:** Variants, Product-Period Snapshots, Inventory Observations, Season assignments, Ad/Spend Allocations and Task references. Product cost input differs from incurred fee.
- **Lifecycle:** tier editing/addition UI and 20 current products observed; publication/discontinuation/deletion workflow not established.
- **Invariants:** I05/I12/I14/I15/I19; product/variant and current/period data remain separate.
- **Sources / map:** live Product GID/internal ID/name; historical `RAW_SKU!B` product labels and Product_Size. Nineteen historical labels versus 20 live products does not establish a one-to-one crosswalk.
- **Questions:** PD13 identity/variant stock; PD04/PD14 advice; PD08 metadata authority; PD07 economics validity.

## E17 — Variant / SKU

- **Purpose / treatment:** sellable product option/configuration distinguished from product and descriptive SKU text; PRESERVED/NORMALIZED.
- **Grain / identity:** one evidenced variant of one Product; canonical Variant identity. SKU/parsed label is a source identifier/alias only when its scope is established; no global uniqueness assumption.
- **Ownership:** same Merchant as Product.
- **Attributes:** options such as size, source label/SKU, unit price/cost observations with effective/source basis; external native variant ID if later evidenced.
- **Relationships:** owning Product; matched Order Items/description observations and Inventory Observations. Unmatched labels remain unresolved.
- **Lifecycle:** 60 historical keys/19 product labels; staged additions partly incorporated. Rename, reparenting, SKU reuse and retired variants unresolved.
- **Invariants:** I05/I07/I14; spelling-dependent matches are not canonical identity proof.
- **Sources / map:** `RAW_SKU!A:E`, Bosta description slots; live stock aggregation/native variant keys not inspected.
- **Questions:** PD13 variant IDs, aliases/reuse, crosswalk and product ownership; PD18 item allocations.

## E18 — Product-Period Snapshot

- **Purpose / treatment:** reproducible dated product performance observation with inputs, definitions and revisions; PRESERVED/NORMALIZED. A historical snapshot is distinct from a live recalculation over the same sales interval.
- **Grain / identity:** one snapshot observation/revision for one Product, period and basis/source. A logical series identifies merchant+product+period+observation kind+definition/source basis; each retained observation/revision has its own canonical evidence identity. Correction within unchanged series preserves the series reference. Changed product, period, basis, definition or manually reported versus calculated observation kind creates a different series, not an overwrite. Product/week alone is insufficient for conflicting sources.
- **Ownership:** same Merchant as Product.
- **Attributes:** period boundaries/calendar, units/gross/discounts/returns/spend, ending stock and cumulative orders as dated observations, currency, source/rebuild/as-of times, definitions, completeness and revision origin. Derived net sales/ROAS/sell-through have definition references, not event meaning.
- **Relationships:** Product, contributing spend/inventory/economics observations if known, source references; recommendation projection tied to exact inputs and policy.
- **Lifecycle:** seven weekly rows and manual same-week overwrite UI contract. Canonical revision preservation is proposed; how to choose current version is PD08/PD21.
- **Invariants:** I12–I15/I19; snapshot stock/order counts retain their basis even when current values change.
- **Sources / map:** live manual `weekStart`/weekly history and product CSV period rows; historical Product_Size/Weekly/Monthly are aggregates with other grains, not equivalent snapshot IDs.
- **Questions:** PD08 overwrite/authority; PD01 periods; PD14 recommendation formula; PD21 completeness/as-of/late revisions.

## E19 — Inventory Observation

- **Purpose / treatment:** retain a point-in-time stock quantity assertion with exact subject/scope; NORMALIZED, not an inventory transaction or production order.
- **Grain / identity:** one observation of quantity for one Product **or** Variant, one stock scope and as-of/source basis; canonical Observation identity. No variant breakdown is manufactured from product stock.
- **Ownership:** same Merchant as observed subject.
- **Attributes:** quantity and unit, current/ending/incoming scope, as-of/source observation time, location if evidenced, aggregation scope and uncertainty. Available/reserved/on-hand equivalence is unresolved.
- **Relationships:** one subject, optional contributing source/snapshot reference; incoming/minimum-batch copy does not establish Production Batch identities.
- **Lifecycle:** current product stock and dated ending stock observed; movements, reservations and reconciliation lifecycle not reconstructed.
- **Invariants:** I05/I12/I15; unknown as-of/scope is explicitly unknown; no double counting aggregate and component inventory.
- **Sources / map:** Shopify current-stock marker, live stock now/incoming display and snapshot endingStock; historical SKU table is pricing/cost, not inventory movement evidence.
- **Questions:** PD13 variant/location/aggregation; PD21 timestamp; PD23 Production/incoming/minimum batch.

## E20 — Season

- **Purpose / treatment:** merchant-named time horizon for product seasonal management; PRESERVED/NORMALIZED.
- **Grain / identity:** one season definition with canonical Season identity; separate from season-assignment relationship and derived Now/Upcoming label.
- **Ownership:** exactly one Merchant.
- **Attributes:** name, start/end dates, calendar basis and source/revision. All year is the current unassigned fallback, not a fabricated season entity.
- **Relationships:** zero or more Product assignments. At most one current assignment is a proposed normalization of the move/untick UI contract, not proved server cardinality.
- **Lifecycle:** creation/edit/delete UI; untick/delete→All year and tick→move are unexecuted contracts. Overlap, start/end validation and historical assignment preservation unresolved.
- **Invariants:** I12/I13/I19; historical advice retains the effective season definition even after an edit.
- **Sources / map:** `/products/seasons`, current two named seasons/assignment checkboxes; no historical workbook equivalent established.
- **Questions:** PD14 season overlap/assignment/restock semantics; PD08 revisions and deletion behavior.

## E21 — Advertisement

- **Purpose / treatment:** identity of an external advertisement when independently established, separate from a name-based match; NORMALIZED, conditional identity.
- **Grain / identity:** one advertisement in one merchant Source Context; canonical Ad identity. No native ad ID was retained in Phase 1. Names/keywords alone may be ambiguous.
- **Ownership:** exactly one Merchant; shared campaign/account semantics are PD20.
- **Attributes:** source-native ID if provided, observed names/name history, source context, periods and matching evidence. Do not introduce Campaign/Ad Set entities without evidence need.
- **Relationships:** Spend Observations; product-match/keyword relationships can be many-to-many pending PD14. A match is not spend ownership proof.
- **Lifecycle:** own-ad names/counts displayed; activation, deletion and renaming lifecycle unverified.
- **Invariants:** I07/I12/I19; unresolved ad identity remains an observation, not a guessed key.
- **Sources / map:** live Own ads / own ads count and Meta name/keyword wording; no historical implementation counterpart.
- **Questions:** PD14 native grain/matching collisions/VAT/currency; PD20 source accounts.

## E22 — Advertising Spend Observation

- **Purpose / treatment:** one source spend measure with period, scope and monetary provenance; NORMALIZED, distinct from allocation to products and audited invoice/payment.
- **Grain / identity:** one spend observation/revision for a source-specified ad/account/unresolved scope and interval. Logical series identifies merchant+native source namespace/scope+interval+measure basis; each revision has a distinct canonical Observation identity and retains that series reference. Revised amount/as-of under unchanged basis is another revision; changed scope/interval/source namespace/measure definition is another series. Ad-level evidence is optional. Aggregate product spend cannot recreate native source events.
- **Ownership:** exactly one Merchant.
- **Attributes:** amount/currency, interval/calendar, source measure grain, VAT inclusion assertion, original own/generic characterization if known, revision/as-of, completeness. Net/negative adjustments remain recorded if evidenced; validity is policy-dependent.
- **Relationships:** Source Context; optional Advertisement; contributing Allocations. Account totals and ad components are different scopes, not additive duplicates.
- **Lifecycle:** recent 1–2 days may revise per UI; no underlying event/statement/import lifecycle proved.
- **Invariants:** I12/I14/I19; source scope and revision prevent accidental double counting.
- **Sources / map:** Meta incl VAT wording, estimated own/generic product spend export. Native external IDs/VAT rules unverified.
- **Questions:** PD14 daily/full-week basis/collisions/zero sales/VAT/currency; PD21 rebuild and finality.

## E23 — Spend Allocation

- **Purpose / treatment:** independently traceable attribution result distributing spend to product-periods; NORMALIZED, conditional entity proposal. Independent identity is useful when the portion has separate reconciliation/history. Otherwise it can remain a projection with an evidence/result reference; no first-class entity is mandatory merely because a calculation is retained. Either representation remains derived evidence, not a factual customer/courier event.
- **Grain / identity:** one allocation portion in a logical series from a defined spend scope to one Product/interval under one method/version. If independently tracked, canonical Allocation identity denotes that series; each calculation revision has its own result/evidence identity. Changed target, period, source scope or method creates a different series; a rebuild with revised same-basis inputs is a new result revision. Aggregate amount may retain unavailable source decomposition.
- **Ownership:** same Merchant as source spend and Product.
- **Attributes:** allocated amount/currency, own/generic basis, matching/weight inputs if known, interval, method/policy version, calculation/rebuild time, uncertainty and unallocated remainder where known.
- **Relationships:** Product, source Spend Observation(s) with scope, optional Advertisement and Product-Period Snapshot. Many products per source is allowed canonically, but exact matching/allocation constraints are PD14.
- **Lifecycle:** observed estimates can rebuild; canonical revisions preserve previous result basis. No transfer/approval lifecycle is invented.
- **Invariants:** I12/I14/I19; allocations are not extra incurred charges; totals are reconciled within a single nonoverlapping scope/revision, subject to PD14 rounding/remainder policy.
- **Sources / map:** own ads/generic share fields and name/keyword/sales-proportion UI; no workbook-native equivalent.
- **Questions:** PD14 conservation/collisions/zero-sales/rounding and source decomposition; PD21 revisions.

## E24 — Cost / Fee Record

- **Purpose / treatment:** retain one independently identifiable charge/fee observation, actual assessment or explicit estimate; PRESERVED/NORMALIZED. Product per-unit cost/rate inputs are economics value objects, not incurred charges.
- **Grain / identity:** one source cost/fee entry or explicit modeled-charge estimate against a defined subject, with canonical Record identity. Source tracking ID links the subject; it is not necessarily a fee-entry ID.
- **Ownership:** exactly one Merchant.
- **Attributes:** amount/currency, charge kind, assessed/completed time and coverage basis, actual/modeled designation, source/reference, missingness and revision. Preserve zero/negative entries; the workbook's positive-only acceptance is a historical calculation rule, not universal validity.
- **Relationships:** optional matched Shipment Leg/Order or explicitly identified other subject; unmatched wallet entries remain records. Estimate and actual for same subject coexist with authority policy, not blind addition.
- **Lifecycle:** 1,381 wallet rows observed; source assessments/adjustments possible but not verified. Actual-versus-model selection remains PD07/PD08.
- **Invariants:** I07/I12/I14; missing cost is not zero, fee subject identity differs from entry identity, no unapproved FX conversion.
- **Sources / map:** fee/credit/component and Total Fees assertions within the named Courier Wallet Observation (`RAW_Costs!C` carrier tracking / `Q:AF` components/total), `DATA_Master!AI:AJ`, Paymob heuristic/zone model. A wallet row also contains payment/net/cash-out assertions; it is not itself a single fee entry. Preserve component-versus-aggregate basis and do not add both views as independent incurred charges. No live financial ledger verified.
- **Questions:** PD07 economics still active; PD02 unmatched coverage; PD08 fee authority; PD24 refunds/financial transactions.

## E25 — Operational Task

- **Purpose / treatment:** one independently recorded human work commitment, distinct from a calculated issue/queue membership; NORMALIZED, optional first-class record.
- **Grain / identity:** one authored work item with canonical Task identity; repeated appearances in queues are not new tasks. Do not instantiate from every flag.
- **Ownership:** exactly one Merchant.
- **Attributes:** purpose, subject evidence, responsible actor/role if known, due date/clock basis if supplied, recorded action/progress/completion assertion, review/provenance. Completion assertion differs from completed shipment/refund consequence.
- **Relationships:** optional Order/Return/Pickup/Product/Source Context, relevant Contact Events/External Actions; multiple linked subjects require evidence, not guessed cardinality.
- **Lifecycle:** historical report actions sidecar describes save/load/carry-over; no supplied task history/current task table. Assignment/closure transitions and “resolved” policy unverified.
- **Invariants:** I09/I11/I16; an issue clearing from a queue does not prove human work or external action completed.
- **Sources / map:** historical actions.py/report structure and manual SOP duties; live cleanup/call/New queues are projections, not direct task migration sources.
- **Questions:** PD06 resolution; PD08 authority; PD11 responsibility; PD25 whether independent tasks are needed/currently used.

## E26 — Platform Operator Assignment

- **Purpose / treatment:** explicit platform-scoped administrative/observational participation for a OpsHub SaaS operator; **NEW SAAS**, required by the owner's bounded correction. It provides the control-plane authority context without requiring Merchant Membership in every tenant.
- **Grain / identity:** one explicit platform participation/authority assignment to one identified User/Operator, with a stable canonical Assignment identity. Its scope is the OpsHub SaaS control plane, not a Merchant. Exact role composition, concurrent assignment rules and permission scopes are deferred to the PRD.
- **Ownership:** platform-scoped; no owning Merchant and no mandatory Merchant Membership. A referenced merchant remains a target of administration/observation, not the assignment's tenant owner.
- **Attributes:** User reference, platform authority-context designation, assignment purpose and authority/provenance reference; effective period/recorded actor where known. Exact roles, permissions and capability enumeration are not defined.
- **Relationships:** exactly one User; User may have zero or more Assignments. The assignment supplies the authority context for potentially administering/observing Merchant/Workspace records and merchant memberships under later policy. It does not itself imply unrestricted access to any/all merchants. A User can separately hold E03 memberships; no memberships are synthesized for platform access.
- **Lifecycle:** assignment grant/change/removal, provisioning, invitation, suspension, onboarding, deletion, delegated/support access and impersonation workflows are deferred to the PRD. No transitions or super-admin behavior are invented here.
- **Invariants:** I27; identity alone creates no authority; merchant and platform participation are independent; control-plane access does not transfer ownership of merchant records.
- **Sources / map:** no verified Phase 1 live or historical platform-operator representation. The source is the owner's future SaaS identity-boundary instruction, not an inference about the current Gentry application. Native/source assignment IDs and historical crosswalks are absent; none are fabricated.
- **Questions:** exact platform roles/permissions, super-admin capabilities, support impersonation, delegated access and access-control implementation are deferred to the PRD/architecture. The identity/context distinction itself is established by this correction; existing PD11/PD20 questions remain unchanged.

## Objects that are not additional entities

| Concept | Canonical classification / reason |
|---|---|
| Order relationship | Directed typed relation between distinct Orders (reship-of/replacement-of/unknown legacy association), with evidence and Request/Action link if known; no separate “replacement order” species. PD17 governs semantics/cycles/multiplicity. |
| Shipment/return item allocation | Quantity/description relationship to known Items/Variants; incomplete values permitted. Separate Return Item identity deferred pending PD18. No duplicate ordered/revenue quantity from leg descriptions. |
| Season assignment | Product↔Season relationship with observed/effective history; “All year” means no assigned season in current UI. PD14/PD08 govern applicability and history. |
| Money / valuation provenance | Amount, currency, actual/estimated/proxy/source/basis; value object. Order value, COD, sales, fees, unit cost and cash collection remain distinct. |
| Product economics observation | Source/effective-dated unit price/cost, margin, lead input and basis attached to Product/Variant; not an inferred expense/payment transaction. |
| Actor attribution | Known User with Merchant Membership or Platform Operator Assignment context where applicable, human label, automation label, importer/recorder or unknown, each independently evidenced. Neither authority context can be inferred from the User reference alone. Never create a User from every name/tag. |
| Source assertion / evidence reference | Original value, source identity/locator, occurred/effective/observed/captured times, certainty and revision. Shared semantic envelope, not a blanket event-sourcing architecture. |
| Courier Wallet Observation | Named source-observation value object: one courier financial/cash-cycle row at one artifact/revision, merchant and Source Context. Preserve candidate Business ID, tracking/business reference, COD, Online Payment Amount, named fee/discount/credit/VAT components, Total Fees, Net Value, Payment Status, Paid At and Cash-out ID with their original labels/bases. Optional Leg/Order match; unmatched wallet rows remain at source context. Candidate cash-out grouping relates rows sharing a source-scoped reference; 78 distinct values do not prove 78 settled bank transactions. No audited payment/settlement entity or inferred net-value formula. |
| Contact Intake Summary | Named source-observation value object: one tracking-subject intake row/revision, retaining Date, narrative/legacy labels, contact-state assertion, cumulative **support contact** attempts, governed cause/resolution/refund/recoverability and original blanks. It is neither Contact Event nor courier attempt. `RAW_Intake!A` Date does not become contact occurrence time; source top-up instructions map Bosta Created At there. Unmatched/uncertain subjects stay source-scoped. |
| Classification observation | Original label, classification kind (contact reach/reason/return type/courier exception), taxonomy/version, source/actor evidence, mapped responsibility/trust category and mapping version. Product/Courier/Ops/Customer/Unknown responsibility is not a User, Membership, permission grant or Task assignee. Later remapping preserves the original classification. |
| Effect result / receipt observation | Source-native consequence reference and provenance, distinct from Action intent and a receipt describing it. Several receipts can describe one result; one intent may have multiple evidenced duplicate results. Not a new mandatory entity or assumed executed transaction. |
| Courier/provider | Source kind/context identifies Bosta; configurable courier directory not justified by single-provider evidence. |
| Operational exception / issue | Source exception text is an assertion; calculated quality/cleanup issue is a projection with predicate and subjects. Only independently tracked human work becomes Task; an independent exception-case lifecycle is deferred (PD25). |
| Outcome, status, stage | Separately named source assertions/projections; no generic Status entity. |
| Tier / suggestion / recommendation | Assigned classification versus calculated advice; no Tier or Recommendation entity required. Retained advice has inputs/definition/as-of provenance. |
| KPI / metric definition | Named grain, population, numerator/denominator, calendar, null handling and policy/version value object; KPI value is a projection, never an event merely because retained. |
| Refund | Contact refund assertion; separately evidenced refund action can use E15. Actual monetary transaction identity is deferred (PD24); aggregate product returns/refunds cannot create individual transactions. Courier wallet payment/cash-out assertions are retained independently and are not evidence of customer refund. |
| Production / incoming batch | Stock assertions exist; independent production/batch/order lifecycle not reconstructed. Defer PD23. |
| Dashboard, master sheet, report, queue | Presentation/aggregate/worklist, not independent commerce entities. Report eligibility, authored narrative, Operations review and approval assertion are distinct; proposed approval attribution identifies the reviewed revision. No persistence/send implementation is assumed. |
| SaaS commercial/billing boundary | Subscription, Plan, Invoice and SaaS Payment entities are not introduced. Billing is outside the reconstructed merchant operational domain and will be evaluated during the PRD/product-boundary phase; omission does not decide that the SaaS will lack billing. |
