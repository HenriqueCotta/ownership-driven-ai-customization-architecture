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

## A Realistic Ownership Map

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        features/
          checkout/
            behavior.instructions.md
        design-system/
          tokens/
            consistency.instructions.md
        state/
          auth/
            security.instructions.md
      docs/
        ux/
          general.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      consistency/
        code-docs-consistency.instructions.md
```

## Why This Map Is Realistic

- `src/general` holds broad frontend expectations
- `features/checkout/` gets a local node because checkout behavior is usually business-critical and user-visible
- `design-system/tokens/` gets a local node because token changes have large consistency blast radius
- `state/auth/` gets a local node because auth state often carries security-sensitive expectations
- `docs/ux/` is explicit because UX-facing documentation is a real owned surface

What is intentionally not mapped:

- `features/search/` and `features/notifications/` stay under broad `src/general`
- `app/routes/` does not get a local owner unless the routing shell has special rules
- `tests/` stays driven mainly by overlays and follow-through
- `lib/api-client/` and `state/cart/` stay under broader guidance until they prove they need narrower rules

That is usually more realistic than assigning instructions to every feature folder.

## Prompt-Driven Situations

### Update Checkout Validation In `src/features/checkout/`

Example prompt:

```text
Update checkout validation so gift cards cannot be combined with subscription purchases. Adjust tests, user messaging, and analytics if needed.
```

Likely instruction context:

- `src/general`
- `src/features/checkout/behavior`
- testing-quality overlay
- code-docs-consistency overlay if user-facing copy or docs change

How the architecture shapes the process:

1. The checkout node keeps the model focused on behavioral and product rules.
2. The testing overlay pushes coverage updates instead of leaving them implied.
3. The docs-consistency overlay reminds Copilot that user-facing copy and support docs may need alignment.

Likely follow-through:

- unit and integration tests
- UX copy or product docs
- analytics events if the validation path changes funnel behavior

### Change Design Tokens In `src/design-system/tokens/`

Example prompt:

```text
Rename the old warning color token set to the new semantic alert tokens and update downstream references.
```

Likely instruction context:

- `src/general`
- `src/design-system/tokens/consistency`
- code-docs-consistency overlay

How the architecture shapes the process:

1. The tokens node frames the change as a consistency change, not just a rename.
2. The overlay keeps docs and code references moving together.
3. Follow-through catches screenshots, token docs, and test snapshots without requiring a node for every component.

Likely follow-through:

- token docs
- visual regression or snapshot tests
- component references that still use the old names

### Adjust Auth State In `src/state/auth/`

Example prompt:

```text
Persist MFA enrollment state across refresh, but keep the cache invalidation conservative. Update tests and any related docs.
```

Likely instruction context:

- `src/general`
- `src/state/auth/security`
- testing-quality overlay

How the architecture shapes the process:

1. The auth node pushes the model toward safety and session semantics.
2. The testing overlay pushes for state-transition coverage.
3. Follow-through catches route guards, login flows, and docs without turning them all into local nodes.

Likely follow-through:

- auth tests
- route guard behavior
- login or session docs
- analytics only if the user-visible flow changes materially

## Teaching Takeaway

This repository works well with the architecture because it avoids the trap of making every feature its own instruction owner:

- only high-value or high-risk paths get local nodes
- overlays stay small and purposeful
- most work still routes through a small number of broad owners
- follow-through handles secondary surfaces instead of inflating the tree
