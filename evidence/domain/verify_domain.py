"""Read-only document checks plus a Phase 2 verification report; no app code."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
DOMAIN = ROOT / "docs/domain"
REPORT = ROOT / "evidence/domain/verification.json"
EXPECTED = [
    "00-canonical-domain-overview.md",
    "01-entity-catalog.md",
    "02-identities-and-relationships.md",
    "03-events-and-projections.md",
    "04-state-machines.md",
    "05-domain-invariants.md",
    "06-canonical-glossary.md",
    "07-policy-decision-register.md",
    "08-reconstruction-to-canonical-mapping.md",
    "09-open-domain-questions.md",
]


def heading_slug(value):
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    return re.sub(r"[^\w\- ]", "", value.lower()).replace(" ", "-")


baseline = json.loads(
    (ROOT / "evidence/domain/phase2-baseline-manifest.json").read_text(encoding="utf-8")
)
changes = []
for relative, previous in baseline["files"].items():
    path = ROOT / relative
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != previous["sha256"]:
        changes.append(relative)

errors = []
for name in EXPECTED:
    if not (DOMAIN / name).is_file():
        errors.append(f"Missing deliverable: {name}")

documents = {p.name: p.read_text(encoding="utf-8") for p in DOMAIN.glob("*.md")}
if set(documents) != set(EXPECTED):
    errors.append("Domain document set differs from requested ten deliverables")
mermaid_count = 0
for name, contents in documents.items():
    path = DOMAIN / name
    if contents.count("```") % 2:
        errors.append(f"Unbalanced code fences: {name}")
    mermaid_count += contents.count("```mermaid")
    for match in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", contents):
        target = match.group(1)
        if re.match(r"[a-zA-Z]+://", target):
            continue
        relative, _, anchor = target.partition("#")
        linked = path.parent / relative if relative else path
        if not linked.is_file():
            errors.append(f"Missing link target: {name} -> {target}")
        elif anchor and linked.suffix == ".md":
            headings = re.findall(r"^#{1,6}\s+(.+)$", linked.read_text(encoding="utf-8"), re.M)
            if anchor not in {heading_slug(h) for h in headings}:
                errors.append(f"Missing heading target: {name} -> {target}")

catalog = documents.get("01-entity-catalog.md", "")
sections = re.split(r"^## (E\d\d) — (.+)$", catalog, flags=re.M)
entity_ids = []
fields = [
    "Purpose / treatment", "Grain / identity", "Ownership", "Attributes",
    "Relationships", "Lifecycle", "Invariants", "Sources / map", "Questions",
]
for index in range(1, len(sections), 3):
    entity_id, title, body = sections[index:index + 3]
    entity_ids.append(entity_id)
    for field in fields:
        if field not in body and not (
            field == "Sources / map" and "Sources / historical-current map" in body
        ):
            errors.append(f"Missing catalog field: {entity_id} {field}")
if entity_ids != [f"E{i:02}" for i in range(1, 27)]:
    errors.append("Entity ID sequence differs from the declared 26 kinds")

decision_text = documents.get("07-policy-decision-register.md", "")
decisions = set(re.findall(r"\| (PD\d\d) ", decision_text))
invariants = set(re.findall(r"\| (I\d\d) \|", documents.get("05-domain-invariants.md", "")))
all_text = "\n".join(documents.values())
for prefix, defined in [("PD", decisions), ("I", invariants), ("E", set(entity_ids))]:
    referenced = set(re.findall(rf"\b{prefix}\d\d\b", all_text))
    for undefined in sorted(referenced - defined):
        errors.append(f"Undefined reference: {undefined}")
if len(decisions) != 25:
    errors.append("Decision register differs from the declared 25 entries")

result = {
    "review_date": "2026-10-14",
    "protected_files_checked": len(baseline["files"]),
    "protected_source_files": sum(p.startswith("source/") for p in baseline["files"]),
    "protected_reconstruction_documents": sum(p.startswith("docs/reconstruction/") for p in baseline["files"]),
    "protected_existing_evidence_files": sum(p.startswith("evidence/") for p in baseline["files"]),
    "baseline_changes": changes,
    "deliverables": sorted(documents),
    "entity_kinds": len(entity_ids),
    "policy_decisions": len(decisions),
    "invariants": len(invariants),
    "mermaid_diagrams": mermaid_count,
    "validation_errors": errors,
    "pass": not changes and not errors,
    "limits": [
        "Checks are structural/provenance checks, not proof of business-policy correctness.",
        "Mermaid fences and linked headings checked; diagrams not renderer-tested.",
        "No application code, production actions, or Phase 1 modifications.",
    ],
}
REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if result["pass"] else 1)
