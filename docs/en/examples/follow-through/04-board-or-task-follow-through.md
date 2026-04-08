# Board Or Task Follow-Through

## Scenario

You finish an implementation and realize the scope changed:

- one acceptance criterion is no longer correct
- a new follow-up item was discovered

## Wrong First Guess

"Task tracking should be another owner under `src`."

## Correct Classification

Task tracking is usually a cross-cutting overlay.

## Why

It spans many kinds of work:

- code,
- docs,
- design,
- operations,
- rollout.

## Follow-Through

A `Follow-Through Triggers` section may say:

- if scope, status, acceptance criteria, or follow-up work changed materially, review task tracking

Expected flow:

1. reassess what changed,
2. decide whether the task is now stale,
3. update it if the workflow supports that,
4. otherwise explain exactly what needs updating.
