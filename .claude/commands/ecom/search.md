---
description: Optimize ecommerce site search for findability and conversion
argument-hint: [site_url search_query]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `ecommerce-search` (id `doddle.ecommerce.search` v1.5.1, pack `doddle-ecommerce-skills`), `page-cro`, `seo-mastery`, `copywriting` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**NOTE**: Replaces legacy routing via `/cro:*` and `/pricing:strategy`.

---

## Interactive Parameter Collection

### Step 1: Ask Site URL

**Question:** "What is the store / site URL?"
**Header:** "Site URL"
**MultiSelect:** false

**Options:**
- **Enter URL** - I'll share the store link
- **Skip** - Audit from description only

---

### Step 2: Ask Search Query

**Question:** "What is the test search query?"
**Header:** "Search Query"
**MultiSelect:** false

**Options:**
- **Enter query** - I'll share the query to test
- **Skip** - Use top category query

---

### Step 3: Confirmation

**Display summary:**
- Site URL: [site_url]
- Search query: [search_query]
- Skill: ecommerce-search (`doddle.ecommerce.search`)

**Question:** "Proceed with search optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `site_url` + `search_query` from steps above.
2. **Run skill blueprint** - Execute `doddle-ecommerce-skills/.claude/skills/ecommerce-search/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Search relevance audit and findability fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, site-search recommendations.
Save to: `./docs/ecom/ecommerce-search-[slug].md`
