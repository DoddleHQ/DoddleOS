"""Deterministic weighted scoring for ICP definitions and account lists.

A score is a weighted mean of 0-100 attribute scores. Criteria weight the attributes; weights
are normalised over the criteria that were actually scored, so a missing attribute lowers the
coverage rather than the score. Same inputs -> same score.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


def _clamp(v: float) -> float:
    return max(0.0, min(100.0, v))


def score_attributes(criteria: List[Dict[str, Any]], target: str = "target") -> Dict[str, Any]:
    """Score one target.

    ``criteria`` is ``[{"name", "weight", "score"}]`` where ``score`` is 0-100 (or ``None`` if
    unmeasured). Returns a weighted score, coverage and the per-criterion contributions.
    """
    rows: List[Dict[str, Any]] = []
    earned = 0.0
    weight_total = 0.0
    weight_measured = 0.0
    for c in criteria:
        name = str(c.get("name", "?"))
        weight = float(c.get("weight") or 0)
        raw = c.get("score")
        s = None if raw is None else _clamp(float(raw))
        contribution = None if s is None else s * weight
        rows.append({"name": name, "weight": weight, "score": s, "contribution": contribution})
        weight_total += weight
        if s is not None:
            earned += contribution
            weight_measured += weight
    composite = round(earned / weight_measured, 1) if weight_measured else None
    coverage = round(weight_measured / weight_total, 4) if weight_total else None
    return {
        "target": target,
        "criteria": rows,
        "composite": composite,
        "coverage": coverage,
        "missing": [r["name"] for r in rows if r["score"] is None],
        "weight_total": weight_total,
    }


def score_accounts(criteria: List[Dict[str, Any]], weight_key: str = "weight") -> Dict[str, Any]:
    """Score a list of accounts.

    ``criteria`` is ``[{"name", <weight>, "score"}]`` for a single account OR
    ``[{"name", "weights": {account: w}, "scores": {account: s}}]``. This helper handles the
    simple flat list (one weighted score per criterion applied to one account); for many
    accounts, call :func:`score_attributes` per account.
    """
    return score_attributes(criteria)
