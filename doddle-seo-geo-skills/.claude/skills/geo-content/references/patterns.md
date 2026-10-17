# Editorially quotable content — before/after patterns

Reference for `geo-content`. Each pattern maps to a deterministic citability signal. Use these
to turn `findings[].detail` into concrete edits. The edits are **advisory**; only a re-run of
`dseo citability` can confirm a change.

## Self-containment (signal: `citability.self_containment`)

A passage must make sense lifted out of the page, because that is how it gets quoted.

**Before**
> This is why it matters. It can also break rendering, and they often miss it.

**After**
> Server rendering matters because AI crawlers do not execute JavaScript. A client-only
> page can look complete in a browser while the crawler sees an empty shell.

Rule: replace each leading pronoun with the noun phrase it stands for. The `detail.worst_example`
from the envelope shows the exact offender to fix first.

## Answer-first (signal: `citability.answer_first`)

**Before**
> There are many factors to consider when configuring AI-crawler access. Before deciding, let us
> look at how robots.txt groups work, and then we will compare search and training crawlers.

**After**
> Allow the search crawlers (for example `OAI-SearchBot` and `PerplexityBot`) in `robots.txt`.
> The rest of this section explains why search crawlers matter more than training crawlers.

Rule: the first sentence is the answer; the sentences after it are the reasoning. Keep the first
sentence under about 40 words and drop openers like "In this article…" or "Welcome…".

## Structure (signal: `citability.structure`)

- Give each sub-question its own H2.
- Phrase important headings as the question users ask.
- Convert three or more parallel facts into a list.
- Convert any comparison into a table.
- Keep exactly one H1.

**Before**
> Our plans. Starter gives you one seat and email support. Growth gives five seats, priority
> support and analytics. Enterprise is unlimited with a dedicated manager.

**After**
> ## What does each plan include?
>
> | Plan | Seats | Support | Analytics |
> |------|-------|---------|-----------|
> | Starter | 1 | Email | No |
> | Growth | 5 | Priority | Yes |
> | Enterprise | Unlimited | Dedicated manager | Yes |

## Evidence density (signal: `citability.evidence_density`)

Every passage should carry at least one verifiable datum: a number with a unit, a year, a named
source, or a short quotation.

**Before**
> Our pages load fast, which helps both users and crawlers.

**After**
> Our pages render their main content in 1.2 s on a 4G connection (internal test run,
> 2026-01), so the text is present before any AI crawler gives up.

Rule: never invent the datum. If you do not have a real number or source, keep the claim but mark
it as still needing evidence rather than fabricating one.

## Extractability (signal: `citability.extractability`)

If this signal is `null` with a `skipped_reason`, the page has almost no server-rendered text.

- Server-render (SSR/SSG) the primary content so it is in the HTML response.
- Add SSR or prerendering for indexable routes in client-rendered frameworks.
- Do not rely on `noscript` to carry the answer.

## Order of operations

1. Extractability — a page with no text cannot be quoted, whatever else you fix.
2. Self-containment — make each passage stand alone.
3. Answer-first — lead each section with the answer.
4. Structure and evidence density — make it findable and factual.

Re-run `dseo citability <url> --json` after the edits to remeasure. Until then, the rewrite is
advisory and the score is unchanged.
