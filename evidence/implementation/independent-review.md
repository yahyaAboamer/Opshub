# Independent review of the first Phase 6 draft

Date: 15 October 2026. Reviewed draft: P6-r1, manifest digest `2d6bac43ae8578d1ec99304b05c2c4c9b3af394d2df647f56093f6542a994945`, 113 tasks. This is an independent documentation review and paper walkthrough. No application, provider, migration, infrastructure or production operation was executed. Implementation tests remain PLANNED, not PASS. Static verification was being prepared separately and is not treated as a missing completed deliverable here.

Disposition: **CHANGES REQUIRED before presenting the full catalog as implementation-ready.** The local/synthetic versus qualified/operational boundaries are strong. The material gaps are concrete implementation homes and deployment prerequisites, rather than a reason to reopen the approved product or architecture.

## Review basis

Inspected the canonical manifest and coverage mappings, decision-gate register, Mermaid graph and complete topological order, START-HERE, execution state, both future agent prompts, roadmap, parallel-safety declarations, cross-cutting chapters and detailed task Markdown. Detailed checks focused on T0001–T0009, T0206/T0208/T0209, T0301–T0308, T0401–T0405, T0503–T0507, T0601–T0609, T0701–T0710, T0904–T0914, T1101–T1108 and T1201–T1306. Approved product, architecture and migration contracts were opened only as needed. No original customer-level evidence was copied.

## Material findings

### IR01 — P1: Concrete runtime transports have no clear implementation task

**Evidence:** T0008 scope/contract (task lines 45–55) explicitly supplies a fake independent store; T0206 lines 52–62 supplies a private-file access port and postpones S3 operational use; T1202 lines 49–67 qualifies actual S3 but can edit only qualification tests and its contract. T1201 provisions services, rather than implementing an application driver. The analogous read tasks describe fake-backed mappers/ports (T0301, T0303, T0401, T0904), while actual-account tasks T0308/T0405/T0914 own qualification-test areas. T0702–T0705 describe fake-backed mutation ports/adapters; T0707–T0710 own actual qualification-test areas. The current ownership map does not unambiguously allocate the real HTTP/S3 runtime drivers, supported client versions and composition wiring.

**Consequence:** A fresh agent must either expand a mapper or a qualification task outside its stated boundary, or qualify a test-only client that is not the production execution path. ARC-RECOVERY and ADR-009 coverage links to T1202 are structurally present but cannot alone demonstrate that application dispatch/contact/privacy/seed/file operations use the qualified S3 implementation.

The same gap exists for account mail and diagnostics: T0107 specifies a fake Resend mail port, while T1203's actual-mail task owns only `tests/qualification/identity/` and its contract. T0005 defines Sentry/OTEL ports using no-op local exporters; T1204 says to install monitoring scrubbing but owns release-operation paths rather than the runtime observability package. Allocate real Resend delivery and Sentry/OTEL exporters/wiring explicitly, with local mock-sink/no-message tests and redaction sentinels before controlled operational qualification. The already-implemented Auth0-compatible OIDC path in T0104 is not the same missing-port case.

**Bounded repair:** Add stable tasks for the actual S3/file/recovery adapter and each source read transport, using mock endpoints locally. Add real per-class mutation transport tasks after T0706 no-retry compatibility and before actual qualification. Allocate runtime/package/lockfile/wiring areas explicitly; qualification must exercise the same built driver and pinned client, not a second implementation. Preserve all real-account authorization gates. Suggested IDs accepted for drafting by the primary planner: T0210, T0309, T0406, T0915 and T0711–T0714. Their future production capability remains unqualified until the existing actual-account tasks pass.

### IR02 — P1: Production environment and disabled production release have no prerequisite home

**Evidence:** T1201 lines 43–49 explicitly provisions staging with production endpoints absent. T1204 lines 46–64 deploys only staging. T1207 lines 44–60 then runs production read-only shadow, and T1306 lines 45–60 performs production cutover with only a cutover-document area. Architecture `13-deployment-and-environments.md:12` requires a dedicated production project/workspace, secrets, storage namespace and database. ADR-009's coverage mapping currently names T1201/T1202/T1204/T1205, which does not cover a production environment/release.

**Consequence:** The roadmap silently assumes an operational target exists between staging qualification and production shadow/cutover. Reusing the staging environment would contradict the approved isolation contract; placing provisioning inside cutover would exceed that bounded task and bundle distinct approvals.

**Bounded repair:** Add separately authorized production provisioning and egress-off production deployment/ownership-validation tasks. Consume the approved staging evidence, actual pinned image/schema/contracts, purchased-service/privacy scope and exact production grants/credentials. Make production shadow consume their accepted contract. Keep mutation/contact enablement and cutover approvals separate. Suggested stable IDs: T1209/T1210.

### IR03 — P1: T0008 can rely on database tooling before compatibility is accepted

**Evidence:** T0008 line 5 declares only T0006; T0006 depends on T0002, not T0003. T0008 lines 45–51 require separate DB rollback, and line 62 allocates an explicit SQL migration. A08-DATABASE applies to T0007/T0101, not T0008. The displayed topological order happens to put T0003 first, but the graph permits T0001→T0002→T0006→T0008 while T0003 is still not accepted.

**Consequence:** A valid alternative schedule starts a DB-dependent recovery task before the selected DB/migration/role behavior has been qualified. This violates the prompt's compatibility-before-reliance rule and cannot be repaired by a recommended order alone.

**Bounded repair:** Add T0003/C-T0003-v1 and A08-DATABASE as T0008 prerequisites, or explicitly remove all database work/rollback dependence from T0008 and allocate it to a later task. The first option preserves the current bounded scope.

### IR04 — P1: Staged recovery can test a release that predates its required features

**Evidence:** T1204's dependencies include T1202/T1203/T0307/T0404/T0009. T1205 lines 23–27 additionally consumes T0609, T0913, T1005 and T1106. Those local contracts may merge after T1204 is accepted in another valid graph order. No task then deploys that complete candidate before T1205 runs against actual services. Updating a branch from main does not update an immutable deployed web/worker image.

**Consequence:** Recovery/privacy/seed/repair tests may run against an earlier staging image lacking their accepted implementation, or require an undeclared release action during a validation-only task. Later source drivers and class transports also need explicit release inclusion.

**Bounded repair:** Keep the early disabled staging release if useful, then add an exact complete-candidate deployment before T1205. Its accepted record must bind actual image/lockfile/schema/protocol/feature commits to the required contracts and require matching web/worker versions. Subsequent actual qualification must verify that the deployed candidate contains the driver it tests. Suggested stable ID: T1208. A release revalidation rule must invalidate stale downstream readiness after material contract/image changes.

### IR05 — P2: T0001's clone assertion does not define the private-evidence boundary

**Evidence:** T0001 lines 37–43 says to ignore secrets/generated/private evidence and preserve all planning/source files. Lines 69–74 require a fresh clone to preserve protected paths. START-HERE binds protection to the complete 298-file evidence baseline. `04-repository-structure.md` separately says real customer intake/private test evidence stay out of Git.

**Consequence:** The first agent must decide whether every protected source/evidence file belongs in Git. A fresh clone cannot reproduce intentionally untracked private evidence; treating the clone assertion literally risks committing sensitive originals, while ignoring them appears to fail the test. Preserving files on disk and tracking them in Git need distinct, explicit assertions.

**Bounded repair:** Make T0001 produce a reviewed public/synthetic trackable inventory and private/untracked custody inventory using paths/digests only. Verify the original workspace's entire protected baseline is unchanged; verify a clone reproduces only the approved trackable inventory; prove private paths are ignored and no remote push is part of this task. State the first-repository bootstrap exception to normal branch/main rules without inventing a baseline commit now.

### IR06 — P2: T0605's smallest reading set omits its named fault contracts

**Evidence:** T0605 lines 80–86 requires EA10/EA12/EA16/RV07. Its Relevant specifications section lists architecture fallback/recovery and product requirements, but does not list `docs/migration/09-external-action-safety-validation.md` or `11-recovery-validation.md`. The exact EA scenarios are at migration09 lines 34/36/40; RV07 is in migration11's recovery matrix. Predecessor declarations describe the general boundary but do not provide those ordered experiments.

**Consequence:** The task is understandable, but its promised fresh-context reading set does not define the fault ordering and expected evidence associated with its own test names. An agent must discover an unstated source or guess what the combined phrase “worker/handover race” covers.

**Bounded repair:** Add the exact EA10/EA12/EA16 and RV07 source rows plus relevant experiment-protocol sections to the task reading set; separate their asserted request/issuance/hold outcomes in the tests. No additional product decision is needed.

### IR07 — P2: Many OP/A gate owners are labels, not accountable decision makers

**Evidence:** `decision-gates.yaml:20` sets OP01's responsible decision maker to “OP01 Narrow pilot qualification”; lines 56–446 do the same for OP02–OP14. A01 at line 468 is “A01 — integrated pilot readiness”, and A02–A07 repeat decision names. The protected A01 source row itself identifies “merchant owner + provider-qualified engineer”; MD gates usually retain actual roles.

**Consequence:** The register promises an accountable resolver but provides a topic. A resuming coding agent can identify the blocking gate yet cannot reliably route its decision/evidence or distinguish the merchant, owner, engineering and privacy signers.

**Bounded repair:** Retain original source labels/locators unchanged, but populate responsible decision maker with the source-supported accountable role(s), using owner review where the original product register does not name one. Preserve separate factual evidence review and policy authority. Do not give coding agents authority to sign these decisions.

## Fresh-context paper walkthrough

### T0001 — early foundation

Using only the task, listed architecture sections and no predecessor, the intended action is clear: after local approval inspect the non-Git workspace, preserve evidence, establish a minimal npm workspace and version boundary without installing/scaffolding the application. Node major is fixed and patch qualification correctly belongs to T0002. No live provider or infrastructure is needed. **Walkthrough result: actionable after IR05 clarifies the trackable/private inventory and first-repository bootstrap.** The no-existing-repository stop is sensible for the captured baseline; a later existing repository requires review rather than reinitialization.

### T0504 — workflow

The task and `architecture/07-background-jobs-and-reconciliation.md:33–58` explain reserve → durable independent marker outside the DB lock → current authority/reservation recheck → issued permission. C-T0503 supplies ordinal/eligibility and must fix an independently reviewed synthetic timing/no-call TEST-POLICY; C-T0105 supplies current authority; C-T0008 supplies independent append/coverage; C-T0209 supplies inherited/repair holds. The local permitted scope and T1303 restriction prevent a synthetic Start contact UI from authorizing real calls. **Walkthrough result: coherent on paper; no new product policy or extra direct dependency needed if the actual accepted predecessor contracts contain their promised interfaces/policies.** Tests must count issued authorizations separately from actual calls and keep lost-response uncertainty held; the existing task already requires that behavior. Production OP04/MD08 decisions remain deferred, not silently selected.

### T0605 — high-risk action/recovery

The task, architecture06 lines 79–85 and C-T0604/C-T0206 define the intended boundary: current Admin, known-unstarted or reliable no-effect, contained prior sender, pending exclusive reservation, independent durable descriptor before human permission, then native-result reconciliation into the same scope. Unknown effects remain blocked. LOCAL_SYNTHETIC limits correctly avoid real fallback. **Walkthrough result: boundary understood, but IR06 prevents executing the named test matrix solely from its stated reading set.** Add the exact experiments rather than broadening the task into provider qualification. Actual terminal-negative semantics remain unavailable until the relevant class is qualified; use only an independently fixed fake contract here.

## Checks that did not produce findings

- The Q-BOOKING/Q-REPLACEMENT gate records explicitly require `QUALIFIED_SUPPORTED_CORE`; accepted dossiers with UNAVAILABLE/BLOCKED capability are expressly insufficient. Optional annotation/cancellation exceptions stay unavailable. This distinction is correct and must survive repairs.
- Local fake slices do not require provider accounts. AUTH gates distinguish controlled reads/effects/storage/mail, staging, shadow, actions, contact and cutover. Operational task accountable roles prohibit coding-agent self-approval.
- The three recommended parallel pairs have distinct edit/lock areas and explicit integration-owner/current-main restrictions. No overlapping same-ID concurrency is authorized. Root package/router/migration changes still need allocated locks.
- The catalog retains OD01–OD09 distinctions, focused actor list/detail/journey work, source uncertainty, migration/history closure, inherited contact/action holds, repair union-of-scopes, privacy replay suppression and explicit deferred-feature containment. I found no justification to drop those safeguards or reopen approved scope.
- Future application checks are labelled PLANNED and actual completion evidence is empty. No future runtime test was represented as already executed in the inspected draft.

## Required closure

The primary planner has acknowledged IR01–IR04 and proposed new stable task homes; these were proposals at review time, not verified changes. Recheck generated tasks, dependency/gate/coverage updates, deployment-image freshness and source digests after incorporation. Re-run the static verifier and its negative controls separately. Close IR05–IR07 or document a source-grounded bounded disposition. Only then may this review support presenting the plan for human approval; it never authorizes implementation.
