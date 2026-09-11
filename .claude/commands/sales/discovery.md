---
description: Run structured sales discovery and qualification
argument-hint: [deal-context stage]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `sales-discovery` (id `doddle.sales.discovery`).

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Deal Context

**Question:** "What is the deal context?"
**Header:** "Deal Context"
**MultiSelect:** false

**Options:**
- **Enter context** - I'll share account, need, deal size
- **Skip** - Use generic deal placeholder

---

### Step 2: Ask Stage

**Question:** "What is the current deal stage?"
**Header:** "Stage"
**MultiSelect:** false

**Options:**
- **Early** - First call / qualification
- **Mid** - Demo / evaluation / multi-threaded
- **Late** - Proposal / negotiation / close

---

### Step 3: Confirmation

**Display summary:**
- Deal Context: [deal_context]
- Stage: [stage]
- Skill: sales-discovery (`doddle.sales.discovery`)

**Question:** "Proceed with discovery?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `deal_context` + `stage` from steps above.
2. **Run skill blueprint** - Execute `doddle-sales-skills/.claude/skills/sales-discovery/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Discovery questions and qualification summary per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized questions, next-step recommendations.
Save to: `./docs/sales/sales-discovery-[slug].md`
