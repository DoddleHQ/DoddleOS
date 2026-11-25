# WordPress Agent Skills Matrix

## Routing and evidence

| Order | Skill | Purpose |
|-------|-------|---------|
| 1 | `wordpress-router` | Classify repo kind, tooling, version hints, and intended workflow |
| 2 | `wp-project-triage` | Emit deterministic JSON evidence with `detect_wp_project.mjs` |
| 3 | Domain skill | Follow the upstream procedure, references, and verification steps |

## Domain map

| Workflow | Skills | Typical verification |
|---------|--------|----------------------|
| Blocks and themes | `wp-block-development`, `wp-block-themes`, `wp-patterns` | `@wordpress/scripts` lint/test/build, block deprecation checks, theme validation |
| Plugins and security | `wp-plugin-development`, `wp-plugin-directory-guidelines` | PHPUnit, PHPCS, Plugin Check, GPL/header review |
| REST and abilities | `wp-rest-api`, `wp-abilities-api`, `wp-ability-development`, `wp-abilities-audit`, `wp-abilities-verify` | Schema checks, permission round-trips, runtime callback verification |
| Interactivity and UI | `wp-interactivity-api`, `wpds` | Build/tests, hydration checks, accessibility review |
| Operations | `wp-wpcli-and-ops`, `wp-env`, `wp-playground`, `blueprint` | Targeting/dry-run checks, backups, smoke tests, Blueprint validation |
| Quality and performance | `wp-performance`, `wp-phpstan` | Profiles, query evidence, PHPStan, before/after measurements |

## Safety classes

- **Read-only:** `wordpress-router`, `wp-project-triage`, `wp-abilities-audit`, `wp-performance`, `wp-plugin-directory-guidelines`, `wp-playground`.
- **Write-class:** all remaining skills. Their blueprints include `approve_changes` before execution.
- `wp-abilities-verify` is gated because runtime verification may invoke ability callbacks.
- WP-CLI and environment skills retain upstream guardrails; the graph gate does not replace dry runs, backups, environment confirmation, or multisite scoping.

## Dependency rule

Domain skills call `doddle.wordpress.wordpress-router` first. If the router is absent, stop and install the full pack; do not guess the workflow.
