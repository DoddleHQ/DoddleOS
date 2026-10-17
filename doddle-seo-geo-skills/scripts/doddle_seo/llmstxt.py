"""llms.txt parsing, validation and generation.

Format (llmstxt.org): an H1 project name, an optional blockquote summary, then H2
sections whose items are ``- [Title](url): note`` link lines.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

LINK_RE = re.compile(r"^\s*[-*]\s+\[([^\]]+)\]\(([^)]+)\)\s*(?::\s*(.*))?$")
H1_RE = re.compile(r"^#\s+(.+)$")
H2_RE = re.compile(r"^##\s+(.+)$")


@dataclass
class Item:
    title: str
    url: str
    note: str = ""


@dataclass
class Section:
    title: str
    items: List[Item] = field(default_factory=list)


@dataclass
class LlmsTxt:
    present: bool = False
    name: str = ""
    summary: str = ""
    sections: List[Section] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    @property
    def link_count(self) -> int:
        return sum(len(s.items) for s in self.sections)


def parse(text: str) -> LlmsTxt:
    doc = LlmsTxt(present=bool((text or "").strip()))
    if not doc.present:
        doc.errors.append("empty or missing llms.txt")
        return doc
    section: Optional[Section] = None
    in_summary = False
    summary_lines: List[str] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        m1 = H1_RE.match(line)
        m2 = H2_RE.match(line)
        ml = LINK_RE.match(line)
        if m1 and not doc.name:
            doc.name = m1.group(1).strip()
            in_summary = False
        elif m2:
            section = Section(title=m2.group(1).strip())
            doc.sections.append(section)
            in_summary = False
        elif ml:
            item = Item(title=ml.group(1).strip(), url=ml.group(2).strip(), note=(ml.group(3) or "").strip())
            if section is None:
                section = Section(title="(uncategorised)")
                doc.sections.append(section)
            section.items.append(item)
            in_summary = False
        elif line.strip().startswith(">") and not doc.summary:
            summary_lines.append(line.strip().lstrip(">").strip())
            in_summary = True
        elif in_summary and line.strip():
            summary_lines.append(line.strip())
        elif line.strip():
            # Plain prose not attached to a section — drop, but note it.
            pass
    doc.summary = " ".join(summary_lines).strip()
    if not doc.name:
        doc.errors.append("missing H1 project name")
    if doc.link_count == 0:
        doc.errors.append("no link lines found")
    return doc


def generate(name: str, summary: str, sections: List[Section]) -> str:
    out: List[str] = [f"# {name}", ""]
    if summary:
        out += [f"> {summary}", ""]
    for s in sections:
        if not s.items:
            continue
        out.append(f"## {s.title}")
        out.append("")
        for it in s.items:
            line = f"- [{it.title}]({it.url})"
            if it.note:
                line += f": {it.note}"
            out.append(line)
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def build_from_pages(site_name: str, summary: str, pages: List[Dict[str, str]]) -> str:
    """Build an llms.txt draft from crawled pages.

    ``pages`` items: ``{url, title, description, section}``. Keys the site cannot supply
    are left out rather than invented.
    """
    buckets: Dict[str, Section] = {}
    for p in pages:
        sec_title = p.get("section") or "Docs"
        sec = buckets.setdefault(sec_title, Section(title=sec_title))
        sec.items.append(Item(title=p.get("title") or p.get("url", ""), url=p.get("url", ""), note=p.get("description", "")))
    return generate(site_name, summary, list(buckets.values()))


def stats(doc: LlmsTxt) -> Dict[str, object]:
    return {
        "present": doc.present,
        "name": doc.name,
        "summary_present": bool(doc.summary),
        "sections": len(doc.sections),
        "links": doc.link_count,
        "errors": doc.errors,
    }
