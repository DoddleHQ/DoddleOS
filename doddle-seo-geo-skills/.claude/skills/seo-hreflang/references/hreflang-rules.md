# hreflang rules

Reference for `seo-hreflang`. Read when validating or building an hreflang cluster. These rules
are applied by judgement (`advisory`): the `technical` envelope does not expose hreflang values,
so every item below is confirmed against the page source or an alternate-set supplied by the
user.

## What the toolkit does and does not give you

| Item | Available? | Where |
|------|-----------|-------|
| Declared page language | yes | `technical.lang.detail.lang` |
| Canonical URL | yes | `technical.canonical.detail.canonical` |
| Indexability | yes | `technical.indexable.detail.noindex` |
| hreflang alternates | **no** | parser records them internally; not in `signals[]` — manual check |
| Reachable localized URLs | partial | `dseo audit` discovery |

## The cluster rules

1. **Self-referencing.** Every page in the cluster must include an hreflang tag pointing to
   itself. Omitting it is the most common error.
2. **Return tags (reciprocity).** If page A annotates a link to page B, page B must annotate a
   link back to A. A one-way annotation is discarded.
3. **x-default.** Exactly one URL per cluster should carry `hreflang="x-default"` — the page
   served when no language/region matches the user.
4. **Valid codes.**
   - Language: ISO 639-1 (`en`, `fr`, `de`).
   - Region: ISO 3166-1 alpha-2, uppercase (`en-GB`, `pt-BR`, `zh-Hans-CN`).
   - `en-UK` is invalid (region should be `GB`); a region without a language is invalid.
5. **Canonical + hreflang consistency.** Each language/region version should be
   self-canonicalising. Pointing every locale's canonical at the default version collapses the
   cluster and can remove the others from results. The canonical of a page must agree with its
   own hreflang entry.
6. **Absolute, indexable targets.** hreflang URLs must be absolute and must not be `noindex`
   or robots-blocked. A target that cannot be served cannot be matched.
7. **One method.** Do not mix `<link>` tags, HTTP headers, and XML sitemap annotations for the
   same cluster in conflicting ways; pick one and keep it consistent.

## Placement options

| Method | Where | Notes |
|--------|-------|-------|
| HTML `<link rel="alternate">` | `<head>` | Most common; fine for small clusters |
| HTTP `Link` header | Response headers | Useful for non-HTML files (PDFs) |
| XML sitemap `<xhtml:link>` | Sitemap | Scales well; keeps the `<head>` light |

## Verification workflow (advisory)

1. Take the intended locale set (the `locales` input or the user's list).
2. For each URL, read its hreflang annotations from the source.
3. Check self-reference, reciprocity across the whole set, and exactly one x-default.
4. Validate every code against ISO 639-1 / ISO 3166-1.
5. Confirm each target is absolute, indexable, and self-canonical.
6. Report which pages are missing which annotation, citing the source you read — not a number
   the toolkit did not produce.
