---
name: content-strategy
id: doddle.marketing.content-strategy
version: 1.5.1
blueprint: ./blueprint.yaml
description: Content planning, creation, and distribution strategy. Use when planning content calendars, developing content pillars, creating editorial strategies, or optimizing content for different funnel stages.
---

# Content Strategy

Content planning, creation, and distribution for sustainable organic growth.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply content strategy expertise when:
- Planning content calendars and editorial workflows
- Developing content pillars and themes
- Creating distribution strategies
- Mapping content to funnel stages
- Repurposing content across channels
- Measuring content performance

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Goals, pillars or topics, resources, timeframe |
| audience | string | no | Target audience or segment |
| channel | string | no | Delivery channel or page context |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| draft | markdown | Content plan, see Expected Output Format |
| variants | json | Alternative angles and repurposing options with rationale |

---

## Core Concepts

### Content Pillars

Content pillars are the main themes your content revolves around.

**Criteria for Strong Pillars**:
- Aligned with business goals
- Relevant to audience pain points
- Differentiates from competitors
- Sustainable long-term (evergreen potential)
- SEO opportunity (search volume)

**Example Pillar Structure**:
| Pillar | Purpose | Content Types |
|--------|---------|---------------|
| Industry Insights | Thought leadership | Reports, trends, analysis |
| How-To/Tutorials | Education | Guides, videos, templates |
| Customer Success | Social proof | Case studies, testimonials |
| Product Updates | Awareness | Release notes, feature deep-dives |
| Company Culture | Employer brand | Behind-scenes, team stories |

### Content by Funnel Stage

| Stage | Goal | Content Type | Format | CTA |
|-------|------|--------------|--------|-----|
| TOFU (Awareness) | Attract | Blog posts, social, video | Short, shareable | Subscribe, Follow |
| MOFU (Consideration) | Educate | Ebooks, webinars, guides | In-depth, gated | Download, Register |
| BOFU (Decision) | Convert | Case studies, demos, comparisons | Specific, proof-heavy | Trial, Demo, Buy |
| Retention | Retain | Tutorials, community, newsletters | Ongoing value | Upgrade, Refer |

### Content Mix Framework

**70-20-10 Rule**:
- 70% proven content (what works, repeat it)
- 20% iterative improvements (variations on winners)
- 10% experimental (new formats, topics, channels)

**Content Type Mix**:
- 40% Educational (builds trust)
- 30% Engaging (builds community)
- 20% Inspirational (builds connection)
- 10% Promotional (drives action)

### Content Calendar Structure

**Weekly Cadence Example**:
| Day | Primary Channel | Content Type | Goal |
|-----|-----------------|--------------|------|
| Monday | Blog | Educational | SEO traffic |
| Tuesday | LinkedIn | Thought leadership | B2B engagement |
| Wednesday | Email | Nurture | Subscriber retention |
| Thursday | Social | Community | Engagement |
| Friday | Video | Educational | Multi-channel |

### Content Repurposing Matrix

| Original | → Blog Post | → Social | → Email | → Video |
|----------|-------------|----------|---------|---------|
| Webinar | Recap post | Key quotes | Summary | Clips |
| Case Study | Detailed post | Stats carousel | Teaser | Interview |
| Research Report | Analysis post | Data graphics | Key findings | Explainer |
| Podcast | Transcript post | Audiograms | Highlights | Video version |

---

## Content Distribution Playbook

### Distribution Framework

**The 80/20 Rule:**
- 20% creation, 80% promotion
- Every piece needs a distribution plan
- Repurpose aggressively
- Build distribution into process

### Distribution Channels

| Channel | Type | Best For | Effort |
|---------|------|----------|--------|
| Organic Search | SEO | Long-term, evergreen | High |
| Social Media | Organic | Engagement, community | Medium |
| Email | Owned | Nurture, retention | Low |
| Paid Social | Paid | Reach, targeting | Medium |
| Content Syndication | Partner | Reach, backlinks | Low |
| Community | Organic | Niche, engagement | Medium |
| Influencer | Partner | Credibility, reach | High |

### Distribution Timeline

**Week 1: Launch**
| Day | Channel | Action |
|-----|---------|--------|
| Day 1 | Email | Send to subscribers |
| Day 1 | Social | Share across platforms |
| Day 1 | Community | Post in relevant groups |
| Day 2 | Outreach | Notify mentioned people |
| Day 3 | Paid | Boost top-performing post |

**Week 2-4: Amplify**
| Day | Channel | Action |
|-----|---------|--------|
| Week 2 | Syndication | Republish on Medium, LinkedIn |
| Week 2 | Influencer | Share with industry experts |
| Week 3 | Social | Repurpose key quotes |
| Week 3 | Email | Include in newsletter |
| Week 4 | Paid | Retarget visitors |

**Month 2+: Sustain**
| Day | Channel | Action |
|-----|---------|--------|
| Monthly | Social | Reshare with new angle |
| Monthly | Email | Include in digest |
| Quarterly | Update | Refresh and update |

### Channel-Specific Distribution

**LinkedIn Distribution:**
- Share as native document/carousel
- Key insights in comments
- Tag mentioned people/companies
- Engage with all comments
- Post 2-3x in first week

**Twitter/X Distribution:**
- Thread with key takeaways
- Individual quote cards
- Engage in relevant conversations
- Quote tweet with insights
- Post 5-7x in first week

**Email Distribution:**
- Send to full list (Day 1)
- Segment by interest
- Include in weekly digest
- Add to nurture sequences
- Follow up with related content

**Community Distribution:**
- Share in relevant Slack/Discord groups
- Post in Reddit communities
- Submit to niche forums
- Engage in Facebook groups
- Provide value, not just links

### Content Syndication Strategy

| Platform | Format | Best For | Tips |
|----------|--------|----------|------|
| Medium | Full article | Reach, SEO | Add canonical tag |
| LinkedIn Articles | Full article | B2B reach | Native publishing |
| Hacker News | Link | Tech audience | Title optimization |
| Reddit | Link + context | Niche communities | Provide value first |
| Quora | Answer + link | Intent traffic | Answer questions thoroughly |

### Paid Amplification

**When to Boost Content:**
- High organic engagement
- Strong conversion potential
- Important announcement
- Competitive keyword target

**Budget Allocation:**
| Content Type | % of Budget | Goal |
|--------------|-------------|------|
| Evergreen | 40% | Long-term traffic |
| Product launches | 30% | Awareness |
| Case studies | 20% | Conversion |
| Trending topics | 10% | Reach |

### Distribution Metrics

| Metric | Target | Tool |
|--------|--------|------|
| Traffic by Source | Track channel contribution | Google Analytics |
| Social Shares | Growing trend | Social analytics |
| Backlinks Earned | Quality links | Ahrefs |
| Email Clicks | >2% CTR | ESP |
| Community Engagement | Comments, discussions | Manual tracking |

---

## Best Practices

### Planning Excellence
1. **Audience-First**: Research pain points before creating
2. **Keyword Integration**: SEO considerations in topic selection
3. **Competitive Gap**: What are competitors NOT covering?
4. **Resource Reality**: Plan for actual capacity, not aspirations

### Creation Excellence
1. **Hook First**: Lead with value, not background
2. **Scannable Format**: Headers, bullets, visuals
3. **One CTA per Piece**: Clear next step
4. **Evergreen Priority**: Maximize content lifespan

### Distribution Excellence
1. **Channel-Native**: Adapt format per platform
2. **Timing Optimization**: Post when audience is active
3. **Promotion Balance**: 20% creation, 80% promotion
4. **Amplification Partners**: Influencers, communities, syndication

## Agent Integration

| Agent | How They Use This Skill |
|-------|------------------------|
| `planner` | Building content calendars and editorial plans |
| `copywriter` | Creating content aligned with strategy |
| `attraction-specialist` | SEO-optimized content creation |
| `email-wizard` | Email content aligned with nurture goals |

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Wrong | Do This Instead |
|--------------|----------------|-----------------|
| Creating without strategy | Random content, no compounding | Define pillars first |
| All BOFU content | Ignores 97% not ready to buy | Full-funnel approach |
| Publish and forget | Wastes content investment | Promote and repurpose |
| Quantity over quality | Dilutes brand, wastes resources | Better content, less often |
| Ignoring data | Repeating what doesn't work | Analyze and iterate |

## Metrics to Track

### Content Performance Metrics
| Stage | Key Metrics | Good Benchmark | Tool |
|-------|-------------|----------------|------|
| TOFU | Traffic, reach, impressions | +10% MoM growth | Google Analytics |
| MOFU | Downloads, signups, engagement | 2-5% conversion | Google Analytics |
| BOFU | Demos, trials, influenced revenue | 10-20% of pipeline | CRM |
| Overall | Content ROI, CAC impact | 3:1 return | Finance + Analytics |

### Content Efficiency Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Content Velocity | Pieces published per month | Sustainable pace | Editorial calendar |
| Content Utilization | % of content being used/promoted | >80% | Content audit |
| Repurpose Ratio | # of pieces from one source | >5x | Manual tracking |
| Time to Publish | Creation to live | <1 week | Project management |

### Audience Growth Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Email List Growth | New subscribers from content | >10% monthly | ESP |
| Organic Traffic Growth | Search visitors | >15% quarterly | Google Analytics |
| Social Following Growth | Platform subscribers | >5% monthly | Platform analytics |
| Return Visitor Rate | Coming back for more | >30% | Google Analytics |

### Revenue Attribution Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Content-Influenced Pipeline | Deals touching content | Track trend | CRM |
| Content Attribution Model | Multi-touch vs. last-click | Implement model | Analytics |
| Cost per Content Lead | Spend per lead from content | Below sales lead cost | Finance |
| Content LTV Impact | Lifetime value of content leads | Higher than non-content | CRM |

---

## Related Commands

- `/campaign/calendar` - Generate content calendar
- `/content/blog` - Create SEO-optimized blog post
- `/content/social` - Create platform-specific social content

## References

- `references/content-pillars.md` - Building pillar strategy
- `references/editorial-calendar.md` - Calendar planning
- `references/repurposing.md` - Content multiplication
- `references/distribution.md` - Amplification strategies

---

## Expected Output Format

Structure your response as:

### Content Pillars
[3-5 pillars with purpose and formats]

### Content Calendar
[Cadence by channel with goals]

### Distribution Plan
[Launch, amplify, sustain per piece]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Random acts of content | No compounding results | Define pillars first |
| Publish and forget | Low ROI per piece | Attach distribution plan to every piece |
| All BOFU | Ignores 97% not ready to buy | Full-funnel mix |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.notion.pages | Calendars, briefs, content docs | Plans, drafts | no |
| doddle.tool.v1.hubspot.contacts | Audience segments, lifecycle | Segment sizes, conversion data | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| planner | Calendar building | Editorial plans, timelines |
| copywriter | Content creation | Drafts aligned to strategy |
| attraction-specialist | SEO content | Keyword-mapped topics |
| email-wizard | Nurture alignment | Email content planning |

---

## Related Skills

- **copywriting**: For creating pillar and funnel content
- **email-sequence**: For nurture sequences distributing content
- **seo-mastery**: For keyword and search strategy
- **social-media**: For channel-native distribution

---

## Questions to Ask

1. Business goal and how content success is measured?
2. Target audience and their top pain points?
3. Existing pillars, resources, and publishing capacity?
4. Priority channels and current performance baseline?
