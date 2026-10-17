# Content brief template

Reference for `seo-content-brief`. Copy this skeleton into the brief and fill every field. Mark
each field with its provenance: `live` (from `doddle.tool.v1.dataforseo.serp` or the user) or
`advisory` (judgement). Never leave a metric implied.

## Skeleton

```
# Brief: <working title>
Target keyword: <keyword>            [source]
Intent: <informational|commercial|transactional|navigational>   [advisory]
Audience / funnel stage: <...>       [source]
Format: <guide|comparison|product|FAQ|...>   [advisory from SERP]
Existing URL: <url or "new">         [source]

## Intent job
One sentence: what the reader must be able to do after reading.

## Outline
H1 <title>
  H2 <section>  → sub-intent served
    H3 <subsection>
  H2 <section>  → sub-intent served
  ...

## Entities to cover
- <entity>            [live|advisory]
- <entity>            [live|advisory]

## Questions to answer (answer-first)
- <question>          [live PAA | unverified]
- <question>          [live PAA | unverified]

## Internal links
- Up to hub: <url>    [source]
- Across to: <url>    [source]
- Canonical: <url>

## Schema
- <type> and the fields it requires   [advisory; validate with `dseo schema`]

## Success metric
- Metric: <...>  Tool: <doddle.tool.v1.gsc.query | doddle.tool.v1.ga4.getReport>
- Baseline: <value or "not yet measured">
```

## Rules

- One page per intent. If the outline needs two intents, it is two briefs.
- Every H2 earns its place by serving a sub-intent; cut sections that only mirror competitors.
- Answer-first questions: the first sentence answers, the rest explains.
- Do not state a numeric target without a measured baseline. "Not yet measured" is a valid value.
- If the SERP tool is unavailable, every question is marked unverified and the brief says so at
  the top.
