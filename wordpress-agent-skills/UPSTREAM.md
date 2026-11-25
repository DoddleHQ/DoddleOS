# Upstream provenance and adaptations

## Source

- Repository: https://github.com/WordPress/agent-skills
- Imported commit: `7374e6f1c913b3b02b25465d266d9c0e0a04fc96`
- License: GPL-2.0-or-later
- Copyright: 2026 WordPress Contributors
- Compatibility contract: WordPress 7.0+, PHP 7.4.0+

The upstream README discloses AI-assisted generation and WordPress contributor
review. The disclosure is preserved in `docs/ai-authorship.md`.

## Imported unchanged in substance

- All 20 upstream skill directories, including `SKILL.md`, `references/`, and `scripts/`.
- All 52 upstream JSON eval scenarios plus their scenario README.
- Shared version/reference data and helper scripts.
- Principles, authoring guide, compatibility policy, and AI-authorship disclosure.
- The upstream GPL-2.0-or-later notice plus the full GPLv2 text in `COPYING`.

## DoddleOS adaptations

1. Added `id`, `version`, and `blueprint` frontmatter to every `SKILL.md`.
2. Added one `blueprint.yaml` per skill using agent/call/gate nodes.
3. Added `wordpress-surveyor`, `wordpress-engineer`, and `wordpress-reviewer` roles.
4. Added `approve_changes` gates to 14 write-class graphs.
5. Changed upstream repo-relative `skills/...` paths to `.claude/skills/...`.
6. Adapted shared helper scripts to discover `.claude/skills/`.
7. Added this pack's manifests, README, skills matrix, and full GPLv2 text in `COPYING`.
8. Normalized trailing EOF whitespace without changing upstream content.

No upstream procedure, reference, deterministic script, or eval scenario was removed.

## Sync policy

- Treat upstream WordPress documentation as canonical.
- Keep skill bodies short and procedural; put depth in `references/`.
- Add or update an eval scenario for every new or materially changed skill.
- Preserve `compatibility:` and the WP 7.0+ / PHP 7.4.0+ contract unless upstream changes it.
- Record the new upstream commit and adaptation diff when syncing.
