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
2. inspect sample configs,
3. inspect tests,
4. inspect docs,
5. update or justify no-op.
