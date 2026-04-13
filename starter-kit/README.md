# Starter Kit

This starter kit is a small, copyable example of the Ownership-Driven Architecture.

It is not meant to be a universal default.

It is meant to give you:

- a clear starting structure
- a minimal ownership tree
- a minimal overlay set
- two example outcome-based skills
- one canonical way to represent ownership nodes on disk

## Included Structure

```text
starter-kit/
  .github/
    copilot-instructions.md
    instructions/
      ownership/
        src/
          general.instructions.md
          api/
            general.instructions.md
            admin/
              general.instructions.md
            orders.ts/
              contract.instructions.md
              framework.instructions.md
        docs/
          general.instructions.md
      overlays/
        quality/
          testing-quality.instructions.md
        operability/
          observability.instructions.md
    skills/
      debug-behavior/
        SKILL.md
      sync-docs/
        SKILL.md
```

## How To Read This Tree

Use this simple grammar:

- every owned boundary is represented by a folder node
- repository directories stay directories in the instruction tree
- repository files also become folder nodes, such as `orders.ts/`
- instruction files inside each node are named by concern, such as `general`, `contract`, or `framework`
- a node folder may contain zero, one, or many instruction files

That means:

- `src/` is a broad ownership node
- `src/api/` is a narrower ownership node
- `src/api/admin/` is a narrower subtree node
- `src/api/orders.ts/` is a file-level ownership node with two distinct instruction files

There is no required "main" instruction file for a node.

If one file is enough, keep one.

If several concerns belong to the same node, split them into several files.

Optional shortcut:

- a leaf file node with exactly one instruction may be written directly as `orders.ts.instructions.md`
- this starter kit keeps the folder form because it teaches the canonical grammar

## How To Use It

1. Copy `.github/` into a repository you want to test.
2. Replace the example `applyTo` values with your real ownership map.
3. Remove anything you do not need.
4. Add narrower ownership nodes only when a subtree truly needs different guidance.
5. Split one node into several instruction files only when that node truly needs several distinct guidance lenses.
6. Add overlays only when one concern spans multiple owners.
7. Keep the skill set small and outcome-based instead of creating one skill per follow-through trigger.
8. Prefer scripts, CI checks, or runbooks when a process needs exact repeatable steps.

## Important

- the folder is the ownership node
- `general.instructions.md`, `contract.instructions.md`, and `framework.instructions.md` are instruction files that live inside a node
- repeated filenames such as `general.instructions.md` are fine; use frontmatter `name` for clearer UI labels
- `testing-quality.instructions.md` and `observability.instructions.md` are overlays.
- `Follow-Through Triggers` live inside those files. They are not a separate file type.
- The trigger condition should be anchored in the instruction that can observe the originating change.
- Many different follow-through triggers should usually reuse the same few skills, such as docs sync, review, or debugging.
- Exact procedures belong better in scripts, CI, or runbooks than in generic trigger or skill prose.
- The internal writing format of each instruction is repository-owned. The example files here show one possible shape, not a required one.
