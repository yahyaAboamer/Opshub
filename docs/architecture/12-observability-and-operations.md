# OpsHub — observability and operations

**Proposal:** structured redacted logs, a small explicit metric set, selected correlation traces and restricted platform health projections. Monitoring is separate from business audit. Unknown effects and incomplete coverage are visible even when HTTP/process health is green.

## Signals

| Signal | Required content and use |
|---|---|
| Request/job logs | UTC time, environment/release, safe correlation/work/effect IDs, tenant pseudonym, category/state, duration and sanitized error code; never bodies/tokens/contacts/narrative/signed URLs |
| Request/service metrics | Error/latency, connection-pool/DB health, worker heartbeat, oldest ready job, queue depth, missing eligible domain-run work and retry/dead-letter counts |
| Integration health | Capability state, authorization expiry/category, last receipt/accepted/source-as-of, requested/observed coverage, sync cursor age, rate deferral/schema mismatch |
| Action health | Unstarted/started/async/unknown/no-effect counts and oldest unknown age; reconciliation progress, duplicate-effect discrepancy and pre-dispatch journal failures |
| Trust/analytics health | Conflicts/unmatched/unsupported counts, source coverage/freshness, projection lag/generation/version, unavailable/provisional spend/ROAS |
| Export/retention health | Job failure/age, forbidden download, object expiry/hold, backup age/restore-drill result and approved deletion-manifest status |

Use low-cardinality global metrics by provider/job type/result/release. Per-tenant detail belongs in access-controlled Postgres health summaries/log searches, not unrestricted metric labels. Platform summary contains administrative IDs/names/status, counts/watermarks and redacted failure categories; no contact/order narrative, operational value drill-down or credentials.

Hosted Sentry captures explicitly scrubbed errors and selected transaction traces; structured hosting logs handle ordinary diagnostics. OpenTelemetry spans can link API → committed work ID → worker → provider read/effect → reconciliation, without copying payloads. Queue/library traces do not establish effect success. Keep business health metrics in the platform projection initially; no separate Prometheus/collector/dashboard fleet required. [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/), [Sentry project scrubbing controls](https://docs.sentry.io/api/projects/update-a-project/).

## Alerting and visibility

Immediately surface unknown/duplicate external results and unauthorized effect attempts as merchant Admin attention and actionable platform redacted incidents. Operational alerts cover absent worker, increasing queue/domain-run age, failed sync/authentication, sustained stale coverage, DB/storage failure and failed backup/restore checks. Exact thresholds/notification routing/on-call owner need A06/OP13; no broad alert on every unchanged poll. Aggregate alerts group repeated same-incident failures and include safe run/release reference and next owner.

Product work stays in-app; infrastructure incident notifications to the authorized team are an operational service proposal, not automated customer messaging. Audit captures consequential decisions/history durably; debug logs can expire without losing the ability to explain approvals/results. Alert acknowledgement cannot close a merchant case or certify an unknown effect.

## Recovery playbook contracts

| Incident | Safe initial action / recovery evidence |
|---|---|
| Provider outage | Defer safe reads/new dispatch, retain prior data as stale, retry qualified reads; never mark unknown mutation no-effect |
| Expired/compromised credential | Disable connection dispatch, revoke/rotate with Admin ownership verification, then reconcile existing effects; reconnect does not approve them |
| Unknown mutation | Hold objective, quarantine old execution, gather qualified provider result/negative proof or escalate to Admin/provider; no generic job redrive |
| Parser/schema drift | Stop affected interpretation/capability, retain original typed/raw evidence within policy, update adapter fixture/schema revision and safe replay |
| Projection discrepancy | Preserve published generation, compare contributor/evidence/method, rebuild new generation; no silent revision of retained export |
| Cross-tenant suspicion | Revoke suspect session/key, suspend affected access/dispatch as appropriate, preserve safe audit; investigate using restricted evidence, never dump all tenants |
| Database loss/restore | Enter global mutation-egress-off recovery mode;13 requires dispatch-journal/provider reconciliation and no restored job replay before release |
| Object storage unavailable | Export/upload defer; mutation journal fails closed before send. Read-only operational work may continue; uncertain storage writes remain unresolved |

Health endpoint exposes only service readiness, not tenant data/credentials. Manual support can locate safe correlation IDs within assignment scope. Infrastructure console/backup/customer payload access is restricted to authorized operators with MFA; product Platform Admin status alone does not authorize those credentials.
