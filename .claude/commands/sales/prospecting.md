---
description: Build ICP-based prospecting list and outreach angles
argument-hint: [icp tam]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `sales-prospecting` (id `doddle.sales.prospecting`).

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask ICP

**Question:** "Who is your ideal customer profile?"
**Header:** "ICP"
**MultiSelect:** false

**Options:**
- **Enter ICP** - I'll describe title, industry, size
- **Skip** - Use generic B2B placeholder

---

### Step 2: Ask TAM

**Question:** "What is your target market scope?"
**Header:** "TAM"
**MultiSelect:** false

**Options:**
- **SMB** - Small / mid-market accounts
- **Mid-Market** - 200-2000 employee companies
- **Enterprise** - Large / strategic accounts

---

### Step 3: Confirmation

**Display summary:**
- ICP: [icp]
- TAM: [tam]
- Skill: sales-prospecting (`doddle.sales.prospecting`)

**Question:** "Proceed with prospecting?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `icp` + `tam` from steps above.
2. **Run skill blueprint** - Execute `doddle-sales-skills/.claude/skills/sales-prospecting/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Prospect list criteria and outreach angles per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored segments, prioritized accounts, outreach angles.
Save to: `./docs/sales/sales-prospecting-[slug].md`
