---
name: travel-itinerary
id: doddle.travel.itinerary
version: 1.0.0
blueprint: ./blueprint.yaml
description: Build day plans (leisure) and trip chains (corporate) with routing + buffers. Use when shortlist chosen and plan needed, or multi-city travel unclear. For search, see travel-search. For tickets, see travel-booking.
---

# Travel Itinerary

Pace + routing + backups. Leisure 1-2 anchors/day; corporate buffers + red-eye rules.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Leisure: days unplanned, overstuffed, or transit-heavy
- Corporate: multi-city chain, meeting buffers, overnight rules
- Rain/disruption risk with no plan B
- Group with mixed pace needs

## Initial Assessment

1. **Frame**
   - Days, base(s), pace (packed vs relaxed)?
   - Corporate: meetings fixed? Red-eyes allowed?
2. **Constraints**
   - Mobility, food, budget per day? Must-see list?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| destination_dates | string | yes | Place(s) + dates; ask if missing |
| party_style | string | no | Party + pace; default 2 relaxed |
| motion | string | no | leisure or corporate; default leisure |
| must_see | string | no | Non-negotiable stops |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Day-by-day plan with routing + backups |
| action_list | json | Bookings to make + docs to prep |

---

## Core Framework

### Step 1: Anchor
1-2 anchors/day leisure; meetings first corporate.

### Step 2: Route
Transit times real, food/rest buffers, cluster by area.

### Step 3: Back Up
Rain/disruption alternative per day + booking links to verify.

---

## Detailed Guidance

### Leisure Days

**Checklist:**
- [ ] Area-clustered stops, no zigzag
- [ ] Buffer: lunch + rest daily, kids/elderly slower
- [ ] Pre-book timed entries; free windows for wander
- [ ] Dining holds flagged → `restaurant-reservations` pattern

### Corporate Chains

**Checklist:**
- [ ] Meeting buffers ≥60 min same-city, 3h+ connections
- [ ] Backup flight per critical leg
- [ ] Hotel near first meeting, late checkout if red-eye
- [ ] Per-diem + ground transport pre-cleared

### Shared

**Checklist:**
- [ ] Transit time per move stated
- [ ] Packing/docs checklist per leg
- [ ] Emergency contacts + insurance note

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| 5 stops/day | Exhaustion, misses | 1-2 anchors |
| No buffer | One delay cascades | 30% slack |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Back-to-back cities, no night | Burnout | 2-night minimum leisure |
| Red-eye before keynote | Performance hit | Arrive night prior |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Transit guessed | Missed slots | Verify durations |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Anchors/day | Planned mains | ≤2 leisure | Manual |
| Buffer share | Unplanned time | ≥25% | Manual |
| Backup coverage | Days with plan B | 100% | Manual |

---

## Decision Tree

Fixed meetings → build around them. Rain season → indoor alternatives first. Mixed pace → split tracks, shared meals.

---

## Quick Assessment Checklist

1. [ ] Dest + dates?
2. [ ] Pace + mobility?
3. [ ] Must-sees?
4. [ ] Corporate rules?
5. [ ] Booking access?

---

## Expected Output Format

### Day Plan
[Days, anchors, transit, food]

### Book Now
[Timed entries, holds, backups]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Overstuffed | No rest | Cut lowest-value stop |
| No plan B | Rain ruins day | Indoor swap list |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.dataforseo.serpGoogle | Stop validation | Hours, closures | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| planner | Day sequencing | Routing logic |
| researcher | Hours, closures | Fact checks |
| copywriter | Shareable version | Guest-ready plan |

---

## Related Skills

- **travel-search**: Shortlist input
- **travel-booking**: Ticket the plan
- **travel-support**: Docs + disruption

---

## Questions to Ask

1. Destination + dates + party?
2. Pace + must-sees?
3. Corporate constraints?
