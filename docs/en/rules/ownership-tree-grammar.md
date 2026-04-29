# Ownership Tree Grammar

Audience: maintainers who need one predictable way to represent ownership boundaries on disk.  
Goal: define the canonical grammar of the ownership tree so the map is easy to teach, inspect, and extend.

## On This Page

- [Canonical Rule](#canonical-rule)
- [Canonical Grammar](#canonical-grammar)
- [Repository Root Owner](#repository-root-owner)
- [What A Node Folder Can Contain](#what-a-node-folder-can-contain)
- [Optional Shortcut For A Simple File Node](#optional-shortcut-for-a-simple-file-node)
- [Naming Guidance](#naming-guidance)
- [When To Add A Narrower Node](#when-to-add-a-narrower-node)
- [When To Split A Node Into Multiple Instruction Files](#when-to-split-a-node-into-multiple-instruction-files)
- [Relationship To Follow-Through](#relationship-to-follow-through)
- [Related Material](#related-material)

## Canonical Rule

Represent the repository root owner as `.github/instructions/ownership/repository/`.

The folder name `repository/` is literal. Do not replace it with the repository's actual checkout name.

Represent every narrower owned boundary as a child node folder under that root owner.

That rule applies whether the owned boundary in the repository is:

- a directory such as `src/api/`
- a file such as `src/api/orders.ts`

The folder is the node.

The instruction files inside the folder describe the guidance that belongs to that node.

## Canonical Grammar

Use these rules:

1. `repository/` is the explicit repository root owner.
2. Repository directories stay directories below `repository/` in the instruction tree.
3. Repository files may also become folder nodes, named after the file.
4. Instruction files inside a node folder are named by concern or purpose, not by the path again.
5. Child folders represent narrower ownership boundaries.

Minimal canonical example:

```text
.github/
  instructions/
    ownership/
      repository/
        general.instructions.md
        src/
          general.instructions.md
          api/
            general.instructions.md
            orders.ts/
              contract.instructions.md
              framework.instructions.md
```

## Repository Root Owner

Use `ownership/repository/` when the guidance belongs to the repository root boundary.

This is useful for repo-owned contracts that apply from the root down, but that would make the baseline too large or too procedural.

Examples:

- `ownership/repository/general.instructions.md`
- `ownership/repository/supporting-sources.instructions.md`
- `ownership/repository/repository-structure.instructions.md`

The `repository/` node is explicit on purpose.

It prevents `ownership/` itself from becoming an ambiguous bucket for every global rule.

It also avoids coupling the instruction tree to a local clone name, fork name, or future repository rename.

It also keeps narrower owners inside the same tree: a real top-level `src/` path becomes `ownership/repository/src/`, not a sibling of the repository root owner.

Keep the baseline short and use the root owner for repo-owned guidance that still deserves an instruction file.

Do not use the root owner as a second baseline, a source registry for every document, or a place to hide cross-cutting overlays.

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

- `ownership/repository/src/api/orders.ts.instructions.md`

instead of:

- `ownership/repository/src/api/orders.ts/<concern>.instructions.md`

Use this shortcut only for a repository-file boundary that needs exactly one instruction and where the shorter tree improves readability.

Prefer the canonical folder form when the file node may grow, when teachability and uniformity matter more than brevity, or when a second representation in the same area would make the map harder to read.

## Naming Guidance

Name instruction files by concern or purpose.

Good examples:

- `general.instructions.md`
- `contract.instructions.md`
- `framework.instructions.md`
- `authorization.instructions.md`
- `diagnostics.instructions.md`

Because names such as `general.instructions.md` may repeat across the tree, rely on the node path plus filename as the canonical identity. Keep `.instructions.md` frontmatter minimal and portable; treat any extra UI metadata as surface-specific and optional.

## When To Add A Narrower Node

Grow the tree incrementally.

Do not mirror the whole repository structure up front.

Add a narrower node when:

- the broader owner no longer gives guidance that is honest enough for that subtree
- the subtree has stable local behavior, constraints, or terminology that deserve their own guidance
- the narrower node reduces ambiguity rather than merely increasing detail

Do not add a narrower node only because:

- the repository has another folder there
- you might need a rule there someday
- you want every path to have its own instruction
- you are trying to encode follow-through enumeration locally instead of reusing a broader rule

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

It is also optional.

If a node has no distinct downstream rule worth stating, omit the trigger section instead of copying generic follow-through prose downward.

This convention changes how the tree is laid out on disk.

It does not create a new structural layer.

## Related Material

- [Operating Model](../model/operating-model.md)
- [Follow-Through Triggers](../model/follow-through-triggers.md)
- [Decision Rules](./decision-rules.md)
- [Examples](../examples/README.md)
- [Repository Archetypes](../examples/repositories/README.md)
