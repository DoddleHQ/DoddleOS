---
name: claims-review
id: doddle.marketing.claims-review
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants campaign copy, ads, or creative checked for claims, compliance, prohibited language, or disclosure requirements. Also use when the user mentions "claims review," "legal check," "can we say," "substantiation," "regulatory," "disclaimer," "regulated industry," "compliance audit," or "is this claim OK." Produces a claim-by-claim matrix with status and fixes — runs before the approval gate.
---

# Claims Review

The compliance filter between creative production and the approval gate. Reviews every significant claim in draft content: is it substantiated, assumed, or prohibited? What disclosure is required? What wording must change? Advertising rules apply to AI-suggested copy exactly as they do to a human's.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- Any campaign asset makes a product claim (performance, results, guarantees, comparisons)
- Operating in a regulated vertical (health, finance, real estate, supplements, etc.)
- Ads are about to enter platform review (meta/Google policy risk)
- Creator/UGC content will be amplified as ads with the brand's bag
- The user asks "can we legally say this?"

## Initial Assessment

Before matrixing, identify:

1. **Content surface**
   - Which claims does the draft actually make? Comparisons, results, guarantees, numbers, "safest/best" wording.
2. **Regulatory context**
   - Vertical + region. Platform policies that apply (meta/Google ad policy restrictions).

3. **Evidence inventory**
   - What evidence exists per claim (trials, certifications, customer stats, disclosures)? What claims were already approved?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| draft | string | yes | Copy or creative to review |
| category | string | no | Regulated-vertical context; infer if missing |
| claims | string | no | Approved claim list or evidence source; propose assumption list if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| claims_matrix | json | Every significant claim: text, status (substantiated/assumed/prohibited), evidence, fix |
| review_notes | markdown | Compliance review notes: required disclosures, wording fixes, red flags |

---

## Core Framework

### Step 1: Inventory the Claims
Extract every claim from the draft verbatim — including implicit claims (numbered + "proven"), and claims a creator puts in dialogue. Include the CTA: a promise ("cancel anytime, keep access") is also a claim.

### Step 2: Classify Each Claim

| Status | Meaning | Action |
|--------|---------|--------|
| substantiated | Evidence exists and is on file | Clear to run; cite evidence ref |
| assumed | Plausible but not evidenced | Soften wording or quantify as assumption; flag to owner |
| prohibited | Banned by regulation or platform policy | Strike and propose compliant alternative |

### Step 3: Fix the Language
Concrete rewordings: "results guaranteed" → "results based on pilot data from N customers"; "safest" → compliant alternative; "no side effects" → strike. Never delete a claim silently — record it in review notes for creative owners to see what was cut and why.

### Step 4: Specify Disclosures
List required disclosures with placement rules ("in-video, first 3s", "above the fold on landing page", "in every email footer"). Assumption-flag anything the user hasn't confirmed.

### Step 5: Gate Handoff
Emit the matrix + review notes back to the creating agents. The approval gate (`approve_copy` / `approve_content`) should not be exercised before a clean matrix exists for claimed content.

---

## Claims Matrix Guidance

```json
{
  "asset": "ad-01",
  "claims": [
    {
      "text": "Lowers payroll costs 30%",
      "status": "substantiated",
      "evidence": "2025 customer study, n=41",
      "required_context": "plain-language study citation on the landing page (link)"
    },
    {
      "text": "The safest invoicing tool available",
      "status": "assumed",
      "fix": "Replace with a feature comparison"
    },
    {
      "text": "No tax filings required ever",
      "status": "prohibited",
      "fix": "Strike entirely (financial advice claim)"
    }
  ]
}
```

Ad platform risk notes on the review notes (e.g. "meta disapproves weight-loss before/after imagery in some regions — verify current policy").

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Review as afterthought | Ads/platform rejections cost days; removals break messaging | Review before the gate, not after launch |
| "Assumed" left as-is | Fake data means liability + policy risk | Soften or substantiate or strike |
| Silent deletions | Creators claim they didn't change copy | Log every change in review notes |
| Ignoring creator content | Same rules apply to UGC | Creator contains claims → same matrix |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Evidence-less numbers | "Studies show" is not a study | Require a citation or strike |
| Missing region dimension | Which jurisdiction applies matters | Record per-policy region where relevant |
| Compliance = single pass | Claims appear at every stage | Re-run on revised creative after changes |

---

## Related Skills

- `doddle.marketing.copywriting`, `doddle.marketing.email-sequence`, `doddle.marketing.social-media` — content that feeds this review
- `doddle.marketing.ugc-creator` — creator claims need the same substantiation standard
- `/campaign:run` Stage 6 — approval gate should sit after a clean claims matrix
