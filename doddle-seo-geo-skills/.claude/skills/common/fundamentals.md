# SEO & GEO Fundamentals (shared reference)

The concepts every skill assumes. Load this when you need to explain or orient, not on
every call.

## The two disciplines

- **SEO** optimises for ranked results in classic search: crawl → index → rank → click.
  The unit of value is the ranked page.
- **GEO** (a.k.a. AEO, LLM SEO) optimises for being *cited* inside an AI answer: retrieve →
  read → synthesise → cite. The unit of value is a **self-contained, quotable passage**.

They overlap heavily (crawlability, structure, authority, freshness) but differ in emphasis:
GEO weights extractability, self-containment, entity clarity, and machine-readable authorship
above link volume.

## How AI answers are built (mental model)

1. **Retrieval.** An engine's crawler/index (or a live fetch) retrieves candidate pages.
   If the crawler is blocked in `robots.txt`, the page is invisible here.
2. **Extraction.** The engine selects passages, not pages. Passages that depend on context
   ("This is why it matters") extract badly.
3. **Attribution.** The engine decides whether a source is safe to cite: who wrote it, when,
   and whether the entity resolves.
4. **Synthesis.** The answer is composed from one or more sources. Being *first* matters less
   than being *quotable* and *trusted*.

## Crawlers worth knowing

- **Search/answer crawlers** (blocking removes AI visibility): `OAI-SearchBot`,
  `PerplexityBot`, `Claude-SearchBot`, `YouBot`, `DuckAssistBot`, `bingBot`, `GoogleBot`.
- **Training crawlers** (blocking does not affect search): `GPTBot`, `ClaudeBot`,
  `Google-Extended`, `Applebot-Extended`, `CCBot`, `Bytespider`, `meta-externalagent`.
- **User-initiated fetches** (treat like a visitor): `ChatGPT-User`, `Claude-User`,
  `Perplexity-User`.

The authoritative list lives in the toolkit registry (`data_version`). Never hardcode it.

## E-E-A-T

Experience, Expertise, Authoritativeness, Trustworthiness. Signals: named authors with
credentials, original data, cited sources, visible published/updated dates, About/Contact
pages, and entity markup that ties the site to a real organization.

## Entity resolution

An engine answers about a *thing*, not a domain. A brand resolves when it has: a consistent
name, an Organization schema node with `url`/`logo`/`sameAs`, and corroboration elsewhere
(Wikipedia/Wikidata, LinkedIn, Crunchbase, review sites). `sameAs` is the one part entirely
in the site owner's control.

## Structured data that moves AI

`Organization` (with `sameAs`), `WebSite`, `Article` (author + dates), `Product`/`Offer`,
`FAQPage`, `BreadcrumbList`, `Person`. JSON-LD is preferred. Validity matters: a broken node
is worse than none.

## Content patterns that get cited

- Lead each section with the answer, then the reasoning.
- One idea per paragraph; each paragraph understandable alone.
- Numbers, units, dates, and named sources per passage.
- Question-shaped headings matching real queries.
- Visible author byline and a refresh date.

## Common myths

- "AI only cites big brands." Authority helps, but extractability and entity clarity are the
  levers a smaller site can actually pull.
- "Blocking GPTBot hurts my rankings." Training crawlers are separate from Search. Decide by
  policy, not fear.
- "More backlinks = more citations." Backlinks help discovery; they do not make a passage
  quotable.
- "Keyword density." It is not a meaningful AI-citation signal. Intent match is.

## Glossary

| Term | Meaning |
|------|---------|
| AEO | Answer Engine Optimization; synonym for GEO |
| GEO | Generative Engine Optimization |
| LLMO | LLM Optimization; synonym for GEO |
| AIO | Google AI Overviews |
| SERP feature | A non-standard result (snippet, PAA, AIO, knowledge panel) |
| Passage | A block of content an engine can extract as an answer |
| Citability | How liftable a passage is as a standalone answer |
| SSR | Server-side rendering; content present in the HTML response |
| CSR shell | A page whose HTML is empty until JavaScript runs |
| Entity | A resolvable thing (organization, person, product) |
| llms.txt | A proposed markdown index of a site for LLMs, at `/llms.txt` |
