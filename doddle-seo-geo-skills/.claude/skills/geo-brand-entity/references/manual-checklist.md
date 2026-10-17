# Entity authority manual checklist

Everything here is a **manual check**. It is not computed by `dseo` and must never be reported
as a measured result or a fabricated count. Record each item as one of:
`confirmed present`, `confirmed absent`, or `not checked`.

Only `schema.same_as`, `schema.same_as_count`, `schema.knows_about`, the entity `@id`s, and
`schema.errors[]` / `schema.warnings[]` come from the deterministic envelope.

## Controllable (the site owner can change these today)

| Check | What to look for | Status |
|-------|------------------|--------|
| `Organization` node exists | A typed entity node, not just `WebSite` | not checked |
| Consistent brand name | `<title>`, `Organization.name`, footer, and profiles match exactly | not checked |
| `url` and `logo` on the node | Point to the canonical domain and a fetchable logo | not checked |
| Stable `@id` | One `@id` reused across pages and `@graph` references | not checked |
| `sameAs` links | One entry per authoritative profile that already exists | not checked |
| `knowsAbout` topics | Topical statements consistent with real expertise | not checked |
| `ContactPoint` / address | Real, matching the site's contact page | not checked |

## Earned (independent coverage — cannot be created to order)

For each, check whether an entry/page already exists and note the exact URL. Do not create or
edit the community content yourself, and never promise an outcome.

| Source | What to check | Why it matters | Status |
|--------|---------------|----------------|--------|
| Wikipedia | Does an article exist? Is the name exactly right? | Strong corroboration **if** independently notable | not checked |
| Wikidata | Is there a QID? Are `official website` / `sameAs` values populated? | Machine-readable identity | not checked |
| LinkedIn company page | Exists, name/URL match the site | Directory corroboration | not checked |
| Crunchbase | Company profile present and current | Directory corroboration | not checked |
| Reddit | Do threads mention/recommend the brand unprompted? | Reflects real usage, not a lever | not checked |
| YouTube | Reviews, demos, or explainers from third parties | Earned coverage | not checked |
| Press / news | Independent articles naming the brand | Earned authority | not checked |
| Review sites | Verified profiles with real reviews | Earned trust signals | not checked |

## Honest framing to give the user

- **Controllable:** the entity node, consistent naming, `sameAs`, stable `@id`. Fix these first
  and they are fully reproducible.
- **Earned:** Wikipedia/Wikidata, community threads, third-party video, press. These follow
  independent coverage and real usage. State that they cannot be manufactured, and that paid or
  astroturfed attempts are out of scope and usually counter-productive.
