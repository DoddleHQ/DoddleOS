import json
import re
import subprocess
import sys
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PACK / "scripts"))

from lint_pack import EXPECTED_AGENTS, EXPECTED_SKILLS, run_checks  # noqa: E402


def test_pack_lint_is_clean():
    errors, warnings = run_checks()
    assert errors == []
    assert warnings == []


def test_pack_inventory():
    skills = {d.name for d in (PACK / ".claude" / "skills").iterdir() if d.is_dir() and d.name != "common"}
    agents = {p.stem for p in (PACK / ".claude" / "agents").glob("*.md")}
    assert skills == EXPECTED_SKILLS
    assert agents == EXPECTED_AGENTS


def test_every_skill_has_a_blueprint_and_shared_references():
    for name in EXPECTED_SKILLS:
        assert (PACK / ".claude" / "skills" / name / "SKILL.md").exists()
        assert (PACK / ".claude" / "skills" / name / "blueprint.yaml").exists()
    for reference in ("evidence-envelope.md", "data-contracts.md", "pql-model.md", "attribution-models.md"):
        assert (PACK / ".claude" / "skills" / "common" / reference).exists()


def test_write_capable_tools_are_gated():
    """A blueprint may only bind a write-capable tool behind an approval gate."""
    registry = PACK.parent / "doddle-core" / "registry" / "integrations"
    write_tools = set()
    for config in registry.glob("*/config.json"):
        data = json.loads(config.read_text(encoding="utf-8"))
        write_tools.update(data.get("writeTools", []))
    for blueprint in (PACK / ".claude/skills").glob("*/blueprint.yaml"):
        text = blueprint.read_text(encoding="utf-8")
        bound = set(re.findall(r"doddle\.tool\.v1\.[\w-]+\.[\w-]+", text))
        risky = bound & write_tools
        if risky:
            assert "type: gate" in text, (
                f"{blueprint} binds write-capable tool(s) {sorted(risky)} without an approval gate"
            )


def test_cli_tool_nodes_only_use_registered_clis():
    """CLI tool nodes must reference a CLI that exists in the central CLI registry."""
    cli_registry = PACK.parent / "doddle-core" / "registry" / "cli"
    known = {p.stem for p in cli_registry.glob("*.json")}
    assert known, "no CLI registry entries found"
    for blueprint in (PACK / ".claude/skills").glob("*/blueprint.yaml"):
        text = blueprint.read_text(encoding="utf-8")
        for cli in set(re.findall(r"doddle\.tool\.cli\.([\w-]+)", text)):
            assert cli in known, f"{blueprint} references unregistered CLI '{cli}'"


def test_manifests_parse():
    for name in ("package.json", "marketplace.json", ".claude-plugin/plugin.json"):
        json.loads((PACK / name).read_text(encoding="utf-8"))


def test_drev_runs_version():
    out = subprocess.run([sys.executable, str(PACK / "scripts" / "drev"), "version"],
                         capture_output=True, text=True, check=True)
    data = json.loads(out.stdout)
    assert data["toolkit_version"] == "1.0.0"
    assert data["scoring_version"] == "revops-1"
