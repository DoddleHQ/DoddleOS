"""Pack tests: structure, frontmatter/blueprint ids, tool registry, common refs, no market claims."""

import json
import os
import re
import sys

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


NODE_RE = re.compile(
    r"^\s+- \{id: (?P<id>[^,]+), type: (?P<type>[^,]+), ref: (?P<ref>[^,]+)"
    r"(?:, args: (?P<args>\[[^\]]*\]))?, needs: \[(?P<needs>[^\]]*)\], "
    r"produces: \[(?P<produces>[^\]]*)\]\}$",
    re.MULTILINE,
)


def _items(value):
    return [item.strip() for item in value.split(",") if item.strip()]


def _nodes(text):
    nodes = []
    for match in NODE_RE.finditer(text):
        node = match.groupdict()
        node["args"] = json.loads(node["args"]) if node["args"] else []
        node["needs"] = _items(node["needs"])
        node["produces"] = _items(node["produces"])
        nodes.append(node)
    return nodes


def _declared_outputs(text):
    match = re.search(r"^outputs:\n((?:  - .*\n)+)", text, re.MULTILINE)
    assert match, "missing outputs block"
    return set(re.findall(r"\{name: ([^,]+),", match.group(1)))


def _declared_tools(text):
    return set(re.findall(
        r"^  - \{id: (doddle\.tool\.[A-Za-z0-9_.]+), required: false, fallback: manual_review\}$",
        text, re.MULTILINE))


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
def test_blueprint_graph_integrity_and_tool_invocations(path):
    text = _read(os.path.join(path, "blueprint.yaml"))
    nodes = _nodes(text)
    assert nodes, "no parsed nodes"

    available = {"inputs"}
    produced = set()
    for node in nodes:
        assert node["needs"], f"{node['id']} has no dependency"
        for need in node["needs"]:
            assert need in available, f"{node['id']} needs unknown/later {need}"
        assert node["produces"], f"{node['id']} produces nothing"
        available.add(node["id"])
        produced.update(node["produces"])
    assert _declared_outputs(text) <= produced, "declared output is never produced"

    declared = _declared_tools(text)
    invoked = {node["ref"] for node in nodes if node["type"] == "tool"}
    assert declared == invoked, "tool declarations and invocations differ"
    first_agent = next(i for i, node in enumerate(nodes) if node["type"] == "agent")
    for node in nodes:
        if node["type"] == "tool" and node["ref"].startswith("doddle.tool.v1."):
            assert node["args"], "MCP invocation lacks an input mapping"
            assert all(arg.startswith("{inputs.") for arg in node["args"])
            assert nodes.index(node) < first_agent, "MCP node must run before narration"


FRAMEWORK_SLUGS = {
    "gtm-positioning": "positioning-canvas",
    "gtm-messaging": "messaging-house",
    "gtm-competitive": "competitive-teardown",
    "gtm-persona": "persona-template",
    "gtm-outbound": "demand-gen-plan",
    "gtm-launch": "launch-checklist",
    "gtm-sales-narrative": "sales-narrative",
    "gtm-enablement": "sales-narrative",
    "gtm-battlecards": "battlecard",
    "gtm-partnerships": "partnership-model",
}


@pytest.mark.parametrize("slug,framework", FRAMEWORK_SLUGS.items())
def test_framework_nodes_require_the_intended_slug(slug, framework):
    text = _read(os.path.join(SKILLS, slug, "blueprint.yaml"))
    calls = [node["args"] for node in _nodes(text)
             if node["ref"] == "doddle.tool.cli.dgtm" and node["args"][0] == "frameworks"]
    assert calls == [["frameworks", "--name", framework]]


def test_pipeline_segment_is_wired_into_audit_and_report():
    text = _read(os.path.join(SKILLS, "gtm-pipeline-analytics", "blueprint.yaml"))
    calls = {node["args"][0]: node["args"] for node in _nodes(text)
             if node["ref"] == "doddle.tool.cli.dgtm"}
    assert calls["audit"] == ["audit", "{inputs.export}", "--segment", "{inputs.segment}"]
    assert calls["report"] == ["report", "{inputs.export}", "--segment", "{inputs.segment}"]


@pytest.mark.parametrize("slug", ["gtm-icp", "gtm-abm"])
def test_clearbit_has_an_optional_explicit_domain_binding(slug):
    text = _read(os.path.join(SKILLS, slug, "blueprint.yaml"))
    assert "doddle.tool.v1.clearbit.company" in _declared_tools(text)
    live = [node for node in _nodes(text) if node["ref"] == "doddle.tool.v1.clearbit.company"]
    assert len(live) == 1
    assert live[0]["args"] == ["{inputs.domain}"]
    assert live[0]["needs"] == ["run"]
    agent = next(node for node in _nodes(text) if node["type"] == "agent")
    assert agent["needs"] == ["run", "live_1"]


def test_blueprints_match_generator():
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import gen_blueprints  # noqa: E402

    assert len(gen_blueprints.SPECS) == len(skill_dirs)
    for spec in gen_blueprints.SPECS:
        slug = spec[0]
        assert _read(os.path.join(SKILLS, slug, "blueprint.yaml")) == gen_blueprints.build(spec), slug


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


def test_export_paths_are_positional_in_docs():
    advocacy = _read(os.path.join(SKILLS, "gtm-advocacy", "SKILL.md"))
    revenue_ops = _read(os.path.join(AGENTS, "revenue-operations.md"))
    partner_manager = _read(os.path.join(AGENTS, "partner-manager.md"))
    assert "dgtm report <export.json|csv>" in advocacy
    assert "dgtm report --export" not in advocacy
    assert "dgtm audit <export.json|csv>" in revenue_ops
    assert "dgtm audit --export" not in revenue_ops
    assert "dgtm report --export" not in partner_manager


def test_manifests_parse():
    for rel in (".claude-plugin/plugin.json", "marketplace.json", "package.json"):
        json.loads(_read(os.path.join(ROOT, rel)))
