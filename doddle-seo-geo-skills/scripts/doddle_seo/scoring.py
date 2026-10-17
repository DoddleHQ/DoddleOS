"""Per-page scoring: technical foundations, schema, citability, and findings.

This module is the single source of truth for a page's numbers. ``score`` (one page) and
``audit`` (a site) both build on :func:`analyze_page`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

from . import DATA_VERSION, SCORING_VERSION, TOOLKIT_VERSION
from . import schema as schema_mod
from .citability import score_citability
from .envelope import (
    CURRENT,
    DETERMINISTIC,
    HEURISTIC,
    Finding,
    Signal,
    error_envelope,
    make_envelope,
    tier_for,
)
from .fetch import Fetched, fetch
from .htmlparse import Parsed, parse

SEVERITY_RANK = {"critical": 1, "high": 2, "medium": 3, "low": 4}
EFFORT_RANK = {"low": 1, "medium": 2, "high": 3}

TITLE_MIN, TITLE_MAX = 15, 65
META_MIN, META_MAX = 50, 165
MIN_WORDS = 300


@dataclass
class PageReport:
    url: str
    fetched: Fetched
    page: Optional[Parsed] = None
    signals: List[Signal] = field(default_factory=list)
    findings: List[Finding] = field(default_factory=list)
    categories: Dict[str, Optional[float]] = field(default_factory=dict)
    missing: List[str] = field(default_factory=list)
    error: Optional[str] = None

    @property
    def ok(self) -> bool:
        return self.error is None and self.page is not None


def _finding(sev: str, effort: str, points: float, fid: str, title: str, detail: str, url: str, excerpt: Optional[str] = None) -> Finding:
    return Finding(
        id=fid,
        priority=SEVERITY_RANK.get(sev, 3),
        severity=sev,
        effort=effort,
        points_lost=round(points, 1),
        title=title,
        detail=detail,
        pages=[url],
        excerpt=excerpt,
    )


def _ratio(numerator: int, denominator: int) -> float:
    return (numerator / denominator) if denominator else 0.0


def _technical(page: Parsed, url: str) -> tuple[List[Signal], List[Finding], Dict[str, Optional[float]]]:
    signals: List[Signal] = []
    findings: List[Finding] = []
    weights = {"lang": 1, "title": 3, "meta": 3, "canonical": 2, "viewport": 2,
               "h1": 2, "indexable": 5, "https": 3, "alt": 2, "content": 2}
    scores: Dict[str, float] = {}

    # indexability
    robots_meta = page.meta_robots.lower()
    noindex = "noindex" in robots_meta
    scores["indexable"] = 0.0 if noindex else 1.0
    signals.append(Signal("technical.indexable", scores["indexable"], 1, DETERMINISTIC,
                          {"meta_robots": page.meta_robots or None, "noindex": noindex}))
    if noindex:
        findings.append(_finding("critical", "low", weights["indexable"], "tech.noindex",
                                 "Page is set to noindex", "The meta robots tag contains noindex; search engines and AI indexes will drop this page. Remove it unless intentional.", url))

    scores["lang"] = 1.0 if page.lang else 0.0
    signals.append(Signal("technical.lang", scores["lang"], 1, DETERMINISTIC, {"lang": page.lang or None}))
    if not page.lang:
        findings.append(_finding("low", "low", weights["lang"], "tech.lang",
                                 "No HTML lang attribute", "Add a lang attribute to <html> so engines know the page language.", url))

    tlen = len(page.title)
    scores["title"] = 1.0 if TITLE_MIN <= tlen <= TITLE_MAX else (0.5 if page.title else 0.0)
    signals.append(Signal("technical.title", scores["title"], 1, DETERMINISTIC,
                          {"title": page.title or None, "length": tlen, "target": f"{TITLE_MIN}-{TITLE_MAX}"}))
    if not page.title:
        findings.append(_finding("high", "low", weights["title"], "tech.title.missing",
                                 "Missing title tag", "Add a unique, descriptive <title> of 15-65 characters.", url))
    elif tlen > TITLE_MAX:
        findings.append(_finding("medium", "low", weights["title"], "tech.title.long",
                                 "Title too long", f"Title is {tlen} chars; aim for {TITLE_MIN}-{TITLE_MAX} so it is not truncated.", url, page.title[:120]))
    elif tlen < TITLE_MIN:
        findings.append(_finding("medium", "low", weights["title"], "tech.title.short",
                                 "Title too short", f"Title is {tlen} chars; aim for {TITLE_MIN}-{TITLE_MAX}.", url, page.title[:120]))

    mlen = len(page.meta_description)
    scores["meta"] = 1.0 if META_MIN <= mlen <= META_MAX else (0.5 if page.meta_description else 0.0)
    signals.append(Signal("technical.meta_description", scores["meta"], 1, DETERMINISTIC,
                          {"present": bool(page.meta_description), "length": mlen, "target": f"{META_MIN}-{META_MAX}"}))
    if not page.meta_description:
        findings.append(_finding("high", "low", weights["meta"], "tech.meta.missing",
                                 "Missing meta description", "Add a compelling 50-165 character description.", url))

    scores["canonical"] = 1.0 if page.canonical else 0.0
    signals.append(Signal("technical.canonical", scores["canonical"], 1, DETERMINISTIC, {"canonical": page.canonical or None}))
    if not page.canonical:
        findings.append(_finding("medium", "low", weights["canonical"], "tech.canonical",
                                 "No canonical tag", "Add a rel=canonical to consolidate duplicates and help AI attribute the source.", url))

    scores["viewport"] = 1.0 if page.has_viewport else 0.0
    signals.append(Signal("technical.viewport", scores["viewport"], 1, DETERMINISTIC, {"viewport": page.viewport or None}))
    if not page.has_viewport:
        findings.append(_finding("medium", "low", weights["viewport"], "tech.viewport",
                                 "No mobile viewport", "Add a viewport meta tag for mobile-first indexing.", url))

    scores["h1"] = 1.0 if len(page.h1s) == 1 else 0.0
    signals.append(Signal("technical.single_h1", scores["h1"], 1, DETERMINISTIC, {"h1_count": len(page.h1s)}))
    if len(page.h1s) != 1:
        findings.append(_finding("medium", "low", weights["h1"], "tech.h1",
                                 f"{len(page.h1s)} H1 headings", "Use exactly one H1 that states the page topic.", url))

    scheme_ok = urlparse(url).scheme == "https" or not url.startswith("http")
    scores["https"] = 1.0 if scheme_ok else 0.0
    signals.append(Signal("technical.https", scores["https"], 1, DETERMINISTIC, {"https": scheme_ok}))

    if page.images:
        with_alt = sum(1 for i in page.images if (i.get("alt") or "").strip())
        alt_ratio = _ratio(with_alt, len(page.images))
        scores["alt"] = round(alt_ratio, 4)
        signals.append(Signal("technical.image_alt", scores["alt"], 1, DETERMINISTIC,
                              {"images": len(page.images), "with_alt": with_alt, "ratio": round(alt_ratio, 4)}))
        if alt_ratio < 0.8:
            findings.append(_finding("low", "low", weights["alt"] * (1 - alt_ratio), "tech.alt",
                                     "Images missing alt text", f"{len(page.images) - with_alt} of {len(page.images)} images lack alt text.", url))
    else:
        scores["alt"] = 1.0
        signals.append(Signal("technical.image_alt", 1.0, 1, DETERMINISTIC, {"images": 0}))

    scores["content"] = 1.0 if page.word_count >= MIN_WORDS else round(_ratio(page.word_count, MIN_WORDS), 4)
    signals.append(Signal("technical.content_length", scores["content"], 1, DETERMINISTIC, {"word_count": page.word_count, "target": MIN_WORDS}))
    if page.word_count < MIN_WORDS and page.word_count > 0:
        findings.append(_finding("medium", "high", weights["content"] * (1 - scores["content"]), "tech.thin",
                                 "Thin content", f"{page.word_count} words; pages under {MIN_WORDS} rarely satisfy intent or earn citations.", url))

    weighted = sum(scores[k] * weights[k] for k in weights)
    category = round(weighted / sum(weights.values()) * 100, 1)
    return signals, findings, {"technical": category}


def _schema_and_citability(page: Parsed, url: str) -> tuple[List[Signal], List[Finding], Dict[str, Optional[float]], List[str]]:
    signals: List[Signal] = []
    findings: List[Finding] = []
    report = schema_mod.analyze(page.jsonld)
    # schema category: presence + validity + entity linkage
    schema_score = 0.0
    if report.present:
        schema_score = 50.0
        if report.node_count and not report.errors:
            schema_score += 25.0
        if report.same_as:
            schema_score += 15.0
        if report.entity_ids:
            schema_score += 10.0
    schema_score = round(min(schema_score, 100.0), 1)
    signals.append(Signal("schema.present", 1.0 if report.present else 0.0, 1, DETERMINISTIC, schema_mod.signals(report)))
    if not report.present:
        findings.append(_finding("high", "low", 10, "schema.missing",
                                 "No structured data", "Add JSON-LD (Organization/WebSite at minimum) so engines can identify the entity.", url))
    elif report.errors:
        findings.append(_finding("medium", "low", 6, "schema.errors",
                                 "Invalid structured data", f"{len(report.errors)} schema issues: {report.errors[0]['message']}", url))
    if report.present and not report.same_as:
        findings.append(_finding("medium", "low", 4, "schema.sameas",
                                 "No sameAs entity links", "Add sameAs URLs (Wikipedia, LinkedIn, etc.) to the Organization node.", url))

    cites = score_citability(page)
    signals.extend(cites.signals)
    for s in cites.signals:
        if s.skipped_reason:
            continue
        if s.value is None:
            continue
        ratio = s.value / s.max
        if ratio < 0.5 and s.id in ("citability.answer_first", "citability.self_containment"):
            findings.append(_finding(
                "high", "medium", s.max - s.value, s.id,
                f"Low {s.id.split('.')[-1].replace('_', ' ')}",
                s.detail.get("worst_example", "") or "Passages do not stand alone / sections bury the answer.",
                url,
                excerpt=s.detail.get("worst_example"),
            ))
        if s.id == "citability.attribution" and ratio < 0.5:
            findings.append(_finding("medium", "low", s.max - (s.value or 0), "citability.attribution",
                                     "Weak attribution signals", "Add byline, published/modified dates, Article schema and a canonical.", url))
        if s.id == "citability.freshness" and (s.value or 0) <= 1:
            findings.append(_finding("medium", "low", s.max - (s.value or 0), "citability.freshness",
                                     "Stale or undated content", "Add and refresh a visible modified date; engines prefer current sources.", url))

    categories = {"schema": schema_score, "citability": cites.composite}
    return signals, findings, categories, cites.missing  # type: ignore[return-value]


def analyze_page(url: str, *, html: Optional[str] = None, fetched: Optional[Fetched] = None,
                 allow_private: bool = False, timeout: float = 20.0) -> PageReport:
    if fetched is None and html is None:
        fetched = fetch(url, allow_private=allow_private, timeout=timeout)
    elif fetched is None:
        fetched = Fetched(url, url, 200, html or "", "text/html")

    if fetched.error and not fetched.body:
        return PageReport(url=url, fetched=fetched, error=fetched.error)
    if not fetched.body:
        return PageReport(url=url, fetched=fetched, error=f"empty response (status {fetched.status})")

    page = parse(fetched.body, base_url=fetched.final_url or url)
    tech_signals, tech_findings, tech_cat = _technical(page, url)
    schema_signals, schema_findings, schema_cat, missing = _schema_and_citability(page, url)

    signals = tech_signals + schema_signals
    findings = tech_findings + schema_findings
    categories = {**tech_cat, **schema_cat}
    return PageReport(url=url, fetched=fetched, page=page, signals=signals, findings=findings, categories=categories, missing=missing)


def score_to_envelope(url: str, *, html: Optional[str] = None, allow_private: bool = False, timeout: float = 20.0) -> Dict[str, Any]:
    report = analyze_page(url, html=html, allow_private=allow_private, timeout=timeout)
    if not report.ok:
        code = report.fetched.status
        msg = report.error or "unknown error"
        hint = "Check the URL is reachable over HTTPS, or pass --allow-private for localhost/staging."
        if report.fetched.headers.get("hint"):
            hint = report.fetched.headers["hint"]
        return error_envelope(
            "score", url, msg, hint,
            toolkit_version=TOOLKIT_VERSION, scoring_version=SCORING_VERSION, data_version=DATA_VERSION,
            pages_ok=0,
            pages_failed=[{"url": url, "reason": msg, "status": code}],
        )

    composite = report.categories.get("citability")
    measured = [s for s in report.signals if s.value is not None]
    scores = {
        "composite": composite,
        "tier": tier_for(composite),
        "categories": {k: v for k, v in report.categories.items() if v is not None},
    }
    notes = []
    if report.fetched.final_url and report.fetched.final_url != url:
        notes.append(f"redirected to {report.fetched.final_url}")
    return make_envelope(
        "score", url,
        toolkit_version=TOOLKIT_VERSION, scoring_version=SCORING_VERSION, data_version=DATA_VERSION,
        evidence_stamp=CURRENT, pages_ok=1, notes=notes,
        categories={k: v for k, v in report.categories.items() if v is not None},
        missing=report.missing,
        signal_count=len(measured), signal_total=len(report.signals),
        scores=scores, signals=report.signals, findings=report.findings,
    )


def summarize_findings(findings: List[Finding], limit: Optional[int] = None) -> List[Finding]:
    ordered = sorted(findings, key=lambda f: (f.priority, EFFORT_RANK.get(f.effort, 2), -f.points_lost))
    return ordered[:limit] if limit else ordered
