---
name: saas-security
id: doddle.saas.security
version: 1.0.0
blueprint: ./blueprint.yaml
description: Trust center that unblocks enterprise deals. Use for SOC2 pages, DPA flow, questionnaires.
---

# SaaS Security

Prove before asked. No invented certs — NOT AVAILABLE if missing.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Enterprise deals stall on security
- Questionnaire answers ad hoc
- Trust page thin

## Initial Assessment

1. **Posture**
   - Stack, certs, gaps?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Stack, certs, gaps |
| goal | string | no | Trust goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| trust_audit | markdown | Gaps vs bar |
| page_pack | markdown | Trust page + proof |
| questionnaire_kit | json | Answers + owners |

---

## Core Framework

### Step 1: Audit
Certs, pen-test recency, subprocessors, DPA.

### Step 2: Page
What/where/who-accesses + status link.

### Step 3: Kit
Versioned answers, owner per question.

---

## Detailed Guidance

### Trust

**Checklist:**
- [ ] No claimed cert without artifact
- [ ] Subprocessors + DPA linked
- [ ] Security contact + SLA stated

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Vague badges | Enterprise bounce | Artifacts + dates |
| One-off answers | Drift | Versioned kit |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Security cycle | Open → cleared days | Down | Manual |

---

## Decision Tree

No cert → roadmap + compensating controls, never fake.

---

## Quick Assessment Checklist

1. [ ] Stack + certs context?

---

## Expected Output Format

### Trust Pack
[Audit + page + kit]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Fake compliance | Deal loss + risk | NOT AVAILABLE + plan |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.notion.pages | Policy base | Docs | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | Trust copy | Pages |

---

## Related Skills

- **b2b-rfp**: Questionnaire consumer
- **saas-pricing**: Enterprise fence

---

## Questions to Ask

1. Stack + certs + gaps?
