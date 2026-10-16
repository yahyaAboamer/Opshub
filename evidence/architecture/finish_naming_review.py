"""Verify naming-only edits against the captured byte hashes and record the review."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / 'evidence/architecture/phase4-input-baseline.json').read_text(encoding='utf-8'))['files']
PATHS = ['AGENTS.md', 'docs/domain/00-canonical-domain-overview.md', 'docs/domain/01-entity-catalog.md', 'docs/domain/02-identities-and-relationships.md']
RULE = '\n## Durable naming rule\n\nGentry = legacy evidence; OpsHub = target SaaS.\nPreserve Gentry in historical evidence, source names, quotations and legacy behavior; use OpsHub for future-product design.\n'
rows = []
for relative in PATHS:
    path = ROOT / relative
    current = path.read_bytes().decode('utf-8-sig').replace('\r\n', '\n')
    old = current.replace(RULE, '', 1) if relative == 'AGENTS.md' else current.replace('OpsHub SaaS', 'Gentry SaaS')
    found = None
    for nl in ['\n', '\r\n']:
        for bom in ['', '\ufeff']:
            for end in range(4):
                trial = (bom + old.rstrip('\n').replace('\n', nl) + nl * end).encode('utf-8')
                if hashlib.sha256(trial).hexdigest() == BASE[relative]:
                    found = (nl, bom, end)
    if found is None:
        raise SystemExit(f'Not an exact naming-only transformation: {relative}')
    nl, bom, end = found
    data = (bom + current.rstrip('\n').replace('\n', nl) + nl * end).encode('utf-8')
    path.write_bytes(data)
    rows.append((relative, BASE[relative], hashlib.sha256(data).hexdigest(), current.count('OpsHub SaaS') if relative != 'AGENTS.md' else 1))
body = '''# Phase 4 — controlled naming consistency review

14 October 2026. Canonical rule: **Gentry = legacy evidence; OpsHub = target SaaS.** The owner's Phase 4 instruction authorizes only this bounded correction in closed inputs.

## Changed documentation paths

| Path | Bounded change |
|---|---|
| `AGENTS.md` | Added the durable naming rule and preservation sentence; retained all existing reconstruction instructions |
| `docs/domain/00-canonical-domain-overview.md` | Future platform control-plane sentence and diagram label: Gentry SaaS → OpsHub SaaS |
| `docs/domain/01-entity-catalog.md` | Shared entity contract and E26 purpose/scope: three future SaaS references corrected |
| `docs/domain/02-identities-and-relationships.md` | E26 participation table: future control plane corrected |

Six future-product references corrected across three domain documents. Root rule is one additional bounded insertion. No product-document naming correction was necessary. Old approval/phase-status statements remain historical snapshots; current human approval supersedes them for Phase 4.

## Preservation and verification

Reviewed Gentry references across root instructions, domain and product documents. Preserved legacy behavior/comparisons, historical quotations, filenames/URLs, workbook/sheet/evidence labels, routes/screens and hashes/manifests. Source files, closed reconstruction and pre-existing evidence were not edited. Historical council/review evidence was not renamed. No phase semantics, domain cardinality, policy status or PRD scope was rewritten.

The script reconstructs each original byte hash by undoing only the approved insertion/name substitutions, and preserves original encoding/newline style. Final Phase 4 verification compares all captured input hashes and allows only these four explicitly recorded changes. Older closed baseline verifiers would flag the authorized domain naming changes; their reports/manifests are retained rather than overwritten/rebaselined.

## Hash trace

| Path | Before SHA256 | After SHA256 |
|---|---|---|
'''
body += '\n'.join(f'| `{p}` | `{before}` | `{after}` |' for p, before, after, count in rows) + '\n'
(ROOT / 'evidence/architecture/naming-consistency-review.md').write_text(body, encoding='utf-8')
print(json.dumps({'changed_paths': PATHS, 'naming_only_verified': True, 'original_style_preserved': True}))
