# OpsHub — MVP feature prioritization

**Draft scope.** MUST HAVE — MVP means required for the coherent daily operational product. SHOULD HAVE — shortly after MVP has value after that workflow works. LATER needs additional policy/evidence or a separate product commitment. EXCLUDED will not be pursued in this MVP. Domain vocabulary is not a requirement to implement every canonical concept.

| ID | Module / bounded capability | Priority | Why / dependency |
|---|---|---|---|
| MR01 | Assisted merchant/workspace creation, initial Admin, readiness and activation | MUST HAVE — MVP | A merchant must reach first usable work; source ownership and verified Admin required |
| MR02 | Sign in/access, merchant memberships, invitations, role changes/suspension, context selection | MUST HAVE — MVP | SaaS shell and authority; two merchant roles, separate platform scope |
| MR03 | Orders/items, source identifiers, lookup/filter and independent status/history | MUST HAVE — MVP | Central daily job; no guessed source links or global resolved order |
| MR04 | Focused data-quality/cleanup attention and Admin correction requests | MUST HAVE — MVP | Missing/conflicting inputs and unbooked/return/pickup exceptions must be actionable |
| MR05 | Confirmation process and explicit evidence | MUST HAVE — MVP | Pre-dispatch daily work; process-entry denominator required |
| MR06 | Per-case contact queue, attempts, reach/reasons and required-action completion | MUST HAVE — MVP | OD03/OD04; keeps reached-but-unfinished work visible |
| MR07 | One outbound shipment/order, integrated supported booking/tracking/result and exception attention | MUST HAVE — MVP | OD08 round trip with Admin authority; manual execution is fallback |
| MR08 | One return case/order, disposition/contact/action/physical-return assertions | MUST HAVE — MVP | Returns are an evidenced major daily job; no refund or stock-restoration inference |
| MR09 | One pickup case/order, separate collection/payment, age and follow-up | MUST HAVE — MVP | Prevent paid-to-collected errors; pending excluded from final-outcome KPI |
| MR10 | Reship/replacement request, Admin decision, linked new order and external-result reconciliation | MUST HAVE — MVP | Preserve essential service recovery with OD06/OD07 |
| MR11 | Operational dashboard, six canonical operational KPIs, linked product analytics/ROAS, record drill-down and scoped export | MUST HAVE — MVP | OD05/OD09 trustworthy results and attention |
| MR12 | Shopify/Bosta core connections, Meta spend input/connection where applicable, mappings/reconciliation/freshness and manual fallback | MUST HAVE — MVP | OD08 integrated normal path; provider gaps/failures visible, safe imports/exports retained |
| MR13 | Small merchant configuration set and policy/source history | MUST HAVE — MVP | Merchant/source/currency/calendar boundaries and safe operating thresholds |
| MR14 | Audit, import provenance, uncertainty states and corrections | MUST HAVE — MVP | Required for meaningful truth and consequential-action evidence |
| MR15 | Platform merchant/member administration and aggregate operational monitoring | MUST HAVE — MVP | Operate multiple merchant accounts without business-action access |
| MR16 | Manual subscription/plan state, billing contact, activation/suspension and data preservation | MUST HAVE — MVP | Minimum commercial shell; prices and access policy need owner decision |
| MR17 | Focused case ownership, due/overdue/action-waiting/approval attention | MUST HAVE — MVP | Work must not disappear after a call; embedded workflow work, no general task manager |
| F18 | Basic product/SKU lookup and source mapping needed to understand order items | MUST HAVE — MVP | Supports operations; unresolved variants remain explicitly unmapped |
| F19 | Product/SKU sales, revenue, delivery/RTO/return performance, periods, comparisons and drill-down | MUST HAVE — MVP | OD09 operational product decisions; transparent item/outcome mapping and populations |
| F20 | Product-level advertising spend/economics and canonical ROAS with input-quality states | MUST HAVE — MVP | OD09; Meta evidenced source, qualified attribution/VAT/revenue policy remains a launch gate |
| F21 | Source season/classification context needed by analysis; richer season management | MUST HAVE — MVP only for necessary analytical context; richer workflows SHOULD HAVE — shortly after MVP | Preserve available label/time/mapping; analytics works without full season creation/edit/delete/bulk assignment |
| F22 | Costs/fees statement reconciliation and contribution estimates | LATER | Unmatched wallet scopes and financial semantics unresolved; raw evidence may be retained now |
| F23 | Automated tier/replenishment recommendations, production planning and advanced inventory automation | LATER | OD09 explicitly defers automation; dated stock/product observations may appear in MVP analysis |
| F24 | Critical Shopify/Bosta ingestion and supported consequential action execution/results; applicable Meta spend connection | MUST HAVE — MVP | OD08 integrated core; exact action support/evidence gates in08, fallback only for unavailable/unsupported exceptions |
| F25 | Period operational summary/export with metric definitions and caveats | MUST HAVE — MVP | Part of MR11; export preserves active scope and privacy |
| F26 | Rich printable executive briefs, reviewed narrative revisions | SHOULD HAVE — shortly after MVP | Human review remains useful; elaborate historical layouts not core |
| F27 | Native refund initiation/payment or settlement accounting | LATER | Actual transaction evidence and financial rules absent; MVP can record reported evidence without claiming execution |
| F28 | Executive/read-only merchant persona; split platform roles | SHOULD HAVE — shortly after MVP | Not necessary for pilot; avoid inventing unnecessary roles now |
| F29 | Proactive email/SMS/customer messaging and embedded telephony | LATER | MVP shows attention in application and records externally performed calls; no message automation required |
| F30 | Partial/repeated return/pickup episodes, consolidated logistics, multi-store workspace | LATER | Requires further boundaries; imports surface exceptions rather than flattening them |
| F31 | Multiple outbound shipments under one order | EXCLUDED | Violates approved OD06; later owner change would be required |
| F32 | Arbitrary reports, configurable workflow builder, extensive automation engine | EXCLUDED | Feature breadth unrelated to first usable daily job |
| F33 | Platform impersonation or merchant business-action override | EXCLUDED | OD07 exceptional future access; no MVP support requirement justifies it |
| F34 | Sophisticated usage metering, self-serve payment checkout/invoice engine | LATER | Manual commercial administration sufficient for pilot; no processor/pricing selected |
| F35 | Native mobile applications, deep historical BI and broad provider marketplace | LATER | Named pilot connections and focused operational/product analysis suffice |
| F36 | Copy workbook sheets/ranges, named employee roles, dormant rate-card scenarios and nonessential legacy matrices | EXCLUDED | Preserve evidence and business meaning, not spreadsheet mechanics |

MUST requirements are exercised by [merchant workflows](04-merchant-workflows.md), [platform workflows](05-platform-admin-workflows.md) and [acceptance gates](11-mvp-acceptance-criteria.md). Core source/action connections and Product/SKU/ROAS analytics are explicit dependencies under OD08/OD09. A replenishment or native refund engine is not required.

OP01 now qualifies the named pilot's supported source/action/round-trip scope; integrated-versus-manual priority is settled by OD08. Provider action targets are not proof of verified legacy execution. Temporary/unsupported/incomplete-onboarding exceptions use attributed manual fallback; a permanently manual core round trip cannot pass the integrated pilot gate.
