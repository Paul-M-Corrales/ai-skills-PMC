"""Basic stdlib-only local Agent Skills validation. Not a full YAML parser."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
name_pattern = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
if not paths:
    errors.append("No skills found")
for path in paths:
    content = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not match:
        errors.append(f"{path}: missing YAML frontmatter")
        continue
    header = match.group(1)
    name = re.search(r"^name:\s*(\S+)\s*$", header, re.M)
    description = re.search(r"^description:\s*(.+?)\s*$", header, re.M)
    if not name or not name_pattern.fullmatch(name.group(1)) or name.group(1) != path.parent.name or len(name.group(1)) > 64:
        errors.append(f"{path}: invalid or mismatched name")
    if not description or not (1 <= len(description.group(1)) <= 1024):
        errors.append(f"{path}: missing or invalid description")
    if not content[match.end():].strip():
        errors.append(f"{path}: empty instructions")

catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
seen = set()
for item in catalog["sources"]:
    if item["id"] in seen or not item["url"].startswith("https://github.com/"):
        errors.append(f"Invalid or duplicate catalog entry: {item['id']}")
    seen.add(item["id"])
if errors:
    print("\n".join("ERROR: " + item for item in errors))
    sys.exit(1)
print(f"PASS: {len(paths)} skills and {len(seen)} catalog sources validated (basic checks)")
