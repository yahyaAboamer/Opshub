"""Read-only custody check for previously observed legacy CSVs; no customer field extraction."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
ROOT=Path(__file__).resolve().parents[2]
pairs=[
("Gentry orders","D:/Downloads/orders-2026-10-13.csv","evidence/live/order-export-profile.json"),
("Gentry contacts","D:/Downloads/call-log-2026-10-13.csv","evidence/live/call-export-profile.json"),
("Gentry products","D:/Downloads/products-2026-10-05_to_2026-10-11-2026-10-13.csv","evidence/live/product-export-profile.json")]
items=[]
for name,filename,profile in pairs:
    path=Path(filename)
    evidence=json.loads((ROOT/profile).read_text(encoding="utf-8"))
    actual=hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    expected=evidence.get("sha256")
    items.append({"source":name,"capture_file":filename,"exists":path.is_file(),"sha256":actual,"prior_profile":profile,"profile_sha256":expected,"matches_prior_profile":actual==expected if expected is not None else "profile_has_no_sha256"})
report={"checked_at_utc":datetime.now(timezone.utc).isoformat(),"scope":"Custody/hash only; no new live acquisition, row normalization or migration","items":items}
(ROOT/"evidence/migration/legacy-capture-custody.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps({"capture_files":len(items),"available":sum(x["exists"] for x in items),"prior_hash_matches":sum(x["matches_prior_profile"] is True for x in items)}))

