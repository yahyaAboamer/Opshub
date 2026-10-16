"""Capture immutable Phase 4 inputs before the authorized naming-only edits."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'evidence/architecture/phase4-input-baseline.json'
if OUT.exists():
    raise SystemExit('Baseline already exists; refusing to replace it')
files = {}
for directory in ['source', 'docs/reconstruction', 'docs/domain', 'docs/product', 'evidence']:
    for path in sorted((ROOT / directory).rglob('*')):
        if not path.is_file() or 'architecture' in path.relative_to(ROOT).parts:
            continue
        files[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
files['AGENTS.md'] = hashlib.sha256((ROOT / 'AGENTS.md').read_bytes()).hexdigest()
OUT.write_text(json.dumps({'captured_at': datetime.now(timezone.utc).isoformat(), 'files': files}, indent=2), encoding='utf-8')
print(f'Captured {len(files)} pre-existing input files')
