---
name: creative-direction
id: doddle.marketing.creative-direction
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants a campaign concept, big idea, or art direction before producing channel assets. Also use when the user mentions "creative brief," "big idea," "concept," "art direction," "moodboard," "campaign theme," "visual direction," or "why does everything look off-brand." Produces the concept system and visual rules every downstream asset must follow.
---

# Creative Direction

The creative spine of a campaign: one concept system that makes every channel asset recognizable, consistent, and narratively connected. Runs before asset production (Stage 5 of `/campaign:run`); its outputs are the first input to copywriting, image, video, and social work.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- Starting a campaign that spans multiple channels and needs one concept
- Assets look fragmented ("each channel tells a different story")
- Launching a new offer that needs its own theme and vocabulary
- Briefing designers or creators who need visual + verbal rules, not just copy

## Initial Assessment

Before directing, evaluate:

1. **Brief state**
   - Goal, audience, offer locked? Creative direction on an unlocked brief = waste.
2. **Existing brand material**
   - Voice guidelines, prior campaigns' winners, visual identity to respect?
3. **Channel scope**
   - Which channels? Asset formats needed per channel?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Campaign brief with goal, audience, offer |
| channels | string | no | Channels in scope; infer from brief if missing |
| voice | string | no | Brand voice guidelines or docs path |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| creative_brief | markdown | Concept system: big idea, message hierarchy, tone, do/don't rules |
| art_direction | markdown | Visual direction: palette, layout patterns, asset specs per channel |
| creative_review | markdown | Guardian pass: deviations from brand voice and fixes |

---

## Core Framework

### Step 1: Interrogate the Brief
Find the tension the campaign resolves: what does the audience want, what stands in the way, what does this offer change? The best concept is one sentence long and built on that tension — not a tagline contest.

### Step 2: Generate Concept Options
Produce 2–3 distinct concepts (not 10 variations of one). For each: one-sentence idea + why it connects to the tension + risk. Recommend one; document the runners-up with reversal triggers.

### Step 3: Write the Message Hierarchy
Per channel, the concept degrades gracefully: what is the 1-second, 5-second, and 30-second message? List banned phrases and required phrases per the brand voice docs.

### Step 4: Set the Art Direction
Palette + typography direction, layout patterns, photography/illustration style, and per-channel asset specs (dimensions, safe zones, motion notes). Specify what a template must keep so systems stay recognizable.

### Step 5: Guardian Pass
Run the brand-voice-guardian review on direction vs. guidelines. Log every deviation with a fix or a documented reason; unresolved items land in the review notes.

---

## Creative Brief Template

```markdown
# Creative Brief: [Campaign]
## Concept
**Big idea:** [one sentence]
**Tension it resolves:** [audience want × blocker × change this offer makes]
## Message Hierarchy
| Horizon | Message |
|---------|---------|
| 1 second | [visual/verbal hook] |
| 5 seconds | [core claim] |
| 30 seconds | [full narrative + proof] |
## Do / Don't
- **Do:** [required phrases, proof format]
- **Don't:** [banned claims, tired tropes]
## Art Direction
- [palette, type, imagery style, per-channel specs]
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Concepts before the brief unlocked | Direction on guesses, redo after intake | Lock primary KPI + offer first |
| Ten near-identical options | False choice | 2–3 genuinely distinct ideas |
| Concept as tagline | Cannot degrade into per-channel assets | Message hierarchy per horizon |
| Ignoring existing brand equity | Campaign fights the brand system | Inherit voice docs; flag tensions explicitly |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No asset specs per channel | Production restarts discovery per asset | Specs + safe zones in art_direction |
| Guardian pass skipped | Off-voice direction propagates downstream | Mandatory guard node before asset work |
| Silent concept reversal trigger | Team can't tell when the idea failed | Document triggers when recommending |

---

## Related Skills

- `doddle.marketing.marketing-intake` — supplies the unlocked brief it consumes
- `doddle.marketing.copywriting`, `doddle.marketing.image`, `doddle.marketing.video-marketing`, `doddle.marketing.social-media` — produce assets against this direction
- `doddle.marketing.ugc-creator` — creator briefs inherit this concept
