"""Integrity, scope and redaction-shape checks for the Phase 1B package."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
docs = ROOT / 'docs/reconstruction'
baseline = json.loads((HERE / 'document-baseline.json').read_text(encoding='utf-8-sig'))
changed = [x['Name'] for x in baseline if hashlib.sha256((docs/x['Name']).read_bytes()).hexdigest() != x['SHA256'].lower()]
allowed = {'00-system-map.md', *[p.name for p in docs.glob('*.md') if p.name[:2] in {'08','09','10','11','12','13','14','15'}]}
analysis = json.loads((HERE/'static-analysis.json').read_text(encoding='utf-8'))
asset_errors, snippet_errors = [], []
for asset in analysis['assets']:
    data = (HERE/asset['file']).read_bytes()
    if len(data) != asset['bytes'] or hashlib.sha256(data).hexdigest() != asset['sha256']:
        asset_errors.append(asset['file'])
for item in analysis['evidence_snippets']:
    data = (HERE/item['file']).read_bytes()
    excerpt = data[item['byte_start']:item['byte_end_exclusive']].decode('utf-8')
    if excerpt != item['snippet'] or hashlib.sha256(data).hexdigest() != item['source_sha256']:
        snippet_errors.append(item['id'])
link_errors = []
for folder in [docs, HERE]:
    for path in folder.glob('*.md'):
        text = path.read_text(encoding='utf-8-sig')
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
            if target.startswith(('https://','http://','codex://','#')):
                continue
            if not (path.parent/target.split('#',1)[0].strip('<>')).resolve().exists():
                link_errors.append({'file':str(path.relative_to(ROOT)),'target':target})
contracts = json.loads((HERE/'browser-contracts.json').read_text(encoding='utf-8'))
contract_text = json.dumps(contracts)
redaction_shape_issues = []
if re.search(r'/(?:orders|products)/[a-z0-9]{15,}', contract_text):
    redaction_shape_issues.append('Unnormalized dynamic record path')
for key in ['customerName','customerPhone','receiverName','phone','firstLine','secondLine','notes','calledBy']:
    # Field-name strings are permitted; retained field-value objects are not.
    if re.search(r'"'+key+r'"\s*:',contract_text):
        redaction_shape_issues.append('Customer field value key: '+key)
for key in ['cookie','authorization','session_token','password','bound_values']:
    if re.search(r'"'+key+r'"\s*:',contract_text,flags=re.I):
        redaction_shape_issues.append('Sensitive value key: '+key)
headers_duplicate = {}
for path in docs.glob('*.md'):
    headings = re.findall(r'^## .+$',path.read_text(encoding='utf-8-sig'),flags=re.M)
    duplicate = sorted({h for h in headings if headings.count(h)>1})
    if duplicate:
        headers_duplicate[path.name] = duplicate
report = {
    'verified_at_utc':datetime.now(timezone.utc).isoformat(),
    'changed_documents':changed,'document_changes_within_authorized_scope':set(changed)<=allowed,
    'unchanged_baseline_documents':[x['Name'] for x in baseline if x['Name'] not in changed],
    'assets_checked':len(analysis['assets']),'asset_errors':asset_errors,
    'exact_snippets_checked':len(analysis['evidence_snippets']),'snippet_errors':snippet_errors,
    'local_link_errors':link_errors,'duplicate_section_headings':headers_duplicate,
    'sanitized_contract_shape_issues':redaction_shape_issues,
    'privacy_review_scope':'Structural scan of curated JSON plus manual review of saved fields/locators. Does not certify arbitrary code strings contain no possible secrets.',
    'network_limitation':'No authenticated request/response capture; no mutation tested.'
}
(HERE/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
assert set(changed)<=allowed and not (asset_errors or snippet_errors or link_errors or headers_duplicate or redaction_shape_issues)

