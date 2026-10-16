# ADR-010 — Append-only evidence and explainable working state

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

Source disagreement/manual correction/actor/time uncertainty must survive normalization and consequential execution.

## Decision

Bounded raw observations, typed assertions and revisioned selected interpretations; corrections/conflicts with actor/reason; append-only audit/action history and minimal recovery records, approved retention/redaction hooks. Keep privacy disposition manifests independently of database rollback and replay approved dispositions before restored access opens; preserve minimized evidence supporting current selections.

## Alternatives

Newest-wins overwrite; unlimited raw payloads; full event sourcing; logs as audit.

## Consequences

Ordinary edits cannot erase prior claims; privacy deletion under approved controlled retention remains possible. Infrastructure owner is privileged, so append-only grants are not an absolute tamperproof certification.

Details and evidence: [architecture chapter](../11-audit-provenance-and-privacy.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
