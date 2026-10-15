---
name: b2b-linkedin
id: doddle.b2b.linkedin
version: 1.0.0
blueprint: ./blueprint.yaml
description: LinkedIn outbound that books: profile, warm engagement, DM sequences. Use for founder-led and AE prospecting.
---

# B2B LinkedIn

Profile converts, warmth unlocks, DM closes. Calls cold-email for angles.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- LinkedIn reply <5%
- New AE/founder motion
- Email-only stall

## Initial Assessment

1. **Offer**
   - ICP? Offer + proof?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| icp | string | yes | Titles + industries |
| offer | string | yes | Offer + proof |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| profile_pack | markdown | Headline + about + featured |
| sequence_pack | json | Connect + warm + DM steps |
| reply_playbook | markdown | Reply trees + handoff bar |

---

## Core Framework

### Step 1: Angles
Call `cold-email` for hooks using offer as brief.

### Step 2: Warm
Comment 3x before connect, no pitch.

### Step 3: DM
Permission → value → ask, 3 touches max.

---

## Detailed Guidance

### Sequence

**Checklist:**
- [ ] Connect note <200 chars, no pitch
- [ ] 3 touches then drop, meeting bar stated
- [ ] Handoff = held + qualified, not replied

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Pitch on connect | Ignored | Warm first |
| Endless followup | Spam flag | 3 then recycle |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Accept rate | Connects accepted | >30% | Manual |
| Reply → held | Replies to meetings | Up | HubSpot |

---

## Decision Tree

Low accept → profile + note fix. Low reply → angle + offer fix.

---

## Quick Assessment Checklist

1. [ ] ICP + offer?

---

## Expected Output Format

### Sequence Pack
[Steps + copy]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Automation ban | Restricted | Manual + limits |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Target base | Contacts | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | DM copy | Angles |

---

## Related Skills

- **b2b-list**: Accounts input
- **b2b-outbound**: Email sibling

---

## Questions to Ask

1. ICP + offer + proof?
