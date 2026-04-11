# Instruction Conflicts And Precedence

Audience: maintainers who need to design a safe instruction map and avoid ambiguous guidance.  
Goal: explain what the platform clearly guarantees, what it does not guarantee, and how to write refinement safely.

## On This Page

- [Operational Reality](#operational-reality)
- [Safe Mental Model](#safe-mental-model)
- [Safe Refinement Pattern](#safe-refinement-pattern)
- [Practical Precedence Rules](#practical-precedence-rules)
- [Conflict Smells](#conflict-smells)
- [How To Fix A Conflict](#how-to-fix-a-conflict)
- [Related Architecture Docs](#related-architecture-docs)

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
- child: "Inside `src/api/orders/**`, map HTTP input early and call order services directly"

Bad:

- parent: "API handlers should stay thin and delegate business work"
- child: "Inside `src/api/orders/**`, put validation, business rules, persistence, and retries directly in the handler"

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
4. Put downstream review and update rules in `Follow-Through Triggers`.
5. Anchor a follow-through trigger in the instruction that can observe the originating change.
6. Reuse a small outcome-based skill set rather than creating one skill per trigger.
7. Keep exact repeatable procedures in scripts, CI, or runbooks.
8. Keep discoverability hints inside existing docs or instructions rather than inventing a hint layer.
9. If two instructions seem to fight, fix the ownership map instead of hoping precedence will save you.

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
- a new skill is proposed for every trigger or ownership node
- exact procedural steps are being copied into generic instructions or skills
- a separate hint layer is being proposed just to connect triggers and skills

## How To Fix A Conflict

When conflict appears, start with the map itself:

1. Move broad defaults upward into the broadest real owner.
2. Move local specialization downward into the narrowest real owner.
3. Rewrite child guidance as refinement instead of reversal.
4. Move truly cross-cutting concerns into overlays.
5. Keep downstream review and update behavior inside `Follow-Through Triggers` rather than inventing a new layer.
6. Move any misplaced follow-through rule to the instruction scope that can actually observe its triggering change.
7. Consolidate overlapping workflow variants into a small set of outcome-based skills instead of one skill per trigger.
8. Move exact procedural steps into scripts, CI, or runbooks when natural-language guidance becomes brittle.
9. Keep any discoverability text as a small cue inside existing docs or instructions rather than a new hint layer.

If the map is clean, the need for hard conflict resolution usually drops sharply.

## Related Architecture Docs

- [Ownership vs Overlay](../model/ownership-vs-overlay.md)
- [Follow-Through Triggers](../model/follow-through-triggers.md)
- [Decision Rules](./decision-rules.md)
- [Ownership Tree Grammar](./ownership-tree-grammar.md)
- [Examples](../examples/README.md)
