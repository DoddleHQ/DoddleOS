"""Citability: can an AI engine lift a passage and use it as an answer?

Seven signals, 100 points total. Every value is computed from the parsed page; the model
explains but never re-derives.

    citability.self_containment  25  passages stand alone (no dangling "this/it")
    citability.answer_first      20  sections lead with the answer
    citability.structure         15  headings, question headings, lists/tables
    citability.evidence_density  15  facts, numbers, citations per passage
    citability.extractability    15  text-to-HTML ratio; not JavaScript-gated
    citability.attribution        5  byline, dates, Article schema, canonical
    citability.freshness          5  how recently the page was updated
"""

from __future__ import annotations

import datetime
import re
from dataclasses import dataclass
from typing import Dict, List, Optional

from .envelope import DETERMINISTIC, HEURISTIC, Signal
from .htmlparse import Block, Parsed

DANGLING_RE = re.compile(
    r"^(this|that|these|those|it|they|them|he|she|we|us|you|there|such|"
    r"the former|the latter|as (mentioned|discussed|noted|described|stated)|"
    r"the above|additionally|moreover|furthermore|however|therefore|thus|also|"
    r"and|but|so|because)\b",
    re.IGNORECASE,
)
FACT_RE = re.compile(r"(\d[\d,\.]*\s?%|\$\s?\d|€\s?\d|£\s?\d|\b\d{4}\b|\b\d+(\.\d+)?\s?(ms|s|x|k|m|bn|gb|mb)\b|\b\d+\.\d+\b)", re.IGNORECASE)
CITATION_RE = re.compile(r"\(([^)]*\b(19|20)\d{2}\b[^)]*)\)|\[[0-9]+\]|https?://")
FILLER_RE = re.compile(r"^(in this (article|post|guide)|welcome|let'?s (take a|dive|explore)|in today'?s|as you (may|might) know|before we)\b", re.IGNORECASE)

MIN_BLOCK_WORDS = 8
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


@dataclass
class Citability:
    signals: List[Signal]
    composite: Optional[float]
    missing: List[str]

    def to_dict(self) -> Dict[str, object]:
        return {
            "composite": self.composite,
            "signals": [s.to_dict() for s in self.signals],
            "missing": self.missing,
        }


def _words(text: str) -> int:
    return len(re.findall(r"\w+", text))


def _candidates(page: Parsed) -> List[Block]:
    return [b for b in page.blocks if not b.is_heading and _words(b.text) >= MIN_BLOCK_WORDS]


def _extractability(page: Parsed) -> Signal:
    ratio = page.content_ratio
    target = 0.15
    value = round(min(1.0, ratio / target) * 15, 1)
    gated = page.word_count < 50
    detail = {
        "content_chars": page.text_chars,
        "html_chars": page.html_chars,
        "content_ratio": ratio,
        "word_count": page.word_count,
        "javascript_gated": gated,
    }
    if gated:
        return Signal("citability.extractability", 0.0, 15, HEURISTIC, detail, skipped_reason="not applicable: page has almost no server-rendered text")
    return Signal("citability.extractability", value, 15, HEURISTIC, detail)


def _structure(page: Parsed) -> Signal:
    headings = page.headings
    question_headings = [h for h in headings if h.is_question]
    component = 0.0
    component += 4 if len(headings) >= 2 else (2 if len(headings) == 1 else 0)
    component += 3 if len(page.h1s) == 1 else 0
    component += 4 if question_headings else 0
    component += 4 if (page.has_list or page.has_table) else 0
    detail = {
        "headings": len(headings),
        "h1_count": len(page.h1s),
        "question_headings": len(question_headings),
        "has_list": page.has_list,
        "has_table": page.has_table,
        "breakdown": {"headings": 4 if len(headings) >= 2 else 0, "single_h1": 3 if len(page.h1s) == 1 else 0,
                       "questions": 4 if question_headings else 0, "list_or_table": 4 if (page.has_list or page.has_table) else 0},
    }
    return Signal("citability.structure", round(component, 1), 15, HEURISTIC, detail)


def _self_containment(page: Parsed) -> Signal:
    cands = _candidates(page)
    if not cands:
        return Signal("citability.self_containment", None, 25, HEURISTIC, {"candidate_blocks": 0},
                      skipped_reason="not applicable: no prose passages to assess")
    bad = [b for b in cands if DANGLING_RE.match(b.text)]
    good = len(cands) - len(bad)
    ratio = good / len(cands)
    detail = {
        "candidate_blocks": len(cands),
        "self_contained": good,
        "ratio": round(ratio, 4),
        "worst_example": (bad[0].text[:160] if bad else None),
    }
    return Signal("citability.self_containment", round(ratio * 25, 1), 25, HEURISTIC, detail)


def _sections(page: Parsed) -> List[List[Block]]:
    sections: List[List[Block]] = []
    current: Optional[List[Block]] = None
    for b in page.blocks:
        if b.is_heading:
            if b.level and b.level >= 2:
                current = []
                sections.append(current)
            continue
        if current is not None:
            current.append(b)
    return [s for s in sections if s]


def _answer_first(page: Parsed) -> Signal:
    sections = _sections(page)
    if not sections:
        return Signal("citability.answer_first", None, 20, HEURISTIC, {"sections": 0},
                      skipped_reason="not applicable: no section structure")
    good = 0
    example = None
    for sec in sections:
        first = sec[0].text
        sentence = re.split(r"(?<=[.!?])\s+", first, maxsplit=1)[0]
        words = sentence.split()
        leads = len(words) <= 40 and not FILLER_RE.match(sentence)
        if leads:
            good += 1
        elif example is None:
            example = first[:160]
    ratio = good / len(sections)
    detail = {"sections": len(sections), "answer_first": good, "ratio": round(ratio, 4), "worst_example": example}
    return Signal("citability.answer_first", round(ratio * 20, 1), 20, HEURISTIC, detail)


def _evidence_density(page: Parsed) -> Signal:
    cands = _candidates(page)
    if not cands:
        return Signal("citability.evidence_density", None, 15, HEURISTIC, {"candidate_blocks": 0},
                      skipped_reason="not applicable: no prose passages to assess")
    with_facts = [b for b in cands if FACT_RE.search(b.text) or CITATION_RE.search(b.text)]
    ratio = len(with_facts) / len(cands)
    external_domains = _external_domains(page)
    detail = {
        "blocks_with_facts": len(with_facts),
        "candidate_blocks": len(cands),
        "external_domains": external_domains,
    }
    return Signal("citability.evidence_density", round(ratio * 15, 1), 15, HEURISTIC, detail)


def _attribution(page: Parsed) -> Signal:
    checks = {
        "byline": bool(page.author),
        "dates": bool(page.published or page.modified),
        "article_schema": any(t in page.jsonld_types for t in ("Article", "NewsArticle", "BlogPosting")),
        "canonical": bool(page.canonical),
    }
    present = sum(1 for v in checks.values() if v)
    value = round(present / 4 * 5, 1)
    detail = dict(checks)
    return Signal("citability.attribution", value, 5, DETERMINISTIC, detail)


def _freshness(page: Parsed) -> Signal:
    stamp = page.modified or page.published
    if not stamp:
        return Signal("citability.freshness", 0.0, 5, DETERMINISTIC, {"date": None, "reason": "no published/modified date present"})
    match = DATE_RE.search(stamp)
    if not match:
        return Signal("citability.freshness", 0.0, 5, DETERMINISTIC, {"date": stamp, "reason": "date not parsable"})
    try:
        when = datetime.date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    except ValueError:
        return Signal("citability.freshness", 0.0, 5, DETERMINISTIC, {"date": stamp, "reason": "invalid date"})
    age_days = (datetime.date.today() - when).days
    if age_days <= 180:
        value = 5.0
    elif age_days <= 365:
        value = 4.0
    elif age_days <= 730:
        value = 2.5
    else:
        value = 1.0
    return Signal("citability.freshness", value, 5, DETERMINISTIC, {"date": when.isoformat(), "age_days": age_days})


def _external_domains(page: Parsed) -> int:
    from urllib.parse import urlparse

    domains = set()
    host = urlparse(page.base_url).netloc
    for link in page.links:
        netloc = urlparse(link.get("absolute", "")).netloc
        if netloc and netloc != host:
            domains.add(netloc)
    return len(domains)


def score_citability(page: Parsed) -> Citability:
    signals = [
        _self_containment(page),
        _answer_first(page),
        _structure(page),
        _evidence_density(page),
        _extractability(page),
        _attribution(page),
        _freshness(page),
    ]
    measured = [s for s in signals if s.value is not None]
    missing = [s.id for s in signals if s.value is None]
    if measured:
        got = sum(s.value for s in measured)
        maxv = sum(s.max for s in measured)
        composite = round(got / maxv * 100, 1) if maxv else None
    else:
        composite = None
    return Citability(signals=signals, composite=composite, missing=missing)
