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
2. use the trigger to inspect implementations, tests, and docs,
3. if the downstream work is small, update those surfaces directly,
4. if the change exposed broader documentation drift, reuse a generic docs-sync or review skill,
5. if the repository has exact compatibility scans or validation commands, keep them in automation or runbooks; use skills for the broader review workflow around them.
