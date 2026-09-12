---
name: travel-booking
id: doddle.travel.booking
version: 1.0.0
blueprint: ./blueprint.yaml
description: Hold, confirm, change travel with accuracy gates + policy compliance. Use when ready to ticket leisure or corporate trips, group splits, or changes/cancellations loom. For compare, see travel-search.
---

# Travel Booking

Hold → verify → ticket → track. Name accuracy gate + policy guardrails every time.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Itinerary approved, ready to hold/ticket
- Group travel with splits + deposits
- Corporate approval + cost-center tagging required
- Changes/cancellations with fee exposure

## Initial Assessment

1. **What**
   - What to ticket (flights, stays, activities)? PNRs exist?
   - Names/DOBs/passports match IDs exactly?
2. **Rules**
   - Corporate: approver, caps, card to charge?
   - Leisure: deposit schedule, insurance accepted/declined?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| itinerary_ref | string | yes | Approved plan or PNRs; ask if missing |
| travelers_docs | string | no | Names/DOBs/passports; gate before ticket |
| motion | string | no | leisure or corporate; default leisure |
| payment_policy | string | no | Card + caps + approver |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Ticketing sequence with gates + fee table |
| action_list | json | Holds, payments, approvals, tracking |

---

## Core Framework

### Step 1: Gate
Names, docs, policy, payment — no ticket till green.

### Step 2: Sequence
Holds first (expiring), then non-refundables, then extras.

### Step 3: Track
Confirmations filed, deadlines calendared, refund watch on.

---

## Detailed Guidance

### Accuracy Gate

**Checklist:**
- [ ] Names exactly as IDs, DOBs, passport nos + 6-mo validity
- [ ] Contact email/phone that receives schedule changes
- [ ] Seat/bag/meals selected before pay (no rework fees)

### Leisure Booking

**Checklist:**
- [ ] Group split: who pays what, deposit dates
- [ ] Insurance offered + decision recorded
- [ ] Cancellation windows per item calendared

### Corporate Booking

**Checklist:**
- [ ] Class/rate caps pass, approver sign-off filed
- [ ] Cost-center + trip purpose tags on every item
- [ ] Refundable default unless savings > change risk
- [ ] Corp card vs personal + reclaim path stated

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Ticket before gate | Name-change fees | Gate checklist first |
| Non-refundable to save 5% | Change costs 10x | Refundable default |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Holds expire | Price lost | Calendar every hold |
| No confirmation file | Chaos at airport | Single trip folder |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Fees untracked | Money left | Refund watch list |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Gate pass | Bookings passing gate | 100% | Manual |
| Policy fit | Corp items in caps | 100% | CRM |
| Change fees | $ paid avoidable | 0 | Expense |
| Refunds recovered | Claimed / owed | 100% | Manual |

---

## Decision Tree

Docs incomplete → hold, never ticket. Over cap → approver or cheaper option. Group → splits written before any charge.

---

## Quick Assessment Checklist

1. [ ] Plan or PNRs?
2. [ ] Docs exact?
3. [ ] Payment + caps?
4. [ ] Approver (corp)?
5. [ ] Insurance decision?

---

## Expected Output Format

### Ticketing Sequence
[Gates, order, deadlines]

### Fee + Track
[Change table, refund watch]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Name mismatch | Denied boarding risk | Re-verify vs ID now |
| Expired hold | Fare jump | Re-hold immediately |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Corp traveler + approver | Contacts, owners | no |
| doddle.tool.v1.hubspot.deals | Trip budget tracking | Deal, stage | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| planner | Ticketing order | Sequence |
| email-wizard | Confirmation pack | Guest comms |
| continuity-specialist | Change handling | Recovery flow |

---

## Related Skills

- **travel-search**: Compare first
- **travel-itinerary**: Plan input
- **travel-support**: Post-ticket care

---

## Questions to Ask

1. Plan or PNRs to ticket?
2. Docs exact for all travelers?
3. Payment + approver (corp)?
