# Identity mapping contract


## IM05 — Reservation continuity during identity repair

A selected crosswalk may change; an immutable execution-time native account/subject/intent and its started, unknown or succeeded effect reservation do not get rekeyed or released. Before publishing a repair, enumerate the union of old/new Orders/cases/objectives, actual/uncertain contact allowance, handovers, realized results and dependent native bindings. Quarantine both affected business scopes until independent evidence establishes which obligations/allowances belong where. If scope cannot be bounded, quarantine the connection/merchant.

Append a correction relationship explaining old binding, new candidate, source evidence and decision. Keep original event/dispatch lineage; neither transfer completion to a different recipient nor reset a budget because an association was detached. Current safe selections/reservations and an independently retained minimal repair descriptor must agree before publication; descriptor/schema/coverage uncertainty keeps the repair operationally held. This uses Phase4's independent recovery storage, with exact protocol compatibility a MD16 gate.

**IM-T11:** false OA→native subject match, three consumed/uncertain contacts plus unknown/succeeded/handed-over booking; repair to OB, re-import, restore before repair, rediscover provider objects, request new contacts/effects on both sides. Expected zero new starts while disputed, unchanged original execution history, recoverable old↔new correction/hold scope. Releasing one subject requires positive reviewed scope evidence, not merely a new canonical UUID.
**IM01:** bind each merchant-owned canonical subject by verified tenant + native provider/account namespace + object kind + exact source ID. Canonical IDs are opaque UUIDs under [Phase 4 persistence](../architecture/04-data-architecture.md); fixture symbols are test locators, not an alternative ID design. Source artifact/hash/sheet/row is evidence lineage, never automatically a native namespace.

## Mapping record and confidence

Every attempted mapping records merchant, environment, source context, verified native account (or unknown), object kind, original source ID and type, artifact/row/object locator, canonical kind/ID if resolved, candidate IDs, mapping policy/version, actor/reason/time, match confidence, disposition, collision/unmatched reason and retained prior mapping.

Use categorical evidence confidence: **VERIFIED_NATIVE** (same qualified native identity), **REVIEWED_CROSSWALK** (explicit evidence-backed Admin decision), **CANDIDATE** (descriptive link only), **UNRESOLVED**, **COLLISION**. Do not invent probability scores. Auto-accept only a qualified native binding or an approved deterministic crosswalk contract; confidence alone is not authority.

## Entity mappings

| Canonical kind | Source namespace / source ID | Canonical match; collision, ambiguous and unmatched behavior |
|---|---|---|
| Merchant E01 | Verified pilot organization + connection ownership; legacy Business ID candidate | Fresh authorized Merchant UUID. A worksheet name/Business ID cannot provision ownership. Competing account-owner claims block connection/migration |
| User E02 | Managed issuer/subject for current users; historical caller/confirmers separately sourced | Current authorized User binding only. Same name/email claim cannot authenticate history; unknown historical actors remain claims. No migrated session/invite/role grant |
| Customer E05 | Shopify store/customer native ID if present | Merchant-local customer UUID; preserve recipient/purchaser snapshot separately. Phone/name equality yields candidates only. Guest order may have no Customer |
| Order E06 | Shopify store/Order native ID; separate Gentry internal ID and order-name alias | Same native ID → same Order. Store/order name alone needs reviewed namespace/time crosswalk. Collisions hold; unmatched source observation stays unresolved |
| Order Item E07 | Store/Order/LineItem native ID | Distinct item UUID under same Order. Repeated identical variant lines remain distinct. Export without line ID uses artifact-group ordinal only as evidence locator until crosswalk, never universal item identity |
| Shopify Product E16 | Store/Product native ID/GID, exact accepted representation | Product UUID; Gentry product ID separately crosswalked. Name/season is candidate. Reused name cannot merge Products |
| Shopify Variant E17 | Store/ProductVariant native ID; parent Product binding | Variant UUID and verified parent. SKU is alias, mutable/nonunique. Same SKU across products/time remains distinct; unmatched RAW_SKU retained as context observation |
| Shipment E08 | Bosta account/native delivery ID; tracking binding qualified separately | Shipment UUID + purpose. Tracking display and native delivery ID are not presumed interchangeable. Colliding/reused tracking or unknown account held; independent extra outbound retained as discrepancy under OD06 |
| Bosta tracking/delivery identity | Bosta account/object-kind/exact native/tracking ID | Source binding to above Shipment, not Order. Business reference links only through a qualified commerce crosswalk; blank/ambiguous links remain source-scoped |
| Delivery Attempt E09 | Account/delivery/native attempt-event ID and reliable occurrence | Individual event only when evidenced. Aggregate numberOfAttempts remains observation; no generated count-many events |
| Return E12 | Verified Order + canonical return case; native return identity/leg when independently linked | One accepted return case per Order under OD06. Repeat/partial/reverse-leg ambiguity held; do not mint a case per call or courier row |
| Pickup E13 | Verified Order + canonical pickup case + physical purpose evidence | One accepted pickup case per Order. Customer handover/courier collection are separate physical dimensions/populations; classification change does not mint another budget. Ambiguous/repeated history held |
| Contact Event E10 | Qualified source-native event ID, otherwise file/row observation | Native event → stable event UUID. Without ID, exact snapshot replay is safe; cross-export identical text/time is not proof of duplicate. MD05 chooses reviewed event continuity; uncertain row excluded from dated case KPI |
| Confirmation Evidence E11 | Native tag/source observation revision or independently identified confirmation event | Evidence UUID + source basis; unique Order participation retained across reopen. Tag capture time does not become process-entry/consent time; absent basis held for dated cohort |
| Replacement relationship E14/E15 | Independently evidenced original/new native Order IDs, relation source/revision | Two distinct Orders + directed typed relation. No phone/COD same-value match. Self-link/cycle/cross-tenant/competing originals held; unknown historical effect remains blocked |
| Meta account/campaign/ad E21 | Provider account/native campaign/ad IDs at declared object kind | Separate scoped identities. Mutable names/keywords only candidates; unavailable native level stays source observation. No guessed SKU relation |
| Spend observation E22 | Account + reporting level + object ID + interval/timezone + currency/tax basis + parameter/breakdown set | Stable **series** identity; amount/as-of/provider version produces revisions, not another additive spend object. Campaign/ad/account alternative aggregation levels cannot be combined blindly |
| Spend allocation E23 | Selected spend revision + approved mapping/method version + target/period | New allocation interpretation/run with portions and unallocated remainder. Native spend unchanged; corrected mapping supersedes selection, preserves prior generation |
| Cost/wallet E24 | Bosta account/native wallet row ID if available; otherwise artifact row/revision | Tracking is charged-subject link, not universally wallet-row identity. Separate components/total/cash-out grouping; no dedup by tracking alone |
| Source Context E04 / inventory/season E19/E20 | Verified account namespace; dated subject/observation; sourced season identity | Keep unknown namespace/stock date/historical assignment unknown. Archive lineage never upgrades ownership/confidence |

## Collision and replay rules

**IM02:** a verified binding cannot point to two accepted canonical subjects in one scope. Stop affected group, retain all candidates and raise COLLISION; never merge canonical objects to make a unique constraint pass. A late approved remap retains old evidence links and interpretation history, recomputes affected cohorts and invalidates unstarted dependent approvals.

**IM03:** a known native object observed in workbook, export and API maps once with multiple observations/revisions. Identical snapshot replay preserves IDs and adds no duplicate business entity. Source row fingerprint detects exact intake replay, not semantic event continuity across changed files.

**IM04:** new verified provider account binding requires ownership review. Shared/rebound accounts cannot silently import one tenant's objects into another; preserved old namespace remains with its original owner/history. A run cannot infer merchant from a filename, payload field or browser-selected tenant.

## Historical grain and authority constraints

Order ≠ Shipment ≠ Attempt; call event ≠ summary; confirmation evidence ≠ projection; payment ≠ collection; Product ≠ Variant/SKU; native spend ≠ product allocation; assertion ≠ correction ≠ selected interpretation. Apply [OD06](../product/00-owner-decisions.md) to accepted MVP state while retaining incompatible historical legs/cases as qualified evidence. Imported extra events—including an independently evidenced fourth call—remain violation evidence; they cannot authorize another contact.

Mapping manual decisions require current Merchant Admin scope and selected evidence/reason. Historical callers/users are not granted memberships. A Platform Admin acting in platform context cannot accept merchant corrections or approve migrated business effects. See [10](10-tenant-and-authorization-validation.md).

## Required identity tests

IM-T01 two stores reuse order name/SKU/phone/tracking: no merge. IM-T02 three captures same native Order: one Order, separate assertions. IM-T03 same Item text twice with different native IDs: two Items. IM-T04 unchanged file rerun: same accepted IDs. IM-T05 changed export repeats same-text contacts: unresolved unless event contract proves continuity. IM-T06 second outbound: retained discrepancy, one accepted association, action blocked. IM-T07 unknown account: no native binding/activation. IM-T08 reversed/cyclic/cross-tenant replacement: hold. IM-T09 native ID reassignment: collision, no overwrite. IM-T10 false descriptive match correction: old relation/generation preserved; affected approval invalidated; no external mutation.
