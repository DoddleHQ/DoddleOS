---
name: b2b-deliverability
id: doddle.b2b.deliverability
version: 1.0.0
blueprint: ./blueprint.yaml
description: Fix deliverability: DNS, warmup, volume, monitoring. Use when bounce/spam rises or new domains launch.
---

# B2B Deliverability

Infra before copy. Audit → warm → monitor.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Spam placement or blocks
- New domain/inbox launch
- Bounce >3%

## Initial Assessment

1. **Infra**
   - Domain? Volume per inbox?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| domain | string | yes | Sending domain |
| volume | string | no | Daily volume per inbox |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| infra_audit | markdown | DNS + warmup audit |
| warmup_plan | json | Ramp with guards |
| monitor_checklist | markdown | Monitors + thresholds |

---

## Core Framework

### Step 1: Audit
SPF/DKIM/DMARC, warmup age, volume.

### Step 2: Ramp
Start 20/d, +20% daily if bounce <2%.

### Step 3: Monitor
Bounce, spam, blocklist daily.

---

## Detailed Guidance

### Guards

**Checklist:**
- [ ] Separate domains for outbound vs corporate
- [ ] 1 inbox per 2k prospects max
- [ ] Bounce >3% → pause + clean

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Blast day 1 | Burned domain | Warm 14d |
| No monitoring | Silent death | Daily checks |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Inbox rate | Inbox / sent | >90% | Manual |
| Bounce | Hard bounce | <2% | HubSpot |

---

## Decision Tree

New domain → 14d warmup. Burning → halve volume + clean list.

---

## Quick Assessment Checklist

1. [ ] Domain + volume?

---

## Expected Output Format

### Infra Audit
[Findings + ramp]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Shared domain | Corp spam | Split domains |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Bounce base | Bounces | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| email-wizard | Ramp logic | Warmup plan |

---

## Related Skills

- **b2b-outbound**: Copy after infra fixed

---

## Questions to Ask

1. Domain + volume?
