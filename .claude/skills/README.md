# Moved: Doddle Marketing OS pack

Marketing skills moved to `doddle-marketing-skills/.claude/skills/` as an independent peer pack (61 skills, `doddle.marketing.*` v1.6.0). The skills are here in this same repo, one directory up from root: every peer pack lives at the repo top level under `doddle-*/`.

- Registry: `doddle-core/registry/packs.json` (18 peer packs; pack table in `README.md`)
- Validator discovers `doddle-*/.claude/skills/*/` — no hardcoded paths
- If you cloned the pre-v2 layout, install from the pack dir instead:
  `cp -r doddle-marketing-skills/.claude/skills/* your-project/.claude/skills/`
  `cp -r doddle-marketing-skills/.claude/agents/* your-project/.claude/agents/`
- This dir intentionally empty — kept only as a redirect for the old install path (DoddleOS v2 peer model)
