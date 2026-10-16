# OpsHub — architecture review and quality gate

14 October 2026. **Documentation review complete; proposed architecture pending human Phase 4 review.** The independent council challenge, documented amendments and focused amendment check are complete. This result concerns architecture sufficiency. No application, provider, queue-adapter, deployment or restore tests were executed, and the ADRs remain proposed.

## Review method and evidence

The first complete draft was frozen as [31-document archive](../../evidence/architecture/council-reviewed-draft.zip) with its [hash manifest](../../evidence/architecture/council-reviewed-draft-manifest.json). That archive preserves the reviewed draft, including its original weaknesses; the current documents incorporate the amendments below. An earlier dispatch was interrupted by the usage limit before any member answers persisted.

Using the LLM Council procedure, five separately tasked reviewers applied pragmatist, red-team, domain-rigor, first-principles and generalist lenses. Five fresh reviewers then blind-ranked the anonymized responses. All used the available inherited model; this is **not cross-vendor review**, and correlated model blind spots remain. Rankings compare the usefulness of critiques, not safety probabilities or provider facts. The chair evaluated the reasoning against approved OD01–OD09 and the actual draft rather than accepting votes as truth.

Preserved evidence: [anonymized member responses](../../evidence/architecture/council-stage1-anonymized.md), [blind peer reviews](../../evidence/architecture/council-stage2-blind-reviews.md), [rankings and method](../../evidence/architecture/council-result.json), and [focused check of amended contracts](../../evidence/architecture/council-amendment-check.md). The focused check found no material issue remaining from the domain rigorist's four original findings and supported the architectural direction subject to the existing qualification gates.

| Lens | Mean blind ranking position |
|---|---|
| Domain rigorist |1.2 |
| Red-teamer |1.8 |
| Pragmatist |3.0 |
| First principles |4.0 |
| Generalist |5.0 |

Four peer reviewers ranked the domain rigorist first and the red-teamer second; one reversed those two. All retained the modular monolith/PostgreSQL direction, separate merchant/platform authority, explainable provenance and containment of uncertain external effects. None supplied new provider-account evidence.

## Major critiques and disposition

| Critique | Disposition and reason | Amended design |
|---|---|---|
| A dispatch marker containing only local IDs/hash cannot reconstruct reservations lost after a backup | **Incorporated.** Recovery needs constructable business scope and native bindings, not just proof that an opaque operation might have run |13 requires minimal versioned dispatch/handover/contact descriptors, known dependencies/results, independent enumeration/coverage and restore-horizon retention. Missing identity/coverage quarantines the affected merchant/connection |
| DB rollback can erase manual handover exclusion before a connected dispatch marker exists | **Incorporated.** Manual and connected paths must share an exclusive reservation that survives rollback |06/13 persist independent handover knowledge before permission to execute; uncertainty blocks both paths and pending storage I/O retains exclusion |
| Fresh login after restore can reactivate revoked grants, used invitations or deleted customer data | **Incorporated.** Authentication alone does not establish current authority or privacy disposition |03/11/13 require an independently enforced recovery epoch, invalid restored sessions/invitations, provisional grants, verified current authority and independent privacy-manifest replay before reads/exports/writes reopen |
| Recording a call after it happens cannot prevent concurrent use of the same final contact allowance | **Incorporated.** Authorization must reserve eligibility, actor and ordinal before permitting a call |04/07/08 require atomic reservation, independent contact descriptor and final authority recheck before issuance. Lost responses/expiry do not return uncertain allowance; actual excess or independently made calls remain violating evidence |
| Reopening or relabeling a case could mint another contact objective or alter K05/K06 denominators | **Incorporated.** Stable canonical case identity is necessary for both contact limits and metrics |04 constrains one case per merchant/Order/case kind and one objective per case;09 uses that identity, separates actual contact from reservations and exposes ambiguous imported populations |
| Provenance could become a generic rule/EAV framework; job state could duplicate queue lifecycle | **Incorporated with limits.** Retain necessary business evidence/state while removing speculative generality |04 bounds typed concepts and transactionally owned interpretation/current state.07/ADR007 choose one pg-boss transport with enqueue on the exact domain transaction/connection; no generic parallel outbox lifecycle. Adapter/grant compatibility remains A08 |
| Product revenue should distinguish eligible attributed revenue from unattributed revenue | **Clarified; alleged existing formula error rejected.** The original09/OP09 already required an approved attribution policy; the critique did not establish a wrong implemented formula |09 now explicitly separates revenue eligibility/attribution and spend mapping, retains unattributed balance, and refuses implicit product-membership attribution.14's numerical oracle assumes an approved method; OD05/OD09 are unchanged |

Removing necessary action/run/projection obligations, dropping conflicting source evidence, using lease expiry as no-effect proof, or automatically retrying unknown writes was not accepted. These would weaken the approved semantics. The queue simplification preserves atomic publication and domain recovery; it does not permit an unprotected enqueue after commit. The contact protocol controls the OpsHub-authorized workflow, not a person's independent physical use of a telephone.

Chapter 14 records adversarial test oracles for lost reservations/handover/contact allowance, revived grants/invitations/privacy state, concurrent contacts, stable case denominators, revenue attribution and transactional enqueue rollback. They are a future testing strategy, not executed test evidence.

## Final documentation quality gate

| Gate | Result and evidence |
|---|---|
| Every approved MUST has an architectural home; excluded scope contained | **PASS — traceability.** Chapter 02 maps all 23 MUST capabilities and preserves F31/F32/F33/F36 exclusions |
| Tenant boundaries and independent platform authority | **PASS — specified design.**01/03/04/10 cover explicit context, composite tenant relationships, forced RLS/nonowner roles, limited platform grants and job/file/export/projection isolation |
| Provider failure, unknown effects and recovery | **PASS — specified containment.**05/06/07/13 retain stable reservations, separate steps in partial replacement, safe reads, old-path termination and reconstructable independent recovery knowledge |
| Manual fallback rejoins connected truth | **PASS — specified protocol.**06 binds handover and reconciliation to the same business effect and native evidence, blocks competing paths and preserves unresolved uncertainty |
| Explainable analytics and source provenance | **PASS — specified design.**04/09/11 pin definitions, contributors, cohort/window/as-of/coverage, source conflicts and attributable corrections; overlapping product counts and conserved money allocation remain explicit |
| Small-team complexity and credible stack | **PASS — reasoned proposal.**02/07/15/16 use one codebase, primary database, web/worker and one job transport; alternatives/trade-offs/exit paths are documented |
| Security, privacy, access and restore | **PASS — specified mitigations.**10–14 cover threats, finite proposed retention, restored-access/privacy gates and adversarial test strategy; approval and runtime proof remain outstanding |
| Scope boundary | **PASS.** No application, production migrations, integration implementation, deployment, migration execution or implementation backlog was produced |

The [static verification report](../../evidence/architecture/verification.json) is authoritative for the final file hashes and check counts. It checks 20 architecture documents, 11 proposed ADRs, local links/anchors, structural formatting, MUST/excluded coverage, council evidence and archived-draft hashes. It compares 198 pre-existing baseline files: 194 are unchanged, including all 38 original source files. The four authorized naming paths reverse exactly to their original hashes when the naming-only changes are undone; see [naming review](../../evidence/architecture/naming-consistency-review.md). Five Mermaid fences receive structural checks only; visual rendering is unverified.

## Residual risks and human review boundary

The [provider matrix](18-provider-capability-review.md) and [source-access record](../../evidence/architecture/provider-verification-sources.md) distinguish current documented capabilities, limitations, account qualification and unverified contracts. Bosta's full reference and some Meta developer pages were inaccessible; reliable duplicate/create-result lookup, account permissions, callback guarantees, exact reporting finality and attribution cannot be promoted to verified behavior. Shopify cancellation side effects and competing provider/native booking activity still require controlled qualification. No live mutation was used to fill a gap.

[A01–A08](17-open-architecture-decisions.md) remain explicit evidence/owner/compatibility gates: provider-account readiness, mutation recovery, operational policy, identity/access, privacy/legal, operating envelope/recovery, analytics policy and implementation compatibility. Independent recovery records are an availability and privacy obligation, not a promise of automatic reconciliation or exactly-once provider execution. Actual tenant isolation, storage protection, transaction enlistment and restore feasibility must be demonstrated in a later authorized build.

**Recommended next step:** human review of [summary](00-architecture-summary.md), the proposed ADRs, provider qualifications and open decisions. This completes Phase 4's architecture package and review record. Stop before Phase 5; architecture review does not authorize subsequent implementation, provider writes or migration work.
