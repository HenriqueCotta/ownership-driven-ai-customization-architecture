# One Path, One Owner

## Scenario

You have this path:

```text
src/api/orders/create_order.ts
```

## Wrong First Guess

"This needs an overlay because it is important."

## Correct Classification

This is an ownership-tree problem.

Likely ownership nodes:

- `src/**/*.ts`
- `src/api/**/*.ts`
- `src/api/orders/**/*.ts`

## Why

The path belongs to a clear responsibility boundary:

- code,
- then API code,
- then order API code.

That is hierarchy by ownership, not a cross-cutting concern.

## Follow-Through

No downstream review is required unless the change affects behavior, contracts, config, or documentation.
