---
description: Handle sales objections and close negotiation
argument-hint: [deal-size objection]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `sales-negotiation` (id `doddle.sales.negotiation`).

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Deal Size

**Question:** "What is the deal size?"
**Header:** "Deal Size"
**MultiSelect:** false

**Options:**
- **Enter size** - I'll share ACV / range
- **SMB** - Small, fast-close deal
- **Enterprise** - Large, multi-stakeholder deal

---

### Step 2: Ask Objection

**Question:** "What is the main objection?"
**Header:** "Objection"
**MultiSelect:** false

**Options:**
- **Price** - Too expensive / discount ask
- **Timing** - Delay / no urgency / budget cycle
- **Competitor / Risk** - Competitor preference or risk concern

---

### Step 3: Confirmation

**Display summary:**
- Deal Size: [deal_size]
- Objection: [objection]
- Skill: sales-negotiation (`doddle.sales.negotiation`)

**Question:** "Proceed with negotiation plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `deal_size` + `objection` from steps above.
2. **Run skill blueprint** - Execute `doddle-sales-skills/.claude/skills/sales-negotiation/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Objection responses and close plan per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored tactics, prioritized responses, negotiation recommendations.
Save to: `./docs/sales/sales-negotiation-[slug].md`
