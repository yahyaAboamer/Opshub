"""Aggregate five exact blind rankings and preserve review lineage; no implementation tests."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"evidence/migration"
rankings=[]
for index in range(1,6):
    path=OUT/f"council-reviews/ranking-{index}.md"
    body=path.read_text(encoding="utf-8")
    tail=body.rsplit("FINAL RANKING:",1)[-1]
    rows=re.findall(r"^([1-5])\. Response ([A-E])\s*$",tail,re.MULTILINE)
    if len(rows)!=5 or [int(n) for n,_ in rows]!=list(range(1,6)) or set(x for _,x in rows)!=set("ABCDE"):
        raise SystemExit(f"Invalid blind ranking {index}")
    rankings.append({"reviewer":index,"order":[label for _,label in rows],"evidence":path.relative_to(ROOT).as_posix()})
scores={label:sum(r["order"].index(label)+1 for r in rankings) for label in "ABCDE"}
aggregate=sorted(scores,key=lambda label:(scores[label],label))
lenses={"A":"Pragmatist","B":"Red-teamer","C":"Domain rigorist","D":"First-principles","E":"Generalist"}
lineage={}
for path in sorted((OUT/"council-reviews").glob("*.md")):
    lineage[path.relative_to(ROOT).as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
result={
"status":"complete","completed_at_utc":datetime.now(timezone.utc).isoformat(),
"method":"Five independent answers, five fresh blind rankings plus final amendment audits, chairman evidence-based synthesis",
"stage1_completed":5,"stage2_completed":5,
"model_scope":"Internal Codex models; four available gpt-6-astra first-round members and one inherited-model replacement after model usage limit; blind reviewers use available inherited model",
"concurrency_adaptation":"Three child agents maximum; five-member rounds completed in batches",
"failed_attempts_not_counted":[{"lens":"First-principles","reason":"Requested review model usage limit","resolution":"Fresh inherited-model replacement completed response-4.md"}],
"rankings":rankings,
"aggregate":[{"response":label,"lens":lenses[label],"average_rank":str(Fraction(scores[label],5))} for label in aggregate],
"accepted_amendments":["CAR"+f"{i:02d}" for i in range(1,11)],
"chairman_disposition":"Incorporate justified critiques from all five responses, including lower-ranked monetary/clock/privacy insights; preserve owner/account/execution gates",
"remaining_material_design_gaps_in_audited_amendments":[],
"remaining_future_gates":"MD01-MD16 and independently reviewed per-scenario realization, account/provider/application/RLS/action/recovery/operational/rollout evidence",
"review_lineage_sha256":lineage,
"final_document_sha256":{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/"docs/migration").glob("*.md"))},
"golden_contract_sha256":hashlib.sha256((OUT/"golden-contracts.json").read_bytes()).hexdigest(),
"logical_fixture_sha256":hashlib.sha256((OUT/"golden-logical-fixtures.json").read_bytes()).hexdigest(),
"limitations":"Internal AI review has correlated blind spots; no live migration/application/provider/security/restore/performance/cutover validation was executed"
}
(OUT/"council-result.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({"status":result["status"],"members":5,"blind_reviewers":5,"aggregate":result["aggregate"]},indent=2))

