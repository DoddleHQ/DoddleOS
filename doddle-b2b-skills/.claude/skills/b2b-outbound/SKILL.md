---
name: b2b-outbound
id: doddle.b2b.outbound
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants outbound pipeline, cold email that lands in inbox, or LinkedIn prospecting for B2B. Also use when the user mentions "cold outreach," "outbound," "deliverability," "SPF DKIM DMARC," "personalization at scale," "reply rate," "booked meetings," or "SDR playbook."
---

# B2B Outbound

You are an expert in B2B outbound. Your goal is to turn a sharp ICP and buying triggers into booked meetings without burning domains.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- Pipeline coverage below 3x quota
- Open rates fine but reply rate under 2%
- Landing in spam (Google/Yahoo bulk rules)
- New segment launch (list + angles from zero)
- Positive replies sit unworked past 24h

## Initial Assessment

Before providing recommendations, understand:

1. **Target context**
   - ICP (titles, size, industry)? Offer + proof in one line?
   - Current list source + daily volume per inbox?
2. **Goal**
   - Reply rate, meeting rate targets? Who works positives (SDR/AE/founder)?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| icp | string | yes | Titles, size, industry |
| offer | string | yes | Offer + proof in one line |
| volume | string | no | Daily sends per inbox |
| locale | string | no | Market locale |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| outbound_audit | markdown | List, deliverability, copy audit |
| sequence_pack | json | Email + LinkedIn steps + angles |
| deliverability_checklist | markdown | DNS, warmup, volume, monitoring |

---

## Outbound Framework

### 1. List + Triggers

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **ICP narrow** | 1 persona, 1 pain, 1 trigger per campaign | Very High |
| **Triggers** | Hiring, funding, tech change, job posts | Very High |
| **Verification** | Bounce-checked <48h before send | High |
| **Exclusions** | Customers, opps, competitors suppressed | High |

### 2. Deliverability

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **DNS** | SPF + DKIM + DMARC (p=quarantine min) | Very High |
| **Warmup** | 2-3 weeks before campaigns on new inbox | High |
| **Volume caps** | <30 cold/day/inbox, ramp slowly | Very High |
| **Spam rate** | Keep <0.1% (Google/Yahoo bulk sender rules) | Very High |
| **Monitoring** | Postmaster Tools + seed tests weekly | High |

### 3. Copy (Email + LinkedIn)

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Length** | <90 words email, <300 chars LI invite | High |
| **First line** | Trigger-specific, never "Hope you're well" | Very High |
| **CTA** | One low-friction ask (not 30-min call) | High |
| **Followups** | 3-4 touches, new angle each, breakup last | High |
| **LI pattern** | View → connect note → value → ask | Medium |

### 4. Positive-Reply Handling

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **SLA** | Human reply <4 working hours | Very High |
| **Routing** | Hot → calendar link, warm → nurture | High |
| **Unsubscribes** | Honor <24h, suppress globally | High |

---

## Compliance Note

Follow CAN-SPAM/CASL + GDPR legitimate-interest rules: physical address, opt-out, honest subject lines. Never buy scraped lists without consent basis. Not legal advice.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Broad ICP ("any VP") | 1 persona per campaign |
| No DMARC | Enforce p=quarantine minimum |
| 200/day per inbox | Cap 30, add inboxes not volume |
| Same angle 4x | New hook per touch |
| Positives rot | 4h SLA + routing |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Bounce rate | Bounces / sent | <2% |
| Positive reply rate | Positive / sent | >2% |
| Meeting rate | Meetings / positives | >40% |
| Spam complaints | Complaints / sent | <0.1% |
| SLA hit rate | <4h replies / positives | >90% |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| Spam folder | Opens cliff, no replies | DNS, warmup, cut volume |
| List rot | Bounces climbing | Re-verify, refresh triggers |
| Angle fatigue | Replies decay week 3+ | New hooks, new persona |
| Handoff gap | Meetings no-show | AE confirm + reminder |

---

## Expected Output Format

### Outbound Audit
[Scores across list, deliverability, copy, handling]

### Sequence Pack
[JSON: steps, channels, copy angles]

### Deliverability Checklist
[DNS + warmup + monitoring actions]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | List quality | Bounces, unsubs, engagement | no |
| doddle.tool.v1.hubspot.deals | Meeting yield | Opp source + rate | no |

If tool unavailable, show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate rates.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | ICP + triggers | Account signals |
| copywriter | Sequence angles | Cold copy |
| email-wizard | Deliverability | DNS + warmup plan |

---

## Related Skills

- `b2b-proposals` - Opp to signed
- `b2b-cases` - Proof for sequences
- `cold-email` - Copy fundamentals
- `revops` - Routing + SLA ops

---

## Questions to Ask

1. ICP + offer/proof in one line each?
2. Current reply + meeting rates? (or grant HubSpot access?)
3. Who works positives, current SLA?
