---
description: Build law firm reputation with reviews and trust signals
argument-hint: [firm-name location]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `legal-reputation` (id `doddle.legal.reputation`) skill.

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

### Step 2: Ask Location

**Question:** "What is the firm location?"
**Header:** "Location"
**MultiSelect:** false

**Options:**
- **Enter location** - City / state or region
- **Skip** - Use generic location placeholder

---

### Step 3: Confirmation

**Display summary:**
- Firm: [firm_name]
- Location: [location]
- Skill: legal-reputation (`doddle.legal.reputation`)

**Question:** "Proceed with reputation build?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `firm_name` + `location` from steps above.
2. **Run skill blueprint** - Execute `doddle-legal-skills/.claude/skills/legal-reputation/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Review and trust-signal playbook per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized actions, reputation recommendations.
Save to: `./docs/legal/legal-reputation-[slug].md`
