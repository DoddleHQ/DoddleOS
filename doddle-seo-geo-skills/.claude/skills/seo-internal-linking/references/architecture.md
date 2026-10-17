# Internal link architecture

Reference for `seo-internal-linking`. Read when designing the hub-spoke model, deciding depth,
or setting an anchor policy. All of this is `advisory`: the toolkit measures reachability, not
link equity.

## What the deterministic run gives you

`dseo audit` follows internal links from the start page and reads sitemaps, up to `--max-pages`.
It returns:

- `evidence.pages_ok` — pages fetched and scored.
- `evidence.pages_failed[]` — pages attempted but not evaluable.
- `findings[].pages` — the pages behind each finding.

It does **not** return a link graph, inbound counts, click depth, or link-equity values. Any
depth/orphan/hub claim you make is your analysis of the discovered set and the sitemap, and must
be labelled `advisory`.

## Hub-and-spoke model

- **Hub** — a broad topic page (e.g. "Technical SEO"). It links *down* to every spoke and is
  linked *up* from the spokes.
- **Spoke** — a specific page (e.g. "Fixing noindex"). It links *up* to its hub and *across* to
  closely related spokes.
- **Rule of thumb** — every page should be reachable from a hub, and every hub from the primary
  navigation or the homepage. A page with no route from a hub is an orphan candidate.

```
Home / Nav
  └─ Hub A ── Spoke A1
  │        └─ Spoke A2
  └─ Hub B ── Spoke B1 ── (sibling link) ── Spoke B2
```

## Orphan detection (advisory)

An orphan is a page you intend to rank that no internal page links to (and that is not in the
crawl frontier). To find them:

1. Take the intended URL set (sitemap or the user's list).
2. Compare with what the crawl reached.
3. Anything intended but not reached, and not linked from a hub, is an orphan candidate.
4. Confirm by searching the source for an inbound `<a href>` to that URL.

The audit's `pages_failed` list is **not** the orphan list — those URLs were reached but could
not be evaluated.

## Depth

Click depth is the number of link hops from an entry point (home or a hub). Deep pages are
crawled less often and are harder for readers to find. Reduce depth by:

- Linking the most important deep pages directly from a hub.
- Adding "related" cross-links between spokes at the same depth.
- Avoiding link chains where each page links only to the next.

Since depth is not in the envelope, state your method and call the result an estimate.

## Anchor strategy

| Good | Why |
|------|-----|
| Descriptive, names the destination ("hreflang return tags") | Reader and crawler both learn the topic |
| Varied across links to the same page | Avoids a single repeated exact-match pattern |
| Contextual, inside a sentence | More meaningful than a footer link farm |

| Bad | Why |
|-----|-----|
| "click here", "read more" | No topical information |
| The same exact-match anchor on every link | Reads as manipulation |
| Links buried in boilerplate/footer only | Weak editorial signal |

## Ordering the fixes

1. Indexability (a page that is `noindex` cannot benefit from links).
2. Orphans (a page nobody links to is hard to discover).
3. Depth (shortcut the pages that matter).
4. Anchors (polish, only after the structure is right).
