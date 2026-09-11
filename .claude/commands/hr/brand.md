---
description: Build employer brand to attract talent for key roles
argument-hint: [company roles]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `hr-brand` (id `doddle.hr.brand`), `brand-building`, `content-strategy` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Company

**Question:** "What is the company name?"
**Header:** "Company"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the company name
- **Skip** - Use generic company placeholder

---

### Step 2: Ask Roles

**Question:** "Which roles should employer brand target?"
**Header:** "Roles"
**MultiSelect:** false

**Options:**
- **Enter roles** - I'll list priority roles
- **All roles** - General employer brand refresh

---

### Step 3: Confirmation

**Display summary:**
- Company: [company]
- Roles: [roles]
- Skill: hr-brand (`doddle.hr.brand`)

**Question:** "Proceed with employer brand plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build brand** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `company` + `roles` from steps above.
2. **Run skill blueprint** - Execute `doddle-hr-skills/.claude/skills/hr-brand/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Employer brand messaging and channel plan per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, employer-brand recommendations.
Save to: `./docs/hr/hr-brand-[slug].md`
