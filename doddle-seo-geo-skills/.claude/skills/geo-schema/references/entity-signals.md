# Entity signals for GEO

Reference for `geo-schema`. Read when explaining why an entity fix matters or drafting a
JSON-LD graph.

## Why entity understanding, not rich results

Rich results are a Google/Bing presentation feature. AI engines instead need to *resolve* an
entity: which organization is this, is it the same one across pages, what does it know, who
authored this page. The signals below serve resolution.

## The signals

| Signal | Where | What it enables |
|--------|-------|-----------------|
| stable `@id` | on every node | one entity, referenced consistently across pages |
| `Organization.name` / `.url` | Organization | the canonical brand identity |
| `sameAs` | Organization / Person | authoritative profiles (Wikipedia, LinkedIn, official) that confirm identity |
| `knowsAbout` | Organization / Person | topics the entity is authoritative on |
| `author` | Article / BlogPosting / NewsArticle | machine-readable authorship |
| `datePublished` / `dateModified` | Article | recency and provenance |
| `publisher` | Article | ties the article back to the organization |

## Minimum entity graph

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Example",
  "url": "https://example.com",
  "sameAs": [
    "https://en.wikipedia.org/wiki/Example",
    "https://www.linkedin.com/company/example"
  ],
  "knowsAbout": ["observability", "serverless"]
}
```

Reference the same `@id` from an Article:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "https://example.com/guides/quickstart#article",
  "headline": "Quickstart",
  "author": {"@id": "https://example.com/authors/jane#person"},
  "datePublished": "2026-01-15",
  "dateModified": "2026-03-02",
  "publisher": {"@id": "https://example.com/#organization"}
}
```

## Boundaries

- The toolkit's required-property checks are minimal, not a full schema.org validator. Confirm
  details against schema.org before shipping.
- `Product`, `Offer`, `FAQPage`, `BreadcrumbList`, `HowTo`, `Recipe`, and `VideoObject` are
  rich-result types — route those to `seo-schema`.
- Never invent values (no fabricated `sameAs` URLs or dates). If the site cannot supply a
  value, leave it out and report the gap rather than guessing.
