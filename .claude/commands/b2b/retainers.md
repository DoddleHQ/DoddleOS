---
description: Design B2B retainer offer for recurring revenue
argument-hint: [service arpa]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `b2b-retainers` (id `doddle.b2b.retainers`), `pricing-strategy`, `offers` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Service

**Question:** "What is the retainer service?"
**Header:** "Service"
**MultiSelect:** false

**Options:**
- **Enter service** - I'll share scope + deliverables
- **Skip** - Use generic service placeholder

---

### Step 2: Ask ARPA

**Question:** "What is target monthly ARPA?"
**Header:** "ARPA"
**MultiSelect:** false

**Options:**
- **Starter** - Under $2k/mo
- **Growth** - $2k-$10k/mo
- **Scale** - Over $10k/mo

---

### Step 3: Confirmation

**Display summary:**
- Service: [service]
- ARPA: [arpa]
- Skill: b2b-retainers (`doddle.b2b.retainers`)

**Question:** "Proceed with retainer design?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, design** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `service` + `arpa` from steps above.
2. **Run skill blueprint** - Execute `doddle-b2b-skills/.claude/skills/b2b-retainers/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Retainer tiers and scope per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, retainer recommendations.
Save to: `./docs/b2b/b2b-retainers-[slug].md`
