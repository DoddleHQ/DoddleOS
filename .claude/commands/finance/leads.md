---
description: Generate qualified leads for finance firm by niche
argument-hint: [firm-name niche]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `finance-leads` (id `doddle.finance.leads`), `page-cro`, `form-cro` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Compliance**: No guaranteed returns; all messaging must be compliant, no misleading claims.

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

### Step 2: Ask Niche

**Question:** "What is the target niche?"
**Header:** "Niche"
**MultiSelect:** false

**Options:**
- **Wealth / Advisory** - HNW, retirement, planning
- **Lending / Mortgage** - Home loans, refi, SME
- **Insurance / Other** - Life, general, specialty

---

### Step 3: Confirmation

**Display summary:**
- Firm: [firm_name]
- Niche: [niche]
- Skill: finance-leads (`doddle.finance.leads`)

**Question:** "Proceed with lead generation?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, generate** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `firm_name` + `niche` from steps above.
2. **Run skill blueprint** - Execute `doddle-finance-skills/.claude/skills/finance-leads/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Lead sources, offers, and capture fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, lead-gen recommendations.
Save to: `./docs/finance/finance-leads-[slug].md`
