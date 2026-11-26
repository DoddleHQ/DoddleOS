"""Signal routing (Stage 2) and community attribution (Stage 11)."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .envelope import make_envelope
from .io import as_float, load_rows, parse_date, pick


def route_signals(
    *,
    events_path: str,
    rules_path: str,
    now: Optional[dt.datetime] = None,
) -> Dict[str, Any]:
    try:
        events, snapshot = load_rows(events_path)
        rules = json.loads(Path(rules_path).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "route-signals", rules_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load routing inputs: {exc}",
                   "hint": "Provide events (JSONL/CSV) and a rules file (JSON) with routes[]."},
        )

    window_days = int(rules.get("recency_window_days", 14))
    reference = now or dt.datetime.now(dt.timezone.utc)
    window_start = reference - dt.timedelta(days=window_days)
    routes = {str(r.get("signal")): r for r in rules.get("routes", []) if r.get("signal")}

    entries: List[Dict[str, Any]] = []
    unrouted: Dict[str, int] = {}
    signals_seen = 0
    for event in events:
        signals_seen += 1
        signal = str(pick(event, "signal", "signal_type", "event_name", "type") or "").strip()
        occurred = parse_date(pick(event, "occurred_at", "event_at", "timestamp", "time"))
        if not signal:
            unrouted["<missing signal>"] = unrouted.get("<missing signal>", 0) + 1
            continue
        if not occurred or occurred < window_start or occurred > reference:
            continue
        route = routes.get(signal)
        if not route:
            unrouted[signal] = unrouted.get(signal, 0) + 1
            continue
        age_days = round((reference - occurred).total_seconds() / 86400.0, 2)
        priority = int(route.get("priority", 5))
        entries.append({
            "account_id": str(pick(event, "account_id", "account") or ""),
            "contact_id": str(pick(event, "contact_id", "lead_id") or ""),
            "signal": signal,
            "occurred_at": occurred.isoformat(),
            "age_days": age_days,
            "channel": route.get("channel", "unknown"),
            "owner": route.get("owner", "unassigned"),
            "priority": priority,
            "action": route.get("action", "review"),
        })

    entries.sort(key=lambda e: (e["priority"], -e["age_days"]))
    per_account: Dict[str, List[Dict[str, Any]]] = {}
    for entry in entries:
        per_account.setdefault(entry["account_id"], []).append(entry)

    for account_id, account_entries in per_account.items():
        best = account_entries[0]
        payload = {
            "text": (f"[{best['signal']}] {account_id or 'unknown account'} — "
                     f"{best['age_days']}d ago · route: {best['channel']} · owner: {best['owner']}"),
            "account_id": account_id,
            "signals": [e["signal"] for e in account_entries],
            "priority": best["priority"],
            "channel": best["channel"],
            "owner": best["owner"],
            "delivery": "dry-run — not sent",
        }
        best["slack_payload"] = payload

    return make_envelope(
        "route-signals", rules_path,
        metrics={
            "signals_seen": signals_seen,
            "signals_routed": len(entries),
            "signals_unrouted": sum(unrouted.values()),
            "accounts_routed": len(per_account),
            "window_days": window_days,
            "as_of": reference.isoformat(),
        },
        inputs={"events": events_path, "rules": rules_path, "recency_window_days": window_days},
        rows=entries,
        missing=list(unrouted.keys()),
        notes=[f"unrouted signal types: {unrouted}"] if unrouted else [],
    )


def community_attribution(
    *,
    community_path: str,
    surveys_path: str,
    deals_path: str,
    min_sample: int = 30,
) -> Dict[str, Any]:
    try:
        community, community_snapshot = load_rows(community_path)
        surveys, survey_snapshot = load_rows(surveys_path)
        deals, deals_snapshot = load_rows(deals_path)
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "community-attribution", deals_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load community inputs: {exc}",
                   "hint": "Provide community activity (CSV/JSON), survey responses (CSV/JSON), and deals (CSV/JSON)."},
        )

    members: Dict[str, Dict[str, Any]] = {}
    for row in community:
        person = str(pick(row, "person_id", "member_id", "contact_id") or "").strip()
        if not person:
            continue
        entry = members.setdefault(person, {"person_id": person, "activities": 0, "communities": set(), "dates": []})
        entry["activities"] += 1
        community_name = pick(row, "community", "space", "channel")
        if community_name:
            entry["communities"].add(str(community_name))
        occurred = parse_date(pick(row, "activity_date", "occurred_at", "date"))
        if occurred:
            entry["dates"].append(occurred.isoformat())

    self_reported: Dict[str, int] = {}
    modeled: Dict[str, int] = {}
    consented = 0
    missing_consent = 0
    for row in surveys:
        person = str(pick(row, "person_id", "contact_id") or "").strip()
        heard = pick(row, "heard_from", "how_did_you_hear", "attribution")
        other = pick(row, "other_source", "other", "secondary_source")
        consent = pick(row, "consent", "consent_to_use", "opted_in")
        if consent is None or str(consent).strip().lower() in {"", "unknown"}:
            missing_consent += 1
        else:
            consented += 1
        if heard:
            self_reported[str(heard)] = self_reported.get(str(heard), 0) + 1
        elif other:
            modeled[str(other)] = modeled.get(str(other), 0) + 1

    influenced = 0.0
    influenced_deals = 0
    won_from_community = 0
    community_deals = 0
    for deal in deals:
        person = str(pick(deal, "person_id", "contact_id", "lead_id") or "").strip()
        outcome = str(pick(deal, "outcome", "status", "result") or "").strip().lower()
        amount = as_float(pick(deal, "amount", "value")) or 0.0
        if person not in members:
            continue
        community_deals += 1
        if outcome in {"won", "closed won", "closed-won", "win"}:
            won_from_community += 1
            influenced += amount
            influenced_deals += 1

    sample = len(surveys)
    confidence = "low" if sample < min_sample else ("medium" if sample < min_sample * 3 else "high")
    return make_envelope(
        "community-attribution", deals_path,
        metrics={
            "community_members": len(members),
            "survey_responses": sample,
            "self_reported_sources": len(self_reported),
            "modeled_sources": len(modeled),
            "community_linked_deals": community_deals,
            "community_won_deals": influenced_deals,
            "influenced_revenue": round(influenced, 2),
            "consent_recorded": consented,
            "consent_missing": missing_consent,
            "confidence": confidence,
        },
        inputs={
            "community": community_path,
            "surveys": surveys_path,
            "deals": deals_path,
            "min_sample": min_sample,
        },
        rows=[{"kind": "source", "basis": "self_reported", "source": k, "count": v} for k, v in sorted(self_reported.items())]
             + [{"kind": "source", "basis": "modeled", "source": k, "count": v} for k, v in sorted(modeled.items())]
             + [{"kind": "member", "person_id": m["person_id"], "activities": m["activities"],
                 "communities": sorted(m["communities"])} for m in list(members.values())[:500]],
        missing=["consent"] if missing_consent else [],
        notes=[f"confidence is '{confidence}' because only {sample} survey responses were supplied"]
        if confidence == "low" else [],
    )
