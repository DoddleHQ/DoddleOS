---
description: Plan B2B partnership for co-marketing growth
argument-hint: [partner-type goal]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `b2b-partnerships` (id `doddle.b2b.partnerships`), `partnerships`, `content-strategy` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Partner Type

**Question:** "What type of partner?"
**Header:** "Partner Type"
**MultiSelect:** false

**Options:**
- **Technology** - Integration / co-build partner
- **Channel** - Reseller / referral partner
- **Brand** - Co-marketing / content partner

---

### Step 2: Ask Goal

**Question:** "What is the partnership goal?"
**Header:** "Goal"
**MultiSelect:** false

**Options:**
- **Enter goal** - I'll share pipeline / revenue target
- **Skip** - Use awareness-first placeholder

---

### Step 3: Confirmation

**Display summary:**
- Partner type: [partner_type]
- Goal: [goal]
- Skill: b2b-partnerships (`doddle.b2b.partnerships`)

**Question:** "Proceed with partnership plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, plan** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `partner_type` + `goal` from steps above.
2. **Run skill blueprint** - Execute `doddle-b2b-skills/.claude/skills/b2b-partnerships/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Partnership plan and outreach per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, partnership recommendations.
Save to: `./docs/b2b/b2b-partnerships-[slug].md`
