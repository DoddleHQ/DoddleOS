# MCP Tool Integration Guide

This guide shows which MCP tools to use for each marketing skill.

---

## Quick Reference by Skill

| Skill | Primary MCP Tools | Secondary MCP Tools |
|-------|-------------------|---------------------|
| seo-mastery | Google Search Console, Semrush, DataForSEO | Google Analytics |
| page-cro | Google Analytics | Hotjar (if available) |
| email-marketing | HubSpot | - |
| email-sequence | HubSpot | - |
| social-media | Twitter, TikTok, Crosspost | - |
| content-strategy | Notion, Asana | - |
| paid-advertising | Meta Ads | Google Analytics |
| analytics-attribution | Google Analytics | HubSpot |
| brand-building | - | Notion |
| community-building | Slack, Discord | HubSpot |
| partnerships | HubSpot, Slack | Notion |

---

## SEO Tools Integration

### Google Search Console
**When to Use:**
- Checking search performance
- Monitoring indexing status
- Analyzing search queries
- Reviewing Core Web Vitals

**Key Tools:**
- `getSearchAnalytics` - Query and page performance
- `inspectUrl` - URL inspection
- `getSitemaps` - Sitemap status

**Workflow:**
1. Pull search analytics for target keywords
2. Identify pages with high impressions, low CTR
3. Optimize titles and meta descriptions
4. Monitor indexing issues

### Semrush
**When to Use:**
- Keyword research
- Competitor analysis
- Backlink analysis
- Position tracking

**Key Tools:**
- `keywordResearch` - Keyword metrics
- `domainOverview` - Competitor analysis
- `backlinkAnalytics` - Link profile

**Workflow:**
1. Research keywords for topic
2. Analyze competitor rankings
3. Identify content gaps
4. Track position changes

### DataForSEO
**When to Use:**
- SERP data
- Keyword metrics
- Competitor SERP analysis

**Key Tools:**
- `serpGoogle` - SERP results
- `keywordsGoogle` - Keyword data

---

## Analytics Tools Integration

### Google Analytics
**When to Use:**
- Website traffic analysis
- Conversion tracking
- User behavior analysis
- Campaign attribution

**Key Tools:**
- `getReport` - Custom reports
- `getRealtime` - Real-time data
- `getConversionEvents` - Conversions

**Workflow:**
1. Pull traffic by channel
2. Analyze conversion paths
3. Identify top-performing content
4. Track campaign performance

---

## CRM Tools Integration

### HubSpot
**When to Use:**
- Contact management
- Deal tracking
- Email marketing
- Lead scoring

**Key Tools:**
- `contacts` - Contact management
- `deals` - Deal pipeline
- `companies` - Company records
- `email` - Email campaigns

**Workflow:**
1. Pull contact data for segmentation
2. Track deal progression
3. Analyze email performance
4. Score leads based on activity

---

## Social Media Tools Integration

### Twitter/X
**When to Use:**
- Tweet scheduling
- Engagement monitoring
- Trend tracking
- Competitor analysis

**Key Tools:**
- `tweets` - Post tweets
- `search` - Search tweets
- `analytics` - Performance data

### TikTok
**When to Use:**
- Trend discovery
- Content research
- Performance tracking

**Key Tools:**
- `trending` - Trending content
- `search` - Content search

### Crosspost
**When to Use:**
- Multi-platform posting
- Content scheduling
- Cross-platform analytics

---

## Project Management Tools Integration

### Notion
**When to Use:**
- Content calendar management
- Documentation
- Knowledge base
- Editorial planning

**Key Tools:**
- `pages` - Create/edit pages
- `databases` - Query databases
- `blocks` - Content blocks

### Asana
**When to Use:**
- Task management
- Project tracking
- Team coordination

**Key Tools:**
- `tasks` - Task management
- `projects` - Project tracking
- `teams` - Team management

---

## Communication Tools Integration

### Slack
**When to Use:**
- Team notifications
- Campaign alerts
- Performance updates
- Community management

**Key Tools:**
- `messages` - Send messages
- `channels` - Channel management

---

## Skill-Specific MCP Workflows

### SEO Audit Workflow
1. **Google Search Console**: Pull search analytics
2. **Semrush**: Analyze competitor rankings
3. **DataForSEO**: Get SERP data
4. **Google Analytics**: Check traffic patterns

### Campaign Performance Workflow
1. **Google Analytics**: Pull traffic data
2. **HubSpot**: Check conversion data
3. **Meta Ads**: Review ad performance
4. **Slack**: Send performance report

### Content Calendar Workflow
1. **Notion**: Pull editorial calendar
2. **Asana**: Check task status
3. **Google Analytics**: Identify top content
4. **Semrush**: Research keywords

### Email Campaign Workflow
1. **HubSpot**: Pull contact segments
2. **HubSpot**: Create email campaign
3. **Google Analytics**: Track email conversions
4. **Slack**: Notify team of results

---

## MCP Tool Selection Guide

| Situation | Primary Tool | Why |
|-----------|--------------|-----|
| Need SEO data | Semrush | Comprehensive keyword data |
| Need website analytics | Google Analytics | Traffic and behavior data |
| Need CRM data | HubSpot | Contact and deal management |
| Need social posting | Crosspost | Multi-platform efficiency |
| Need project tracking | Notion | Flexible, visual |
| Need team notifications | Slack | Real-time communication |

---

## Integration Best Practices

1. **Cache responses** - Don't call same API repeatedly
2. **Batch requests** - Combine multiple queries
3. **Handle errors gracefully** - Fall back to alternatives
4. **Respect rate limits** - Don't exceed API limits
5. **Log API calls** - Track usage and costs
6. **Validate data** - Check for completeness
7. **Document assumptions** - Note data limitations
