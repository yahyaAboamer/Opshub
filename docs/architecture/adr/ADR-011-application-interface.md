# ADR-011 — REST at application boundary

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

Client, worker and provider operations need explicit session, version/conflict and durable pending-result contracts.

## Decision

Same-origin v1 REST/JSON; internal typed calls; separate merchant/platform guards; provider GraphQL confined to adapter; generated validated DTO/client types later.

## Alternatives

SSR application actions; GraphQL product API; public type-safe RPC; simultaneous interfaces.

## Consequences

Explicit 202 operation/status/error contract and tests; more client plumbing than SSR. No full schema/code generated in Phase 4.

Details and evidence: [architecture chapter](../08-api-and-application-boundaries.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
