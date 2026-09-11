#!/usr/bin/env python3
"""Validate DoddleOS skills: SKILL.md + blueprint.yaml pairs.

Usage (repo root): python3 doddle-core/scripts/validate.py [--strict]
Discovery-based: scans .claude/skills/ plus every doddle-*/.claude/skills/
pack found on disk. Adding a pack requires NO validator edit.

Checks (stdlib only, no deps):
- SKILL.md frontmatter has name, id, version, blueprint, description
- blueprint.yaml exists, has id/version/kind/engine/inputs/outputs/nodes
- frontmatter id == blueprint id
- tool IDs use doddle.tool.v1 namespace
- nodes have id/type/needs
Exit 1 on errors, 0 on pass (warnings ok unless --strict).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SKILL_DIRS = [d for d in sorted((ROOT / ".claude" / "skills").glob("*/")) if d.is_dir()]
SKILL_DIRS += [d for d in sorted(ROOT.glob("doddle-*/.claude/skills/*/")) if d.is_dir()]
SKIP = {"common", "document-skills"}

FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)
REQUIRED_FM = ["name", "id", "version", "blueprint", "description"]
TOOL_RE = re.compile(r"doddle\.tool\.v1\.[\w-]+\.[\w-]+")
NODE_TYPES = {"agent", "tool", "call", "gate"}


def section(text, key):
    m = re.search(r"^" + key + r":\s*\n((?:[ \t]+.*\n?)*)", text, re.M)
    return m.group(1) if m else ""


def collect_ids(dirs):
    ids = set()
    for d in dirs:
        if not d.is_dir():
            continue
        skill = d / "SKILL.md"
        if skill.exists():
            fm = parse_fm(skill.read_text())
            if fm.get("id"):
                ids.add(fm["id"])
        bp = d / "blueprint.yaml"
        if bp.exists():
            m = re.search(r"^id:\s*(\S+)", bp.read_text(), re.M)
            if m:
                ids.add(m.group(1))
    return ids


def parse_fm(text):
    m = FM_RE.search(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def check_skill(d, errors, warnings, known_ids):
    name = d.name
    if name in SKIP:
        return
    skill = d / "SKILL.md"
    if not skill.exists():
        warnings.append(f"{d}: missing SKILL.md")
        return
    fm = parse_fm(skill.read_text())
    for f in REQUIRED_FM:
        if f not in fm or not fm[f]:
            errors.append(f"{skill}: missing frontmatter '{f}' (v2 required)")
    bp_path = d / fm.get("blueprint", "./blueprint.yaml").lstrip("./")
    if not bp_path.exists():
        warnings.append(f"{skill}: missing {bp_path.name} (migration pending)")
        return
    bp = bp_path.read_text()
    for key in ["id:", "version:", "kind: skill", "engine:", "inputs:", "outputs:", "nodes:"]:
        if key not in bp:
            errors.append(f"{bp_path}: missing '{key}'")
    m = re.search(r"^id:\s*(\S+)", bp, re.M)
    if m and "id" in fm and m.group(1) != fm["id"]:
        errors.append(f"{skill}: frontmatter id {fm['id']} != blueprint id {m.group(1)}")
    if "doddle.tool" in bp and not TOOL_RE.search(bp):
        errors.append(f"{bp_path}: tool IDs must use doddle.tool.v1.<server>.<tool>")
    if "needs:" not in bp:
        errors.append(f"{bp_path}: nodes must declare needs:")
    own = fm.get("id", "")
    nodes_sec = section(bp, "nodes")
    for lit in re.findall(r"\{[^{}]*\}", nodes_sec):
        tm = re.search(r"type:\s*(\w+)", lit)
        if not tm:
            errors.append(f"{bp_path}: node missing type: {lit[:60]}")
            continue
        t = tm.group(1)
        if t not in NODE_TYPES:
            errors.append(f"{bp_path}: unknown node type '{t}'")
        if t == "call":
            rm = re.search(r"ref:\s*([^\s,}]+)", lit)
            if not rm:
                errors.append(f"{bp_path}: call node missing ref")
            elif rm.group(1) not in known_ids:
                errors.append(f"{bp_path}: call ref unknown skill '{rm.group(1)}'")
            elif rm.group(1) == own:
                errors.append(f"{bp_path}: skill calls itself")
        if t == "gate" and ("approvers:" not in nodes_sec or "timeout_s" not in nodes_sec):
            errors.append(f"{bp_path}: gate node requires approvers + timeout_s")
    ffm = re.search(r"^fallback_for:\s*(.+)$", bp, re.M)
    if ffm:
        for item in re.findall(r"[\w.]+", ffm.group(1)):
            if item == own:
                errors.append(f"{bp_path}: fallback_for self-reference")
            elif item not in known_ids:
                errors.append(f"{bp_path}: fallback_for unknown skill '{item}'")
    out_names = set(re.findall(r"name:\s*([^,\s\}]+)", section(bp, "outputs")))
    produced = set()
    for lst in re.findall(r"produces:\s*\[([^\]]*)\]", bp):
        produced |= {x.strip() for x in lst.split(",") if x.strip()}
    missing = out_names - produced
    if missing:
        errors.append(f"{bp_path}: outputs never produced: {sorted(missing)}")


def main():
    strict = "--strict" in sys.argv
    errors, warnings = [], []
    known_ids = collect_ids(SKILL_DIRS)
    for d in SKILL_DIRS:
        if d.is_dir():
            check_skill(d, errors, warnings, known_ids)
    for w in warnings:
        print(f"WARN {w}")
    for e in errors:
        print(f"ERR {e}")
    print(f"\n{len(errors)} errors, {len(warnings)} warnings across {len(SKILL_DIRS)} dirs")
    if errors or (strict and warnings):
        sys.exit(1)


if __name__ == "__main__":
    main()
