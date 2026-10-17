# llms.txt format and adoption status

Reference for `geo-llmstxt`. Read when validating a file or writing a draft.

## Format

- **H1**: the project / site name (required).
- **Blockquote** (`>`) immediately after: a one-paragraph summary (optional, recommended).
- **H2 sections**, each followed by link lines: `- [Title](url): optional note`.
- Links that appear before any H2 land under `(uncategorised)`.

Example:

```
# Acme Docs

> Acme builds observability tooling for serverless teams.

## Guides
- [Quickstart](https://acme.example/quickstart): install and first trace in 5 minutes

## Reference
- [Pricing](https://acme.example/pricing): plans and limits
```

Validation errors the toolkit emits:

- `empty or missing llms.txt`
- `missing H1 project name`
- `no link lines found`

The envelope reports `sections`, `links`, `name`, and `summary_present` so you can describe
the file without re-parsing it.

## Adoption status — be honest

llms.txt was proposed as a community convention. Engine support is partial and unproven: no
major AI engine has committed publicly to consuming it, and behaviour can change without
notice. It is a low-cost, machine-readable surface that may help tools and agents understand a
site. It is **not** a ranking factor. State this in any report, assert no effect the evidence
does not support, and verify current support before claiming engine behaviour. Do not embed
dated third-party market figures; if a source is needed, cite it with a date and mark it
advisory.

## When it is worth doing

- The site has a stable set of canonical pages worth pointing at (docs, product, pricing).
- The team wants a single curated index rather than relying on the crawl alone.
- There is a place to keep it fresh; a stale map is worse than none.
