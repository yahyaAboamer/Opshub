# Testing and CI

Current evidence is planning/static only. No future application tests are reported as run. T0009 establishes these proposed scripts: check:format/check:lint/check:types/test:unit/test:db/test:contracts/test:e2e/test:golden/test:recovery/build. Every implementation task records actual selected command/version/fixture/output evidence after scripts exist.

| Lane | When required | Evidence |
|---|---|---|
| Fast PR | Every code change | Format/lint/typecheck/relevant unit, secret/forbidden-egress checks and build |
| DB/migration | Any persisted data/grant/query/invariant change | Disposable PostgreSQL17 apply/no-op/target guard, nonowner RLS read/write, tenant FK/grant inventory and migration review |
| Authorization/session | Every access-sensitive change | Independent direct API/worker/current-grant tests, invitation/CSRF/context and revoked access |
| Provider mock/contract | Any ingress/read/action adapter | Versioned fixtures, malformed/duplicate/out-of-order/partial/unknown behavior and request/effect counts |
| Golden semantics | Changed normalization/identity/policy/projection/workflow | Exact member/amount/exclusion/clock/quality/generation assertions, not scalar equality |
| Browser vertical slice | Changed actor journey or shared UI foundation | Playwright against running OpsHub web/API/PostgreSQL (worker when asynchronous) with fake providers: navigation/roles, loading/empty/validation-error/forbidden/stale/pending/unknown/partial-source/success, narrow and desktop viewports, keyboard/focus/labels/understandable errors, automated accessibility scan and tenant late-response race |
| Heavy scheduled/pre-release | Relevant risk and release | Full EA/TI/AU/RV/GD/KR, randomized alternate deterministic barriers, full E2E, approved volume/restore measurements |
| Real qualification | Only authorized controlled environments | Account/version/scopes/side effects/native counts/positive-negative recovery and sanitized evidence |

A user-facing task needs at least one browser vertical-slice test through real UI → API → PostgreSQL. Component tests, API contract tests and mocked-API browser tests support it but never replace it. Contract tests on producer read/command ports enumerate every client-visible state and prove no state collapses into null/false/zero. A consumer UI task's client contract test pins the REST shape it relies on (fields, cursor/filter, error codes, version semantics per [architecture chapter 08](../architecture/08-api-and-application-boundaries.md)).

Do not run every heavy suite for a trivial view edit; run the relevant deterministic regression and broaden only for changed risk or failure. Security/tenancy/auth, schema migrations, external mutation, independent recovery and analytics definitions require a second reviewer with the applicable expertise and stronger evidence. LLM review cannot replace those tests.

Fixture realization starts T0207, money/clock inputs T0912, all semantic assertions T0913/T1106. Fix expected inputs before evaluation independently of implementation. Deliberately wrong identities/parsers/clocks/quality/same-total member sets must fail. All applicable hard-correctness gates have zero unexplained mismatch tolerance.

[Phase6 verifier](../../evidence/implementation/verify_plan.py) separately checks this planning package with schema, independent source inventory, graph/gates/locks/views/digests and negative controls. It makes no runtime-security claim.
