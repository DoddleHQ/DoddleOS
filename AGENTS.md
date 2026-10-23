# AGENTS.md — Using DoddleOS from any LLM workspace

This file is the entry point for AI agents regardless of vendor (Claude Code, Gemini CLI, Codex, Cursor, Grok, Copilot, etc.). Follow it when working in this repository.

## What this repo is

DoddleOS is a library of **186 skills across 19 peer packs** — marketing, agency, sales, b2b, GTM, travel, ecommerce, local, SaaS, health, legal, finance, devops, and more. Each skill is a pair of files: `SKILL.md` (the instructions) + `blueprint.yaml` (an ordered execution graph). No runtime ships here — **you are the runtime**: read the skill, walk the graph, do the work.

## Core consumption rule

Before doing a task in any covered domain:

1. **Find the skill.** Pack table: `README.md` → "Independent OS Packs". Registry: `doddle-core/registry/packs.json`. Per-pack catalog: `<pack>/README.md`. Directories follow `doddle-<domain>-skills/.claude/skills/<skill>/SKILL.md`.
2. **Read the SKILL.md fully** and follow its Core Framework, Inputs/Outputs, and Common Mistakes.
3. **Read `blueprint.yaml` as ordered steps.** Node types: `agent` (delegate/act as that role), `tool` (call an MCP tool), `call` (recurse into another skill's blueprint), `gate` (STOP and get human approval — never skip a gate). Dependencies are in `needs`; every declared output is produced by some node.
4. **If a skill's prerequisites are missing**, produce a partial result with assumptions flagged, or stop and ask — per that skill's `on_fail` / Missing Data Rule.

## Portable rules (apply everywhere, in every workspace)

- **NEVER fabricate data.** Use MCP tools for real metrics. If unavailable: show `⚠️ NOT AVAILABLE — <server> not configured` with setup pointer. Every number is either sourced or labeled `assumed`. (Full rules: `.claude/workflows/data-reliability-rules.md`.)
- **Respond in the user's language.** Match it exactly (Vietnamese → Vietnamese, Spanish → Spanish).
- **Token efficiency:** sacrifice grammar for concision; list unresolved questions at the end of any report.
- **Approval gates are hard stops.** Skills with `type: gate` nodes (or a "Stage 6 / Approval" step in commands) require explicit human approval before distribution/publication of outputs.
- **Data + regions + assumptions:** inputs marked required are required; optional inputs you can't infer get flagged assumptions, never invented values.

## File map: portable vs. workspace-specific

| Path | Portable? | Notes |
|------|-----------|-------|
| `doddle-*/.claude/skills/*/SKILL.md` | ✅ fully | Plain markdown instructions — read and follow in any workspace |
| `doddle-*/.claude/skills/*/blueprint.yaml` | ✅ fully | Plain YAML graph — walk it yourself |
| `.claude/workflows/*.md` | ✅ fully | Mandatory rules (data-reliability first) |
| `docs/`, pack `README.md`, `skills-matrix.md` | ✅ fully | Reference material |
| `.claude/commands/*/*.md` | ⚠️ body portable, wrapper Claude-specific | Copy the body into your workspace's prompt-template/command feature |
| `.claude/agents/*.md` | ⚠️ body portable, wrapper Claude-specific | Usable as subagent system prompts; re-wrap per tool |
| `.claude/skills/` (root) | — | Redirect stub only; real skills live in `doddle-*/` |
| MCP config (`.claude/.mcp.json`) | ⚠️ format per tool | Tool ids are stable and portable: `doddle.tool.v1.<server>.<tool>` |
| `GEMINI.md` | ⚠️ role-specific | Defines an MCP-proxy JSON-only sub-role for Gemini CLI — do **not** treat it as primary agent instructions |

## Multi-step tasks

- Check `.claude/workflows/` for an existing workflow covering the task (marketing, sales, CRM) before improvising.
- For cross-skill dependencies (which skills combine with which), see `doddle-marketing-skills/.claude/skills/skills-matrix.md` and each pack's README.
- Cross-pack `call` nodes assume the target pack may be absent: if a called skill doesn't exist, degrade per `on_fail` (default `manual_review`) and note it.

## What does NOT exist yet

- No blueprint runner/harness (spec is draft at `doddle-core/spec/harness*.md`). Graphs execute only by you following them.
- **Stub MCP integrations** (`google-business-profile`, `stripe`, `sensortower`, `zalo`): config reserved, server/API keys pending (`doddle-core/registry/integrations/_registry.md`). Skills bind their tool ids with `required: false` / `fallback: manual_review` and show `⚠️ NOT AVAILABLE` until promoted — outputs are templates requiring setup, not live data.
