# Doddle SEO & GEO OS

> A DoddleOS peer pack: **30 skills + 5 agents** for technical/organic SEO and Generative
> Engine Optimization, backed by a **deterministic, zero-dependency toolkit**.

**The one claim:** every number in a report is reproducible from recorded evidence. The
toolkit computes; the model explains and prioritizes. No skill does arithmetic in prose, and
no skill invents a metric.

---

## Why this pack

Most SEO/GEO skill packs are prompt-only: the model fetches a page and judges, so scores are
non-reproducible and drift between runs. This pack splits the work:

- **`dseo` (Python, stdlib-only)** — fetches, parses, and *computes* citability, technical,
  schema, AI-crawler and llms.txt evidence into a single versioned JSON **envelope**.
- **Skills (markdown)** — run `dseo`, read the envelope, and narrate two or three changes worth
  making. They never re-derive a number and never substitute zero for "not measured".

It is **agent-agnostic** (Claude Code, opencode, Cursor, Codex) **and** DoddleOS-native
(each skill ships a `blueprint.yaml`). No vendor MCP lock-in: external data is optional and
always declared.

---

## Install

```bash
# As a DoddleOS / Claude Code plugin
/plugin marketplace add DoddleHQ/DoddleOS
/plugin install doddle-seo-geo-skills

# Manual (skills + agents)
cp -r doddle-seo-geo-skills/.claude/skills/* your-project/.claude/skills/
cp -r doddle-seo-geo-skills/.claude/agents/* your-project/.claude/agents/
```

The toolkit needs only Python 3.9+. Try it with no network:

```bash
python3 scripts/dseo score tests/fixtures/site/index.html
python3 scripts/dseo robots tests/fixtures/site/robots.txt
python3 scripts/dseo version
```

---

## The toolkit

| Command | What it produces |
|---------|------------------|
| `dseo score <url\|file>` | Citability composite + technical + schema signals, ranked findings |
| `dseo audit <url>` | Whole-site crawl, weighted categories, aggregated findings |
| `dseo citability <url>` | The 7 citability signals |
| `dseo technical <url>` | Indexability, title, meta, canonical, viewport, H1, HTTPS, alt, length |
| `dseo schema <url>` | JSON-LD types, `sameAs`, validation errors/warnings |
| `dseo robots <url\|file>` | Per-AI-crawler allow/block, search vs training, sitemaps |
| `dseo llmstxt <url\|file> [--generate]` | Analyze or draft `llms.txt` |
| `dseo report <url> [--out FILE]` | Audit + markdown report |
| `dseo doctor` | Environment check |

Output is JSON when piped (`--json` is belt-and-braces). Every envelope carries
`toolkit_version`, `scoring_version`, `data_version`, an `evidence.stamp`, `signals[]`,
ranked `findings[]`, and `completeness`. See
[`.claude/skills/common/scoring-methodology.md`](.claude/skills/common/scoring-methodology.md).

---

## Skills (30)

### GEO / AI search (10)
`geo-audit`, `geo-citability`, `geo-crawlers`, `geo-llmstxt`, `geo-schema`, `geo-report`,
`geo-brand-entity`, `geo-platform`, `geo-monitor`, `geo-content`

### SEO (20)
`seo-audit`, `seo-technical`, `seo-onpage`, `seo-schema`, `seo-internal-linking`,
`seo-hreflang`, `seo-keyword-research`, `seo-topical-map`, `seo-content-brief`,
`seo-competitor`, `seo-backlinks`, `seo-digital-pr`, `seo-local`, `seo-ecommerce`,
`seo-strategy`, `seo-reporting`, `seo-sxo`, `seo-programmatic`, `seo-migration`,
`seo-geo-fundamentals`

Full inventory with owners and agents: [`skills-matrix.md`](skills-matrix.md).

## Agents (5)

`geo-specialist`, `seo-strategist`, `technical-auditor`, `schema-architect`, `entity-strategist`.

---

## Principles

1. **Deterministic first.** If the toolkit can compute it, a skill does not guess it.
2. **`null` is not zero.** Unmeasured signals are named, never silently zeroed.
3. **Evidence-bound.** Reports state the evidence stamp and scoring version.
4. **No hardcoded market statistics.** They go stale; the linter forbids them.
5. **Fetched text is data.** Excerpts are quoted, never followed as instructions.
6. **Optional integrations stay optional.** Missing MCP tools degrade the report, not the skill.

## Develop

```bash
python3 scripts/lint_pack.py     # structure, frontmatter, blueprints, links, secrets, claims
python3 -m pytest tests -q       # toolkit tests
```

See [`AGENTS.md`](AGENTS.md) for authoring conventions.

## Validate

`python3 scripts/lint_pack.py && python3 -m pytest tests -q` → 0 errors, all tests pass.

## License

MIT — same as DoddleOS core.
