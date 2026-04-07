# Ownership-Driven AI Customization Architecture

Audience: maintainers designing a scalable Copilot customization model for one or many repositories.  
Goal: define a reusable structure that is predictable, low-overhead, and easy to maintain.

## What This Folder Documents

This folder is repository-agnostic.

It documents a reusable architecture for organizing:

- repository-wide Copilot instructions,
- path-based ownership instructions,
- cross-cutting overlays,
- reusable skills,
- downstream review/update behavior.

Formal name:

- `Ownership-Driven AI Customization Architecture`

Operational shorthand:

- `baseline + ownership tree + cross-cutting overlays`

## Architecture At A Glance

The architecture has four structural parts:

- `baseline`
  - the short repository-wide operating layer
- `ownership tree`
  - instructions tied to stable path-owned responsibility boundaries
- `cross-cutting overlays`
  - instructions for concerns that span multiple owners
- `skills`
  - reusable workflows that are deeper than always-on instructions

`Follow-Through Triggers` is not another file type.

It is a section that may live inside baseline, ownership-tree, or overlay instructions to describe what else may need review after a meaningful change.

## When This Architecture Fits

Use this architecture when you want:

- a path-based customization model that can scale across many repositories,
- predictable routing without turning every concern into an agent,
- clear separation between ownership and cross-cutting concerns,
- a structure that stays readable for both first-time readers and long-term maintainers.

## Documentation Map

- [Why This Architecture](./why-this-architecture.md)
  - the business case, expected gains, non-goals, and alignment with official guidance
- [Core Model](./core-model.md)
  - the conceptual model, core terms, routing logic, and where follow-through belongs
- [Instruction Conflicts And Precedence](./instruction-conflicts-and-precedence.md)
  - what the platform really guarantees, how refinement should work, and how to avoid ambiguous instruction maps
- [Examples And Flows](./examples-and-flows.md)
  - worked examples that teach the model by scenario
- [Replication Playbook](./replication-playbook.md)
  - how to reproduce the architecture in other repositories

## Suggested Reading Paths

If this is your first contact with the architecture:

1. Read this file.
2. Read [Why This Architecture](./why-this-architecture.md).
3. Read [Core Model](./core-model.md).
4. Read [Examples And Flows](./examples-and-flows.md).

If you are designing a new repository:

1. Read this file.
2. Read [Why This Architecture](./why-this-architecture.md).
3. Read [Core Model](./core-model.md).
4. Read [Replication Playbook](./replication-playbook.md).

If you are debugging ambiguity or instruction conflicts:

1. Read this file.
2. Read [Instruction Conflicts And Precedence](./instruction-conflicts-and-precedence.md).
3. Read [Core Model](./core-model.md).
4. Read [Examples And Flows](./examples-and-flows.md).

## Core Design Rules

- Start with stable ownership boundaries, not abstract themes.
- Use overlays only for concerns that truly span multiple owners.
- Keep downstream review/update logic in `Follow-Through Triggers`, not in extra file types.
- Treat narrower instructions as refinements of broader ones, not as arbitrary reversals.
- Keep the overview short and push detail into dedicated reference documents.
