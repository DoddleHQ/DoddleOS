"""JSON-LD / schema.org analysis for both rich results and AI entity signals.

Validates presence of common types and their required properties, and extracts the
entity signals (``sameAs``, ``@id``, ``knowsAbout``) that matter for GEO.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# Minimal required properties per type. Not a full schema.org validator.
REQUIRED: Dict[str, List[str]] = {
    "Organization": ["name", "url"],
    "WebSite": ["url"],
    "WebPage": ["url"],
    "Article": ["headline", "author", "datePublished"],
    "NewsArticle": ["headline", "author", "datePublished"],
    "BlogPosting": ["headline", "author", "datePublished"],
    "Product": ["name", "offers"],
    "Offer": ["price", "priceCurrency"],
    "FAQPage": ["mainEntity"],
    "Question": ["name", "acceptedAnswer"],
    "BreadcrumbList": ["itemListElement"],
    "LocalBusiness": ["name", "address"],
    "Person": ["name"],
    "SoftwareApplication": ["name", "applicationCategory", "operatingSystem"],
    "Event": ["name", "startDate", "location"],
    "HowTo": ["name", "step"],
    "Recipe": ["name", "recipeIngredient", "recipeInstructions"],
    "VideoObject": ["name", "thumbnailUrl", "uploadDate"],
}

RECOMMENDED = {
    "Organization": ["logo", "sameAs", "description"],
    "Product": ["aggregateRating", "review", "image"],
    "Article": ["dateModified", "image", "publisher"],
}


@dataclass
class SchemaReport:
    present: bool = False
    node_count: int = 0
    types: List[str] = field(default_factory=list)
    errors: List[Dict[str, str]] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    same_as: List[str] = field(default_factory=list)
    entity_ids: List[str] = field(default_factory=list)
    knows_about: List[str] = field(default_factory=list)

    @property
    def valid_nodes(self) -> int:
        return max(self.node_count - len({e["node"] for e in self.errors}), 0)


def _nodes(obj: Any) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    if isinstance(obj, dict):
        if "@graph" in obj and isinstance(obj["@graph"], list):
            for node in obj["@graph"]:
                out.extend(_nodes(node))
        else:
            out.append(obj)
        # nested entities under known containers
        for key in ("mainEntity", "itemListElement", "offers", "acceptedAnswer", "author", "publisher"):
            if key in obj:
                out.extend(_nodes(obj[key]))
    elif isinstance(obj, list):
        for item in obj:
            out.extend(_nodes(item))
    return out


def analyze(jsonld_blocks: List[str]) -> SchemaReport:
    report = SchemaReport(present=bool(jsonld_blocks))
    for raw in jsonld_blocks:
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as exc:
            report.errors.append({"node": raw[:40], "message": f"invalid JSON: {exc.msg}"})
            continue
        for node in _nodes(obj):
            report.node_count += 1
            types = node.get("@type")
            type_list = [types] if isinstance(types, str) else list(types or [])
            for t in type_list:
                if t not in report.types:
                    report.types.append(t)
                for prop in REQUIRED.get(t, []):
                    if prop not in node:
                        report.errors.append({"node": t, "message": f"missing required property: {prop}"})
                for prop in RECOMMENDED.get(t, []):
                    if prop not in node:
                        report.warnings.append(f"{t} missing recommended property: {prop}")
            if isinstance(node.get("sameAs"), list):
                report.same_as.extend(str(x) for x in node["sameAs"])
            elif isinstance(node.get("sameAs"), str):
                report.same_as.append(node["sameAs"])
            if node.get("@id"):
                report.entity_ids.append(str(node["@id"]))
            ka = node.get("knowsAbout")
            if isinstance(ka, list):
                report.knows_about.extend(str(x) for x in ka)
            elif isinstance(ka, str):
                report.knows_about.append(ka)
    report.types = sorted(set(report.types))
    report.same_as = sorted(set(report.same_as))
    return report


def signals(report: SchemaReport) -> Dict[str, Any]:
    return {
        "present": report.present,
        "types": report.types,
        "node_count": report.node_count,
        "errors": report.errors,
        "warnings": report.warnings,
        "same_as_count": len(report.same_as),
        "same_as": report.same_as[:20],
        "knows_about": report.knows_about[:20],
    }
