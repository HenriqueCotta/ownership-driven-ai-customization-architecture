# One Local Source

## On This Page

- [Situation](#situation)
- [Repository Shape](#repository-shape)
- [Supporting Source Instruction](#supporting-source-instruction)
- [Consumer Instruction](#consumer-instruction)
- [Docs Owner Instruction](#docs-owner-instruction)
- [Common Questions](#common-questions)
- [Why This Is Enough](#why-this-is-enough)

## Situation

A small service keeps customer-facing product behavior notes in `docs/product/`.

The repository also has other docs under `docs/`, but those are not part of this source.

There are no private systems, no live provider docs, and no special access method.

The team wants agents to know when `docs/product/` should be used as evidence for product intent without making every task open the docs folder.

## Repository Shape

```text
<repository-root>/
  .github/
    copilot-instructions.md
    instructions/
      ownership/
        repository/
          supporting-sources.instructions.md
          docs/
            general.instructions.md
          src/
            notifications/
              general.instructions.md
  docs/
    product/
      notifications.md
    runbooks/
      deploy.md
  src/
    notifications/
```

The `docs/` owner and the `product-docs` source have different jobs.

The `docs/` owner explains how to edit documentation files.

The `product-docs` source tells other instructions when `docs/product/` is evidence for product intent.

## Supporting Source Instruction

```md
---
applyTo: "**"
---

# Supporting Sources

Use these sources only when they could change the decision.

Do not open docs by reflex.

## product-docs

Where: `docs/product/`
Scope: product behavior notes only; this does not mean every file under `docs/`.
Use for: customer-visible behavior, product wording, and product intent.
Do not use for: deployment runbooks, architecture notes, or current implementation behavior.
If unavailable: preserve existing behavior and surface the missing product context when it could change the result.
If it conflicts: product docs own intended customer semantics, but implementation and tests may reveal drift.
```

## Consumer Instruction

```md
---
applyTo: "src/notifications/**"
---

# Customer Notifications

Notification behavior should stay understandable from the customer's point of view.

If a change alters customer-visible wording, delivery timing, opt-out behavior, or customer-facing defaults, use supporting source `product-docs` before treating the change as complete.

Do not consult `product-docs` for internal refactors that preserve customer-visible behavior.
```

## Docs Owner Instruction

```md
---
applyTo: "docs/**"
---

# Documentation

Keep docs concise, current, and organized by reader need.

When editing `docs/product/`, preserve product intent and customer-facing semantics unless the task explicitly changes them.

This owner instruction governs how documentation files are edited. It does not make all docs a supporting source for code changes.
```

## Common Questions

### Is The Source `docs/` Or `docs/product/`?

In this example, the source is `docs/product/`.

That narrower source is intentional.

The repository may contain runbooks, architecture notes, onboarding docs, and release notes under `docs/`. Treating all of `docs/` as one source would make the agent guess which docs own product intent.

### Does A Docs Owner Instruction Conflict With A Docs Source?

No.

They answer different questions.

The `docs/` owner instruction is active when the agent edits documentation paths.

The `product-docs` source is consulted by another instruction when product evidence could change a decision.

### Why Not Just Say "Check The Docs"?

"Check the docs" is vague.

It does not say which docs matter, when to consult them, what claim they own, or what to do if they are missing or stale.

A small source entry gives the agent just enough structure without creating a large registry.

### When Should The Source Be Used?

Use `product-docs` when a change could alter what customers see, understand, receive, opt into, or opt out of.

Do not use it for internal cleanup, formatting, dependency updates, or tests that preserve customer-visible behavior.

### Is A Skill Needed?

No.

The source is local and the lookup is simple.

A skill would only become useful if source lookup turned into a repeatable workflow, such as comparing several product documents, reconciling stale docs, or preparing a structured product-impact report.

## Why This Is Enough

The source is local, narrow, and stable.

The source entry names the exact folder that owns the relevant claim.

The consumer instruction explains when the source matters.

The docs owner instruction remains free to govern documentation edits without becoming a source map.
