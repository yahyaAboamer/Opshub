# Normalization, data cleaning and row dispositions


## Current privacy and interpretation quality

Every normalized/asserted field checks MP-PRIV01 current privacy scope before it can become accessible. A suppressed unit still has a disposition and reason/minimal safe locator; do not hide it from count reconciliation. Unique evidence under an approved restricted hold is distinct from ordinary access.

Complete source capture is not complete interpretation. An unmapped finality/physical outcome that could alter a denominator makes the calculable known-subset result **provisional**. A positively known pending state under an approved mapping can coexist with a complete known-population final ratio. Unknown subject/denominator that cannot support a valid subset makes the result unavailable. Apply trust state consistently to display, contributor detail and export.
**CL01:** preserve original evidence and record transformations. Normalization cannot increase evidentiary certainty. Never silently discard an invalid row, manufacture missing facts, or substitute a spreadsheet-derived output for source truth.

## Rules

| Area | Deterministic contract / exception |
|---|---|
| Dates/timezones | Preserve original string/Excel epoch/date precision; parse only declared format. Known-zone instants → UTC plus source offset/zone. Ambiguous day/month, missing zone or DST ambiguity → qualification/hold; no default midnight event. Date-only can join an approved date cohort, cannot prove contact spacing. Reject impossible calendar values explicitly |
| Clock basis | Occurred/effective/source-updated/observed/ingested/calculated differ. Export date and maximum source date are not TODAY, call occurrence or consent entry |
| Currency/money | Exact decimal strings with sourced currency and tax/net/gross basis. Evidenced zero, null and negative adjustments differ. Merchant default cannot fill missing transaction currency; no silent FX/VAT uplift. Missing/incompatible basis holds affected monetary metric/action |
| Phones | Preserve original privately; normalized candidate only using explicitly supplied country/format rules. Ambiguous local/international/extension values stay qualified. Phone is never customer/case/order identity; scoped pseudonym is still protected data |
| IDs | Preserve strings, type and leading zeros; no scientific-notation truncation, float rounding, prefix stripping or numeric fallback equality. Already-truncated Excel ID remains ambiguous; original native re-acquisition/crosswalk required |
| Missing values | Distinguish absent column, blank, explicit null, source N/A/error, evidenced zero and not applicable. No blank-to-zero fee/spend or no-row-to-failure |
| Duplicated rows | Same snapshot locator replay is known duplicate. Qualified native object/revision repeated across captures is duplicate observation/change no-op. Identical contact narrative/time or wallet tracking does not prove duplicate real event/charge |
| Malformed exports | Validate delimiter/encoding/headers/quoted fields/continuation groups, actual occupied cells rather than stale worksheet dimensions; reject unsupported macros/external execution. Truncation/page gaps mean incomplete coverage, not zero records |
| Status vocabulary | Retain source state/type/code/exception and mapped concept/version. Unknown/obsolete/conflicting state → unresolved concept, visible count; never substring “deliver” classification for current truth |
| Courier exceptions | Service/purpose-specific mapping, independent of source reason reliability and contact root cause. Same code may have different physical meaning; neither an exception nor reverse Delivered proves original outbound RTO |
| SKU/product aliases | Preserve spelling/raw label; normalize search candidate only. Name/SKU collision, quantity parsing or historical reparenting needs native evidence/review. Unlimited native line items take precedence over four-slot legacy derived parser |
| Historical formulas/errors | Preserve formula/cache/error and locator. Current/v3 lack caches; no false computed zero. Chart-suppression #N/A differs from broken operational formula. Model/proxy fee/value is historical output |
| Contact summaries | Keep cumulative count and last asserted date privately with precision; do not synthesize events or age-reset budgets. Counter inconsistent with known events → unresolved budget/hold |
| Confirmation/collection | Tags/paid/Resolved labels remain assertions unless approved entry/physical/action-evidence rules accept them; keep excluded/unknown counts |
| Spreadsheet injection/control text | Treat input as data, never executable script/formula. Future CSV/export neutralizes formula-leading cells without changing protected source; retain safety transformation. Bound size/decompression/row lengths; failure counted |
| Seasons/stock/costs | Preserve observation date/source/grain and historical assignments if evidenced; unknown history stays unknown. Current values never backfill prior periods silently |

## Mutually exclusive primary dispositions

For every data row/API object (including invalid and duplicate units), persist exactly one **primary disposition** at that run revision, plus independent warnings/conflict flags and field-level qualifications.

| Disposition | Meaning / activation |
|---|---|
| accepted | Required identity/schema/concept evidence valid under approved mapping; may contribute to validated generation |
| accepted with qualification | Core identity valid; explicitly bounded uncertainty in nonrequired fields. Only eligible facts/metrics activate; uncertainty is visible |
| duplicate of known identity | Reference original accepted binding/observation/group and duplicate basis. No new business object or double contribution |
| unresolved | Evidence retained; coverage/conflict/chronology/native-scope prevents interpretation. No trusted affected fact/effect activation |
| rejected | Unsafe/unparseable/nonbusiness/unsupported unit, with reason and private locator; retained/accounted under approved policy |
| requires manual mapping | Plausible subject/policy candidates require current authorized decision; no auto-binding |

Imported formula/helper rows and file headers are structural units, counted separately with exclusion reason. A physical row is not necessarily a logical Order or observation. Report source physical units, structural units and accounted data units separately.

**Conservation:** data units = accepted + qualified + duplicate + unresolved + rejected + manual mapping. Expanded normalized assertions/items can outnumber source rows; grouped Orders can be fewer. Retain a source-unit→group→assertion→canonical-object bridge; a row may contribute multiple facts but has only one primary disposition. Conflicts/chronology warnings are orthogonal and cannot be added as another row total.

Unreadable whole file has file-level rejection with byte count and **unknown row count**, never a invented zero. Parsed units before truncation are held until coverage is qualified; report unknown remaining count. Native paged acquisition records requested/observed coverage and unaccounted page failure.

## Historical corrections

Preserve original assertion, corrected value, correction source/locator, concept/effective scope, reason, claimed actor, occurred time, recording actor/time, evidence confidence and selection policy. Missing values say unknown, including reason/actor/time; do not assign today's importer as historical author. A correction can be retained without being selected.

Admin acceptance creates a **new current selection decision**, explicitly dated now and scoped to merchant/concept. It never authenticates the historic claimant or proves physical payment/collection occurred. Late source evidence competes under MD01, not last-arrival precedence. Reversing/remapping correction appends a superseding interpretation, retained evidence and impacted-generation list.

## Qualification versus rejection

An unknown phone in an otherwise valid historical sale may permit qualified commerce analytics but blocks contact/action requiring that recipient. Unknown courier finality excludes the shipment from final-outcome denominator while preserving pending/unknown visibility. Unmatched wallet rows remain evidence; do not force an Order. A duplicate additional outbound result is preserved as a physical discrepancy, though a second accepted outbound association is forbidden. Acceptance of evidence does not equal operational approval.

Required future tests CL-T01 exact conservation; CL-T02 malformed final line and stale Excel dimensions; CL-T03 leading-zero/long IDs; CL-T04 DST/date-only spacing; CL-T05 zero/negative/missing money; CL-T06 same-text real contacts; CL-T07 correction without actor; CL-T08 formula/error cell; CL-T09 unknown state; CL-T10 truncated file with unknown remainder. Each checks disposition, original retained value, canonical eligibility and contributor exclusion reason.
