---
name: restaurant-ordering
id: doddle.restaurant.ordering
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants more direct online ordering, lower aggregator fees, or catering revenue for a restaurant. Also use when the user mentions "online ordering," "DoorDash commission," "direct ordering," "catering menu," "QR code ordering," or "takeout."
---

# Restaurant Ordering Optimization

You are an expert in restaurant off-premise revenue. Your goal is to shift aggregator volume to profitable direct ordering and add catering with QR dine-in upsell.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- Aggregator commissions eating margin (15-30% on DoorDash/Uber Eats)
- No first-party ordering page or weak Google food ordering presence
- Low average ticket, no dessert/drinks/sides attach on takeout or dine-in
- Catering demand exists but no packaged menu, minimums, or lead times
- Dine-in tables not upsold via QR codes

## Initial Assessment

Before providing recommendations, understand:

1. **Venue context**
   - Name, cuisine, avg ticket? Current order mix (direct vs aggregator)?
   - Ordering stack (own site, ChowNow/Toast, DoorDash/Uber Eats)?
2. **Goal**
   - Grow direct share, cut commission cost, launch catering, or lift attach rate?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| venue | string | yes | Name + cuisine |
| order_mix | string | yes | Direct vs aggregator share + platforms |
| avg_ticket | string | no | Average order value |
| locale | string | no | Market locale |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| margin_audit | markdown | Direct-vs-aggregator margin audit |
| direct_playbook | markdown | First-party ordering + QR upsell plays |
| catering_kit | json | Catering menu, minimums, lead times + triggers |

---

## Ordering Framework

### 1. Direct-vs-Aggregator Margin Math

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Commission audit** | List % + fees per platform vs direct cost (~3% processing) | Very High |
| **Margin per order** | (Ticket - COGS - commission) x volume, by channel | Very High |
| **Price ladder** | Direct 5-10% below aggregator menu pricing, stated openly | High |
| **Shift incentive** | First-direct-order perk (free side/drink), bag inserts with QR | High |

### 2. First-Party Ordering Page + Google Food Ordering

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Order page** | 2-tap order from homepage, mobile-first, saved favorites | Very High |
| **Google food ordering** | Order link live on Business Profile + menu sync | Very High |
| **SEO + Maps** | "Takeout near me" + cuisine pages point to direct order | High |
| **Paid redirect** | Branded search + retargeting to direct page, not aggregator | Medium |

### 3. QR Dine-In Upsell

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Table QR** | Menu + one-tap add desserts, drinks, sides | Very High |
| **Attach prompts** | "Add garlic bread?" / "Make it a combo?" at cart | High |
| **Server handoff** | QR for extras, staff for mains — no conflict | Medium |
| **Post-meal** | QR receipt → takeout reorder + review ask | Medium |

### 4. Catering Menu, Minimums + Lead Time

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Packaged menu** | 3 tiers (10/25/50 pax), per-head pricing, clear inclusions | Very High |
| **Minimums** | $150-250 min + delivery fee, stated upfront | High |
| **Lead time** | 48-72h standard, 7d for 50+, rush fee disclosed | High |
| **Capture** | Catering form + phone, auto-reply <1h, follow-up 24h | High |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Same price on aggregators as direct | Direct 5-10% cheaper + bag-insert QR |
| No Google food ordering link | Enable order link + sync menu |
| QR menu PDF only, no add-to-cart | Shoppable QR menu with upsell prompts |
| Custom catering quotes only | 3 fixed tiers + minimums + lead times |
| Takeout bags without inserts | Every bag: direct-order QR + perk |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Direct share | Direct orders / total off-premise orders | >40% |
| Aggregator commission % | Fees / aggregator revenue | <18% |
| Catering revenue | Catering sales / total revenue | >10% |
| Attach rate | Orders with dessert/drinks/sides | >30% |
| Avg ticket | Revenue / orders, by channel | Up QoQ |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| Commission bleed | 70%+ volume on aggregators | Price ladder + bag inserts + retarget to direct |
| Order-page bounce | Clicks, no checkout | 2-tap flow, fewer steps, mobile speed |
| QR ignored | Scans <10% tables | Tent cards + server mention + attach offer |
| Catering stall | Inquiries, no closes | Fixed tiers + 1h response + 24h follow-up |

---

## Expected Output Format

### Margin Audit
[Commission by platform, margin per order, shift opportunity]

### Direct Playbook
[First-party page + Google ordering + QR upsell actions]

### Catering Kit
[JSON: tiers, minimums, lead times, triggers, owners]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Order funnel drop-off | Visits → order starts → checkouts | no |
| doddle.tool.v1.meta-ads.adsInsights | Retargeting to direct page | CTR, ROAS by direct-order campaign | no |

If tool unavailable, show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate rates.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| conversion-optimizer | Order funnel audit | Heuristic scores |
| continuity-specialist | Catering + repeat order flows | Retention plays |
| copywriter | Menu + upsell copy | Short-form CTAs |

---

## Related Skills

- `restaurant-reservations` - Fill tables alongside takeout growth
- `offers` - First-direct-order perks and bundles
- `page-cro` - Ordering page conversion fundamentals

---

## Questions to Ask

1. Venue, cuisine, avg ticket, current direct vs aggregator mix?
2. Ordering stack + Google food ordering live? (or grant analytics access?)
3. Catering capacity, minimums, lead times?
