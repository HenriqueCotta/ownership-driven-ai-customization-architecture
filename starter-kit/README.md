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
      impact-review/
        SKILL.md
```

## Support Note

This starter kit assumes a Copilot surface that can load repository-wide instructions, path-specific instructions, and, when relevant, skills.

Not every surface supports that full combination in the same way.

If you test in a surface that only reads `.github/copilot-instructions.md`, you will not see the full ownership-tree behavior from `.github/instructions/**`, and you may not see repository skills at all.

Check GitHub's current support docs before treating a partial result as an ODA problem:

- [Support for different types of custom instructions](https://docs.github.com/en/copilot/reference/custom-instructions-support)
- [Creating agent skills for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)

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
7. Add a `Follow-Through Triggers` section only when that instruction has a real, source-anchored downstream rule worth stating.
8. If several sibling nodes would repeat almost the same trigger, move the shared part upward instead of copying it downward.
9. Keep the skill set small and outcome-based instead of creating one skill per follow-through trigger.
10. Keep the included baseline if its short hybrid closure policy fits your repository, or replace that policy with your own short default.
11. Prefer scripts, CI checks, or runbooks when a process needs exact repeatable steps.
12. If the repository will actively maintain its Copilot customization over time, consider also copying the optional [oda-copilot-customization skill](../.github/skills/oda-copilot-customization/SKILL.md) from this repository.
13. If you want to reuse that skill across repositories, point Copilot CLI at this repository's `.github/skills` directory with `/skills add`, or copy the skill into the personal skills location your tooling supports.

## Important

- the folder is the ownership node
- `general.instructions.md`, `contract.instructions.md`, and `framework.instructions.md` are instruction files that live inside a node
- repeated filenames such as `general.instructions.md` are fine; use frontmatter `name` for clearer UI labels
- `testing-quality.instructions.md` and `observability.instructions.md` are overlays.
- `Follow-Through Triggers` live inside those files. They are not a separate file type.
- Not every instruction needs a trigger section.
- Some included examples intentionally omit `Follow-Through Triggers`. The admin API owner relies on broader source/API follow-through, and the testing overlay is shown as a pure cross-cutting guidance overlay.
- The trigger condition should be anchored in the instruction that can observe the originating change.
- If many local triggers would say almost the same thing, that is usually a sign to move the shared rule upward.
- The included baseline already demonstrates a short hybrid closure policy. Keep it if it fits, or replace it with your repository's own short default.
- Many different follow-through triggers should usually reuse the same few skills, such as `impact-review`, docs reconciliation, or debugging.
- If the repository needs a reusable workflow for shaping or auditing the customization map itself, `oda-copilot-customization` is a good optional repository-maintenance skill.
- Exact procedures belong better in scripts, CI, or runbooks than in generic trigger or skill prose.
- The internal writing format of each instruction is repository-owned. The example files here show one possible shape, not a required one.
