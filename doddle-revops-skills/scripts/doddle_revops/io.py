"""Shared JSON/CSV loaders and freshness helpers."""

from __future__ import annotations

import csv
import datetime as dt
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def load_rows(path: str) -> Tuple[List[Dict[str, Any]], Optional[str]]:
    """Load JSON array/object or CSV. Returns rows plus an optional snapshot timestamp."""
    p = Path(path)
    raw = p.read_text(encoding="utf-8")
    snapshot = None
    if p.suffix.lower() == ".csv":
        return [dict(r) for r in csv.DictReader(raw.splitlines())], snapshot
    if p.suffix.lower() == ".jsonl":
        return [json.loads(line) for line in raw.splitlines() if line.strip()], snapshot
    data = json.loads(raw)
    if isinstance(data, dict):
        for key in ("snapshot_at", "exported_at", "generated_at", "as_of"):
            if data.get(key):
                snapshot = str(data[key])
                break
        for key in ("rows", "items", "data", "records", "deals", "touchpoints", "events", "accounts"):
            if isinstance(data.get(key), list):
                return data[key], snapshot
        return [data], snapshot
    if isinstance(data, list):
        return data, snapshot
    raise ValueError("input must be a JSON array/object or CSV")


def parse_date(value: Any) -> Optional[dt.datetime]:
    if value in (None, ""):
        return None
    text = str(value).strip().replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        try:
            parsed = dt.datetime.combine(dt.date.fromisoformat(text[:10]), dt.time())
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def file_freshness(path: str, max_age_days: int) -> Tuple[str, Optional[float]]:
    mtime = dt.datetime.fromtimestamp(Path(path).stat().st_mtime, tz=dt.timezone.utc)
    age_days = max(0.0, (dt.datetime.now(dt.timezone.utc) - mtime).total_seconds() / 86400.0)
    return ("CURRENT" if age_days <= max_age_days else "STALE"), round(age_days, 2)


def snapshot_freshness(snapshot: Optional[str], max_age_days: int) -> Tuple[str, Optional[float]]:
    parsed = parse_date(snapshot)
    if not parsed:
        return "UNKNOWN", None
    age_days = max(0.0, (dt.datetime.now(dt.timezone.utc) - parsed).total_seconds() / 86400.0)
    return ("CURRENT" if age_days <= max_age_days else "STALE"), round(age_days, 2)


def as_float(value: Any) -> Optional[float]:
    if value in (None, ""):
        return None
    try:
        return float(str(value).replace(",", "").replace("$", ""))
    except ValueError:
        return None


def as_int(value: Any) -> Optional[int]:
    number = as_float(value)
    return int(number) if number is not None else None


def pick(row: Dict[str, Any], *keys: str) -> Any:
    for key in keys:
        for candidate in row:
            if candidate.lower().strip() == key:
                return row[candidate]
    return None
