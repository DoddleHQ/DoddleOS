# Backlink profile health, anchors & prospecting

Deeper guidance for `seo-backlinks`. Every number here comes from
`doddle.tool.v1.ahrefs.backlinks`; nothing in this file is a threshold the toolkit computes.
Interpretation is `advisory`.

## Reading a profile

Judge a profile on four axes, all from the live response:

1. **Scale** — referring domains (distinct sites), not raw backlink count. One site linking
   fifty times is one relationship, not fifty.
2. **Relevance** — are the referring domains in the same language, market, and topic as the
   target? Off-topic links do little.
3. **Concentration** — what share of domains come from a handful of sources? High concentration
   is fragile: one link removal can move the profile.
4. **Direction** — new vs lost referring domains over the reported window. Name the window; an
   unstated window is not a finding.

## Anchor taxonomy

Classify the anchor text the tool returns into these buckets:

| Bucket | Example | Note |
|--------|---------|------|
| Branded | "Acme", "Acme Analytics" | Natural; the backbone of a healthy profile |
| Naked URL | "acme.com", "https://acme.com/pricing" | Natural |
| Generic | "click here", "read more", "this article" | Natural; carries little signal |
| Partial-match | "enterprise analytics platform" | Healthy in moderation |
| Exact-match | "enterprise analytics platform" (the head term verbatim) | Heavy concentration is an over-optimisation risk |
| Image / empty | `alt` text or no anchor | Note separately |

Report the distribution as `live`; flag exact-match over-concentration as `advisory`. If the tool
does not expose anchor text, say so — do not infer it.

## Toxicity proxies

Some tools return a link-quality or "toxicity" proxy, some do not, and the scales differ between
vendors. Treat any such field as a **signal to investigate**, never a verdict:

- Report the field under the vendor's own name and scale.
- Never convert one vendor's proxy into another's.
- A high-toxicity link is not automatically disavowed; only act on a clear, manual review, and
  note that disavow is an expert action.

## Prospecting rubric

For each on-site target (from `dseo audit`), shortlist link targets on:

- **Relevance** — would this site plausibly link to this topic?
- **Editorial** — is placement editorial (in-content) rather than a footer/directory/comment?
- **Reach** — only use tool-verified metrics; never a guessed DR/DA.
- **Feasibility** — is there a real reason for the link (data, reference, resource)?

Volume is not a goal. Ten relevant editorial links beat a thousand directory listings. Hand the
shortlist and the asset idea to `seo-digital-pr` to run outreach.
