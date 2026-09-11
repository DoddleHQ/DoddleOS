---
name: seo-mastery
id: doddle.marketing.seo-mastery
version: 1.5.1
blueprint: ./blueprint.yaml
description: Search engine optimization strategies and tactics for organic growth. Use when optimizing content for search, conducting keyword research, performing SEO audits, or building link strategies.
---

# SEO Mastery

Search engine optimization strategies and tactics for sustainable organic growth.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply SEO expertise when:
- Optimizing content for search rankings
- Conducting keyword research
- Performing technical SEO audits
- Building link acquisition strategies
- Analyzing search performance
- Creating content strategies for organic growth

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| topic_or_url | string | yes | Topic or URL to optimize; ask if missing |
| keyword | string | no | Primary keyword; infer from topic if missing |
| locale | string | no | Locale for language/market context; default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | SEO audit with keyword, on-page, technical, link recommendations |
| action_list | json | Prioritized SEO actions with impact and effort |

---

## Core Concepts

### Search Intent Types

| Intent | User Goal | Content Type | Examples |
|--------|-----------|--------------|----------|
| Informational | Learn something | How-to, guides, definitions | "how to write email copy" |
| Navigational | Find specific site | Brand pages | "HubSpot login" |
| Commercial | Research before buying | Comparisons, reviews | "best email marketing tools" |
| Transactional | Complete purchase | Product pages, pricing | "buy mailchimp subscription" |

### Keyword Research Framework

**Keyword Metrics to Evaluate**:
| Metric | What It Means | Good Range |
|--------|--------------|------------|
| Search Volume | Monthly searches | 100-10,000 for most |
| Keyword Difficulty | Competition level | 0-30 for new sites |
| CPC | Commercial intent | Higher = more valuable |
| SERP Features | What's on page 1 | Fewer = easier |

**Keyword Types**:
- **Head Terms**: 1-2 words, high volume, very competitive
- **Body Terms**: 2-3 words, medium volume, competitive
- **Long-tail**: 4+ words, low volume, less competitive

### On-Page SEO Elements

**Title Tag** (50-60 characters):
- Primary keyword near front
- Compelling and click-worthy
- Unique per page
- Include brand (if room)

**Meta Description** (150-160 characters):
- Include primary keyword naturally
- Call-to-action
- Unique value proposition
- Match search intent

**Header Structure**:
```
H1: Main Page Title (one per page, contains keyword)
  H2: Major Section (keyword variations)
    H3: Subsection (semantic terms)
      H4: Supporting detail
```

**Content Optimization Checklist**:
- [ ] Keyword in first 100 words
- [ ] Natural keyword density (1-2%)
- [ ] Semantic variations throughout
- [ ] Internal links to related content (3-5 per post)
- [ ] External links to authoritative sources (1-2)
- [ ] Image alt text with keywords
- [ ] Short, descriptive URLs

### Technical SEO Essentials

**Core Web Vitals**:
| Metric | Target | What It Measures |
|--------|--------|------------------|
| LCP (Largest Contentful Paint) | <2.5s | Loading performance |
| FID (First Input Delay) | <100ms | Interactivity |
| CLS (Cumulative Layout Shift) | <0.1 | Visual stability |

**Crawlability Checklist**:
- [ ] XML sitemap submitted
- [ ] Clean robots.txt
- [ ] No broken links (4xx errors)
- [ ] Proper redirects (301 for permanent)
- [ ] Mobile-friendly design
- [ ] HTTPS enabled

**Indexability Checklist**:
- [ ] Canonical tags on duplicate pages
- [ ] No accidental noindex
- [ ] Hreflang for international
- [ ] Proper pagination handling

### Link Building Strategies

| Strategy | Effort | Impact | Best For |
|----------|--------|--------|----------|
| Guest Posting | High | Medium | New sites, authority |
| Broken Link Building | Medium | Medium | Quick wins |
| Resource Pages | Medium | Medium | Comprehensive content |
| Digital PR | High | High | Brand + links |
| Original Research | Very High | Very High | Thought leadership |
| HARO | Low | Variable | Easy opportunities |

### Content Clusters

**Pillar-Cluster Model**:
```
Pillar Page (comprehensive, 3000+ words)
├── Cluster 1 (specific subtopic, links to pillar)
├── Cluster 2 (specific subtopic, links to pillar)
├── Cluster 3 (specific subtopic, links to pillar)
└── Cluster N (specific subtopic, links to pillar)
```

**Benefits**:
- Establishes topical authority
- Improves internal linking
- Captures long-tail variations
- Better user navigation

## Best Practices

### Keyword Research Excellence
1. **Intent Match**: Align content with search intent
2. **Realistic Targets**: Start with achievable difficulty
3. **Cluster Thinking**: Group related keywords
4. **Commercial Balance**: Mix informational and transactional

### Content Excellence
1. **10x Content**: Be definitively better than page 1
2. **Comprehensive Coverage**: Answer all related questions
3. **Updated Regularly**: Refresh for freshness signals
4. **Multimedia Rich**: Images, videos, interactive elements

### Technical Excellence
1. **Speed Priority**: Fast sites rank better
2. **Mobile-First**: Google indexes mobile version
3. **Clean Architecture**: Logical URL and site structure
4. **Structured Data**: Schema markup for rich snippets

---

## Local SEO

### Local SEO Checklist
- [ ] Google Business Profile optimized
- [ ] NAP (Name, Address, Phone) consistent everywhere
- [ ] Local keywords in title tags and meta descriptions
- [ ] Location pages for each service area
- [ ] Local backlinks from community organizations
- [ ] Reviews strategy (generate and respond)
- [ ] Local schema markup (LocalBusiness)
- [ ] Google Maps integration

### Google Business Profile Optimization
| Element | Best Practice |
|---------|---------------|
| Business Name | Exact legal name, no keywords |
| Category | Most specific primary category |
| Description | 750 chars, keywords naturally |
| Hours | Accurate, holiday hours updated |
| Photos | High-quality, regular uploads |
| Posts | Weekly updates, offers, events |
| Q&A | Monitor and respond promptly |
| Reviews | Respond to all, positive and negative |

### Local Ranking Factors
| Factor | Weight | Optimization |
|--------|--------|--------------|
| Google Business Profile | 25% | Complete, accurate, active |
| Reviews | 15% | Quantity, quality, responses |
| On-Page SEO | 15% | Local keywords, NAP |
| Backlinks | 15% | Local, relevant links |
| Behavioral Signals | 10% | Click-through, calls |
| Citations | 10% | Consistent NAP across web |
| Personalization | 10% | User proximity, history |

### Local Content Strategy
- Create location-specific landing pages
- Write about local events and news
- Feature local customer stories
- Partner with local organizations
- Create local resource guides

---

## Voice Search Optimization

### Voice Search Characteristics
| Characteristic | Implication |
|----------------|-------------|
| Conversational queries | Use natural language |
| Question-based | Answer questions directly |
| Local intent | Optimize for "near me" |
| Featured snippets | Aim for position zero |
| Mobile-first | Fast, mobile-friendly |

### Voice Search Keyword Strategy
| Query Type | Example | Optimization |
|------------|---------|--------------|
| Question | "How do I..." | FAQ content |
| Near me | "Best [service] near me" | Local SEO |
| Action | "Call [business]" | Click-to-call |
| Comparison | "What's better, X or Y?" | Comparison content |
| Definition | "What is [term]" | Clear definitions |

### Voice Search Content Framework
1. **Answer questions directly**: Featured snippet format
2. **Use natural language**: Conversational tone
3. **Be concise**: 29-41 words average answer
4. **Structure for scanners**: Lists, tables, headers
5. **Local focus**: "Near me" optimization

### Schema Markup for Voice Search
| Schema Type | Use Case |
|-------------|----------|
| FAQPage | Question-answer content |
| HowTo | Step-by-step instructions |
| LocalBusiness | Local business information |
| Product | Product details |
| Review | Reviews and ratings |

---

## Agent Integration

| Agent | How They Use This Skill |
|-------|------------------------|
| `attraction-specialist` | Full SEO strategy and execution |
| `copywriter` | SEO-optimized content creation |
| `researcher` | Competitor SEO analysis |
| `docs-manager` | SEO documentation and audits |

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Wrong | Do This Instead |
|--------------|----------------|-----------------|
| Keyword stuffing | Hurts rankings, UX | Natural density |
| Buying links | Penalty risk | Earn links |
| Duplicate content | Cannibalization | Canonical or consolidate |
| Ignoring search intent | Poor engagement signals | Match intent exactly |
| Chasing only volume | Ignores conversion | Balance volume + intent |

## Metrics to Track

### Organic Traffic Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Organic Sessions | Traffic from search engines | Growing trend | Google Analytics |
| Organic Click-Through Rate | % clicking your result | >3% | Google Search Console |
| Impressions | Times shown in search | Growing trend | Google Search Console |
| Position/Average Rank | Average ranking position | Top 10 for target keywords | Google Search Console |

### Keyword Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Keyword Rankings | Positions for target keywords | Improving trend | SEMrush/Ahrefs |
| Keywords in Top 10 | # of ranking keywords | Growing | SEMrush/Ahrefs |
| Featured Snippets Owned | # of snippet positions | Growing | SEMrush/Ahrefs |
| Keyword Difficulty vs. Rank | Ranking vs. difficulty | Outperforming | SEMrush/Ahrefs |

### Technical SEO Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Core Web Vitals Score | LCP, FID, CLS | All "Good" | PageSpeed Insights |
| Crawl Errors | 4xx, 5xx errors | 0 | Google Search Console |
| Index Coverage | Pages indexed vs. submitted | >90% | Google Search Console |
| Mobile Usability Issues | Mobile problems | 0 | Google Search Console |

### Backlink Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Domain Authority/Rating | Overall site authority | Growing trend | Ahrefs/Moz |
| Referring Domains | # of linking domains | Growing | Ahrefs |
| New Backlinks | Links acquired per month | Positive net | Ahrefs |
| Toxic Backlinks | Harmful links | <5% | Ahrefs |

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Targeting only high-volume keywords | Too competitive for new sites | Mix head + long-tail |
| Ignoring search intent | Rankings but no clicks | Match content to intent |
| No content strategy | Random, no compounding | Build topic clusters |
| Ignoring technical SEO | Foundation problems | Fix technical first |

### On-Page Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Keyword stuffing | Penalties, poor readability | Natural, semantic variations |
| Duplicate content | Cannibalization | Canonical tags, consolidate |
| Thin content | No value to index | Comprehensive, detailed content |
| Slow page speed | Ranking factor | Optimize Core Web Vitals |

### Link Building Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Buying links | Penalty risk | Earn links through value |
| Low-quality directories | No value, potential spam | Quality over quantity |
| Ignoring internal linking | Missed ranking opportunities | Strategic internal links |
| No link diversity | Unnatural profile | Varied anchor text, sources |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Chasing vanity metrics | Traffic without conversions | Focus on conversion metrics |
| Ignoring competitor analysis | Missing opportunities | Regular competitor monitoring |
| No regular audits | Issues compound | Monthly technical audits |
| Not tracking rankings | Can't measure progress | Track target keywords weekly |

---

## Related Commands

- `/seo/keywords` - Keyword research
- `/seo/audit` - Comprehensive SEO audit
- `/seo/competitor` - Competitor SEO analysis
- `/seo/optimize` - Content optimization
- `/checklist/seo-weekly` - Weekly SEO maintenance

## References

- `references/keyword-research.md` - Keyword research methodology
- `references/on-page-seo.md` - On-page optimization checklist
- `references/technical-seo.md` - Technical SEO requirements
- `references/link-building.md` - Link acquisition strategies
- `references/local-seo.md` - Local search optimization
- `references/seo-audit-checklist.md` - Comprehensive audit framework

---

## Expected Output Format

### SEO Audit
[Keyword gaps, on-page scores, technical issues, link gaps]

### Optimization Strategy
[Prioritized fixes by impact and effort]

### Implementation Plan
[Steps and timeline]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.gsc.getSearchAnalytics | Search performance | Queries, CTR, position | no |
| doddle.tool.v1.semrush.keywordResearch | Keyword research | Volume, difficulty | no |
| doddle.tool.v1.dataforseo.serpGoogle | SERP analysis | Rankings, SERP features | no |
| doddle.tool.v1.ga4.getReport | Traffic behavior | Organic sessions, conversions | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| seo-specialist | Technical SEO, audits | Keyword, on-page, technical review |
| copywriter | SEO content creation | Optimized copy |
| researcher | Competitor analysis | SERP and competitor gaps |

---

## Questions to Ask

1. What topic or URL should be optimized?
2. What are your target keywords and search intent?
3. Do you have GSC / GA4 access, or should I proceed without live data?
