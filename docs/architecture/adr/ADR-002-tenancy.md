# ADR-002 — Shared schema tenancy with defense in depth

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

Same identity and repeated source labels must not mix merchant records; platform authority is independent.

## Decision

Mandatory merchant keys/composite FKs, scoped server context, transaction-local RLS and nonowner runtime roles; restricted control-plane pool/health summaries.

## Alternatives

Schema-per-tenant; database-per-tenant; application filtering alone.

## Consequences

One migration/backup; disciplined role/context/query/job/file tests needed. Full runtime compromise exceeds RLS. Revisit database isolation on contractual or measured need.

Details and evidence: [architecture chapter](../03-multi-tenancy-and-identity.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
