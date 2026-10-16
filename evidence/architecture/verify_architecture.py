"""Static architecture coverage/integrity checks. Does not test an application."""
from pathlib import Path
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs/architecture'
OUT = ROOT / 'evidence/architecture'
EXPECTED = [
    '00-architecture-summary.md', '01-system-context.md', '02-architecture-style-and-modules.md',
    '03-multi-tenancy-and-identity.md', '04-data-architecture.md', '05-integrations.md',
    '06-external-action-safety.md', '07-background-jobs-and-reconciliation.md',
    '08-api-and-application-boundaries.md', '09-analytics-architecture.md',
    '10-security-threat-model.md', '11-audit-provenance-and-privacy.md',
    '12-observability-and-operations.md', '13-deployment-and-environments.md',
    '14-testing-strategy.md', '15-technology-selection.md', '16-cost-and-scale-review.md',
    '17-open-architecture-decisions.md', '18-provider-capability-review.md', '19-architecture-review.md',
]
ALLOWED = {'AGENTS.md', 'docs/domain/00-canonical-domain-overview.md', 'docs/domain/01-entity-catalog.md', 'docs/domain/02-identities-and-relationships.md'}
errors = []
if sorted(p.name for p in DOCS.glob('*.md')) != EXPECTED:
    errors.append('Required architecture inventory differs')
adrs = sorted((DOCS / 'adr').glob('ADR-*.md'))
if len(adrs) != 11:
    errors.append('Expected eleven proposed ADRs')
baseline = json.loads((OUT / 'phase4-input-baseline.json').read_text(encoding='utf-8'))['files']
changed = []
for relative, digest in baseline.items():
    path = ROOT / relative
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        changed.append(relative)
if set(changed) != ALLOWED:
    errors.append('Input changes differ from authorized four-path naming set')
source_inventory = {path.relative_to(ROOT).as_posix() for path in (ROOT / 'source').rglob('*') if path.is_file()}
if source_inventory != {relative for relative in baseline if relative.startswith('source/')}:
    errors.append('Original source inventory differs from baseline')
rule = '\n## Durable naming rule\n\nGentry = legacy evidence; OpsHub = target SaaS.\nPreserve Gentry in historical evidence, source names, quotations and legacy behavior; use OpsHub for future-product design.\n'
for relative in ALLOWED:
    path = ROOT / relative
    value = path.read_bytes().decode('utf-8-sig')
    nl = '\r\n' if '\r\n' in value else '\n'
    previous = value.replace(rule.replace('\n', nl), '', 1) if relative == 'AGENTS.md' else value.replace('OpsHub SaaS', 'Gentry SaaS')
    encoding = 'utf-8-sig' if path.read_bytes().startswith(b'\xef\xbb\xbf') else 'utf-8'
    if hashlib.sha256(previous.encode(encoding)).hexdigest() != baseline[relative]:
        errors.append(f'Naming-only reverse hash mismatch: {relative}')

links = 0
mermaids = 0
words = 0
inventory = {}
for path in list(DOCS.glob('*.md')) + adrs + [OUT / 'naming-consistency-review.md', OUT / 'provider-verification-sources.md']:
    body = path.read_text(encoding='utf-8-sig')
    words += len(body.split())
    inventory[path.relative_to(ROOT).as_posix()] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'words': len(body.split())}
    if body.count('```') % 2:
        errors.append(f'Unbalanced fences: {path.name}')
    mermaids += body.count('```mermaid')
    if path in adrs and not all(f'## {heading}' in body for heading in ['Status', 'Context', 'Decision', 'Alternatives', 'Consequences']):
        errors.append(f'Missing ADR field: {path.name}')
    if path in adrs and '**Proposed — pending human Phase 4 architecture review.**' not in body:
        errors.append(f'ADR approval status differs: {path.name}')
    for match in re.finditer(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', body):
        target = match.group(1).strip('<>')
        if re.match(r'[a-z]+://', target):
            continue
        relative, _, anchor = target.partition('#')
        linked = (path.parent / relative).resolve() if relative else path
        links += 1
        if not linked.is_file():
            errors.append(f'Broken local link: {path.name} -> {target}')
        elif anchor and linked.suffix == '.md':
            headings = re.findall(r'^#{1,6}\s+(.+)$', linked.read_text(encoding='utf-8-sig'), re.M)
            slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
            if anchor not in slugs:
                errors.append(f'Broken anchor: {path.name} -> {target}')
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if re.match(r'^#{1,6} ', line) and i + 1 < len(lines) and lines[i+1].strip():
            errors.append(f'Heading spacing: {path.name}:{i+1}')
    if path.parent != OUT and re.search(r'Gentry SaaS|future Gentry SaaS', body):
        errors.append(f'Future target naming violation: {path.name}')
priorities = (ROOT / 'docs/product/03-mvp-feature-prioritization.md').read_text(encoding='utf-8-sig')
must = []
excluded = []
for line in priorities.splitlines():
    if not re.match(r'^\| (?:MR|F)\d+', line):
        continue
    fields = line.split('|')
    rid = fields[1].strip()
    priority = fields[3].strip()
    if 'MUST HAVE' in priority:
        must.append(rid)
    if 'EXCLUDED' in priority:
        excluded.append(rid)
modules = (DOCS / EXPECTED[2]).read_text(encoding='utf-8')
for rid in must:
    if not re.search(r'^\| '+rid+r' \|', modules, re.M):
        errors.append(f'MUST home missing: {rid}')
for rid in excluded:
    if rid not in modules:
        errors.append(f'Excluded boundary missing: {rid}')
provider = (DOCS / EXPECTED[18]).read_text(encoding='utf-8')
for status in ['CONFIRMED CURRENT CAPABILITY', 'CONFIRMED LIMITATION', 'REQUIRES PILOT ACCOUNT VERIFICATION', 'NOT CURRENTLY VERIFIED']:
    if status not in provider:
        errors.append(f'Provider status missing: {status}')
tests = (DOCS / EXPECTED[14]).read_text(encoding='utf-8')
if 'No application/provider tests are executed' not in tests:
    errors.append('Missing honest application-test boundary')
council_members = sorted((OUT / 'council-inputs').glob('response-*.md'))
council_reviewers = sorted((OUT / 'council-reviews').glob('review-*.md'))
if [path.name for path in council_members] != [f'response-{label}.md' for label in 'ABCDE']:
    errors.append('Council member inventory differs')
if [path.name for path in council_reviewers] != [f'review-{index}.md' for index in range(1, 6)]:
    errors.append('Blind peer-review inventory differs')
for path in council_members + council_reviewers + [OUT / 'council-stage1-anonymized.md', OUT / 'council-stage2-blind-reviews.md', OUT / 'council-amendment-check.md']:
    if not path.is_file() or not path.read_text(encoding='utf-8-sig').strip():
        errors.append(f'Missing council evidence: {path.name}')
council = json.loads((OUT / 'council-result.json').read_text(encoding='utf-8-sig'))
rankings = council.get('rankings', [])
if council.get('stage1_members') != 5 or council.get('stage2_fresh_reviewers') != 5 or len(rankings) != 5:
    errors.append('Council method counts differ')
elif any(sorted(item.get('ranking', [])) != list('ABCDE') for item in rankings):
    errors.append('Blind rankings are not five-member permutations')
else:
    means = {label: sum(item['ranking'].index(label) + 1 for item in rankings) / len(rankings) for label in 'ABCDE'}
    if means != council.get('average_position') or sorted(means, key=means.get) != council.get('overall_order'):
        errors.append('Council aggregate disagrees with blind rankings')
manifest = json.loads((OUT / 'council-reviewed-draft-manifest.json').read_text(encoding='utf-8-sig'))['files']
archive_files_verified = 0
with zipfile.ZipFile(OUT / 'council-reviewed-draft.zip') as archive:
    if set(archive.namelist()) != set(manifest) or len(manifest) != 31:
        errors.append('Reviewed draft archive inventory differs')
    for relative, digest in manifest.items():
        if relative not in archive.namelist() or hashlib.sha256(archive.read(relative)).hexdigest() != digest:
            errors.append(f'Reviewed draft archive hash mismatch: {relative}')
        else:
            archive_files_verified += 1
review = (DOCS / EXPECTED[19]).read_text(encoding='utf-8-sig')
if '**Documentation review complete; proposed architecture pending human Phase 4 review.**' not in review or 'independent LLM Council challenge and final integrity verification are pending' in review:
    errors.append('Final review status is unfinished or differs')
source_count = sum(p.startswith('source/') for p in baseline)
protected_unchanged = sum(p not in changed for p in baseline)
report = {'verified_at': datetime.now(timezone.utc).isoformat(), 'scope': 'documentation integrity and traceability only; not application/provider tests', 'architecture_documents': len(EXPECTED), 'adrs': len(adrs), 'mermaid_fences_structurally_checked': mermaids, 'mermaid_rendering_verified': False, 'local_links_checked': links, 'must_capabilities': must, 'excluded_capabilities': excluded, 'baseline_files': len(baseline), 'source_files_unchanged': source_count, 'protected_files_unchanged': protected_unchanged, 'authorized_naming_paths': changed, 'naming_only_reverse_hash_verified': not any('Naming-only reverse hash mismatch' in error for error in errors), 'council_members': len(council_members), 'blind_peer_reviewers': len(council_reviewers), 'reviewed_draft_archive_files_verified': archive_files_verified, 'words': words, 'inventory': inventory, 'errors': errors, 'result': 'PASS' if not errors else 'FAIL'}
(OUT / 'verification.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({key: value for key, value in report.items() if key != 'inventory'}, indent=2))
raise SystemExit(bool(errors))
