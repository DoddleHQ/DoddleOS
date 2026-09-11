---
description: Plan healthcare paid ads for high-value procedures
argument-hint: [practice-name procedures monthly-budget]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `healthcare-ads` (id `doddle.health.ads`), `paid-advertising`, `conversion-copywriting`, `page-cro` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**HIPAA**: Never request or store PHI; no condition-based targeting using patient data.

---

## Interactive Parameter Collection

### Step 1: Ask Practice Name

**Question:** "What is the practice name?"
**Header:** "Practice Name"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the practice name
- **Skip** - Use generic practice placeholder

---

### Step 2: Ask Procedures + Budget

**Question:** "Which procedures should ads promote, and what is the monthly budget?"
**Header:** "Procedures + Budget"
**MultiSelect:** true

**Options:**
- **Implants / Ortho** - High-ticket dental
- **Aesthetic** - Injectables / laser / body
- **Elective medical** - LASIK / physio packages / screening
- **Budget: <2k / 2-5k / 5k+** - State range with selection

---

### Step 3: Confirmation

**Display summary:**
- Practice: [practice_name]
- Procedures: [procedures]
- Monthly budget: [monthly_budget]
- Skill: healthcare-ads (`doddle.health.ads`)

**Question:** "Proceed with ads plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, plan** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `practice_name` + `procedures` + `monthly_budget` from steps above.
2. **Run skill blueprint** - Execute `doddle-healthcare-skills/.claude/skills/healthcare-ads/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Campaign structure, ad angles, and budget split per skill output contract.

---

## Output Format + Location
Short report per skill outputs: campaign plan, ad copy angles, landing brief, budget allocation.
Save to: `./docs/health/healthcare-ads-[slug].md`
