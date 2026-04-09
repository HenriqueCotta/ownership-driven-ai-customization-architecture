# Ownership vs Overlay

Audience: maintainers who need to understand the most important conceptual distinction in the architecture.  
Goal: explain the difference between path-owned behavior and cross-cutting concerns before rule-writing begins.

## On This Page

- [The Core Distinction](#the-core-distinction)
- [Use Ownership When](#use-ownership-when)
- [Use An Overlay When](#use-an-overlay-when)
- [Examples](#examples)
- [Common Mistakes](#common-mistakes)
- [Related Docs](#related-docs)

## The Core Distinction

Use ownership when the path is the owner of a kind of logic.

Use an overlay when one extra concern spans several different owners.

Short version:

- `ownership`
  - who owns this path and its local behavior
- `overlay`
  - what extra lens should apply across several owners

## Use Ownership When

Choose ownership when:

- the path exists because that part of the repository owns a specific kind of logic
- maintainers would naturally explain the area as a subsystem, slice, or responsibility boundary
- the guidance is useful most of the time within that path

Ownership is about stable responsibility, not convenience grouping.

## Use An Overlay When

Choose an overlay when:

- the concern spans multiple ownership areas
- the concern is important enough to load automatically in matching paths
- the concern is not itself a stable architectural owner

An overlay is an extra lens, not a second ownership tree.

## Examples

- `src/api/orders/**/*.ts`
  - ownership node
  - that subtree owns order API logic
- `src/billing/invoices/**/*.ts`
  - ownership node
  - that subtree owns invoice logic
- `src/**/*.ts, tests/**/*.ts, scripts/**/*.ts`
  - good overlay candidate for language quality or testing quality
- `src/api/**/*.ts, src/billing/**/*.ts`
  - good overlay candidate for observability

`docs/**/*.md` is usually its own ownership node, not an overlay.

The relationship between code and docs usually comes from follow-through, not from turning docs into a cross-cutting layer.

## Common Mistakes

Treat these as modeling mistakes:

- using overlays to represent narrower owners
- naming overlays by crossed paths instead of by one coherent concern
- treating documentation as a cross-cutting concern when it is actually its own owned surface
- creating a new ownership node only because a change has downstream consequences

## Related Docs

- [Operating Model](./operating-model.md)
- [Follow-Through Triggers](./follow-through-triggers.md)
- [Decision Rules](../rules/decision-rules.md)
- [Examples](../examples/README.md)
