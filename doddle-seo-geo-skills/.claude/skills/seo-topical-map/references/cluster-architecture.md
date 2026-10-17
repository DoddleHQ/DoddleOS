# Cluster architecture and cannibalisation

Reference for `seo-topical-map`. Read when designing the hub-spoke shape, ordering the build, or
deciding whether two pages compete. All `advisory`.

## The shape

- **Hub (pillar).** One page per head intent. Broad, links out to every spoke in its cluster.
- **Spoke.** One page per sub-intent. Links back to the hub; cross-links only to genuinely
  related spokes, never to every sibling.
- **Cluster boundary.** A cluster ends where the search intent changes. If two pages answer the
  same question, they are the same node, not two.

## Build order

1. Hub intent that is closest to existing authority.
2. Spokes whose parent hub already exists and ranks.
3. Adjacent clusters that reuse the same entities and links.
4. Distant clusters last.

Spokes published before the hub have no link target and inherit no authority. Sequence by
dependency, not by keyword volume.

## Cannibalisation rules

| Situation | Call | Reasoning to state |
|-----------|------|--------------------|
| Two URLs, same intent, same format | `consolidate` | One stronger URL beats two weak ones |
| Two URLs, same intent, different audience/format | `differentiate` | Make the distinction explicit in title and intro |
| Blog post matches a product page's intent | `retarget` or `consolidate` | Decide which URL should own the intent, then point others at it |
| Near-duplicate location pages | `consolidate` unless uniqueness is real | Thin duplicates dilute the set |

Cannibalisation is *observed* when two URLs appear for the same query (from
`doddle.tool.v1.gsc.query` or `doddle.tool.v1.dataforseo.serp`); otherwise it is *suspected* from
overlapping intent. Say which one you are reporting.

## Labelling provenance

The architectural calls are `advisory`. Any keyword, ranking, or URL count drawn from the user or
an MCP tool is `live`. Never present an advisory hub choice as if the data had chosen it.
