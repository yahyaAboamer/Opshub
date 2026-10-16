"""Preserve exactly the documentation/synthetic contract supplied to Council."""
import hashlib
import json
import zipfile
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "evidence/migration"
manifest_path = OUT / "council-draft-manifest.json"
if manifest_path.exists():
    raise SystemExit("Refusing to overwrite the reviewed first draft")
paths = sorted((ROOT / "docs/migration").glob("*.md")) + [OUT / "golden-contracts.json"]
manifest = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
manifest_path.write_text(json.dumps({"captured_at_utc": datetime.now(timezone.utc).isoformat(), "data_class": "Documentation and synthetic fixtures only", "files": manifest}, indent=2), encoding="utf-8")
with zipfile.ZipFile(OUT / "council-reviewed-first-draft.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    for path in paths:
        archive.write(path, path.relative_to(ROOT).as_posix())
print(json.dumps({"reviewed_files": len(paths), "real_customer_rows": 0}))
