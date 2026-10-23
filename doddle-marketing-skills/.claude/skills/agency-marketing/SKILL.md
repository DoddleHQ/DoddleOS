---
name: agency-marketing
id: doddle.marketing.agency-marketing
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants to market their agency's own website — a marketing agency, software dev agency, AI consulting agency, or any consulting business. Also use when the user mentions "agency website," "services page," "case studies," "agency positioning," "agency homepage," "why clients choose us," "agency marketing," or "our website doesn't convert." Produces positioning, site copy, and a page-by-page site map with booking CTAs.
---

# Agency Marketing

The plumber's leaky pipe: agencies that sell marketing, dev, or consulting to clients are terrible at marketing themselves. This skill handles the distinct genre of agency websites — you're selling trust and expertise, not a product; the buyer is sophisticated, proof matters more than features, and the conversion is a booked call, not a purchase.

Covers marketing agencies, software dev agencies, AI consulting agencies, and any consulting business.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- An agency's own website needs positioning, copy, or a rebuild
- Services pages read as a deliverables list instead of outcome-led offers
- Case studies are missing, thin, or don't convert
- The site gets traffic but the "book a call" button doesn't get clicked
- The agency is pivoting (new service line, new ICP, repositioning)
- The user says "our website doesn't convert" or "we need to look more professional"

## Initial Assessment

Before positioning, evaluate:

1. **Agency state**
   - Type (marketing / dev / AI / general consulting)? Team size? Years operating?
   - Services offered, average deal size, typical engagement length?
2. **Proof inventory**
   - Case studies, testimonials, client logos, measurable results, certifications?
   - What proof exists but isn't on the site?
3. **Current site**
   - What does the existing site say (audit if provided)? Where does it lose the visitor?
4. **Buyer**
   - Who signs the contract (role, company size, budget authority)? What triggered them to search for an agency?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Agency type, services, target clients, differentiators |
| existing_site | string | no | Current site content or URL for audit |
| portfolio | string | no | Case studies, results, testimonials available for proof |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| positioning | markdown | ICP, differentiation, messaging pillars, proof strategy |
| site_copy | markdown | Homepage, services page, case-study template, about angle, CTAs |
| site_map | json | Page-by-page section structure with content slots and booking CTAs |

---

## Core Framework

### Step 1: Define the ICP (Ideal Client Profile)
Who signs the contract? The mistake: "anyone who needs [service]". The fix: one primary ICP — role (CMO, CTO, founder), company stage/size, budget authority, and the trigger event that makes them search ("just raised Series A", "inherited a broken codebase", "marketing isn't converting"). One sentence: "[Role] at [company type] who just [trigger event]."

### Step 2: Position Against the Field
The agency market is crowded with interchangeable claims ("full-service", "results-driven", "partner, not vendor"). Positioning requires a specific, defensible claim:

| Weak | Strong |
|------|--------|
| "We do digital marketing" | "We turn Series A SaaS trial signups into paying customers" |
| "Full-stack development" | "We rescue legacy Rails apps without a rewrite" |
| "AI consulting" | "We build AI workflows that cut your ops team's ticket time in half" |

The claim must be provable — every positioning claim maps to a case study or proof artifact. No proof = soften the claim, don't amplify it.

### Step 3: Structure the Services Page (Outcome-Led)
Deliverables lists don't sell; outcomes do. Per service, lead with the outcome, then the mechanism, then the proof:

```markdown
## [Service Name — outcome, not deliverable]
**The outcome:** [what changes for the client in concrete terms]
**How we do it:** [2-3 sentence mechanism — the differentiator is here]
**Proof:** [case-study ref, number, or testimonial]
**Who it's for:** [one-line ICP match]
```

No more than 3–4 services on the page. If the agency does 12 things, the page says what it does best and links to the rest.

### Step 4: Build the Proof Architecture
Trust is the product. The proof stack, in order of persuasiveness:

1. **Measurable results in case studies** ("cut onboarding time 40% in 6 weeks" — never "improved efficiency")
2. **Client logos** (recognizable names beat adjectives)
3. **Testimonials with names, roles, companies** (anonymous quotes lose weight)
4. **Process transparency** ("here's exactly how we work" — reduces perceived risk)
5. **Team credibility** (founder bios with relevant track record, not headshots alone)

For case studies, use the template: **Problem → Approach → Result → Quote**. The Result section must lead with a number. If no measurable result exists, frame the story around the problem-solution-impact arc and note the missing metric as a gap.

### Step 5: Design for the Booking CTA
The conversion event is a booked call (or a qualified inquiry). Every page ends with it, and the ask must be low-friction:

- CTA copy: "Book a 30-min call" / "See if we're a fit" — not "Contact us" or "Get a quote"
- The booking CTA appears: hero, after the first proof block, after each service, page footer
- No form longer than: name, email, one qualifying question ("what's your biggest challenge right now?")
- Social proof adjacent to every CTA ("Join 40+ [ICP] teams we've worked with")

---

## Positioning Template

```markdown
# Positioning: [Agency Name]
## ICP
- **Role:** [signer role]
- **Company:** [stage/size/vertical]
- **Trigger:** [what makes them search now]
## Differentiation
- **Claim:** [specific, provable one-liner]
- **Mechanism:** [how we deliver it differently]
- **Proof mapping:** [claim → proof artifact]
## Messaging Pillars
1. [Pillar 1: outcome] — [proof ref]
2. [Pillar 2: mechanism] — [proof ref]
3. [Pillar 3: trust] — [proof ref]
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| "We do everything" positioning | Buyers hire specialists; generalists get compared on price | One ICP, one claim, 3-4 services |
| Services listed as deliverables | "We offer SEO, PPC, social" — no outcomes, no differentiation | Outcome-led service blocks with proof |
| Proof-free claims | Sophisticated buyers smell marketing language | Every claim maps to a case study or number |
| Anonymous testimonials | "A Fortune 500 company" is not trust | Named, attributed, with company and role |
| CTA is a contact form | Friction kills booking rate; forms feel like commitment | "Book a call" with one qualifying question |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Homepage does everything | Hero + services + team + blog = no path to conversion | Homepage: claim → proof → CTA; services live on their own page |
| Case studies without numbers | "Great results!" persuades no one | Lead with the metric; if none, note the gap |
| No ICP on the page | "Who is this for?" — every visitor wonders | Name the ICP explicitly ("Built for Series A SaaS CTOs") |
| Copy-pasting client work tone | Agency site should sound like the agency, not a client | Match tone to agency personality; it's the one place to be yourself |

---

## MCP Tool Integration

No MCP tools required — this is strategy and copy work. If the user provides a live site for audit (`existing_site`), review the content they paste; if they want traffic data, route to `analytics-attribution` or `gsc-reporting` skills.

---

## Related Skills

- `doddle.marketing.copywriting` — page-level copy mechanics this builds on
- `doddle.marketing.conversion-copywriting` — persuasion frameworks for the services page
- `doddle.marketing.brand-building` — brand voice and identity if the agency needs a full rebrand
- `doddle.marketing.page-cro` — deeper CRO audit once the site is live
- `doddle.marketing.page-build-spec` — dev handoff after copy is approved
- `doddle.marketing.content-strategy` — ongoing content (blog, thought leadership) post-launch
