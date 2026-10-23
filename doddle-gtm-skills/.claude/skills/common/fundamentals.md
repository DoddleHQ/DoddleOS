# GTM Fundamentals (shared vocabulary)

Shared concepts every skill assumes. Keep definitions here; do not re-define them per skill.

## The GTM motion

Go-to-market is the sequence that turns a market into revenue: **segment → position → message →
reach → qualify → sell → onboard → expand**. Every skill maps to one step of that sequence and
should name which step it is working on.

## Core terms

- **ICP** — ideal customer profile, at the account level (firmographics, technographics,
  triggers). Distinct from a **persona**, which is a role inside the account.
- **Segment** — a group of accounts sharing a trait you act on (size, vertical, geography,
  motion). **Tiering** ranks accounts within a segment by value.
- **Funnel** — the ordered stages a prospect passes through. **Conversion** is between adjacent
  stages; **drop-off** is the absolute loss. All from counts the user provides.
- **Pipeline** — the set of open deals. **Coverage** is pipeline value ÷ quota. **Velocity** is
  how fast deals move. **Cycle time** is created → closed.
- **Unit economics** — CAC (cost to acquire one customer), ARPA (revenue per account per
  month), gross margin, churn. **LTV** = ARPA × gross margin ÷ churn. **Payback** = months to
  recover CAC. **Magic number** = net new ARR ÷ prior-period S&M spend.
- **Pricing vs packaging** — price is the number; packaging is what you bundle and how you meter
  it (the **value metric**).
- **Expansion / NRR** — revenue growth from existing customers via upsell, cross-sell and
  retention, net of churn.
- **Motion** — how you reach customers: **sales-led**, **marketing-led**, **product-led (PLG)**,
  or **partner-led**. SMB defaults toward PLG and lower-touch, but confirm per case.
- **ABM** — account-based marketing: choosing a small set of accounts and coordinating
  marketing and sales against each.

## Segments (this pack defaults to SMB-first)

Skills assume **SMB** as the default segment unless told otherwise: lower ACV, faster cycles,
self-serve or low-touch, volume over depth. State the segment and its assumptions in every
output, because the same funnel or unit-economics inputs mean different things for SMB vs
mid-market vs enterprise.

## What "evidence" means here

Two kinds, always distinguished:

- **Measured (`live`)** — pulled from the user's own CRM/analytics via a tool, or read from an
  export file. A fact about their business right now.
- **Assumption (`advisory`)** — a number the user states (ACV, churn, weights, market size).
  The toolkit computes with it reproducibly, but it is still a belief, and is labelled as one.

Compounds like LTV or TAM may rest entirely on assumptions. That is allowed — hiding it is not.

## Shared file map

- Response order and hard rules: `common/response-contract.md`
- Source precedence and stamps: `common/data-reliability.md`
- Formulas and thresholds: `common/scoring-methodology.md`
- Named templates: `common/frameworks-registry.md`
- Tool IDs: `common/mcp-integration-guide.md`
