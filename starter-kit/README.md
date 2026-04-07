# Starter Kit

This starter kit is a small, copyable example of the Ownership-Driven AI Customization Architecture.

It is not meant to be a universal default.

It is meant to give you:

- a clear starting structure
- a minimal ownership tree
- a minimal overlay set
- two example skills

## Included Structure

```text
starter-kit/
  .github/
    copilot-instructions.md
    instructions/
      ownership/
        src.instructions.md
        api.instructions.md
        docs.instructions.md
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

## How To Use It

1. Copy `.github/` into a repository you want to test.
2. Replace the example `applyTo` values with your real ownership map.
3. Remove anything you do not need.
4. Add narrower ownership nodes only when a subtree truly needs different guidance.
5. Add overlays only when one concern spans multiple owners.

## Important

- `src.instructions.md` and `api.instructions.md` are ownership nodes.
- `testing-quality.instructions.md` and `observability.instructions.md` are overlays.
- `Follow-Through Triggers` live inside those files. They are not a separate file type.
- The internal writing format of each instruction is repository-owned. The example files here show one possible shape, not a required one.
