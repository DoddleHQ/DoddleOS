# Personalization Evidence Standard

The gate that decides whether a 1:1 line survives: **every claim traces to a dated,
attributable, account-scoped fact.**

## Claim → evidence contract

```json
{
  "account": {"name": "Northwind Robotics", "domain": "northwind.io", "segment": "smb"},
  "claims": [
    {"text": "They just raised a Series B", "evidence_id": "ev_1"}
  ]
}
```

```csv
id,source,fact,observed_at,domains
ev_1,https://northwind.io/news/series-b,Announced a Series B in October,2026-10-02,northwind.io
```

`drev sdr-validate --account <account.json> --evidence <evidence.csv|json>` checks each claim and
returns `supported: true|false` with a reason.

## What counts as evidence

| Requirement | Why |
|--------------|-----|
| Dated (`observed_at`) | "They raised recently" decays |
| Attributable (`source` URL) | The reader can check it |
| Account-scoped (`domains` includes the account domain) | Competitor evidence is not their evidence |
| Has a fact | A link with no content proves nothing |

## Rejection reasons the tool returns

| Reason | Fix |
|--------|-----|
| `no evidence with this id` | The claim references evidence that was not supplied — collect it or drop the claim |
| `evidence has no fact` | Capture the observation, not just the link |
| `evidence is not for this account domain` | Wrong company — get the right source |
| `evidence has no observation date` | Undated facts are not evidence |

## Coverage

`metrics.coverage` = supported claims ÷ total claims. It is a **draft quality** measure, not a
target to optimise by weakening the claims list.

## Rules

- Unsupported claims are **deleted**, not softened into vaguer sentences.
- Never infer a fact ("they probably use Postgres") — that is a guess, and guesses are what the
  gate exists to remove.
- Never scrape gated or paywalled data to manufacture a hook.
- Keep the claim list short: three well-evidenced claims beat ten thin ones.
- Outreach copy is a **proposal**. Sending, sequencing, and deliverability are separate systems.
