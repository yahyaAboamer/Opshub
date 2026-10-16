# ADR-003 — PostgreSQL and explicit relational ownership

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

Domain grains, atomic reservations and explainable monetary contributors need reliable relationships/transactions.

## Decision

PostgreSQL 17; canonical UUIDs separate from provider identity; typed relational domain data and bounded JSONB observations/intent; Kysely with reviewed SQL later.

## Alternatives

Document-first giant order blob; MySQL; ORM automatic schema generation; full event sourcing.

## Consequences

Database invariants/locks are explicit, portable SQL mostly retained. Team owns tenant grants/migrations/type generation. No production DDL in this phase.

Details and evidence: [architecture chapter](../04-data-architecture.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
