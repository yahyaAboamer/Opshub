# Execution principles

Work one accepted contract at a time. Implement vertical actor journeys using synthetic inputs/fake adapters before actual qualified integrations. Preserve order/shipment, payment/physical collection, case resolution/contact reach/action completion and observed fact/selected interpretation/legacy result as separate dimensions.

Every capability starts with current merchant authority, forced RLS/scoped relations, provenance, audit and negative tests. Append evidence; don't manufacture actors, timestamps, attempts, native identity, consent or physical effects. Ingestion and reconciliation never initiate business mutations.

One checked transaction owns local state/audit/queue insertion. Provider/storage I/O is outside DB locks. ExecutionStarted is conservatively may-have-sent. Unknown outcomes retain exclusion and permit safe investigation, not blind connected/manual repeat. Reliable no-effect additionally needs old-path containment.

MVP has at most one accepted outbound, return and pickup per Order. A replacement is a new linked Order. Three ordinary contacts include successes/failures; reopen/relabel/Admin cannot reset allowance. Reserve before external-call permission and retain independent knowledge before issuance.

Local acceptance proves local functionality only. A fake demo is not qualified integrated completion. Account qualification, production read shadow, each consequential class/contact permission and cutover have separate evidence and authorization gates.

Current source priority: owner decisions → PRD → canonical domain → architecture → migration validation → Gentry reconstruction. Compatible validation/safety contracts accumulate. A genuine conflict receives exact locators, affected tasks, consequence and bounded proposal; neither engineering nor an LLM silently chooses business policy.

## Vertical product slices

Amended 16 October 2026 (owner-directed plan maintenance; product scope unchanged). OpsHub is built as vertical product slices, not backend-first with UI later:

1. A user-facing milestone is incomplete until its required journey works through UI → REST application/API → PostgreSQL and worker/background behavior where applicable.
2. Backend or API success alone never completes a user-facing task or milestone.
3. UI requirements shape the client-facing contract. A consumer UI task writes its journey client contract against accepted producer ports before building components, and a producer read/command contract is stable only once it exposes every state that journey must show. A missing field or state becomes a versioned producer amendment, never a UI invention.
4. Every applicable backend state is representable in the UI: loading, empty, validation/error, permission/forbidden, stale, pending/async, unknown/reconciliation-required, partial/incomplete-source and success/completed. States are never collapsed into blank, zero, false or "not sent".
5. User-facing acceptance covers narrow/mobile-class and desktop-class viewports.
6. Accessibility is tested and reviewed: keyboard use, focus, labels/semantics and understandable error states.
7. Important journeys need browser integration/E2E evidence against the running OpsHub stack, not API-only or mocked-API evidence.
8. UI work may use installed UI/React skills for implementation quality. Skills never override PRD, domain or task behavior.

Client conventions come from the approved [architecture chapter 08](../architecture/08-api-and-application-boundaries.md): REST/JSON, 202 operation status, stable error codes, `(sort_value,id)` cursor pagination, version/freshness in responses and expected-version conflicts. Producer tasks own domain rules and consequential commands and publish their client-visible state, version and provenance semantics in their contract. Each consumer UI task owns only its journey's read/presenter adapter in its listed `apps/api/modules/<module>/http/` area. T0004 supplies the shared frontend foundation every slice reuses.

## Integration

After a dependent merge, update from current accepted main, inspect actual contract change and rerun affected tests. Do not defer security/golden evidence to launch. Split an unexpectedly broad task into new IDs; never recycle a stable ID or start an unjustified XL task.
