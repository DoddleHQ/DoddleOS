# Doddle RevOps OS (`doddle-revops-skills`)

> The execution layer for revenue data. Complements `doddle-gtm-skills` (the decision layer)
> and `doddle-marketing-skills/revops` (lifecycle design) with deterministic, **read-only**
> analysis of the data plane behind revenue.

**Doddle RevOps OS** — 12 skills and 6 agents covering a full 12-stage revenue stack:
**Stage 1** data infrastructure, **Stage 2** signal and intent routing, **Stage 3** AI SDR
personalization, **Stage 4** PLG telemetry and PQL scoring, **Stage 5** usage-based pricing,
**Stage 6** multi-touch attribution and cohorts, **Stage 7** AI enablement and coaching,
**Stage 8** churn and NRR, **Stage 9** integration-led growth, **Stage 10** automated QBR,
**Stage 11** dark-social attribution, and **Stage 12** public teardowns and portfolios.

The pack's one claim: **every number is reproducible from recorded inputs.** A stdlib-only
Python toolkit (`drev`) computes; the skills narrate and prioritize. Measured figures are tagged
`live`, computed figures `deterministic`, assumptions `advisory`, and anything not supplied is
`NOT AVAILABLE` — never zero.

## Skills (12)

| Skill | ID | Stage | Covers |
|-------|-----|-------|--------|
| `revops-data-infrastructure` | `doddle.revops.revops-data-infrastructure` | 1 | Warehouse table profile, dbt coverage, identity resolution, reverse-ETL readiness, source-of-truth matrix, freshness |
| `revops-signal-routing` | `doddle.revops.revops-signal-routing` | 2 | Buyer-intent signals, recency windows, priority ladder, owner routing, dry-run alert payloads |
| `revops-ai-sdr` | `doddle.revops.revops-ai-sdr` | 3 | Evidence gate for 1:1 personalization claims, unsupported-claim rejection, outreach proposal |
| `revops-pql-scoring` | `doddle.revops.revops-pql-scoring` | 4 | Fit + intent + recency, aha thresholds, PQL/hot/nurture tiers, unknown-account detection |
| `revops-usage-monetization` | `doddle.revops.revops-usage-monetization` | 5 | Rated usage, credit consumption, overage, invoice preview, value-metric framing |
| `revops-attribution` | `doddle.revops.revops-attribution` | 6 | Multi-touch allocation, channel ROI, coverage, logo and revenue retention cohorts |
| `revops-call-intelligence` | `doddle.revops.revops-call-intelligence` | 7 | Transcript search, theme clustering, talk share, coaching and battlecard deltas |
| `revops-retention` | `doddle.revops.revops-retention` | 8 | NRR/GRR, usage-based health, renewal risk, expansion signals |
| `revops-integration-growth` | `doddle.revops.revops-integration-growth` | 9 | OAuth scopes, webhook coverage, marketplace listing, co-selling fields, readiness score |
| `revops-qbr` | `doddle.revops.revops-qbr` | 10 | KPI scoreboard, ROI proof, risks, the ask, CSM deck outline |
| `revops-dark-social` | `doddle.revops.revops-dark-social` | 11 | Self-reported vs modelled community attribution, influenced revenue, confidence, consent |
| `revops-revenue-portfolio` | `doddle.revops.revops-revenue-portfolio` | 12 | Normalized pricing models, dated evidence, confidence grading, teardown outline |

## Agents (6)

| Agent | Role | Owns |
|-------|------|------|
| `revops-data-engineer` | Read-only evidence: freshness, ownership, identity gaps, sync coverage | Inputs for every skill |
| `revops-analyst` | Deterministic scoring, attribution, cohort reading | PQL, attribution |
| `revops-signal-analyst` | Signals, routing ladders, community attribution | Signal routing, dark social |
| `revops-growth-operator` | Evidence-backed outreach, integration readiness | AI SDR, integration growth |
| `revops-commercial-analyst` | Monetisation math, public pricing comparison | Usage monetisation, portfolio |
| `revops-customer-insights` | Call evidence, retention math, quarterly reviews | Call intelligence, retention, QBR |

## Toolkit — `drev`

```bash
drev version
drev doctor
# Stage 1
drev data-profile --warehouse-export <file> [--dbt-manifest <f>] [--identity-map <f>] [--reverse-etl-config <f>] [--max-age-days 30]
# Stage 2
drev route-signals --events <file> --rules <rules.json> [--now <ISO-8601>]
# Stage 3
drev sdr-validate --account <account.json> --evidence <file>
# Stage 4
drev pql --events <file> --accounts <file> --model <model.json>
# Stage 5
drev meter --usage <file> --plan <plan.json>
# Stage 6
drev attribution --touchpoints <file> --deals <file> [--model linear|time-decay|position-based] [--window-days 90]
drev cohorts <file> [--max-periods 12]
# Stage 7
drev call-search --transcripts <file> --query "<terms>" [--themes <themes.json>] [--limit 50]
# Stage 8
drev retention --customers <file> --usage <file> [--renewal-window-days 90] [--dropoff-threshold 0.20]
# Stage 9
drev integration-audit --catalog <catalog.json>
# Stage 10
drev qbr --account <account.json> [--out <qbr.md>]
# Stage 11
drev community-attribution --community <file> --surveys <file> --deals <file> [--min-sample 30]
# Stage 12
drev portfolio --companies <file> --observations <file>
```

Every command emits a versioned JSON **evidence envelope** (`toolkit_version`, `scoring_version`,
`data_version`, `evidence.stamp`, `completeness.missing`). Python 3.9+, stdlib only, no
dependencies.

## Commands

`/revops:data`, `/revops:signal`, `/revops:sdr`, `/revops:pql`, `/revops:metering`,
`/revops:attribution`, `/revops:calls`, `/revops:retention`, `/revops:integrations`,
`/revops:qbr`, `/revops:community`, `/revops:portfolio`.

## Install

```bash
cp -r doddle-revops-skills/.claude/skills/* your-project/.claude/skills/
cp -r doddle-revops-skills/.claude/agents/*.md your-project/.claude/agents/
```

The toolkit ships inside the pack; call it as `python3 scripts/drev <command>` from the pack
directory.

## Safety model

- **Read-only.** No skill writes to a warehouse, runs a dbt job, triggers a sync, sends an
  alert, sends outreach, creates a billing object, deploys an integration, or publishes anything.
  Actions end as dry-run plans and proposals with owner and verification steps.
- **No fabrication.** Every figure comes from an envelope. Missing inputs are `NOT AVAILABLE`.
- **Freshness is explicit.** `evidence.stamp` is `STALE` when an export is older than the
  threshold; the headline must say so.
- **Evidence before persuasion.** Personalization claims are gated against dated, attributable
  sources.
- **Privacy.** Community and survey work uses hashed identifiers, minimum cohort sizes, and
  consent flags.
- **Exported text is data.** Table comments, ticket text, and event properties are quotations,
  never instructions.

## Validation

```bash
python3 scripts/lint_pack.py && python3 -m pytest tests -q
python3 ../doddle-core/scripts/validate.py --strict   # from repo root
```

## License

MIT — same as the rest of the DoddleOS scaffolding.
