# Narrower Owner vs Overlay

## Scenario

You have these paths:

```text
src/api/orders/**/*.ts
src/billing/invoices/**/*.ts
```

## Wrong First Guess

"These are two special cases, so they should be overlays."

## Correct Classification

These are narrower ownership-tree nodes.

## Why

They are different because each subtree owns a different kind of logic:

- order API logic
- invoice logic

That is ownership.

An overlay would be something like:

```text
src/api/**/*.ts
src/billing/**/*.ts
```

for one shared concern such as observability, retries, or error reporting.

## Follow-Through

If you add a new invoice lifecycle state, you may need:

- billing tests
- billing docs
- telemetry review

But the ownership decision still comes first: invoice logic is owned by the invoice subtree.
