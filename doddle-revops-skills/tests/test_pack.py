import json
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


def test_pack_is_read_only():
    """No skill blueprint may invoke a write-capable MCP tool."""
    for blueprint in (PACK / ".claude" / "skills").glob("*/blueprint.yaml"):
        text = blueprint.read_text(encoding="utf-8")
        assert "doddle.tool.v1." not in text, f"{blueprint} declares a live MCP tool"


def test_manifests_parse():
    for name in ("package.json", "marketplace.json", ".claude-plugin/plugin.json"):
        json.loads((PACK / name).read_text(encoding="utf-8"))


def test_drev_runs_version():
    out = subprocess.run([sys.executable, str(PACK / "scripts" / "drev"), "version"],
                         capture_output=True, text=True, check=True)
    data = json.loads(out.stdout)
    assert data["toolkit_version"] == "1.0.0"
    assert data["scoring_version"] == "revops-1"
