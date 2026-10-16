# ADR-007 — One transactional PostgreSQL queue

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

Sync/reconciliation/projections/export need durable background execution without a datastore fleet.

## Decision

pg-boss is the sole routine scheduler/retry transport. Enqueue on the same checked domain transaction/connection through a pinned verified adapter. Retain authoritative action/effect, sync checkpoint/run, export and requested projection state; no second generic outbox lifecycle. One worker initially with fair account budgets.

## Alternatives

Redis/BullMQ; managed queue plus scheduler; separate transactional outbox/dispatcher; distributed orchestration.

## Consequences

Shared DB capacity/library/adapter/grant compatibility is a release gate. Domain rollback must rollback enqueue; an unprotected separate-connection send is forbidden. Domain IDs/checkpoints keep effects explainable and allow a later reviewed queue change, while the selected adapter intentionally couples the initial enqueue path to pg-boss. Redelivery cannot repeat a started mutation.

Details and evidence: [architecture chapter](../07-background-jobs-and-reconciliation.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
