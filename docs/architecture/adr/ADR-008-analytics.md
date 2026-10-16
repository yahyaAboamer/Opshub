# ADR-008 — Revisioned relational projections and contributors

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

MVP operational/Product/SKU/ROAS values must be reproducible under late evidence and incomplete source coverage.

## Decision

Postgres indexed reads plus RLS-protected result/contributor generation tables with input/definition/policy versions; conserved spend/reversal allocations.

## Alternatives

Transactional-only unretained ratios; ordinary global materialized views; warehouse/CDC.

## Consequences

Bounded generation retention and dirty-cohort rebuilds need tests; no warehouse ops. Product presence is nonadditive; historical as-of requires retained state/evidence.

Details and evidence: [architecture chapter](../09-analytics-architecture.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
