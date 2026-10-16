# Phase 5 — OpsHub migration and validation summary

**Design for human review: drafted 14 October, amended 15 October 2026.** The owner's Phase 5 request approves Phases 1–4 and supersedes their historical pending-approval text. It does not resolve OP01–OP13 or A01–A08 automatically. Gentry remains legacy evidence; OpsHub is the target product. No importer, application, provider mutation, production activation or engineering backlog is created here.

## Proposed strategy

Rebuild valid canonical state from qualified Shopify, Bosta and Meta evidence and reviewed merchant observations. Preserve **migrated fact**, **recomputed OpsHub interpretation**, and **legacy Gentry result** as three separately identified records with lineage. An import that finishes is only an intake result. Validation independently proves identity, row conservation, domain semantics, contributor arithmetic, authority and operational safety.

Use one controlled pilot merchant and explicit provider-account ownership. Acquire immutable, minimized intake snapshots; parse and resolve in an inactive run; retain all dispositions and conflicting assertions; compute interpretation/projection candidates; reconcile; approve one consistent activation generation. Imported tags, completed labels and bookings describe evidence: they never authorize an action, fabricate consent, reset a contact budget or replay a historical effect.

## Historical scope recommendation

Start with **all open operational work and uncertain effects regardless of age**, plus **eight complete merchant-local weeks and the current partial week** of qualified orders/items, outbound observations and analytics inputs, with dependency closure outside the horizon. This is a review proposal, not an approved retention or automatic cutoff. Two adjacent four-week windows permit a recent versus prior comparison; Phase 1 observed four-full-week product context. That supplies a useful candidate, not evidence that eight weeks covers all returns or effects.

The source package cannot establish the pilot's open-case age tail. Shopify's default 60-day history may not cover eight full weeks plus the current week or old open work. MD02 therefore requires a discovery census and a coverage decision before committing the horizon. Reduce optional closed-history scope if needed; never omit old open obligations to fit a provider limit. Keep the 18 June–17 August 2026 historical cohort as an oracle reference, not as the pilot launch date or a universal complete population. Details: [01](01-source-inventory-and-authority.md).

## Validation and rollout

1. Versioned synthetic [golden contracts](06-golden-datasets.md) and exact [KPI contributor sets](07-kpi-regression-suite.md).
2. Controlled [provider qualification](08-provider-contract-validation.md), including ambiguous-create recovery and competing native booking.
3. [Action race/failure](09-external-action-safety-validation.md), [tenant/authorization](10-tenant-and-authorization-validation.md) and [restore](11-recovery-validation.md) proofs.
4. Production **shadow mode first**: synchronized evidence and computed queues/KPIs, zero consequential external action or customer-contact starts.
5. Gradual capability enablement under the cross-class conflict matrix: one compatible authority for overlapping scopes, verified competing holds or grouped transfer, capability flags and trained Admin; bounded parallel comparison, then [cutover](13-cutover-and-rollback.md).

No rollout step is authorized by this document. Future controlled real effects require separate authorization.

## Correctness gates

Zero unexplained tenant leakage, unauthorized effects, blind duplicate mutation dispatch, silently dropped inputs, fabricated events/actors, incompatible active associations, unexplained contributor mismatches, or access opened before recovery privacy/authority gates. All source units have a disposition; all activated objects have traceable accepted evidence and valid tenant relations. An unresolved record may remain in evidence or be an explicitly approved operational hold; it cannot silently become trusted truth. Availability/freshness/volume targets require measured discovery and MD13 approval rather than arbitrary pass percentages.

## Package navigation

| Concern | Contract |
|---|---|
| Source scope and authority | [01](01-source-inventory-and-authority.md) |
| Identity and grain | [02](02-identity-mapping.md) |
| Runs, stages and replay | [03](03-migration-pipeline.md), [04](04-data-cleaning-and-dispositions.md) |
| Legacy comparison | [05](05-legacy-regression-oracle.md) |
| Golden/KPI proof | [06](06-golden-datasets.md), [07](07-kpi-regression-suite.md) |
| Providers and effects | [08](08-provider-contract-validation.md), [09](09-external-action-safety-validation.md) |
| Isolation, authority and recovery | [10](10-tenant-and-authorization-validation.md), [11](11-recovery-validation.md) |
| Shadow/parallel run and cutover | [12](12-shadow-and-parallel-run.md), [13](13-cutover-and-rollback.md) |
| Reconciliation/sign-off and privacy | [14](14-reconciliation-and-signoff.md), [15](15-privacy-and-test-data.md) |
| Decisions and future validation order | [16](16-open-migration-decisions.md), [17](17-migration-validation-plan.md) |

## Evidence and confidence

Inputs: [OD01–OD09](../product/00-owner-decisions.md), [canonical entities](../domain/01-entity-catalog.md), [architecture safety](../architecture/06-external-action-safety.md), [recovery](../architecture/13-deployment-and-environments.md), [D01–D25](../reconstruction/13-live-vs-spec-discrepancies.md), and immutable source/evidence. The Phase 5 [baseline](../../evidence/migration/phase5-input-baseline.json) protects 253 files, including 38 source files and 72 closed documents.

Council amendments require independently retained inherited migration restrictions, repair-time reservation continuity, privacy suppression on re-import, acquisition closure under changing pages, cross-class conflict controls, and explicit temporal/contributor/quality fixtures. Eight source-complete weeks cannot by themselves establish complete interpretation or safe authority transfer.

High confidence in approved semantic boundaries and testable safety requirements; moderate confidence in the proposed migration process; limited confidence in historical chronology, account coverage, physical collection and provider negative-result contracts. Documentation verification is not executed application, migration, security or provider testing. [Verification](../../evidence/migration/verification.json) and [review disposition](../../evidence/migration/quality-review.md) state their actual scope. Human review of this package and remaining MD decisions precedes Phase 6.
