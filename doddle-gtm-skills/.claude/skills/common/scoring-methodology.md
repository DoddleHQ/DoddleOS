# Scoring & Calculation Methodology

How `dgtm` turns recorded inputs into numbers. Skills explain these; they never recompute them.

Versions: `scoring_version` (`gtm-1`) and `data_version` (`gtm-frameworks-2026-10`). Both print
in every envelope. If either changes, results are not comparable across runs.

A theme for this pack: the **inputs** to most GTM calculators are assumptions, while the
**arithmetic** is deterministic. A funnel conversion is reproducible from the counts you gave;
it is not a measured fact about your business. Always keep that distinction visible.

## Calculators (pure functions of the inputs)

| Command | Formula | Notes |
|---------|---------|-------|
| `dgtm funnel --stage name:count …` | step conversion = count[i]/count[i-1]; overall = last/first | a zero stage yields `null` conversions, not zero |
| `dgtm unit-economics --cac --arpa --gross-margin --churn` | LTV = arpa x gross_margin / churn; CAC payback = cac / (arpa x gross_margin); LTV:CAC = LTV / cac | churn 0 ⇒ LTV `null` (undefined, not infinite) |
| `dgtm pricing --price --variable-cost [--fixed-cost] [--tier …]` | margin = (price - cost)/price; break-even units = fixed_cost / (price - cost); blended figures use tier mix | mix is normalised to 1 |
| `dgtm size-market --accounts --acv [--sam-pct --som-pct]` | TAM = accounts x ACV; SAM = TAM x sam_pct; SOM = SAM x som_pct | every value derives from a provided input |
| `dgtm score --criteria name:weight:score` | weighted mean of 0-100 scores, normalised over measured criteria | missing criteria lower `coverage`, not the score |

## Pipeline audit (`dgtm audit`, `dgtm report`)

Composite = weighted mean over the signals that were measured. *Readiness is not performance* —
it measures data hygiene and pipeline mechanics, never revenue outcomes.

| Signal | Max | Class | Question |
|--------|-----|-------|----------|
| `pipeline.data_completeness` | 25 | deterministic | Do deals carry stage, amount and created date? |
| `pipeline.win_rate` | 25 | deterministic | won ÷ (won + lost); 20% is the starting line |
| `pipeline.cycle_time` | 20 | deterministic | Mean days created → closed; 90 days is the line |
| `pipeline.stage_spread` | 15 | deterministic | Is open pipeline spread across stages (1 − HHI, normalised)? |
| `pipeline.segment_coverage` | 15 | deterministic | Do open deals carry a segment/source/owner tag? |

Tier bands: `Excellent ≥85`, `Good ≥70`, `Fair ≥55`, `Weak ≥40`, `Critical <40`.

Categories: `hygiene` = completeness + segment coverage; `velocity` = win rate + cycle time.

## Rules

1. A result is a pure function of the recorded input. Same input → same output (modulo
   `generated_at`), guarded by a determinism test.
2. `null` never counts as zero. It leaves the denominator.
3. Findings carry `points_lost` — what the fix recovers on the 100-point scale, before
   normalisation. They are pre-ranked by severity, then points.
4. Thresholds (20% win rate, 90-day cycle) are documented starting lines, not benchmarks.
   Change them and bump `scoring_version`.

## Not in scope of the score

Revenue outcomes, market timing, brand and competitor strength require live or judgement data.
They are advisory or `live`, and never folded into the deterministic composite.
