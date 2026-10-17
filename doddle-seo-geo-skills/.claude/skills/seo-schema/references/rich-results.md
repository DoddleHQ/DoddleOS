# Rich-result types and properties

Reference for `seo-schema`. Read when deciding which type a page should carry and which
properties the toolkit will flag. The required/recommended lists below mirror what `dseo schema`
checks; they are a minimal subset, not the full schema.org or Google eligibility spec.

## Type → rich result → required properties

| `@type` | Rich result it supports | Required (checked) | Recommended (checked) |
|---------|------------------------|--------------------|-----------------------|
| `Article` / `NewsArticle` / `BlogPosting` | Article rich result | `headline`, `author`, `datePublished` | `dateModified`, `image`, `publisher` |
| `Product` | Product rich result | `name`, `offers` | `aggregateRating`, `review`, `image` |
| `Offer` | Price in the product result | `price`, `priceCurrency` | — |
| `FAQPage` | FAQ rich result | `mainEntity` | — |
| `Question` | A FAQ entry | `name`, `acceptedAnswer` | — |
| `HowTo` | How-to rich result | `name`, `step` | — |
| `BreadcrumbList` | Breadcrumb trail | `itemListElement` | — |
| `Review` / `AggregateRating` | Review stars (via `Product`) | nested under `Product` | flagged as `Product` warnings if absent |
| `Organization` | Logo / knowledge panel | `name`, `url` | `logo`, `sameAs`, `description` |
| `WebSite` | Sitelinks search box | `url` | — |
| `WebPage` | Page entity | `url` | — |
| `LocalBusiness` | Local result | `name`, `address` | — |
| `Event` | Event result | `name`, `startDate`, `location` | — |
| `Recipe` | Recipe result | `name`, `recipeIngredient`, `recipeInstructions` | — |
| `VideoObject` | Video result | `name`, `thumbnailUrl`, `uploadDate` | — |
| `SoftwareApplication` | App result | `name`, `applicationCategory`, `operatingSystem` | — |
| `Person` | Author entity | `name` | — |

`Product`'s recommended list includes `aggregateRating` and `review`; when they are absent the
envelope emits a **warning** for `Product`, which is where review-star markup surfaces.

## How to choose the type

1. Match the type to what the page *is*, not what you wish it were. A blog post is an
   `Article`, not a `Product`.
2. One primary entity per page; nest the rest (`author` as `Person`, `offers` as `Offer`,
   `mainEntity` as `Question`).
3. Prefer the most specific applicable subtype (`NewsArticle` over `Article` for news).
4. Add `BreadcrumbList` alongside the primary type; it is additive, not exclusive.

## Two warnings that override everything

1. **Markup must match visible content.** Every marked-up property must be visible on the page.
   Hidden or invented values violate structured-data policy. The toolkit cannot see the rendered
   page, so this is always a manual confirmation.
2. **Valid ≠ guaranteed display.** Passing the required-property checks means the markup is
   well-formed and complete enough to be eligible. Whether a rich result actually appears depends
   on the search engine's systems. Never promise a rich result.

## Reading `errors` vs `warnings`

- `schema.errors[]` — a **required** property is missing for that node's type. Fix these.
- `schema.warnings[]` — a **recommended** property is missing. Add them for a stronger result,
  but they do not block validity.

Invalid JSON in a JSON-LD block is also reported under `errors` (`invalid JSON: …`) so a
malformed block is never silently ignored.
