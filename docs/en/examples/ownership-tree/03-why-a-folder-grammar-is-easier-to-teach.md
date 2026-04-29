# Why A Folder Grammar Is Easier To Teach

## On This Page

- [Scenario](#scenario)
- [Wrong First Guess](#wrong-first-guess)
- [Correct Classification](#correct-classification)
- [Why](#why)
- [On Disk](#on-disk)
- [Follow-Through](#follow-through)

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
2. enter the explicit root owner at `ownership/repository/`,
3. walk the same path inside that root owner,
4. read the instruction files in the matching node folders.

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
      repository/
        src/
          general.instructions.md
          api/
            general.instructions.md
            orders.ts/
              contract.instructions.md
```

## Follow-Through

Once the reader knows which ownership nodes apply, they can evaluate overlays and follow-through in the usual way.
