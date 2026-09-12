---
name: digital-pr
id: doddle.marketing.digital-pr
version: 1.0.0
blueprint: ./blueprint.yaml
description: Earn authority via digital PR, outreach, linkable assets. Use when needing backlinks, coverage, journalist pitches, HARO, resource links. For internal links, see internal-linking. For audits, see seo-mastery.
---

# Digital PR

Outreach-driven authority: prospects, angles, assets, pitches, coverage tracking. Covers infographic block 6 (111-132).

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Referring domains flat, authority gap vs competitors
- Launch / data / case study needing coverage
- Unlinked mentions, lost links to reclaim
- Journalist, podcast, guest contribution pushes

## Initial Assessment

1. **Assets**
   - Linkable asset? Data, study, tool, case?
   - Proof available? Quotes, founders, clients?
2. **Targets**
   - Niche? Competitor backlinks to steal?
   - Prior coverage? Blacklist topics?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| domain_or_topic | string | yes | Site or campaign topic; ask if missing |
| asset | string | no | Existing asset; propose if missing |
| competitor | string | no | Competitor domain for backlink gap |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Prospect list, angles, pitch drafts, outreach plan |
| action_list | json | Prioritized outreach actions with impact/effort |

---

## Core Framework

### Step 1: Prospect
Gap vs competitors, broken links, mentions, resource pages.

### Step 2: Angle
Journalist framing, data story, expert quote, newsjack hook.

### Step 3: Pitch
Asset match, personalized outreach, calendar, follow-up, velocity track.

---

## Detailed Guidance

### Prospecting

**Checklist:**
- [ ] Prospect list (111), competitor gap (120)
- [ ] Broken outreach (112), unlinked mentions (113)
- [ ] Resource pages (125), partnership ideas (118)
- [ ] Citation shortlist (129) — trusted sources
- [ ] Toxic review (121), anchor diversity (131)

### Angles & Assets

**Checklist:**
- [ ] Journalist angle (114), data pitch (115)
- [ ] Asset planner (117) — why link?
- [ ] Case promotion (128), newsjack review (124)
- [ ] Authority snapshot (132) — baseline

### Outreach

**Checklist:**
- [ ] Expert quote (116), HARO draft (119) — concise
- [ ] Podcast pitch (126), guest ideas (127)
- [ ] PR calendar (123) — schedule moments
- [ ] Lost-link recovery (122), velocity review (130)

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Mass blast pitches | 0% reply | 20 tailored > 500 generic |
| No asset | Nothing to link | Build asset first |
| Buy links | Penalty risk | Earn via value |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Long pitches | Journalists skim | 120 words, hook first |
| No follow-up | 50% replies late | 1-2 nudges max |
| Ignore mentions | Free links lost | Claim unlinked first |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Count links not domains | Inflates | Track referring domains |
| Ignore anchor mix | Unnatural | Diversity check |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Referring domains | Unique linking domains | Growing net | Semrush/Ahrefs |
| Coverage rate | Pitches → links | >5% | Manual |
| Unlinked claimed | Mentions converted | 100% | Alerts |
| Toxic share | Suspicious links | <5% | Audit |
| Anchor mix | Branded vs exact | Natural spread | Audit |

---

## Decision Tree

No asset → planner first. Mentions exist → claim before cold. Gap large → broken + resource quick wins. Launch soon → calendar + newsjack.

---

## Quick Assessment Checklist

1. [ ] Domain / topic?
2. [ ] Asset exists?
3. [ ] Competitor to gap?
4. [ ] Spokesperson available?
5. [ ] Prior penalties / toxic?

---

## Expected Output Format

### Prospect List
[Targets, gaps, quick wins]

### Angles + Pitches
[Hooks, drafts, assets]

### Outreach Plan
[Calendar, follow-up, tracking]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No hook | Silence | Data / contrarian angle |
| Wrong targets | Irrelevant links | Niche filter |
| Over-outreach | Spam flags | Cap velocity |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.semrush.keywordResearch | Authority gaps | Backlinks, domains | no |
| doddle.tool.v1.dataforseo.serpGoogle | Coverage SERP | Who ranks, cites | no |
| doddle.tool.v1.gsc.getSearchAnalytics | Link impact | Impressions lift | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | Prospecting, gaps | Target lists |
| copywriter | Pitch drafts | Hooks, angles |
| seo-specialist | Toxic/anchor review | Risk check |

---

## Related Skills

- **seo-mastery**: Link-building refs, audits
- **internal-linking**: On-site equity flow
- **content-strategy**: Asset editorial

---

## Questions to Ask

1. Domain or campaign topic?
2. Asset available, or build new?
3. Competitor to benchmark?
