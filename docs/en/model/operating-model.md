# Operating Model

Audience: maintainers who need the conceptual map of the architecture before writing rules or applying it to a repository.  
Goal: define the structural parts of the model clearly, without mixing in disk-layout conventions or rollout steps.

## On This Page

- [The Operating Formula](#the-operating-formula)
- [What The Architecture Standardizes](#what-the-architecture-standardizes)
- [The Structural Parts](#the-structural-parts)
- [Relationship Map](#relationship-map)
- [Related Docs](#related-docs)

## The Operating Formula

Use this formula:

- `baseline + ownership tree + cross-cutting overlays`

That formula describes the structural part of the architecture.

`Follow-Through Triggers` is not another structural layer.

It is a behavioral section that may live inside baseline, ownership, or overlay instructions.

## What The Architecture Standardizes

The architecture standardizes:

- the structural roles in the instruction map
- the path-first routing backbone
- the distinction between ownership and cross-cutting concerns
- where downstream review and update behavior belongs

It does not standardize the internal prose format of each instruction.

The headings, writing style, and exact Markdown organization inside an instruction still belong to the adopting repository or team.

## The Structural Parts

### Baseline

The baseline is the short repository-wide operating layer.

It should hold only guidance that is:

- broadly valid across the repository
- short enough to remain readable
- unlikely to change often
- useful no matter which ownership path is active

### Ownership Tree

The ownership tree is the path-based map of stable responsibility boundaries.

It answers:

- which part of the system owns this path
- where local behavioral guidance should live
- where narrower path-based refinement is legitimate

### Cross-Cutting Overlays

An overlay adds one extra concern across multiple ownership areas.

It exists for concerns that:

- span several owners
- still benefit from consistent guidance
- are not themselves stable architectural owners

### Skills

Skills are reusable workflows.

Use them for task-shaped guidance that is deeper than always-on instructions and should only be pulled in when relevant.

### Follow-Through Triggers

`Follow-Through Triggers` captures what else may now need review after a meaningful change.

It is not another file type.

It is the downstream consequence layer that sits inside the structural parts above.

## Relationship Map

Think of the model like this:

- `baseline`
  - broad repository defaults
- `ownership tree`
  - path-owned local behavior
- `cross-cutting overlays`
  - one extra lens across several owners
- `skills`
  - reusable workflows that should not always be loaded
- `Follow-Through Triggers`
  - downstream review and update consequences

The architecture stays scalable because each part has a narrow job.

## Related Docs

- [Ownership vs Overlay](./ownership-vs-overlay.md)
- [Follow-Through Triggers](./follow-through-triggers.md)
- [Decision Rules](../rules/decision-rules.md)
- [Ownership Tree Grammar](../rules/ownership-tree-grammar.md)
