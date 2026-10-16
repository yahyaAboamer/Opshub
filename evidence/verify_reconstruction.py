"""Read-only integrity and link verification for the reconstruction package."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
baseline = json.loads((ROOT / 'evidence/source-manifest-before.json').read_text(encoding='utf-8-sig'))
source_results = []
for item in baseline:
    path = ROOT / item['Path']
    digest = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
    source_results.append({'path': item['Path'], 'unchanged': digest == item['SHA256'].lower()})
expected = [
    '00-system-map.md', '01-source-inventory.md', '02-feature-inventory.md',
    '03-domain-model.md', '04-workflows-and-state-machines.md', '05-business-rules.md',
    '06-calculations-and-metrics.md', '07-data-model-observations.md',
    '08-api-and-integration-observations.md', '09-roles-and-permissions.md',
    '10-data-ingestion-and-background-jobs.md', '11-ui-route-map.md',
    '12-file-to-feature-traceability.md', '13-live-vs-spec-discrepancies.md',
    '14-open-questions.md', '15-saas-migration-risks.md',
]
documents = ROOT / 'docs/reconstruction'
missing = [name for name in expected if not (documents / name).is_file()]
broken = []
for doc in documents.glob('*.md'):
    text = doc.read_text(encoding='utf-8-sig')
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
        if target.startswith(('https://', 'http://', 'codex://', '#')):
            continue
        path_part = target.split('#', 1)[0].strip('<>')
        if not (doc.parent / path_part).resolve().exists():
            broken.append({'document': doc.name, 'target': target})
json_errors = []
json_count = 0
for path in (ROOT / 'evidence').rglob('*.json'):
    json_count += 1
    try:
        json.loads(path.read_text(encoding='utf-8-sig'))
    except Exception as error:
        json_errors.append({'path': str(path.relative_to(ROOT)), 'error': str(error)})
actual_source = {str(p.relative_to(ROOT)).replace('\\', '/') for p in (ROOT / 'source').rglob('*') if p.is_file()}
baseline_source = {item['Path'] for item in baseline}
report = {
    'verified_at_utc': datetime.now(timezone.utc).isoformat(),
    'source_file_count': len(source_results),
    'source_hashes_unchanged': all(item['unchanged'] for item in source_results),
    'source_file_set_unchanged': actual_source == baseline_source,
    'source_hash_results': source_results,
    'required_document_count': len(expected),
    'missing_documents': missing,
    'broken_local_links': broken,
    'evidence_json_files_checked': json_count,
    'evidence_json_errors': json_errors,
    'limitations': ['Local links checked for existence, not every Markdown anchor.',
                    'No production workflow executed or backend behavior tested.',
                    'Source hashes confirm byte preservation, not authoritative business correctness.'],
}
(ROOT / 'evidence/verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({key: value for key, value in report.items() if key != 'source_hash_results'}, indent=2))
