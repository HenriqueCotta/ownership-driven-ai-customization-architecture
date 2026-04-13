<p align="center">
  <img src="./docs/assets/branding/oda_lockup.svg?v=20260413" alt="ODA lockup" height="200">
</p>

<p align="center">
  <a href="./docs/en/README.md">
    <img alt="Docs EN" src="https://img.shields.io/badge/docs-EN-2563eb?style=for-the-badge">
  </a>
  <a href="./docs/pt-BR/README.md">
    <img alt="Docs PT-BR" src="https://img.shields.io/badge/docs-PT--BR-16a34a?style=for-the-badge">
  </a>
  <a href="./starter-kit/README.md">
    <img alt="Starter Kit" src="https://img.shields.io/badge/starter--kit-ready-f59e0b?style=for-the-badge">
  </a>
  <a href="./templates/README.md">
    <img alt="Templates" src="https://img.shields.io/badge/templates-copyable-7c3aed?style=for-the-badge">
  </a>
  <a href="./LICENSE">
    <img alt="License MIT" src="https://img.shields.io/badge/license-MIT-111827?style=for-the-badge">
  </a>
  <a href="https://github.com/HenriqueCotta/ownership-driven-ai-customization-architecture/releases">
    <img alt="Latest Release" src="https://img.shields.io/github/v/release/HenriqueCotta/ownership-driven-ai-customization-architecture?style=for-the-badge">
  </a>
</p>

# Ownership-Driven Architecture (ODA)

A scalable architecture for GitHub Copilot custom instructions, path-specific instructions, skills, and AGENTS.md across large repositories and monorepos.

It helps teams organize `baseline`, `ownership tree`, `cross-cutting overlays`, `Follow-Through Triggers`, and `skills` without turning everything into custom agents.

Formal architecture name:

- `Ownership-Driven Architecture`

Portuguese version:

- [README.pt-BR.md](./README.pt-BR.md)

## On This Page

- [Ownership-Driven Architecture (ODA)](#ownership-driven-architecture-oda)
  - [On This Page](#on-this-page)
  - [Who This Is For](#who-this-is-for)
  - [Architecture Snapshot](#architecture-snapshot)
  - [Why This Exists](#why-this-exists)
  - [What You Get](#what-you-get)
  - [Quick Start](#quick-start)
  - [Repository Map](#repository-map)
  - [Principles](#principles)
  - [Open Source Intent](#open-source-intent)
  - [License](#license)

## Who This Is For

This repository is for teams that need to scale GitHub Copilot customization across:

- large repositories
- monorepos
- path-specific instruction maps
- shared skills
- AGENTS.md compatibility
- long-lived codebases with multiple ownership boundaries

## Architecture Snapshot

At a glance, the model separates:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `skills`

Keep the repository overview short here.

Put the canonical ownership-tree layout, naming rules, and shortcuts in [docs/en/rules/ownership-tree-grammar.md](./docs/en/rules/ownership-tree-grammar.md).

Put worked scenarios and repository archetypes in [docs/en/examples/README.md](./docs/en/examples/README.md).

## Why This Exists

Many Copilot setups grow in the same unhealthy direction:

- one large repository-wide instruction file
- duplicated rules across multiple files
- unclear responsibility boundaries
- custom agents created for topics that should have been instructions or skills
- stale docs and templates that drift away from the actual routing model

This project proposes a simpler operating model:

- keep the baseline short
- tie most behavior to ownership boundaries
- use overlays only for truly cross-cutting concerns
- keep downstream review and update behavior in `Follow-Through Triggers`
- use skills only for reusable workflows that would bloat always-on instructions

## What You Get

- architecture documentation in English and Brazilian Portuguese
- a clear rationale for why this model exists and where it fits
- a starter kit you can copy into a repository
- templates for baseline, ownership nodes, and overlays
- community files for running this as an open source project

## Quick Start

1. Read the architecture docs in [docs/en](./docs/en/README.md).
2. Read [Why This Architecture](./docs/en/why-this-architecture.md), [Operating Model](./docs/en/model/operating-model.md), [Decision Rules](./docs/en/rules/decision-rules.md), and [Ownership Tree Grammar](./docs/en/rules/ownership-tree-grammar.md).
3. Copy the [starter-kit](./starter-kit/README.md) into a test repository.
4. Adapt the ownership map to your own paths.
5. Add only the overlays that truly span multiple owners.
6. Keep workflows in skills, not in always-on instructions.

## Repository Map

- [docs/en](./docs/en/README.md)
  - English architecture docs
- [docs/pt-BR](./docs/pt-BR/README.md)
  - documentation in Brazilian Portuguese
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

- what worked
- what felt unclear
- what broke down at scale
- what naming or routing decisions improved the model

## License

This repository is released under the [MIT License](./LICENSE).
