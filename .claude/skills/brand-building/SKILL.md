---
name: brand-building
id: doddle.marketing.brand-building
version: 1.5.1
blueprint: ./blueprint.yaml
description: Brand strategy, identity, positioning, and voice development. Use when developing brand guidelines, creating positioning statements, defining brand voice, or building brand architecture.
---

# Brand Building

Brand strategy, identity, and positioning for differentiated market presence.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply brand expertise when:
- Developing or refreshing brand strategy
- Creating brand guidelines and standards
- Defining brand voice and tone
- Building positioning and messaging frameworks
- Designing brand architecture for multi-product companies
- Ensuring brand consistency across channels

## Core Concepts

### Brand Foundation Elements

| Element | Definition | Example |
|---------|------------|---------|
| Brand Purpose | Why you exist beyond profit | "To inspire and nurture the human spirit" (Starbucks) |
| Brand Vision | Where you're going | "A computer on every desk" (Microsoft 1980s) |
| Brand Mission | How you'll get there | "Organize the world's information" (Google) |
| Brand Values | What you stand for | Innovation, Integrity, Customer-first |
| Brand Personality | Human traits | Confident, Playful, Trustworthy |
| Brand Voice | How you communicate | Conversational, Expert, Warm |
| Brand Promise | What customers can expect | "15 minutes could save you 15%" (GEICO) |

### Positioning Framework

**Positioning Statement Template**:
> For [target audience] who [need/opportunity], [product name] is a [category] that [key benefit]. Unlike [competitors], we [unique differentiator] because [reason to believe].

**Elements of Strong Positioning**:
1. **Target Audience**: Specific, not "everyone"
2. **Frame of Reference**: Category you compete in
3. **Point of Differentiation**: Why you're different AND better
4. **Reason to Believe**: Proof points and credentials

### Brand Architecture Models

**Branded House**
- One master brand across all products
- Sub-brands under umbrella
- Example: Google (Maps, Drive, Cloud, etc.)
- Best for: B2B, trust-dependent, related offerings

**House of Brands**
- Independent brands, parent company behind scenes
- Each brand has distinct positioning
- Example: P&G (Tide, Pampers, Gillette)
- Best for: Diverse categories, different audiences

**Endorsed Brands**
- Sub-brands with parent endorsement
- Partial independence with credibility boost
- Example: Marriott (Courtyard by Marriott)
- Best for: Extending into adjacent categories

**Hybrid**
- Mix of approaches based on strategic fit
- Example: Apple (Apple, Beats by Dr. Dre)

### Brand Voice Spectrum

| Dimension | Spectrum | Choose Based On |
|-----------|----------|-----------------|
| Formal ←→ Casual | Professional vs. Friendly | Audience expectations, industry norms |
| Serious ←→ Playful | Authoritative vs. Fun | Product category, brand personality |
| Technical ←→ Simple | Expert vs. Accessible | Audience expertise, product complexity |
| Humble ←→ Confident | Understated vs. Bold | Brand maturity, market position |

### Brand Equity Components

1. **Brand Awareness**: Recognition and recall
2. **Brand Associations**: What people think/feel about you
3. **Perceived Quality**: Expectations of excellence
4. **Brand Loyalty**: Repeat behavior and advocacy

## Best Practices

### Strategy Excellence
1. **Research First**: Base positioning on customer insights, not assumptions
2. **Differentiate Meaningfully**: Different AND relevant to target audience
3. **Own a Word**: Be known for one thing (Volvo = Safety)
4. **Consistency Over Time**: Brand building takes years, not months

### Guidelines Excellence
1. **Practical Examples**: Show don't just tell
2. **Do/Don't Examples**: Clear boundaries
3. **Context-Specific**: Guidelines for different channels/situations
4. **Living Document**: Update as brand evolves

### Voice Excellence
1. **Character, Not Rules**: Define personality, not just word lists
2. **Situational Flexibility**: Same voice, different tone by context
3. **Training Examples**: Real-world application samples
4. **Vocabulary Bank**: Words we use / words we avoid

## Agent Integration

| Agent | How They Use This Skill |
|-------|------------------------|
| `copywriter` | Maintaining brand voice in all content |
| `sales-enabler` | Messaging consistency in sales materials |
| `brainstormer` | Creative concepts aligned with brand |
| `docs-manager` | Brand guideline documentation |

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Wrong | Do This Instead |
|--------------|----------------|-----------------|
| Copying competitors | Leads to sameness | Find unique positioning |
| Positioning for everyone | Appeals to no one | Focus on specific audience |
| Changing brand often | Destroys equity | Evolve, don't abandon |
| Voice without personality | Sounds generic | Define human traits |
| Guidelines without examples | Hard to apply | Show real applications |

## Related Commands

- `/brand/voice` - Create brand voice guidelines
- `/brand/book` - Generate comprehensive brand book
- `/brand/assets` - Manage brand assets

## References

- `references/brand-strategy.md` - Strategic foundation
- `references/visual-identity.md` - Design guidelines
- `references/voice-tone.md` - Verbal identity
- `references/positioning.md` - Market positioning frameworks

---

## Initial Assessment

Before providing recommendations, understand:

1. **Brand context**
   - Current perception, category, competitors?
   - Audience and what brand should own (one word)?
2. **Goal**
   - Strategy refresh, voice, guidelines, or architecture?
   - Channels where inconsistency hurts most?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Brand, audience, category, current perception |
| goal | string | no | Brand goal (positioning, voice, guidelines) |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Positioning, architecture, voice guidance |
| recommendations | json | Prioritized brand actions with impact/effort |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Brand recall | Aided/unaided awareness | Increasing | doddle.tool.v1.hubspot.contacts |
| Share of voice | Mentions vs competitors | Growing | doddle.tool.v1.ga4.getReport |
| Consistency score | Guideline adherence audit | >80% | doddle.tool.v1.notion.pages |

---

## Expected Output Format

### Brand Assessment
[Positioning, architecture, voice review]

### Recommendations
[Table: action | impact | effort | owner]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Generic positioning | Sounds like competitors | Own one word, explicit differentiator |
| Voice without examples | Inconsistent content | Add do/don't samples per channel |
| Rebrand churn | Equity loss | Evolve, do not abandon |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Branded search, referrals | Sessions, sources | no |
| doddle.tool.v1.hubspot.contacts | Audience segments | Contacts, personas | no |
| doddle.tool.v1.notion.pages | Guideline docs | Pages, assets | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Questions to Ask

1. Audience, category, and competitors?
2. What one word should the brand own?
3. Which channels need consistency first? (or share guideline docs?)
