---
name: travel-reviews
id: doddle.travel.reviews
version: 1.0.0
blueprint: ./blueprint.yaml
description: Capture post-trip reviews, referrals, loyalty. Use when trips complete and proof thin, or repeat bookings flat. For leisure UGC and corporate program feedback.
---

# Travel Reviews

Ask → publish → refer → rebook. Reviews flywheel + loyalty gap close.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Trips end with no review captured
- Referrals ad-hoc, group leaders unrewarded
- Loyalty points expire unused, status gaps unknown
- Corporate program lacks traveler feedback loop

## Initial Assessment

1. **Base**
   - Trips completed? Guest list + contacts?
   - Review platforms (Google, TripAdvisor, OTA)?
2. **Goal**
   - Reviews, referrals, or rebooks priority?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| trip_ref | string | yes | Completed trip(s); ask if missing |
| motion | string | no | leisure or corporate; default leisure |
| platform | string | no | Review target; infer if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Review plan, referral offer, loyalty audit |
| action_list | json | Asks with owner + timing |

---

## Core Framework

### Step 1: Ask
Checkout + 48h post-return + expense approval moments.

### Step 2: Publish
Route: property, experience, OTA; respond <48h all.

### Step 3: Convert
Referral give-get + loyalty gap + rebook nudge.

---

## Detailed Guidance

### Ask Moments

**Checklist:**
- [ ] Checkout QR + 48h email/SMS (leisure)
- [ ] Expense approval ping (corporate traveler)
- [ ] Group leader personal ask (highest yield)

### Reviews + Response

**Checklist:**
- [ ] Photo prompt (room, view, food) with ask
- [ ] Negative → private recovery before public reply
- [ ] All reviews answered <48h, keywords natural

### Referral + Loyalty

**Checklist:**
- [ ] Give-get credit per booking, group-leader bonus
- [ ] Points audit: balances, expiry, status gap
- [ ] Rebook nudge: same season next year, early rate

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Ask once at checkout | Lowest response | 3 moments |
| No leader reward | Groups leak | Pay the organizer |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Ignore negatives | Rating slides | Recover + reply |
| Points expire | Free money lost | Expiry alerts |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Count reviews only | No revenue link | Track rebooks |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Review velocity | New / mo | Growing | Listings |
| Rating | Avg stars | >4.5 | Google/OTA |
| Referral share | Bookings referred | >15% | CRM |
| Repeat rate | Rebooks / trips | Growing | CRM |
| Points rescued | Expiry avoided $ | Tracked | Loyalty |

---

## Decision Tree

No reviews → 3-moment asks first. Rating <4.3 → fix + reply before scaling. Flat repeats → loyalty gap + nudge.

---

## Quick Assessment Checklist

1. [ ] Completed trips?
2. [ ] Platforms?
3. [ ] Leader contacts?
4. [ ] Loyalty programs?
5. [ ] Corporate feedback path?

---

## Expected Output Format

### Review Plan
[Asks, routing, responses]

### Growth
[Referral, loyalty, rebook]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Ask fatigue | Same guests spammed | Cap 2 asks/trip |
| Unanswered negatives | Trust drop | 48h SLA |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Guest + leader lists | Contacts | no |
| doddle.tool.v1.gsc.getSearchAnalytics | Review impact | Branded queries | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| email-wizard | Post-trip sequences | Ask automation |
| copywriter | Review replies | Response copy |
| researcher | Theme mining | Feedback analysis |

---

## Related Skills

- **travel-booking**: Trip source
- **local-reviews**: Review mechanics depth
- **referral-program**: Flywheel mechanics

---

## Questions to Ask

1. Which completed trips?
2. Platforms to target?
3. Referral or rebook priority?
