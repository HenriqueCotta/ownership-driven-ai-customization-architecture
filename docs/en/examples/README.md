# Examples

Audience: maintainers who want to learn the architecture through concrete scenarios instead of theory first.  
Goal: provide short, linkable examples that teach classification, follow-through, and ownership-tree layout without forcing readers through one long file.

## On This Page

- [How To Use This Folder](#how-to-use-this-folder)
- [Classification](#classification)
- [Follow-Through](#follow-through)
- [Ownership Tree](#ownership-tree)
- [Supporting Sources](#supporting-sources)
- [Repository Archetypes](#repository-archetypes)
- [Quick Review Checklist](#quick-review-checklist)

## How To Use This Folder

Read examples by theme:

- `classification/`
  - how to tell ownership apart from overlays
- `follow-through/`
  - how downstream follow-through logic should work
- `ownership-tree/`
  - how the ownership tree should look on disk
- `supporting-sources/`
  - how source guidance, consumer instructions, conflicts, and source workflows fit together
- `repositories/`
  - how the architecture looks in realistic repository archetypes and day-to-day prompts

If this is your first pass, read them in this order:

1. [One Path, One Owner](./classification/01-one-path-one-owner.md)
2. [A Real Overlay](./classification/02-a-real-overlay.md)
3. [Narrower Owner vs Overlay](./classification/03-narrower-owner-vs-overlay.md)
4. [Contract Change](./follow-through/01-contract-change.md)
5. [Configuration Change](./follow-through/02-configuration-change.md)
6. [Shared Trigger Beats Repeated Local Copies](./follow-through/06-shared-trigger-beats-repeated-local-copies.md)
7. [One File Node With Two Instruction Files](./ownership-tree/01-one-file-node-with-two-instruction-files.md)
8. [Grow The Tree Only When The Broad Owner Stops Being Enough](./ownership-tree/04-grow-the-tree-only-when-the-broad-owner-stops-being-enough.md)
9. [Repository-Root Supporting-Source Instruction](./supporting-sources/02-repository-root-supporting-source-instruction.md)
10. [Consumer Instructions](./supporting-sources/03-consumer-instructions.md)

## Classification

- [One Path, One Owner](./classification/01-one-path-one-owner.md)
- [A Real Overlay](./classification/02-a-real-overlay.md)
- [Narrower Owner vs Overlay](./classification/03-narrower-owner-vs-overlay.md)

## Follow-Through

- [Contract Change](./follow-through/01-contract-change.md)
- [Configuration Change](./follow-through/02-configuration-change.md)
- [Documentation As Its Own Owner](./follow-through/03-documentation-as-its-own-owner.md)
- [Board Or Task Follow-Through](./follow-through/04-board-or-task-follow-through.md)
- [No Follow-Through Needed](./follow-through/05-no-follow-through-needed.md)
- [Shared Trigger Beats Repeated Local Copies](./follow-through/06-shared-trigger-beats-repeated-local-copies.md)

## Ownership Tree

- [One File Node With Two Instruction Files](./ownership-tree/01-one-file-node-with-two-instruction-files.md)
- [Mixed Children Under One Parent](./ownership-tree/02-mixed-children-under-one-parent.md)
- [Why A Folder Grammar Is Easier To Teach](./ownership-tree/03-why-a-folder-grammar-is-easier-to-teach.md)
- [Grow The Tree Only When The Broad Owner Stops Being Enough](./ownership-tree/04-grow-the-tree-only-when-the-broad-owner-stops-being-enough.md)

## Supporting Sources

- [Supporting Source Examples Index](./supporting-sources/README.md)
- [One Local Source](./supporting-sources/01-one-local-source.md)
- [Repository-Root Supporting-Source Instruction](./supporting-sources/02-repository-root-supporting-source-instruction.md)
- [Consumer Instructions](./supporting-sources/03-consumer-instructions.md)
- [Multiple Sources And Conflicts](./supporting-sources/04-multiple-sources-and-conflicts.md)
- [Local Summary As Safety Guard](./supporting-sources/05-local-summary-as-safety-guard.md)
- [Source-Specific Interpretation Instruction](./supporting-sources/06-source-specific-interpretation-instruction.md)

## Repository Archetypes

- [Repository Archetypes Index](./repositories/README.md)
- [API Service](./repositories/01-api-service.md)
- [Web Product App](./repositories/02-web-product-app.md)
- [Product Monorepo](./repositories/03-product-monorepo.md)

## Quick Review Checklist

After a meaningful change, ask:

1. Which path is the primary owner of this file?
2. Which broader or narrower ownership-tree nodes also apply?
3. Is there a real cross-cutting concern here, or am I mislabeling ownership as an overlay?
4. Does an existing `Follow-Through Triggers` section describe what else may now be stale?
5. If not, should that guidance be added to an existing broader instruction rather than copied into many local ones?
6. Does this instruction even need a trigger, or am I adding one by reflex?
7. Is the downstream work small enough to do directly, or does it warrant an existing outcome-based skill?
8. Would any exact repeatable check be clearer as automation or a runbook?
9. If deeper or live evidence matters, is source location, access, fallback, and conflict handling clear?
10. Am I inventing a new hint layer, source registry, or one skill per trigger where the existing map is already enough?
11. Am I growing the tree deeper before the broader owner has actually proved insufficient?
