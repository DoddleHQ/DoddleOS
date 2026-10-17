# SERP feature taxonomy and snippet formats

Depth for `seo-sxo`. Features are query- and market-specific; only report the ones
`doddle.tool.v1.dataforseo.serp` returned for the target query. The format each feature rewards
is `advisory` guidance, not a measured result.

## Features and the format that wins them

| Feature | What it is | Page-side prerequisite | Format that wins it |
|---------|------------|------------------------|---------------------|
| Featured snippet | A highlighted answer above the results | `citability.answer_first` high; a self-contained answer | A concise definition or a short ordered/unordered list directly under a matching heading |
| People Also Ask | Expandable related questions | Question-shaped headings; a direct answer below each | One short answer per question, each self-contained |
| AI Overview | A synthesised answer with cited sources | Extractable, quotable passages; entity clarity | Answer-first sections, facts with units/dates/sources |
| Sitelinks | Sub-links under the main result | Clear site structure; descriptive anchor text | Strong internal linking and distinct section titles |
| Image / video pack | Visual results | Descriptive `alt`; captioned media | Accurate `alt` text and media markup |
| Knowledge panel | Entity card | Resolvable brand entity (`sameAs`) | Organization/Person schema and off-site corroboration |

The page-side prerequisites map to deterministic signals: `citability.structure`,
`citability.answer_first`, `citability.evidence_density`, and the `technical.*` tags. The
feature list itself is `live`; whether a page can win one is `advisory`.

## Snippet-ready structure

- Lead each section with the answer in one short sentence, then explain.
- Put a definition where a definition snippet could lift it; put steps in an ordered list;
  put comparisons in a table.
- Keep each candidate passage understandable on its own (no dangling "this"/"it").
- Include the units, dates, and named sources a snippet will keep.

## CTR work (the part `seo-onpage` defers)

Snippet readiness earns the *impression*; the title and meta earn the *click*. This skill owns
the CTR copy:

- The title should carry the promise the query is looking for, not just repeat the keyword.
- The meta description is ad copy: it sets the expectation the click must satisfy.
- Character targets come from `dseo technical` (`detail.target` for `technical.title` and
  `technical.meta_description`) — never invented pixel widths.
- If a query ranks top-five with a weak CTR, the snippet is the lever; if it ranks lower, fix
  the rank first.

## What is not deterministic

Feature presence, snippet ownership, and CTR deltas are `live` or `advisory`. The toolkit does
not report which competitor holds a snippet. Never claim a feature exists or was won without the
live SERP tool.
