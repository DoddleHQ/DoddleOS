"""Registry of known AI/search crawlers and their purpose.

Kept as data, versioned by ``DATA_VERSION`` in :mod:`doddle_seo`. A skill must never
hardcode this list; it reads the envelope produced from here.

``kind`` values:
    training  — used to build model training corpora (blocking this does NOT block search)
    search    — used to build the search/answer index (blocking this removes AI visibility)
    user      — a user-initiated fetch (treat like a normal visitor)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Crawler:
    id: str
    token: str
    operator: str
    kind: str
    note: str = ""


CRAWLERS: List[Crawler] = [
    # OpenAI
    Crawler("gptbot", "GPTBot", "OpenAI", "training", "Corpus for model training."),
    Crawler("oai_searchbot", "OAI-SearchBot", "OpenAI", "search", "Powers ChatGPT search results."),
    Crawler("chatgpt_user", "ChatGPT-User", "OpenAI", "user", "Live fetch when a user browses."),
    # Anthropic
    Crawler("claudebot", "ClaudeBot", "Anthropic", "training", "Corpus for Claude training."),
    Crawler("claude_user", "Claude-User", "Anthropic", "user", "Live fetch when a user browses."),
    Crawler("claude_searchbot", "Claude-SearchBot", "Anthropic", "search", "Powers Claude search."),
    Crawler("anthropic_ai", "anthropic-ai", "Anthropic", "training", "Legacy Anthropic corpus crawler."),
    # Perplexity
    Crawler("perplexitybot", "PerplexityBot", "Perplexity", "search", "Powers Perplexity answers."),
    Crawler("perplexity_user", "Perplexity-User", "Perplexity", "user", "Live fetch when a user asks."),
    # Google
    Crawler("google_extended", "Google-Extended", "Google", "training", "Gemini/Vertex training; does not affect Search."),
    Crawler("googlebot", "GoogleBot", "Google", "search", "Classic Search index; AI Overviews derive from it."),
    Crawler("google_cloudvertexbot", "Google-CloudVertexBot", "Google", "training", "Vertex AI agent corpus."),
    # Microsoft / Bing
    Crawler("bingbot", "bingBot", "Microsoft", "search", "Bing index; powers Copilot."),
    Crawler("applebot", "Applebot", "Apple", "search", "Siri/Spotlight; -Extended controls AI training."),
    Crawler("applebot_extended", "Applebot-Extended", "Apple", "training", "Apple Intelligence training."),
    # Others
    Crawler("ccbot", "CCBot", "Common Crawl", "training", "Open corpus many models train on."),
    Crawler("bytespider", "Bytespider", "ByteDance", "training", "ByteDance/TikTok corpus."),
    Crawler("amazonbot", "Amazonbot", "Amazon", "training", "Alexa / Amazon services."),
    Crawler("meta_externalagent", "meta-externalagent", "Meta", "training", "Meta AI corpus."),
    Crawler("facebookbot", "FacebookBot", "Meta", "training", "Legacy Meta corpus."),
    Crawler("cohere_ai", "cohere-ai", "Cohere", "training", "Cohere training crawler."),
    Crawler("youbot", "YouBot", "You.com", "search", "You.com answers."),
    Crawler("duckassistbot", "DuckAssistBot", "DuckDuckGo", "search", "DuckDuckGo AI answers."),
    Crawler("diffbot", "Diffbot", "Diffbot", "training", "Knowledge-graph extraction."),
    Crawler("imagesiftbot", "ImagesiftBot", "ImageSift", "training", "Image corpus."),
    Crawler("omgili", "omgili", "Webz.io", "training", "Webz.io corpus."),
    Crawler("timpibot", "Timpibot", "Timpi", "training", "Timpi search corpus."),
]

# De-duplicate by (token, kind) while preserving order.
_seen = set()
UNIQUE_CRAWLERS: List[Crawler] = []
for c in CRAWLERS:
    key = (c.token, c.kind)
    if key in _seen:
        continue
    _seen.add(key)
    UNIQUE_CRAWLERS.append(c)

BY_TOKEN: Dict[str, Crawler] = {}
for c in UNIQUE_CRAWLERS:
    BY_TOKEN.setdefault(c.token.lower(), c)


def lookup(token: str) -> Optional[Crawler]:
    return BY_TOKEN.get((token or "").lower())


def by_kind(kind: str) -> List[Crawler]:
    return [c for c in UNIQUE_CRAWLERS if c.kind == kind]
