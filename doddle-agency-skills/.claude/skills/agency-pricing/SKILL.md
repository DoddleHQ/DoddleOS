---
name: agency-pricing
id: doddle.agency.pricing
version: 1.0.0
blueprint: ./blueprint.yaml
description: When an agency sets or revises its pricing: retainer vs project vs value-based models, rate cards, hourly rates, margin analysis, or pricing a specific engagement. Also use when the user mentions "pricing," "rate card," "how much should we charge," "retainer vs project," "hourly rate," "margins," "undercharging," or "pricing model." Produces a recommended pricing model, machine-readable rate card, and margin scenarios.
---

# Agency Pricing

The money model for selling services. Pick the pricing model that fits the work (retainer / project / value-based / hybrid), build a defensible rate card from cost + margin math, and stress-test it against lean/base/stretch scenarios before it meets a client.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- An agency has no rate card, or rates were set by vibes years ago
- Choosing between retainer, fixed project, time-and-materials, or value-based pricing
- Undercharging suspicion (busy team, thin margins)
- Pricing a specific engagement ("they asked for a quote")
- Raising rates without churning existing clients

## Initial Assessment

Before modeling, evaluate:

1. **Cost reality**
   - Team cost per month (salaries + tooling + overhead)? Billable capacity?
   - Current effective hourly rate after hidden unbilled work?
2. **Work shape**
   - Ongoing, predictable workload (retainer fit) or bounded deliverables (project fit)?
   - Is the outcome measurable and valuable enough for value-based pricing?
3. **Market position**
   - Where does the agency compete — premium expertise, mid-market, or price floor?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Services offered, delivery costs, market position, target clients |
| financials | string | no | Cost base, current margins, historical rate data; propose assumption if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| pricing_model | markdown | Recommended model with rationale, guardrails, transitions |
| rate_card | json | Roles, rates, tiers, minimums |
| margin_analysis | markdown | Margin math, break-even, scenarios, pricing risks |

---

## Core Framework

### Step 1: Model Selection
| Model | Fits when | Watch out for |
|-------|-----------|---------------|
| Retainer | Ongoing, predictable workload; client buys capacity | Scope definition; utilization creep |
| Fixed project | Bounded deliverables, clear acceptance | Estimation risk; change requests |
| Time & materials | Exploratory / uncertain scope | Client's cost anxiety; needs trust |
| Value-based | Outcome is measurable and valuable | Requires outcome visibility; harder to set |
| Hybrid | Common: retainer base + project sprint | Rule for when each applies must be written |

The recommendation includes a transition plan (how existing engagements migrate) — pricing changes can't teleport.

### Step 2: Build the Rate Card from Cost Math
- `cost per person-day = (monthly fully-loaded cost) / (billable days)` — billable ≠ 20; use realistic 12-16
- `target rate = cost per day × (1 + target margin)` with margin stated
- Rate card: role → day rate → effective hourly → project minimum → retainer minimums
- Every number carries its assumption (costs assumed vs confirmed)

### Step 3: Guardrails
Floor prices (never below cost × minimum margin), price-increase rules for existing clients, discount approval thresholds, and non-billable leakage budget (meetings, admin) so the rate isn't eroded silently.

### Step 4: Scenario Stress Test
Lean (-30%) / base / stretch (+30%): revenue, margin, capacity required per scenario. Identify which lever (utilization, rate, mix) moves the model most.

### Step 5: Handoff
The rate card feeds `agency-proposals` (pricing options) and `agency-marketing` (positioning must match the price tier — premium claims need premium rates).

---

## Rate Card Guidance

```json
{
  "currency": "USD",
  "model": "hybrid (retainer base + fixed projects)",
  "roles": [
    {"role": "strategist", "day_rate": 1600, "hourly": 200, "min_project": 8000},
    {"role": "specialist", "day_rate": 1100, "hourly": 140, "min_project": 5000}
  ],
  "floors": {"min_margin_pct": 35, "discount_approval": "founder > 10%"},
  "assumptions": ["fully-loaded costs assumed from team size × avg salary (unconfirmed)"]
}
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Hourly rates from habit | Prices track effort, not value | Value-anchored tiers with rate floors |
| Pricing below cost | Busy agency, no profit | Cost math first; margins stated |
| One model for all work | Retainers on bounded projects bleed | Model-per-work-shape decision table |
| Raising rates silently | Existing clients churn from price shock | Migration plan + grandfathering rules |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Fictional cost data | Margin math on invented numbers | Ask for real costs or flag assumptions |
| Ignoring non-billable time | Effective rate 30% below stated | Leakage budget in the model |
| Rate card without floors | One discount unravels the model | Written floors + approval thresholds |

---

## Related Skills

- `doddle.agency.proposals` — consumes the rate card to present pricing tiers
- `doddle.agency.marketing` — positioning must align with the price tier
- `doddle.agency.reporting` — utilization and margin visibility per client
- `doddle.marketing.budget-allocator` — for the *client's* budget side of the same deals
