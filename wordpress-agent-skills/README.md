# WordPress Agent Skills for DoddleOS

A standalone DoddleOS peer pack containing **20 WordPress skills**, adapted from
[WordPress/agent-skills](https://github.com/WordPress/agent-skills) at commit
`7374e6f1c913b3b02b25465d266d9c0e0a04fc96`.

Each skill preserves the upstream procedural `SKILL.md`, references, and deterministic
scripts, and adds a DoddleOS `blueprint.yaml`. Target baseline: **WordPress 7.0+,
PHP 7.4.0+**. The pack is LLM-agnostic: read the skill, then walk the graph.

## Install

```bash
# From the DoddleOS repository root
cp -r wordpress-agent-skills/.claude/skills/* your-project/.claude/skills/
cp -r wordpress-agent-skills/.claude/agents/*.md your-project/.claude/agents/
```

Or use the upstream-compatible pack builder:

```bash
cd wordpress-agent-skills
node shared/scripts/skillpack-build.mjs --clean
node shared/scripts/skillpack-install.mjs --dest=../your-wp-project --targets=claude,codex,vscode,cursor
```

## Prerequisites

- WordPress 7.0+ and PHP 7.4.0+ for target-project compatibility.
- Node.js 18+ for the bundled deterministic inspectors and pack builder.
- WP-CLI, Docker, Composer, PHPStan, Plugin Check, and Playground CLI only when the selected workflow requires them.
- `wpds` requires an externally configured WPDS MCP server; it is not bundled. If unavailable, the skill reports `⚠️ NOT AVAILABLE` instead of fabricating canonical documentation.

## Start here

1. `wordpress-router` classifies the repository and selects the workflow.
2. `wp-project-triage` emits deterministic project/tooling/version evidence.
3. The selected domain skill supplies the procedure and references.
4. Write-class graphs stop at `approve_changes`; read-only graphs do not.
5. `wordpress-reviewer` verifies with real commands and reports unavailable checks honestly.

## Skills

| Skill | ID | Covers | Approval gate |
|-------|----|--------|---------------|
| `wordpress-router` | `doddle.wordpress.wordpress-router` | Repo classification and workflow routing | — |
| `wp-project-triage` | `doddle.wordpress.wp-project-triage` | Deterministic project/tooling/version report | — |
| `wp-block-development` | `doddle.wordpress.wp-block-development` | `block.json`, attributes, rendering, deprecations, builds | `approve_changes` |
| `wp-block-themes` | `doddle.wordpress.wp-block-themes` | `theme.json`, templates, patterns, style variations | `approve_changes` |
| `wp-patterns` | `doddle.wordpress.wp-patterns` | Block patterns, registration, markup, a11y, i18n | `approve_changes` |
| `wp-plugin-development` | `doddle.wordpress.wp-plugin-development` | Hooks, settings, storage, security, release packaging | `approve_changes` |
| `wp-rest-api` | `doddle.wordpress.wp-rest-api` | Routes, schemas, auth, permissions, responses | `approve_changes` |
| `wp-interactivity-api` | `doddle.wordpress.wp-interactivity-api` | Directives, stores, state/actions, hydration | `approve_changes` |
| `wp-abilities-api` | `doddle.wordpress.wp-abilities-api` | Ability/category registration, REST exposure, permissions | `approve_changes` |
| `wp-ability-development` | `doddle.wordpress.wp-ability-development` | Ability schema and behavior design | `approve_changes` |
| `wp-abilities-audit` | `doddle.wordpress.wp-abilities-audit` | REST-surface audit and registration proposal | — |
| `wp-abilities-verify` | `doddle.wordpress.wp-abilities-verify` | Annotation/callback/schema/permission verification | `approve_changes` |
| `wp-wpcli-and-ops` | `doddle.wordpress.wp-wpcli-and-ops` | Guarded migrations, multisite, cron, automation | `approve_changes` |
| `wp-performance` | `doddle.wordpress.wp-performance` | Profiling, queries, caching, cron, HTTP, Server-Timing | — |
| `wp-phpstan` | `doddle.wordpress.wp-phpstan` | PHPStan config, baselines, WordPress typing | `approve_changes` |
| `wp-env` | `doddle.wordpress.wp-env` | Local `@wordpress/env` setup and troubleshooting | `approve_changes` |
| `wp-playground` | `doddle.wordpress.wp-playground` | Playground CLI, previews, mounts, snapshots, Xdebug | — |
| `blueprint` | `doddle.wordpress.blueprint` | Playground Blueprint JSON and bundles | `approve_changes` |
| `wp-plugin-directory-guidelines` | `doddle.wordpress.wp-plugin-directory-guidelines` | GPL, naming, trademarks, upsells, Plugin Check | — |
| `wpds` | `doddle.wordpress.wpds` | WordPress Design System components and tokens | `approve_changes` |

## Agents

| Agent | Role |
|-------|------|
| `wordpress-surveyor` | Read-only classification, tooling detection, and evidence collection |
| `wordpress-engineer` | Approved implementation using existing project tooling |
| `wordpress-reviewer` | Verification, security/compatibility review, and handoff evidence |

## Upstream standards retained

- Small, composable skills; depth stays in `references/`.
- Deterministic scripts for detection and inspection.
- `compatibility:` frontmatter targets WordPress 7.0+ / PHP 7.4.0+.
- Explicit procedure, verification, failure modes, and escalation.
- 52 JSON eval scenarios (plus their README) under `eval/scenarios/`.
- Upstream authoring, principles, compatibility, and AI-authorship docs under `docs/`.

See `UPSTREAM.md` for provenance and the exact DoddleOS adaptations.

## Validation

```bash
# From this pack directory
npm test
npm run lint

# Or directly
node shared/scripts/validate-skills.mjs
python3 ../doddle-core/scripts/validate.py --strict
```

## License and attribution

Copyright (C) 2026 WordPress Contributors. This pack is distributed under
**GPL-2.0-or-later**; see `LICENSE` and the full license text in `COPYING`. Upstream skill content was generated with AI
assistance and reviewed/edited by WordPress contributors, as disclosed in
`docs/ai-authorship.md` and the upstream README. DoddleOS adaptations are also
provided under GPL-2.0-or-later.
