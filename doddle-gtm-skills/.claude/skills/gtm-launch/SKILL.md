---
name: gtm-launch
id: doddle.gtm.launch
version: 1.0.0
blueprint: ./blueprint.yaml
description: Tiered launch with gates. Use for feature, product, or market launches.
---

# GTM Launch

Soft → EA → GA with gates, never big-bang hope. Calls launch-strategy.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Launch date set, plan missing
- Last launch underwhelmed
- Cross-team readiness unclear

## Initial Assessment

1. **Launch**
   - Context: what, audience, channels, timeline?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | What, audience, channels, timeline |
| goal | string | no | Launch goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| launch_plan | markdown | Phases + owners + dates |
| phase_gates | json | Gate criteria |
| rollout_checklist | markdown | Ready + rollback |

---

## Core Framework

### Step 1: Strategy
Call `launch-strategy` for channel plan.

### Step 2: Gate
Product, marketing, sales, CS ready checks.

### Step 3: Roll
Checklist + rollback triggers per phase.

---

## Detailed Guidance

### Gates

**Checklist:**
- [ ] Gate fails → phase slips, no silent ship
- [ ] Rollback owner + trigger named
- [ ] Comms per phase: internal → design partners → GA

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Big-bang | Breaks everything | Tiered |
| No gate | Unready ship | Gate + slip |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Gate pass | First-try pass | Up | Manual |
| Launch → pipeline | Sourced pipe | Up | HubSpot |

---

## Decision Tree

Unready gate → slip phase, not waive. Small audience → soft only.

---

## Quick Assessment Checklist

1. [ ] Launch context + goal?

---

## Expected Output Format

### Launch Plan
[Phases + gates]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Date-locked | Unready ship | Re-tier scope |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.slack.postMessage | Gate alerts | Approvals | no |
| doddle.tool.v1.notion.pages | Plan base | Docs | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| planner | Sequencing | Phases |

---

## Related Skills

- **gtm-strategy**: Upstream plan
- **gtm-enablement**: Asset readiness

---

## Questions to Ask

1. Launch context + goal?
