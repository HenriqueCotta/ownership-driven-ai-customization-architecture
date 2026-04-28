# Source-Specific Interpretation Instruction

## Situation

A repository uses a work board to track planned work, deferred follow-through, release coordination, and accepted follow-ups.

The supporting-source instruction already has a compact `work-board` source entry.

That entry is enough for most tasks.

The team also has a few repo-owned rules about how to interpret board state. Those rules are important, but they are too detailed for the central source map.

## Preferred Default

Avoid creating one instruction per source.

Most sources should stay as compact entries:

```md
## work-board

Where: board `checkout-work`
Access: project-management MCP, if available.
Use for: planned work, accepted follow-ups, and explicit carry-forward.
Do not use for: current behavior unless linked to merged code, tests, or accepted docs.
If unavailable: do not invent board state; surface missing planning context when it could change the result.
```

This keeps the source map easy to scan.

## When The Extra Instruction Is Worth It

Create a source-specific interpretation instruction only when the source has repo-owned interpretation policy that lighter source guidance cannot carry safely, and the value of that policy justifies always-on context.

That last point matters.

Current path-specific instructions route by file path. If board interpretation can apply anywhere in the repository, the instruction usually needs `applyTo: "**"`, which means it can stay in context whenever that surface supports matching instructions.

## Repository Shape

```text
<repository-root>/
  .github/
    copilot-instructions.md
    instructions/
      ownership/
        repository/
          supporting-sources.instructions.md
          work-board.instructions.md
      overlays/
```

## Supporting Source Entry

```md
## work-board

Where: board `checkout-work`
Access: project-management MCP, if available.
Use for: planned work, accepted follow-ups, and explicit carry-forward.
Do not use for: current behavior unless linked to merged code, tests, or accepted docs.
Details: use `ownership/repository/work-board.instructions.md` only when board interpretation could change the decision.
```

## Source-Specific Interpretation Instruction

```md
---
applyTo: "**"
---

# Work Board Interpretation

Use this instruction only when the task involves planned work, deferred follow-through, issue status, release coordination, or board-backed decisions.

The board owns planning state and explicit carry-forward. It does not prove current implementation behavior unless linked to merged code, tests, or accepted docs.

If board state conflicts with code, tests, or accepted docs, classify the disputed claim first. Code and tests own current implementation behavior. Accepted docs own documented behavior. The board owns planned or deferred work.

Do not create, move, close, or rewrite board items unless the user asks for board changes or the repository closure policy requires explicit carry-forward.
```

## What Stays Out

Do not put exact board operations in this instruction.

Operational board changes belong in an explicit procedural workflow surface.

## Teaching Takeaway

A source-specific interpretation instruction is useful when the repository needs durable interpretation policy for a source.

It is not the default source format.

Use it carefully because repo-wide source-specific interpretation instructions are often always-on context.
