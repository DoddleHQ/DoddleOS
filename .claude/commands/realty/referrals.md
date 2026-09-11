---
description: Generate referrals and reviews from past clients and sphere
argument-hint: [brokerage past_clients]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `realty-referrals` (id `doddle.realty.referrals`), `referral-program`, `email-sequence` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Fair Housing**: Never use discriminatory language; comply with Fair Housing Act in all copy.

---

## Interactive Parameter Collection

### Step 1: Ask Brokerage

**Question:** "What is the brokerage name?"
**Header:** "Brokerage"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the brokerage brand
- **Skip** - Use generic brokerage placeholder

---

### Step 2: Ask Past Clients

**Question:** "How many past clients in sphere?"
**Header:** "Past Clients"
**MultiSelect:** false

**Options:**
- **Enter count** - I'll share past client / sphere size
- **Skip** - Use generic sizing assumptions

---

### Step 3: Confirmation

**Display summary:**
- Brokerage: [brokerage]
- Past clients: [past_clients]
- Skill: realty-referrals (`doddle.realty.referrals`)

**Question:** "Proceed with referral engine?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `brokerage` + `past_clients` from steps above.
2. **Run skill blueprint** - Execute `doddle-real-estate-skills/.claude/skills/realty-referrals/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Referral asks, review engine, sphere touches per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, referral-engine recommendations.
Save to: `./docs/realty/realty-referrals-[slug].md`
