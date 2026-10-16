# OpsHub — merchant configuration and policy

**Draft requirements.** Configuration is justified by merchant/source differences; independent facts, OD06 cardinality and OD07 authority are not adjustable preferences. [Gentry BRxx](../reconstruction/05-business-rules.md) and [PDxx](../domain/07-policy-decision-register.md) provide evidence/questions, not universal defaults.

## Configuration boundary

| Configuration / rule | MVP treatment | Authority / reason |
|---|---|---|
| Merchant identity, designated Admin/billing contact and source ownership | Required explicit values; one workspace is the operational merchant boundary; multi-store/shared source cases await OP02 | Merchant Admin confirms business/source ownership; platform manages account state |
| Operational timezone and currency | Required; proposed pilot Cairo timezone/EGP only if merchant explicitly confirms; no silent currency filling or conversion | Admin; clocks/money must be comparable |
| Calendar/cohort definitions | One named reviewed MVP definition set; calendar as proposed in 06; no arbitrary denominator editor | Admin chooses only supported approved options; OP07 |
| Calling policy | Approved maximum three total contact attempts, including successful ones, approximately 24 hours apart over 48 hours; fixed MVP default. Reopening does not reset the same objective. No Admin bypass; higher limit requires future owner change | OD04; exact timing tolerance and exception-attention treatment OP04 |
| Queue priority/assignment | Due-first/earliest due proposed; Admin assigns/reassigns; no generic workflow builder | New product proposal responding to conflicting oldest/newest Gentry guidance |
| Pickup ageing / unbooked / stale-input attention | Preserve proposed pickup/unbooked attention values and clock basis pending OP08. Qualify separate commerce/courier/spend freshness and action-result targets for the integrated pilot; daily fallback files retain coverage/as-of | Historical3/7d and live10+/3d remain scoped observations. Earlier daily-file24h assumption does not become integrated-source SLA. Attention only, no automatic cancellation |
| Source field/status/identity mappings | Approved source-specific mapping, coverage and physical/final outcome evidence requirements | Admin approves; unknowns reviewed, never silently mapped |
| Source authority/manual overrides | Source-specific selection for each concept; competing claims and manual correction reason retained; no blanket newest-wins | Admin; OP10 must approve pilot authority matrix |
| Operational reason taxonomy | One basic purpose-specific taxonomy plus Unknown/Other and preserved source labels; Admin approves changes | Reached customer cause separate from courier exception; legacy values retained |
| Consequential action policy | Admin-only; reviewed intent, changed-intent reapproval, per-effect evidence and failed/unknown recovery | OD07; cannot delegate to Operator via MVP setting |
| Episode cardinality | At most one outbound/zero-or-one return/zero-or-one pickup per order | OD06; not merchant-configurable |
| KPI formulas | OD05 fixed; population/time/finality qualifications visible | No merchant switch that redefines a canonical label |
| Pickup collection versus payment; order versus shipment; per-case resolved | Fixed independent dimensions | OD01–OD03; never configurable into equivalence |
| Prices, plan and entitlements | Manual reviewed commercial record; no fabricated prices/quota | Platform commercial authority; OP11 |
| Product/SKU analytics, attribution/economics and tax basis | MVP: reviewed item/product/outcome mapping, revenue adjustments, direct/generic/unallocated spend method, currency/tax/effective scope and meaningful analytical season context | Admin-only significant policy changes; OP09 qualifies methods. No unapproved Gentry numerical defaults |
| Rich season management / tiers / restock / production automation | Necessary supplied season/classification context is analytical MVP; richer season CRUD/bulk assignment SHOULD HAVE. Automated tier/replenishment/production decisions remain LATER | OD09; source cost/stock/season observations do not authorize recommendation engines or adopt2.8/3.8/20/.15/1.7% policies |
| Privacy/retention/export and account suspension access | Narrow role-based visibility proposal; approved retention/availability policy required before pilot | OP11/OP12; no technical implementation chosen |

## Change behavior

CFG01 — Show value, meaning, unit, clock/population, applied version/effective time, authority and reason. Historical source setting and approved OpsHub setting are distinct.

CFG02 — A significant operational/economic or source-authority change requires Merchant Admin. Platform cannot change it as a support shortcut. Before acceptance, show affected merchant, current/new value and impacted work/metrics.

CFG03 — Do not silently rewrite past contact events or prior KPI exports when policy changes. Existing cases retain the applied calling policy; Admin can review attention/eligibility with reason/history but cannot lift or reset OD04's MVP three-contact ceiling for the same objective. A future owner-approved rule can change later queue projection without claiming a past event changed.

CFG04 — Undefined source/finality mappings produce unknown/review states. Missing required readiness values block the affected capability and explain how to finish configuration; unrelated valid work can continue.

CFG05 — Fixed approved defaults remain operationally usable while exact pilot tolerances/thresholds await owner review of this draft. Thresholds in this document are recommendations, not additional APPROVED MVP DECISIONS. They must not become hard-coded historical Gentry facts.

Before launch, qualify OP01/OP09's integrated-source and analytics details plus the existing OP02–OP08/OP10–OP13 choices as applicable. Integrated core and Product/SKU/ROAS priority are approved under OD08/OD09. See [13](13-open-product-decisions.md).
