---
name: page-build-spec
id: doddle.marketing.page-build-spec
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants a landing page turned into a developer-ready build spec, or approved copy handed to a site developer. Also use when the user mentions "build spec," "impl," "handoff to dev," "section map," "wireframe," "component spec," "responsive rules," "what should the dev build," or "events wiring" for a page. Produces a section-by-section build spec and machine-readable section map — the bridge between approved marketing copy and web development.
---

# Page Build Spec

The handoff from marketing to web development. Takes approved page copy (and optional art direction + tracking), and emits a developer-ready spec: every section as a component with content slots, responsive rules, event bindings, and load-order notes. Produces the spec only — building the page is outside DoddleOS marketing scope.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- Approved copy needs to become a page (dev handoff or site-build agent)
- A rebuild/refresh needs a specification, not a redesign from scratch
- Page events (analytics, form submits) must be documented for the measurement plan
- Copy was approved via a gate and now needs the production step

## Initial Assessment

Before structuring the spec, evaluate:

1. **Source material state**
   - Is the copy approved via a gate? Flag any unapproved sections explicitly.
   - Is art direction available, or does the spec defer visual decisions?
2. **Target platform**
   - Site builder (CMS/stack constraints), template system, or dev from scratch?
3. **Event surface**
   - Which page events must fire (view, CTA clicks, form submittal) per the measurement plan or tracking document?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| draft | string | yes | Approved page copy or existing page content |
| art_direction | string | no | Creative-direction output: visual rules |
| tracking | string | no | UTMs + events the page must fire |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| build_spec | markdown | Section-by-section build spec for a dev or site agent |
| section_map | json | Machine-readable section map: component types, content slots, event bindings |
| spec_review | markdown | CRO pass: conversion elements, load order, mobile rules |

---

## Core Framework

### Step 1: Decompose into Sections
Split the approved copy into sections in DOM order, following the page's chosen persuasion structure (PAS/AIDA/BAB/4 Ps/FAB per `conversion-copywriting` — default hero, value props, social proof, offer, FAQ, final CTA if none was declared). Each section gets: purpose, component type (one of the platform's primitives), and behavioral notes.

### Step 2: Slot the Content
For each section, map copy fragments to typed content slots: heading (string), body (rich text), image (alt text mandatory), CTA (label + href + event name). The event names come from the measurement plan — an unnamed CTA event is a build blocker.

### Step 3: Write Responsive + Load Rules
Per section: mobile stack order, above-the-fold budget (hero + primary CTA only), image weights/formats, skeleton states. Anything visual not covered by the given art direction notes is explicitly a "defer to dev" row, not a guess.

### Step 4: CRO Pass
Run the conversion-optimizer review: form friction, CTA count and placement, proof placement, and mobile CTA visibility. Log each finding and fix spec values.

### Step 5: Handoff Notes
Deliver the spec with a build order (what can be built in parallel), acceptance criteria per section, and the review's open items.

---

## Section Map Guidance

```json
{
  "page": "pricing-[yy][mm]",
  "template": "landing_v2",
  "sections": [
    {
      "id": "hero",
      "component": "hero_split",
      "slots": {
        "heading": "Pricing copy that converts",
        "cta": {"label": "Start trial", "href": "/signup", "event": "cta_clicked_hero"}
      },
      "responsive": {"mobile": "stack", "image": {"max_kb": 120}},
      "events": ["page_viewed", "cta_clicked_hero"]
    }
  ]
}
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Specing from unapproved copy | Creative revision mid-build resets the project | Gate approval before spec work |
| Copy-paste spec (no component types) | Dev re-decides everything | Component types + slot boundaries |
| CTA without an event name | Page ships measuring nothing | Event bindings from measurement-plan |
| Inventing visual specs | Spec claims design decisions it doesn't own | Defer-to-dev rows + list them at review |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Alt text omitted | SEO + a11y regression | Mandatory alt text per image slot |
| No mobile stack order | Layout decisions deferred to... nobody | Explicit mobile rules |
| Everything above the fold | Hero + 4 sections = load death | Above-the-fold budget, load-order note |

---

## Related Skills

- `doddle.marketing.copywriting` — supplies the approved copy (approve_copy gate)
- `doddle.marketing.creative-direction` — supplies art direction consumed by the spec
- `doddle.marketing.measurement-plan` — supplies event names for bindings
- `/campaign:run` Stage 5+6 — this skill sits right after content approval
