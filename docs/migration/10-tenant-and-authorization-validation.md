# Tenant isolation and authorization proof matrix


## TI21/AU13 — Repair, seed and suppression boundaries

Use the logical supplement's actual MA/MB Order/Customer/Variant observations with repeated native text/aliases but separate accounts, plus repeated same-variant line IDs in one Order. Assert distinct tenant bindings and two distinct Items. Test cross-tenant substitution in migration-safety-seed/repair/privacy descriptors: no foreign reservation/allowance/disposition applied or disclosed.

Current Merchant Admin accepts migration/remap source decisions only within their merchant; independent storage writer identity does not become business approval. Completed privacy scope remains enforced on all old/new runs and download generations. Test MD09 current authority after a seed was signed and before transfer, including revocation and Platform Admin substitution.
Authority: [tenancy/RLS](../architecture/03-multi-tenancy-and-identity.md), [composite ownership](../architecture/04-data-architecture.md), [PER01–PER07](../product/02-personas-and-permissions.md), OD07. Use two synthetic merchants with repeated external display references/SKU/phone sentinels, distinct canonical ownership, MA/MB Admin/Operator, scoped Platform Admin, dual-context User and suspended memberships.

## Two independent layers

**DB proof:** real PostgreSQL17/pinned implementation version, nonowner/nonsuperuser/no-BYPASSRLS runtime roles, forced RLS and invoker views; correct MA transaction context deliberately queries/writes MB rows without tenant predicates. Missing context denies. Inspect all new table/projection/file/evidence/anchor grants and composite FKs. Pool reuse MA→MB→missing context cannot leak settings.

**Application proof:** forged route/body/header/IDs, unsupported capability, revoked/current context and relationship requests fail before disclosure/dispatch. Test direct API/worker/download paths, not hidden buttons. DB denial does not substitute for a guard, and a correct guard does not substitute for RLS. RLS does not claim to contain arbitrary SQL by someone holding a trusted runtime credential and changing session context.

## Isolation matrix

| ID/surface | Application attack and expected result | DB/storage/background proof |
|---|---|---|
| TI01 direct ID | MA reads/updates/deletes MB opaque ID; nonenumerating denied/not-found, zero side effect | Deliberately unfiltered SELECT/UPDATE/DELETE under MA sees/modifies zero MB rows |
| TI02 list/search | Forged merchant filter/full-text/search/count/autocomplete/export query | RLS blocks foreign rows/counts; pagination/facets/suggestions carry only MA population |
| TI03 relationships | MA item/case/effect/return/replacement points to MB parent | Guard rejects; composite FK/anchor tenant checks reject cross-tenant association |
| TI04 imports | Filename/row/native-account says MB while MA run owns scope | Verified namespace/run ownership governs; reject/hold foreign group; RLS write checks, no imported platform/user grants |
| TI05 exports | MA uses MB requester/scope/run ID, export queued before suspension | Current authorization at generation/download; RLS on run/contributors/file metadata; no MB object produced |
| TI06 files | Guess storage key/ID or reuse revoked/switch-tenant access | Private no public listing; authenticated tenant metadata first, authorized session download; object namespace/policy and safe error verified |
| TI07 projections | Read MB generation or mixed tenant publish | Tenant FKs/RLS and atomic generation enforce isolation; current result never joins MB evidence |
| TI08 KPI contributors | MA drill-down/export uses MB contributor/native key | Contributor set entirely MA with same generation; RLS+ownership anchor proof |
| TI09 jobs | Tamper queue merchant/connection/effect IDs; trusted type wrong tenant | Envelope not authority; checked business binding establishes context; separate tenant pool rejects wrong rows, zero request |
| TI10 webhooks | Valid provider auth but wrong account/tenant claim | Verified connection binding sets tenant; payload merchant ignored; mismatch held safely before any domain change |
| TI11 cache/client | Merchant switch/logout/suspension during outstanding request | Keys include tenant/permission/revision; late MA response cannot render in MB; purge contact state/download refs |
| TI12 Platform Admin | Platform context requests order/contact/action/import/raw-payload routes | Control-plane grants exclude operational tables/effects; only allowlisted scoped administration/health available |
| TI13 merchant switching | Shared User MA Admin/MB Operator forges selector or reuses approval | Recheck current membership/capability per route; no global tenant variable or inherited MA authority |
| TI14 logs/support | Deliberate wrong-tenant error/raw payload/token/phone sentinels | No foreign record details in errors/logs/traces; platform diagnostics redact contacts/narratives/URLs |
| TI15 restore/backup | Restored old IDs/files/grants accessed before recovery | User access denied until epoch/current authority/privacy replay; backup/object access restricted outside runtime |
| TI16 source/account rebind | Same external native ID account rebound to MB | No automatic old-history transfer; explicit ownership review and retained namespace, unique active owner |
| TI17 views/pools | Query invoker view and reused DB connection after error/rollback | All tenant tables including observations/anchors/contributors forced RLS; transaction-local settings reset; missing context fail closed |
| TI18 aggregate/admin health | Platform asks arbitrary metric join/customer drill-down | Dedicated safe aggregate only; no raw-data control-plane SELECT even if aggregate service fails |
| TI19 asynchronous file generation | Permission revoked while export running/download issued | Reauthorize before publication/download; invalidate availability; no “approved once forever” bearer file path |
| TI20 privacy mapping | Customer same phone in MA/MB; MA redaction/request | Verified source-scoped native identity only; no foreign disclosure/deletion; manifest/app/DB ownership agrees |

## Authorization matrix

| ID/action | Merchant Operator | Merchant Admin | Platform Admin in platform context |
|---|---|---|---|
| AU01 own operational read/contact/evidence | Allowed within current active membership/policy | Allowed within merchant | Denied customer operational access |
| AU02 prepare/request booking/cancel/replacement | Allowed prepare/request only | Allowed prepare/request | Denied |
| AU03 approve/dispatch consequential action | Denied direct/API/worker path; zero requests | Exact current merchant authority + reviewed intent/capability/dependencies | Denied, even if platform can provision/suspend merchant |
| AU04 accept consequential manual result/significant correction/mapping/economics | Denied acceptance; may submit evidence under policy | Current scoped review and audit | Denied merchant acceptance |
| AU05 import/sync | Approved read/mapping scope only, zero business mutations | Current approved mappings/connection authority | No customer migration access by default |
| AU06 export | Contact-free allowed only current scope | Explicit contact-bearing scope/step-up/current auth/policy | Redacted administrative diagnostics only |
| AU07 membership suspension | Next request/unstarted contact denied per selected policy | Suspended approval invalid; next unstarted effect denied | Revoked assignment denies admin routes; other memberships independent |
| AU08 platform operations | Denied absent independent assignment | Merchant role does not confer platform rights | Only assigned capabilities/targets; no self-grant/recovery impersonation |
| AU09 worker | Automation origin grants no business authority | Worker validates recorded approval/current membership before every unstarted effect | Platform credential/assignment cannot substitute |
| AU10 dual-context identity | Each context uses its own active relationship | Merchant authority only via explicit membership route | Platform session cannot borrow merchant grant silently |
| AU11 invitation/recovery | Forged email/used token/last-Admin race denied | Authorized member process; no lost-history authority fabrication | Narrow verified recovery procedure, no grant to self |
| AU12 suspended continuity | Policy-gated, unresolved OP11 access | Proposed bounded safe read/result reconciliation only where approved | Safe scoped health/recovery; no business mutation |

AU07/AU12 must use approved OP11/MD09 service-access policy; pending policy blocks launch, not role tests. Authentication alone never proves membership. Denial audit uses safe actor/category/correlation, never the forbidden target's contents.

## Pass evidence

For each TI/AU row retain actual request/command, role/grants/context, expected versus actual disclosed field sets/row counts, relationship integrity, changed-row count, provider request count, private-object availability, log sentinel scan and pass/fail. A missing surface test is “not executed”, not passed. Test RLS read **and** write checks under real roles, application guards independently, and browser late-response races.

Zero unexplained cross-tenant observation/modification, unauthorized consequential dispatch or sensitive export. Aggregate redaction and global User/IdP records use their approved control-plane visibility rather than invented merchant ownership. Phase 5 is the matrix specification, not proof the future application passes it.
