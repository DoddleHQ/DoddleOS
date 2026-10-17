# Intent classification and SERP clustering

Reference for `seo-keyword-research`. Read when the user asks how an intent or a cluster was
decided, or disputes a grouping. Everything here is `advisory`: it is a documented rule of
thumb, not a deterministic measurement.

## Intent classes

| Intent | Signal you look for | Typical format that wins |
|--------|---------------------|--------------------------|
| Informational | How/why/what phrasing; guides, definitions, and long-form results fill the SERP | Guide, explainer, tutorial |
| Commercial | "best", "top", "review", "compare"; listicles and comparison tables rank | Roundup, comparison, review |
| Transactional | "buy", "price", "pricing", "demo", "download"; product and pricing pages rank | Product, pricing, signup |
| Navigational | Brand or product name; the brand's own pages own the SERP | Homepage, login, brand page |

The SERP is the evidence: classify by the dominant result *format*, not only by the keyword's
wording. A keyword can mix intents; if it does, split it into two clusters rather than averaging.

## Clustering by SERP overlap

Two keywords belong in the same cluster when they return **the same ranking URLs**. Overlap is
measured by comparing result sets, not by string similarity:

- High overlap (most of the top URLs shared) → one page should target both.
- Low overlap (different URLs) → different pages; do not merge.
- Partial overlap → same cluster only if the dominant format matches; note the split.

When `doddle.tool.v1.dataforseo.serp` is unavailable, you may fall back to lexical/semantic
similarity, but every cluster produced that way is `advisory` and must be labelled as not
SERP-validated.

## URL decision

| Decision | When | Risk if wrong |
|----------|------|---------------|
| `create` | No existing page covers the cluster's intent | Missing coverage |
| `optimise` | One existing page partially matches the intent | Under-targeted page |
| `consolidate` | Several existing pages compete for the same intent | Cannibalisation |

Never decide by keyword count. Decide by whether an existing URL already serves the intent;
hand the URL inventory to `seo-topical-map` when the picture is larger than one cluster.

## Provenance

Every metric in the output is `live` (from `doddle.tool.v1.semrush.domain`, or supplied by the
user). Intent, clustering, and the URL decision are `advisory`. Do not present an advisory
judgement with the authority of a measured number.
