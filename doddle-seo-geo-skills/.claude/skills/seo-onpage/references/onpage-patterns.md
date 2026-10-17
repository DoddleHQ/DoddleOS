# On-page patterns

Reference for `seo-onpage`. Read when the user asks *how* to write the title, meta, headings,
or when a page is technically fine but still underperforms. Nothing here is a measured metric;
these are patterns, applied with judgement and tagged `advisory`.

## What is deterministic vs advisory

| Concern | Source | Class |
|---------|--------|-------|
| Title presence + `length` vs `15-65` | `technical.title.detail` | deterministic |
| Meta description presence + `length` vs `50-165` | `technical.meta_description.detail` | deterministic |
| Exactly one H1 | `technical.single_h1.detail.h1_count` | deterministic |
| Indexable / canonical / viewport | `technical.*` | deterministic |
| Intent match | SERP + judgement | advisory (needs `dataforseo.serp`) |
| Heading hierarchy (order, skips) | manual source read | advisory |
| Format the SERP rewards | SERP + judgement | advisory |

## Title patterns

- Lead with the entity the user searched, then the differentiator, then the brand: `Primary
  topic — qualifier | Brand`.
- Put the distinguishing word early; the tail is what gets truncated in a snippet.
- One page, one title. Do not template the brand onto every title if the topic already repeats.
- Keep to the toolkit's `15-65` character target. Longer is not "more keywords", it is a
  truncated title.

## Meta description patterns

- Write it as the answer's hook, not a keyword dump: state what the page helps the reader do.
- Include the primary term once, naturally, plus a reason to click (a number, a benefit, a
  concrete outcome).
- Keep to the toolkit's `50-165` character target. A missing description uses `tech.meta.missing`
  and is high severity in the envelope.

## Heading hierarchy

The envelope reports only `h1_count`. Verify the rest by reading the source:

- Exactly one H1 that states the page topic.
- H2s for each sub-question; H3s nested under the H2 they belong to. Do not skip levels
  (H2 → H4) — it signals a structural mistake to readers and parsers.
- Prefer question-shaped H2s when the SERP shows a People-Also-Ask block.

## Matching the format the SERP rewards

1. Pull the SERP for the target query and note the dominant result format (guide, list, table,
   comparison, product, FAQ, tool).
2. Compare with `citability.structure` and `answer_first` from `dseo score`:
   - No list/table but the SERP is list-dominated → the page format is the gap.
   - Sections bury the answer → `answer_first` will be low.
3. Recommend the format change first, wording second. A well-formatted page with plain prose
   beats a keyword-stuffed page in the wrong shape.

## Intent classification (advisory)

| Intent | Signals in the SERP | Page should be |
|--------|---------------------|----------------|
| Informational | Featured snippet, PAA, guides, "what is" | Explanatory, answer-first |
| Commercial | Reviews, comparisons, "best" | Comparison tables, pros/cons |
| Transactional | Product pages, prices, shopping | Product/offer detail, clear CTA |
| Navigational | Brand homepages, login pages | The specific destination |

State the intent you inferred and let the reader correct it; never present a guess as measured.
