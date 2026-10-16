# Roles, responsibilities and permissions

Historical operational responsibility and current server authorization are different evidence categories.

## Historical intended responsibility

Source: architecture 184–195; current Support/Operations/Owner SOPs; detailed [text analysis](../../evidence/artifacts/text/nonworkbook-analysis.md).

| Role | Intended duties / boundaries |
|---|---|
| Customer Support | Contact new orders and apply confirmation/attempt tags; call returned customers; preserve narrative and log status, attempt count, governed cause, fit detail and resolution. Do not edit intake identity fields A–E or delete return rows. Return type J belongs to Operations. Escalate new taxonomy, repeat returns, courier/product issues and failed third confirmation. |
| Operations | Export/paste raw sources, top up call queue, maintain Config/SKU/maps/taxonomy and Change_Log, inspect quality, prepare briefs and pickup actions, review before forwarding. Current weekly SOP governs operating rhythm over base spec. |
| Brand Owner | Review summary, decide product/supplier/payment/COD/courier/staffing policy. Not expected to receive raw customer rows. Proposed thresholds require explicit confirmation. |

Named historical holders are Hadeer, Omar and Hassan; roles should not be treated as permanently tied to names. Source language about Support writing J–Q conflicts with narrower current SOP reserving J to Operations. This is a source governance discrepancy, not a discovered permission rule.

## Current session access observed

Evidence: [live ledger](../../evidence/live/observation-ledger.md) L04–L13, L27.

| Surface / action | Omar-session observation | Enforcement confidence |
|---|---|---|
| Order/Product sections, records and CSV exports | Visible and read successfully. | Verified access for this session only. |
| Add/edit order and call/reship forms | Visible; required controls inspected. | Submit authorization untested. |
| Calls import / Called done | Visible; UI uses signed-in username for quick completion. | Actual actor stamping and access control untested. |
| Reship approval queue | Page accessible, pending empty; historical replacements visible. | UI names Omar approver; occupied request action/other-role denial untested. |
| Product metadata, snapshots, settings and seasons | Edit/save/delete/assignment controls visible. | No changes; server permission boundaries unknown. |
| Logout | Control visible, untouched. | Authentication/login/session expiry/MFA not inspected. |
| Production/incoming stock | Referenced in product copy; no route exposed. | Role-limited or absent navigation unresolved. |
| Merchant/user/audit administration | No visible route in desktop/mobile navigation or home. | Existence and access remain unresolved. |

The chrome's “Team” text is not evidence of an administrator role. Caller text in the detailed call form can be free text; historical exported Called by is not proved to reference an authenticated identity. No assumption is made that every visible control can execute successfully.

## Phase 1B authentication and permission structure

Evidence: [technical ledger](../../evidence/live/phase1b/technical-ledger.md), [browser contracts](../../evidence/live/phase1b/browser-contracts.json), [client analysis APP04](../../evidence/live/phase1b/static-analysis.md).

**VERIFIED:** an independent GET of /orders without browser credentials returned a server 307 redirect to /login?from=%2Forders. This establishes a server-side guard for that request, not the session storage mechanism, cookie/token name, expiry, MFA or every-route protection. No credential/session data was extracted. The theme cookie found in client code is a presentation preference and provides no authentication evidence.

**VERIFIED delivered navigation metadata:**

| Observed route | Permission property |
|---|---|
| /orders; /orders/cleanup | orders.view |
| /orders/calls | orders.calls |
| /orders/reships | orders.reship |
| /orders/new | orders.edit |
| /orders/lookup; visible product routes | No permission value in sampled props |

The inspected SideNav/TabNav functions render their supplied items without a client permission predicate. An upstream server can select those items; the evidence does not establish how. These labels are stronger evidence of a permission vocabulary than historical duties, but do not prove current-user grants, role membership, server action checks, export scope or record/merchant isolation. Missing metadata does not make a route public. No other role or denial test was performed.

## Auditability observations

- Historical Change_Log is a human-readable record, not immutable audit evidence.
- Live calls have dated history and actor labels; CSV exports retain event grain. That is evidence of recorded history, not tamper protection.
- Reship history links original to replacement, but no approver timestamp or audit contract was reconstructed.
- Manual snapshot overwrite is a UI claim; version/revision history is not exposed.
- No audit-log page, before/after change record, soft-delete retention policy or administrative override mechanism was inspected.

## Required further verification

An authorized Support and Owner session should be checked for read/export scopes, form visibility and server denial in a nonproduction environment. A controlled test should distinguish trusted actor identity from editable caller text, check request approval separation, and verify per-record/merchant authorization if such concepts exist. No permission bypass or cross-account production test is proposed here.
