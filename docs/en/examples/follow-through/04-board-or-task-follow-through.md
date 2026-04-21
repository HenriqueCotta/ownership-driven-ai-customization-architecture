# Board Or Task Follow-Through

## Scenario

You finish an implementation and realize the scope changed:

- one acceptance criterion is no longer correct
- a new follow-up item was discovered

## Wrong First Guess

"Task tracking should be another owner under `src`."

## Correct Classification

If the repository keeps task tracking or planning state inside the repository map, it is usually a cross-cutting overlay.

If that carry-forward surface lives outside the repository, it stays outside the repository map.

## Why

When a repository chooses to preserve follow-through outside conversation memory, that planning surface can span many kinds of work:

- code,
- docs,
- design,
- operations,
- rollout.

## Follow-Through

A `Follow-Through Triggers` section may say:

- if scope, status, acceptance criteria, or follow-up work changed materially, review the repository's explicit carry-forward surface when one exists

Expected flow:

1. reassess what changed,
2. use the trigger to inspect the affected board, task, or equivalent carry-forward surface if the repository keeps one,
3. if the update is straightforward, make it directly,
4. if the repository uses a broader planning or review workflow, reuse that generic skill instead of creating a task-specific skill for this trigger,
5. if the repository has exact board automation, keep it in scripts or platform workflow rules; use skills for the broader review or planning workflow around it.
