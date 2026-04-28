# Repository-Root Supporting-Source Instruction

## Situation

A repository uses several sources:

- local docs
- a private product workspace
- a work board
- a design system repository
- current provider documentation

The team wants one place that tells agents where these sources live and how to handle conflicts, but it does not want a rigid schema.

## Repository Shape

```text
<repository-root>/
  .github/
    copilot-instructions.md
    instructions/
      ownership/
        repository/
          supporting-sources.instructions.md
      overlays/
  docs/
  src/
```

The source instruction applies globally because source guidance can be useful from several owners.

It lives under `ownership/repository/` because the repository root owner owns the repo-wide source policy.

It is still auxiliary evidence, not another structural layer or a registry of every document.

## Baseline Pointer

```md
# Repository Baseline

Start from the narrowest relevant owner instruction and apply overlays only when their concern is affected.

When deeper or live evidence could change a decision, use `.github/instructions/ownership/repository/supporting-sources.instructions.md`.

Consult only the source entries that could affect the current claim. Do not list, open, or check every source just because the source instruction exists.
```

## Supporting Source Instruction

```md
---
applyTo: "**"
---

# Supporting Sources

These entries are not a required schema. They are stable source IDs the repository uses when "check the docs" would be too vague.

Use supporting sources only when they could change the decision, explain a conflict, or prevent unsafe guessing.

## Conflict Handling

When sources diverge, classify the disputed claim first: implementation behavior, product intent, external platform fact, policy, planned work, or design-system contract.

Prefer the source that owns that claim. If the owning source is unavailable and the missing fact could change the result, treat that part as verification-blocked.

Do not let external provider docs override repository product intent, policy constraints, or local security rules. Do not let local mirrors override current provider facts.

## repo-docs

Where: `docs/`
Use for: repository-owned architecture notes, rationale, and local examples.

## product-workspace

Where: product workspace `checkout-product-notes`
Access: product-docs MCP, if available.
Use for: checkout product intent and accepted product decisions.
If unavailable: preserve existing customer-visible behavior and surface missing product intent when it could change the result.

## work-board

Where: board `checkout-work`
Access: project-management MCP, if available.
Use for: planned work, accepted follow-ups, and explicit carry-forward.
Do not use for: current behavior unless linked to merged code or accepted docs.

## design-system

Where: `../design-system/` or `org/design-system`
Access: local checkout first; source-control MCP if needed.
Use for: shared UI component contracts, tokens, accessibility states, and visual interaction rules.
If unavailable: avoid inventing new component behavior; follow existing local UI patterns.

## payment-provider-docs

Where: `https://provider.example/docs`
Access: web or provider-docs MCP, if available.
Use for: provider-owned fields, limits, auth, idempotency, errors, and API behavior.
Freshness: verify current docs before changing provider-specific behavior.
If unavailable: do not introduce behavior that depends on unverified provider support.
If it conflicts: current provider docs own provider facts; local notes may be stale.
```

## Teaching Takeaway

The entries do not all use the same fields.

That is intentional.

The stable part is the source ID and the decision guidance. The Markdown format stays repository-owned.
