# Configuration Change

## Scenario

You change config loading or defaults:

```text
src/config/load_config.ts
```

## Wrong First Guess

"This is internal plumbing, so only the config file matters."

## Correct Classification

Primary instruction context:

- baseline
- ownership-tree node for configuration

Possible downstream surfaces:

- docs
- sample config files
- tests

## Why

Configuration changes often affect what users type, what operators expect, and what tests encode.

## Follow-Through

A `Follow-Through Triggers` section may say:

- if precedence, defaults, source-of-truth rules, or validation changed, review examples, docs, and tests

Expected flow:

1. change config behavior,
2. use the trigger to inspect sample configs, tests, and docs,
3. if the downstream work is small, update those surfaces directly,
4. if the change exposed broader docs or operator drift, reuse a generic impact-review skill or a narrower repository-owned docs-reconciliation skill,
5. if the repository has exact validation commands or rollout checks, keep them in automation or runbooks; use skills for the broader review workflow around them.
