---
description: Create SEO listing pages and property marketing for real estate
argument-hint: [market listing_url]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `realty-listings` (id `doddle.realty.listings`), `programmatic-seo`, `page-cro` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Fair Housing**: Never use discriminatory language; comply with Fair Housing Act in all copy.

---

## Interactive Parameter Collection

### Step 1: Ask Market

**Question:** "What is the target market?"
**Header:** "Market"
**MultiSelect:** false

**Options:**
- **Enter market** - I'll share city / neighborhood
- **Skip** - Use generic market placeholder

---

### Step 2: Ask Listing URL

**Question:** "What is the listing URL?"
**Header:** "Listing URL"
**MultiSelect:** false

**Options:**
- **Enter URL** - I'll share the property link
- **Skip** - Create template without live listing

---

### Step 3: Confirmation

**Display summary:**
- Market: [market]
- Listing URL: [listing_url]
- Skill: realty-listings (`doddle.realty.listings`)

**Question:** "Proceed with listing marketing?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `market` + `listing_url` from steps above.
2. **Run skill blueprint** - Execute `doddle-real-estate-skills/.claude/skills/realty-listings/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Listing pages, property copy, SEO fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, listing-page recommendations.
Save to: `./docs/realty/realty-listings-[slug].md`
