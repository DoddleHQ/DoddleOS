# Design: `doddle-devops-skills` pack

Date: 2026-09-14
Status: approved (design review passed)

## Context

The `dev-agents-v2` project (`~/Documents/Agents/dev-agents-v2`) contains a DevOps
power agent under `agent_src/power_agents/devops/`:

- **10 skills** in Anthropic SKILL.md convention (lean runbooks, 49–65 lines each,
  `name` + `description` frontmatter only):
  methodical-diagnosis, nginx-systemd-playbook, processes-and-signals,
  filesystems-and-mounting, lvm-and-raid, io-and-memory-forensics,
  systemd-and-journal, network-diagnostics, syslog-and-logrotate,
  backup-and-transfer
- **5 SSH operator tools** (`ssh_registry.py`): ssh_connect, ssh_shell,
  ssh_write_file, ssh_approve_action, ssh_disconnect — with a safety model:
  catastrophic blocklist, static mutation classifier, approval gating
  (15-min window), backup-before-write, TOFU known_hosts, strict credentials
- **One operator persona** (`devops_agent.py`): propose-before-change,
  verify-every-repair, evidence-first diagnosis

DoddleOS-Skills (this repo) is a monorepo of 16 peer skill packs where every
skill = `SKILL.md` (full v2 template) + `blueprint.yaml` (DoddleOS v2 graph
blueprint), validated by `doddle-core/scripts/validate.py` (0 errors,
0 warnings gate).

## Decisions (user-approved)

| Decision | Choice |
|----------|--------|
| Scope | DevOps pack only (seo_audit / website_content fleets excluded) |
| SSH binding | New `ssh` integration **stub** in `doddle-core/registry/integrations/` |
| Pack extras | Skills-only, like the travel pack — no root slash commands |
| Content depth | Full v2 template rewrite; source procedural content preserved verbatim |

## Design

### 1. Pack structure

Follows the travel-pack precedent (newest pack, commit 54d989d):

```
doddle-devops-skills/
├── .claude/
│   ├── agents/
│   │   └── devops-operator.md
│   └── skills/
│       ├── methodical-diagnosis/      # SKILL.md + blueprint.yaml
│       ├── nginx-systemd-playbook/
│       ├── processes-and-signals/
│       ├── filesystems-and-mounting/
│       ├── lvm-and-raid/
│       ├── io-and-memory-forensics/
│       ├── systemd-and-journal/
│       ├── network-diagnostics/
│       ├── syslog-and-logrotate/
│       └── backup-and-transfer/
├── .claude-plugin/plugin.json
├── marketplace.json
├── package.json
├── README.md
└── LICENSE
```

- Skill IDs: `doddle.devops.<name>`, version 1.0.0, OS name "Doddle DevOps OS"
- Flat skill dir names (all packs use flat layout). The source's category
  grouping (troubleshooting/, disk-ops/, …) is dropped from paths and survives
  as Related Skills links and README grouping.
- `plugin.json`: requirements `doddleOS >=2.0`, skills + agents components.
- `package.json`: `test` script runs `python3 ../../doddle-core/scripts/validate.py`
  (travel-pack pattern).

### 2. Skill transformation

Each SKILL.md is authored in the full v2 template (~150–200 lines) per
`doddle-core/spec/skill-template.md`:

- Frontmatter description = source trigger text (already "Use when…" quality),
  extended with cross-references per template convention.
- Source procedural content (commands, flags, warnings, ordering rules) is
  preserved **verbatim** and placed into Core Framework steps, Detailed
  Guidance, and Checklists. Example: methodical-diagnosis's
  survey→isolate→hypothesize→verify loop becomes the Core Framework.
- Authored-around sections: When to Use, Initial Assessment, Inputs Schema,
  Outputs Schema, Common Mistakes (strategy/execution/analysis), Metrics to
  Track, Decision Tree, Quick Assessment Checklist, Expected Output Format,
  Common Failure Modes, MCP Tool Integration, Agent Collaboration,
  Related Skills, Questions to Ask.
- Every SKILL.md includes the standard Language & Quality Standards block and
  references `data-reliability-rules.md` (never fabricate command output;
  state NOT AVAILABLE when the SSH tool surface is absent).

Two blueprint shapes encode the safety model:

- **Diagnostic skills** (methodical-diagnosis, io-and-memory-forensics,
  network-diagnostics, systemd-and-journal, processes-and-signals,
  syslog-and-logrotate):

  ```
  survey    (agent: devops-operator, needs [inputs])   → produces [survey_data]
  enrich    (tool: doddle.tool.v1.ssh.shell, optional) → produces [command_output]
  diagnose  (agent: devops-operator)                    → produces [diagnosis]
  report    (agent: devops-operator)                    → produces [report]
  ```

- **Repair-capable skills** (nginx-systemd-playbook, filesystems-and-mounting,
  lvm-and-raid, backup-and-transfer) add the approval + apply + verify tail:

  ```
  … diagnose → approve_fix (gate: approvers [owner], timeout_s 3600)
             → apply (tool: ssh.shell | ssh.writeFile)
             → verify (agent) → report
  ```

  This maps the source agent's propose→approve→execute loop onto the spec's
  `gate` node (`harness-phase2.md` §2.1): approval becomes graph structure,
  not prose. Gate `on_approve: proceed`, `on_reject: revise`.

- `call` nodes used sparingly where idiomatic (e.g. nginx-systemd-playbook
  calls `doddle.devops.methodical-diagnosis` for its survey loop). Refs must
  be known ids (validator-enforced).
- `on_fail: {retry: 1, fallback: manual_review}` everywhere (repo standard).

### 3. SSH integration stub

`doddle-core/registry/integrations/ssh/`:

- `config.json`: name `ssh`, type `custom`, status stub, 5 planned tools,
  env `SSH_KEY_PATH`, `DEVOPS_KNOWN_HOSTS_FILE`, source = dev-agents-v2
  reference implementation.
- `index.md`: planned tool table + the safety contract (blocklist categories,
  mutation classifier semantics, approval window, TOFU, backup-before-write,
  output caps/tail-biased truncation) + Used By list.
- `_registry.md`: new row (Infrastructure | Custom | ⚠️ Stub), new
  Infrastructure category section, env-var block, "Current stubs" list.

Tool IDs (camelCase per `tool-namespace.md`):

| Tool ID | Contract |
|---------|----------|
| `doddle.tool.v1.ssh.connect` | Strict-credential session open; TOFU known_hosts; mismatch = hard fail |
| `doddle.tool.v1.ssh.shell` | Read-only commands run freely; classified mutations require recorded approval; blocklist refused outright |
| `doddle.tool.v1.ssh.writeFile` | Backup-before-write (`<path>.bak.<ts>`), 64 KB cap, approval-gated |
| `doddle.tool.v1.ssh.approveAction` | Consent record quoted from the user; 15-min window |
| `doddle.tool.v1.ssh.disconnect` | Session close |

Blueprints bind these `required: false, fallback: manual_review` (stub
convention). No Python code ships in this repo — the stub documents the
contract; the reference implementation stays in dev-agents-v2.

### 4. `devops-operator` agent

`doddle-devops-skills/.claude/agents/devops-operator.md`, frontmatter matching
the repo agent format (name, description with example blocks, `model: sonnet` —
operator-grade reasoning on production servers, vs `haiku` for the lightweight
lookup agents other packs bundle).
Body carries the ported persona and safety rules:

- Evidence-first: survey before hypothesizing; exit codes are evidence
- Propose-before-change: every state-changing command needs an explicit user
  approval first; one variable at a time
- Never run blocklisted commands (recursive root deletes, mkfs, raw-device
  writes, power control, fork bombs, interactive root shells); propose safer
  alternatives
- Verify every repair: re-run reproducer, tail logs, check neighbour services
- Honest reporting: never fabricate output; missing tool surface → ⚠️ NOT
  AVAILABLE
- Language directive + data-reliability compliance (repo standards)

### 5. Registration & docs updates

- `doddle-core/registry/packs.json`: append pack entry — name
  `doddle-devops-skills`, source `./doddle-devops-skills/.claude/skills`,
  ids `doddle.devops.*`, version 1.0.0, skills 10, os "Doddle DevOps OS".
- Root `README.md`: pack table row; counts 16→17 packs, 128→138 skills.
- `doddle-core/README.md`: "16 independent OS packs" → 17 (and peer-pack
  phrasing if stale).
- Pre-existing manifest drift (`.claude-plugin/plugin.json` v2.0.0 legacy
  naming, root `marketplace.json` counts) is **out of scope** — separate
  cleanup task; this change does not worsen it.

### 6. Verification

1. `python3 doddle-core/scripts/validate.py` → **0 errors, 0 warnings**
   (exercises: frontmatter fields, id equality, node types, gate
   approvers/timeout, call refs, output coverage).
2. Content-preservation audit: every command, flag explanation, and warning
   from the 10 source SKILL.mds appears in the ported skill (checked by
   reviewing each source file against its port).
3. Structural review: each SKILL.md contains all template-required sections;
   each blueprint matches one of the two sanctioned shapes.
4. No runtime code ships → no unit tests; validator is the test.

## Failure modes & mitigations

| Risk | Mitigation |
|------|------------|
| Content drift during rewrite (losing source commands) | Verbatim-preserve rule + preservation audit (verification #2) |
| Validator gate-node false positives | Gate nodes always carry `approvers` + `timeout_s`; run validator per-skill while authoring |
| Stub mistaken for live MCP | `index.md` leads with stub status banner; `required: false` + `manual_review` fallback everywhere |
| Scope creep into manifest cleanup | Explicitly out of scope; noted for follow-up |

## Out of scope (follow-ups)

- seo_audit + website_content fleet ports (42 skills)
- Root `/devops:*` slash commands
- Manifest/branding drift cleanup across `.claude-plugin/`, root marketplace.json
- Live SSH MCP server implementation (stub → live promotion per
  `_registry.md` path)
