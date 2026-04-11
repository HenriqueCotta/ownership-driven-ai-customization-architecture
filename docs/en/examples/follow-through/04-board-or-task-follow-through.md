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
2. use the trigger to inspect the affected task or board state,
3. if the update is straightforward, make it directly,
4. if the repository uses a broader planning or review workflow, reuse that generic skill instead of creating a task-specific skill for this trigger,
5. if the repository has exact board automation, keep it in scripts or platform workflow rules; use skills for the broader review or planning workflow around it.
