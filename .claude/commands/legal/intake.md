---
description: Optimize legal client intake flow for conversion speed
argument-hint: [firm-name practice-area]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `legal-intake` (id `doddle.legal.intake`) skill.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Bar Rules**: Follow attorney advertising rules; no guaranteed outcomes; include disclaimers where required.

---

## Interactive Parameter Collection

### Step 1: Ask Firm Name

**Question:** "What is the firm name?"
**Header:** "Firm Name"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the firm name
- **Skip** - Use generic firm placeholder

---

### Step 2: Ask Practice Area

**Question:** "What is the practice area?"
**Header:** "Practice Area"
**MultiSelect:** false

**Options:**
- **Personal Injury** - PI / accidents / mass tort
- **Family / Criminal / Immigration** - High-emotion practice areas
- **Corporate / Real Estate / Other** - Business or niche practice

---

### Step 3: Confirmation

**Display summary:**
- Firm: [firm_name]
- Practice Area: [practice_area]
- Skill: legal-intake (`doddle.legal.intake`)

**Question:** "Proceed with intake optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `firm_name` + `practice_area` from steps above.
2. **Run skill blueprint** - Execute `doddle-legal-skills/.claude/skills/legal-intake/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Intake friction audit and speed-to-lead fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, intake-flow recommendations.
Save to: `./docs/legal/legal-intake-[slug].md`
