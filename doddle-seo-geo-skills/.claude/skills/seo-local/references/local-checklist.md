# Local search checklist

Reference for `seo-local`. The `dseo schema` envelope only validates the required properties
(`LocalBusiness` → `name`, `address`). Everything below is `advisory`: confirm each item by hand
and record a status. Never assert a check you have not made.

## LocalBusiness markup

Author the node so the visible page and the markup agree:

| Property | Required by checker | Note |
|----------|---------------------|------|
| `name` | yes | Exactly the name used on GBP |
| `address` (`PostalAddress`) | yes | `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry` |
| `telephone` | no | Match the NAP phone exactly |
| `url` | no | The location page URL |
| `geo` (`GeoCoordinates`) | no | `latitude`, `longitude` |
| `openingHoursSpecification` | no | Days, opens, closes |
| `priceRange` | no | e.g. a tier symbol, not a market claim |
| `sameAs` | no | GBP, social, directory profiles |
| `areaServed` | no | For service-area businesses |
| `@type` | — | Use the most specific subtype (`Restaurant`, `Store`, …) |

Choice on `@type`: a specific subtype says more than the generic `LocalBusiness`. If no subtype
fits, use `LocalBusiness`.

## Google Business Profile

- Claim and verify the listing (owner access).
- Primary category = what the business is; secondary categories only where genuinely relevant.
- Complete hours, services, attributes, photos, and the description.
- Post updates; answer Q&A; respond to reviews.
- Keep the name, address, phone, and website identical to the site and directories.

## NAP consistency

NAP = Name, Address, Phone. The same string everywhere. Check at least:

- Site footer and contact page.
- Google Business Profile.
- Apple Maps, Bing Places, and the relevant local/industry directories.
- Data aggregators that feed other directories.

List the sources and mark each `consistent` / `mismatch` / `not checked`.

## Service-area pages

- One page per service × location, each with genuinely distinct content (staff, projects, local
  detail), not a template with the place name swapped.
- Unique title, H1, and body per page; local `LocalBusiness`/`Service` markup; internal links from
  a locations hub.
- **Doorway pages** — near-duplicate pages that differ only by location — are the failure mode.
  If two pages cannot offer unique value, consolidate them.

## Reviews

- Ask customers directly; make leaving a review easy.
- Respond to reviews, positive and negative.
- Never buy, incentivise, or write reviews. Reviews are earned and cannot be created to order.

## Local rank

Local-pack and map-grid positions are **not** in the envelope and no configured tool provides
them. Report them `⚠️ NOT AVAILABLE — no local-rank tool configured`; never estimate a position.
