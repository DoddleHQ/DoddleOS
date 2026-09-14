<p align="center">
  <img src="assets/logo.svg" alt="DoddleOS Logo" width="80" height="80">
</p>

<h1 align="center">DoddleOS</h1>

<p align="center">
  <a href="https://github.com/doddleOS/doddleOS-marketing/stargazers"><img src="https://img.shields.io/github/stars/doddleOS/doddleOS-marketing?style=flat" alt="Stars"></a>
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/Claude_Code%20|%20Cursor%20|%20Copilot-Compatible-blueviolet" alt="AI Assistants">
  <br>
  <img src="https://img.shields.io/badge/Agents-20-green" alt="Agents">
  <img src="https://img.shields.io/badge/Commands-164-orange" alt="Commands">
  <img src="https://img.shields.io/badge/Skills-52-blue" alt="Skills">
</p>

<p align="center">
  <strong>Agentic task execution operating system for Claude Code, Cursor, GitHub Copilot, and any AI assistant supporting agents & skills.</strong>
</p>

<p align="center">
  Validated graph blueprints (SKILL.md + blueprint.yaml) executed as agent/tool DAGs: 138 skills across 17 independent peer packs — marketing, GTM, travel, devops, ecom, local, SaaS, health, legal, finance, and more. Each pack installs and runs standalone; cross-pack binding via blueprint call nodes.
</p>

<p align="center">
  <a href="https://doddlehq.com/marketing.html">Website</a> •
  <a href="https://docs.doddlehq.com">Docs</a> •
  <a href="#installation">Install</a> •
  <a href="#training">Training</a>
</p>

---

## What's Inside

Works with **Claude Code**, **Cursor**, **GitHub Copilot**, and any AI assistant supporting agents & skills. Install as plugin or copy components manually.

```
doddleOS-marketing/
|-- .claude-plugin/      # Plugin and marketplace manifests
|   |-- plugin.json            # Plugin metadata and component paths
|   |-- marketplace.json       # Marketplace catalog for /plugin marketplace add
|
|-- .claude/
|   |-- agents/          # 18 specialized marketing agents
|   |   |-- attraction-specialist.md    # Lead gen, SEO, landing pages
|   |   |-- lead-qualifier.md           # Lead scoring, segmentation
|   |   |-- email-wizard.md             # Email sequences, automation
|   |   |-- sales-enabler.md            # Sales collateral, battlecards
|   |   |-- continuity-specialist.md    # Retention, re-engagement
|   |   |-- upsell-maximizer.md         # Revenue expansion
|   |   |-- copywriter.md               # High-converting copy
|   |   |-- conversion-optimizer.md     # CRO specialist
|   |   |-- seo-specialist.md           # SEO optimization
|   |   |-- brand-voice-guardian.md     # Brand consistency
|   |   |-- ...and more
|   |
|   |-- commands/        # 93 slash commands by category
|   |   |-- campaign/    # /campaign:plan, /campaign:brief, /campaign:analyze
|   |   |-- content/     # /content:blog, /content:landing, /content:email
|   |   |-- seo/         # /seo:keywords, /seo:audit, /seo:programmatic
|   |   |-- cro/         # /cro:page, /cro:form, /cro:popup, /cro:signup
|   |   |-- growth/      # /growth:launch, /growth:referral, /growth:free-tool
|   |   |-- ...and more
|   |
|   |-- skills/          # moved → doddle-marketing-skills/ (independent peer pack, 52 skills)
|   |
|   |-- workflows/       # Core marketing workflows
|       |-- primary-workflow.md         # Campaign lifecycle
|       |-- sales-workflow.md           # Lead to customer
|       |-- crm-workflow.md             # Contact lifecycle
|
|-- training/            # 19 interactive training lessons
|-- docs/                # Documentation and guides
|-- marketplace.json     # Self-hosted marketplace config
```

---

## Installation

### Option 1: Install as Plugin (Recommended)

Install directly via Claude Code's plugin system:

```bash
# Add this repo as a marketplace
/plugin marketplace add doddleOS/doddleOS-marketing

# Install the plugin
/plugin install doddleOS-marketing@doddleOS-marketing
```

Or add directly to your `~/.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "doddleOS-marketing": {
      "source": {
        "source": "github",
        "repo": "doddleOS/doddleOS-marketing"
      }
    }
  },
  "enabledPlugins": {
    "doddleOS-marketing@doddleOS-marketing": true
  }
}
```

This gives you instant access to all commands, agents, skills, and workflows.

---

### Option 2: Clone and Use

Clone the repository and work within it:

```bash
git clone https://github.com/doddleOS/doddleOS-marketing.git
cd doddleOS-marketing
claude
```

---

### Option 3: Manual Installation

Copy individual components to your Claude config:

```bash
# Clone the repo
git clone https://github.com/doddleOS/doddleOS-marketing.git

# Copy agents
cp doddleOS-marketing/.claude/agents/*.md ~/.claude/agents/

# Copy commands
cp -r doddleOS-marketing/.claude/commands/* ~/.claude/commands/

# Copy skills
cp -r doddleOS-marketing/.claude/skills/* ~/.claude/skills/

# Copy workflows
cp -r doddleOS-marketing/.claude/workflows/* ~/.claude/workflows/
```

---

## Quick Start

### Campaign Launch

```bash
# Research and plan
/research:market "SaaS productivity tools"
/competitor:deep "competitor.com"
/campaign:plan "Q1 Product Launch"

# Generate content
/content:landing "new feature" "target audience"
/content:email "product launch" "trial users"
/content:blog "feature announcement" "primary keyword"

# Optimize
/cro:page "landing page for conversion"
/seo:optimize "content.md" "target keyword"
```

### Content Creation

```bash
/content:good "Blog post about AI marketing"
/content:editing "polish this draft"
/seo:keywords "ai marketing automation"
```

### Conversion Optimization

```bash
/cro:page "homepage conversion audit"
/cro:form "lead capture optimization"
/cro:signup "registration flow"
/test:ab-setup "headline variations"
```

### Growth & Strategy

```bash
/marketing:ideas "SaaS product"
/marketing:psychology "pricing objections"
/growth:launch "Product Hunt strategy"
/pricing:strategy "tier structure"
```

---

## Available Skills

| Skill | Description | Use When |
|-------|-------------|----------|
| **Core Marketing** |
| `marketing-psychology` | 70+ mental models for marketing | Persuasion, pricing, objections |
| `marketing-ideas` | 140 proven SaaS strategies | Need marketing ideas |
| `marketing-fundamentals` | Funnel, journey, positioning | Foundation concepts |
| **Conversion Optimization** |
| `page-cro` | Landing page, homepage, pricing | Page not converting |
| `form-cro` | Lead capture, contact forms | Form optimization |
| `popup-cro` | Modals, overlays, exit intent | Popup creation |
| `signup-flow-cro` | Registration, trial signup | Signup friction |
| `onboarding-cro` | Post-signup activation | User activation |
| `paywall-upgrade-cro` | In-app paywalls, upgrade screens | Freemium conversion |
| `ab-test-setup` | Experiment design | A/B testing |
| **Content & Copy** |
| `copywriting` | Marketing page copy | Write new copy |
| `copy-editing` | Edit and polish | Improve existing copy |
| `email-sequence` | Drip campaigns, nurture | Email automation |
| **SEO & Growth** |
| `seo-mastery` | Keyword, technical, on-page | SEO optimization |
| `programmatic-seo` | Template pages at scale | Scaled SEO |
| `schema-markup` | Structured data, rich snippets | Schema implementation |
| `competitor-alternatives` | vs pages, alternatives | Comparison content |
| `launch-strategy` | Product launches, announcements | Go-to-market |
| `pricing-strategy` | Pricing, packaging, tiers | Pricing decisions |
| `referral-program` | Referral, affiliate | Viral growth |
| `free-tool-strategy` | Engineering-as-marketing | Free tool planning |

### Independent OS Packs (DoddleOS v2 blueprints, peers — no cross-pack install deps)

| Pack | Skills | IDs | Commands |
|------|--------|-----|----------|
| Doddle Marketing OS (`doddle-marketing-skills/`) | CRO, copy, SEO, growth, content, analytics (52) | `doddle.marketing.*` v1.5.1 | `/content:*`, `/seo:*`, `/cro:*`, `/growth:*`, `/marketing:*` |
| Doddle GTM OS (`doddle-gtm-skills/`) | strategy, ABM, win-loss, playbook, channel, advocacy (6) | `doddle.gtm.*` v1.0.0 | `/gtm:strategy`, `/gtm:abm`, `/gtm:win-loss`, `/gtm:playbook`, `/gtm:channel`, `/gtm:advocacy` |
| Doddle Travel OS (`doddle-travel-skills/`) | search, itinerary, booking, support, reviews (5) | `doddle.travel.*` v1.0.0 | `/travel:search`, `/travel:itinerary`, `/travel:booking`, `/travel:support`, `/travel:reviews` |
| Doddle DevOps OS (`doddle-devops-skills/`) | processes, storage, LVM/RAID, boot/systemd, cron/logging, monitoring, packages, networking/ssh, kernel, backup (10) | `doddle.devops.*` v1.0.0 | skills-first pack (derived from *Linux System Administration*, Paul Cobbaut, GFDL 1.3) |
| Doddle Ecommerce OS (`doddle-ecommerce-skills/`) | PLP, PDP, checkout, search, revenue | `doddle.ecommerce.*` v1.5.1 | `/ecom:plp`, `/ecom:pdp`, `/ecom:checkout`, `/ecom:search`, `/ecom:revenue` |
| Doddle Local OS (`doddle-local-skills/`) | GBP, reviews, location pages, booking, local ads | `doddle.local.*` v1.0.0 | `/local:gbp`, `/local:reviews`, `/local:pages`, `/local:booking`, `/local:ads` |
| Doddle SaaS OS (`doddle-saas-skills/`) | homepage, pricing, trial, retention, expansion | `doddle.saas.*` v1.0.0 | `/saas:homepage`, `/saas:pricing`, `/saas:trial`, `/saas:retention`, `/saas:expansion` |
| Doddle Health OS (`doddle-healthcare-skills/`) | booking, recall, intake, reputation, ads | `doddle.health.*` v1.0.0 | `/health:booking`, `/health:recall`, `/health:intake`, `/health:reputation`, `/health:ads` |
| Doddle Real Estate OS (`doddle-real-estate-skills/`) | listings, valuation, open-house, nurture, referrals | `doddle.realty.*` v1.0.0 | `/realty:listings`, `/realty:valuation`, `/realty:openhouse`, `/realty:nurture`, `/realty:referrals` |
| Doddle B2B OS (`doddle-b2b-skills/`) | outbound, proposals, cases, retainers, partnerships | `doddle.b2b.*` v1.0.0 | `/b2b:outbound`, `/b2b:proposals`, `/b2b:cases`, `/b2b:retainers`, `/b2b:partnerships` |
| Doddle Restaurant OS (`doddle-restaurant-skills/`) | reservations, ordering, loyalty, events, reputation | `doddle.restaurant.*` v1.0.0 | `/restaurant:reservations`, `/restaurant:ordering`, `/restaurant:loyalty`, `/restaurant:events`, `/restaurant:reputation` |
| Doddle HR OS (`doddle-hr-skills/`) | recruiting, screening, onboarding, culture, employer-brand | `doddle.hr.*` v1.0.0 | `/hr:recruiting`, `/hr:screening`, `/hr:onboarding`, `/hr:culture`, `/hr:brand` |
| Doddle Sales OS (`doddle-sales-skills/`) | prospecting, discovery, negotiation, forecasting, enablement | `doddle.sales.*` v1.0.0 | `/sales:prospecting`, `/sales:discovery`, `/sales:negotiation`, `/sales:forecasting`, `/sales:enablement` |
| Doddle Creator OS (`doddle-creator-skills/`) | ideation, scripting, packaging, publishing, monetization | `doddle.creator.*` v1.0.0 | `/creator:ideation`, `/creator:scripting`, `/creator:packaging`, `/creator:publishing`, `/creator:monetization` |
| Doddle Legal OS (`doddle-legal-skills/`) | intake, guides, consults, reputation, referrals | `doddle.legal.*` v1.0.0 | `/legal:intake`, `/legal:guides`, `/legal:consults`, `/legal:reputation`, `/legal:referrals` |
| Doddle Finance OS (`doddle-finance-skills/`) | leads, onboarding, reviews, cross-sell, referrals | `doddle.finance.*` v1.0.0 | `/finance:leads`, `/finance:onboarding`, `/finance:reviews`, `/finance:crosssell`, `/finance:referrals` |
| Doddle Education OS (`doddle-education-skills/`) | enrollment, open-house, content, nurture, alumni | `doddle.edu.*` v1.0.0 | `/edu:enrollment`, `/edu:openhouse`, `/edu:content`, `/edu:nurture`, `/edu:alumni` |

Validate all: `python3 doddle-core/scripts/validate.py` (0 errors target).

---

## Marketing Agents

### Core Agents
| Agent | Focus |
|-------|-------|
| `attraction-specialist` | Lead gen, SEO, landing pages |
| `lead-qualifier` | Lead scoring, segmentation |
| `email-wizard` | Email sequences, automation |
| `sales-enabler` | Sales collateral, battlecards |
| `continuity-specialist` | Retention, re-engagement |
| `upsell-maximizer` | Revenue expansion, cross-sell |

### Supporting Agents
| Agent | Focus |
|-------|-------|
| `researcher` | Market research, competitive intel |
| `brainstormer` | Campaign ideation, creative concepts |
| `planner` | Campaign planning, calendars |
| `copywriter` | High-converting copy |
| `project-manager` | Campaign coordination |
| `docs-manager` | Marketing documentation |

### Reviewer Agents
| Agent | Perspective |
|-------|-------------|
| `brand-voice-guardian` | Brand consistency |
| `conversion-optimizer` | CRO best practices |
| `seo-specialist` | SEO optimization |
| `solopreneur` | Freelancer/small business |
| `startup-founder` | Early-stage startup |

---

## Command Categories

| Category | Commands | Examples |
|----------|----------|----------|
| Campaign | 4 | `/campaign:plan`, `/campaign:brief` |
| Content | 10 | `/content:blog`, `/content:landing`, `/content:editing` |
| SEO | 6 | `/seo:keywords`, `/seo:audit`, `/seo:programmatic` |
| CRO | 6 | `/cro:page`, `/cro:form`, `/cro:signup` |
| Ecom | 5 | `/ecom:plp`, `/ecom:pdp`, `/ecom:checkout` |
| Growth | 3 | `/growth:launch`, `/growth:referral` |
| Email | 4 | `/sequence:welcome`, `/sequence:nurture` |
| Analytics | 5 | `/analytics:roi`, `/analytics:funnel` |
| Sales | 9 | `/sales:pitch`, `/sales:battlecard`, `/sales:prospecting`, `/sales:discovery`, `/sales:forecasting` |
| Research | 3 | `/research:market`, `/research:persona` |
| Marketing | 2 | `/marketing:psychology`, `/marketing:ideas` |
| Testing | 1 | `/test:ab-setup` |
| Local | 5 | `/local:gbp`, `/local:reviews`, `/local:booking` |
| SaaS | 5 | `/saas:trial`, `/saas:pricing`, `/saas:retention` |
| Health | 5 | `/health:booking`, `/health:recall`, `/health:reputation` |
| Realty | 5 | `/realty:listings`, `/realty:valuation`, `/realty:openhouse` |
| B2B | 5 | `/b2b:outbound`, `/b2b:proposals`, `/b2b:retainers` |
| Restaurant | 5 | `/restaurant:reservations`, `/restaurant:ordering`, `/restaurant:loyalty` |
| HR | 5 | `/hr:recruiting`, `/hr:onboarding`, `/hr:culture` |
| Creator | 5 | `/creator:ideation`, `/creator:scripting`, `/creator:packaging` |
| Legal | 5 | `/legal:intake`, `/legal:guides`, `/legal:consults` |
| Finance | 5 | `/finance:leads`, `/finance:onboarding`, `/finance:reviews` |
| Education | 5 | `/edu:enrollment`, `/edu:openhouse`, `/edu:nurture` |
| ...more | 45+ | See full command reference |

---

## Training

**22 interactive lessons** to master AI-powered marketing. Learn by doing real marketing work inside your AI assistant.

| | |
|---|---|
| **Method** | Interactive lessons taught by Claude |
| **Project** | Markit agency working for client Doddle Marketing OS |
| **Duration** | 5-6 hours total |
| **Prerequisite** | Claude Code, Cursor, or compatible AI assistant |

```bash
# Start training now
/training:start-0-0
```

---

### Practice Project: Markit Agency

You're a Marketing Strategist at **Markit**, a B2B SaaS marketing agency.

**Your Client:** Doddle Marketing OS - AI marketing automation toolkit

| | |
|---|---|
| **Product** | Enterprise-grade AI marketing automation |
| **Target** | SaaS founders, marketers, and growth teams |
| **Pricing** | Free & Open Source (MIT license) |
| **Competitors** | Jasper, Copy.ai, HubSpot |

**Key Personas:**
- **Solo Sam** (25-35) - Solopreneur/indie hacker, bootstrapped SaaS
- **Marketer Maya** (30-40) - Marketing manager, mid-size SaaS company
- **Founder Felix** (28-40) - Technical founder, early-stage startup

---

### Module 0: Getting Started (30 min)

Learn the basics and complete your first marketing task.

| Command | Lesson | Duration |
|---------|--------|----------|
| `/training:start-0-0` | Course Introduction | 10 min |
| `/training:start-0-1` | Installation & Setup | 15 min |
| `/training:start-0-2` | Your First Marketing Task | 15 min |

**What You'll Learn:**
- AI assistant interface and basic commands
- File creation and management
- Interacting with AI for marketing tasks

---

### Module 1: Core Concepts (90 min)

Master fundamental workflows through the Markit agency project.

| Command | Lesson | Duration |
|---------|--------|----------|
| `/training:start-1-1` | Welcome to Markit | 20 min |
| `/training:start-1-2` | Working with Marketing Files | 25 min |
| `/training:start-1-3` | First Marketing Tasks | 30 min |
| `/training:start-1-4` | Using Agents for Marketing | 35 min |
| `/training:start-1-5` | Reviewer Agents Deep Dive | 30 min |
| `/training:start-1-6` | Project Memory (CLAUDE.md) | 20 min |
| `/training:start-1-7` | Navigation & Search | 20 min |

**What You'll Learn:**
- Campaign brief creation
- Brand voice and persona development
- Agent coordination and delegation
- File organization best practices
- Using project memory effectively

**What You'll Build:**
- Complete campaign brief
- Brand guidelines document
- Customer personas
- Custom reviewer agents

---

### Module 2: Advanced Applications (120 min)

Apply skills to real marketing scenarios at scale.

| Command | Lesson | Duration |
|---------|--------|----------|
| `/training:start-2-1` | Write a Campaign Brief | 45 min |
| `/training:start-2-2` | Develop Content Strategy | 40 min |
| `/training:start-2-3` | Generate Marketing Copy | 35 min |
| `/training:start-2-4` | Analyze Campaign Data | 35 min |
| `/training:start-2-5` | Competitive Analysis | 30 min |
| `/training:start-2-6` | SEO Optimization | 40 min |

**What You'll Learn:**
- Strategic campaign planning
- Multi-channel content creation
- Data analysis and insights
- Competitive intelligence gathering
- SEO best practices

**What You'll Build:**
- Complete content library (blog, email, social, ads)
- Competitive analysis report
- SEO optimization plan
- Campaign analytics dashboard

---

### Module 3: CRO & Conversion (60 min)

Master conversion rate optimization with specialized CRO skills.

| Command | Lesson | Duration |
|---------|--------|----------|
| `/training:start-3-1` | CRO Fundamentals | 20 min |
| `/training:start-3-2` | Form & Signup Optimization | 20 min |
| `/training:start-3-3` | Popup & Onboarding CRO | 20 min |

**What You'll Learn:**
- 7 CRO skills for the full conversion funnel
- Form optimization (5-field rule)
- Signup flow best practices
- Popup design and triggers
- Onboarding and activation
- Paywall and upgrade screens
- A/B test design

**What You'll Build:**
- Landing page CRO audit
- Optimized form design
- Onboarding flow
- Upgrade screen
- A/B test hypotheses

**Full CRO Funnel Coverage:**
```
Visitor → Page CRO → Form CRO → Signup CRO
     ↓
  Popup CRO (capture abandoners)
     ↓
New User → Onboarding CRO → Activation
     ↓
Free User → Paywall CRO → Paid Customer
```

---

### Bonus Content

| Command | Description |
|---------|-------------|
| `/training:bonus-patterns` | Pattern library for headlines, emails, social, ads, CRO |
| `/training:bonus-secret` | The 10x Marketer Framework |
| `/training:help` | Show all available training commands |

---

### The Compounding Effect

Each campaign makes the next one faster:

| Campaign | Time | Improvement |
|----------|------|-------------|
| First (Module 2) | 40 hrs | Build from scratch |
| 5th campaign | 15 hrs | 62% faster |
| 10th campaign | 10 hrs | 75% faster |

**What You'll Accumulate:**
- Campaign brief templates
- Brand voice guidelines
- Content templates (blog, email, social, ads)
- Persona frameworks
- Competitive analysis templates
- SEO optimization checklists
- Custom reviewer agents
- Workflow automation patterns

---

## Learning Paths

### Path 1: Quick Start (30 min)
For experienced marketers - jump straight to production:
```bash
/campaign:plan "Your campaign"
/content:good "Your content"
/cro:page "Your landing page"
```

### Path 2: Full Training (5-6 hrs)
For beginners - complete interactive training:
```bash
/training:start-0-0  # Start here
```

### Path 3: Skill-Specific (15-30 min each)
Learn specific skills as needed:

| Goal | Commands |
|------|----------|
| **Improve conversions** | `/cro:page`, `/cro:form`, `/marketing:psychology` |
| **Write better copy** | `/content:good`, `/content:editing` |
| **Launch a product** | `/growth:launch`, `/campaign:plan` |
| **Optimize pricing** | `/pricing:strategy` |
| **Scale SEO** | `/seo:programmatic`, `/seo:schema` |
| **Design referrals** | `/growth:referral` |
| **A/B testing** | `/test:ab-setup` |

### Path 4: CRO Mastery (60 min)
Complete conversion optimization training:
```bash
/training:start-3-1  # Start with fundamentals
/training:start-3-2  # Form & signup
/training:start-3-3  # Popup & onboarding
```

---

## MCP Integrations

Real data from connected services (see `data-reliability-rules.md`):

| Server | Use For |
|--------|---------|
| `sensortower` | App analytics, ASO |
| `google-search-console` | Search performance |
| `google-analytics` | Web analytics |
| `semrush` | Keywords, backlinks |
| `dataforseo` | SERP data |
| `meta-ads` | Facebook/Instagram ads |
| `hubspot` | CRM, automation |

---

## Contributing

Contributions welcome! If you have:
- Improved agents or skills
- New marketing commands
- Better workflows
- Bug fixes

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ideas for Contributions
- Industry-specific skills (B2B, e-commerce, SaaS)
- Platform-specific agents (TikTok, YouTube, Reddit)
- Regional marketing (APAC, EMEA, LATAM)
- Analytics integrations

---

## Resources

### Doddle Marketing OS
- [Doddle Marketing OS Homepage](https://doddlehq.com)
- [Marketing Kit Page](https://doddlehq.com/marketing.html)
- [Documentation](https://docs.doddlehq.com)
- [Doddle Marketing OS CLI](https://github.com/doddleOS/doddleOS-cli)

### AI Assistants
- [Claude Code Docs](https://docs.claude.com/en/docs/claude-code/overview)
- [Cursor Docs](https://docs.cursor.com)
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- [Model Context Protocol](https://modelcontextprotocol.io)

### Community
- [GitHub Issues](https://github.com/doddleOS/doddleOS-marketing/issues)
- [GitHub Discussions](https://github.com/doddleOS/doddleOS-marketing/discussions)

---

## Star History

<a href="https://star-history.com/#doddleOS/doddleOS-marketing&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=doddleOS/doddleOS-marketing&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=doddleOS/doddleOS-marketing&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=doddleOS/doddleOS-marketing&type=Date" />
 </picture>
</a>

---

## License

MIT - Use freely, modify as needed, contribute back if you can.

---

**Star this repo if it helps. Start building AI-powered marketing campaigns today.**
