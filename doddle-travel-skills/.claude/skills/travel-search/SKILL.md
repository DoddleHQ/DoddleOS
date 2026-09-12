---
name: travel-search
id: doddle.travel.search
version: 1.0.0
blueprint: ./blueprint.yaml
description: Compare flights, stays, activities on price + policy + loyalty. Use when planning leisure trips or corporate travel, or when fares/policies unclear. For day plans, see travel-itinerary. For holds and tickets, see travel-booking.
---

# Travel Search

Shortlist engine: leisure flex + corporate policy in one compare. Never fabricate prices — rank on rules, mark live fares NOT AVAILABLE without booking access.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Leisure: dates flexible, budget band set, vibe undecided
- Corporate: class caps, preferred carriers, refundability mandated
- Comparing options across providers with different fee/policy terms
- Loyalty earn/burn changes the math

## Initial Assessment

1. **Trip**
   - Leisure or corporate? Travelers, dates (±flex?), origin/dest?
   - Budget band + must-haves (nonstop, bags, cancellation)?
2. **Policy (corporate)**
   - Class cap? Preferred carriers/hotels? Approval needed over $X?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| origin_dest | string | yes | Origin + destination(s); ask if missing |
| dates_party | string | yes | Dates (±flex) + travelers; ask if missing |
| motion | string | no | leisure or corporate; default leisure |
| budget_band | string | no | Per-person cap; infer if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Ranked shortlist with trade-off table |
| action_list | json | Next steps (verify fares, holds, approvals) |

---

## Core Framework

### Step 1: Constrain
Dates/party/budget + corporate guardrails. Kill bad-fit early.

### Step 2: Compare
Total cost (fees, bags, seats) + terms (changes, refunds) + loyalty earn.

### Step 3: Shortlist
Top 3 ranked with why + what to verify live before paying.

---

## Detailed Guidance

### Leisure Search

**Checklist:**
- [ ] Flex window (±3 days) scanned for fare drops
- [ ] Total cost incl. bags, seats, transfers — not base fare
- [ ] Cancellation terms noted per option
- [ ] Loyalty earn vs cheaper off-program trade-off stated

### Corporate Search

**Checklist:**
- [ ] Class cap + preferred carrier/hotel applied first
- [ ] Refundable/changeable default for volatile schedules
- [ ] Cost-center tag + approval threshold flagged
- [ ] Status-safe option listed alongside cheapest

### Compare Rules

**Checklist:**
- [ ] No invented prices — ranges + verify links, else NOT AVAILABLE
- [ ] Rain/disruption alternative noted for key legs
- [ ] Visa/docs impact on routing (transit visas) checked

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Base-fare ranking | Fees eclipse savings | Total-cost compare |
| Ignore policy | Rejected expense | Guardrails first |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Fake live fares | Hallucinated prices | Ranges + verify |
| One option only | No fallback | Top 3 always |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Loyalty ignored | Real money left | Earn/burn line per option |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Policy fit | Options inside guardrails | 100% corp | Manual |
| Total-cost delta | Cheapest vs recom. | Stated | Manual |
| Verify rate | Shortlist verified live | 100% pre-book | Manual |

---

## Decision Tree

Corporate → policy filter before ranking. Flexible dates → flex scan first. No live access → ranges + verify links, never exact fares.

---

## Quick Assessment Checklist

1. [ ] Leisure or corporate?
2. [ ] Origin, dest, dates, party?
3. [ ] Budget + must-haves?
4. [ ] Policy caps (corp)?
5. [ ] Live booking access or manual?

---

## Expected Output Format

### Shortlist
[Top 3, trade-offs, loyalty]

### Verify List
[What to check live + approvals]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Price hallucination | Exact fares, no source | NOT AVAILABLE + ranges |
| Policy breach | Rejected trip | Re-filter, resubmit |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.dataforseo.serpGoogle | Route demand signals | SERP, carriers | no |
| doddle.tool.v1.hubspot.contacts | Corp traveler history | Prior trips, prefs | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | Route + provider intel | Options, policies |
| planner | Shortlist sequencing | Ranking logic |
| copywriter | Stakeholder summary | Approval one-pager |

---

## Related Skills

- **travel-itinerary**: Day plans from shortlist
- **travel-booking**: Holds + tickets
- **travel-support**: Docs + disruption

---

## Questions to Ask

1. Leisure or corporate, party + dates?
2. Budget band + must-haves?
3. Policy caps (if corporate)?
