# One File Node With Two Instruction Files

## Scenario

You have this repository path:

```text
src/api/orders.ts
```

That file needs two distinct kinds of guidance:

- contract guidance
- framework guidance

## Wrong First Guess

"A file can only have one ownership instruction, so I need a special naming workaround."

## Correct Classification

This is still one ownership node.

It is a file-level node with two instruction files.

## Why

The owned boundary is still the file itself:

- `src/`
- `src/api/`
- `src/api/orders.ts/`

The node does not change just because it needs more than one guidance lens.

Only the contents of the node change.

## On Disk

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        api/
          general.instructions.md
          orders.ts/
            contract.instructions.md
            framework.instructions.md
```

## Follow-Through

If the contract changes, the contract instruction may trigger tests and docs review.

If the request-handling flow changes, the framework instruction may trigger integration checks.
