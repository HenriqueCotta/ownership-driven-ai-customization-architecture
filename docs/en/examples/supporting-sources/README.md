# Supporting Source Examples

These examples show how repositories can use supporting sources without turning them into another ODA layer.

They are examples of shape and judgment, not required templates.

## On This Page

- [Included Examples](#included-examples)
- [Reading Cue](#reading-cue)
- [Naming Cue](#naming-cue)

## Included Examples

Read them as variations:

- [One Local Source](./01-one-local-source.md)
  - the smallest useful local-source pattern and common implementation questions
- [Repository-Root Supporting-Source Instruction](./02-repository-root-supporting-source-instruction.md)
  - a repository-root source instruction with mixed entry styles
- [Consumer Instructions](./03-consumer-instructions.md)
  - owners and overlays that refer to source IDs without restating access details
- [Multiple Sources And Conflicts](./04-multiple-sources-and-conflicts.md)
  - several sources, claim ownership, conflict handling, and a reconciliation skill
- [Local Summary As Safety Guard](./05-local-summary-as-safety-guard.md)
  - when a small duplicate summary is safer than relying on access alone
- [Source-Specific Interpretation Instruction](./06-source-specific-interpretation-instruction.md)
  - when a source needs durable interpretation policy, but not exact operations

## Reading Cue

Use the lightest form that makes source use clear.

If a source is obvious and local, the example can stay small.

If a source is external, private, live, or likely to conflict with other evidence, give the agent enough location, access, fallback, and conflict guidance to avoid guessing.

If one source needs detailed interpretation policy, prefer a separate source-specific instruction only when lighter source guidance would not be enough.

Be cautious with repo-wide source-specific instructions because they usually require `applyTo: "**"` and can become always-on context.

## Naming Cue

Consumer instructions should usually reference a stable source ID:

```md
Use supporting source `product-docs`.
```

That is clearer than relying on a human title such as `Sources > Product Documentation`, and it does not force one exact filename or heading structure.
