# Controlled provider qualification plan


## PC-C01 — Provider acquisition closure qualification

Apply MP-ACQ01 separately to Shopify order/line/product connections, Bosta account/detail/history and Meta report pages/async completion. Document actual cursor/snapshot/order/timestamp tie semantics, late visibility/revision bounds, child completeness, authoritative removal and initial→incremental continuity. Inject changes between pages, cursor restart, exact-cutoff ties and late observations in mocks/controlled tests; compare independently fixed native identity/revision sets.

A granted read scope plus exhausted pagination does not establish complete historical or open-work coverage. Missing provider guarantees require qualified reconciled exports/inventory or an explicit unresolved coverage hold. No numerical overlap window or provider finality guarantee is invented here. Current object removal is accepted only from a qualified authoritative record/complete parent revision, preserving history.
**Future controlled tests, not executed in Phase 5.** Start with [Phase 4 capability review](../architecture/18-provider-capability-review.md), A01/A02/A07 and actual pilot ownership. Public documentation is insufficient proof of account capability, current field meanings, uniqueness or no-effect recovery.

## Qualification envelope and authorization

Each PC record identifies provider/account/merchant/environment, exact action/read capability, pinned API/schema/client versions, granted scopes/distribution, test identities, authorized side effects, correlation/idempotency semantics and retention, callback authentication, read/result/negative-evidence contract, error taxonomy, cleanup/recovery plan, tester/responsible Merchant Admin, source docs checked date, expected/actual native references, sanitized evidence digest and pass/limited/failed/blocked status.

First run mocks/schema fixtures; then read-only controlled-account tests; then separately authorized nonproduction or tightly bounded synthetic pilot effects. Block real customer communication/financial/physical operations outside the experiment's approved scope. A development “test” order may still trigger a native courier connector; inventory all automations first. No broad provider write credentials or trial fixture imply safe isolation.

## Shopify qualification

| ID | Test and expected evidence |
|---|---|
| PC-S01 auth/scopes | Prove store ownership, app distribution/token refresh/protected fields and minimum granted read/write permissions. Wrong/expired/revoked scope gives controlled limited state, no cross-store read |
| PC-S02 initial sync/history | Exhaust pagination, nested line pagination and fixed coverage; native Order/LineItem/customer/product/variant IDs and currency. Requests outside granted history explicit, never silently truncated |
| PC-S03 incremental | Create/update/cancel/refund/product changes in authorized synthetic context; out-of-order/lost events recovered by qualified reads/overlap. Source update/capture clocks distinct |
| PC-S04 webhooks/duplicates | Raw-body authenticity, store binding, delivery versus logical event IDs; same receipt twice/out-of-order receipt no duplicate object/effect; forged/wrong-account rejected safely |
| PC-S05 catalog | Duplicate/mutable SKU/name, deleted/unavailable variant, multiple identical lines; retain native identity/parent and source snapshots |
| PC-S06 cancellation | Eligible/ineligible synthetic states; reviewed refund/restock/notification/authorization-release consequences; ack/job/result distinction. Unapproved unavoidable consequence blocks capability |
| PC-S07 replacement creation | Exact new Order/item/COD/payment/discount/inventory/notification settings; distinct original link and create-time correlation marker; booking/annotation are independent effects |
| PC-S08 annotations | Add/update required tags/notes/metafields without erasing unrelated values; stale digest/version behavior; marker native read/lookup verified. Annotation alone not evidence of creation |
| PC-S09 error/idempotency | Validation/auth/throttle/transport errors; test exact operation-specific idempotency support/parameter mismatch/key lifetime if documented. No universal orderCreate/orderCancel write-retry assumption |
| PC-S10 ambiguous result | Drop response after provider accepts; positive native recovery via qualified marker/job/object binding. Empty/incomplete search is not no-effect. Old sender quarantined; retry/manual path blocked until qualified result |
| PC-S11 privacy/uninstall | Forged/duplicate privacy request, source-scoped handling and independent manifests; uninstall/revocation blocks new starts while uncertain results remain held |

Shopify [Order documentation](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) rechecked14 October2026 confirms default60-day access with older-access qualification. Select a reviewed stable version at future execution, rather than testing against a moving latest contract.

## Bosta qualification

| ID | Test and expected evidence |
|---|---|
| PC-B01 account/key | Verify native business/account ownership, HTTPS/auth header/read/read-write/full scopes and revocation. Read key cannot create shipment |
| PC-B02 create | Synthetic reviewed payload/service/purpose/address/COD/package; native delivery ID/tracking/business reference returned and read back. Actual logistics excluded unless separately authorized |
| PC-B03 reference/identity | Duplicate businessReference and string/numeric tracking forms under controlled contract; establish uniqueness/reuse/lookup bounds rather than assuming enforcement |
| PC-B04 status/history | Complete paginated read/detail/native coverage, service-specific finality and timestamps; attempt counter versus independently identified history |
| PC-B05 callbacks | Configured auth/account binding/retry/order/native event or revision identity; duplicate callback no duplicate state/effect. If signature/replay guarantees absent, qualified authenticated read corroborates |
| PC-B06 outcome/attempt | Outbound/RTO/customer-return/exchange/physical collection distinctions; “Picked up” and Delivered meanings tested by service. Counter cannot fabricate events |
| PC-B07 termination | Optional cancellation/termination support, native eligibility/scope/result/physical consequences; separately gated, no assumption of Shopify equivalence |
| PC-B08 return/pickup | Supported optional return/exchange/business pickup purpose/capability/fee/finality; distinguish business parcel collection, consignee return pickup and merchant/customer handover |
| PC-B09 ambiguous create | Inject success/lost response then recover positive delivery identity via exact correlation/read/provider support evidence; absence/repeated callback insufficient for no-effect |
| PC-B10 competing booking | Exercise current Shopify→Bosta native connector and manual process in controlled context; identify exactly one normal booking authority. Replacement creation must not trigger unintended duplicate automatic booking |
| PC-B11 errors/rates | Account-specific limits/error/no-effect classifications and schema drift; bounded reads, no generic SDK write retry or lease-expiry resend |

Bosta's [callback guide](https://docs.bosta.co/docs/how-to/get-delivery-status-via-webhook/) rechecked14 October2026 describes service-dependent states and attempt counters. It does not by itself establish pilot uniqueness, event history or an exhaustive no-effect search.

## Meta qualification

| ID | Test and expected evidence |
|---|---|
| PC-M01 auth/access | Qualified read-only permission/token/account ownership/expiry/revocation and actual current approval requirements; no ad/budget mutation |
| PC-M02 spend | Retrieve selected nonoverlapping account/campaign/ad report grain with native IDs, spend/currency, fields and full pagination/async completion |
| PC-M03 windows | Exact since/until boundary/timezone/time_increment/breakdown/attribution-report parameters; provider daily aggregates cannot silently be rebucketed |
| PC-M04 revisions | Repeat same recent and closed periods; record revised amount/as-of/series version, actual delay behavior; no claimed finality SLA |
| PC-M05 currency/basis | Prove account currency/tax/report amount basis; no inferred VAT inclusion or silent FX |
| PC-M06 mapping | Native catalog/product links actually available versus mutable names; collisions and unallocated spend. Revenue eligibility is separate from spend-to-product mapping |
| PC-M07 rates/errors | Pagination interruption, auth expiry, throttling, invalid parameter combinations/schema drift; partial report never complete/missing→zero |

Meta's [official reporting request](https://www.postman.com/meta/facebook-marketing-api/request/gdbk43j/getreportforinsight2) rechecked14 October2026 exposes spend/account_currency and reporting-window parameters. This is contract evidence, not account access or SKU attribution certification.

## Pass and capability gating

A read capability passes only with owned namespace, truthful coverage, stable IDs, duplicate/revision behavior and redacted failure evidence. An action capability additionally needs current Admin authority, reviewed side effects, one normal mutation authority, durable pre-dispatch marker, result/unknown recovery, old-process containment, kill switch, monitor/escalation and proven recovery/restore plan.

A known unsupported optional operation remains unavailable with qualified safe fallback. Required core Bosta booking/Shopify replacement/read round trips and MVP Product/ROAS inputs cannot be permanently replaced by manual copying to claim OD08/OD09 integrated readiness. Missing safe unknown-result resolution is a release blocker for that action, not permission to blind retry. Sign-off [14](14-reconciliation-and-signoff.md); sequencing [12](12-shadow-and-parallel-run.md).
