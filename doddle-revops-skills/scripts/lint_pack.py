#!/usr/bin/env python3
"""Lint the Doddle RevOps pack: structure, frontmatter, blueprints, links, secrets."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

PACK = Path(__file__).resolve().parent.parent
SKILLS = PACK / ".claude" / "skills"
AGENTS = PACK / ".claude" / "agents"
EXPECTED_SKILLS = {"revops-data-infrastructure", "revops-pql-scoring", "revops-attribution"}
EXPECTED_AGENTS = {"revops-data-engineer", "revops-analyst"}
REQUIRED_SECTIONS = [
    "## Deterministic Toolkit",
    "## Workflow",
    "## Sub-flows",
    "## Response Contract",
    "## Common Mistakes",
    "## Related Skills",
    "## Inputs",
    "## Outputs",
]
REQUIRED_FM = ["name", "id", "version", "blueprint", "description"]
FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)
TOOL_RE = re.compile(r"doddle\.tool\.(?:cli\.[\w-]+|v1\.[\w-]+\.[\w-]+)")
SECRET_RE = re.compile(
    "(sk_" + "live_|sk_" + "test_|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY)")


def parse_frontmatter(text: str) -> dict:
    match = FM_RE.match(text)
    if not match:
        return {}
    out = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip().strip('"')
    return out


def run_checks() -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []

    skill_dirs = {d.name for d in SKILLS.iterdir() if d.is_dir() and d.name != "common"}
    if skill_dirs != EXPECTED_SKILLS:
        errors.append(f"skill inventory mismatch: expected {sorted(EXPECTED_SKILLS)}, found {sorted(skill_dirs)}")

    agent_files = {p.stem for p in AGENTS.glob("*.md")}
    if agent_files != EXPECTED_AGENTS:
        errors.append(f"agent inventory mismatch: expected {sorted(EXPECTED_AGENTS)}, found {sorted(agent_files)}")

    for name in sorted(EXPECTED_AGENTS):
        path = AGENTS / f"{name}.md"
        if not path.exists():
            continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        for key in ("name", "description"):
            if not fm.get(key):
                errors.append(f"{path}: missing frontmatter '{key}'")
        if fm.get("name") and fm["name"] != name:
            errors.append(f"{path}: frontmatter name '{fm['name']}' != filename '{name}'")

    for skill_dir in sorted(SKILLS.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name == "common":
            continue
        skill_md = skill_dir / "SKILL.md"
        blueprint = skill_dir / "blueprint.yaml"
        if not skill_md.exists():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        if not blueprint.exists():
            errors.append(f"{skill_dir}: missing blueprint.yaml")
            continue

        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        for key in REQUIRED_FM:
            if not fm.get(key):
                errors.append(f"{skill_md}: missing frontmatter '{key}'")
        if fm.get("name") and fm["name"] != skill_dir.name:
            errors.append(f"{skill_md}: name '{fm['name']}' != directory '{skill_dir.name}'")
        expected_id = f"doddle.revops.{skill_dir.name}"
        if fm.get("id") and fm["id"] != expected_id:
            errors.append(f"{skill_md}: id '{fm['id']}' != '{expected_id}'")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{skill_md}: missing section '{section}'")

        bp = blueprint.read_text(encoding="utf-8")
        bp_id = re.search(r"^id:\s*(\S+)", bp, re.M)
        if not bp_id:
            errors.append(f"{blueprint}: missing id")
        elif bp_id.group(1) != fm.get("id"):
            errors.append(f"{blueprint}: id '{bp_id.group(1)}' != frontmatter id '{fm.get('id')}'")
        for key in ("version:", "kind: skill", "engine:", "inputs:", "outputs:", "tools:", "nodes:", "on_fail:"):
            if key not in bp:
                errors.append(f"{blueprint}: missing '{key}'")
        for tool_id in re.findall(r"id:\s*(doddle\.tool\.[^\s,}]+)", bp):
            if not TOOL_RE.fullmatch(tool_id):
                errors.append(f"{blueprint}: invalid tool id '{tool_id}'")
        for ref in re.findall(r"ref:\s*([^\s,}]+)", bp):
            if ref.startswith("doddle.tool."):
                continue
            if ref not in agent_files:
                errors.append(f"{blueprint}: unknown agent ref '{ref}'")
        outputs_section = re.search(r"^outputs:\s*\n((?:[ \t]+.*\n?)*)", bp, re.M)
        declared = set(re.findall(r"name:\s*([^,\s\}]+)", outputs_section.group(1) if outputs_section else ""))
        produced = set()
        for lst in re.findall(r"produces:\s*\[([^\]]*)\]", bp):
            produced |= {x.strip() for x in lst.split(",") if x.strip()}
        missing = declared - produced
        if missing:
            errors.append(f"{blueprint}: outputs never produced: {sorted(missing)}")

        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = link.split("#", 1)[0]
            if not target:
                continue
            if not (skill_dir / target).exists():
                errors.append(f"{skill_md}: broken relative link '{link}'")

        for file_path in PACK.rglob("*"):
            if not file_path.is_file() or ".git" in file_path.parts:
                continue
            if file_path.suffix not in {".md", ".py", ".json", ".yaml", ".yml", ".csv"}:
                continue
            try:
                content = file_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if SECRET_RE.search(content):
                errors.append(f"{file_path}: possible secret committed")

    try:
        result = subprocess.run([sys.executable, str(PACK / "scripts" / "drev"), "version"],
                                capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            errors.append("drev version failed to run")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"drev version failed to run: {exc}")

    return errors, warnings


def main() -> int:
    errors, warnings = run_checks()
    for warning in warnings:
        print(f"WARN {warning}")
    for error in errors:
        print(f"ERR {error}")
    print(f"\nlint_pack: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
