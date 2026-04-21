# Shared Trigger Beats Repeated Local Copies

## Scenario

A repository has sibling ownership nodes such as:

```text
src/domain/orders/
src/domain/payments/
src/domain/invoices/
```

Each local instruction is starting to gain its own trigger list for tests, docs, examples, and observability.

## Wrong First Guess

"Every node with an instruction should also have its own local trigger list."

## Correct Classification

If the downstream rule is mostly the same across siblings, the shared part usually belongs in a broader source-side owner or in the baseline.

The narrower nodes should keep only truly local deltas, or no trigger at all.

## Why

Repeated local enumeration drifts quickly:

- one node forgets tests
- another adds docs but forgets examples
- another uses different wording for the same idea

That creates duplication without trustworthy coverage.

## Better Shape

Broader shared rule:

- if public behavior, contract meaning, defaults, or operational expectations changed, review the downstream surfaces that encode those expectations

Only keep local additions when they are genuinely different, such as:

- a payments node that must also review compliance evidence
- an invoices node that must also review generated PDF fixtures

## Follow-Through

Expected flow:

1. check whether the local node really has a unique downstream consequence,
2. if not, remove the repeated local trigger and move the shared rule upward,
3. keep only true local deltas in the narrower node,
4. reuse the same small skill set for the broader review instead of inventing one skill per local trigger.
