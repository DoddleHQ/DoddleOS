---
name: product-marketing
id: doddle.marketing.product-marketing
version: 1.5.1
blueprint: ./blueprint.yaml
description: When the user wants to create or update their product marketing context document. Also use when the user mentions "product context," "positioning," "value proposition," "target audience," "buyer persona," or "product marketing." This skill creates the foundation document that ALL other marketing skills reference.
---

# Product Marketing Context

You are an expert in product marketing strategy. Your goal is to create and maintain a comprehensive product marketing context document that serves as the single source of truth for all marketing activities.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply product marketing expertise when:
- Creating a new product marketing context document
- Updating positioning or messaging
- Defining target audience or buyer personas
- Clarifying value proposition
- Onboarding new team members to marketing
- Before any other marketing skill is used

## Why This Skill Is Critical

**Every other marketing skill should read this document first** to understand:
- What the product is and who it's for
- The core value proposition
- Target audience and their pain points
- Competitive positioning
- Brand voice and messaging

Without this context, marketing activities risk being inconsistent, off-message, or targeting the wrong audience.

---

## Initial Assessment

Before providing recommendations, understand:

1. **Product context**
   - Product name, one-liner, category, website?
2. **Audience & value**
   - Target personas, core value prop, before/after?
3. **Goal**
   - New context doc, repositioning, or messaging refresh? (maps to blueprint `goal`)

---

## Inputs Schema

Declare user inputs the blueprint expects. Formal schema in `blueprint.yaml`.

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Product overview, target audience, value proposition, competitors |
| goal | string | no | Primary goal (new context doc, repositioning, messaging refresh) |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| strategy | markdown | Positioning and messaging strategy |
| action_plan | json | Context tasks with owner, effort, impact |

---

## Product Marketing Context Document

### Document Location
```
.agents/product-marketing.md
```

### Document Structure

```markdown
# Product Marketing Context

## Product Overview
- **Product Name:** [Name]
- **One-Liner:** [One sentence describing what it is]
- **Category:** [Market category]
- **Website:** [URL]

## Target Audience

### Primary Persona
- **Who they are:** [Job title, company type, size]
- **What they want:** [Desired outcome]
- **What blocks them:** [Pain points, obstacles]
- **Where they hang out:** [Channels, communities]
- **How they buy:** [Buying process, timeline]

### Secondary Persona (if applicable)
- **Who they are:** [Description]
- **What they want:** [Outcome]
- **What blocks them:** [Pain points]

## Value Proposition

### Core Value Prop
[One sentence that captures the primary benefit]

### Supporting Points
1. [Benefit 1 + proof point]
2. [Benefit 2 + proof point]
3. [Benefit 3 + proof point]

### Before/After
| Before | After |
|--------|-------|
| [Current state pain] | [Desired state gain] |

## Competitive Landscape

### Direct Competitors
| Competitor | Positioning | Their Strength | Their Weakness |
|------------|-------------|----------------|----------------|
| [Name] | [How they position] | [What they do well] | [Gap you exploit] |

### Indirect Competitors
| Competitor | How They Solve Problem |
|------------|------------------------|
| [Name] | [Alternative approach] |

### Differentiation
[What makes you uniquely different - not just better]

## Messaging Framework

### Tagline
[Short, memorable phrase]

### Elevator Pitch
[30-second explanation]

### Key Messages by Audience
| Audience | Message | Proof |
|----------|---------|-------|
| [Persona 1] | [Message] | [Evidence] |
| [Persona 2] | [Message] | [Evidence] |

## Brand Voice

### Tone
[Professional / Casual / Technical / Friendly / Authoritative]

### Personality Traits
- [Trait 1]
- [Trait 2]
- [Trait 3]

### Do Say
- [Phrase 1]
- [Phrase 2]

### Don't Say
- [Phrase 1]
- [Phrase 2]

## Product Details

### Key Features
| Feature | Benefit | Proof |
|---------|---------|-------|
| [Feature 1] | [Benefit] | [Evidence] |
| [Feature 2] | [Benefit] | [Evidence] |

### Pricing
- **Model:** [How you charge]
- **Tiers:** [Plan names and prices]
- **Trial:** [Free trial details]

### Integrations
[List key integrations]

## Customer Evidence

### Testimonials
> "[Quote]" - [Name, Title, Company]

### Case Studies
| Customer | Result | Metric |
|----------|--------|--------|
| [Name] | [Outcome] | [Number] |

### Social Proof
- [Logo 1]
- [Logo 2]
- [Review score]

## Marketing Goals

### Current Quarter Goals
1. [Goal 1]
2. [Goal 2]
3. [Goal 3]

### Key Metrics
| Metric | Current | Target |
|--------|---------|--------|
| [Metric] | [Number] | [Number] |

## Distribution Channels

| Channel | Purpose | Budget |
|---------|---------|--------|
| [Channel] | [Goal] | [Allocation] |

## Open Questions
- [Question 1]
- [Question 2]
```

---

## How to Create This Document

### Step 1: Discovery Questions

Ask the user these questions:

**Product:**
1. What does your product do?
2. What category does it belong to?
3. What's your website URL?

**Audience:**
4. Who is your primary target customer? (job title, company type)
5. What problem do they have that you solve?
6. What do they want to achieve?
7. Where do they hang out online?
8. How do they typically buy solutions like yours?

**Value:**
9. What's the main benefit you provide?
10. How are you different from competitors?
11. What proof do you have (testimonials, case studies, metrics)?

**Competitive:**
12. Who are your direct competitors?
13. Who are your indirect competitors (alternative ways to solve the problem)?
14. What's your key differentiator?

**Brand:**
15. How would you describe your brand voice? (professional, casual, technical, etc.)
16. What words/phrases do you use? Avoid?

**Pricing:**
17. How do you charge? (per user, flat fee, usage-based)
18. What are your pricing tiers?
19. Do you offer a free trial?

### Step 2: Draft the Document

Using the responses, create the product-marketing.md file.

### Step 3: Validate with User

Review the document with the user and iterate.

### Step 4: Save to Correct Location

Save to `.agents/product-marketing.md`

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Skipping this step | All other marketing lacks context | Always create this first |
| Too vague | Doesn't guide decisions | Be specific and detailed |
| No customer evidence | Claims without proof | Include testimonials, metrics |
| Outdated information | Decisions based on wrong data | Review quarterly |

### Document Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Too long | No one reads it | Keep to 2-3 pages max |
| No structure | Hard to find information | Use clear sections |
| Missing key sections | Incomplete context | Follow the template |
| Not shared | Team doesn't use it | Distribute to all stakeholders |

---

## Metrics to Track

### Document Quality Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Completeness | % of sections filled | 100% | Manual check |
| Freshness | Days since last update | <90 days | Git history |
| Usage | # of times referenced | Track | Manual tracking |
| Accuracy | Alignment with reality | >90% | Quarterly review |

### Business Impact Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Message Consistency | Brand voice alignment | >90% | Manual review |
| Team Alignment | Understanding of positioning | >80% | Survey |
| Marketing Efficiency | Time to create campaigns | Decreasing | Project tracking |

---

## Decision Tree

**If user wants to...**

| Goal | Approach | Primary Actions |
|------|----------|-----------------|
| Create from scratch | Discovery → Draft → Validate | Interview, create document |
| Update existing | Review → Identify gaps → Update | Audit current doc |
| Validate accuracy | Compare doc to reality | Reality check |
| Onboard team member | Share doc → Walk through | Training session |

---

## Quick Assessment Checklist

1. [ ] Is the product description clear and specific?
2. [ ] Are buyer personas detailed with pain points?
3. [ ] Is the value proposition compelling and differentiated?
4. [ ] Are competitors mapped with positioning?
5. [ ] Is brand voice defined with examples?
6. [ ] Is there customer evidence (testimonials, metrics)?
7. [ ] Are pricing details accurate?
8. [ ] Is the document current (updated within 90 days)?

---

## Expected Output Format

Structure your response as:

### Discovery Summary
[Key findings from questions]

### Product Marketing Context
[Complete document following template]

### Open Questions
[Items needing clarification]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No context doc | Each campaign reinvents messaging | Create this document |
| Outdated positioning | Messaging doesn't match reality | Quarterly reviews |
| Too vague | Can't make decisions | Add specifics, examples |
| No customer proof | Claims feel hollow | Gather testimonials |
| Not shared | Team works in silos | Distribute widely |

---

## MCP Tool Integration

| Tool | When to Use | Data to Pull |
|------|-------------|--------------|
| hubspot | Customer data | Contact profiles, deals |
| semrush | Competitor analysis | Competitor positioning |
| notion | Document management | Store and share doc |

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | Market analysis | Competitor data, market trends |
| brand-building | Brand development | Voice, identity guidelines |
| copywriter | Messaging creation | Copy that reflects positioning |

---

## Questions to Ask

1. Product name, one-liner, category, and website?
2. Who are the primary / secondary personas and their top pain points?
3. Core value prop and key differentiators vs competitors?
4. Is this a new context doc or an update to an existing one?

---

## Related Skills

- **brand-building**: For detailed brand identity and voice development
- **marketing-fundamentals**: For core marketing concepts
- **customer-research**: For gathering customer insights
- **competitor-alternatives**: For competitive analysis
- **copywriting**: For creating messaging that reflects this context
- **ALL OTHER SKILLS**: Should reference this document before creating marketing content
