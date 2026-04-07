# Replication Playbook

Audience: maintainers designing this architecture for other repositories.
Goal: provide a concise method for building and maintaining the structure without overfitting it to one codebase.

## Principle

Replicate the model, not the filenames.

Replicate the `Ownership-Driven AI Customization Architecture`, not one repository's exact file names.

The stable part is the structure:

- baseline,
- ownership tree,
- cross-cutting overlays,
- skills,
- hygiene checks.

The variable part is the ownership map of the target repository.

## Do Not Overstandardize Instruction Writing

Standardize the architecture, not the internal prose format of each instruction.

The architecture should standardize:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `Follow-Through Triggers`
- the decision boundary for when to use skills

The internal writing format of instructions is owned by the adopting repository or team and is outside the scope of this architecture.

## Teaching Principle

When you teach or document this model, move from concrete to abstract:

1. show one file path,
2. show which instructions apply,
3. explain why each one applies,
4. only then introduce general rules.

This is easier to understand than starting with taxonomy alone.

## Recommended Build Order

1. Define the repository-wide baseline.
2. Identify the largest stable ownership boundaries.
3. Add only the ownership-tree instructions that match those boundaries.
4. Add the cross-cutting overlays that truly span multiple ownership areas.
5. Add a small set of reusable skills.
6. Add checks that prevent drift, dead layers, and legacy structures.

## How To Identify Ownership Tree Nodes

Start from stable responsibility boundaries in the path structure, not from abstract topics.

Good sources of ownership boundaries:

- architecture slices,
- deployment boundaries,
- contract boundaries,
- layer boundaries,
- subsystem boundaries.

Good examples:

- `src/**/*.ts`
- `src/api/**/*.ts`
- `src/api/orders/**/*.ts`
- `src/billing/invoices/**/*.ts`
- `docs/**/*.md`

Bad sources:

- vague quality themes,
- temporary tasks,
- one-off initiatives.

If a boundary changes how Copilot should think about the files in that path, it may deserve an ownership-tree instruction.

The tree should become more specific only when the narrower subtree really needs different guidance.

## How To Identify Cross-Cutting Overlays

A cross-cutting overlay is appropriate when:

1. the concern spans multiple ownership areas,
2. the concern still benefits from consistent guidance,
3. the concern is not itself a stable architectural owner.

Typical overlays:

- testing,
- documentation,
- configuration,
- observability,
- task tracking.

Non-example:

- `src/api/orders/**/*.ts` and `src/billing/invoices/**/*.ts`

If those paths are different because each subtree owns a different kind of logic, they belong in the ownership tree.

They are not overlays just because they are narrower than `src/**/*.ts`.

## How To Organize Overlay Files

Once overlays grow beyond a handful of files, avoid keeping them all in one flat directory.

Use subdirectories under `overlays/` that group overlays by concern family.

Good families:

- `quality/`
- `operability/`
- `consistency/`
- `workflow/`
- `tooling/`

Example:

```text
.github/instructions/
  overlays/
    quality/
      testing-quality.instructions.md
      language-quality.instructions.md
    operability/
      observability.instructions.md
      failure-diagnostics.instructions.md
    consistency/
      code-docs-consistency.instructions.md
```

Do not group overlays by the exact path combination they happen to touch.

Group them by the concern they represent.

## A Minimal Teaching Example

Start with a tiny structure:

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

Then explain it in this order:

1. `baseline`
   - applies everywhere
2. `src/**/*.ts`
   - broad code owner
3. `src/api/**/*.ts`
   - API owner
4. `src/api/orders/**/*.ts`
   - narrower owner for order endpoints
5. `src/**/*.ts, tests/**/*.ts`
   - testing-quality or language-quality overlay
6. `docs/**/*.md`
   - documentation owner, not an overlay

Finally add the downstream rule:

- if `create_order.ts` changes public behavior, a `Follow-Through Triggers` section may tell Copilot to review tests and docs

Important distinction:

- step 5 is about the extra quality lens that applies when those files are in scope
- the final downstream rule is about what else may need review after a meaningful change

## Decision Matrix

Put guidance in the baseline when it is:

- repository-wide,
- short,
- broadly useful,
- unlikely to change often.

Put guidance in an ownership-tree instruction when it is:

- tied to a stable path family,
- specific to that responsibility boundary,
- useful most of the time in that path.

Put guidance in a cross-cutting overlay when it is:

- relevant across multiple ownership areas,
- not owned by one architectural slice,
- still important enough to load automatically in matching paths.

Put guidance in a skill when it is:

- a reusable workflow,
- deeper than always-on policy,
- not naturally tied to one path.

Consider an agent only when:

- the team will use an explicit mode,
- the mode has a distinct role or tool boundary,
- a skill is not enough.

## Rule For Downstream Consequences

Do not create a new instruction file just because a change has downstream consequences.

Instead:

- add or refine a `Follow-Through Triggers` section in the existing baseline, ownership-tree, or cross-cutting instruction that already owns the concern.

## Parent And Child Guidance

Treat narrower ownership nodes as refinements of broader ones.

Good refinement:

- parent: "API handlers should stay thin and delegate business work"
- child: "inside `src/api/orders/**`, map HTTP input early and call order services directly"

Bad refinement:

- parent: "API handlers should stay thin and delegate business work"
- child: "inside `src/api/orders/**`, put validation, business rules, persistence, and retries directly in the handler"

The goal is not arbitrary override.

The goal is controlled specialization for a smaller path boundary.

## Anti-Bloat Checks

Review the structure whenever one of these happens:

- a rule appears in multiple instructions,
- an instruction no longer maps to a stable boundary,
- an instruction is mostly workflow and should be a skill,
- a new instruction is being proposed for a downstream consequence rather than an ownership boundary,
- maintainers can no longer predict which instructions apply to a given file.

## Healthy End State

The model is healthy when:

- maintainers can explain the ownership map clearly,
- the instruction set is small enough to reason about,
- downstream consequences are handled through `Follow-Through Triggers` sections instead of ad hoc duplication,
- the same structure can be reused in another repository with a different ownership map.
