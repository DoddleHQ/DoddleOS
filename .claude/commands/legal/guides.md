---
description: Create legal practice-area guides for SEO and lead capture
argument-hint: [practice-area market]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `legal-guides` (id `doddle.legal.guides`) skill.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Bar Rules**: Follow attorney advertising rules; no guaranteed outcomes; include disclaimers where required.

---

## Interactive Parameter Collection

### Step 1: Ask Practice Area

**Question:** "What is the practice area?"
**Header:** "Practice Area"
**MultiSelect:** false

**Options:**
- **Personal Injury** - PI / accidents / mass tort
- **Family / Criminal / Immigration** - High-emotion practice areas
- **Corporate / Real Estate / Other** - Business or niche practice

---

### Step 2: Ask Market

**Question:** "What is the target market?"
**Header:** "Market"
**MultiSelect:** false

**Options:**
- **Enter market** - City / state or region
- **Skip** - Use national / generic targeting

---

### Step 3: Confirmation

**Display summary:**
- Practice Area: [practice_area]
- Market: [market]
- Skill: legal-guides (`doddle.legal.guides`)

**Question:** "Proceed with guide creation?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, create** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `practice_area` + `market` from steps above.
2. **Run skill blueprint** - Execute `doddle-legal-skills/.claude/skills/legal-guides/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Guide outline and lead-capture assets per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized topics, guide recommendations.
Save to: `./docs/legal/legal-guides-[slug].md`
