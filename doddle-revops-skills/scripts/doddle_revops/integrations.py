"""Integration-led growth readiness audit (Stage 9)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from .envelope import make_envelope
from .io import load_rows, parse_date, pick


def audit_integrations(*, catalog_path: str) -> Dict[str, Any]:
    try:
        catalog = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "integration-audit", catalog_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load integration catalog: {exc}",
                   "hint": "Provide a JSON catalog with integrations[]."},
        )

    integrations = catalog.get("integrations", []) if isinstance(catalog, dict) else []
    rows: List[Dict[str, Any]] = []
    ready = 0
    for entry in integrations:
        name = str(entry.get("name", "unnamed"))
        kind = str(entry.get("type", "native"))
        oauth_scopes = entry.get("oauth_scopes", []) or []
        webhooks = entry.get("webhooks", []) or []
        events = entry.get("events", []) or []
        listing = entry.get("listing", {}) or {}
        co_sell = entry.get("co_sell", {}) or {}
        owner = entry.get("owner")

        checks: Dict[str, bool] = {
            "owner_assigned": bool(owner),
            "has_oauth_scopes": bool(oauth_scopes) or kind in {"native", "partner"},
            "has_webhook_coverage": bool(webhooks) or bool(events),
            "listing_complete": bool(listing.get("status") and listing.get("url")),
            "co_sell_fields_present": bool(co_sell.get("fields")) or kind in {"partner"},
            "documented": bool(entry.get("docs_url")),
        }
        failures = [name for name, ok in checks.items() if not ok]
        score = round(100.0 * sum(checks.values()) / len(checks), 1)
        if not failures:
            ready += 1
        rows.append({
            "integration": name,
            "type": kind,
            "readiness_score": score,
            "checks": checks,
            "failures": failures,
            "oauth_scopes": len(oauth_scopes),
            "webhooks": len(webhooks),
            "events": len(events),
            "listing_status": listing.get("status"),
            "owner": owner,
        })

    rows.sort(key=lambda r: r["readiness_score"])
    return make_envelope(
        "integration-audit", catalog_path,
        metrics={
            "integrations": len(rows),
            "ready": ready,
            "not_ready": len(rows) - ready,
            "average_readiness": round(sum(r["readiness_score"] for r in rows) / len(rows), 1) if rows else None,
        },
        inputs={"catalog": catalog_path},
        rows=rows,
        missing=[],
        notes=["readiness is a checklist result, not a go-to-market decision"] if rows else [],
    )
