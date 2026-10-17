# Per-engine reference

Deep detail for `geo-platform`. The right-hand column always points at a signal id that must
appear in *this run's* `dseo` envelope. Engine descriptions are **advisory** — they describe
typical behaviour and must be labelled as such, never as a measured fact.

## ChatGPT (Search)

- **Surfaces:** inline citations with links when Search mode is used; browsed pages for answers.
- **Favours:** server-rendered text it can fetch and lift whole passages from; clear attribution.
- **Deterministic checks:** `robots.crawlers[]` entry for ChatGPT's search crawler must be
  `allowed`; `citability.extractability`; `citability.self_containment`.
- **If blocked:** fix crawler access before any content change.

## Perplexity

- **Surfaces:** numbered citations for essentially every claim.
- **Favours:** factual, self-contained passages with named sources and numbers it can attribute.
- **Deterministic checks:** `citability.evidence_density`; `citability.self_containment`;
  `citability.answer_first`; the crawler entry for `PerplexityBot`.

## Google AI Overviews

- **Surfaces:** generated summaries above classic organic results.
- **Favours:** indexable, well-structured pages with clear question-and-answer shape and valid
  structured data.
- **Deterministic checks:** `technical.indexable` (no noindex); `schema.present`;
  `citability.answer_first`; `citability.structure`.

## Bing Copilot

- **Surfaces:** answers grounded in the Bing index, with citations.
- **Favours:** content already indexed by Bing; clean technical foundations.
- **Deterministic checks:** `robots.crawlers[]` for `bingbot` must be `allowed`;
  `technical.indexable`; `schema.present`.

## Claude (web)

- **Surfaces:** cited summaries drawn from pages it fetches.
- **Favours:** passages that stand alone and name who said them and when.
- **Deterministic checks:** `citability.extractability`; `citability.self_containment`;
  `citability.attribution`.

## Gemini

- **Surfaces:** grounded answers built from Google's index.
- **Favours:** indexable, well-structured pages with strong entity and structured-data signals.
- **Deterministic checks:** `technical.indexable`; `schema.types`;
  `citability.structure`; `citability.attribution`.

## How to keep this honest

1. Open the envelope and confirm each signal id above is present with a non-`null` value.
2. For any that is `null` or in `completeness.missing`, report it as not measured with the
   reason — not as a zero.
3. Tag every engine-behaviour statement `advisory`; tag every quoted signal `deterministic`.
4. Do not port numbers from a previous run; only the current envelope counts.
