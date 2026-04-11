# Examples

Audience: maintainers who want to learn the architecture through concrete scenarios instead of theory first.  
Goal: provide short, linkable examples that teach classification, follow-through, and ownership-tree layout without forcing readers through one long file.

## On This Page

- [How To Use This Folder](#how-to-use-this-folder)
- [Classification](#classification)
- [Follow-Through](#follow-through)
- [Ownership Tree](#ownership-tree)
- [Repository Archetypes](#repository-archetypes)
- [Quick Review Checklist](#quick-review-checklist)

## How To Use This Folder

Read examples by theme:

- `classification/`
  - how to tell ownership apart from overlays
- `follow-through/`
  - how downstream review and update logic should work
- `ownership-tree/`
  - how the ownership tree should look on disk
- `repositories/`
  - how the architecture looks in realistic repository archetypes and day-to-day prompts

If this is your first pass, read them in this order:

1. [One Path, One Owner](./classification/01-one-path-one-owner.md)
2. [A Real Overlay](./classification/02-a-real-overlay.md)
3. [Narrower Owner vs Overlay](./classification/03-narrower-owner-vs-overlay.md)
4. [Contract Change](./follow-through/01-contract-change.md)
5. [Configuration Change](./follow-through/02-configuration-change.md)
6. [One File Node With Two Instruction Files](./ownership-tree/01-one-file-node-with-two-instruction-files.md)
7. [Mixed Children Under One Parent](./ownership-tree/02-mixed-children-under-one-parent.md)

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

## Ownership Tree

- [One File Node With Two Instruction Files](./ownership-tree/01-one-file-node-with-two-instruction-files.md)
- [Mixed Children Under One Parent](./ownership-tree/02-mixed-children-under-one-parent.md)
- [Why A Folder Grammar Is Easier To Teach](./ownership-tree/03-why-a-folder-grammar-is-easier-to-teach.md)

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
5. If not, should that guidance be added to an existing instruction rather than a new file?
6. Is the downstream work small enough to do directly, or does it warrant an existing outcome-based skill?
7. Would any exact repeatable check be clearer as automation or a runbook?
8. Am I inventing a new hint layer or one skill per trigger where the existing map is already enough?
