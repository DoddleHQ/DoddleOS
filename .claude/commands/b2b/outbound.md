---
description: Build B2B outbound sequence for pipeline
argument-hint: [icp offer]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `b2b-outbound` (id `doddle.b2b.outbound`), `cold-email`, `copywriting` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask ICP

**Question:** "Who is the ICP?"
**Header:** "ICP"
**MultiSelect:** false

**Options:**
- **Enter ICP** - I'll share title + industry + size
- **Skip** - Use generic B2B placeholder

---

### Step 2: Ask Offer

**Question:** "What is the offer?"
**Header:** "Offer"
**MultiSelect:** false

**Options:**
- **Enter offer** - I'll share value prop + CTA
- **Skip** - Use discovery-call placeholder

---

### Step 3: Confirmation

**Display summary:**
- ICP: [icp]
- Offer: [offer]
- Skill: b2b-outbound (`doddle.b2b.outbound`)

**Question:** "Proceed with outbound build?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `icp` + `offer` from steps above.
2. **Run skill blueprint** - Execute `doddle-b2b-skills/.claude/skills/b2b-outbound/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Outbound sequence and messaging angles per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, outbound recommendations.
Save to: `./docs/b2b/b2b-outbound-[slug].md`
