# Documentation As Its Own Owner

## Scenario

You edit:

```text
docs/orders.md
```

## Wrong First Guess

"Documentation must always be an overlay because it relates to code."

## Correct Classification

`docs/**/*.md` is usually its own ownership-tree node.

## Why

Documentation is its own surface with its own quality rules:

- clarity,
- source of truth,
- structure,
- update discipline.

It is related to code, but that relationship is usually expressed through follow-through, not by turning docs into an overlay for source code.

## Follow-Through

If the doc is being changed because code already changed, Copilot should verify:

- the current implementation,
- the related tests,
- whether the doc is still accurate.
