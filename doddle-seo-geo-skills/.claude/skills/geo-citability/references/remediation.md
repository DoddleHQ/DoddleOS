# Citability remediation patterns

Rewrite patterns per failing signal. Use these to turn `findings[].detail` into concrete edits.

## self_containment (dangling references)

Bad: "This is why it matters."
Good: "Server rendering matters because AI crawlers do not execute JavaScript."

Rule: replace the leading pronoun with the noun phrase it stands for. Each paragraph should
make sense if it were the only paragraph on the page.

## answer_first (buried answer)

Bad: "There are many factors to consider. First, we should look at crawler access, and then…"
Good: "Allow `OAI-SearchBot` and `PerplexityBot` in `robots.txt`. The rest of this section
explains why search crawlers matter more than training crawlers."

Rule: first sentence = the answer. Subsequent sentences = the reasoning.

## structure

- Add H2s for each sub-question.
- Convert key headings into the question users ask (question-shaped headings).
- Turn three or more parallel facts into a list; turn comparisons into a table.
- Keep exactly one H1.

## evidence_density

Add at least one verifiable datum per passage: a number with a unit, a year, a named source, or
a short quotation. "Fast" → "loaded in 1.2 s on 4G (WebPageTest, 2026)."

## extractability (JS-gated / thin)

- Server-render (SSR/SSG) the primary content so it is in the HTML response.
- If a framework renders client-side, add SSR or prerendering for indexable routes.
- Do not rely on `noscript` for the core answer.

## attribution

- Add a visible byline linking to an author page.
- Show `published` and `updated` dates, machine-readable (`datePublished`/`dateModified`).
- Add `Article` (`author`, `datePublished`, `dateModified`, `publisher`).
- Add a `rel=canonical`.

## freshness

- Update the content and the `dateModified`; a real change, not a date bump.
- Refresh statistics and examples so the date is honest.
