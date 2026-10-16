# Data ingestion and background operations

Evidence: [workbook findings](../../evidence/artifacts/workbooks/WORKBOOK_FINDINGS.md), [text/script analysis](../../evidence/artifacts/text/nonworkbook-analysis.md), [live ledger](../../evidence/live/observation-ledger.md).

## Historical manual ingestion chain

Current supplied Operations SOP describes:

1. Export all Bosta statuses for the relevant period, not returns only; paste values into RAW_Bosta starting A3.
2. Export Cash Cycles/wallet costs and paste RAW_Costs.
3. Export Shopify orders including cancelled records; paste RAW_Shopify starting A3.
4. Top up new returned tracking IDs in external call sheet, check duplicate flag S, notify Support.
5. Download/paste call intake; add new exact SKU variants with price and supplier cost.
6. Force full workbook recalculation; inspect Data_Quality and channel reconciliation before briefs.

Old Operations SOP maps Bosta Created At/name/phone/tracking/description/type to call-sheet A/B/C/D/E/J. Sources are values-only evidence; formulas/master outputs are not manual paste zones. The upgrade pack includes list/migration instructions; Apps Script handles validation for manual edits and requires explicit backfill after API imports.

No deployed scheduled refresh was proved by these human instructions.

## What was actually incorporated in supplied files

| Input | Verified relationship / uncertainty |
|---|---|
| Bosta stage 569 | Every row and input value matches current RAW_Bosta. |
| Shopify stage 664 lines /476 refs | All refs in current; complete line sequences compared. Four orders have meaningful changed fields between stage and current. Current additionally includes older history, so not a single wholesale stage snapshot. |
| Historical Shopify CSV 495 lines /353 refs | Matches v3 backup across all 79 export columns and complete line sequences. |
| SKU additions 22 | Nine incorporated unchanged; 13 absent. May be intentional scope or unfinished update; unresolved. |
| Call top-up 27 | All IDs match current Bosta legs (25 RTO + 2 exchange), none occur in current 75-row intake. External sheet may have been updated later; file preparation is not execution evidence. |
| Current intake 75 | Same as v2/v3. New return-type/refund/recoverable/fit-detail fields all blank. |
| Wallet 1,381 vs Bosta 569 | All 569 legs have positive matching wallet fees; 812 wallet IDs lack source shipment match. Full wallet fee sum differs from master joined fee total. |

Current/v3 formulas have no cached outputs. Investigation did not execute historical scripts or recalculate originals. Twelve v2 cache values support bounded independent arithmetic. Stale XML dimensions and fixed named ranges are distinct capacity concerns; current 1,635 orders fit master slots.

## Historical report automation

| Component | Trigger / input / output / actual limit |
|---|---|
| Weekly extractor | User/agent invocation; unique main workbook found; temporary copy+LibreOffice recalc; fixed-cell metrics/worklists JSON. No scheduler or sending. |
| Chart | JSON input; optional drop-last removes final item without date validation; missing metrics plotted 0. |
| Actions sidecar | Explicit save/load; latest filename selection; no supplied history. Completion is authored judgment, not automatic state transition. |
| Monthly extractor | Report state period start+raw sources after copy recalc; creation-month metrics; wallet 90% gate with no-entry exception; current execution month partialness. |
| Monthly builder | Metrics JSON+authored narrative; requires nine slots; DOCX/chart. No state.json update despite its comment, no PDF conversion/send. |
| report_kit | Shared document styling. Copies byte-identical; no integration or scheduler. |
| Sheets Apps Script | Manual edit touching return type J on Sheet1 applies validation M from Lists; backfill batch manual. Errors swallowed; existing causes not cleared; call reached not checked. |

Config-driven intent conflicts with hardcoded monthly thresholds and instructional gates not fully executed in code. Required metrics/narrative JSONs and report action sidecars are absent, preventing exact archived-report reproduction.

## Current visible refresh behavior

Orders/product sections say refresh every 10 minutes **while section is open**, with manual Sync now. Without clicking it, markers/counters changed: orders 14:21→18:39 and products 18:53; cleanup 11→20 actionable; product previous-week units 175→179 after rebuild 13:24→18:39.

**VERIFIED:** updates are observable during inspection. Phase 1B adds order markers 19:15→19:47 and product markers 19:15→19:56, without manual Sync now. Product dashboard rebuild stayed 18:39 before a later printable report displayed 19:57. These Cairo labels are data watermarks, distinct from UTC evidence-capture times. **INFERRED:** section/navigation activity may be associated with refresh. **UNRESOLVED:** browser-driven polling, server scheduler, webhook, lazy/render-triggered rebuild, refresh interval accuracy, concurrent-user duplication, locking, watermarks and failure recovery. Do not describe a cron job or causal navigation trigger as established.

The [Phase 1B delivered-client analysis](../../evidence/live/phase1b/static-analysis.md) found generic router refresh/revalidation support but no recurring Gentry timer/integration request in retained navigation/date/print/upload functions. PrintButton's 400 ms timeout is a one-shot browser-print delay. No authenticated network trace was available to observe timed requests. Bounded client inspection does not exclude unseen components, server jobs, integration polling or webhooks; the ten-minute claim remains a verified UI statement rather than an implemented schedule proved by this pass.

Meta copy says recent 1–2 days revise. Product metrics/stock combine selected sales period with current stock/rebuild timestamp; readers must retain both.

## Current CSV call import contract — unexecuted

UI accepts Google Sheets CSV and says match by Bosta tracking in order ID or phone; add only new calls; repeating entire file safe. No importer was run. Phase 1B verifies client component CallSheetUpload and public server-reference symbol uploadCallSheet. It submits file through React action state and expects added/alreadyThere/noCallStatus/unmatched feedback or error; at most 15 unmatched entries display. These are client expectations, not an observed server result. No client CSV parser/schema/size validator was found in that component. Required headers/date parsing/timezone, fallback match ambiguity, duplicate-event key, existing-event updates, rollback and historical status translation remain unknown.

Observed call export includes old taxonomy/status values and seven calls earlier than matched order date. These are reasons to inspect import provenance, not sufficient proof of the cause.

## Failure and reconciliation concerns

Tag-only dispatched sample has no matched Bosta detail; historical bosta_sync_failed can be legitimate for pickup. Counter changes do not prove rows deleted or integration failures. Pagination/incremental scopes and late changes require authorized logs/API response inspection. Source June completeness claims conflict; full matched creation/completion-period evidence must settle it.

No customer communications, real booking, refund, cancellation, import, configuration edit or manual sync was triggered.
