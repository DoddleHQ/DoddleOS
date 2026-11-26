# Credits and Value Metrics

## Value metric choice

| Model | Fits when | Watch out |
|-------|-----------|-----------|
| Seat | Value scales with people using the product | Seat sharing, login sharing |
| Metered | Value scales with consumption (API calls, storage, sends) | Bill shock, unpredictable budgets |
| Hybrid | Platform base plus overage on one metered axis | Complexity — cap at two axes |
| Flat | Value is hard to attribute to a unit | Cheap for high-usage customers |

The metric must scale with customer value, be predictable, and be hard to game. If the customer
cannot predict their bill, it fails all three.

## Credits vs included units

They are different mechanisms and the order matters:

1. **Credits burn first** — one credit per unit of usage, consumed from the granted balance.
2. **Included units** are consumed next, at no charge.
3. **The remainder bills** at `unit_price`.

Credits let you grant usage without revenue (launch credits, support gestures, onboarding
allowances). Included units are the plan's built-in allowance.

## Fields the meter emits

| Field | Meaning |
|-------|---------|
| `quantity` | Raw usage for the account and period |
| `credits_available` / `credits_used` | Granted credits and how many were consumed |
| `included_units` | Allowance before billing starts |
| `billable_units` | Units actually charged at `unit_price` |
| `base_amount` / `overage_amount` / `total_amount` | The invoice preview |

## Guardrails

- **Bill shock**: any account whose total jumps sharply is a churn risk, not a revenue win.
  Report it by name.
- **Unrated usage**: usage that matched no tier is excluded from the total. It is a data gap —
  resolve the tier mapping, never absorb it silently.
- **Preview only**: `drev meter --usage <file> --plan <plan.json>` produces an invoice
  **preview**. It creates no billing object and changes no subscription.
- **Version the plan**: price, units, and credits are configuration; change them through a
  versioned plan file so a later audit can explain a past bill.

## Change management

A price or unit change needs: the plan version, the affected accounts, the expected delta, and
the notice period. Those are commercial decisions — this pack only shows the math.
