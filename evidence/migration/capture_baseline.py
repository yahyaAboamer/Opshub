"""Phase 5 documentation-only baseline; never reads customer values into prompts."""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "evidence/migration/phase5-input-baseline.json"
if OUT.exists():
    raise SystemExit("Refusing to overwrite the Phase 5 input baseline")
paths = []
for folder in ("source", "docs/reconstruction", "docs/domain", "docs/product", "docs/architecture", "evidence"):
    for path in sorted((ROOT / folder).rglob("*")):
        if path.is_file() and not path.is_relative_to(ROOT / "evidence/migration"):
            paths.append(path)
manifest = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
OUT.write_text(json.dumps({"captured_at_utc": datetime.now(timezone.utc).isoformat(), "scope": "All existing source, closed Phase 1-4 documents and evidence files", "files": manifest}, indent=2), encoding="utf-8")
print(json.dumps({"protected_files": len(manifest), "source_files": sum(p.startswith("source/") for p in manifest), "closed_documents": sum(p.startswith("docs/") for p in manifest)}))
