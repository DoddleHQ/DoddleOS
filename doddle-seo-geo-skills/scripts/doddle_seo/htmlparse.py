"""Parse HTML into the structures the scorers need. stdlib-only.

We use ``html.parser`` rather than a third-party DOM so the toolkit stays zero-dependency
and the fixture tests run with no install.
"""

from __future__ import annotations

import html as _html
from html.parser import HTMLParser
import json
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin, urlparse

BLOCK_TAGS = {
    "p", "li", "h1", "h2", "h3", "h4", "h5", "h6",
    "blockquote", "td", "th", "dd", "dt", "figcaption", "pre", "summary",
}
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
SKIP_TAGS = {
    "script", "style", "noscript", "nav", "footer", "header", "aside",
    "template", "svg", "form", "iframe",
}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

QUESTION_RE = re.compile(r"\?\s*$")
DATE_META_KEYS = (
    "article:published_time", "article:modified_time", "og:updated_time",
    "datepublished", "datemodified", "date", "publishdate", "last-modified",
)


@dataclass
class Block:
    tag: str
    text: str
    level: Optional[int] = None

    @property
    def is_heading(self) -> bool:
        return self.level is not None

    @property
    def is_question(self) -> bool:
        return bool(QUESTION_RE.search(self.text))


@dataclass
class Parsed:
    base_url: str = ""
    title: str = ""
    meta_description: str = ""
    meta_robots: str = ""
    canonical: str = ""
    lang: str = ""
    has_viewport: bool = False
    viewport: str = ""
    headings: List[Block] = field(default_factory=list)
    blocks: List[Block] = field(default_factory=list)
    links: List[Dict[str, str]] = field(default_factory=list)
    images: List[Dict[str, str]] = field(default_factory=list)
    jsonld: List[str] = field(default_factory=list)
    og: Dict[str, str] = field(default_factory=dict)
    twitter: Dict[str, str] = field(default_factory=dict)
    hreflangs: List[Dict[str, str]] = field(default_factory=list)
    author: str = ""
    published: str = ""
    modified: str = ""
    text: str = ""
    word_count: int = 0
    html_chars: int = 0
    text_chars: int = 0
    amp: bool = False
    has_list: bool = False
    has_table: bool = False
    jsonld_types: List[str] = field(default_factory=list)

    @property
    def h1s(self) -> List[Block]:
        return [h for h in self.headings if h.level == 1]

    @property
    def content_ratio(self) -> float:
        if self.html_chars <= 0:
            return 0.0
        return round(self.text_chars / self.html_chars, 4)


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", _html.unescape(text)).strip()


class _Parser(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.p = Parsed(base_url=base_url)
        self._skip_depth = 0
        self._buf: List[str] = []
        self._buf_tag: Optional[str] = None
        self._full: List[str] = []
        self._in_title = False
        self._in_jsonld = False
        self._jsonld_buf: List[str] = []
        self._in_author = False
        self._author_buf: List[str] = []

    # -- text accumulation -------------------------------------------------
    def _flush(self) -> None:
        if self._buf_tag is None:
            self._buf = []
            return
        text = _norm("".join(self._buf))
        if text:
            block = Block(tag=self._buf_tag, text=text)
            if self._buf_tag in HEADING_TAGS:
                block.level = int(self._buf_tag[1])
                self.p.headings.append(block)
            self.p.blocks.append(block)
        self._buf = []
        self._buf_tag = None

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag in SKIP_TAGS:
            self._skip_depth += 1
        if tag in BLOCK_TAGS and self._skip_depth == 0:
            self._flush()
            self._buf_tag = tag
        if tag in ("ul", "ol"):
            self.p.has_list = True
        elif tag == "table":
            self.p.has_table = True
        if tag == "html" and a.get("lang"):
            self.p.lang = a["lang"].strip()
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            name = (a.get("name") or a.get("property") or "").lower()
            content = a.get("content", "")
            if name == "description":
                self.p.meta_description = _norm(content)
            elif name in ("robots", "googlebot"):
                self.p.meta_robots = (self.p.meta_robots + " " + content).strip()
            elif name == "viewport":
                self.p.has_viewport = True
                self.p.viewport = content
            elif name.startswith("og:"):
                self.p.og[name] = content
            elif name.startswith("twitter:"):
                self.p.twitter[name] = content
            elif name in DATE_META_KEYS:
                value = _norm(content)
                if "modified" in name and not self.p.modified:
                    self.p.modified = value
                elif not self.p.published:
                    self.p.published = value
            elif name in ("author", "article:author", "byl"):
                self.p.author = self.p.author or _norm(content)
        elif tag == "link":
            rel = (a.get("rel", "") + "").lower()
            if "canonical" in rel:
                self.p.canonical = a.get("href", "")
            if "amphtml" in rel:
                self.p.amp = True
            hreflang = a.get("hreflang")
            if hreflang:
                self.p.hreflangs.append({"hreflang": hreflang, "href": a.get("href", "")})
        elif tag == "a":
            href = a.get("href", "")
            self.p.links.append({"href": href, "rel": a.get("rel", ""), "title": a.get("title", "")})
        elif tag == "img":
            self.p.images.append({"src": a.get("src", ""), "alt": a.get("alt", ""), "loading": a.get("loading", "")})
        elif tag == "script":
            stype = (a.get("type", "") or "").lower()
            if stype == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_buf = []
        elif tag in ("p", "span", "div", "address") and "author" in (a.get("class", "") + a.get("itemprop", "")).lower():
            self._in_author = True
            self._author_buf = []

    def handle_startendtag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag == "img" or tag == "link" or tag == "meta":
            return

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "script":
            if self._in_jsonld:
                raw = "".join(self._jsonld_buf).strip()
                if raw:
                    self.p.jsonld.append(raw)
                    self._collect_jsonld_types(raw)
                self._in_jsonld = False
            if self._skip_depth > 0:
                self._skip_depth -= 1
        elif tag in SKIP_TAGS and self._skip_depth > 0:
            self._skip_depth -= 1
        if tag in BLOCK_TAGS and self._skip_depth == 0:
            self._flush()

    def handle_data(self, data: str) -> None:
        if self._in_jsonld:
            self._jsonld_buf.append(data)
            return
        if self._in_title:
            self.p.title += data
        if self._in_author:
            self._author_buf.append(data)
        if self._skip_depth == 0:
            self._full.append(data)
            if self._buf_tag is not None:
                self._buf.append(data)

    # -- helpers -----------------------------------------------------------
    def _collect_jsonld_types(self, raw: str) -> None:
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            return
        for node in _walk_jsonld(obj):
            t = node.get("@type")
            if isinstance(t, str):
                self.p.jsonld_types.append(t)
            elif isinstance(t, list):
                self.p.jsonld_types.extend(str(x) for x in t)

    def finish(self) -> Parsed:
        self._flush()
        self.p.text = _norm("".join(self._full))
        self.p.title = _norm(self.p.title)
        self.p.author = self.p.author or _norm("".join(self._author_buf))
        self.p.word_count = len(re.findall(r"\w+", self.p.text))
        self.p.text_chars = len(self.p.text)
        return self.p


def _walk_jsonld(obj) -> List[Dict]:
    out: List[Dict] = []
    if isinstance(obj, dict):
        out.append(obj)
        for v in obj.values():
            out.extend(_walk_jsonld(v))
    elif isinstance(obj, list):
        for item in obj:
            out.extend(_walk_jsonld(item))
    return out


def _original_size(html: str) -> int:
    return len(html)


def parse(html: str, base_url: str = "") -> Parsed:
    parser = _Parser(base_url)
    try:
        parser.feed(html)
        parser.close()
    except Exception:  # noqa: BLE001 - malformed markup must not crash scoring
        pass
    parsed = parser.finish()
    parsed.html_chars = _original_size(html)
    # Resolve internal/external links.
    host = urlparse(base_url).netloc
    for link in parsed.links:
        href = link["href"]
        absolute = urljoin(base_url, href) if base_url and not base_url.startswith("/") else href
        link["absolute"] = absolute
        netloc = urlparse(absolute).netloc
        link["internal"] = "1" if (not netloc or netloc == host) else "0"
    return parsed
