# Scoring Methodology

How `dseo` turns evidence into numbers. Skills explain these; they never recompute them.

Versions: `scoring_version` (weights/thresholds) and `data_version` (crawler registry).
Both are printed in every envelope. If either changes, scores are not comparable across runs.

## Single page (`dseo score`, `dseo citability`)

Composite = **citability**, 100 points across 7 signals. Missing (not-applicable) signals are
excluded and the composite is normalised over the measured maximum.

| Signal | Max | Class | Question |
|--------|-----|-------|----------|
| `citability.self_containment` | 25 | heuristic | Do passages stand alone (no dangling "this/it")? |
| `citability.answer_first` | 20 | heuristic | Does each section lead with its answer? |
| `citability.structure` | 15 | heuristic | Headings, question headings, lists/tables? |
| `citability.evidence_density` | 15 | heuristic | Facts/numbers/citations per passage? |
| `citability.extractability` | 15 | heuristic | Server-rendered text-to-HTML ratio; not JS-gated? |
| `citability.attribution` | 5 | deterministic | Byline, dates, Article schema, canonical? |
| `citability.freshness` | 5 | deterministic | How recently updated? |

Tier bands: `Excellent ≥85`, `Good ≥70`, `Fair ≥55`, `Weak ≥40`, `Critical <40`.

## Site (`dseo audit`, `dseo report`)

Composite = weighted mean of category scores over the pages that scored.

| Category | Weight | Built from |
|----------|--------|-----------|
| citability | 0.40 | mean per-page citability |
| technical | 0.30 | indexability, title, meta, canonical, viewport, H1, HTTPS, alt, length |
| schema | 0.15 | JSON-LD presence, validity, sameAs, `@id` |
| content | 0.15 | structure, evidence density, attribution, freshness |

## Rules

1. A score is a pure function of the recorded page bytes. Same input → same bytes out
   (modulo `generated_at`), guarded by a determinism test.
2. `null` never counts as zero. It leaves the denominator.
3. Findings carry `points_lost` — what the fix recovers on the 100-point category scale,
   before weighting. They are pre-ranked by severity, then effort, then points.
4. Machine-readable authorship, entity markup, and crawler access rank differently by site
   kind (publisher vs docs vs commerce). The scorer is kind-agnostic; the model supplies kind
   from `jsonld_types`, URL shapes, and visible dating, and says what it concluded.

## Not in scope of the score

Brand/entity presence, live AI-citation share, and search rankings require third-party data.
They are advisory or `live`, and never folded into the deterministic composite.
