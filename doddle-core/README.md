# Doddle Core (kernel)

Domain-neutral execution substrate for DoddleOS graph blueprints. No marketing concepts live here.

## Layers

```
doddle-core/            Layer 0 — kernel (this pack)
├── spec/               Blueprint schema, skill template, tool namespace
├── registry/           Integrations + pack index (all domains as peers)
└── scripts/            Discovery-based validator (no hardcoded packs)

./.claude/skills/       Marketing domain pack (peer, v1.5.1, doddle.marketing.*)
                        Physically historic, logically equal to doddle-*/ packs.
doddle-*/               Domain packs (ecom, local, saas, health, realty, b2b,
                        restaurant, hr, sales, creator, legal, finance, edu)
```

## Rules

1. Kernel never imports domain packs. Packs bind kernel tool IDs.
2. New pack = new `doddle-*/` dir. No validator/spec edit needed (discovery).
3. Shared mechanics graduate to kernel `spec/` only if ≥2 domains use them.
4. Marketing is one domain in `registry/packs.json`, not the owner of infra.

## Validate

```bash
python3 doddle-core/scripts/validate.py   # 0 errors target
```
