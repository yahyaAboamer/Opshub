# Reconstruction review and verification

Completed 13 October 2026. Scope: the 16 requested documents, source artifact analyses and current read-only browser evidence.

The second investigation pass specifically revisited broad courier-stage membership, export outcome gaps, return-call event grains/dates, waiting paid pickups, refresh-sensitive product values, season membership, hidden navigation and historical-only financial/reporting behavior. Current tag guidance was re-read literally to confirm that Hadeer attribution requires Confirmed; attempt tags alone were not claimed to confirm an order.

Critical evidence review corrected:

- Source-only order dates overlap the live date range; a simple cutoff does not explain every omission.
- The domain diagram must not imply mandatory parents where shipment references or wallet joins are absent.
- Exported attempt counts include zero.
- Tag/no-courier disagreement does not prove a failed booking's causal history.
- Inventory synchronization was not established merely from different current and historical stock numbers.
- Cause capture counts any nonblank intake cause; validity is separate.
- Historical confirmation coverage combines Hadeer/auto and excludes Omar.
- Matched-COGS lost margin is clamped at zero; the blended fallback is not.

All required documents exist. Local evidence/document links were checked for file existence, JSON evidence parsed, and all 38 source hashes/file membership matched the baseline. Details: [verification](verification.json). Workbook ZIP checks and bounded arithmetic/privacy checks: [workbook verification](artifacts/workbooks/verification.json), [additional checks](artifacts/workbooks/additional_checks.json). Non-workbook sources were statically inspected and preserved; no original script was executed.

Limits remain explicit: one authenticated role, no backend/API trace, no live production writes or consequential state-transition tests, no exact Excel-engine recalculation of current/v3 files, and no physical customer/courier verification. Human decisions and controlled further investigation are listed in the reconstruction's open questions. The package is ready for first human review, not a claim that every current rule is proved.
