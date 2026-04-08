# Core Model

Audience: maintainers who need to understand how the architecture works before applying it to a repository.  
Goal: define the model clearly enough that someone can classify instructions, design routing, and place follow-through logic without guessing.

## The Operating Formula

Use this formula:

- `baseline + ownership tree + cross-cutting overlays`

That formula describes the structural part of the architecture.

`Follow-Through Triggers` is a behavioral section inside those instructions, not a separate structural layer.

## What The Architecture Does Not Standardize

The architecture standardizes:

- structural layers,
- routing logic,
- ownership versus overlay boundaries,
- where downstream consequences should live.

It does not define the internal writing format of an instruction.

The internal prose, headings, and Markdown structure of an instruction are owned by the adopting repository or team.

The only block that is architecturally special inside instructions is:

- `Follow-Through Triggers`

## The Structural Parts

### Baseline

The baseline is the short repository-wide operating layer.

It should hold only rules that are:

- broadly valid across the repository,
- short enough to stay readable,
- unlikely to change often,
- useful regardless of which ownership path is active.

Typical baseline content:

- engineering posture,
- default expectations for safe changes,
- short repository-wide follow-through reminders,
- concise guidance about how to report assumptions, validation, or risk.

### Ownership Tree

The ownership tree is the path-based structure of stable responsibility boundaries.

Think of it as a hierarchy of who owns what kind of logic:

- broad code owner,
- narrower subsystem owner,
- narrower feature owner,
- sometimes a still narrower sub-boundary if it truly needs different guidance.

Examples:

- `src/**/*.ts`
- `src/api/**/*.ts`
- `src/api/orders/**/*.ts`
- `src/billing/invoices/**/*.ts`
- `docs/**/*.md`

Use ownership when the path itself is the owner of a kind of logic.

### Canonical Node Layout

In this architecture, the canonical layout represents every owned boundary as a node folder under `.github/instructions/ownership/`.

Use this short rule:

- repository directories become node folders with the same path
- repository files also become node folders, such as `orders.ts/`
- instruction files inside a node folder are named by concern, such as `general`, `contract`, or `framework`
- child folders represent narrower ownership boundaries

Minimal example:

```text
.github/instructions/
  ownership/
    src/
      general.instructions.md
      api/
        general.instructions.md
        orders.ts/
          contract.instructions.md
```

This gives the model one visual grammar for directory owners and file owners.

Optional shortcut:

- a leaf file node with exactly one instruction may be written directly as `orders.ts.instructions.md`
- use that only when you want a shorter tree for a simple file owner
- switch to the folder form once that file owner needs several instruction files

For the full convention, naming guidance, and edge cases, read [Ownership Tree Convention](./ownership-tree-convention.md).

### Cross-Cutting Overlays

An overlay adds one extra lens across multiple owners.

Use an overlay when:

- the concern spans several ownership areas,
- the concern benefits from consistent guidance,
- the concern is not itself a stable architectural owner.

Examples of good overlay concerns:

- testing quality,
- language quality,
- observability,
- failure diagnostics,
- code-docs consistency.

Important:

- an overlay says how to think,
- it does not automatically say that another surface must now change.

### Skills

Skills are reusable workflows.

Use them for tasks that are deeper than always-on instructions, such as:

- debugging,
- review passes,
- implementation planning,
- docs synchronization,
- structured brainstorming.

## First-Contact Questions

If this is the first time you are classifying a repository path, ask these four questions:

1. What file or path is being changed?
2. Which part of the system owns that path?
3. Which extra concerns also apply there?
4. What else may now be stale because of this change?

Those questions map directly to:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `Follow-Through Triggers`

## Ownership vs Overlay

This is the most important distinction in the model.

Use ownership when the path is the owner of a kind of logic.

Use an overlay when the same concern needs to span several different owners.

Short version:

- `overlay` = extra lens
- `follow-through` = downstream consequence

Examples:

- `src/api/orders/**/*.ts`
  - ownership node
  - that subtree owns order API logic
- `src/billing/invoices/**/*.ts`
  - ownership node
  - that subtree owns invoice logic
- `src/**/*.ts, tests/**/*.ts, scripts/**/*.ts`
  - good overlay candidate for language or testing quality
  - the concern spans several owners
- `src/api/**/*.ts, src/billing/**/*.ts`
  - good overlay candidate for observability
  - the concern spans several owners

Rule of thumb:

- if the cut exists because those files are responsible for a type of logic, use ownership
- if the cut exists because one extra concern spans multiple owners, use an overlay

`docs/**/*.md` is usually its own ownership node, not an overlay.

The link between code and docs usually comes from follow-through, not from turning docs into an overlay.

## Where Follow-Through Belongs

`Follow-Through Triggers` should live inside the instruction that best understands the origin of the change.

Default placement:

- baseline
  - for short repository-wide downstream rules
- ownership node
  - when the source-side owner best understands the blast radius
- overlay
  - only when the downstream rule is truly owned by that cross-cutting concern

In other words:

- the internal writing format of the rest of the file is out of scope for the architecture
- downstream consequences should still be easy to find and should not be duplicated arbitrarily across the tree

Examples:

- contract changed
  - follow-through usually belongs in the contract owner
- config defaults changed
  - follow-through usually belongs in the config owner
- public behavior changed in `src/**`
  - follow-through usually belongs in the relevant source-side owner or in the baseline
- testing-quality overlay
  - helps shape how tests are written
  - does not, by itself, own the generic rule "if `src/**` changes, review tests"

## A Simple Routing Example

Imagine this repository shape:

```text
repo/
  src/
    api/
      orders/
        create_order.ts
    billing/
      invoices/
        issue_invoice.ts
  tests/
    api/
      orders/
        create_order.test.ts
  docs/
    orders.md
```

If Copilot is editing `src/api/orders/create_order.ts`, a healthy structure usually looks like this:

- baseline
- ownership-tree nodes such as:
  - `src/**/*.ts`
  - `src/api/**/*.ts`
  - `src/api/orders/**/*.ts`
- cross-cutting overlays such as:
  - a testing-quality overlay
  - an observability overlay for operational code paths

Examples of what those overlays may mean:

- testing-quality overlay
  - prefer behavior-focused tests
  - keep fixtures small
  - keep test names explicit
- observability overlay
  - log meaningful operational events
  - keep error signals diagnosable
  - preserve useful telemetry context

Then, if the change affects public behavior, contract semantics, config, or operational expectations, a `Follow-Through Triggers` section in the best-matching owner may tell Copilot to inspect tests, docs, implementations, or configs.
