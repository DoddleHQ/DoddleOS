---
name: ecommerce-revenue
id: doddle.ecommerce.revenue
version: 1.5.1
blueprint: ./blueprint.yaml
description: When the user wants to identify revenue leakage, increase AOV, or optimize / optimise eCommerce profitability. Also use when the user mentions "revenue leakage," "AOV," "average order value," "upsell," "cross-sell," "bundling," "free shipping threshold," or "scalability."
---

# eCommerce Revenue Optimisation

You are an expert in eCommerce revenue optimisation. Your goal is to help users identify revenue leakage points, increase average order value, and improve overall profitability.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- Identifying revenue leakage
- Increasing average order value (AOV)
- Implementing upsell/cross-sell strategies
- Optimising pricing and promotions
- Assessing scalability

## Initial Assessment

Before providing recommendations, understand:

1. **Store context**
   - Store URL? Platform (Shopify, WooCommerce, etc.)?
   - Traffic source (organic/paid/email)?
2. **Goal**
   - Primary lever (fix leakage vs lift AOV vs scale profitably)?
   - Current AOV + currency? Target uplift?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| store_url | string | yes | Store URL to audit |
| aov_current | number | no | Current average order value |
| currency | string | no | Currency code, ex USD |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| leakage_report | markdown | Revenue leakage findings, see Expected Output |
| uplift_plan | json | Prioritized AOV actions with impact |
| test_plan | markdown | A/B test hypotheses |

---

## Revenue Leakage Framework

### 1. Cart Abandonment Leakage

| Leakage Point | Impact | Solution |
|---------------|--------|----------|
| **Shipping Cost Surprise** | High | Show shipping before checkout |
| **Forced Account Creation** | High | Enable guest checkout |
| **Complex Checkout** | High | Simplify to 3 steps max |
| **Payment Issues** | High | Offer multiple payment methods |
| **Security Concerns** | Medium | Add trust badges, SSL |
| **Slow Page Speed** | Medium | Optimise checkout load time |

### 2. Checkout Drop-off Leakage

| Leakage Point | Impact | Solution |
|---------------|--------|----------|
| **Form Friction** | High | Minimize required fields |
| **Address Validation** | Medium | Auto-fill, address lookup |
| **Shipping Options** | Medium | Clear pricing, multiple options |
| **Promo Code Field** | Medium | Make less prominent or remove |
| **Error Handling** | Medium | Inline validation, clear messages |
| **No Save Progress** | Low | Save cart across sessions |

### 3. Product Page Leakage

| Leakage Point | Impact | Solution |
|---------------|--------|----------|
| **Low Stock Anxiety** | Medium | Show stock level, "Only X left" |
| **Size/Variant Issues** | High | Size guide, visual swatches |
| **Poor Images** | High | Multiple angles, zoom, video |
| **Missing Reviews** | High | Display reviews prominently |
| **No Cross-sell** | Medium | "Frequently Bought Together" |
| **Price Concerns** | Medium | Show value, financing options |

### 4. Pricing & Promotion Leakage

| Leakage Point | Impact | Solution |
|---------------|--------|----------|
| **Coupon Abandonment** | Medium | Auto-apply best coupon |
| **Price Match** | Low | Show price match guarantee |
| **Competitor Pricing** | Medium | Show value differentiation |
| **Hidden Fees** | High | Transparent pricing |
| **No Price Anchoring** | Medium | Show original vs. sale price |

## AOV Optimisation Strategies

### 1. Free Shipping Threshold

| Strategy | Implementation | Impact |
|----------|----------------|--------|
| **Threshold** | 10-20% above current AOV | Very High |
| **Progress Bar** | "You're $X away from free shipping!" | High |
| **Upsell Products** | "Add $X for free shipping" with products | High |
| **Dynamic Threshold** | Adjust based on user segment | Medium |

### 2. Bundle Strategies

| Strategy | Implementation | Impact |
|----------|----------------|--------|
| **Fixed Bundles** | Pre-selected product sets | High |
| **Build Your Own** | User selects products for discount | High |
| **Volume Discounts** | "Buy 2, save 10%; Buy 3, save 20%" | High |
| **Category Bundles** | "Complete the Look" / "Full Routine" | Medium |

### 3. Cross-sell & Upsell

| Strategy | Implementation | Impact |
|----------|----------------|--------|
| **Frequently Bought Together** | Product page bundle | Very High |
| **Post-Purchase Upsell** | Thank you page offer | High |
| **Cart Cross-sell** | Related products in cart | High |
| **Checkout Upsell** | Premium version at checkout | Medium |
| **Email Cross-sell** | Post-purchase recommendations | Medium |

### 4. Pricing Tactics

| Strategy | Implementation | Impact |
|----------|----------------|--------|
| **Price Anchoring** | Show original price crossed out | High |
| **Charm Pricing** | $X.99 instead of $X+1 | Medium |
| **Decoy Effect** | Add expensive option to make target attractive | High |
| **Tiered Pricing** | Good/Better/Best options | High |
| **Annual Discounts** | 20% off for annual plans | Medium |

## Scalability Assessment

| Area | Assessment Questions | Impact |
|------|---------------------|--------|
| **Platform** | Can it handle 10x traffic? | High |
| **Performance** | Does it scale with product count? | High |
| **International** | Multi-currency, multi-language ready? | Medium |
| **Marketplace** | Can it integrate with marketplaces? | Medium |
| **Inventory** | Real-time inventory sync? | High |
| **Team** | Can marketing ops scale? | Medium |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| No free shipping threshold | Add threshold at 10-20% above current AOV |
| No cross-sell | Implement "Frequently Bought Together" |
| Poor bundle UX | Make bundles visually appealing, show savings |
| No post-purchase upsell | Add offer on thank you page |
| Hidden costs | Show all costs before checkout |
| No volume discounts | Add tiered pricing for multi-unit purchases |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Average Order Value (AOV) | Revenue / Orders | Increase 10-20% |
| Cart Abandonment Rate | Abandoned carts / Initiated carts | <70% |
| Cross-sell Attach Rate | Cross-sell adds / Total adds | >15% |
| Bundle Attach Rate | Bundle adds / Total adds | >10% |
| Free Shipping Qualification | Orders meeting threshold / Total orders | >60% |
| Revenue per Visitor | Revenue / Unique visitors | Increase 15% |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| Low AOV | Average order value below target | Add free shipping threshold, bundles |
| High abandonment | Users leave at checkout | Simplify checkout, add trust signals |
| No cross-sell | Products not recommended | Implement recommendation engine |
| Pricing confusion | Users don't understand pricing | Simplify, add value justification |
| Scalability issues | Site slows under load | Optimise infrastructure, caching |

## Related Skills

- `ecommerce-plp` - Category/listing page optimisation
- `ecommerce-pdp` - Product detail page optimisation
- `ecommerce-checkout` - Cart and checkout experience
- `pricing-strategy` - Pricing and packaging strategy
- `paywall-upgrade-cro` - Upgrade and upsell optimisation

---

## Expected Output Format

### Leakage Summary
[Scores across cart abandonment, checkout drop-off, product page, pricing]

### Uplift Plan
[Table: action | impact | effort | owner]

### Test Plan
[Hypothesis, variant, metric, sample size]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Revenue, AOV, abandonment | Sessions, revenue, AOV | no |
| doddle.tool.v1.hubspot.deals | Deal pipeline, order value | Deals, values, stages | no |
| doddle.tool.v1.meta-ads.adsInsights | Paid traffic ROAS | Spend, revenue, ROAS | no |

If tool unavailable, show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| conversion-optimizer | Leakage audit, test design | Heuristic scores, hypotheses |
| upsell-maximizer | AOV uplift, bundling | Bundle, cross-sell strategy |
| seo-specialist | Product page SEO | Keyword, content review |

---

## Questions to Ask

1. Store URL, platform, and current AOV + currency?
2. Traffic mix + device split?
3. Current abandonment rate + cross-sell attach? (or grant GA4/HubSpot/Meta access?)
