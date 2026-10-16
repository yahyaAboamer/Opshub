"""Sanitized schema, category and calculation checks for UI downloads."""
import csv, collections, decimal, hashlib, json
from pathlib import Path

output_dir = Path(__file__).parent
read = lambda p: list(csv.DictReader(p.open(encoding="utf-8-sig", newline="")))
calls_file = Path(r"D:\Downloads\call-log-2026-10-13.csv")
products_file = Path(r"D:\Downloads\products-2026-10-05_to_2026-10-11-2026-10-13.csv")
orders_file = Path(r"D:\Downloads\orders-2026-10-13.csv")
calls, products, orders = read(calls_file), read(products_file), read(orders_file)
order_dates = {r["Order"]: r["Date"] for r in orders}
before = [r for r in calls if r["Order"] in order_dates and r["Called at"][:10] < order_dates[r["Order"]]]
call_data = {
    "evidence_id": "L24-call-export", "route": "/export/calls", "date": "2026-10-13",
    "sha256": hashlib.sha256(calls_file.read_bytes()).hexdigest(),
    "headers": list(calls[0]), "row_count": len(calls),
    "unique_order_names": len({r["Order"] for r in calls}),
    "call_date_min": min(r["Called at"][:10] for r in calls),
    "call_date_max": max(r["Called at"][:10] for r in calls),
    "status_counts": dict(collections.Counter(r["Call status"] for r in calls)),
    "reason_counts": dict(collections.Counter(r["Reason"] for r in calls)),
    "resolution_counts": dict(collections.Counter(r["Resolution"] for r in calls)),
    "calls_predating_order_date": len(before),
    "predating_call_statuses": dict(collections.Counter(r["Call status"] for r in before)),
    "limitations": ["Date comparison uses exported ISO date components; no time-zone or event provenance validation.", "No customer, staff, phone, notes, or order identifiers retained.", "Export is event-grain and does not accept the displayed dashboard period in its observed href."]
}
output_dir.joinpath("call-export-profile.json").write_text(json.dumps(call_data,ensure_ascii=False,indent=2),encoding="utf-8")
number = lambda r,k: decimal.Decimal(r[k] or "0")
checks = []
for r in products:
    spend = number(r,"Ad spend est. (EGP)")
    net = number(r,"Gross sales (EGP)") - number(r,"Discounts (EGP)") - number(r,"Returns (EGP)")
    checks.append({"product":r["Product"],"calculated_net_roas":str(net/spend) if spend else None,"display_net_roas":r["Net ROAS"],"own_plus_generic_residual":str(spend-number(r,"Ad spend: own ads (EGP)")-number(r,"Ad spend: generic share (EGP)")),"stock_now":r["Stock left (now)"],"units":r["Units sold"],"orders_period":r["Orders (period)"],"orders_alltime":r["Orders (all-time)"],"tier":r["Tier"],"suggested":r["Suggested tier"]})
product_data = {
    "evidence_id":"L25-product-export","route":"/export/products","date":"2026-10-13",
    "sha256":hashlib.sha256(products_file.read_bytes()).hexdigest(),"headers":list(products[0]),"row_count":len(products),
    "periods":sorted({(r["Period"],r["From"],r["To"]) for r in products}),
    "units_total":str(sum(number(r,"Units sold") for r in products)),
    "gross_sales_total":str(sum(number(r,"Gross sales (EGP)") for r in products)),
    "discounts_total":str(sum(number(r,"Discounts (EGP)") for r in products)),
    "returns_total":str(sum(number(r,"Returns (EGP)") for r in products)),
    "spend_total":str(sum(number(r,"Ad spend est. (EGP)") for r in products)),
    "own_spend_total":str(sum(number(r,"Ad spend: own ads (EGP)") for r in products)),
    "generic_share_total":str(sum(number(r,"Ad spend: generic share (EGP)") for r in products)),
    "roas_checks":checks,
    "limitations":["No backend calculation implementation inspected.","Export fields labelled estimated ad spend, whereas page calls it Meta incl VAT.","CSV rounding can make sums differ slightly from displayed whole-EGP values."]
}
output_dir.joinpath("product-export-profile.json").write_text(json.dumps(product_data,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(call_data,ensure_ascii=False,indent=2))
print(json.dumps(product_data,ensure_ascii=False,indent=2))
