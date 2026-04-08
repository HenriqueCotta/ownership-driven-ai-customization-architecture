# Ownership Tree Convention

Audience: maintainers who need a simple, teachable way to lay out ownership-tree instructions on disk.  
Goal: define one canonical folder grammar, plus one small optional shortcut, that supports directory owners, file owners, mixed children, and multiple instructions per node without confusion.

## The One-Sentence Rule

Represent every owned boundary as a node folder under `.github/instructions/ownership/`.

That rule applies whether the owned boundary in the repository is:

- a directory such as `src/api/`
- a file such as `src/api/orders.ts`

The folder is the node.

The instruction files inside the folder describe the guidance that belongs to that node.

## The Canonical Grammar

Use these rules:

1. Every ownership boundary becomes a folder node.
2. Repository directories stay directories in the instruction tree.
3. Repository files also become folder nodes, named after the file.
4. Instruction files inside a node folder are named by concern or purpose, not by the path again.
5. Child folders represent narrower ownership boundaries.

Examples of concern-based names:

- `general.instructions.md`
- `contract.instructions.md`
- `framework.instructions.md`
- `authorization.instructions.md`
- `diagnostics.instructions.md`

## What A Node Folder Can Contain

A node folder may contain:

- no instruction files yet
- one instruction file
- several instruction files
- narrower child nodes
- both instruction files and narrower child nodes at the same time

There is no required "main" or `_self` instruction file.

If one instruction is enough, keep one.

If several distinct concerns belong to the same boundary, split them into several files.

For worked examples and teaching flows, read [Examples](./examples/README.md).

## Optional Shortcut For A Simple File Node

If a repository file is a leaf node and needs exactly one instruction, you may use a shorter file form:

- `src/api/orders.ts.instructions.md`

instead of:

- `src/api/orders.ts/<concern>.instructions.md`

Use this shortcut only when all of these are true:

- the owned boundary is a repository file, not a directory
- that file node needs exactly one instruction
- you are optimizing for a shorter tree

Prefer the canonical folder form when:

- you expect that file node to grow,
- you want the most teachable and uniform grammar,
- or you want to avoid introducing a second representation in the same area.

If that file node later needs a second instruction, switch it to the canonical folder form.

## Naming Guidance

Since names such as `general.instructions.md` may repeat across the tree, prefer setting a clear frontmatter `name` for better labels in tools and UIs.

Example:

```md
---
name: "ownership: src api orders contract"
description: "Contract guidance for the orders API file."
applyTo: "src/api/orders.ts"
---
```

The repeated filename is fine.

The `name` field is what makes the UI label human-friendly.

If you use the single-file shortcut, the same advice still applies:

```md
---
name: "ownership: src api orders"
description: "General guidance for the orders API file."
applyTo: "src/api/orders.ts"
---
```

## When To Split A Node Into Multiple Instruction Files

Split only when the same owned boundary needs genuinely different guidance lenses.

Good reasons to split:

- one file needs both contract guidance and framework guidance
- one subtree needs both architecture guidance and authorization guidance
- one boundary has one stable set of general rules plus one narrower operational concern

Bad reasons to split:

- you are trying to encode downstream consequences as separate files
- you are duplicating the same advice with slightly different wording
- the extra file exists only because the naming scheme feels clever

## Relationship To Follow-Through

`Follow-Through Triggers` still live inside the most relevant instruction file.

This convention changes how the tree is laid out on disk.

It does not create a new structural layer.
