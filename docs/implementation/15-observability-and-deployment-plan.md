# Observability environments and deployment

The complete deployment chain is explicit: T1204 early disabled staging read slice; T1208 complete reviewed staging candidate; T1205 recovery/security evidence; T1209 distinct purchased production environment; T1210 exact disabled production candidate and storage/current-owner probes; T1211 production identity/controlled-invitation proof; then separately authorized T1207 read shadow. Changed relevant driver/client/protocol/current authority invalidates affected evidence. Unchanged artifact attestations plus integration regressions may preserve scoped qualification across unrelated image changes.

T0005 introduces redacted request/job/release correlation immediately. Later sync/action/contact/export/migration tasks add owned health events alongside behavior. Signals distinguish process readiness, provider receipt versus source coverage/freshness, job eligibility/age, projection lag, unknown effects, marker/seed/privacy coverage and migration dispositions. Tenant detail stays access-controlled; unrestricted metrics have low-cardinality categories only.

Sentry/OpenTelemetry ports initially use local no-op exporters; real scrubbing/retention/cost/region/on-call routing are reviewed in T1201/T1204. Unknown/duplicate effects and unauthorized starts create merchant Admin attention and safe platform incidents. No unchanged-poll notification spam or customer outreach.

Local/CI use synthetic fixtures, fake OIDC/mail/provider/storage and disposable real PostgreSQL. No live provider account is required. T1201 may be scheduled after M0 for controlled staging qualification: paid Render web/API+worker+PostgreSQL17, private Amazon S3, separate Auth0/Resend/Sentry and environment-specific secrets. Actual service procurement/provisioning needs explicit permission. Production secrets never enter local/CI.

T1202 qualifies storage protection/independent coverage. T1203 qualifies hosted identity and bounded invitation mail. T1204 deploys a reviewed immutable staging image/schema with target/lock/version checks and all action/contact egress off. T1205 restores into a new isolated DB and proves current authority/privacy/access versus egress gates before real reliance.

T0308/T0405/T0914 then qualify actual controlled reads. T0707–T0710 require separate exact-effect envelopes and staged recovery proof. Production read shadow, individual action/contact enablement and cutover have later distinct approvals. Real credentials are needed only at those scoped environment tasks.

Release migrations are reviewed explicit SQL, schema-owner only, serialized expansion before compatible app/worker. Destructive contraction waits a reviewed rollback window; runtime never auto-syncs schema. Graceful shutdown/old-sender termination cannot release unknown reservations by lease expiry. Compatible application rollback retains newer effects, holds, privacy and recovery epoch; incompatible protocol means disable egress and forward repair.
