# Follow-Through Triggers

Audience: maintainers who need to model downstream review and update behavior without inventing extra layers.  
Goal: explain what `Follow-Through Triggers` is, why it exists, and where it should live.

## On This Page

- [What Follow-Through Triggers Is](#what-follow-through-triggers-is)
- [Why It Exists](#why-it-exists)
- [Where It Lives](#where-it-lives)
- [Typical Triggers](#typical-triggers)
- [What It Is Not](#what-it-is-not)
- [Related Docs](#related-docs)

## What Follow-Through Triggers Is

`Follow-Through Triggers` describes what else may now need review after a meaningful change.

It is a behavioral section inside an instruction.

It is not a separate file type and not another architectural layer.

## Why It Exists

Many important changes have secondary consequences:

- docs may now be stale
- tests may need updates
- configs may need review
- runbooks, dashboards, or workflows may need adjustment

The model makes those consequences explicit so they are not lost in prompt phrasing or hidden team memory.

## Where It Lives

`Follow-Through Triggers` should live inside the instruction that best understands the origin of the change.

Default placement:

- baseline
  - for short repository-wide downstream rules
- ownership node
  - when the source-side owner best understands the blast radius
- overlay
  - only when the downstream rule is truly owned by that cross-cutting concern

## Typical Triggers

Typical examples:

- a public contract changes
  - review consumers, docs, and tests
- configuration defaults change
  - review rollout assumptions, docs, and runtime checks
- behavior changes in a public API area
  - review tests, docs, and error handling expectations

## What It Is Not

`Follow-Through Triggers` is not:

- a second ownership tree
- a reason to create new instruction files by itself
- a replacement for CI, review, or testing

It is a structured reminder of likely downstream work.

## Related Docs

- [Operating Model](./operating-model.md)
- [Ownership vs Overlay](./ownership-vs-overlay.md)
- [Decision Rules](../rules/decision-rules.md)
- [Examples](../examples/README.md)
