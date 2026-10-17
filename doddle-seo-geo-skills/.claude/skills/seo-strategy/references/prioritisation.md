# Prioritisation reference

Depth for `seo-strategy`. The formula and the dependency rules are `advisory` judgement; state
them so the reader can challenge them. No number here is measured.

## The score

```
priority = impact × confidence ÷ effort
```

- **Impact** — the size of the prize against the stated business goal. Source it from evidence
  (a sibling skill's finding, `hubspot.contacts` segment value, or a user figure). A 1–5 ordinal
  is fine; say it is ordinal, not a measured value.
- **Confidence** — how strong the underlying evidence is:

  | Evidence | Confidence |
  |----------|------------|
  | Deterministic `dseo` finding on the exact pages | high |
  | Live tool data (Search Console, GA4, CRM) | medium–high |
  | Heuristic signal or a close analogue page | medium |
  | Expert judgement with no supporting data | low |

- **Effort** — advisory estimate of build/research time. Use t-shirt sizes (S/M/L) or days;
  never present it as a measured cost.

A large impact with low confidence should not outrank a moderate impact with high confidence,
unless the cheap test to raise confidence is itself the first step.

## Dependency ordering

Score orders the *candidates*; dependencies order the *execution*. Apply, in order:

1. **Blockers first.** Indexability, rendering, crawler access, canonical conflicts. Work behind
   a blocker recovers nothing until the blocker clears.
2. **Foundations before surfaces.** Architecture, site structure, and internal linking before
   leaf-page optimisation.
3. **Compounding before one-off.** Work that lifts a whole template beats work that lifts one
   URL when both score similarly.
4. **Evidence-raising before big commitments.** If confidence is the bottleneck, schedule the
   cheap measurement first.

## Building the roadmap

- **Now** — the single bet plus any blocker that gates it.
- **Next** — items whose dependencies are satisfied by the Now phase.
- **Later** — everything else, with the dependency that unlocks it named.

Each entry carries: item, impact, confidence, effort, evidence source, owner, dependency,
and the assumption it rests on.

## Ending on one bet

The headline is the single recommended next move, phrased as an action, with:

- the evidence behind it and its class (`deterministic`, `live`, `advisory`),
- the assumption it depends on,
- what would change the decision.

Everything else is the roadmap behind that bet, not a second headline.
