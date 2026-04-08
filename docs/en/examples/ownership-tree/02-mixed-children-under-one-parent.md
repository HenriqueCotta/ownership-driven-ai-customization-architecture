# Mixed Children Under One Parent

## Scenario

You have this repository shape:

```text
src/routes/
  health.ts
  orders.ts
  admin/
    users.ts
```

## Wrong First Guess

"The tree becomes confusing here because some children are files and one child is a folder."

## Correct Classification

This is a normal ownership-tree shape.

One parent can contain:

- file nodes
- narrower directory nodes
- instruction files for the parent itself

## Why

All of these are children of the same owned boundary:

- `src/routes/health.ts`
- `src/routes/orders.ts`
- `src/routes/admin/`

The folder grammar handles this naturally because both repository files and repository directories are represented as node folders.

## On Disk

```text
.github/
  instructions/
    ownership/
      src/
        routes/
          general.instructions.md
          health.ts/
            diagnostics.instructions.md
          orders.ts/
            contract.instructions.md
            framework.instructions.md
          admin/
            authorization.instructions.md
            users.ts/
              validation.instructions.md
```

## Follow-Through

The parent node can carry broad route guidance.

Each child node can carry narrower behavior without forcing a second tree grammar.
