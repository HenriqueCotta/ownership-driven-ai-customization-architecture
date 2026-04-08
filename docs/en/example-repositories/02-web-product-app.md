# Web Product App

## Repository Shape

```text
repo/
  src/
    app/
      routes/
        dashboard/
        settings/
      layout/
    features/
      checkout/
      search/
      notifications/
    design-system/
      components/
      tokens/
    state/
      auth/
      cart/
    lib/
      analytics/
      api-client/
  tests/
    e2e/
    integration/
    unit/
  docs/
    ux/
    product/
```

## Healthy Ownership Tree

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        app/
          general.instructions.md
          routes/
            general.instructions.md
        features/
          general.instructions.md
          checkout/
            behavior.instructions.md
          search/
            behavior.instructions.md
        design-system/
          general.instructions.md
          tokens/
            consistency.instructions.md
        state/
          general.instructions.md
          auth/
            security.instructions.md
        lib/
          analytics/
            instrumentation.instructions.md
      tests/
        general.instructions.md
      docs/
        general.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      consistency/
        code-docs-consistency.instructions.md
```

## Why This Is Well-Implemented

- app shell, features, design system, state, and shared libraries are separate ownership boundaries
- checkout and search are narrower feature owners because behavior differs in meaningful ways
- auth state is a narrower owner because it carries security-sensitive expectations
- code-docs consistency is an overlay because product and UX docs span many source owners

## Everyday Situations

### Updating Checkout Validation In `src/features/checkout/`

Likely instruction context:

- `src/general`
- `src/features/general`
- `src/features/checkout/behavior`
- testing-quality overlay
- code-docs-consistency overlay if user-facing messaging changes

Likely follow-through:

- unit and integration tests
- checkout docs or UX copy references
- analytics if conversion events change

### Changing Design Tokens In `src/design-system/tokens/`

Likely instruction context:

- `src/general`
- `src/design-system/general`
- `src/design-system/tokens/consistency`
- code-docs-consistency overlay if token docs exist

Likely follow-through:

- visual regression tests
- component docs
- product screenshots or reference specs

### Adjusting Auth State In `src/state/auth/`

Likely instruction context:

- `src/general`
- `src/state/general`
- `src/state/auth/security`
- testing-quality overlay

Likely follow-through:

- auth tests
- route guards
- session or login docs
- analytics if login funnel behavior changes

### Editing `docs/ux/search.md`

Likely instruction context:

- `docs/general`
- code-docs-consistency overlay if code and docs must stay aligned

Likely follow-through:

- verify the current feature behavior
- verify screenshots or examples
- verify tests still encode the described behavior

## Teaching Takeaway

This repository works well with the architecture because ownership follows product and engineering seams:

- app shell
- features
- design system
- state
- shared libraries

That keeps UI work, design-system work, and product-behavior work from collapsing into one giant frontend instruction.
