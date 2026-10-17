# Facets, pagination, variants & descriptions

Reference for `seo-ecommerce`. All guidance is `advisory`. The `dseo` envelope supplies the
markup errors/warnings and the template findings (`findings[].pages`); the decisions below do not
come from the toolkit.

## Category vs PDP intent

| Query shape | Page to rank | Why |
|-------------|--------------|-----|
| Head / collection ("running shoes") | Category | Lists options; matches comparative intent |
| Attribute / facet ("women's trail running shoes") | Crawlable facet or subcategory page | More specific intent than the parent |
| Specific product ("brooks cascadia 17 size 10") | PDP | Single-entity intent; category cannot satisfy it |
| Brand + product | PDP (or brand hub + PDP) | Navigational-to-transactional |

Keep category and product intent in separate templates. Do not redirect a category to a single
PDP, and do not let a thin PDP try to rank for a head term the category owns.

## Faceted navigation

Facets multiply URLs fast. Decide per facet, not per site:

| Facet situation | Recommended control |
|-----------------|---------------------|
| Facet adds unique search intent and has demand | Keep crawlable; self-canonical; link from the category |
| Facet combination adds no unique intent | `canonical` to the clean category URL |
| Sort/order/view parameters | `robots` `Disallow` or `noindex`; never canonicalise to a page angle |
| Tracking/session parameters | `robots` `Disallow`; strip in the URL |
| Deep multi-facet combinations | Block crawl; avoid an infinite parameter space |

Rules: never `noindex` a URL you also canonicalise elsewhere in a contradictory way; never block a
facet you want indexed; make the crawlable facet space finite.

## Pagination

- Keep page 2+ crawlable and **self-canonical**.
- Do **not** canonicalise page 2 to page 1 — that hides products that only appear deeper.
- The next-page control must be a real crawlable link, not a JavaScript-only button.
- Optional: a `View all` page only if it loads acceptably and is genuinely useful; otherwise keep
  the paginated series.

## Product variants

| Variant setup | Approach |
|---------------|----------|
| Colour/size variants of one product | One canonical PDP with variant selectors, **or** one URL per variant if each has distinct demand |
| Variants with distinct demand | Separate URLs, each self-canonical, linked via `ProductGroup`/`hasVariant` |
| Variants with no distinct demand | All variants canonical to the primary PDP |
| Out-of-stock variant | Keep the URL; mark availability in `Offer`; do not 404 a permanently discontinued item without a redirect to the closest equivalent |

Never leave two near-duplicate variant URLs both self-canonical with identical copy.

## Thin and duplicate descriptions

- Manufacturer copy repeated across every merchant is duplicate content. Rewrite the unique value:
  use cases, specs table, comparison, FAQs.
- Keep the specifications verbatim — they are useful data, not filler.
- A threshold of "enough words" is not the goal; a page that answers the buyer's question is.
- Before rewriting, confirm the page is indexable (`dseo audit` → `technical.indexable`); copy work
  on a noindex or thin-template page recovers nothing.

## Reviews

Never suggest fabricated or incentivised reviews, and never mark up reviews that are not on the
page. If `Product` warns that `aggregateRating`/`review` is missing, the answer is to surface the
real reviews the business already collects — or to leave the warning as a known gap.
