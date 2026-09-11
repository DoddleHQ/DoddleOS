# Skills Dependency Matrix

This file maps relationships between skills, helping identify which skills work together and when to activate multiple skills for complex tasks.

## Skill Categories

| Category | Skills | Primary Use |
|----------|--------|-------------|
| **TOFU (Top of Funnel)** | seo-mastery, social-media, paid-advertising, content-strategy, programmatic-seo | Traffic generation |
| **MOFU (Middle of Funnel)** | email-marketing, email-sequence, lead-qualifier | Lead nurturing |
| **BOFU (Bottom of Funnel)** | page-cro, form-cro, signup-flow-cro, conversion-copywriting | Conversion optimization |
| **Retention** | onboarding-cro, paywall-upgrade-cro, referral-program | Customer success |
| **Brand** | brand-building, marketing-psychology, copywriting | Brand equity |
| **Research** | marketing-fundamentals, marketing-ideas, competitor-alternatives | Market intelligence |

## Dependency Map

### SEO Ecosystem
```
seo-mastery
├── programmatic-seo (scales SEO)
├── schema-markup (technical SEO)
├── competitor-alternatives (content SEO)
└── content-strategy (content SEO)

MCP Tools: google-search-console, semrush, dataforseo
```

### CRO Ecosystem
```
page-cro
├── form-cro (form optimization)
├── signup-flow-cro (registration flows)
├── popup-cro (overlay optimization)
├── paywall-upgrade-cro (in-app monetization)
├── ab-test-setup (testing changes)
└── copywriting (copy improvements)

MCP Tools: google-analytics, hotjar (if available)
```

### Email Ecosystem
```
email-marketing
├── email-sequence (drip campaigns)
├── onboarding-cro (post-signup emails)
└── referral-program (email-driven referrals)

MCP Tools: hubspot, mailchimp (if available)
```

### Content Ecosystem
```
content-strategy
├── copywriting (content creation)
├── copy-editing (content refinement)
├── seo-mastery (content optimization)
├── social-media (content distribution)
└── email-sequence (content delivery)

MCP Tools: notion, asana
```

### Paid Advertising Ecosystem
```
paid-advertising
├── page-cro (landing page optimization)
├── form-cro (lead capture)
├── ab-test-setup (ad testing)
└── analytics-attribution (performance tracking)

MCP Tools: meta-ads, google-ads (if available)
```

### Add-on Pack Ecosystems (DoddleOS v2 blueprints)
```
doddle-ecommerce-skills/ (doddle.ecommerce.* v1.5.1)
├── ecommerce-plp → page-cro, seo-mastery, schema-markup
├── ecommerce-pdp → page-cro, copywriting, schema-markup
├── ecommerce-checkout → form-cro, popup-cro, email-sequence
├── ecommerce-search → seo-mastery, page-cro, analytics-attribution
└── ecommerce-revenue → pricing-strategy, paywall-upgrade-cro
Commands: /ecom:plp, /ecom:pdp, /ecom:checkout, /ecom:search, /ecom:revenue
```
doddle-ecommerce-skills/ (doddle.ecommerce.* v1.5.1)
├── ecommerce-plp → page-cro, seo-mastery, schema-markup
├── ecommerce-pdp → page-cro, copywriting, schema-markup
├── ecommerce-checkout → form-cro, popup-cro, email-sequence
├── ecommerce-search → seo-mastery, page-cro, analytics-attribution
└── ecommerce-revenue → pricing-strategy, paywall-upgrade-cro

doddle-local-skills/ (doddle.local.* v1.0.0)
├── local-gbp → seo-mastery (+references/local-seo.md)
├── local-reviews → email-sequence, sms
├── local-pages → programmatic-seo, schema-markup
├── local-booking → form-cro, email-sequence, sms
└── local-ads → paid-advertising, analytics-attribution
New integration: google-business-profile (stub)

doddle-saas-skills/ (doddle.saas.* v1.0.0)
├── saas-homepage → page-cro, copywriting
├── saas-pricing → pricing-strategy, paywall-upgrade-cro
├── saas-trial → signup-flow-cro, onboarding-cro, revops
├── saas-retention → churn-prevention, email-sequence
└── saas-expansion → referral-program, product-led-growth
New integration: stripe (stub)

doddle-healthcare-skills/ (doddle.health.* v1.0.0)
├── healthcare-booking → local-booking, form-cro, sms
├── healthcare-recall → email-sequence, sms
├── healthcare-intake → form-cro
├── healthcare-reputation → local-reviews, local-gbp
└── healthcare-ads → local-ads, paid-advertising
Compliance: HIPAA-style no-PHI checkpoint in every skill
```

doddle-real-estate-skills/ (doddle.realty.* v1.0.0)
├── realty-listings → programmatic-seo, schema-markup, copywriting
├── realty-valuation → lead-magnets, form-cro, email-sequence
├── realty-openhouse → events, email-sequence, sms
├── realty-nurture → email-sequence, sms
└── realty-referrals → referral-program, local-reviews
Compliance: fair-housing checkpoint in every skill
```

doddle-b2b-skills/ (doddle.b2b.* v1.0.0)
├── b2b-outbound → cold-email, customer-research, revops
├── b2b-proposals → pricing-strategy, offers
├── b2b-cases → copywriting (sales-enabler agent)
├── b2b-retainers → pricing-strategy, churn-prevention
└── b2b-partnerships → partnerships, referral-program
No new integration (hubspot/slack/notion/stripe exist)
```

doddle-restaurant-skills/ (doddle.restaurant.* v1.0.0)
├── restaurant-reservations → local-booking, form-cro, sms
├── restaurant-ordering → page-cro, offers
├── restaurant-loyalty → email-sequence, sms
├── restaurant-events → events (+ b2b-proposals for corporate)
└── restaurant-reputation → local-reviews, local-gbp
```

doddle-hr-skills/ (doddle.hr.* v1.0.0) — first people-ops pack
├── hr-recruiting → copywriting, customer-research
├── hr-screening → form-cro (knockout patterns)
├── hr-onboarding → onboarding-cro, email-sequence
├── hr-culture → brand-building (values), continuity patterns
└── hr-brand → brand-building, social-media
No new integration (notion/asana/slack/crosspost exist)
```

doddle-sales-skills/ (doddle.sales.* v1.0.0) — extends existing /sales:* (no new namespace)
├── sales-prospecting → cold-email, customer-research, revops
├── sales-discovery → revops, lead-qualifier (skill)
├── sales-negotiation → pricing-strategy, offers
├── sales-forecasting → revops, analytics-attribution
└── sales-enablement → product-marketing, copywriting
```

doddle-creator-skills/ (doddle.creator.* v1.0.0)
├── creator-ideation → marketing-ideas, customer-research
├── creator-scripting → video-marketing, conversion-copywriting
├── creator-packaging → image, copywriting, ab-test-setup
├── creator-publishing → social-media, content-strategy
└── creator-monetization → offers, pricing-strategy, partnerships
No new integration (tiktok/crosspost/semrush/notion exist)
```

doddle-legal-skills/ (doddle.legal.* v1.0.0)
├── legal-intake → form-cro, lead-qualifier (skill)
├── legal-guides → seo-mastery, programmatic-seo, copywriting
├── legal-consults → local-booking, email-sequence, sms
├── legal-reputation → local-reviews, local-gbp
└── legal-referrals → referral-program, partnerships
Compliance: bar-rules checkpoint in every skill
```

doddle-finance-skills/ (doddle.finance.* v1.0.0)
├── finance-leads → lead-magnets, form-cro, offers
├── finance-onboarding → signup-flow-cro, onboarding-cro, form-cro
├── finance-reviews → local-reviews, local-gbp
├── finance-crosssell → email-sequence (+ upsell-maximizer agent)
└── finance-referrals → referral-program, partnerships
Compliance: no-guaranteed-returns + disclosure checkpoint in every skill
```

doddle-education-skills/ (doddle.edu.* v1.0.0)
├── edu-enrollment → form-cro, lead-qualifier (skill)
├── edu-openhouse → events, email-sequence, sms
├── edu-content → seo-mastery, programmatic-seo, copywriting
├── edu-nurture → email-sequence, sms
└── edu-alumni → referral-program, local-reviews
Compliance: student-privacy + honest-outcomes checkpoint in every skill
```

## Cross-Skill Workflows

### Campaign Launch Workflow
1. **research** → marketing-fundamentals, competitor-alternatives
2. **strategy** → content-strategy, pricing-strategy
3. **creation** → copywriting, email-sequence
4. **optimization** → page-cro, ab-test-setup
5. **measurement** → analytics-attribution

### Product Launch Workflow
1. **pre-launch** → launch-strategy, waitlist strategy
2. **launch** → paid-advertising, social-media, email-marketing
3. **post-launch** → onboarding-cro, email-sequence
4. **growth** → referral-program, community-building

### Conversion Optimization Workflow
1. **audit** → page-cro, form-cro, signup-flow-cro
2. **hypothesize** → marketing-psychology, conversion-copywriting
3. **test** → ab-test-setup
4. **measure** → analytics-attribution
5. **iterate** → repeat cycle

## Agent Collaboration Patterns

| Primary Agent | Should Collaborate With | When |
|---------------|------------------------|------|
| attraction-specialist | researcher, seo-specialist | TOFU strategy |
| lead-qualifier | email-wizard, sales-enabler | MOFU nurturing |
| email-wizard | copywriter, conversion-optimizer | Email optimization |
| continuity-specialist | upsell-maximizer, onboarding-cro | Retention |
| sales-enabler | researcher, brand-voice-guardian | Sales collateral |

## Skill Activation Triggers

### When user says... | Activate these skills
--- | ---
"landing page isn't converting" | page-cro, copywriting, ab-test-setup
"email open rates are low" | email-marketing, copywriting
"need more traffic" | seo-mastery, content-strategy, paid-advertising
"pricing feels wrong" | pricing-strategy, page-cro
"onboarding is confusing" | onboarding-cro, copywriting
"want to launch product" | launch-strategy, email-marketing, paid-advertising
"competitor comparison page" | competitor-alternatives, seo-mastery, copywriting
"referral program" | referral-program, email-marketing
"social media strategy" | social-media, content-strategy
"SEO audit" | seo-mastery, schema-markup, programmatic-seo

## Priority Matrix

| Skill | Impact | Effort | Priority |
|-------|--------|--------|----------|
| page-cro | High | Medium | P0 |
| email-sequence | High | Low | P0 |
| seo-mastery | High | High | P1 |
| copywriting | High | Low | P0 |
| paid-advertising | Medium | Medium | P1 |
| social-media | Medium | Low | P1 |
| content-strategy | High | High | P1 |
| analytics-attribution | High | Medium | P1 |
| launch-strategy | Medium | Medium | P2 |
| referral-program | Medium | Medium | P2 |
