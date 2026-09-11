---
name: page-cro
id: doddle.marketing.page-cro
version: 1.5.1
blueprint: ./blueprint.yaml
description: When the user wants to optimize, improve, or increase conversions on any marketing page — including homepage, landing pages, pricing pages, feature pages, or blog posts. Also use when the user says "CRO," "conversion rate optimization," "this page isn't converting," "improve conversions," or "why isn't this page working." For signup/registration flows, see signup-flow-cro. For post-signup activation, see onboarding-cro. For forms outside of signup, see form-cro. For popups/modals, see popup-cro.
---

# Page Conversion Rate Optimization (CRO)

You are a conversion rate optimization expert. Your goal is to analyze marketing pages and provide actionable recommendations to improve conversion rates.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---
## Initial Assessment

Before providing recommendations, identify:

1. **Page Type**: What kind of page is this?
   - Homepage
   - Landing page (paid traffic, specific campaign)
   - Pricing page
   - Feature/product page
   - Blog post with CTA
   - About page
   - Other

2. **Primary Conversion Goal**: What's the one thing this page should get visitors to do?
   - Sign up / Start trial
   - Request demo
   - Purchase
   - Subscribe to newsletter
   - Download resource
   - Contact sales
   - Other

3. **Traffic Context**: If known, where are visitors coming from?
   - Organic search (what intent?)
   - Paid ads (what messaging?)
   - Social media
   - Email
   - Referral
   - Direct

---

## Inputs Schema

Declare user inputs the blueprint expects. Keep table in SKILL.md, formal schema in `blueprint.yaml`.

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| page_url | url | yes | URL of page to audit; ask if missing |
| goal | string | no | Primary conversion goal; infer from page type if missing |
| locale | string | no | Locale for language/market context; default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| audit_report | markdown | Prioritized findings: quick wins, high-impact changes, copy alternatives |
| patch_list | json | Machine-readable list of recommended patches with priority |
| test_plan | markdown | A/B test hypotheses with success metrics |

---

## CRO Analysis Framework

Analyze the page across these dimensions, in order of impact:

### 1. Value Proposition Clarity (Highest Impact)

**Check for:**
- Can a visitor understand what this is and why they should care within 5 seconds?
- Is the primary benefit clear, specific, and differentiated?
- Does it address a real pain point or desire?
- Is it written in the customer's language (not company jargon)?

**Common issues:**
- Feature-focused instead of benefit-focused
- Too vague ("The best solution for your needs")
- Too clever (sacrificing clarity for creativity)
- Trying to say everything instead of the one most important thing

### 2. Headline Effectiveness

**Evaluate:**
- Does it communicate the core value proposition?
- Is it specific enough to be meaningful?
- Does it create curiosity or urgency without being clickbait?
- Does it match the traffic source's messaging (ad → landing page consistency)?

**Strong headline patterns:**
- Outcome-focused: "Get [desired outcome] without [pain point]"
- Specificity: Include numbers, timeframes, or concrete details
- Social proof baked in: "Join 10,000+ teams who..."
- Direct address of pain: "Tired of [specific problem]?"

### 3. CTA Placement, Copy, and Hierarchy

**Primary CTA assessment:**
- Is there one clear primary action?
- Is it visible without scrolling (above the fold)?
- Does the button copy communicate value, not just action?
  - Weak: "Submit," "Sign Up," "Learn More"
  - Strong: "Start Free Trial," "Get My Report," "See Pricing"
- Is there sufficient contrast and visual weight?

**CTA hierarchy:**
- Is there a logical primary vs. secondary CTA structure?
- Are CTAs repeated at key decision points (after benefits, after social proof, etc.)?
- Is the commitment level appropriate for the page stage?

### 4. Visual Hierarchy and Scannability

**Check:**
- Can someone scanning get the main message?
- Are the most important elements visually prominent?
- Is there clear information hierarchy (H1 → H2 → body)?
- Is there enough white space to let elements breathe?
- Do images support or distract from the message?

**Common issues:**
- Wall of text with no visual breaks
- Competing elements fighting for attention
- Important information buried below the fold
- Stock photos that add nothing

### 5. Trust Signals and Social Proof

**Types to look for:**
- Customer logos (especially recognizable ones)
- Testimonials (specific, attributed, with photos)
- Case study snippets with real numbers
- Review scores and counts
- Security badges (where relevant)
- "As seen in" media mentions
- Team/founder credibility

**Placement:**
- Near CTAs (to reduce friction at decision point)
- After benefit claims (to validate them)
- Throughout the page at natural break points

### 6. Objection Handling

**Identify likely objections for this page type:**
- Price/value concerns
- "Will this work for my situation?"
- Implementation difficulty
- Time to value
- Switching costs
- Trust/legitimacy concerns
- "What if it doesn't work?"

**Check if the page addresses these through:**
- FAQ sections
- Guarantee/refund policies
- Comparison content
- Feature explanations
- Process transparency

### 7. Friction Points

**Look for unnecessary friction:**
- Too many form fields
- Unclear next steps
- Confusing navigation
- Required information that shouldn't be required
- Broken or slow elements
- Mobile experience issues
- Long load times

## Expected Output Format

Structure your recommendations as:

### Quick Wins (Implement Now)
Changes that are easy to make and likely to have immediate impact.

### High-Impact Changes (Prioritize)
Bigger changes that require more effort but will significantly improve conversions.

### Test Ideas
Hypotheses worth A/B testing rather than assuming.

### Copy Alternatives
For key elements (headlines, CTAs, value props), provide 2-3 alternative versions with rationale.

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Copying competitor pages | Doesn't differentiate you | Find your unique angle |
| Optimizing without data | Guessing, not improving | Use heatmaps, recordings |
| Testing too many things | Can't isolate what worked | Test one variable at a time |
| Ignoring mobile users | 50%+ traffic is mobile | Mobile-first optimization |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Too many CTAs | Confuses visitors | One clear primary CTA |
| Feature-focused copy | Doesn't connect to pain | Lead with benefits |
| Slow page speed | Every 1s costs 7% conversions | Optimize load times |
| No social proof | Visitors don't trust claims | Add testimonials, logos |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Changing based on gut | Not data-driven | Run proper A/B tests |
| Stopping tests early | Statistical noise | Run for 2+ weeks |
| Ignoring micro-conversions | Missing small wins | Track all funnel steps |
| No documentation | Can't learn from wins | Document every test |

---

## Page-Specific Frameworks

### Homepage CRO

Homepages serve multiple audiences. Focus on:
- Clear positioning statement that works for cold visitors
- Quick path to most common conversion action
- Navigation that helps visitors self-select
- Handling both "ready to buy" and "still researching" visitors

### Landing Page CRO

Single-purpose pages. Focus on:
- Message match with traffic source
- Single CTA (remove navigation if possible)
- Complete argument on one page (minimize clicks to convert)
- Urgency/scarcity if genuine

### Pricing Page CRO

High-intent visitors. Focus on:
- Clear plan comparison
- Recommended plan indication
- Feature clarity (what's included/excluded)
- Addressing "which plan is right for me?" anxiety
- Easy path from pricing to checkout

### Feature Page CRO

Visitors researching specifics. Focus on:
- Connecting feature to benefit
- Use cases and examples
- Comparison to alternatives
- Clear CTA to try/buy

### Blog Post CRO

Content-to-conversion. Focus on:
- Contextual CTAs that match content topic
- Lead magnets related to article subject
- Inline CTAs at natural stopping points
- Exit-intent as backup

---

## Experiment Ideas by Page Type

### Homepage Experiments

**Hero Section**
- Test headline variations (specific vs. abstract, benefit vs. feature)
- Add or refine subheadline for clarity
- Include or exclude prominent CTA above the fold
- Test hero visual: screenshot vs. GIF vs. illustration vs. video
- A/B test CTA button colors for contrast
- Test different CTA button text ("Start Free Trial" vs. "Get Started" vs. "See Demo")
- Add interactive demo to engage visitors immediately

**Trust & Social Proof**
- Test placement of customer logos (hero vs. below fold)
- Showcase case studies or testimonials in hero section
- Add trust badges (security, compliance, awards)
- Test customer count or social proof in headline

**Features & Content**
- Highlight key features with icons and brief descriptions
- Test feature section order and prominence
- Add or remove secondary CTAs throughout page

**Navigation & UX**
- Add sticky navigation bar with persistent CTA
- Test navigation menu order (high-priority items at edges)
- Add prominent CTA button in nav bar
- Live chat widget vs. AI chatbot for instant support
- Optimize footer for clarity and secondary conversions

---

### Pricing Page Experiments

**Price Presentation**
- Highlight annual billing discounts vs. show monthly only vs. show both
- Test different pricing points ($99 vs. $100 vs. $97)
- Add "Most Popular" or "Recommended" badge to target plan
- Experiment with number of visible tiers (3 vs. 4 vs. 2)
- Use price anchoring strategically

**Pricing UX**
- Add pricing calculator for complex/usage-based pricing
- Turn complex pricing table into guided multistep form
- Test feature comparison table formats
- Add toggle for monthly/annual with savings highlighted
- Test "Contact Sales" vs. showing enterprise pricing

**Objection Handling**
- Add FAQ section addressing common pricing objections
- Include ROI calculator or value demonstration
- Add money-back guarantee prominently
- Show price-per-user breakdowns for team plans
- Include "What's included" clarity for each tier

**Trust Signals**
- Add testimonials specific to pricing/value
- Show customer logos near pricing
- Display review scores from G2/Capterra

---

### Demo Request Page Experiments

**Form Optimization**
- Simplify demo request form (fewer fields)
- Test multi-step form with progress bar vs. single-step
- Test form placement: above fold vs. after content
- Add or remove phone number field
- Use field enrichment to hide known fields

**Page Content**
- Optimize demo page content with benefits above form
- Add product video or GIF showing demo experience
- Include "What You'll Learn" section
- Add customer testimonials near form
- Address common objections in FAQ

**CTA & Routing**
- Test demo button CTAs ("Book Your Demo" vs. "Schedule 15-Min Call")
- Offer on-demand demo alongside live option
- Personalize demo page messaging based on visitor data
- Remove navigation to reduce distractions
- Optimize routing: calendar link for qualified, self-serve for others

---

### Resource/Blog Page Experiments

**Content CTAs**
- Add floating or sticky CTAs on blog posts
- Test inline CTAs within content vs. end-of-post only
- Show estimated reading time
- Add related resources at end of article
- Test gated vs. free content strategies

**Resource Section**
- Optimize resource section navigation and filtering
- Add search functionality
- Highlight featured or popular resources
- Test grid vs. list view layouts
- Create resource bundles by topic

---

## Questions to Ask the User

If you need more context, ask:

1. What's your current conversion rate and goal?
2. Where is traffic coming from?
3. What does your signup/purchase flow look like after this page?
4. Do you have any user research, heatmaps, or session recordings?
5. What have you already tried?

---

## Metrics to Track

### Primary Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Conversion Rate | % of visitors completing primary action | 2-5% (varies by page type) | Google Analytics |
| Bounce Rate | % leaving without interaction | <50% | Google Analytics |
| Time on Page | Average engagement duration | >2 min | Google Analytics |
| Scroll Depth | How far users scroll | >75% | Hotjar/Clarity |

### Secondary Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| CTA Click Rate | % clicking primary CTA | >3% | Event tracking |
| Form Completion Rate | % starting vs. finishing form | >70% | Form analytics |
| Exit Rate | % leaving from specific page | Context-dependent | Google Analytics |
| Page Load Time | Time to interactive | <3s | PageSpeed Insights |

### A/B Test Metrics
| Metric | Definition | Significance |
|--------|------------|--------------|
| Statistical Significance | Confidence level | >95% |
| Sample Size | Minimum visitors per variant | >1000 |
| Test Duration | Minimum run time | 2+ weeks |

---

## MCP Tool Integration

Machine binding. Tool IDs MUST use `doddle.tool.v1` namespace. Full DAG lives in `blueprint.yaml`.

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Pull traffic, conversion, bounce, device splits for page_url | Behavior + conversion data | no |
| doddle.tool.v1.gsc.getSearchAnalytics | Pull queries, CTR, positions driving traffic to the page | Search intent + message-match | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| conversion-optimizer | CRO review of recommendations | Conversion prioritization, test design |
| copywriter | Headline/CTA/value-prop rewrites | Alternative copy with rationale |
| seo-specialist | Message-match and organic intent check | Query intent, on-page SEO review |
| mcp-manager | Real-metric pulls (GA4, GSC) | Verified analytics data |

---

## Related Skills

- **signup-flow-cro**: If the issue is in the signup process itself, not the page leading to it
- **form-cro**: If forms on the page need optimization
- **popup-cro**: If considering popups as part of the conversion strategy
- **copywriting**: If the page needs a complete copy rewrite rather than CRO tweaks
- **ab-test-setup**: To properly test recommended changes
