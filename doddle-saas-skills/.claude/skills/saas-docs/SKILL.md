---
name: saas-docs
id: doddle.saas.docs
version: 1.0.0
blueprint: ./blueprint.yaml
description: Help-center SEO that deflects tickets. Use for IA, article briefs, findability.
---

# SaaS Docs

Docs as onboarding: findable, task-first, schema'd.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Ticket volume on how-tos high
- Docs unfindable via search
- New feature needs docs hub

## Initial Assessment

1. **Jobs**
   - Docs URL? Job to unblock?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| page_url | string | yes | Docs or product URL |
| activation_goal | string | no | Job docs unblock |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| docs_audit | markdown | Findability + clarity |
| ia_map | json | Taxonomy + hubs |
| article_briefs | markdown | Top-10 briefs |

---

## Core Framework

### Step 1: UX
Call `onboarding-cro` for entry clarity.

### Step 2: IA
Task hubs, not feature dumps.

### Step 3: Briefs
How-to + FAQ schema per article.

---

## Detailed Guidance

### Articles

**Checklist:**
- [ ] Title = user job verbatim
- [ ] Steps <7, video/GIF for clicks
- [ ] Related + escalation path at end

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Feature tour docs | Unfindable | Job-first titles |
| No schema | No rich results | HowTo + FAQ |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Deflection | Ticket share on covered topics | Down | Manual |
| Rank | How-to position | Top 3 | GSC |

---

## Decision Tree

High tickets + no article → brief first. Low rank → schema + internal links.

---

## Quick Assessment Checklist

1. [ ] Docs URL + job?

---

## Expected Output Format

### Docs Pack
[Audit + IA + briefs]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Stale screenshots | Distrust | Version per release |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.gsc.getSearchAnalytics | Demand | How-to queries | no |
| doddle.tool.v1.ga4.getReport | Drop | Search exits | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | Briefs | Outlines |

---

## Related Skills

- **saas-onboarding**: Activation context
- **saas-emails**: Ticket-triggered drip

---

## Questions to Ask

1. Docs URL + job to unblock?
