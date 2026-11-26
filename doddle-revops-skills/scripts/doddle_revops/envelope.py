"""Versioned evidence envelopes for drev."""

from __future__ import annotations

import datetime as dt
from typing import Any, Dict, Optional

from . import DATA_VERSION, SCORING_VERSION, TOOLKIT_NAME, TOOLKIT_VERSION

CURRENT = "CURRENT"


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def make_envelope(
    command: str,
    target: str,
    *,
    ok: bool = True,
    evidence_stamp: str = CURRENT,
    metrics: Optional[Dict[str, Any]] = None,
    inputs: Optional[Dict[str, Any]] = None,
    rows: Optional[list] = None,
    missing: Optional[list] = None,
    notes: Optional[list] = None,
    error: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    return {
        "ok": ok,
        "tool": TOOLKIT_NAME,
        "command": command,
        "target": target,
        "generated_at": utc_now(),
        "toolkit_version": TOOLKIT_VERSION,
        "scoring_version": SCORING_VERSION,
        "data_version": DATA_VERSION,
        "evidence": {"stamp": evidence_stamp},
        "metrics": metrics or {},
        "inputs": inputs or {},
        "rows": rows or [],
        "completeness": {"missing": missing or []},
        "notes": notes or [],
        "error": error,
    }
