# AI crawler kinds and robots.txt patterns

Reference for `geo-crawlers`. The token lists below mirror the toolkit's crawler registry and
its `data_version`; read the envelope for the authoritative per-run set and never hardcode
tokens in a report.

## The three kinds

### search / answer — blocking removes AI visibility

These build the index that produces AI answers. Blocking them is a visibility loss, not a
policy statement.

| Token | Operator | Powers |
|-------|----------|--------|
| `OAI-SearchBot` | OpenAI | ChatGPT search |
| `Claude-SearchBot` | Anthropic | Claude search |
| `PerplexityBot` | Perplexity | Perplexity answers |
| `GoogleBot` | Google | Classic index; AI Overviews derive from it |
| `bingBot` | Microsoft | Bing index; Copilot |
| `Applebot` | Apple | Siri / Spotlight |
| `YouBot` | You.com | You.com answers |
| `DuckAssistBot` | DuckDuckGo | DuckDuckGo AI answers |

### training — blocking is a policy choice, no Search impact

These collect corpora for model training. Blocking them opts out of training and does not
touch classic Search.

| Token | Operator | Note |
|-------|----------|------|
| `GPTBot` | OpenAI | training corpus |
| `ClaudeBot`, `anthropic-ai` | Anthropic | training corpus |
| `Google-Extended` | Google | Gemini/Vertex training; not Search |
| `Google-CloudVertexBot` | Google | Vertex agent corpus |
| `Applebot-Extended` | Apple | Apple Intelligence training |
| `CCBot` | Common Crawl | open corpus |
| `Bytespider` | ByteDance | ByteDance / TikTok |
| `Amazonbot` | Amazon | Alexa / Amazon |
| `meta-externalagent`, `FacebookBot` | Meta | Meta AI, legacy |
| `cohere-ai`, `Diffbot`, `ImagesiftBot`, `omgili`, `Timpibot` | various | corpora |

### user — a live fetch on behalf of a person

A user-initiated fetch when someone browses or asks. Treat like a normal visitor.

| Token | Operator |
|-------|----------|
| `ChatGPT-User` | OpenAI |
| `Claude-User` | Anthropic |
| `Perplexity-User` | Perplexity |

## robots.txt patterns

Address a crawler by token. A group applies via case-insensitive match; a `*` group is the
fallback. An empty `Disallow:` allows everything.

Allow the answer engines to read the whole site, and opt training crawlers out if that is the
policy:

```
# Let AI answer engines read the site
User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

# Opt out of model training (no Search impact)
User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

Sitemap: https://example.com/sitemap.xml
```

Block one path for one crawler rather than the whole site:

```
User-agent: OAI-SearchBot
Disallow: /private/
Allow: /
```

Rules:

- Group agents on `User-agent:` lines; each group's `Allow`/`Disallow` lines follow it.
- Longest matching path wins; `$` anchors the end; `*` is a wildcard.
- Declare `Sitemap:` with an absolute URL so crawlers discover new pages.
- Validate before shipping: `dseo robots ./robots.txt --json`.

## What blocking each kind does

| Blocked kind | AI visibility | Classic Search | Training |
|--------------|---------------|----------------|----------|
| `search` | Removed | Depends on token: `GoogleBot`/`bingBot` also feed Search | n/a |
| `training` | Unaffected | Unaffected | Opted out |
| `user` | Live fetches fail; pages stay indexed | Unaffected | n/a |

Note: blocking `GoogleBot` or `bingBot` is a classic-Search act; blocking `Google-Extended`
or `Applebot-Extended` is not.
