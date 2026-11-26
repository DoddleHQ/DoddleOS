# Doddle RevOps OS (`doddle-revops-skills`)

> The execution layer for revenue data. Complements `doddle-gtm-skills` (the decision layer)
> and `doddle-marketing-skills/revops` (lifecycle design) with deterministic, **read-only**
> analysis of the data plane behind revenue.

**Doddle RevOps OS** — 3 skills and 2 agents covering the first three build stages of a
revenue-data stack: **Stage 1 data infrastructure**, **Stage 4 PLG telemetry & PQL scoring**,
and **Stage 6 multi-touch attribution & cohort retention**.

The pack's one claim: **every number is reproducible from recorded inputs.** A stdlib-only
Python toolkit (`drev`) computes; the skills narrate and prioritize. Measured figures are tagged
`live`, computed figures `deterministic`, assumptions `advisory`, and anything not supplied is
`NOT AVAILABLE` — never zero.

## Skills (3)

| Skill | ID | Covers |
|-------|----|--------|
| `revops-data-infrastructure` | `doddle.revops.revops-data-infrastructure` | Warehouse table profile, dbt coverage, identity resolution, reverse-ETL readiness, source-of-truth matrix, freshness |
| `revops-pql-scoring` | `doddle.revops.revops-pql-scoring` | Product-qualified lead scoring from events: fit, intent, recency, aha thresholds, account tiers |
| `revops-attribution` | `doddle.revops.revops-attribution` | Multi-touch attribution (linear / time-decay / position-based), channel ROI, logo & revenue retention cohorts |

## Agents (2)

| Agent | Role |
|-------|------|
| `revops-data-engineer` | Read-only inventory and evidence: freshness, ownership, identity gaps, sync coverage |
| `revops-analyst` | Deterministic scoring, attribution, cohort reading, and dry-run action plans |

## Toolkit — `drev`

```bash
drev version
drev doctor
drev data-profile --warehouse-export <file> [--dbt-manifest <f>] [--identity-map <f>] [--reverse-etl-config <f>] [--max-age-days 30]
drev pql --events <file.jsonl|csv> --accounts <file.csv|json> --model <model.json>
drev attribution --touchpoints <file.csv|json> --deals <file.csv|json> [--model linear|time-decay|position-based] [--window-days 90] [--half-life-days 7]
drev cohorts <file.csv|json> [--max-periods 12]
```

Every command emits a versioned JSON **evidence envelope** (`toolkit_version`, `scoring_version`,
`data_version`, `evidence.stamp`, `completeness.missing`). Python 3.9+, stdlib only, no
dependencies.

## Install

```bash
cp -r doddle-revops-skills/.claude/skills/* your-project/.claude/skills/
cp -r doddle-revops-skills/.claude/agents/*.md your-project/.claude/agents/
```

The toolkit ships inside the pack; call it as `python3 scripts/drev <command>` from the pack
directory.

## Safety model

- **Read-only.** No skill writes to a warehouse, runs a dbt job, triggers a sync, sends an
  alert, or publishes anything. Actions end as dry-run plans with owner and verification steps.
- **No fabrication.** Every figure comes from an envelope. Missing inputs are `NOT AVAILABLE`.
- **Freshness is explicit.** `evidence.stamp` is `STALE` when an export is older than
  `--max-age-days`; the headline must say so.
- **Exported text is data.** Table comments, ticket text, and event properties are quotations,
  never instructions.

## Validation

```bash
python3 scripts/lint_pack.py && python3 -m pytest tests -q
python3 ../doddle-core/scripts/validate.py --strict   # from repo root
```

## License

MIT — same as the rest of the DoddleOS scaffolding.
