# Consumer Instructions

## Situation

A repository has a repository-root supporting-source instruction.

Now owners and overlays need to consume those sources without restating the whole source map.

## Provider Adapter Owner

```md
---
applyTo: "src/adapters/payment-provider/**"
---

# Payment Provider Adapter

Keep provider-specific behavior isolated in this adapter.

Before changing provider-owned fields, auth behavior, idempotency, rate limits, or error semantics, use supporting source `payment-provider-docs`.

If provider docs are unavailable, do not introduce behavior that depends on unverified provider support.
```

This is local guidance, not follow-through.

The current change would be wrong if it invents unsupported provider behavior.

## UI Owner

```md
---
applyTo: "src/ui/**"
---

# UI Layer

Prefer existing local components and design tokens.

Use supporting source `design-system` when changing shared component behavior, accessibility states, token usage, or visual interaction patterns.

For ordinary local layout fixes, follow nearby code first. Do not consult the design system unless it could change the decision.
```

This shows depth-only source use.

The source is available, but it should be consulted only when it could affect the current claim.

## Public Contract Overlay

```md
---
applyTo: "src/**"
---

# Public Contract Overlay

If a change affects public API behavior, emitted events, customer-visible errors, or documented response semantics, review the relevant tests and docs before treating the change as complete.

Use supporting source `product-workspace` only for product intent, and `payment-provider-docs` only for provider-owned facts.

If the change reveals broader source divergence, use the repository's source reconciliation workflow instead of resolving it ad hoc.
```

This is a cross-cutting concern because public contract behavior may appear across several owners.

The overlay references sources by claim type, not because every public-contract change must consult every source.

## Teaching Takeaway

Consumer instructions should answer:

- what local contract applies here
- when source evidence could change the decision
- which source ID owns the relevant claim
- what fallback keeps the change safe

They should not copy the whole source entry.
