# ADR-001 — Modular monolith

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

MVP must coordinate merchant authority, cases, provider effects and evidence with a small AI-assisted team.

## Decision

One codebase with in-process module capabilities, one primary PostgreSQL database, web/API and worker roles from the same release.

## Alternatives

Microservices/service-oriented databases; a single unstructured application.

## Consequences

Simple transactions/releases/restore; module boundary tests required. Worker workloads can scale separately. Extract only for measured bottleneck, independent security or team ownership.

Details and evidence: [architecture chapter](../02-architecture-style-and-modules.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
