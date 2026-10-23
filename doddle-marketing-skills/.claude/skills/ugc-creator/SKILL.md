---
name: ugc-creator
id: doddle.marketing.ugc-creator
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants a creator program, UGC pipeline, creator briefs, or shot lists for user-generated content. Also use when the user mentions "UGC," "creators," "influencer content," "reviews unboxing," "testimonial videos," "creator brief," "usage rights," or "content licensing." Produces the creator-facing brief, shot-by-shot prompts, and a usage-rights checklist.
---

# UGC Creator Program

Build the machine that turns outside creators into usable campaign assets: the creator-facing brief, shot-by-shot prompts per platform, and the rights-and-compliance checklist. UGC wins on authenticity — the reproducible part is the brief and the approval flow, not the footage.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- Planning a creator/UGC component of a campaign
- Briefing creators for testimonials, unboxings, tutorials, or reviews
- Formalizing rights, usage windows, and disclosure rules for creator content
- Repeated creator briefs become template work ("one more creator, same product")

## Initial Assessment

Before architecting the pipeline, evaluate:

1. **Program shape**
   - One-off creators or an ongoing roster? Paid, gifted, affiliate, or organic?
2. **Product + platform fit**
   - Which product hooks show well on camera? Which platforms?
3. **Compliance surface**
   - Disclosure requirements (per platform + region), claim limits for the vertical?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Product, goal, and campaign context |
| platforms | string | no | Platforms for publishing; infer from brief if missing |
| constraints | string | no | Do-say/avoid lists, claims limits, disclosure rules |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| creator_brief | markdown | Creator-facing brief: product hooks, talking points, what to shoot |
| content_prompts | json | Machine-readable shot lists and prompt variants per platform |
| usage_rights | markdown | Rights checklist: releases, disclosure, usage windows, approval flow |

---

## Core Framework

### Step 1: Pick Camera-Ready Hooks
From the brief, identify 2–3 product attributes that demo well (visible transformation, speed, before/after). Vague benefits ("great quality") are not shootable; concrete moments are.

### Step 2: Write the Creator Brief
What the creator must know: talking points, must-show moments, compliance musts (disclosure wording), and what NOT to claim. Creators get freedom on style, constraints on facts — that balance keeps content authentic and legal.

### Step 3: Build Shot Lists per Platform
Machine-readable prompts: shot duration, framing, action, overlay text, CTA moment. Per-platform variants (vertical short vs. landscape, caption/hook conventions).

### Step 4: Define the Rights Checklist
- Release: signed content/usage release captured before publishing?
- **Disclosure:** platform-required disclosure wording present natively (not buried in a caption)
- Usage window: where and how long do we use re-posts (paid ads, site, lifestyle channels)
- Claim check: does the video make a product claim? Route to `claims-review`

### Step 5: Route into the Pipeline
Creator outputs are assets: after receiving them they need a review pass and the approval gate before distribution (same rules as creative assets). Attach the claims review result.

---

## Usage Rights Checklist (guidance)

```markdown
# Creator [name] — [asset]
- [ ] Signed release: [link] / date [ ] NOT AVAILABLE
- [ ] Disclosure wording: [required text present in-video]
- [ ] Usage granted: [platforms] / window [start→end]
- [ ] Paid-amplification rights: [Y/N]
- [ ] Product claims: [list + claims_matrix ref]
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Briefing for vibes | "Be creative and authentic" produces unusable footage | Concrete must-show moments + free style |
| Rights decided after publishing | Claw-backs, ads blocked, disputes | Rights checklist before camera |
| Same brief to every platform | Format mismatch (aspect ratio, hook pattern) | Per-platform shot lists |
| Claims in creator's mouth | Regulatory exposure is identical to brand claims | claims-review route; approved claim list in brief |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No asset intake format | Files arrive unusable | Checklist at intake: file, format, duration, rights file ref |
| Burying disclosure in caption/links | Platform policy violations | In-video disclosure wording |
| Zero second-rights plan | Best UGC un-reusable | Usage windows + paid amplification rights per asset |

---

## Related Skills

- `doddle.marketing.creative-direction` — concept the creators inherit
- `doddle.marketing.claims-review` — mandatory pass for creator content claims
- `doddle.marketing.measurement-plan` — creator content needs UTM/event attribution like any channel
- `/campaign:run` Stage 6 — creator assets pass the same approval gate
