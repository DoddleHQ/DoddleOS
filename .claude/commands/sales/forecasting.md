---
description: Build sales forecast and pipeline coverage plan
argument-hint: [team-size quota]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `sales-forecasting` (id `doddle.sales.forecasting`).

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Team Size

**Question:** "What is your sales team size?"
**Header:** "Team Size"
**MultiSelect:** false

**Options:**
- **Enter size** - I'll share rep count / segments
- **Solo / Small** - 1-5 reps
- **Large** - 10+ reps / multi-segment team

---

### Step 2: Ask Quota

**Question:** "What is the quota target?"
**Header:** "Quota"
**MultiSelect:** false

**Options:**
- **Enter quota** - I'll share quarterly / annual target
- **Skip** - Use placeholder coverage model

---

### Step 3: Confirmation

**Display summary:**
- Team Size: [team_size]
- Quota: [quota]
- Skill: sales-forecasting (`doddle.sales.forecasting`)

**Question:** "Proceed with forecasting?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `team_size` + `quota` from steps above.
2. **Run skill blueprint** - Execute `doddle-sales-skills/.claude/skills/sales-forecasting/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Forecast model and coverage gaps per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored pipeline, prioritized gaps, forecast recommendations.
Save to: `./docs/sales/sales-forecasting-[slug].md`
