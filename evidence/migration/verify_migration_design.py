"""Verify Phase 5 documents and synthetic EXPECTATIONS, never an OpsHub implementation."""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
from fractions import Fraction
import argparse
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "evidence/migration"
DOCS = ROOT / "docs/migration"
EXPECTED = [
"00-migration-validation-summary.md", "01-source-inventory-and-authority.md",
"02-identity-mapping.md", "03-migration-pipeline.md", "04-data-cleaning-and-dispositions.md",
"05-legacy-regression-oracle.md", "06-golden-datasets.md", "07-kpi-regression-suite.md",
"08-provider-contract-validation.md", "09-external-action-safety-validation.md",
"10-tenant-and-authorization-validation.md", "11-recovery-validation.md",
"12-shadow-and-parallel-run.md", "13-cutover-and-rollback.md",
"14-reconciliation-and-signoff.md", "15-privacy-and-test-data.md",
"16-open-migration-decisions.md", "17-migration-validation-plan.md"]
parser = argparse.ArgumentParser()
parser.add_argument("--final", action="store_true", help="Also require completed Council evidence")
args = parser.parse_args()
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
check(sorted(p.name for p in DOCS.glob("*.md")) == EXPECTED, "18-document inventory differs")
baseline = json.loads((OUT / "phase5-input-baseline.json").read_text(encoding="utf-8"))["files"]
baseline_changes = [name for name, sha in baseline.items()
                    if not (ROOT / name).is_file() or digest(ROOT / name) != sha]
check(not baseline_changes, "Protected Phase 1-4/source/evidence changed")
links = 0
words = 0
bodies = {}
for name in EXPECTED:
    path = DOCS / name
    if not path.is_file():
        continue
    body = path.read_text(encoding="utf-8")
    bodies[name] = body
    words += len(body.split())
    check(len(body.split()) >= 350, f"Document too shallow: {name}")
    check(body.count("```") % 2 == 0, f"Unbalanced code fences: {name}")
    for target in re.findall(r"\]\(([^)]+)\)", body):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        target = target.split("#")[0]
        resolved = (path.parent / target).resolve()
        # The generated report links can refer to the file about to be written.
        if resolved == OUT / "verification.json":
            continue
        check(resolved.exists(), f"Missing relative link: {name} -> {target}")
        links += 1
gold_path = OUT / "golden-contracts.json"
gold = json.loads(gold_path.read_text(encoding="utf-8"))
check(gold["data_class"] == "SYNTHETIC_ONLY", "Golden data must be synthetic")
check(gold["execution_status"] == "SPECIFICATION_NOT_APPLICATION_TEST", "Execution scope drift")
facts = gold["facts"]
cf = facts["confirmation"]
ship = facts["shipments"]
pick = facts["pickups"]
calls = facts["contacts"]
def ids(rows, predicate):
    return sorted(r["id"] for r in rows if predicate(r))
derived = {
"KR01": (ids(cf, lambda r:r["entered"] and r["state"]=="affirmative"), ids(cf, lambda r:r["entered"])),
"KR02": (ids(ship, lambda r:r["outcome"]=="delivered"), ids(ship, lambda r:r["outcome"] in {"delivered","rto","final_other"})),
"KR03": (ids(ship, lambda r:r["outcome"]=="rto"), ids(ship, lambda r:r["outcome"] in {"delivered","rto","final_other"})),
"KR04": (ids(pick, lambda r:r["physical_outcome"]=="collected"), ids(pick, lambda r:r["physical_outcome"] in {"collected","final_cancelled_uncollected","final_no_show_uncollected"})),
"KR05": (ids(calls, lambda r:bool(r["attempts"]) and r["reached"] is True), ids(calls, lambda r:bool(r["attempts"]))),
"KR06": (ids(calls, lambda r:r["action_required"] is True and r["action_complete"] is True), ids(calls, lambda r:r["action_required"] is True)),
}
metrics = {m["id"]:m for m in gold["metrics"]}
for code, (num, den) in derived.items():
    m = metrics[code]
    check(sorted(m["numerator_members"]) == num, f"{code} numerator facts/expectation mismatch")
    check(sorted(m["denominator_members"]) == den, f"{code} denominator facts/expectation mismatch")
    check(len(num) == m["numerator_count"] and len(den) == m["denominator_count"], f"{code} count mismatch")
    check(set(num) <= set(den), f"{code} numerator outside denominator")
    check(len(den) == len(set(m["denominator_members"])), f"{code} duplicate member")
    check(Fraction(len(num), len(den)) == Fraction(m["expected_ratio"]), f"{code} ratio mismatch")
check(metrics["KR02"]["denominator_members"] == metrics["KR03"]["denominator_members"], "Delivery/RTO denominators differ")
check(metrics["KR02"]["pending_members"] == ids(ship, lambda r:r["outcome"]=="pending"), "Shipment pending set differs")
check(metrics["KR02"]["unknown_members"] == ids(ship, lambda r:r["outcome"]=="unknown"), "Shipment unknown set differs")
check(metrics["KR04"]["pending_members"] == ids(pick, lambda r:r["physical_outcome"]=="pending"), "Pickup pending set differs")
check(metrics["KR04"]["unknown_members"] == ids(pick, lambda r:r["physical_outcome"]=="unknown"), "Pickup unknown set differs")
check(sum(r["attempts"] or 0 for r in calls)==8, "Contact-event expected count differs")
for row in facts["items"]:
    check(Decimal(row["gross"])-Decimal(row["discount"])-Decimal(row["reversal"])==Decimal(row["net"]), f"Item arithmetic: {row['id']}")
ship_by_id={s["id"]:s for s in ship}
for kind, objects in (("product",gold["products"]),("variant",gold["variants"])):
    for object_id, expected in objects.items():
        rows=[r for r in facts["items"] if r[kind]==object_id]
        check(sorted(r["id"] for r in rows)==sorted(expected["items"]), f"{kind} item members: {object_id}")
        check(sorted({r["order"] for r in rows})==sorted(expected["orders"]), f"{kind} order members: {object_id}")
        check(sum(Decimal(r["quantity"]) for r in rows)==Decimal(expected["units"]), f"{kind} units: {object_id}")
        check(sum(Decimal(r["net"]) for r in rows)==Decimal(expected["net"]), f"{kind} net: {object_id}")
        if kind=="product":
            final=sorted({r["shipment"] for r in rows if ship_by_id[r["shipment"]]["outcome"] in {"delivered","rto","final_other"}})
            delivered=sorted(s for s in final if ship_by_id[s]["outcome"]=="delivered")
            rto=sorted(s for s in final if ship_by_id[s]["outcome"]=="rto")
            check((final,delivered,rto)==(sorted(expected["final"]),sorted(expected["delivered"]),sorted(expected["rto"])), f"Product outcome members: {object_id}")
for s in facts["spend"]:
    check(Decimal(s["amount"])==Decimal(s["allocated"])+Decimal(s["unallocated"]), f"Spend conservation: {s['id']}")
roas=gold["roas"]
nr=sum(Decimal(v) for v in roas["numerator_contributors"].values())
dr=sum(Decimal(v) for v in roas["denominator_contributors"].values())
check(nr==Decimal(roas["expected_numerator"]) and dr==Decimal(roas["expected_denominator"]), "ROAS contributor totals")
check(Fraction(nr)/Fraction(dr)==Fraction(roas["expected_ratio"]), "ROAS ratio")
for delta in gold["isolated_deltas"]:
    num=delta["numerator_members"]; den=delta["denominator_members"]
    check(set(num)<=set(den), f"{delta['scenario']} invalid membership")
    check(Fraction(len(num),len(den))==Fraction(delta["expected_ratio"]), f"{delta['scenario']} ratio")
revision=gold["spend_revision"]
check(Decimal(revision["source_total"])==Decimal(revision["allocated_A"])+Decimal(revision["unallocated"]), "Revised spend conservation")
check(Fraction(nr)/Fraction(Decimal(revision["allocated_A"]))==Fraction(revision["expected_roas"]), "Revised ROAS")
partial=gold["partial_attribution"]
check(Decimal(partial["eligible"])==Decimal(partial["attributed"])+Decimal(partial["unattributed"]), "Partial revenue conservation")
check(Fraction(Decimal(partial["attributed"]))/Fraction(Decimal(partial["spend"]))==Fraction(partial["expected_roas"]), "Partial attribution ROAS")
logical_path=OUT / "golden-logical-fixtures.json"
logical=json.loads(logical_path.read_text(encoding="utf-8"))
check(logical["data_class"]=="SYNTHETIC_ONLY", "Logical fixtures must be synthetic")
check(not logical["test_policy_rules"]["production_policy_approval"], "Fixture policy cannot approve production policy")
for code in ("KR02","KR03","KR04","KR05","KR06"):
    check(metrics[code]["expected_state"]=="provisional", f"{code} unqualified population marked complete")
check(metrics["KR01"]["expected_state"]=="complete", "Known confirmation population quality")
events=logical["contact_events"]
check(len(events)==8 and len({e["native_id"] for e in events})==8, "Explicit contact event identity/count")
for case in calls:
    if case["attempts"] is None:
        continue
    selected=[e for e in events if e["case_id"]==case["id"]]
    check(len(selected)==case["attempts"], f"Contact source events/count {case['id']}")
    check(any(e["reach"]=="reached" for e in selected)==case["reached"], f"Contact reach evidence {case['id']}")
check({r["case"] for r in logical["requirements"]}==set(metrics["KR06"]["denominator_members"]), "Requirement case members")
check({r["case"] for r in logical["requirements"] if r["state"]=="Succeeded"}==set(metrics["KR06"]["numerator_members"]), "Completion positive result members")
bindings=logical["source_bindings"]
lookup={}
for binding in bindings:
    key=(binding["merchant"],binding["account"],binding["kind"],binding["native_id"])
    check(key not in lookup, "Duplicate native binding in logical scope")
    lookup[key]=binding["expected_canonical"]
ma=[b for b in bindings if b["merchant"]=="MA" and b["kind"]=="Order"][0]
mb=[b for b in bindings if b["merchant"]=="MB" and b["kind"]=="Order"][0]
check(ma["native_id"]==mb["native_id"] and ma["alias"]==mb["alias"] and ma["expected_canonical"]!=mb["expected_canonical"], "MA/MB collision counterpart absent")
repeat=logical["repeated_line_fixture"]
check(len({l["native_id"] for l in repeat["lines"]})==repeat["expected_distinct_items"]==2, "Repeated line identity")
prior=logical["prior_period"]
check({i["id"]:i["net"] for i in prior["items"]}==prior["expected_revenue_contributors"], "Prior amount/member expectation")
check(sum(Decimal(i["net"]) for i in prior["items"])==Decimal(prior["expected_net"]), "Prior net")
check(sum(Decimal(i["quantity"]) for i in prior["items"])==Decimal(prior["expected_units"]), "Prior units")
check(ids(prior["shipments"],lambda s:s["outcome"]=="delivered")==prior["delivered_members"], "Prior delivery members")
check(ids(prior["shipments"],lambda s:s["outcome"] in {"delivered","rto","final_other"})==prior["final_members"], "Prior final members")
check(Fraction(len(prior["delivered_members"]),len(prior["final_members"]))==Fraction(prior["expected_delivery"]), "Prior rate")
attrib=logical["partial_attribution"]["contributors"]
for a in attrib:
    check(Decimal(a["eligible"])==Decimal(a["attributed"])+Decimal(a["unattributed"]), f"Item attribution conservation {a['item']}")
    check(a["item"] in roas["numerator_contributors"] and a["eligible"]==roas["numerator_contributors"][a["item"]], f"Attribution source item basis {a['item']}")
check(sum(Decimal(a["attributed"]) for a in attrib)==Decimal(partial["attributed"]), "Attributed item total")
check(sum(Decimal(a["unattributed"]) for a in attrib)==Decimal(partial["unattributed"]), "Unattributed item total")
new_spend=logical["spend_revision"]
check(sum(Decimal(v) for v in new_spend["contributors"].values())==Decimal(revision["allocated_A"]), "Revised spend portions")
check(sum(Decimal(v) for v in new_spend["unallocated_contributors"].values())==Decimal(revision["unallocated"]), "Revised unallocated portions")
def instant(value):
    return datetime.fromisoformat(value.replace("Z","+00:00"))
start=instant("2026-08-17T00:00:00+03:00")
end=instant("2026-08-24T00:00:00+03:00")
asof=instant(gold["time"]["as_of"])
def current(value):
    return start<=instant(value)<end
temporal={t["id"]:t for t in logical["temporal_cases"]}
check(current(temporal["TC01"]["created_at"]) and not current(temporal["TC01"]["placed_at"]), "Shipment/order clock distinction")
check(not current(temporal["TC02"]["entry_at"]) and current(temporal["TC02"]["observed_at"]), "Entry/observation clock distinction")
check(instant(temporal["TC02"]["placed_at"])<=instant(temporal["TC02"]["entry_at"]), "Confirmation fixture chronology")
check(not current(temporal["TC09"]["placed_at"]) and current(temporal["TC09"]["entry_at"]), "Placement/entry cohort distinction")
check(current(temporal["TC03"]["entry_at"]) and not current(temporal["TC03"]["collected_at"]) and instant(temporal["TC03"]["collected_at"])<=asof, "Pickup entry/as-of distinction")
check(not current(temporal["TC04"]["action_required_at"]) and current(temporal["TC04"]["first_attempt_at"]), "Required/attempted clock distinction")
check(instant(temporal["TC05"]["first_attempt_at"])==end and not current(temporal["TC05"]["first_attempt_at"]), "Exclusive end")
check(temporal["TC06"]["expected_new_contact_start"]=="held_spacing_unknown", "Date-only cannot prove spacing")
fold=temporal["TC07"]
fold_start=instant(fold["window_start"]); fold_end=instant(fold["window_end_exclusive"])
check([e["id"] for e in fold["events"] if "at" in e and fold_start<=instant(e["at"])<fold_end]==fold["expected_members"], "Offset transition member set")
check(fold["held"]==["FOLD_UNKNOWN"], "Ambiguous repeated local hour not held")
late=temporal["TC08"]
check(instant(late["recorded_at"])>instant(late["old_generation_as_of"]) and instant(late["recorded_at"])<instant(late["new_generation_as_of"]), "Late correction generation boundary")
check(late["old_den"]==late["new_den"] and late["old_num"]!=late["new_num"], "Late correction members/retained history")
check(logical["inherited_safety_seed"]["restore_before_migration_post_ops_markers"]==0 and logical["inherited_safety_seed"]["expected_new_dispatches"]==0, "Inherited seed restore case")
check(logical["changing_capture"]["expected_current_objects"]==["N01@v1","N02@v2","N03@v1","N04@v1"], "Independent acquisition inventory")
for scenario in gold["required_scenarios"]:
    check(re.search(r"\| "+scenario+r"\b",bodies["06-golden-datasets.md"]) is not None, f"Scenario missing: {scenario}")
for i in range(1,17):
    check(f"MD{i:02d}" in bodies["16-open-migration-decisions.md"], f"Missing owner decision MD{i:02d}")
for code, size, name in [("PC-S",11,"08-provider-contract-validation.md"),("PC-B",11,"08-provider-contract-validation.md"),("PC-M",7,"08-provider-contract-validation.md"),("EA",26,"09-external-action-safety-validation.md"),("TI",21,"10-tenant-and-authorization-validation.md"),("AU",13,"10-tenant-and-authorization-validation.md"),("RV",21,"11-recovery-validation.md")]:
    for i in range(1,size+1):
        check(code+f"{i:02d}" in bodies[name], f"Missing contract {code}{i:02d}")
draft=json.loads((OUT / "council-draft-manifest.json").read_text(encoding="utf-8"))["files"]
with zipfile.ZipFile(OUT / "council-reviewed-first-draft.zip") as archive:
    for name,sha in draft.items():
        check(hashlib.sha256(archive.read(name)).hexdigest()==sha, f"Council snapshot mismatch {name}")
review_status="pending"
if (OUT / "council-result.json").is_file():
    council=json.loads((OUT / "council-result.json").read_text(encoding="utf-8"))
    review_status=council.get("status","pending")
if args.final:
    check(review_status=="complete", "Council review incomplete")
    for i in range(1,6):
        check((OUT / f"council-reviews/response-{i}.md").is_file(), f"Missing Council answer {i}")
        check((OUT / f"council-reviews/ranking-{i}.md").is_file(), f"Missing blind ranking {i}")
report={
"verified_at_utc":datetime.now(timezone.utc).isoformat(),
"scope":"Static document integrity and arithmetic of synthetic EXPECTATIONS only; no application/provider/migration/restore execution",
"document_count":len(bodies),"words":words,"local_links_checked":links,
"protected_files":len(baseline),"source_files":sum(n.startswith("source/") for n in baseline),
"closed_documents":sum(n.startswith("docs/") for n in baseline),
"baseline_changes":baseline_changes,"golden_dataset_sha256":digest(gold_path),
"logical_fixture_sha256":digest(logical_path),"temporal_scenarios":len(temporal),
"golden_scenarios":len(gold["required_scenarios"]),"baseline_kpis":len(metrics)+1,
"owner_decisions":16,"council_review_status":review_status,
"validation_errors":errors,"pass":not errors,
"future_execution":"NOT EXECUTED"}
(OUT / "verification.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
text_manifest={p.relative_to(ROOT).as_posix():digest(p) for p in sorted(DOCS.glob("*.md"))}
(OUT / "final-document-manifest.json").write_text(json.dumps(text_manifest,indent=2),encoding="utf-8")
print(json.dumps(report,indent=2))
raise SystemExit(1 if errors else 0)
