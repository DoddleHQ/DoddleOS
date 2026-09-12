# Doddle Core (kernel)

Domain-neutral execution substrate for DoddleOS graph blueprints. No marketing concepts live here.

## Layers

```
doddle-core/            Layer 0 — kernel (this pack)
├── spec/               Blueprint schema, skill template, tool namespace
├── registry/           Integrations + pack index (15 peer packs)
└── scripts/            Discovery-based validator (no hardcoded packs)

doddle-*/               15 independent OS packs, incl. doddle-marketing-skills/
                        (52 skills, doddle.marketing.*) + doddle-gtm-skills/
                        (6 skills, doddle.gtm.*) + 13 vertical packs ×5.
                        Each pack ships own skills + bundled agents. No
                        cross-pack install deps; binding via blueprint `call`.
```

## Rules

1. Kernel never imports domain packs. Packs bind kernel tool IDs.
2. New pack = new `doddle-*/` dir. No validator/spec edit needed (discovery).
3. Shared mechanics graduate to kernel `spec/` only if ≥2 domains use them.
4. All 15 packs are peers. Agents resolve pack-local first (`<pack>/.claude/agents/`).
   Cross-pack skill binding only via blueprint `call` nodes (`type: call`,
   `ref: doddle.<domain>.<skill>`); `call` refs must be known skill ids.

## Validate

```bash
python3 doddle-core/scripts/validate.py   # 0 errors target
```
