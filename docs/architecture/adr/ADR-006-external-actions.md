# ADR-006 — Immutable intent and reserved external effects

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

Timeout/duplicate approval/partial replacement cannot lead to duplicate irreversible business consequences.

## Decision

Stable objective/current-intent/effect reservations, Admin exact approval, one precommitted dispatch, independently retained constructable business/native-scope recovery descriptors, per-effect evidence and unknown-result hold; read reconciliation before any repeat/fallback. Persist exclusive manual handover before granting execution permission, including through database rollback.

## Alternatives

Blind retry; queue delivery as exactly-once effect; distributed transaction; automatic compensating refund/cancel.

## Consequences

Safety may require human/provider investigation. Private object storage becomes a pre-send availability dependency to preserve dispatch knowledge through DB restore. No-effect requires exact provider evidence and old-path termination, not lease expiry.

Details and evidence: [architecture chapter](../06-external-action-safety.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
