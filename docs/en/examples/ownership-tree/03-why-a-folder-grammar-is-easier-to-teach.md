# Why A Folder Grammar Is Easier To Teach

## Scenario

A new maintainer needs to understand which ownership instructions apply to:

```text
src/api/orders.ts
```

## Wrong First Guess

"We need a special explanation for directory owners and another explanation for file owners."

## Correct Classification

The same teaching path works for both:

1. find the repository path,
2. walk the same path in `ownership/`,
3. read the instruction files in the matching node folders.

## Why

That teaching script works because the folder is always the node.

The reader does not need to memorize:

- file-node exceptions
- promotion rules
- hidden meanings in filenames

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
```

## Follow-Through

Once the reader knows which ownership nodes apply, they can evaluate overlays and follow-through in the usual way.
