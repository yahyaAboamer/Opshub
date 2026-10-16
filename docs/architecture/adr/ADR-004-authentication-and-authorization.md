# ADR-004 — Managed identity and local authority

## Status

**Proposed — pending human Phase 4 architecture review.** 14 October 2026. Does not authorize implementation or deployment.

## Context

MVP needs verified account access without owning password recovery; IdP/platform identity cannot grant merchant rights.

## Decision

Managed Auth0 OIDC hosted login; local shared User, hashed opaque server sessions, scoped Merchant Membership/Platform Assignment, server guards and live dispatch checks.

## Alternatives

Supabase Auth; self-hosted identity; IdP organizations/roles as business authority; browser-only authorization.

## Consequences

Vendor availability/MFA plan qualification required; OIDC subject mapping permits later replacement. Invitations/recovery/step-up/session limits remain approved-policy gates.

Details and evidence: [architecture chapter](../03-multi-tenancy-and-identity.md). Approved OD01–OD09 remain mandatory; unresolved qualifications are in [17](../17-open-architecture-decisions.md).
