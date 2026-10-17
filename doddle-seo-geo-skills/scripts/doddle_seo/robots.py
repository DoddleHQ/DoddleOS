"""robots.txt parsing and AI-crawler access evaluation (RFC 9309 subset).

Supports: user-agent groups, Allow/Disallow with ``*`` and ``$``, longest-match wins,
empty Disallow means all allowed, and Sitemap discovery.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from . import crawlers as registry


@dataclass
class Group:
    agents: List[str] = field(default_factory=list)
    rules: List[Tuple[bool, str]] = field(default_factory=list)  # (allow?, path)


@dataclass
class Robots:
    groups: List[Group] = field(default_factory=list)
    sitemaps: List[str] = field(default_factory=list)
    raw: str = ""

    def group_for(self, ua: str) -> Optional[Group]:
        ua_l = (ua or "").lower()
        best: Optional[Group] = None
        best_len = -1
        star: Optional[Group] = None
        for g in self.groups:
            for a in g.agents:
                a_l = a.lower()
                if a_l == "*":
                    star = star or g
                elif a_l in ua_l or ua_l in a_l:
                    if len(a_l) > best_len:
                        best, best_len = g, len(a_l)
        return best or star

    def allows(self, path: str, ua: str) -> Optional[bool]:
        """True allowed, False blocked, None if no robots group applies."""
        group = self.group_for(ua)
        if group is None:
            return None
        if not group.rules:
            return True
        path_only = path or "/"
        winner: Optional[Tuple[bool, int]] = None  # (allow, specificity)
        for allow, pattern in group.rules:
            if _matches(pattern, path_only):
                spec = len(pattern.replace("*", "").replace("$", ""))
                if winner is None or spec > winner[1]:
                    winner = (allow, spec)
        return winner[0] if winner else True


def _matches(pattern: str, path: str) -> bool:
    if pattern == "":
        return True
    anchored_end = pattern.endswith("$")
    core = pattern[:-1] if anchored_end else pattern
    regex = "^" + ".*".join(re.escape(part) for part in core.split("*"))
    if anchored_end:
        regex += "$"
    return re.search(regex, path) is not None


def parse(text: str) -> Robots:
    robots = Robots(raw=text or "")
    current: Optional[Group] = None
    pending_agents: List[str] = []
    in_group = False
    for raw_line in (text or "").splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        field_name, _, value = line.partition(":")
        field_name = field_name.strip().lower()
        value = value.strip()
        if field_name == "user-agent":
            if in_group and current is not None and current.rules:
                # A new agent after rules starts a new group only if agents already closed.
                current = None
                pending_agents = []
            pending_agents.append(value)
            in_group = False
        elif field_name in ("allow", "disallow"):
            if current is None:
                current = Group(agents=pending_agents or ["*"])
                robots.groups.append(current)
                pending_agents = []
            current.rules.append((field_name == "allow", value))
            in_group = True
        elif field_name == "sitemap":
            robots.sitemaps.append(value)
        elif field_name == "crawl-delay":
            continue
    return robots


def evaluate(text: str, base_path: str = "/") -> Dict[str, object]:
    """Return per-AI-crawler access and the sitemaps declared."""
    robots = parse(text)
    entries: List[Dict[str, object]] = []
    for c in registry.UNIQUE_CRAWLERS:
        allowed = robots.allows(base_path, c.token)
        entries.append(
            {
                "id": c.id,
                "token": c.token,
                "operator": c.operator,
                "kind": c.kind,
                "allowed": allowed,
                "note": c.note,
            }
        )
    blocked = [e for e in entries if e["allowed"] is False]
    return {
        "present": bool((text or "").strip()),
        "groups": len(robots.groups),
        "sitemaps": robots.sitemaps,
        "crawlers": entries,
        "blocked_count": len(blocked),
        "blocked_search": [e["token"] for e in blocked if e["kind"] == "search"],
        "blocked_training": [e["token"] for e in blocked if e["kind"] == "training"],
    }
