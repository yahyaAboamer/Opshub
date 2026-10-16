# ADR-005 — Separate inbound, action and reconciliation lanes

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

OD08 needs connected normal commerce/courier flow, OD09 spend, but provider contracts differ.

## Decision

Provider adapters with capability/version records; Shopify verified webhook plus read sweep, Bosta qualified callback/read polling, Meta scheduled report revisions; all mutations through action coordinator.

## Alternatives

Polling-only uniform connector; event-only truth; direct mutations inside ingestion; broad marketplace.

## Consequences

Visible coverage/account qualification and safe fallback; more adapter-specific tests, no single uniform retry policy. No inbound-triggered business effects.

Details and evidence: [architecture chapter](../05-integrations.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
