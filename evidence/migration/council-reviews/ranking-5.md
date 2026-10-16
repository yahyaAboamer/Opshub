# Blind Council Stage 2 review — evaluator 5

Reviewed 15 October 2026. Ranked anonymous answers A–E on technical accuracy, safety insight and specificity of their acceptance-contract corrections. No named response identities or other ranking files were read. Selective first-draft documents and the original golden JSON were read directly from `council-reviewed-first-draft.zip` to verify important claims. The final amendment audit used current `docs/migration/`, `golden-contracts.json` and `golden-logical-fixtures.json`.

This is a documentation and synthetic-specification review. It supplies no implementation, actual provider/account qualification, migration, recovery, privacy-operation or production-readiness evidence.

## Individual evaluations

### Response A

Technically sound and particularly strong on the difference between conservation of acquired inputs and proof that acquisition found the intended population. Its repair scenario correctly treats retained historical links as insufficient to preserve action/contact eligibility across old and corrected identities. The independent-oracle finding is valuable: a validator can agree with an importer because they share a mistaken selector, and an Admin decision is not independent historical evidence. The continuous-traffic approval/deadline/abort finding makes operational safety part of the contract without inventing a duration or demanding a new architecture.

The first draft already had broad coverage, independent-validation and approval-invalidation obligations, so these are refinements of proof boundaries rather than evidence that safeguards were wholly absent. A acknowledges this accurately. Its main limitation relative to the highest-ranked answers is that it misses the explicit quality-state inconsistency and the separately important cross-class authority, inherited-seed and ordinary-reimport privacy cases. Its five corrections remain justified and bounded.

### Response B

The strongest overall safety analysis. It identifies three distinct cross-boundary failures that broad local invariants do not necessarily prevent: two exclusive class owners can still execute incompatible actions; imported restrictions can disappear in a restore before migration when there were no new OpsHub dispatch markers; and completed privacy dispositions can be bypassed by ordinary re-import without any restore. The first-draft parallel ledger and RV-G3 support these precise criticisms: they described per-class exclusivity and ordinary dispatch/handover/contact enumeration without expressly composing the missing cases.

Its two-sided remap quarantine, changing-page closure and independent logical-fixture findings are also accurate. Proposed controls preserve immutable native execution history, recognize enforceability limits of an incumbent stop, and quarantine uncertainty rather than solve it by guessing. B does not require distributed locks, a second event store or Phase 5 implementation. It misses the specific complete-versus-unmapped golden contradiction and a concrete temporal oracle, but covers more consequential independent failure boundaries than the other answers. Some items partly derive from existing general obligations; B correctly presents them as missing named validation contracts, not observed application defects.

### Response C

Accurate and unusually precise about temporal falsifiability. A baseline whose relevant clocks all sit in the same interval can pass while the implementation selects the wrong clock. Opposite-boundary placement, entry, action-required, first-attempt and observation cases are an effective remedy. Its prior-period and attributed/revised monetary contributor findings correctly expose scalar equality that cannot adjudicate a wrong member or allocation. Its remap treatment explicitly avoids transferring completion to a different actual recipient and composes replay with independent recovery.

The changing-population acquisition finding is also sound. C consistently separates a missing proof obligation from an implemented defect and accepts later fixture realization. It offers less coverage of independent authority/privacy/inherited-seed boundaries than B and less explicit source-oracle/approval-abort analysis than A. These omissions reduce comparative coverage, not the validity of its four findings.

### Response D

A technically correct, focused review. Its ordinary-intake privacy fence is a real gap in a restore-oriented privacy test catalog. Its exact monetary/prior-member correction and mutable-pagination test address independently verifiable deficiencies in the first draft. It recognizes that strong existing invariants should remain, and its alternative authoritative companion-fixture contract avoids prescribing an implementation format.

D is the least comprehensive of these otherwise strong answers. It does not compose repair with started effects/contact allowance, inherited restrictions with restore before migration, or incompatible classes with different owners. It also misses the directly observable golden quality-state contradiction and distinct-clock oracle. No material technical error was found; its lower rank reflects the narrower safety insight and coverage.

### Response E

The strongest direct internal-consistency finding: the first-draft JSON really marked KR02/KR03 `complete` while listing S08 as unknown and the golden narrative called its finality unmapped. Correct counts on a known subset do not establish complete interpretation. E carefully distinguishes unmapped finality from positively mapped pending rather than mechanically downgrading every pending result. That is both technically precise and relevant to dashboard/contributor/export trust.

Its repair continuity, independent logical source/event fixture and mutable-pagination analyses are well supported. The two-sided quarantine preserves immutable execution-time scope, never grants a fresh allowance merely because canonical identity changed, and includes restore. The fixture criticism is appropriately bounded by an alternative separately reviewed manifest before V2; it does not demand a provider implementation now. E omits B's cross-class, zero-new-marker inherited-seed and ordinary-reimport privacy cases, and A's explicit independent-oracle review expansion and bounded approval protocol. It ranks second because its quality-state contradiction adds a concrete acceptance-boundary defect to a strong broader review.

## Separate final-amendment audit

**Conclusion: CAR01–CAR10 are covered at the design-contract level. No residual actual design-contract gap was found in the reviewed amendments.** This conclusion is not a declaration that the contracts have been implemented or their tests passed.

| Amendment | Verified final coverage | Audit result |
|---|---|---|
| CAR01 acquisition closure | `03` MP-ACQ01/MP-T10 and `08` PC-C01 distinguish traversal/conservation from acquisition closure; independently known current members/revisions, cutoff ties, late visibility, child removal, cursor restart and buffered continuity are required. `changing_capture` fixes N01@v1, N02@v2, N03@v1, N04@v1 and retained LINE-OLD history with exclusion from current selection. | Covered; unsupported closure stays Held. |
| CAR02 repair continuity | `02` IM05/IM-T11, EA24, RV20 and CT-T12 preserve native execution scope and original lineage; quarantine the union of old/new scopes; independent repair descriptor and current reservations must agree before publication. | Covered; no automatic rekey, release, result transfer or budget reset. |
| CAR03 inherited recovery seed | MP-SEED01, EA25, RV19/RV-G3 and CT-T11 explicitly require independent migration-seed enumeration, version/coverage/retention and restore before migration with zero new OpsHub markers. The logical seed includes legacy unknown booking, consumed C04 events and unresolved C07 allowance with wider quarantine. | Covered; ordinary journal emptiness is not accepted as inherited-coverage proof. |
| CAR04 privacy across ordinary replay | MP-PRIV01/MP-T11, `04`, EA26, RV21 and PV11–PV13 apply current protected source-scoped suppression to intake, normalization/publication, changed-parser replay, late receipts and old downloads. | Covered; approved restricted holds and minimized identifiers remain policy gates, not ordinary access exceptions. |
| CAR05 cross-class authority | `12` defines booking/cancellation/replacement/native-booking/edit/annotation conflict dependencies; overlapping scopes require one reviewed coordinator or a verified competing hold/grouped transfer. EA23, GD43 and CT-T09 test incompatible races. `00` also states the cross-class requirement. | Covered; unenforceable ledger assertions cannot enable the target scope. |
| CAR06 exact prior/money contributors | KR16–KR21 and logical PI01–PI04/PS01–PS04 fix prior net 15,000, four units and delivered PS01–PS03 over PS01–PS04. GD31 attribution fixes 4,000/8,000/3,000 by item; GD30 fixes SP01@r1/A=3,000 and SP02@r2/A=2,080 with unallocated 520 and retained r1 results. Same-total/wrong-member negatives are specified. | Covered; exact amounts and membership can now adjudicate scalar-preserving errors. |
| CAR07 explicit logical input semantics | Logical source bindings provide actual MA/MB native-ID/alias/phone/SKU collisions, LINE-X1/LINE-X2 for identical line contents, CE01–CE08 with source scope/occurrence/locator, non-event C07 summary and requirement/result evidence. Concrete test-only clock/finality/contact/revenue/allocation rules are provided. | Covered within the explicitly declared logical-contract scope; every provider-shaped scenario realization remains independently reviewed before V2. |
| CAR08 temporal oracle | TC01–TC09 and KR18–KR20 separate placement, creation, entry, contact/action, observation and late correction. TC02 has placement before prior entry and current observation; TC09 has prior placement and current entry. TC05 excludes exact local exclusive end, TC06 holds spacing, TC07 distinguishes explicit -04/-05 instants and holds the ambiguous local hour, TC08 preserves old/new generation members. | Covered; corrected TC02/TC09 chronology and expectations are consistent. |
| CAR09 quality states | Current golden KR01 remains complete while KR02–KR06 are provisional with specific mapping/summary reasons. `06`/KR21 distinguish positive pending from unmapped finality and require the same state/reason/coverage on tile, contributors and export. Product C is qualified separately from A/B. | Covered; complete capture is no longer treated as complete interpretation. |
| CAR10 independent truth and bounded traffic | OR-INDEP01 fixes expected sets before actual evaluation, records shared dependencies, reviews every critical hold and expands review after a faulty rule. RE01 includes this provenance. `13` binds base/cutoff, reviewed delta classes, material invalidation, held-start deadline, backlog owner and safe abort to MD11–MD13/MD15; CT-T10 rehearses continuous traffic. | Covered; abort may remain held when incumbent return cannot be proven. |

Both JSON files parsed. Read-only specification checks confirmed eight contact events, distinct repeated-line IDs, prior net 15,000/four units/three delivered of four final shipments, attributed total 15,000, valid TC02/TC09 ordering and nine temporal cases. These checks evaluate supplied expectations, not an OpsHub engine.

The golden index and supplement intentionally stop short of complete provider-shaped fixtures for every scenario. `06`, `17` V2 and `reviewed_realization_gate` explicitly require an independent complete realization manifest before V2 can pass; this is an honest future evidence gate, not a residual Phase 5 design-contract defect. Account capabilities, production policies, application/RLS/action behavior, provider semantics and recovery execution remain unproven and gated. No source evidence or design document was edited, and no live action was performed.

FINAL RANKING:
1. Response B
2. Response E
3. Response A
4. Response C
5. Response D
