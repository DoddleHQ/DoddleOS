#!/usr/bin/env python3
"""Lint the pack: skill structure, frontmatter, blueprints, links, secrets, market claims.

Run: ``python3 scripts/lint_pack.py`` (exit 1 on any error). Pure stdlib.
"""

from __future__ import annotations

import os
import re
import sys
from typing import Dict, List, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, ".claude", "skills")
COMMON = os.path.join(SKILLS_DIR, "common")
REQUIRED_FM = ("name", "id", "version", "blueprint", "description")
BLUEPRINT_REQUIRED = ("id", "kind", "engine")

# Tool IDs the blueprints are allowed to reference.
TOOL_REGISTRY = {
    "doddle.tool.v1.cli.dseo",
    "doddle.tool.v1.ga4.getReport",
    "doddle.tool.v1.gsc.query",
    "doddle.tool.v1.hubspot.contacts",
    "doddle.tool.v1.notion.pages",
    "doddle.tool.v1.semrush.domain",
    "doddle.tool.v1.dataforseo.serp",
    "doddle.tool.v1.ahrefs.backlinks",
}
TOOL_RE = re.compile(r"\bdoddle\.tool\.[A-Za-z0-9_.]+")
LINK_RE = re.compile(r"\]\(([^)]+)\)")
# Market-size / share claims we agreed never to hardcode.
MARKET_RE = re.compile(r"\$\s?\d+(\.\d+)?\s?(B|M|bn|billion|million)\b", re.IGNORECASE)
SECRET_RE = re.compile(r"(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{20,})")


class Lint:
    def __init__(self) -> None:
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def parse_frontmatter(text: str) -> Dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    data: Dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def _blueprint_scalar(text: str, key: str) -> str:
    match = re.search(rf"^{key}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip().strip('"').strip("'") if match else ""


def lint_skill(skill_dir: str, lint: Lint) -> None:
    name = os.path.basename(skill_dir)
    skill_md = os.path.join(skill_dir, "SKILL.md")
    blueprint = os.path.join(skill_dir, "blueprint.yaml")
    if not os.path.isfile(skill_md):
        lint.error(f"{name}: missing SKILL.md")
        return
    if not os.path.isfile(blueprint):
        lint.error(f"{name}: missing blueprint.yaml")
    text = _read(skill_md)
    fm = parse_frontmatter(text)
    for key in REQUIRED_FM:
        if key not in fm:
            lint.error(f"{name}: frontmatter missing '{key}'")
    if fm.get("name") and fm["name"] != name:
        lint.error(f"{name}: frontmatter name '{fm['name']}' != dirname")
    if fm.get("id") and fm["id"] != f"doddle.seo.{name}":
        lint.error(f"{name}: id should be doddle.seo.{name}, got {fm.get('id')}")
    if fm.get("description") and len(fm["description"]) < 30:
        lint.warn(f"{name}: description looks too short")
    for section in ("## Response Contract", "## Related Skills"):
        if section not in text:
            lint.warn(f"{name}: missing '{section}' section")

    # market-stat and secret scan
    for label, pattern in (("market-size claim", MARKET_RE), ("possible secret", SECRET_RE)):
        for m in pattern.finditer(text):
            lint.error(f"{name}: {label}: {m.group(0)!r}")

    # relative links resolve (ignore links inside inline/fenced code)
    text_no_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text_no_code = re.sub(r"`[^`]*`", "", text_no_code)
    for link in LINK_RE.findall(text_no_code):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = link.split("#", 1)[0]
        if not target:
            continue
        resolved_os = os.path.normpath(os.path.join(skill_dir, target))
        if not os.path.exists(resolved_os):
            lint.error(f"{name}: broken link '{link}'")

    if os.path.isfile(blueprint):
        bp = _read(blueprint)
        for key in BLUEPRINT_REQUIRED:
            if not _blueprint_scalar(bp, key):
                lint.error(f"{name}: blueprint missing '{key}'")
        if _blueprint_scalar(bp, "kind") and _blueprint_scalar(bp, "kind") != "skill":
            lint.error(f"{name}: blueprint kind must be 'skill'")
        expected_id = f"doddle.seo.{name}"
        if _blueprint_scalar(bp, "id") and _blueprint_scalar(bp, "id") != expected_id:
            lint.error(f"{name}: blueprint id '{_blueprint_scalar(bp, 'id')}' != {expected_id}")
        for tool in set(TOOL_RE.findall(bp)):
            if tool not in TOOL_REGISTRY:
                lint.error(f"{name}: blueprint references unknown tool '{tool}'")
        for label, pattern in (("market-size claim", MARKET_RE), ("possible secret", SECRET_RE)):
            for m in pattern.finditer(bp):
                lint.error(f"{name}: blueprint {label}: {m.group(0)!r}")


def lint_common(lint: Lint) -> None:
    if not os.path.isdir(COMMON):
        lint.error("missing .claude/skills/common/")
        return
    for required in ("response-contract.md", "data-reliability.md", "fundamentals.md", "scoring-methodology.md", "mcp-integration-guide.md"):
        if not os.path.isfile(os.path.join(COMMON, required)):
            lint.error(f"common: missing {required}")


def lint_manifests(lint: Lint) -> None:
    for rel in (".claude-plugin/plugin.json", "marketplace.json", "package.json"):
        path = os.path.join(ROOT, rel)
        if not os.path.isfile(path):
            lint.error(f"missing manifest: {rel}")
            continue
        try:
            import json

            json.loads(_read(path))
        except json.JSONDecodeError as exc:
            lint.error(f"{rel}: invalid JSON: {exc}")


def run(lint: Lint) -> None:
    lint_manifests(lint)
    lint_common(lint)
    if not os.path.isdir(SKILLS_DIR):
        lint.error("missing .claude/skills/")
        return
    skill_dirs = [
        os.path.join(SKILLS_DIR, d)
        for d in sorted(os.listdir(SKILLS_DIR))
        if os.path.isdir(os.path.join(SKILLS_DIR, d)) and d != "common"
    ]
    if not skill_dirs:
        lint.error("no skills found under .claude/skills/")
    for skill_dir in skill_dirs:
        lint_skill(skill_dir, lint)


def main() -> int:
    lint = Lint()
    run(lint)
    for w in lint.warnings:
        print(f"WARN  {w}")
    for e in lint.errors:
        print(f"ERROR {e}")
    print(f"\nlint_pack: {len(lint.errors)} error(s), {len(lint.warnings)} warning(s)")
    return 1 if lint.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
