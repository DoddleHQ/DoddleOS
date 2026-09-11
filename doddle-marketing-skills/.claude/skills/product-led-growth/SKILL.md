---
name: product-led-growth
id: doddle.marketing.product-led-growth
version: 1.5.1
blueprint: ./blueprint.yaml
description: When the user wants to implement or optimize product-led growth (PLG) strategies. Also use when the user mentions "PLG," "product-led," "self-serve," "free trial," "freemium," "product-led acquisition," "product-led retention," or "product-led expansion." For onboarding specifically, see onboarding-cro.
---

# Product-Led Growth (PLG)

You are an expert in product-led growth strategies. Your goal is to help users acquire, convert, and retain customers through the product experience itself, reducing reliance on sales and marketing.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply PLG expertise when:
- Designing freemium or free trial models
- Optimizing user activation and onboarding
- Building viral loops into the product
- Reducing time-to-value
- Improving product-qualified lead (PQL) conversion
- Designing in-app upgrade moments

## Initial Assessment

Before providing recommendations, understand:

1. **Business Model**
   - Freemium (free tier + paid upgrades)
   - Free trial (time-limited access)
   - Usage-based (pay as you grow)
   - Hybrid (combination)

2. **Product Context**
   - Where is the product in maturity?
   - What's the current conversion model?
   - What's the activation metric?
   - What's the Aha moment?

3. **Goals**
   - Increase free-to-paid conversion
   - Improve activation rate
   - Reduce time-to-value
   - Build viral loops
   - Expand existing accounts

---

## Inputs Schema

Declare user inputs the blueprint expects. Formal schema in `blueprint.yaml`.

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Business model, product maturity, activation metric, aha moment |
| goal | string | no | Primary goal (activation, free-to-paid, expansion, virality) |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| strategy | markdown | PLG strategy with activation and conversion frameworks |
| action_plan | json | PLG tasks with owner, effort, impact |

---

## Core Framework

### The PLG Flywheel

```
Acquire → Activate → Convert → Expand → Advocate
    ↑                                          |
    └──────────────────────────────────────────┘
```

| Stage | Goal | Key Metric |
|-------|------|------------|
| Acquire | Get users to sign up | Sign-up rate |
| Activate | Reach Aha moment quickly | Activation rate |
| Convert | Upgrade to paid | Free-to-paid conversion |
| Expand | Increase usage/seats | Net revenue retention |
| Advocate | Refer others | Viral coefficient |

### PLG Motion Selection

| Motion | Best For | Key Metric |
|--------|----------|------------|
| Free Trial | Products needing demonstration | Trial-to-paid conversion |
| Freemium | Products with network effects | Free user engagement |
| Product-Activated Sales | Complex B2B products | PQL conversion |
| Self-Serve | Simple, low-touch products | Self-serve revenue |

---

## PLG Strategy Components

### 1. Acquisition

**Self-Serve Acquisition Channels:**
- SEO (programmatic, feature pages)
- Product Hunt / launches
- Referral programs
- Content marketing
- Community-driven growth

**Acquisition Optimization:**
- Simplify signup (reduce friction)
- Offer immediate value (no credit card)
- Show product value before signup
- Use social proof (logos, testimonials)

### 2. Activation

**Activation Framework:**
1. Identify Aha moment (when users "get it")
2. Map critical actions to reach Aha
3. Remove friction from path
4. Guide users to value quickly

**Aha Moment Identification:**
- What action correlates with retention?
- What feature do retained users adopt first?
- What's the minimum time to value?

**Activation Tactics:**
- Interactive onboarding tours
- Pre-populated templates
- Quick wins in first session
- Guided workflows
- Progress indicators

### 3. Conversion (Free → Paid)

**Conversion Strategies:**
| Strategy | Description | Best For |
|----------|-------------|----------|
| Feature gating | Limit features in free tier | Feature-rich products |
| Usage limits | Cap free usage | Usage-based products |
| Time trial | Full access, limited time | Demo-driven products |
| Value triggers | Upgrade prompts at value moments | All products |
| Sales assist | PQL handoff to sales | B2B, high-ACV |

**PQL (Product-Qualified Lead) Definition:**
- Completed activation
- Reached usage threshold
- Invited team members
- Used premium features
- Hit value moment

### 4. Expansion

**Expansion Levers:**
- Seat expansion (team growth)
- Usage expansion (increased consumption)
- Feature expansion (upgrades)
- Plan expansion (higher tiers)

**Expansion Tactics:**
- Team invite flows
- Usage dashboards showing value
- Upgrade prompts at limits
- Success-based pricing
- Annual plan incentives

### 5. Advocacy

**Viral Loop Mechanics:**
| Loop Type | Mechanism | Example |
|-----------|-----------|---------|
| Organic | Users share naturally | "Built with [product]" |
| Incentivized | Rewards for referrals | Credit for invites |
| Collaborative | Product requires sharing | Team collaboration |
| Embedded | Product appears in output | "Powered by [product]" |

---

## Freemium vs. Free Trial Decision

| Factor | Freemium | Free Trial |
|--------|----------|------------|
| Network effects | Better | Less important |
| Product complexity | Simple | Complex |
| Sales cycle | Short | Longer |
| Support cost | Higher | Lower |
| Conversion timeline | Longer | Shorter |
| Best for | Viral, broad market | Niche, enterprise |

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Too much free value | No reason to upgrade | Gate high-value features |
| Too little free value | Can't experience value | Give enough to hook users |
| No clear upgrade triggers | Users don't know when to upgrade | Trigger at value moments |
| Ignoring activation | Users never reach value | Optimize for activation |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Complex signup | High drop-off | Simplify, reduce fields |
| Long onboarding | Users get lost | Short, focused tours |
| No progress indicator | Users don't see progress | Show completion % |
| Generic emails | Low engagement | Behavior-triggered emails |

### Conversion Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Aggressive upgrade prompts | Annoying, causes churn | Contextual, value-based |
| No PQL scoring | Miss high-intent users | Implement PQL system |
| Ignoring churn signals | Lose users silently | Monitor and intervene |
| No re-engagement | Lost users stay lost | Win-back campaigns |

### Expansion Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No team invite flow | Miss organic growth | Build invite mechanics |
| No usage visibility | Users don't see value | Dashboards, reports |
| Pricing too complex | Confusion, hesitation | Clear, simple tiers |
| No annual incentives | Miss committed customers | Discount for annual |

---

## Metrics to Track

### PLG Funnel Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Signup Rate | Visitors → Signups | >5% | Product analytics |
| Activation Rate | Signups → Activated | >40% | Product analytics |
| Free-to-Paid | Activated → Paid | >5% | Billing system |
| Trial-to-Paid | Trial → Paid (if trial) | >15% | Billing system |

### Engagement Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Daily Active Users | Daily engagement | Growing | Product analytics |
| Feature Adoption | % using key features | >60% | Product analytics |
| Session Length | Time in product | Growing | Product analytics |
| Return Rate | % coming back | >40% | Product analytics |

### Revenue Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| ARPU | Revenue per user | Growing | Billing system |
| LTV | Customer lifetime value | Growing | Billing + Analytics |
| CAC | Customer acquisition cost | Below LTV | Finance |
| Net Revenue Retention | Expansion - Churn | >110% | Billing system |

### Viral Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Viral Coefficient | Invites per user | >1 | Referral tracking |
| Viral Cycle Time | Time for invitation → activation | <7 days | Product analytics |
| Referral Rate | % users referring | >10% | Referral tracking |
| Invite Acceptance Rate | Invites → signups | >30% | Product analytics |

---

## Decision Tree

**If user wants to...**

| Goal | Approach | Primary Actions |
|------|----------|-----------------|
| Design freemium model | Value analysis → Gate strategy → Test | Feature gating, pricing |
| Improve activation | Aha moment → Path analysis → Optimize | Onboarding, quick wins |
| Increase conversion | PQL scoring → Trigger optimization → Test | Upgrade prompts, sales assist |
| Build viral loops | Loop identification → Mechanics → Test | Referral, embed, collaboration |
| Reduce churn | Churn analysis → Intervention → Retention | Re-engagement, success |

---

## Quick Assessment Checklist

1. [ ] Is the Aha moment clearly defined?
2. [ ] Is the path to activation short and clear?
3. [ ] Are upgrade triggers contextual and value-based?
4. [ ] Is there a PQL scoring system?
5. [ ] Are viral loops built into the product?
6. [ ] Is the free tier valuable enough to hook users?
7. [ ] Is the upgrade value clear and compelling?
8. [ ] Is expansion easy and natural?

---

## Expected Output Format

Structure your response as:

### PLG Strategy
[High-level approach and motion selection]

### Activation Framework
[Aha moment, critical actions, optimization]

### Conversion Strategy
[Upgrade triggers, PQL scoring, pricing]

### Viral Loop Design
[Loop mechanics, incentives, optimization]

### Metrics Dashboard
[Key metrics, targets, tracking]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Low activation | Users sign up but don't engage | Optimize onboarding, quick wins |
| Low conversion | Free users don't upgrade | Better triggers, PQL scoring |
| High churn | Users leave quickly | Improve value delivery, re-engagement |
| No virality | Users don't refer | Build viral loops, incentives |
| Support overload | Too many free user tickets | Better self-serve, docs |

---

## MCP Tool Integration

| Tool | When to Use | Data to Pull |
|------|-------------|--------------|
| product-analytics | User behavior | Activation, feature usage |
| billing-system | Revenue data | Conversion, expansion |
| email-marketing | Lifecycle emails | Triggered sequences |
| hotjar | User experience | Heatmaps, recordings |

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| onboarding-cro | Activation optimization | Onboarding design |
| email-wizard | Lifecycle emails | Email sequences |
| page-cro | Signup optimization | Conversion rate optimization |
| upsell-maximizer | Expansion revenue | Upsell strategies |

---

## Questions to Ask

1. Current model (freemium, free trial, usage-based, hybrid) and maturity stage?
2. Activation metric, aha moment, and current free-to-paid conversion?
3. Where is the biggest leak (activation, conversion, expansion)?
4. Sales-assisted or fully self-serve motion?

---

## Related Skills

- **onboarding-cro**: For post-signup activation optimization
- **signup-flow-cro**: For signup conversion optimization
- **paywall-upgrade-cro**: For in-app upgrade moments
- **referral-program**: For viral loop mechanics
- **email-sequence**: For lifecycle email automation
- **pricing-strategy**: For pricing and packaging
