---
name: travel-support
id: doddle.travel.support
version: 1.0.0
blueprint: ./blueprint.yaml
description: Handle disruption, visa/docs, expense for booked trips. Use when flights change, documents unclear, or corporate reconciliation pending. For rebooking leisure groups or T&E compliance.
---

# Travel Support

Disruption → docs → expense. Owner + deadline per item, fastest-safe rebook first.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Delays, cancellations, missed connections
- Visa, passport validity, entry forms uncertain
- Corporate expense + per-diem reconciliation open
- Group needs coordinator updates

## Initial Assessment

1. **Situation**
   - PNRs + what changed? Who is where now?
   - Deadline (meeting, cruise, check-in cutoff)?
2. **Docs/money**
   - Passports/visas verified per leg? Card used?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| booking_ref | string | yes | PNRs or trip summary; ask if missing |
| issue | string | yes | Disruption, docs, or expense; ask if missing |
| motion | string | no | leisure or corporate; default leisure |
| deadline | string | no | Must-arrive-by time |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Ranked options + docs checklist |
| action_list | json | Actions with owner + deadline |

---

## Core Framework

### Step 1: Stabilize
Fastest-safe rebook ranked; protect the deadline first.

### Step 2: Document
Visa/validity/forms per leg; block travel if red.

### Step 3: Settle
Receipts → per-diem vs actuals → reconciliation filed.

---

## Detailed Guidance

### Disruption

**Checklist:**
- [ ] Options ranked: fastest vs cheapest vs status-safe
- [ ] Airline rebook + self-rebook compared (refund risk)
- [ ] Hotel/transfer cascade adjusted, no orphan nights
- [ ] Group update sent once (single coordinator voice)

### Docs

**Checklist:**
- [ ] Passport 6-mo validity every leg incl. transit
- [ ] Visa / eTA / entry form per nationality per leg
- [ ] Vaccines + insurance cert where required
- [ ] Copies stored offline + shared

### Expense (corporate + group)

**Checklist:**
- [ ] Receipts captured daily, no shoebox
- [ ] Per-diem vs actuals per policy, overages flagged
- [ ] Corp card reconciled, personal reclaim filed
- [ ] Disruption costs tagged claimable

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Cheapest rebook only | Misses deadline | Fastest-safe first |
| Docs assumed | Denied boarding | Verify per leg |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| 5 updaters | Confusion | One coordinator |
| Receipts later | Lost 20% | Capture daily |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No claim | Money left | Tag claimables |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Rebook time | Issue → new confirm | <60 min | Manual |
| Doc block rate | Trips blocked pre-travel | 100% caught | Manual |
| Receipt capture | Same-day % | >90% | Expense |
| Claim recovery | Disruption $ back | 100% filed | Finance |

---

## Decision Tree

Deadline critical → fastest regardless of cost (note for claim). Docs red → stop, fix before anything. Group → one voice updates.

---

## Quick Assessment Checklist

1. [ ] PNRs + current positions?
2. [ ] Issue type + deadline?
3. [ ] Docs verified?
4. [ ] Card + policy (corp)?
5. [ ] Coordinator named?

---

## Expected Output Format

### Options
[Ranked rebook / docs status]

### Action Sheet
[Owner + deadline each]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Self-rebook voids refund | No recourse | Check fare rules first |
| Transit visa miss | Stranded | Verify every stop |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Traveler + approver ping | Contacts | no |
| doddle.tool.v1.dataforseo.serpGoogle | Entry-rule check | Visa, forms | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| continuity-specialist | Disruption comms | Recovery flow |
| researcher | Entry rules | Visa/docs facts |
| planner | Re-sequencing | New plan |

---

## Related Skills

- **travel-booking**: Original tickets
- **travel-itinerary**: Plan to repair
- **finance-reviews**: Expense depth

---

## Questions to Ask

1. PNRs + what changed?
2. Deadline to protect?
3. Docs verified per leg?
