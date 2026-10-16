# Privacy during migration and validation


## PV11–PV13 — Re-import cannot resurrect protected content

**PV11:** complete a source-scoped redaction then replay the identical pre-redaction snapshot and a changed-parser/mapping run. Current suppression governs intake accessibility, canonical fields and new projection publication; units remain accounted with safe reason/locator.

**PV12:** late callback/source report or retained old-generation export after completed disposition. No removed fields become accessible via receipt/history/download. Approved minimized evidence hold is separately restricted, not ordinary retained-generation access.

**PV13:** same alias/phone across MA/MB plus an uncertain native privacy reference. No universal phone match/disclosure/deletion. Ambiguous protected scope stays inaccessible pending approved mapping; suppression identifiers and journal reservations are themselves protected.

MD14 defines permitted hold/retention and source reacquisition behavior. This adds current-disposition enforcement to every ingestion/replay path, while preserving Phase5's immutable source/ boundary and all minimum recovery knowledge.
Authority: [Phase 4 privacy](../architecture/11-audit-provenance-and-privacy.md), [environment isolation](../architecture/13-deployment-and-environments.md), OP12/A05. These are migration tooling/data-handling contracts, not a claim of legal compliance or authorization to delete source evidence.

## Data classes and handling

| Surface | Contract / future verification |
|---|---|
| Customer PII | Names/phone/email/address/contact narratives/order-linked tracking/native references remain protected. Capture minimum fields needed for current migration/continuity; no universal customer profile or unnecessary payment-card/contact recording |
| Production acquisition/intake | Authorized account/scope, encrypted private storage, custody/hash/version, tenant/environment partition and limited migration-role access. Immutable via normal editing, subject to approved privacy/retention/hold policy |
| Local/CI/developer | Synthetic logical/provider fixtures and mocks by default; no production credentials or raw customer copies. Separate production egress denied; redacted copy only with explicit approved necessity/process |
| Migration exports | Private scoped files, current Admin for contact-bearing export, exact requester/filter/generation and authorization at generation/download; no casual Downloads/Git artifact publication |
| Temporary files | Dedicated private task/run storage with access control, file inventory, retention classification and validated cleanup plan. Do not write real inputs to generic build/test output or shared temp previews |
| Logs/errors/traces | IDs/correlation/safe categories/counts only; never raw rows, tokens, signed URLs, phone/name/address/narratives. Parser exception must not print offending raw row |
| Screenshots/visual reports | Use synthetic/redacted samples and minimum crop; inspect metadata/text/labels for residual customer details. Real screen evidence restricted and justified, never casually pasted |
| AI coding-agent exposure | Do not put production rows/payloads, customer text, raw exports or secrets into prompts, context, tool-visible exception output or public review bundles. Agents receive schema/aggregates/redacted locators/synthetic data only |
| Golden fixtures/provider examples | Synthetic MA/MB accounts and sentinel tokens, no copied real customer narratives/transaction IDs. Real controlled-account references sanitized before repository/prompt use |
| Hashes/pseudonyms | Raw digest proves capture identity, not anonymity. Native/order/phone-linked hashes may still identify data; scoped keyed pseudonyms remain protected. No unsalted phone hash presented as anonymous |
| Git/shares/review bundles | Allowlist only documentation, synthetic JSON, redacted aggregate evidence and file hashes. Scan contents/archives/metadata before sharing; approval of migration is not public disclosure |
| Disposal/retention | Owner/legal approves exact duration/class/closure/holds; no destructive cleanup or source/ changes in Phase 5. Minimal effect/contact/privacy coverage must outlive all restorable backups and unresolved holds |

## Synthetic/redaction contract

Design fixtures from canonical facts rather than copying a customer row and replacing one name. Keep relational consistency within synthetic merchant; repeat alias values across MA/MB to test isolation. Use obviously synthetic caller/customer labels and invalid nonlive sentinel contact strings for local mocks; controlled provider accounts use separately authorized valid test-recipient details, never fictional delivery to a real person's address.

If a justified redacted sample is later approved, map all identifying fields consistently within source/tenant scope, remove narrative/notes/hidden sheets/document metadata/external links, shift dates only with an explicit retained duration/cohort transformation, and preserve needed currency/status/grain. Tokenization keys remain outside Git/prompts. Verify utility and residual identification risk; do not claim anonymization just because names were removed.

The Phase 5 documents and golden JSON contain only synthetic facts, safe source aggregates and existing redacted evidence references. Raw real datasets were not copied into fixtures, prompts or new review bundles.

## Privacy test plan — PV01–PV10

PV01 sentinel phone/address/token/narrative in a mock parser error → absent from logs/prompts/traces. PV02 contact-bearing export by Operator/platform → denied; current scoped Admin only. PV03 revoke membership during generation/download → file inaccessible. PV04 temporary input/export/helper crash → inventoried restricted file, no public exposure. PV05 nested archives/hidden worksheet metadata → residual scan before approved sharing. PV06 file path/signed URL/error message → no customer or credential disclosure. PV07 MA privacy request with MB same aliases → no cross-tenant access/deletion. PV08 redaction after backup → independent manifest replay before restored access. PV09 retention while unknown effect/contact/journal hold → retain minimized reservation knowledge, no erasure-driven repeat. PV10 council/agent review allowlist → no production rows/private key/token/body included.

## Cleanup and retention decisions

Reuse Phase 4's finite durations only as **proposals awaiting OP12/MD14**, not automatic settings. Raw expiry cannot remove unique evidence needed for open conflict/effect before necessary minimized assertions/hold knowledge are retained. Closure/suspension is not deletion. Backup expiration and independent privacy manifest coverage must prevent restoration of erased content into ordinary access.

For future approved cleanup, list exact generated/temp paths, class/policy/evidence hold and reachability, then remove only authorized files and record manifest/completion. Original source/ and closed evidence remain untouched under this Phase 5 request. Recovery/action reservations cannot be “cleaned up” because they are old or failed. Authorized privacy disposition and completion records survive DB rollback with minimal protected identifiers.
