# Example Repositories

Audience: maintainers who understand the architecture in the abstract and now want to see what a well-implemented repository can look like.  
Goal: show generic repository archetypes, the ownership tree they would use, and how the architecture behaves in everyday situations.

## How To Use This Folder

Each file shows:

- a generic repository shape
- a healthy ownership-tree layout
- a small overlay set
- common day-to-day situations and which instructions should matter

These are not canonical repository templates.

They are teaching examples for the architecture.

## Included Repository Archetypes

- [API Service](./01-api-service.md)
  - a backend service with routes, contracts, config, tests, and docs
- [Web Product App](./02-web-product-app.md)
  - a frontend application with routes, design system, state, tests, and docs
- [Product Monorepo](./03-product-monorepo.md)
  - a monorepo with apps, packages, docs, and infrastructure boundaries

## What To Look For

As you read the examples, focus on these questions:

1. Which paths are stable ownership boundaries?
2. Which concerns deserve overlays instead of ownership nodes?
3. Which changes should trigger follow-through into tests, docs, configs, or operations?
4. How does the folder grammar stay readable as the repository gets bigger?
