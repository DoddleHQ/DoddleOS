"""Site audit: discover pages, score each, aggregate into weighted categories."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin, urlparse

from . import DATA_VERSION, SCORING_VERSION, TOOLKIT_VERSION
from . import robots as robots_mod
from .citability import score_citability
from .envelope import CURRENT, PARTIAL, Finding, error_envelope, make_envelope, tier_for
from .fetch import RateLimiter, fetch
from .htmlparse import parse
from .scoring import analyze_page

LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>", re.IGNORECASE)

CATEGORY_WEIGHTS = {"citability": 0.40, "technical": 0.30, "schema": 0.15, "content": 0.15}


@dataclass
class AuditResult:
    url: str
    pages_ok: int = 0
    pages: List[str] = field(default_factory=list)
    pages_failed: List[Dict[str, Any]] = field(default_factory=list)
    categories: Dict[str, float] = field(default_factory=dict)
    signals: List[Any] = field(default_factory=list)
    findings: List[Finding] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


def discover(base_url: str, *, max_pages: int, allow_private: bool, timeout: float) -> List[str]:
    """Discover internal URLs from the start page and its sitemap."""
    parsed = urlparse(base_url)
    if parsed.scheme not in ("http", "https"):
        # A local file: score just that file, do not crawl link paths.
        return [base_url]
    root = f"{parsed.scheme}://{parsed.netloc}"
    start = fetch(base_url, allow_private=allow_private, timeout=timeout)
    urls: List[str] = [base_url]
    seen = {_norm_url(base_url)}

    if start.ok and start.body:
        page = parse(start.body, base_url=start.final_url or base_url)
        for link in page.links:
            href = link.get("href", "")
            if not href or link.get("internal") != "1":
                continue
            absolute = _norm_url(urljoin(start.final_url or base_url, href))
            if _same_host(absolute, root) and absolute not in seen and _is_htmlish(absolute):
                seen.add(absolute)
                urls.append(absolute)
                if len(urls) >= max_pages:
                    break

    if len(urls) < max_pages:
        for sitemap_url in _sitemap_candidates(root, allow_private, timeout):
            sm = fetch(sitemap_url, allow_private=allow_private, timeout=timeout)
            if not sm.ok or not sm.body:
                continue
            for loc in LOC_RE.findall(sm.body):
                absolute = _norm_url(loc)
                if _same_host(absolute, root) and absolute not in seen and _is_htmlish(absolute):
                    seen.add(absolute)
                    urls.append(absolute)
                    if len(urls) >= max_pages:
                        return urls
    return urls[:max_pages]


def audit_site(url: str, *, max_pages: int = 50, rate: float = 1.0,
               allow_private: bool = False, timeout: float = 20.0) -> Dict[str, Any]:
    limiter = RateLimiter(rate)
    urls = discover(url, max_pages=max_pages, allow_private=allow_private, timeout=timeout)

    result = AuditResult(url=url)
    category_totals: Dict[str, List[float]] = {k: [] for k in CATEGORY_WEIGHTS}
    finding_index: Dict[str, Finding] = {}

    for page_url in urls:
        limiter.wait()
        report = analyze_page(page_url, allow_private=allow_private, timeout=timeout)
        if not report.ok:
            result.pages_failed.append({"url": page_url, "reason": report.error or "failed", "status": report.fetched.status})
            continue
        result.pages_ok += 1
        result.pages.append(page_url)
        cats = dict(report.categories)
        cats["content"] = _content_category(report.page)
        for key in category_totals:
            if cats.get(key) is not None:
                category_totals[key].append(cats[key])
        for f in report.findings:
            existing = finding_index.get(f.id)
            if existing is None:
                finding_index[f.id] = f
            else:
                existing.pages.extend(p for p in f.pages if p not in existing.pages)
                existing.points_lost = max(existing.points_lost, f.points_lost)

    result.categories = {k: round(sum(v) / len(v), 1) for k, v in category_totals.items() if v}
    measured = {k: v for k, v in result.categories.items() if k in CATEGORY_WEIGHTS}
    if measured:
        weight_sum = sum(CATEGORY_WEIGHTS[k] for k in measured)
        composite = round(sum(measured[k] * CATEGORY_WEIGHTS[k] for k in measured) / weight_sum, 1)
    else:
        composite = None
    result.findings = list(finding_index.values())

    if not urls or (result.pages_ok == 0 and result.pages_failed):
        first = result.pages_failed[0] if result.pages_failed else {"reason": "no pages discovered"}
        return error_envelope(
            "audit", url, first.get("reason", "audit failed"),
            "Check the site is reachable over HTTPS. For localhost/staging pass --allow-private.",
            toolkit_version=TOOLKIT_VERSION, scoring_version=SCORING_VERSION, data_version=DATA_VERSION,
            pages_ok=0, pages_failed=result.pages_failed,
        )

    stamp = CURRENT if not result.pages_failed else PARTIAL
    if result.pages_failed:
        result.notes.append(f"{len(result.pages_failed)} page(s) could not be evaluated")
    scores = {
        "composite": composite,
        "tier": tier_for(composite),
        "categories": result.categories,
        "weights": CATEGORY_WEIGHTS,
    }
    return make_envelope(
        "audit", url,
        toolkit_version=TOOLKIT_VERSION, scoring_version=SCORING_VERSION, data_version=DATA_VERSION,
        evidence_stamp=stamp, pages_ok=result.pages_ok, pages_failed=result.pages_failed, notes=result.notes,
        categories={**result.categories, **{f"weight:{k}": v for k, v in CATEGORY_WEIGHTS.items()}},
        scores=scores, signals=result.signals, findings=result.findings,
        signal_count=len(result.categories), signal_total=len(CATEGORY_WEIGHTS),
    )


def _content_category(page) -> float:
    if page is None:
        return 0.0
    cites = score_citability(page)
    by_id = {s.id: s for s in cites.signals}
    total = 0.0
    maxv = 0.0
    for sid, mx in (("citability.structure", 15), ("citability.evidence_density", 15),
                    ("citability.attribution", 5), ("citability.freshness", 5)):
        s = by_id.get(sid)
        if s is None or s.value is None:
            continue
        total += s.value
        maxv += mx
    return round(total / maxv * 100, 1) if maxv else 0.0


def _norm_url(u: str) -> str:
    u = u.split("#", 1)[0]
    return u.rstrip("/") or u


def _same_host(u: str, root: str) -> bool:
    return urlparse(u).netloc == urlparse(root).netloc


def _is_htmlish(u: str) -> bool:
    path = urlparse(u).path.lower()
    if not path or path.endswith("/"):
        return True
    return not re.search(r"\.(png|jpe?g|gif|svg|webp|pdf|zip|gz|css|js|ico|mp4|mp3|woff2?)$", path)


def _sitemap_candidates(root: str, allow_private: bool, timeout: float) -> List[str]:
    candidates = []
    robots_txt = fetch(f"{root}/robots.txt", allow_private=allow_private, timeout=timeout)
    if robots_txt.ok and robots_txt.body:
        for sm in robots_mod.parse(robots_txt.body).sitemaps:
            if sm not in candidates:
                candidates.append(sm)
    if f"{root}/sitemap.xml" not in candidates:
        candidates.append(f"{root}/sitemap.xml")
    return candidates
