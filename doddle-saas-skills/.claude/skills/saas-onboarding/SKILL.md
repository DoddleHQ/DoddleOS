---
name: saas-onboarding
id: doddle.saas.onboarding
version: 1.0.0
blueprint: ./blueprint.yaml
description: Turn signups into activated users via signup and onboarding CRO. Use for trial/fremium activation, aha instrumentation. For paywalls see saas-paywall.
---

# SaaS Onboarding

Signup friction + first-run activation in one pass. Calls marketing CRO, synthesizes SaaS playbook.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Signup → activation rate low
- New onboarding flow or aha redefinition
- SSO, no-card, sample-data decisions pending

## Initial Assessment

1. **Funnel**
   - Signup URL? Trial model + length?
2. **Aha**
   - Activation goal? Events tracked?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| signup_url | string | yes | Signup or onboarding entry URL |
| activation_goal | string | no | Aha moment definition |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| onboarding_audit | markdown | Signup-to-aha audit with scores |
| activation_playbook | markdown | Checklist, empty states, events |
| aha_checklist | json | Instrumentation + test hypotheses |

---

## Core Framework

### Step 1: Friction
Call `signup-flow-cro` for fields, SSO, social proof.

### Step 2: Activation
Call `onboarding-cro` for first-run, empty states, aha path.

### Step 3: Instrument
Aha events + PQL thresholds for handoff.

---

## Detailed Guidance

### Activation

**Checklist:**
- [ ] ≤3 fields or SSO first
- [ ] Sample data preloaded, empty state has 1-click start
- [ ] Aha reachable in <3 clicks, event instrumented
- [ ] No fake progress — real state only

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Tour everything | Cognitive load | 1 aha path |
| No sample data | Blank canvas stall | Preload + templates |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Activation rate | Signup → aha | Up | GA4 |
| TTV | Time to value | Down | GA4 |

---

## Decision Tree

No tracking → manual heuristic audit + instrumentation list. Low activation → onboarding-cro first, signup second.

---

## Quick Assessment Checklist

1. [ ] Signup URL?
2. [ ] Activation goal?
3. [ ] Tracking live or manual?

---

## Expected Output Format

### Onboarding Audit
[Scores + friction ranked]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No data | GA4 missing | Heuristic + instrument |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Funnel drop | Steps, TTV | no |
| doddle.tool.v1.hubspot.contacts | Lifecycle | Stage mix | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| conversion-optimizer | Synthesis | Prioritized fixes |

---

## Related Skills

- **saas-trial**: Broader trial → PQL context
- **saas-emails**: Drip to pull aha forward

---

## Questions to Ask

1. Signup URL + trial model?
2. Aha definition?
