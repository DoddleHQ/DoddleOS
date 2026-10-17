# Programmatic quality gates

Depth for `seo-programmatic`. The gates are `advisory` rules; the evidence that a page fails
them comes from the `dseo` envelope. Set the thresholds with the user and record them, so the
gate is reproducible even though it is not computed by the toolkit.

## The uniqueness gate

Before scaling, sample pages and ask of each: *what does a user get here that no other page in
the set gives?* A passing page has at least:

- a substantive, unique value block (data, figures, comparison, availability) not derivable by
  swapping one token;
- content a reader would not immediately recognise as one of thousands of clones.

If most sampled pages fail, the bottleneck is the dataset, not the template. Fix the data first.

## The thin-content gate

Define a minimum of unique, substantive content per page, and a policy for weak records:

| Record state | Action |
|--------------|--------|
| Full data | Publish normally |
| Partial data | Publish with the missing section suppressed, not stubbed |
| Empty / degenerate data | Do not publish; suppress the URL or return 404/410 |

A page whose only content is a heading plus a template sentence is thin regardless of word
count. Use `signals[].detail.word_count` and the `content` category from `dseo audit` as
evidence, not as the whole verdict.

## The duplicate gate

Detect near-duplicates across the set and decide per set:

- **Differentiate** — add unique data until the pages are genuinely distinct.
- **Canonicalise** — point near-duplicates at the strongest representative, if consolidation is
  intended.
- **Consolidate** — merge into one page and redirect the rest.

Never let two generated URLs compete for the same intent.

## The indexation gate

Decide the index class of every page class *before* generation:

- **Index** — unique, useful pages; include in sitemaps and internal links.
- **Discover-only** — reachable but not sitemapped.
- **No index** — `noindex`; keep out of sitemaps and internal links so crawlers do not chase
  pages that cannot rank.

An index bloat problem is a decision made at generation time, not a clean-up afterwards.

## The shipping gate

1. Sample N URLs representing the set (`dseo audit --max-pages N`).
2. Score against the gates above.
3. Publish only if the sample passes; state N and that it is a sample.
4. Re-check after launch, and monitor index coverage per template with `seo-reporting`.

## Kill criteria

State up front what would stop the rollout: e.g. the sample fails the uniqueness gate, or the
`content` category does not clear the agreed floor. Naming kill criteria before shipping is what
makes the gate real.
