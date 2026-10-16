"""Create blinded Council answers; preserve original responses separately."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "evidence/migration"
intro = "# Blinded answers — Phase 5 safety review\n\nQuestion: Does the first complete design safely migrate a controlled Gentry pilot and prove correct OpsHub interpretation? Evaluate technical accuracy and insight, not style or length. Answers refer to the immutable first-draft snapshot.\n"
parts = [intro]
for label, index in zip("ABCDE", range(1, 6)):
    body = (OUT / f"council-reviews/response-{index}.md").read_text(encoding="utf-8")
    body = re.sub(r"<oai-mem-citation>[\s\S]*?</oai-mem-citation>", "", body)
    body = re.sub(r"^# [^\n]*\n", "", body, count=1)
    for name in ("Pragmatist", "Red-teamer", "First-principles", "Generalist", "domain rigor and technical correctness"):
        body = body.replace(name, "Council member")
    parts.append(f"\n## Response {label}\n\n{body.strip()}\n")
(OUT / "council-stage1-anonymized.md").write_text("\n".join(parts), encoding="utf-8")
print("Five complete answers anonymized; originals retained")

