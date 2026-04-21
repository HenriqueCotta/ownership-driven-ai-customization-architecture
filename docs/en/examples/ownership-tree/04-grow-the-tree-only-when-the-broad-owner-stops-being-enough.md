# Grow The Tree Only When The Broad Owner Stops Being Enough

## Scenario

A team starts ODA adoption in:

```text
src/app/
```

and wants to create instructions immediately for:

```text
src/app/
src/app/checkout/
src/app/checkout/forms/
src/app/checkout/forms/address/
src/app/checkout/forms/payment/
```

## Wrong First Guess

"If we do not map every level now, we are not really applying ODA."

## Correct Classification

Start with the broadest owner that still gives honest and useful guidance.

Add narrower nodes only after a subtree proves it needs different local guidance.

## Why

Early deep trees often create:

- long instruction sets with little local value
- repeated wording across nearby nodes
- fake precision before the team understands where the real boundaries are

ODA is meant to be growable, not finished all at once.

## Better First Pass

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
      src/app/
        general.instructions.md
```

Later, if checkout truly needs distinct guidance:

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
      src/app/
        general.instructions.md
        checkout/
          general.instructions.md
```

## Follow-Through

Expected flow:

1. start with the broad owner,
2. validate real work against that owner,
3. add a narrower node only when the broad node stops being enough,
4. avoid creating leaf-node instructions just to mirror the repository tree.
