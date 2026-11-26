"""Read-only warehouse, dbt, identity, and reverse-ETL profiling."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import DATA_VERSION, SCORING_VERSION, TOOLKIT_VERSION
from .envelope import make_envelope
from .io import as_float, as_int, file_freshness, load_rows, parse_date, pick, snapshot_freshness


def _load_json(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _table_rows(export: Any) -> List[Dict[str, Any]]:
    if isinstance(export, list):
        return [r for r in export if isinstance(r, dict)]
    if isinstance(export, dict):
        for key in ("tables", "rows", "items", "data", "records"):
            if isinstance(export.get(key), list):
                return [r for r in export[key] if isinstance(r, dict)]
        return [export]
    return []


def _column_count(table: Dict[str, Any]) -> Optional[int]:
    columns = table.get("columns")
    if isinstance(columns, list):
        return len(columns)
    if isinstance(columns, dict):
        return len(columns)
    return as_int(table.get("column_count"))


def profile_data_infrastructure(
    *,
    warehouse_export: str,
    dbt_manifest: Optional[str] = None,
    identity_map: Optional[str] = None,
    reverse_etl_config: Optional[str] = None,
    max_age_days: int = 30,
) -> Dict[str, Any]:
    notes: List[str] = []
    missing: List[str] = []
    try:
        export = _load_json(warehouse_export)
    except Exception as exc:  # noqa: BLE001 - surfaced in envelope
        return make_envelope(
            "data-profile", warehouse_export, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not read warehouse export: {exc}",
                   "hint": "Provide a JSON object with a tables[] array or a JSON array of table profiles."},
        )

    file_stamp, file_age = file_freshness(warehouse_export, max_age_days)
    snapshot = None
    if isinstance(export, dict):
        snapshot = export.get("snapshot_at") or export.get("exported_at") or export.get("as_of")
    snap_stamp, snap_age = snapshot_freshness(str(snapshot) if snapshot else None, max_age_days)
    evidence_stamp = "STALE" if "STALE" in (file_stamp, snap_stamp) else file_stamp
    if evidence_stamp == "STALE":
        notes.append(f"warehouse export is older than {max_age_days} days; refresh before treating it as current")

    tables = _table_rows(export)
    table_rows: List[Dict[str, Any]] = []
    for table in tables:
        name = str(table.get("name") or table.get("table") or table.get("table_name") or "unnamed")
        updated = table.get("updated_at") or table.get("last_refreshed") or table.get("snapshot_at")
        table_stamp, table_age = snapshot_freshness(str(updated) if updated else None, max_age_days)
        row_count = as_int(table.get("row_count") or table.get("rows"))
        columns = _column_count(table)
        owner = table.get("owner") or table.get("data_owner")
        primary_key = table.get("primary_key") or table.get("primary_keys")
        authoritative = table.get("authoritative", table.get("source_of_truth"))
        destinations = table.get("destinations") or table.get("reverse_etl_destinations") or []
        if isinstance(destinations, str):
            destinations = [d.strip() for d in destinations.split(",") if d.strip()]
        status = "ready"
        if table_stamp == "STALE":
            status = "stale"
        elif not owner or not primary_key or authoritative in (None, False, "false", "unknown"):
            status = "incomplete"
        table_rows.append({
            "table": name,
            "row_count": row_count,
            "column_count": columns,
            "owner": owner,
            "primary_key": primary_key,
            "authoritative": authoritative,
            "destinations": destinations,
            "freshness": table_stamp,
            "age_days": table_age,
            "status": status,
        })

    dbt_summary: Dict[str, Any] = {"available": False}
    if dbt_manifest:
        try:
            manifest = _load_json(dbt_manifest)
            nodes = manifest.get("nodes", {}) if isinstance(manifest, dict) else {}
            sources = manifest.get("sources", {}) if isinstance(manifest, dict) else {}
            tests = manifest.get("tests", manifest.get("data_tests", {})) if isinstance(manifest, dict) else {}
            model_nodes = [n for n in nodes.values() if isinstance(n, dict) and n.get("resource_type") == "model"]
            undocumented = [n.get("name", "unnamed") for n in model_nodes if not n.get("description")]
            dbt_summary = {
                "available": True,
                "models": len(model_nodes),
                "sources": len(sources),
                "tests": len(tests),
                "undocumented_models": undocumented,
            }
        except Exception as exc:  # noqa: BLE001
            dbt_summary = {"available": False, "error": str(exc)}
            missing.append("dbt_manifest")
    else:
        missing.append("dbt_manifest")

    identity_summary: Dict[str, Any] = {"available": False}
    if identity_map:
        try:
            rows, snap = load_rows(identity_map)
            total = len(rows)
            canonical = [r for r in rows if pick(r, "canonical_id", "master_id", "unified_id")]
            low_conf = [r for r in rows if (as_float(pick(r, "confidence", "match_confidence")) or 0) < 0.8]
            identity_summary = {
                "available": True,
                "records": total,
                "canonical_matches": len(canonical),
                "match_rate": round(len(canonical) / total, 4) if total else None,
                "low_confidence": len(low_conf),
                "freshness": snapshot_freshness(snap, max_age_days)[0],
            }
        except Exception as exc:  # noqa: BLE001
            identity_summary = {"available": False, "error": str(exc)}
            missing.append("identity_map")
    else:
        missing.append("identity_map")

    reverse_summary: Dict[str, Any] = {"available": False}
    if reverse_etl_config:
        try:
            config = _load_json(reverse_etl_config)
            syncs = config.get("syncs", config.get("models", [])) if isinstance(config, dict) else []
            if isinstance(syncs, dict):
                syncs = list(syncs.values())
            enabled = [s for s in syncs if isinstance(s, dict) and s.get("enabled", True)]
            destinations = sorted({str(s.get("destination") or s.get("model") or "unknown") for s in enabled})
            reverse_summary = {
                "available": True,
                "syncs": len(syncs),
                "enabled_syncs": len(enabled),
                "destinations": destinations,
                "unconfigured_syncs": [s.get("name", "unnamed") for s in enabled if not s.get("destination") and not s.get("model")],
            }
        except Exception as exc:  # noqa: BLE001
            reverse_summary = {"available": False, "error": str(exc)}
            missing.append("reverse_etl_config")
    else:
        missing.append("reverse_etl_config")

    ready_tables = sum(1 for t in table_rows if t["status"] == "ready")
    table_coverage = round(ready_tables / len(table_rows), 4) if table_rows else None
    identity_coverage = identity_summary.get("match_rate") if identity_summary.get("available") else None
    reverse_coverage = 1.0 if reverse_summary.get("available") and not reverse_summary.get("unconfigured_syncs") else 0.0 if reverse_summary.get("available") else None
    components = [v for v in (table_coverage, identity_coverage, reverse_coverage) if v is not None]
    readiness = round(100.0 * sum(components) / len(components), 1) if components else None

    return make_envelope(
        "data-profile", warehouse_export,
        evidence_stamp=evidence_stamp,
        metrics={
            "readiness_score": readiness,
            "table_count": len(table_rows),
            "ready_tables": ready_tables,
            "total_rows": sum(t["row_count"] or 0 for t in table_rows),
            "identity_match_rate": identity_coverage,
            "reverse_etl_ready": reverse_coverage == 1.0 if reverse_coverage is not None else None,
        },
        inputs={
            "warehouse_export": warehouse_export,
            "warehouse_file_age_days": file_age,
            "warehouse_snapshot_age_days": snap_age,
            "dbt_manifest": dbt_manifest,
            "identity_map": identity_map,
            "reverse_etl_config": reverse_etl_config,
            "max_age_days": max_age_days,
        },
        rows=[
            {"kind": "table", **t} for t in table_rows
        ] + [
            {"kind": "dbt", **dbt_summary},
            {"kind": "identity", **identity_summary},
            {"kind": "reverse_etl", **reverse_summary},
        ],
        missing=missing,
        notes=notes,
    )
