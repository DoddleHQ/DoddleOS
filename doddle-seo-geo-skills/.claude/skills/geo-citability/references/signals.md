# Citability signal definitions

Reference for `geo-citability`. Read when explaining *why* a signal scored what it did.
Computed by `dseo`. Never re-derive these numbers.

A "candidate block" is a non-heading element (`p`, `li`, `blockquote`, `td`, …) with at least
8 words. Headings are structure, not passages.

| Signal | Max | Class | What it measures | How it's computed |
|--------|-----|-------|------------------|-------------------|
| `self_containment` | 25 | heuristic | Can a passage stand alone? | Share of candidate blocks that do **not** open with a dangling reference (`this`, `it`, `they`, `as mentioned`, `however`, `also`, …). `detail.worst_example` quotes the first offender. |
| `answer_first` | 20 | heuristic | Does each section lead with its answer? | Share of sections whose first sentence is ≤ 40 words and does not start with filler ("In this article…", "Welcome…"). |
| `structure` | 15 | heuristic | Is the page organised for extraction? | 4 pts headings ≥ 2; 3 pts exactly one H1; 4 pts any question-shaped heading; 4 pts a list or table. |
| `evidence_density` | 15 | heuristic | Are passages factual? | Share of candidate blocks containing a number, unit, year, currency, citation marker, or URL. |
| `extractability` | 15 | heuristic | Is text present without JS? | `text_chars / html_chars` scaled to a 0.15 target. If the page has < 50 words, the signal is **not applicable** (`skipped_reason`). |
| `attribution` | 5 | deterministic | Can the source be trusted? | 1.25 pts each for byline, a date, `Article` schema, and a canonical. |
| `freshness` | 5 | deterministic | Is it current? | From modified/published date: ≤180d = 5, ≤365d = 4, ≤730d = 2.5, older = 1, none = 0. |

## Composite

`composite = sum(value) / sum(max over measured signals) * 100`. Not-applicable signals leave
the denominator. Tiers: `Excellent ≥85`, `Good ≥70`, `Fair ≥55`, `Weak ≥40`, `Critical <40`.

## Why provenance matters

`self_containment`, `answer_first`, `structure`, `evidence_density` and `extractability` are
**heuristic**: they encode a documented rule of thumb. Report their `class` so the reader knows
which numbers are exact and which are rules. `attribution` and `freshness` are deterministic.

## Thresholds are versioned

Thresholds live with `scoring_version`. If it changes, a score is not comparable to an older
one; say so rather than comparing across versions.
