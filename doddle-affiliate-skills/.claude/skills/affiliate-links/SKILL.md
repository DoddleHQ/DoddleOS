---
name: affiliate-links
id: doddle.affiliate.links
version: 1.0.0
blueprint: ./blueprint.yaml
description: Earn affiliate links via PR and internal linking. Use for gap analysis and outreach. For content see affiliate-content.
---

# Affiliate Links

Gap → angles → outreach. No spam, no paid links without rel.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New page needs links
- Competitor outranks on authority
- Internal link equity wasted

## Initial Assessment

1. **Base**
   - Domain? Competitors?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| domain | string | yes | Site domain |
| competitors | string | no | Competitor domains |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| link_audit | markdown | Gap + risks |
| outreach_pack | json | Targets and angles |

---

## Core Framework

### Step 1: Gap
Referring-domain overlap vs competitors.

### Step 2: Angles
Stats, free tool, expert quote per target.

### Step 3: Internal
Hub links to money pages first.

---

## Detailed Guidance

### Outreach

**Checklist:**
- [ ] No paid without sponsored rel
- [ ] Followup x2 max, then drop
- [ ] Internal links before external push

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Blast templates | 0% reply | 1:1 angle |
| Ignore internal | Wasted equity | Hub first |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Referring domains | New RD / mo | Up | Semrush |
| Reply rate | Positive replies | >8% | Manual |

---

## Decision Tree

Thin budget → internal + HARO only. Budget → digital PR asset.

---

## Quick Assessment Checklist

1. [ ] Domain?
2. [ ] Competitors?

---

## Expected Output Format

### Link Audit
[Gaps + risks]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Toxic spike | Spam links | Disavow review |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.semrush.domainOverview | Gap | Backlinks | no |
| doddle.tool.v1.dataforseo.serpGoogle | SERP authority | Top pages | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| seo-specialist | Risk check | Toxic flags |

---

## Related Skills

- **affiliate-content**: Linkable asset
- **affiliate-keywords**: Targets

---

## Questions to Ask

1. Domain + competitors?
