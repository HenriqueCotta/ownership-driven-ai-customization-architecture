# Multiple Sources And Conflicts

## On This Page

- [Situation](#situation)
- [Supporting Source Excerpt](#supporting-source-excerpt)
- [Owner Instruction](#owner-instruction)
- [Optional Skill](#optional-skill)
- [Prompt-Driven Flow](#prompt-driven-flow)
- [Teaching Takeaway](#teaching-takeaway)

## Situation

A repository changes subscription billing behavior.

The change may involve product intent, finance policy, provider behavior, tests, docs, and planned follow-up work.

No single source owns all of those claims.

## Supporting Source Excerpt

```md
## Conflict Handling

When sources diverge, classify the disputed claim first: implementation behavior, product intent, external platform fact, policy, planned work, or design-system contract.

Prefer the source that owns that claim. If the owning source is unavailable and the missing fact could change the result, treat that part as verification-blocked.

## product-workspace

Where: product workspace `subscription-product-notes`
Access: product-docs MCP, if available.
Use for: subscription product intent and accepted product decisions.
If it conflicts: owns intended customer semantics; code/tests may reveal implementation drift.

## finance-policy

Where: policy workspace `billing-policy`
Access: policy-docs MCP, if available.
Use for: tax, invoice, refund, and compliance constraints.
Freshness: verify before changing invoice or refund behavior.
If unavailable: do not relax existing finance constraints; mark policy verification blocked.
If it conflicts: owns finance compliance constraints.

## payment-provider-docs

Where: `https://provider.example/docs`
Use for: provider-owned fields, limits, auth, errors, and API behavior.
Freshness: verify current docs before changing provider-specific behavior.
If it conflicts: current provider docs own provider facts; local mirrors may be stale.

## work-board

Where: board `subscription-work`
Use for: accepted follow-ups and explicit carry-forward.
Do not use for: current behavior unless linked to merged code or accepted docs.
```

## Owner Instruction

```md
---
applyTo: "src/subscriptions/**"
---

# Subscriptions

Subscription state changes must keep customer-visible entitlement, billing, and cancellation behavior consistent.

Before changing invoice, refund, or cancellation semantics, use supporting source `product-workspace` for product intent and `finance-policy` for policy constraints.

Use supporting source `payment-provider-docs` only for provider-owned fields, limits, and API behavior.

## Follow-Through Triggers

If subscription behavior changes, review product docs, subscription tests, customer-facing examples, and accepted carry-forward work in supporting source `work-board` when the current pass intentionally defers meaningful follow-through.
```

## Optional Skill

```md
---
name: source-reconciliation
description: Reconcile conflicting repository, product, provider, policy, work-board, and design-system sources. Use when a task requires comparing multiple sources or classifying source divergence.
---

Start by identifying the disputed claim type: implementation behavior, product intent, external platform fact, policy, planned work, or design-system contract.

Use the supporting-source instruction to locate only the sources that can own that claim.

Return: sources checked, conflict classification, chosen authority, blocked verification, and follow-through needed.
```

## Prompt-Driven Flow

Prompt:

```text
Change cancellation so customers keep access until the paid period ends, and update anything else that should move with it.
```

Likely flow:

1. The subscriptions owner provides the local contract.
2. Product intent comes from `product-workspace`.
3. Refund and invoice constraints come from `finance-policy`.
4. Provider behavior is checked only if provider-owned fields or API behavior change.
5. The trigger reveals docs, tests, examples, and accepted carry-forward work.
6. If sources disagree, the reconciliation skill becomes useful because the workflow is now broader than one lookup.

## Teaching Takeaway

Multiple sources are healthy when they prevent authority confusion.

They become unhealthy when the instruction forces the agent to enumerate every source before every change.
