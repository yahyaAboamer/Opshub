"""Read-only Phase 3 document/integrity checks; writes only verification.json."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
PRODUCT = ROOT / "docs" / "product"
EXPECTED = [
    "00-owner-decisions.md",
    "01-product-vision-and-scope.md",
    "02-personas-and-permissions.md",
    "03-mvp-feature-prioritization.md",
    "04-merchant-workflows.md",
    "05-platform-admin-workflows.md",
    "06-analytics-and-kpis.md",
    "07-configuration-and-policy.md",
    "08-data-ingestion-and-integrations-requirements.md",
    "09-saas-commercial-requirements.md",
    "10-audit-data-quality-and-trust.md",
    "11-mvp-acceptance-criteria.md",
    "12-out-of-scope-and-future.md",
    "13-open-product-decisions.md",
    "14-prd.md",
]


def anchors(path):
    result = set()
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not re.match(r"^#{1,6} ", line):
            continue
        name = re.sub(r"^#{1,6} ", "", line).lower()
        name = re.sub(r"[^\w\- ]", "", name).replace(" ", "-")
        result.add(name)
    return result


files = sorted(PRODUCT.glob("*.md"))
errors = []
if [p.name for p in files] != EXPECTED:
    errors.append("Product document inventory differs from required 15 files")

manifest = json.loads((ROOT / "evidence/product/phase3-baseline-manifest.json").read_text(encoding="utf-8-sig"))
changed = []
for row in manifest["protected"]:
    path = ROOT / row["path"]
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
        changed.append(row["path"])
if changed:
    errors.append("Pre-existing protected evidence/domain/reconstruction/source changed")

links_checked = 0
broken_links = []
format_errors = []
naming_hits = []
inventories = {}
for path in files:
    body = path.read_text(encoding="utf-8-sig")
    inventories[path.name] = {
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "words": len(body.split()),
    }
    for number, line in enumerate(body.splitlines(), 1):
        if re.search(r"Gentry (?:SaaS will|will provide|must provide|MVP will)", line, re.I):
            naming_hits.append({"file": path.name, "line": number, "text": line})
    for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", body):
        target = match.group(1).strip("<>")
        if re.match(r"[a-z]+://", target):
            continue
        relative, _, anchor = target.partition("#")
        resolved = (path.parent / relative).resolve() if relative else path
        links_checked += 1
        if not resolved.exists():
            broken_links.append({"file": path.name, "target": target, "reason": "missing file"})
        elif anchor and resolved.suffix == ".md" and anchor not in anchors(resolved):
            broken_links.append({"file": path.name, "target": target, "reason": "missing heading anchor"})
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"^#{1,6} ", line) and i + 1 < len(lines) and lines[i + 1].strip():
            format_errors.append({"file": path.name, "line": i + 1, "reason": "heading needs blank line"})
        if re.match(r"^- ", line) and i > 0 and lines[i - 1].strip() and not re.match(r"^- ", lines[i - 1]):
            format_errors.append({"file": path.name, "line": i + 1, "reason": "list needs preceding blank line"})
if broken_links:
    errors.append("Broken product-document links")
if format_errors:
    errors.append("Markdown spacing violations")
if naming_hits:
    errors.append("Future product appears named Gentry")

owner = (PRODUCT / EXPECTED[0]).read_text(encoding="utf-8-sig")
if not all(f"## OD{i:02}" in owner for i in range(1, 10)):
    errors.append("Missing approved owner decision")
priorities = (PRODUCT / EXPECTED[3]).read_text(encoding="utf-8-sig")
if not all(label in priorities for label in ["MUST HAVE — MVP", "SHOULD HAVE — shortly after MVP", "LATER", "EXCLUDED"]):
    errors.append("Missing prioritization class")
workflows = (PRODUCT / EXPECTED[4]).read_text(encoding="utf-8-sig")
if not all(f"## WF{i:02}" in workflows for i in range(1, 12)):
    errors.append("Missing merchant workflow")
platform = (PRODUCT / EXPECTED[5]).read_text(encoding="utf-8-sig")
if not all(f"## PF{i:02}" in platform for i in range(1, 6)):
    errors.append("Missing platform workflow")
metrics = (PRODUCT / EXPECTED[6]).read_text(encoding="utf-8-sig")
for section in re.split(r"\n## K\d\d", metrics)[1:]:
    if "K03" not in section and "RTO Rate" not in section:
        for field in ["**Numerator:", "**Denominator:", "**Included:", "**Excluded:", "**Time:", "**Drill-down:"]:
            if field not in section:
                errors.append(f"KPI contract field missing: {field}")
acceptance = (PRODUCT / EXPECTED[11]).read_text(encoding="utf-8-sig")
if not all(f"## AC{i:02}" in acceptance for i in range(1, 16)):
    errors.append("Missing acceptance gate")

# OD08/OD09 bounded scope checks; document assertions, not product tests.
correction_checks = {}
for feature in ["F19", "F20", "F24"]:
    row = next((line for line in priorities.splitlines() if line.startswith(f"| {feature} |")), "")
    correction_checks[f"{feature}_must_have"] = "MUST HAVE — MVP" in row
correction_checks["ROAS_is_MVP"] = "## K07 — ROAS (MUST HAVE — MVP)" in metrics
correction_checks["product_contracts"] = all(f"| P{i:02} " in metrics for i in range(1, 7))
integration = (PRODUCT / EXPECTED[8]).read_text(encoding="utf-8-sig")
correction_checks["named_pilot_providers"] = all(name in integration for name in ["Shopify", "Bosta", "Meta"])
correction_checks["integrated_action_and_fallback"] = all(label in integration for label in ["ACT01", "ACT02", "ACT03", "FB01", "FB02", "FB03"])
correction_manifest_path = ROOT / "evidence/product/od08-od09-baseline-manifest.json"
correction_changed = []
if correction_manifest_path.exists():
    correction_baseline = json.loads(correction_manifest_path.read_text(encoding="utf-8-sig"))
    for row in correction_baseline["files"]:
        if hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() != row["sha256"]:
            correction_changed.append(row["path"])
    correction_checks["commercial_document_unchanged"] = "docs/product/09-saas-commercial-requirements.md" not in correction_changed
for check, passed in correction_checks.items():
    if not passed:
        errors.append(f"OD08/OD09 check failed: {check}")
result = {
    "date": "2026-10-14",
    "kind": "Documentation checks only; no application validation or owner approval implied",
    "passed": not errors,
    "product_document_count": len(files),
    "protected_file_count": len(manifest["protected"]),
    "protected_changes": changed,
    "links_checked": links_checked,
    "broken_links": broken_links,
    "format_errors": format_errors,
    "naming_pattern_hits": naming_hits,
    "errors": errors,
    "od08_od09_checks": correction_checks,
    "correction_changed_documents": correction_changed,
    "documents": inventories,
}
(ROOT / "evidence/product/verification.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in result.items() if k != "documents"}, indent=2, ensure_ascii=False))
raise SystemExit(0 if result["passed"] else 1)
