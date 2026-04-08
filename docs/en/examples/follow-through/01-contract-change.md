# Contract Change

## Scenario

You change a public interface:

```text
src/contracts/payment_gateway.ts
```

## Wrong First Guess

"Only the contract file changed, so the change is local."

## Correct Classification

Primary instruction context:

- baseline
- language-quality instruction if the repo uses one
- ownership-tree node for contracts

## Why

Contracts are usually small files with large blast radius.

Even if the edit is local, the meaning of the change is not.

## Follow-Through

A `Follow-Through Triggers` section in the contract instruction may say:

- if fields, defaults, return semantics, or compatibility expectations changed, review implementations, tests, and reference docs

Expected flow:

1. change the contract,
2. inspect implementations,
3. inspect tests,
4. inspect docs,
5. update or explicitly justify no downstream change.
