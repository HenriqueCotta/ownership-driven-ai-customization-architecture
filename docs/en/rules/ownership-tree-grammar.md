# Ownership Tree Grammar

Audience: maintainers who need one predictable way to represent ownership boundaries on disk.  
Goal: define the canonical grammar of the ownership tree so the map is easy to teach, inspect, and extend.

## On This Page

- [Canonical Rule](#canonical-rule)
- [Canonical Grammar](#canonical-grammar)
- [What A Node Folder Can Contain](#what-a-node-folder-can-contain)
- [Optional Shortcut For A Simple File Node](#optional-shortcut-for-a-simple-file-node)
- [Naming Guidance](#naming-guidance)
- [When To Split A Node Into Multiple Instruction Files](#when-to-split-a-node-into-multiple-instruction-files)
- [Relationship To Follow-Through](#relationship-to-follow-through)
- [Related Material](#related-material)

## Canonical Rule

Represent every owned boundary as a node folder under `.github/instructions/ownership/`.

That rule applies whether the owned boundary in the repository is:

- a directory such as `src/api/`
- a file such as `src/api/orders.ts`

The folder is the node.

The instruction files inside the folder describe the guidance that belongs to that node.

## Canonical Grammar

Use these rules:

1. Every ownership boundary becomes a folder node.
2. Repository directories stay directories in the instruction tree.
3. Repository files may also become folder nodes, named after the file.
4. Instruction files inside a node folder are named by concern or purpose, not by the path again.
5. Child folders represent narrower ownership boundaries.

Minimal canonical example:

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

## What A Node Folder Can Contain

A node folder may contain:

- no instruction files yet
- one instruction file
- several instruction files
- narrower child nodes
- both instruction files and narrower child nodes at the same time

Mixed children are normal.

There is no required "main" or `_self` instruction file.

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

- you expect that file node to grow
- you want the most teachable and uniform grammar
- you want to avoid a second representation in the same area

## Naming Guidance

Name instruction files by concern or purpose.

Good examples:

- `general.instructions.md`
- `contract.instructions.md`
- `framework.instructions.md`
- `authorization.instructions.md`
- `diagnostics.instructions.md`

Because names such as `general.instructions.md` may repeat across the tree, prefer setting a clear frontmatter `name` for better labels in tools and UIs.

## When To Split A Node Into Multiple Instruction Files

Split only when the same owned boundary genuinely needs different guidance lenses.

Good reasons to split:

- one file needs both contract guidance and framework guidance
- one subtree needs both architecture guidance and authorization guidance
- one boundary has one stable set of general rules plus one narrower operational concern

Bad reasons to split:

- you are trying to encode downstream consequences as separate files
- you are duplicating the same advice with slightly different wording
- the extra file exists only because the naming scheme feels clever

## Relationship To Follow-Through

`Follow-Through Triggers` still lives inside the most relevant instruction file.

This convention changes how the tree is laid out on disk.

It does not create a new structural layer.

## Related Material

- [Operating Model](../model/operating-model.md)
- [Follow-Through Triggers](../model/follow-through-triggers.md)
- [Decision Rules](./decision-rules.md)
- [Examples](../examples/README.md)
- [Example Repositories](../example-repositories/README.md)
