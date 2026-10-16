"""Read a user-authorized live CSV; retain aggregate/schema evidence only."""
import csv, collections, decimal, hashlib, json
from pathlib import Path

input_file = Path(r"D:\Downloads\orders-2026-10-13.csv")
rows = list(csv.DictReader(input_file.open(encoding="utf-8-sig", newline="")))
counter = lambda key: dict(collections.Counter(row[key] for row in rows))
data = {
    "evidence_id": "L20-order-export",
    "observed_date": "2026-10-13",
    "route": "/export/orders?period=all",
    "sha256": hashlib.sha256(input_file.read_bytes()).hexdigest(),
    "headers": list(rows[0]) if rows else [],
    "row_count": len(rows),
    "unique_order_names": len({r["Order"] for r in rows}),
    "date_min": min(r["Date"] for r in rows),
    "date_max": max(r["Date"] for r in rows),
    "categories": {key: counter(key) for key in ["Channel", "Confirmed by", "Outcome", "Status", "Bosta state", "Attempts", "Last call"]},
    "order_value_egp": str(sum(decimal.Decimal(r["Value (EGP)"] or "0") for r in rows)),
    "outcomes_by_channel": {channel: dict(collections.Counter(r["Outcome"] for r in rows if r["Channel"] == channel)) for channel in {r["Channel"] for r in rows}},
    "limitations": ["Current mutable production snapshot; original CSV stays in the user's downloads, outside evidence.", "No customer, contact, item, or order identifiers are retained here.", "CSV Last call categories may be labels, not a complete event ledger."]
}
Path(__file__).with_name("order-export-profile.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(data, ensure_ascii=False, indent=2))
