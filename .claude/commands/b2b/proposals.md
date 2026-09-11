---
description: Create B2B proposal for active deal
argument-hint: [deal-context deal-size]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `b2b-proposals` (id `doddle.b2b.proposals`), `copywriting`, `offers` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Deal Context

**Question:** "What is the deal context?"
**Header:** "Deal Context"
**MultiSelect:** false

**Options:**
- **Enter context** - I'll share prospect + pain + stage
- **Skip** - Use generic deal placeholder

---

### Step 2: Ask Deal Size

**Question:** "What is the deal size?"
**Header:** "Deal Size"
**MultiSelect:** false

**Options:**
- **SMB** - Under $10k ACV
- **Mid-market** - $10k-$100k ACV
- **Enterprise** - Over $100k ACV

---

### Step 3: Confirmation

**Display summary:**
- Deal context: [deal_context]
- Deal size: [deal_size]
- Skill: b2b-proposals (`doddle.b2b.proposals`)

**Question:** "Proceed with proposal build?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `deal_context` + `deal_size` from steps above.
2. **Run skill blueprint** - Execute `doddle-b2b-skills/.claude/skills/b2b-proposals/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Proposal structure and close plan per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, proposal recommendations.
Save to: `./docs/b2b/b2b-proposals-[slug].md`
