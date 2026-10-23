---
name: agency-proposals
id: doddle.agency.proposals
version: 1.0.0
blueprint: ./blueprint.yaml
description: When an agency needs to write a winning proposal, SOW, or pitch document for a prospective client. Also use when the user mentions "proposal," "SOW," "pitch deck," "statement of work," "scope document," "how do we win this deal," or "quote for the client." Produces a client-facing proposal, a scoped SOW, and pricing options framed by value.
---

# Agency Proposals

Win the deal on paper. This skill turns client context, pricing, and portfolio proof into a proposal that sells the approach (not just the deliverables) — plus an SOW tight enough to prevent scope creep and pricing options framed so the buyer picks the right tier.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- A qualified lead has asked for a proposal or quote
- RFP/RFI response needs a structured document
- A project needs an SOW before work starts
- The proposal exists but reads like a deliverables list / price dump

## Initial Assessment

Before writing, evaluate:

1. **Client state**
   - Who evaluates and who signs? What's their stated problem and budget range?
   - Decision criteria stated or inferred (price / risk / speed / proof)?
2. **Deal state**
   - How competitive? What alternative did they already consider (incumbent, DIY, other agencies)?
3. **Proof inventory**
   - Which portfolio pieces map to this client's situation?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Client context, project scope, decision criteria, budget |
| pricing | string | no | Rate card or pricing model from agency-pricing |
| portfolio | string | no | Relevant case studies to cite |
| regions | string | no | Operating scope: local \| national \| international; infer from brief if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| proposal | markdown | Client-facing proposal: approach, timeline, pricing, terms |
| scope_of_work | markdown | SOW: deliverables, milestones, responsibilities, exclusions |
| pricing_options | json | Pricing tiers with value framing |

---

## Core Framework

### Step 1: Mirror Their Problem Back
Open with the client's problem in their words — not the agency's capabilities. A proposal that starts "We are a full-service agency" already lost. One that starts "Your trial-to-paid conversion sits at 2% while the benchmark is 5%; this proposal targets 4% in 90 days" starts ahead.

### Step 2: Sell the Approach, Not the List
The differentiator is *how*, not *what*. Structure: problem → recommended approach → why this approach fits their constraints → proof it worked before. Deliverables come after the approach is believed.

### Step 3: Scope It Tight (SOW Discipline)
Every SOW states: in-scope deliverables with acceptance criteria, explicit exclusions, client responsibilities (assets, approvals, access), change-request process, and milestone dates with owners. The exclusion list is as important as the deliverable list — it prevents the #1 agency killer: unbounded scope.

### Step 4: Present Pricing as Options, Not a Single Number
Two or three tiers framed by value (good/best): scope and outcome differences, not just price deltas. Anchor to the outcome in the client's problem. Every tier names its fit ("most clients at your stage choose tier 2").

### Step 5: Winnability Review
The reviewer checks: does the proposal answer their decision criteria? Is proof cited? Is the ask (next step) specific and small ("30-min scope call")? Are there obvious objections left unaddressed?

---

## Proposal Template

```markdown
# Proposal: [Client] × [Agency]
## The Problem
[Restate in client's words + quantified impact if known]
## Recommended Approach
[How + why this fits their constraints; name the differentiator]
## Proof
[1-2 mapped case studies: situation → approach → result number]
## Timeline & Milestones
[Milestone | date | owner | acceptance criteria]
## Investment
[Tier table: scope, outcome, price — with recommendation]
## Next Step
[Specific low-friction CTA]
```

---

## Segment Guidance (local | national | international)

Honored via the `regions` input (infer from brief if not stated):

| Dimension | Local | National | International |
|-----------|-------|----------|--------------|
| Document | 1-2 page fixed-price proposal; owner decides same week | Committee + procurement: formal SOW, MSA, security questionnaire | Multi-currency quote, entity/invoicing terms, data-residency clauses |
| Proof | Reviews, local logos, "down the street" trust | National case studies, named enterprise logos | Proof localized per buyer market |
| Cycle | Fast, one decision-maker | Multi-stakeholder, RFP-driven | Multi-region legal review, timezone-shifted follow-ups |

- **National/procurement deals:** RFP responses and security reviews are a specialist skill — use `doddle.b2b.rfp` rather than stretching this proposal template.
---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Capabilities-first opening | Reads as every other agency | Lead with their problem, quantified |
| Deliverables without approach | Buys on price, loses on value | Approach → proof → deliverables order |
| Single-price proposal | No frame for value; negotiation starts at your number | 2-3 tiers with fit guidance |
| Missing exclusions | Scope creep from day one | Explicit exclusion list in SOW |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Generic proof ("worked with big brands") | Trust requires specifics | Map case studies to their situation |
| Vague next step | Proposal goes stale in an inbox | One small, dated, specific ask |
| Assumed budget with no flag | Pricing wrong by 3x | Flag budget as assumption if unstated |
| No acceptance criteria on milestones | "Done" becomes a debate | Every milestone has an objective test |

---

## Related Skills

- `doddle.b2b.proposals` — scoped-SOW + followup mechanics for product-company deals
- `doddle.b2b.rfp` — RFP and security-questionnaire responses (national procurement path)
- `doddle.agency.pricing` — supplies the rate card and pricing model
- `doddle.agency.marketing` — supplies positioning proof and case-study library
- `doddle.agency.client-onboarding` — runs after the proposal is won
- `doddle.agency.reporting` — proves the proposal's promised outcomes post-signature
