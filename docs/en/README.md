# Ownership-Driven Architecture (ODA)

Audience: maintainers designing a scalable Copilot customization model for one or many repositories.  
Goal: provide a documentation portal that makes the architecture easy to learn, inspect, and reuse.

## What This Folder Documents

It documents a reusable architecture for organizing:

- repository-wide Copilot instructions
- path-based ownership instructions
- cross-cutting overlays
- reusable skills
- downstream follow-through behavior

Formal name:

- `Ownership-Driven Architecture`

Operational shorthand:

- `baseline + ownership tree + cross-cutting overlays`

This folder is repository-agnostic.

## On This Page

- [Ownership-Driven Architecture (ODA)](#ownership-driven-architecture-oda)
  - [What This Folder Documents](#what-this-folder-documents)
  - [On This Page](#on-this-page)
  - [Documentation Structure](#documentation-structure)
  - [Documentation Map](#documentation-map)
    - [Explanation](#explanation)
    - [Model](#model)
    - [Rules](#rules)
    - [How-To](#how-to)
    - [Recommended Skill](#recommended-skill)
    - [Worked Examples](#worked-examples)
  - [Suggested Reading Paths](#suggested-reading-paths)
  - [Core Design Rules](#core-design-rules)

## Documentation Structure

This documentation set is organized by reading intent:

- explanation
  - why the architecture exists
- model
  - what the system is and how its parts relate
- rules
  - the conventions and decision boundaries you consult while designing the map
- how-to
  - how to roll the model out in a real repository
- examples
  - how the model behaves in concrete situations

Each document should have one primary job.

If a page starts repeating another page, it should usually link instead of restating.

## Documentation Map

### Explanation

- [Why This Architecture](./why-this-architecture.md)
  - the business case, expected gains, non-goals, and standards alignment

### Model

- [Operating Model](./model/operating-model.md)
  - the structural vocabulary of the architecture
- [Ownership vs Overlay](./model/ownership-vs-overlay.md)
  - the core conceptual distinction in the model
- [Follow-Through Triggers](./model/follow-through-triggers.md)
  - what downstream follow-through guidance is for

### Rules

- [Decision Rules](./rules/decision-rules.md)
  - where guidance belongs and what to do when classification is unclear
- [Ownership Tree Grammar](./rules/ownership-tree-grammar.md)
  - the canonical on-disk grammar, naming rules, and shortcut policy
- [Instruction Conflicts And Precedence](./rules/instruction-conflicts-and-precedence.md)
  - what the platform clearly guarantees and how to avoid ambiguous maps

### How-To

- [Replication Playbook](./replication-playbook.md)
  - how to reproduce the architecture in another repository

### Recommended Skill

- [oda-copilot-customization](../../.github/skills/oda-copilot-customization/SKILL.md)
  - optional repository-maintenance skill for shaping, reviewing, or auditing Copilot customization itself against upstream ODA and current official GitHub Copilot guidance

### Worked Examples

- [Examples](./examples/README.md)
  - short scenario-based examples plus repository archetypes inside the same folder

## Suggested Reading Paths

If this is your first contact with the architecture:

1. Read this file.
2. Read [Why This Architecture](./why-this-architecture.md).
3. Read [Operating Model](./model/operating-model.md).
4. Read [Ownership vs Overlay](./model/ownership-vs-overlay.md).
5. Read [Follow-Through Triggers](./model/follow-through-triggers.md).
6. Read [Ownership Tree Grammar](./rules/ownership-tree-grammar.md).
7. Read [Examples](./examples/README.md).

If you are designing a new repository:

1. Read this file.
2. Read [Why This Architecture](./why-this-architecture.md).
3. Read [Operating Model](./model/operating-model.md).
4. Read [Follow-Through Triggers](./model/follow-through-triggers.md).
5. Read [Decision Rules](./rules/decision-rules.md).
6. Read [Ownership Tree Grammar](./rules/ownership-tree-grammar.md).
7. Read [Replication Playbook](./replication-playbook.md).
8. Read [Examples](./examples/README.md).

If you are debugging ambiguity or instruction conflicts:

1. Read this file.
2. Read [Instruction Conflicts And Precedence](./rules/instruction-conflicts-and-precedence.md).
3. Read [Ownership vs Overlay](./model/ownership-vs-overlay.md).
4. Read [Follow-Through Triggers](./model/follow-through-triggers.md).
5. Read [Decision Rules](./rules/decision-rules.md).
6. Read [Examples](./examples/README.md).

If you are shaping or auditing Copilot customization itself:

1. Read this file.
2. Read [Replication Playbook](./replication-playbook.md).
3. Read [Decision Rules](./rules/decision-rules.md).
4. Use the optional [oda-copilot-customization skill](../../.github/skills/oda-copilot-customization/SKILL.md).

## Core Design Rules

- Start with stable ownership boundaries, not abstract themes.
- Represent ownership boundaries with a tree that is easy to read before it is easy to optimize.
- Use overlays only for concerns that truly span multiple owners.
- Keep downstream follow-through logic in `Follow-Through Triggers`, not in extra file types.
- Compose follow-through from repository policy, source-anchored triggers, reusable skills, automation, and, when needed, an explicit carry-forward surface rather than searching for one universal trigger or one universal skill.
- Treat narrower instructions as refinements of broader ones, not as arbitrary reversals.
- Keep overview pages short and move detail into focused model and rules documents.
