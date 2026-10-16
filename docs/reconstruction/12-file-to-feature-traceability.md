# File-to-feature traceability

Paths are relative to `source/`; all 38 files are listed in [source inventory](01-source-inventory.md). WB refers to [workbook findings](../../evidence/artifacts/workbooks/WORKBOOK_FINDINGS.md), TXT to [text/script analysis](../../evidence/artifacts/text/nonworkbook-analysis.md), and Lxx to the [live ledger](../../evidence/live/observation-ledger.md).

| Source / locator | Historical feature or rule | Current correspondence and limit |
|---|---|---|
| Architecture §13; HANDOVER 29,47–48,87–111; Orders_Master A3:X3 | Order grain, Shopify header extraction, business-reference join and four channels. | Order dashboard/detail/export L02,L14–L20. External identity strongly supported; channel/state rules differ. |
| DATA_Master A2:BC2; RAW_Bosta A2:AC2 | Shipment grain, type/state precedence, attempts, dates and item parser. | Courier fields L15–L17; live leg-selection algorithm unknown. |
| Main system workbook; v3 and v2 backups | Evolving model; v2 lacks Shopify funnel; v3 has 353 order headers; current has 1,635. | All 353 v3 refs/dates match live; current shares 768. Historical snapshots, not current authority. |
| RAW_Costs; DATA_Master AI/AJ; Config C39 | Summed tracking fees, actual versus modeled costs, gateway assumption. | No equivalent live wallet/fee page exposed. |
| Config C36:C38; DATA_Master AA:AH; OPS_Control C50:C53 | Value proxies, catalogue COGS and contribution. | Live order value is visible; contribution/proxy implementation unverified. |
| RAW_Intake A2:T2; Config B93:E117 | Tracking-key intake, contact taxonomy and owner mapping. | Calls import/form/history L04,L16–L17,L23–L24; legacy values survive export. |
| Upgrade Pack, Migration formulas; dependent dropdown .gs 25–110 | Sheets migration and return-type-dependent validation. | CSV bridge visible; deployed external Sheet/validator not inspected. |
| Support SOP T4–T8,T10–T23 | Consent, three failed confirmation attempts, return calling and ownership. | Current attribution and two-NoAnswer return queue differ; server enforcement unknown. |
| Operations SOP T2–T12,P6–P8,T20–T21 | Refresh, quality gate, pickup age and escalation. | Current sync/cleanup L14,L22; identical job/routine enforcement unverified. |
| Owner guide T4,T8,T11–T13 | Financial interpretation, decisions and target authority. | Draft brief/settings approval wording L08,L26; duties are not RBAC proof. |
| Confirmation C13:C14; Config B180:D191; architecture 289–305,340–356 | Tag attribution, Hadeer-only coverage, intervention share and dispatch value. | Separate Whapi and all-confirmed coverage L02,L26. |
| Pickup_Channel H9; Orders_Master J/T/U/V/X; Config C202:C205 | Financial collection inference, no-show, 3/7/2-day rules and export clock. | Paid waiting pickup/10-day cleanup L18,L22 differ. |
| Weekly, Monthly, OPS_Control | Saturday shipment-created cohorts and worklists. | Monday placed-order/current partial comparisons L26 differ. |
| Returns_Channels, Failure_Analysis | Return-leg channels, causes, owners and courier-reason trust. | Outcome-specific reasons visible; full equivalent scorecard unknown. |
| Product_Size, RAW_SKU | Parsed variant/size economics. | Current GID/ad/stock/tier features extend beyond supplied spec; crosswalk unknown. |
| Geo_Courier | City/zone scorecards, minimum five outbound observations for red flag. | City filter/exceptions visible; current scorecard unknown. |
| Customer_Recovery | Reach, recovery and phone-based repeats. | Calls/repeat filters L04,L14; grains differ. |
| Data_Quality, Change_Log, START | Quality gates, provenance and instructions. | No equivalent audit/quality route exposed; START version label stale. |
| Historical Shopify CSV | 495 lines/353 orders, all 79 columns equivalent to v3. | All 353 external order identities match live. |
| Bosta staging XLSX | 569 prepared shipment rows. | Exact incorporation into current RAW_Bosta. |
| Shopify staging XLSX | 664 lines/476 refs. | All refs current; four meaningful field updates; older history outside stage. |
| SKU additions XLSX | 22 proposed variant keys. | Nine current, 13 absent; scope unresolved. |
| Call top-up XLSX | 27 prepared tracking/contact rows, all current Bosta legs. | None in current intake; external ingestion unknown. |
| Config Audit 22–31,54–84 | Proposed thresholds and legacy-resolution issues. | Historical audit, not approved current policy. |
| Confirmation PLAN and Kickoff Prompt | Historical unbuilt assumptions/execution directions. | Final architecture supersedes; not current web source. |
| Three _superseded named-person SOPs | Earlier return/courier-only duties. | Explain drift; current supplied role SOPs govern intended rhythm. |
| Weekly SKILL, report_structure, writing_rules, evals | Human/agent gates, brief structure, carry-over and qualitative examples. | Current HTML brief is only an analogue; no proof same generator/tests passed. |
| Weekly extract_metrics.py 22–75,181,219–293 | Copied workbook recalculation and fixed-cell worklists. | Artifact-only; customer-name extraction conflicts with privacy promise. |
| Weekly actions.py 17–40; make_chart.py 21–40 | Sidecars; optional tail drop/null-to-zero chart. | No supplied sidecar history/current equivalent. |
| Delivery extract.py 67–205 | Raw monthly metrics and statistical/fee/value definitions. | Historical variance, no claim it runs live. |
| Delivery build_report.py 58–169; state.json | Narrative DOCX/chart generation; period history. | Automatic state-update claim unsupported. |
| Both report_kit.py copies | Identical formatting helper. | No separate business-rule versions. |
| Both Python bytecode caches | Generated metadata. | Not loaded or used as authority. |
| Archived review DOCX/PDF P7,P24–25,P40,T11–T12 | June account, statistical interpretation and calling priorities. | Dated supporting output; contradictions retained; all four PDF pages checked. |
| Office lock file | Temporary application metadata. | No business feature or authority. |

Current Meta allocation, seasons, tiers, graduation, restock/incoming stock and snapshots lack supplied implementation specification. Reship approval and cleanup are more explicit in the live UI than the source package. Missing algorithms remain unresolved.

## Phase 1B technical evidence outside the original source package

These generated observations supplement traceability; they do not alter the 38-file source inventory or establish server implementation.

| Evidence / locator | Feature correspondence | Limit |
|---|---|---|
| [browser-contracts.json](../../evidence/live/phase1b/browser-contracts.json) T01–T13 | Safe read paths/filter URLs, Flight module names, unsubmitted fields/action identities, permission props and sync/rebuild markers. | Sanitized DOM/Flight evidence; authenticated HTTP methods/statuses/payloads not captured. |
| [public-http-observations.json](../../evidence/live/phase1b/public-http-observations.json) | 14 exact observed asset GETs (13 JS retained/one 404); unauthenticated /orders redirect. | Separate public requests, no browser credentials. Guard applies to that single route/request observation. |
| [static-analysis.md](../../evidence/live/phase1b/static-analysis.md) APP04–APP11, FW02–FW12 | Shared navigation, date form submission, browser print, uploadCallSheet identity/expected feedback and generic Next action/Flight transport. | Delivered code only; no server importer, role enforcement or integration/job algorithm. Byte-offset snippets/hash evidence retained. |
| [product-export-profile.json](../../evidence/live/phase1b/product-export-profile.json) T13 | September filtered export: 28 columns/20 rows, 385 units/297,500 EGP. | One nondefault period; other filter propagation/status/headers unverified. |
| [rea-partial-summary.json](../../evidence/live/phase1b/rea-partial-summary.json) | REA static summary from initial nine assets. | Timeout/partial graph, six scripts parsed; predates four later retained assets. Independent static analysis covers final 13. |

Full collection boundary and reconciled findings: [technical ledger](../../evidence/live/phase1b/technical-ledger.md).
