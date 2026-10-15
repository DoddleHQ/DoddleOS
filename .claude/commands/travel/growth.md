---
description: Grow travel business via GBP, reviews, itineraries, programmatic SEO
argument-hint: [business-name location destination-dates seed-topic]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `travel-growth` (id `doddle.travel.growth`), `local-reviews`, `programmatic-seo` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Business Name

**Question:** "What is the agency name as listed on Google?"
**Header:** "Business Name"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share agency + city
- **Skip** - Infer from context if obvious

### Step 2: Ask Location

**Question:** "What city / service area?"
**Header:** "Location"
**MultiSelect:** false

### Step 3: Ask Destination + Topic

**Question:** "Hero destination + dates, and seed topic/URL for pages?"
**Header:** "Product + SEO Seed"
**MultiSelect:** false

---

## Execution

1. Call `doddle.local.gbp` + `doddle.local.reviews` for presence.
2. Call `doddle.travel.itinerary` for sellable product (no invented prices).
3. Call `doddle.marketing.programmatic-seo` for page patterns.
4. Synthesize growth_audit + destination_pack + review_engine per `travel-growth` SKILL.md.
