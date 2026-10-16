# Independent council responses — first complete draft

Review question: Does the draft preserve the reconstructed Gentry business semantics while producing a precise implementation-independent multi-merchant model? Critique missing entities, incorrect cardinalities, mixed grains, over-modeling, under-modeling, migration traceability risks and unjustified assumptions.

The responses below concern the first complete draft, before corrections. Reviewer identities/lenses are omitted for blind peer review. No production actions or Phase 1 changes were permitted.

## Response A

The draft preserves the central Gentry semantics well. I found two substantive coverage gaps and two concerns about precision; no evidence-supported universal cardinality error.

1. **P1 — Evidence-supported defect: wallet rows are narrowed to fees.**
   In [01, E24](/D:/Desktop/Opshub/docs/domain/01-entity-catalog.md:288), [03, “Monetary provenance”](/D:/Desktop/Opshub/docs/domain/03-events-and-projections.md:70), and [08, E24 mapping](/D:/Desktop/Opshub/docs/domain/08-reconstruction-to-canonical-mapping.md:32), `RAW_Costs` becomes a charge/fee observation. Phase 1 instead identifies a **wallet/cash-cycle row**, containing COD, Online Payment Amount, Net Value, Payment Status, Paid At and Cash-out ID as well as Total Fees. The immutable profile shows all six fields populated across 1,381 rows; Payment Status includes Paid/Not Paid, and Cash-out ID has 78 distinct values. These are provider assertions, not proof of bank settlement, but they are meaningful source evidence already available.
   **Action:** explicitly preserve cash-cycle/payment observations and source cash-out grouping separately from fee components. A scoped observation/value object is sufficient; do not invent an audited transaction entity. Extend PD24 to distinguish absent gateway evidence from the wallet evidence that exists. Evidence: reconstruction **07, “Supplied raw schemas”**; `evidence/artifacts/workbooks/02_Gentry_Delivery_Performance_System.data_profiles.json`, `RAW_Costs!O:P/AG:AJ`.

2. **P2 — Evidence-supported defect: report review is reduced to generic provenance.**
   [01, “Objects that are not additional entities”](/D:/Desktop/Opshub/docs/domain/01-entity-catalog.md:329) mentions report narrative/review assertions, and [03, “Projection contracts”](/D:/Desktop/Opshub/docs/domain/03-events-and-projections.md:46) preserves quality eligibility. However, [04](/D:/Desktop/Opshub/docs/domain/04-state-machines.md) omits the separate **Operations review before forwarding** boundary. Phase 1 BR24 and L26 establish current DRAFT/Operations-approval wording; reconstruction 04 separates data-quality eligibility from human report review. A CLEAN report is therefore not necessarily approved to forward.
   **Action:** add a short report-review fragment distinguishing eligibility, authored narrative, review assertion and approved report revision. Label current wording as an unexecuted contract and historical review as intent. No Report entity or sending workflow needs to be introduced.

3. **P2 — Proposed design concern: classification semantics remain too implicit.**
   [01, E10](/D:/Desktop/Opshub/docs/domain/01-entity-catalog.md:124) gives “reason/taxonomy reference”; [03](/D:/Desktop/Opshub/docs/domain/03-events-and-projections.md:20) correctly distinguishes narrative, courier exception, governed root cause and blamed owner. It does not define the small classification object an engineer needs to preserve that distinction consistently. Phase 1 BR08 and workbook findings establish cause→Product/Courier/Ops/Customer/Unknown mappings; courier exceptions also have separate trust classifications.
   **Action:** describe a classification value object containing original label, classification kind, taxonomy/version, source attribution and derived responsibility category. Explicitly state that responsibility category is not a Membership, task assignee or permission grant. Preserve later remappings independently of original observations.

4. **P2 — Proposed design concern: derived identities could encourage unnecessary entity proliferation.**
   [00, “Canonical scope”](/D:/Desktop/Opshub/docs/domain/00-canonical-domain-overview.md:43) says entities have independent business identity/history, while [01, E23](/D:/Desktop/Opshub/docs/domain/01-entity-catalog.md:274) makes every allocation portion/revision an entity although it may only be a retained calculation. Its provenance requirements are valuable; independent business identity is less clearly justified.
   **Action:** state that an allocation can remain a projection with a stable evidence/result reference unless independent reconciliation or history gives it business continuity. Apply the same distinction consistently to observations and retained calculations. This is an optional simplification, not a source-semantic defect.

Key assumptions: this review treats Phase 1 as closed, treats UI promises as contracts rather than enforcement, and accepts unresolved links/cardinalities as deliberate containment. Customer, Return/Pickup Case and conditional Delivery Attempt identities should remain proposals; evidence does not justify filling their gaps.

The strongest objection to my review is that the shared assertion envelope can already retain wallet and report details without additional modeling. That is true for raw preservation. My concern is **named semantic coverage**: a senior engineer could preserve the rows while still misinterpreting settlement, report approval or responsibility.

Overall: a strong owner-review draft with careful evidence discipline and appropriate restraint. Address the two coverage gaps, then review the existing identity blockers. It is not yet an approved, fully determinate canonical model, and no implementation should infer answers from its provisional cardinalities.

## Response B

The draft largely preserves Gentry semantics. I found one concrete mapping omission and two proposed-model concerns. I read all ten domain documents and checked the relevant Phase 1 documents and retained workbook profiles.

1. **P1 — Evidence-supported defect: wallet grain is reduced to fee grain.**
   **Location:** `docs/domain/01-entity-catalog.md`, **E24 — Cost / Fee Record**; `03-events-and-projections.md`, **Wallet/fee entry**; `08-reconstruction-to-canonical-mapping.md`, **E24**.
   Phase 1 `07-data-model-observations.md`, **Supplied raw schemas and grain**, describes `RAW_Costs` as a wallet/cash-cycle row. Its retained `.data_profiles.json` records COD, Online Payment Amount, individual fees/discounts/VAT, Total Fees, Net Value, Payment Status, Paid At and Cash-out ID. There are 1,381 rows but 78 distinct cash-out IDs; these are additional asserted grains and relationships, not merely charge amounts. The canonical mapping primarily preserves tracking plus Total Fees and defers transactions. That deferral is appropriate, but it should not omit already evidenced wallet observations.
   **Action:** explicitly preserve a source wallet-row observation, its monetary components, payment assertions and candidate cash-out grouping. Map assessed charges separately. Do not interpret Paid/Cash-out ID as independently verified settlement, or introduce a transaction lifecycle without evidence.

2. **P1 — Proposed design concern: retry wording can erase duplicate external consequences.**
   **Location:** `01-entity-catalog.md`, **E15 — External Business Action**, grain/identity; `05-domain-invariants.md`, **I18**.
   “Repeat observations/attempts of the same intent are not new business consequences” is too absolute. Repeated execution can produce independently evidenced duplicate orders, bookings or refunds even when business intent remains unchanged. Phase 1 **BR18** leaves duplicate submission protection and compensation unknown; `03-events-and-projections.md` correctly acknowledges unknown duplicate effects.
   **Action:** say that retry observations do not *by themselves establish* another consequence. Explicitly allow one intent to have zero, one or several independently evidenced effect results, including unintended duplicates. Keep intent matching and recovery policy unresolved under PD10.

3. **P2 — Proposed design concern: native identity namespace and artifact provenance share one concept.**
   **Location:** `01-entity-catalog.md`, **E04 — Source Context**; `02-identities-and-relationships.md`, **Identity rules**.
   Source Context can represent a Shopify store, courier account or workbook lineage, yet it also forms part of the external identity namespace. An artifact lineage describes where evidence was captured; a store/account scopes the object being described. Treating them interchangeably risks splitting one external object across exports or merging unrelated source namespaces. Phase 1 **Source-to-live reconciliation** demonstrates overlapping references across current, backup and live populations, while account scope remains unknown.
   **Action:** distinguish source-object namespace from evidence artifact/lineage conceptually. Permit an unknown native namespace and retain matching evidence across artifact versions. This needs no connector or storage architecture.

Key assumptions requiring owner review remain well exposed: Merchant equals Workspace; Customer is an optional merchant-local primary party; User account scope is unresolved; Return/Pickup episode identity is unresolved; provisional primary links must not become enforcement. Conditional Delivery Attempt, Advertisement and Task entities should remain conditional. I found no justification for adding stock movements, production batches or executed refund transactions now.

The strongest objection to my review is that the shared preservation contract already requires retaining all original values, and PD10/PD20 explicitly contain the other uncertainties. That substantially limits the risk. My objection is narrower: a generic preservation envelope does not supply the missing wallet semantics, and the retry sentence contradicts the otherwise careful treatment of unknown effects.

Overall, this is a coherent, implementation-independent **review draft**, with especially strong separation of order/line/leg/contact grains, actors, physical pickup, confirmation assertions and projections. Make the bounded revisions above before accepting it as the canonical semantic reference. Do not resolve the remaining cardinalities or policies through conventional commerce assumptions.

## Response C

The draft preserves the major reconstructed distinctions well. I found two concrete evidence/mapping defects and three narrower modeling concerns. I would request a bounded revision before treating it as a precise canonical model.

1. **P1 — Evidence-supported defect: the wallet mapping reduces a cash-cycle observation to a fee record.**
   **Locations:** `01-entity-catalog.md`, **E24 — Cost / Fee Record**; `08-reconstruction-to-canonical-mapping.md`, **E24**; `07-policy-decision-register.md`, **PD24**.
   Phase 1 `07-data-model-observations.md` describes `RAW_Costs` as a wallet/cash-cycle row. Its immutable `.data_profiles.json` includes populated **Online Payment Amount (P), Net Value (AG), Payment Status (AH), Paid At (AI), and Cash-out ID (AJ)**, alongside fee components and Total Fees. Cash-out ID has 78 distinct supplied values; payment status distinguishes Paid/Not Paid. E24’s “one charge/fee entry” does not provide a clear canonical home for this bundle or its payout-group reference.
   **Action:** explicitly preserve the source wallet/cash-cycle observation, its separately named amounts/status/time assertions, and source cash-out grouping. Map fee components and total without double counting. Actual settlement/transaction semantics can remain unresolved; these fields do **not** prove bank settlement. No new financial transaction entity is required merely to retain them.

2. **P1 — Evidence-supported defect: source-account identity uncertainty is overstated.**
   **Locations:** `01`, **E04 — Source Context**; `08`, **E04**; `09`, **External IDs and memberships**.
   The draft says source-account native IDs were not reconstructed/account IDs are unknown. The same retained Phase 1 profile identifies `RAW_Costs!A2` as **Business ID**, populated in all 1,381 rows with one distinct value. Its equivalence to a courier account or merchant boundary remains unverified, but the identifier observation exists.
   **Action:** preserve it as a source-reported business-ID binding candidate and distinguish “available identifier, boundary semantics unresolved” from “identifier absent.” Do not convert it into a canonical Merchant ID. This matters particularly because Source Context supplies the proposed tracking namespace.

3. **P1 — Proposed design concern: intake summaries lack an explicit canonical home at their actual grain.**
   **Locations:** `01`, **E10 — Contact Event**; `03`, **Persistent does not mean factual occurrence**; `08`, **E10**.
   The model correctly forbids converting the 75 tracking-keyed intake rows into contact events, but identifies no explicit summary concept that retains their **cumulative contact attempts, narrative, reach assertion, governed cause, resolution and refund/recoverability assertions** together. Phase 1 `07` and `nonworkbook-analysis.md`, **Domain entities**, establish that summary grain.
   **Action:** name a tracking-subject **contact/intake summary observation** as a value object or observation classification, with its source row/revision and unresolved associations. State that its attempt counter differs from the courier counter and its Date does not become a contact occurrence timestamp.

4. **P2 — Proposed design concern: series identity and revision identity are not consistently distinguished.**
   **Locations:** `00`, **Canonical scope**; `01`, **E18/E22/E23**; `06`, **Snapshot revision**.
   E18 describes one observation/revision as the entity grain while also defining a logical series; E22 and E23 similarly combine “portion/observation” with “revision.” The overview’s definition of an entity as independently identified and historical does not explain which identity survives correction.
   **Action:** state explicitly which identity denotes the business subject/series, which denotes an observation or calculation revision, and when a changed period, source, definition or allocation method creates a different series. Keep manually reported weekly inputs distinct from calculated product-period results. L12’s manual history and L25’s refresh-sensitive export establish different provenance, not interchangeable record identities.

5. **P2 — Proposed design concern: consequential intent and resulting effect multiplicity need one precise relationship.**
   **Locations:** `01`, **E15 — External Business Action**; `02`, **Cardinality register**; `05`, **I18**.
   E15 has one intent targeting one effect, but its result identity is singular in attributes and plural elsewhere. Repeated execution could produce multiple external objects from one intent; repeated receipts could describe the same object. PD10 correctly leaves duplicate policy unresolved.
   **Action:** distinguish intent identity, externally identified consequence and evidence/receipt observations; explicitly permit unresolved or multiple results without treating every retry or receipt as a new consequence. BR18 establishes the multi-effect UI promise, not successful execution or result cardinality.

**Key assumptions:** preservation includes populated historical fields beyond those used by workbook formulas; these findings concern conceptual mapping, not schema design or verified financial execution.

**Strongest objection:** the shared evidence envelope could already retain every omitted field, and several requested clarifications may be deferred to later detailed modeling. That reduces immediate data-loss risk, but does not supply the precise canonical grain and relationship meaning promised by this package.

**Overall assessment:** strong semantic preservation and responsible uncertainty handling. Return/pickup identities and most unknown policies are appropriately deferred; adding conventional commerce entities would weaken the evidence discipline. Resolve the wallet/source-ID defects and tighten the three identity/grain contracts before owner acceptance.
