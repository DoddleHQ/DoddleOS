"""Pack tests: structure, frontmatter/blueprint ids, tool registry, common refs, no market claims."""

import json
import os
import re

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, ".claude", "skills")
AGENTS = os.path.join(ROOT, ".claude", "agents")
COMMON = os.path.join(SKILLS, "common")

TOOL_REGISTRY = {
    "doddle.tool.cli.dgtm",
    "doddle.tool.v1.hubspot.deals",
    "doddle.tool.v1.salesforce.opportunities",
    "doddle.tool.v1.gong.calls",
    "doddle.tool.v1.clearbit.company",
    "doddle.tool.v1.ga4.getReport",
    "doddle.tool.v1.linkedin.ads",
    "doddle.tool.v1.notion.pages",
}
MARKET_RE = re.compile(r"\$\s?\d+(\.\d+)?\s?(B|M|bn|billion|million)\b", re.IGNORECASE)
TOOL_RE = re.compile(r"\bdoddle\.tool\.[A-Za-z0-9_.]+")

skill_dirs = sorted(
    os.path.join(SKILLS, d) for d in os.listdir(SKILLS)
    if os.path.isdir(os.path.join(SKILLS, d)) and d != "common"
) if os.path.isdir(SKILLS) else []


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _frontmatter(text):
    assert text.startswith("---"), "missing frontmatter"
    end = text.find("\n---", 3)
    block = text[3:end]
    data = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            k, _, v = line.partition(":")
            data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def test_thirty_skills():
    assert len(skill_dirs) == 32


@pytest.mark.parametrize("path", skill_dirs, ids=[os.path.basename(p) for p in skill_dirs])
def test_skill_structure(path):
    name = os.path.basename(path)
    skill_md = os.path.join(path, "SKILL.md")
    blueprint = os.path.join(path, "blueprint.yaml")
    assert os.path.isfile(skill_md), "missing SKILL.md"
    assert os.path.isfile(blueprint), "missing blueprint.yaml"

    fm = _frontmatter(_read(skill_md))
    assert fm["name"] == name
    assert fm["id"] == f"doddle.gtm.{name}"
    assert fm.get("blueprint") == "./blueprint.yaml"

    body = _read(skill_md)
    for section in ("## Workflow", "## Response Contract", "## Related Skills", "## Inputs", "## Outputs"):
        assert section in body, f"missing {section}"

    bp = _read(blueprint)
    assert f"id: doddle.gtm.{name}" in bp
    for tool in set(TOOL_RE.findall(bp)):
        assert tool in TOOL_REGISTRY, f"unknown tool {tool}"


@pytest.mark.parametrize("path", skill_dirs, ids=[os.path.basename(p) for p in skill_dirs])
def test_no_market_claims(path):
    for fname in ("SKILL.md", "blueprint.yaml"):
        text = _read(os.path.join(path, fname))
        assert not MARKET_RE.search(text), f"market-size claim in {fname}"


def test_common_refs_present():
    for ref in ("response-contract.md", "data-reliability.md", "fundamentals.md",
                "scoring-methodology.md", "frameworks-registry.md", "mcp-integration-guide.md"):
        assert os.path.isfile(os.path.join(COMMON, ref))


def test_seven_agents():
    agents = sorted(f for f in os.listdir(AGENTS) if f.endswith(".md"))
    assert agents == ["demand-gen-strategist.md", "enablement-lead.md", "gtm-strategist.md",
                      "partner-manager.md", "positioning-strategist.md", "revenue-analyst.md",
                      "revenue-operations.md"]


def test_manifests_parse():
    for rel in (".claude-plugin/plugin.json", "marketplace.json", "package.json"):
        json.loads(_read(os.path.join(ROOT, rel)))
