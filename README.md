# Ownership-Driven AI Customization

A scalable architecture for GitHub Copilot custom instructions, path-specific instructions, skills, and AGENTS.md across large repositories and monorepos.

It helps teams organize baseline instructions, ownership-based routing, cross-cutting overlays, Follow-Through Triggers, and optional skills without turning everything into custom agents.

Formal architecture name:

- `Ownership-Driven AI Customization Architecture`

Portuguese version:

- [README.pt-BR.md](./README.pt-BR.md)

## Who This Is For

This repository is for teams that need to scale GitHub Copilot customization across:

- large repositories
- monorepos
- path-specific instruction maps
- shared skills
- AGENTS.md compatibility
- long-lived codebases with multiple ownership boundaries

## Minimal Working Example

```text
.github/
  copilot-instructions.md
  instructions/
    ownership/
      src/
        general.instructions.md
        api/
          general.instructions.md
          admin/
            authorization.instructions.md
          orders.ts/
            contract.instructions.md
            framework.instructions.md
      docs/
        general.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      operability/
        observability.instructions.md
  skills/
    debug-behavior/
      SKILL.md
```

The canonical layout treats every owned boundary as a node folder in `ownership/`.

That means repository folders stay folders, and repository files also become folders such as `orders.ts/`.

Instruction files inside each node are named for the concern they carry, such as `general`, `contract`, or `framework`.

There is no required "main" instruction file for a node. A node folder can contain zero, one, or many instruction files.

As an optional shortcut, a leaf file node with exactly one instruction may be written directly as `orders.ts.instructions.md`.

This repository documents how to design that structure so it stays predictable, maintainable, and readable over time.

## Why This Tree Scales

- one visual grammar for folder nodes and file nodes
- no "promotion" step when a file grows from one instruction to several
- concern-based file names such as `contract.instructions.md` stay meaningful even when paths change
- mixed children are natural, so one folder can contain subtree nodes and file nodes without special rules
- maintainers can explain the tree by walking directories instead of teaching multiple naming systems

The detailed convention lives in [docs/en/ownership-tree-convention.md](./docs/en/ownership-tree-convention.md).

## Why This Exists

Many Copilot setups grow in the same unhealthy direction:

- one large repository-wide instruction file,
- duplicated rules across multiple files,
- unclear responsibility boundaries,
- custom agents created for topics that should have been instructions or skills,
- stale docs and templates that drift away from the actual routing model.

This project proposes a simpler operating model:

- keep the baseline short,
- tie most behavior to ownership boundaries,
- use overlays only for truly cross-cutting concerns,
- keep downstream review/update behavior in `Follow-Through Triggers`,
- use skills only for reusable workflows that would bloat always-on instructions.

## What You Get

- architecture documentation in English and Brazilian Portuguese
- a clear rationale for why this model exists and where it fits
- a starter kit you can copy into a repository
- templates for baseline, ownership nodes, and overlays
- community files for running this as an open source project

## Quick Start

1. Read the architecture docs in [docs/en](./docs/en/README.md).
2. Read [Why This Architecture](./docs/en/why-this-architecture.md), [Core Model](./docs/en/core-model.md), and [Ownership Tree Convention](./docs/en/ownership-tree-convention.md).
3. Copy the [starter-kit](./starter-kit/README.md) into a test repository.
4. Adapt the ownership map to your own paths.
5. Add only the overlays that truly span multiple owners.
6. Keep workflows in skills, not in always-on instructions.

## Repository Map

- [docs/en](./docs/en/README.md)
  - English reference docs
- [docs/pt-BR](./docs/pt-BR/README.md)
  - Documentação em português do Brasil
- [starter-kit](./starter-kit/README.md)
  - a copyable `.github` example
- [templates](./templates/README.md)
  - reusable file templates
- [CONTRIBUTING.md](./CONTRIBUTING.md)
  - contribution rules
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
  - community expectations
- [SECURITY.md](./SECURITY.md)
  - how to report problems responsibly

## Principles

- Favor predictability over clever routing.
- Favor ownership over abstraction.
- Favor refinement over reversal.
- Favor reusable workflows over giant instructions.
- Favor public examples over hidden conventions.

## Open Source Intent

This project is meant to be improved in public.

If you adopt the architecture in another repository, open an issue or pull request with:

- what worked,
- what felt unclear,
- what broke down at scale,
- what naming or routing decisions improved the model.

## License

This repository is released under the [MIT License](./LICENSE).
