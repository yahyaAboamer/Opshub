# ADR-009 — Paid managed web, worker and PostgreSQL

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

Small team needs normal long-running work, secrets isolation, backup and safe rollback.

## Decision

Paid Render web/worker/Postgres with private access; private S3/files/backups/dispatch markers, independent environments; reviewed release migrations and mutation-egress-off recovery.

## Alternatives

Railway; AWS container/managed stack; serverless-only worker; Kubernetes.

## Consequences

Region/plan/identity/storage cost and restore targets still require evidence. Docker/Postgres/OIDC ports support exit. Restore denies user access and egress, invalidates sessions/invitations with an independent epoch, reverifies current authority and replays independently retained privacy manifests. Constructable dispatch/handover/contact descriptors and provider truth protect lost reservations; missing coverage quarantines affected scope.

Details and evidence: [architecture chapter](../13-deployment-and-environments.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
