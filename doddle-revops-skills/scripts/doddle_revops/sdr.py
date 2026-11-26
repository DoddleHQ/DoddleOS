"""Evidence gate for AI-SDR personalization claims (Stage 3)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from .envelope import make_envelope
from .io import load_rows, parse_date, pick


def validate_sdr_claims(
    *,
    account_path: str,
    evidence_path: str,
) -> Dict[str, Any]:
    try:
        account = json.loads(Path(account_path).read_text(encoding="utf-8"))
        evidence_rows, snapshot = load_rows(evidence_path)
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "sdr-validate", account_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load SDR inputs: {exc}",
                   "hint": "Provide an account JSON with claims[] and an evidence file (JSON/CSV) with id, source, fact."},
        )

    profile = account.get("account", account) if isinstance(account, dict) else {}
    domain = str(profile.get("domain") or "").strip().lower()
    claims = account.get("claims", []) if isinstance(account, dict) else []

    evidence_by_id: Dict[str, Dict[str, Any]] = {}
    for row in evidence_rows:
        evidence_id = str(pick(row, "id", "evidence_id") or "").strip()
        if not evidence_id:
            continue
        domains = pick(row, "domains", "domain", "account_domains")
        if isinstance(domains, str):
            domains = [d.strip().lower() for d in domains.split(",") if d.strip()]
        elif domains is None:
            domains = []
        else:
            domains = [str(d).strip().lower() for d in domains]
        observed = parse_date(pick(row, "observed_at", "date", "seen_at"))
        evidence_by_id[evidence_id] = {
            "id": evidence_id,
            "source": pick(row, "source", "url", "origin"),
            "fact": pick(row, "fact", "text", "observation"),
            "domains": domains,
            "observed_at": observed.isoformat() if observed else None,
        }

    rows: List[Dict[str, Any]] = []
    supported = 0
    for claim in claims:
        text = str(claim.get("text", "")).strip()
        evidence_id = str(claim.get("evidence_id", "")).strip()
        record = evidence_by_id.get(evidence_id)
        reasons: List[str] = []
        if record is None:
            reasons.append("no evidence with this id")
        else:
            if not record["fact"]:
                reasons.append("evidence has no fact")
            if record["domains"] and domain and domain not in record["domains"]:
                reasons.append("evidence is not for this account domain")
            if record["observed_at"] is None:
                reasons.append("evidence has no observation date")
        ok = not reasons
        if ok:
            supported += 1
        rows.append({
            "claim": text,
            "evidence_id": evidence_id,
            "supported": ok,
            "reason": "; ".join(reasons) if reasons else "supported by supplied evidence",
            "source": record["source"] if record else None,
            "observed_at": record["observed_at"] if record else None,
        })

    total = len(rows)
    unsupported = total - supported
    return make_envelope(
        "sdr-validate", account_path,
        metrics={
            "claims": total,
            "supported": supported,
            "unsupported": unsupported,
            "coverage": round(supported / total, 4) if total else None,
            "evidence_records": len(evidence_by_id),
            "stale_evidence": sum(1 for r in evidence_by_id.values() if r["observed_at"] is None),
        },
        inputs={"account": account_path, "evidence": evidence_path, "domain": domain or None},
        rows=rows,
        missing=["evidence"] if unsupported else [],
        notes=["unsupported claims must be removed before the copy is sent — no fabrication"]
        if unsupported else [],
    )
