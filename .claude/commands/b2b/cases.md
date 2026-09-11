---
description: Build B2B case study from client win
argument-hint: [client-name metric]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `b2b-cases` (id `doddle.b2b.cases`), `copywriting`, `content-strategy` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Client Name

**Question:** "What is the client name?"
**Header:** "Client Name"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share client + industry
- **Skip** - Use anonymized placeholder

---

### Step 2: Ask Metric

**Question:** "What is the headline metric?"
**Header:** "Metric"
**MultiSelect:** false

**Options:**
- **Enter metric** - I'll share result + timeframe
- **Skip** - Use qualitative-outcome placeholder

---

### Step 3: Confirmation

**Display summary:**
- Client: [client_name]
- Metric: [metric]
- Skill: b2b-cases (`doddle.b2b.cases`)

**Question:** "Proceed with case build?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `client_name` + `metric` from steps above.
2. **Run skill blueprint** - Execute `doddle-b2b-skills/.claude/skills/b2b-cases/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Case narrative and proof assets per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, case-study recommendations.
Save to: `./docs/b2b/b2b-cases-[slug].md`
