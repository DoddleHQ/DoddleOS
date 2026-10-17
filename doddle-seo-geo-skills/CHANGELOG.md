# Changelog

All notable changes to `doddle-seo-geo-skills` are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/); versioning follows
[Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-10-18

First release. Doddle SEO & GEO OS — a DoddleOS peer pack.

### Added

- **Deterministic toolkit** (`scripts/doddle_seo/`, stdlib-only, Python 3.9+, CLI `dseo`):
  - `fetch` (HTTPS-only, SSRF guard, gzip/deflate, local files), `htmlparse` (stdlib
    `html.parser`), `citability` (7 signals), `robots` + a 27-entry AI-crawler registry,
    `llmstxt` (parse/validate/generate), `schema` (JSON-LD validation + entity signals),
    `scoring` (technical + citability + findings), `audit` (site crawl + weighted
    categories), `report` (markdown), versioned `envelope`.
  - Commands: `score`, `audit`, `citability`, `technical`, `schema`, `robots`, `llmstxt`,
    `report`, `version`, `doctor`.
- **30 skills** (`.claude/skills/`), a hybrid of agent-agnostic `SKILL.md` and DoddleOS
  `blueprint.yaml`:
  - GEO (10): `geo-audit`, `geo-citability`, `geo-crawlers`, `geo-llmstxt`, `geo-schema`,
    `geo-report`, `geo-brand-entity`, `geo-platform`, `geo-monitor`, `geo-content`
  - SEO (20): `seo-audit`, `seo-technical`, `seo-onpage`, `seo-schema`,
    `seo-internal-linking`, `seo-hreflang`, `seo-keyword-research`, `seo-topical-map`,
    `seo-content-brief`, `seo-competitor`, `seo-backlinks`, `seo-digital-pr`, `seo-local`,
    `seo-ecommerce`, `seo-strategy`, `seo-reporting`, `seo-sxo`, `seo-programmatic`,
    `seo-migration`, `seo-geo-fundamentals`
- **5 agents** (`.claude/agents/`): `geo-specialist`, `seo-strategist`, `technical-auditor`,
  `schema-architect`, `entity-strategist`.
- **Shared references** (`.claude/skills/common/`): `response-contract.md`,
  `data-reliability.md`, `fundamentals.md`, `scoring-methodology.md`,
  `mcp-integration-guide.md`.
- **Manifests**: `plugin.json`, `marketplace.json`, `package.json`.
- **Validation**: `scripts/lint_pack.py` and 29 tests (`tests/`), plus CI.
- **Docs**: `README.md`, `skills-matrix.md`, `AGENTS.md`.

### Principles

- Deterministic first: the toolkit computes, skills narrate.
- `null` means not measured, never zero.
- No hardcoded market statistics (linter-enforced).
- Fetched page text is data, never instructions.

[0.1.0]: https://github.com/DoddleHQ/doddle-seo-geo-skills/releases/tag/v0.1.0
