# Instruction Conflicts And Precedence

Audience: maintainers who need to design a safe instruction map and avoid ambiguous guidance.  
Goal: explain how matching instructions behave in practice, what the platform guarantees, and how to write refinement safely.

## Operational Reality

This section describes the practical model, not the idealized one.

What the platform clearly guarantees:

- repository-wide instructions and matching path-specific instructions are both provided when the path matches
- higher-level instruction sources have precedence when conflicts occur, for example personal instructions over repository instructions, and repository instructions over organization instructions

What the platform does not clearly guarantee:

- a fully deterministic object-oriented override model between multiple matching repository instruction files
- a published rule that says "the deepest matching path always wins" in every case

That means you should not design repository instructions as if they were strict inheritance with guaranteed override semantics.

Use the ownership tree as a design discipline, not as a promise of runtime conflict resolution.

## Safe Mental Model

The safest mental model is:

- broader instructions set defaults
- narrower instructions refine those defaults
- overlays add another lens
- `Follow-Through Triggers` describe downstream consequences

If two matching instructions truly contradict each other, the outcome is less predictable than normal code inheritance.

## Safe Refinement Pattern

Write parent and child instructions as refinement, not reversal.

Good:

- parent: "API handlers should stay thin and delegate business work"
- child: "inside `src/api/orders/**`, map HTTP input early and call order services directly"

Bad:

- parent: "API handlers should stay thin and delegate business work"
- child: "inside `src/api/orders/**`, put validation, business rules, persistence, and retries directly in the handler"

Why the first one is safer:

- the child narrows the parent inside a smaller boundary
- the child adds local detail without undoing the larger rule

Why the second one is risky:

- the child tries to reverse the parent
- if both instructions are present, the model receives conflicting guidance instead of refined guidance

## Practical Precedence Rules

When in doubt, use these rules:

1. Put the broad default in the broadest owner that truly owns it.
2. Put local specialization in the narrowest owner that truly needs it.
3. Put cross-cutting quality guidance in overlays.
4. Put downstream review/update rules in `Follow-Through Triggers`.
5. If two instructions seem to fight, fix the ownership map instead of hoping precedence will save you.

In other words:

- rely on structure to reduce conflict
- do not rely on hidden precedence to clean conflict up later

## Conflict Smells

Treat these as signs that the instruction map needs redesign:

- the same rule appears in multiple instructions
- a child instruction tries to reverse the parent instead of refining it
- an overlay is named by crossed paths instead of by one coherent concern
- a docs path is treated as an overlay when it should be its own owner
- a new instruction is proposed only because a change has downstream consequences

## How To Fix A Conflict

When conflict appears, start with the map itself:

1. Move broad defaults upward into the broadest real owner.
2. Move local specialization downward into the narrowest real owner.
3. Rewrite child guidance as refinement instead of reversal.
4. Move truly cross-cutting concerns into overlays.
5. Keep downstream review/update behavior inside `Follow-Through Triggers` rather than inventing a new layer.

If the map is clean, the need for hard conflict resolution usually drops sharply.
