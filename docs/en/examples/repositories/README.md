# Repository Archetypes

Audience: maintainers who already understand the architecture in the abstract and now want realistic repository archetypes.
Goal: show selective ownership maps, small overlay sets, and prompt-driven workflows that resemble day-to-day usage.

## On This Page

- [How To Use This Folder](#how-to-use-this-folder)
- [Included Repository Archetypes](#included-repository-archetypes)
- [What To Look For](#what-to-look-for)

## How To Use This Folder

Each file shows:

- a generic repository shape
- a realistic ownership map, not an exhaustive one
- a small overlay set
- prompt-driven situations that show how the architecture helps in practice

These are not canonical repository templates.

They are teaching examples for how a healthy repository usually applies the architecture:

- not every folder gets its own node
- not every file gets its own instruction
- many paths rely on broader owners plus overlays plus follow-through

## Included Repository Archetypes

- [API Service](./01-api-service.md)
  - a backend service with routes, contracts, config, tests, and docs
- [Web Product App](./02-web-product-app.md)
  - a frontend application with features, design system, state, tests, and UX docs
- [Product Monorepo](./03-product-monorepo.md)
  - a monorepo with apps, shared packages, docs, and infrastructure boundaries

## What To Look For

As you read the examples, focus on these questions:

1. Which paths really deserve their own ownership nodes?
2. Which paths intentionally stay under broader owners?
3. Which overlays are small but genuinely useful?
4. How does the architecture shape the prompt, the implementation flow, and the follow-through?
