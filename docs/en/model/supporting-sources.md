# Supporting Sources

Audience: maintainers whose repositories sometimes need local docs, external docs, private systems, or other evidence outside active instructions.  
Goal: define the smallest useful way to make those sources locatable, governable, and safe to use without turning them into another ODA layer.

## On This Page

- [Core Rule](#core-rule)
- [Where Source Guidance Lives](#where-source-guidance-lives)
- [Source Entries Are Flexible](#source-entries-are-flexible)
- [How Consumer Instructions Refer To Sources](#how-consumer-instructions-refer-to-sources)
- [When A Source Needs Its Own Instruction](#when-a-source-needs-its-own-instruction)
- [When One Source Is Enough](#when-one-source-is-enough)
- [When Several Sources Are Needed](#when-several-sources-are-needed)
- [Duplicating Source Knowledge Safely](#duplicating-source-knowledge-safely)
- [Conflict Handling](#conflict-handling)
- [Relationship To Triggers, Skills, And MCP](#relationship-to-triggers-skills-and-mcp)
- [Common Mistakes](#common-mistakes)
- [Official References](#official-references)
- [Related Docs](#related-docs)

## Core Rule

Supporting sources are optional auxiliary evidence.

They are not a fourth structural layer in the ODA formula.

The structural formula stays:

- `baseline + ownership tree + cross-cutting overlays`

Instructions carry the active contract.

Supporting sources explain where deeper or live evidence lives, how to access it, what kind of claim it can answer, and what to do when access or source agreement fails.

Use supporting sources only when vague guidance such as "check the docs" would be too weak.

## Where Source Guidance Lives

ODA does not require one filename.

### Preferred Pattern

The most common repository-local pattern is a supporting-source instruction owned by the repository root:

```text
.github/
  copilot-instructions.md
  instructions/
    ownership/
      repository/
        supporting-sources.instructions.md
```

```md
---
applyTo: "**"
---

# Supporting Sources

Use these sources only when they could change the decision.
```

Keep the baseline small. It can point to the source instruction with one short rule:

```md
When deeper or live evidence could change a decision, use the repository supporting-source instructions.
```

### Repository Root Owner

Use `ownership/repository/` when source guidance belongs to the repository root owner.

Put it there when it is part of the root owner's contract: the repo-wide map of deeper evidence, source authority, fallback, and conflict handling.

This is a real root node. Other top-level repository owners, such as `docs/` or `src/`, sit under `ownership/repository/`, not beside it.

The folder name `repository/` is a literal convention, not the repository's real name.

Do not use `ownership/` itself as a bucket for every global rule.

Source guidance is still auxiliary evidence.

It should not become a second baseline, a source registry for every document, or another ownership tree.

### Other Surfaces

For agent-facing source policy, prefer a Copilot instruction.

Other surfaces can hold source information, but they do not have the same loading guarantee by themselves.

They are healthy only when active guidance explicitly points to them and explains when to consult them.

The exact surface is less important than making the source reachable without pretending it is automatically loaded.

Avoid putting a standalone `.github/sources.md` in the repository as if Copilot would load it automatically.

A non-instruction source note can still be useful, but it is lower assurance unless a loaded instruction or workflow makes the agent consult it.

Choose the lightest place that makes the source easy to find and hard to misuse, and be honest about how reliably that place enters context.

## Source Entries Are Flexible

A source entry is not a required schema.

It can be one line, a compact card, a table row, or a richer note.

Prefer a stable source ID so consumer instructions can point to it clearly:

```md
## product-docs

Where: `docs/product/`
Use for: product intent and user-facing semantics.
```

Consumer instructions should reference the ID:

```md
Use supporting source `product-docs`.
```

Use only the fields that matter for the source.

Useful fields often include:

- where the source lives
- how it can be accessed
- what kind of claim it can answer
- whether current verification matters
- what to do if access fails
- how to handle conflict with code, docs, tests, instructions, or user intent

Do not require every source entry to carry every field.

The goal is enough guidance for the repository's risk level, not a form to fill out.

## How Consumer Instructions Refer To Sources

Consumer instructions should keep the active local contract visible.

They should refer to a supporting source only when source evidence could change the decision.

Good:

```md
# Payment Provider Adapter

Keep provider-specific behavior isolated in this adapter.

Before changing provider-owned fields, auth behavior, idempotency, rate limits, or error semantics, use supporting source `payment-provider-docs`.

If provider docs are unavailable, do not introduce behavior that depends on unverified provider support.
```

Risky:

```md
Follow the current provider docs.
```

The risky version hides the local contract behind a vague pointer.

The healthy version says what belongs in the adapter and uses the source only for provider-owned facts.

## When A Source Needs Its Own Instruction

Avoid source-specific interpretation instructions by default.

Most sources should stay as compact entries in the repository supporting-source instruction.

That keeps the source map easy to scan and avoids keeping source-specific detail in context for every task.

Create a separate source-specific interpretation instruction only when the guidance is repo-owned interpretation policy, lighter source guidance would not carry it safely, and keeping it in the central source instruction would make the source map harder to scan.

If the guidance is mainly procedural, keep it out of always-on instructions and point to the workflow surface that owns the procedure.

Place repo-wide source-specific interpretation under the repository root owner:

```text
.github/
  instructions/
    ownership/
      repository/
        supporting-sources.instructions.md
        work-board.instructions.md
```

Be careful with `applyTo: "**"`.

Current Copilot custom instructions are routed primarily by repository and path. If source-specific interpretation can apply anywhere, `applyTo: "**"` may be the only portable instruction shape, but it also means that guidance is effectively always on in surfaces that support path-specific instructions.

Use that cost deliberately.

Prefer lighter active source guidance when that is enough.

Good source-specific interpretation instruction:

```md
---
applyTo: "**"
---

# Work Board Interpretation

Use this instruction only when the task involves planned work, deferred follow-through, issue status, release coordination, or board-backed decisions.

The board owns planning state and explicit carry-forward. It does not prove current implementation behavior unless linked to merged code, tests, or accepted docs.

Do not create, move, close, or rewrite board items unless the user asks for board changes or the repository closure policy requires explicit carry-forward.
```

The matching source entry can stay compact:

```md
## work-board

Where: board `checkout-work`
Access: project-management MCP, if available.
Use for: planned work, accepted follow-ups, and explicit carry-forward.
Details: use `ownership/repository/work-board.instructions.md` only when board interpretation could change the decision.
```

If the source requires exact operations, use an explicit procedural workflow surface instead of stretching an always-on instruction.

## When One Source Is Enough

Some repositories only need one local source.

That can stay simple:

```md
## product-docs

Where: `docs/product/`
Use for: user-facing behavior and product wording.
If unavailable: preserve existing behavior and surface the missing product context when it could change the result.
```

An owner can consume it directly:

```md
If a change alters customer-visible behavior, use supporting source `product-docs` before treating the change as complete.
```

No extra source workflow is needed when the source is local and obvious.

## When Several Sources Are Needed

More complex changes may need several sources because different claims have different owners.

```md
Before changing invoice tax behavior, use supporting source `finance-policy` for compliance constraints and `product-docs` for customer-facing semantics.

Use supporting source `payment-provider-docs` only for provider-owned fields, limits, and API behavior.
```

This is not enumeration for its own sake.

It prevents one source from becoming the whole truth for claims it does not own.

## Duplicating Source Knowledge Safely

Sometimes a small local summary should appear in an owner instruction even when the authoritative source lives elsewhere.

This is useful when losing access to the source could lead the agent to relax an important invariant.

Good:

```md
Invoices must remain tax-inclusive at display boundaries.

Local safety summary: existing invoice displays are tax-inclusive. If supporting source `finance-policy` is unavailable, this summary may preserve current behavior, but it must not justify a new tax rule.
```

Risky:

```md
Tax is 17.5%. Discounts use rule ABC. Regional exceptions are listed below...
```

Do not copy long, volatile, or policy-owned details into local instructions.

A local summary should act as a guardrail against unsafe change, not as a stale mirror of the authoritative source.

## Conflict Handling

Put the general conflict rule where the source entries live.

Then add per-source conflict notes only when a source needs a local override.

Example:

```md
## Conflict Handling

When sources diverge, classify the disputed claim first: implementation behavior, product intent, external platform fact, policy, planned work, or design-system contract.

Prefer the source that owns that claim. If the owning source is unavailable and the missing fact could change the result, treat that part as verification-blocked.

Do not let external provider docs override repository product intent, policy constraints, or local security rules. Do not let local mirrors override current provider facts.
```

Source-specific conflict notes can refine that:

```md
## payment-provider-docs

Where: `https://provider.example/docs`
Use for: provider-owned fields, limits, auth, errors, and API behavior.
If it conflicts: current provider docs own provider facts; local notes may be stale.
```

## Relationship To Triggers, Skills, And MCP

A source consultation belongs in the consumer instruction when the source is needed to make the current change correct.

A `Follow-Through Triggers` section is the right place when a change may leave another surface stale.

A supporting-source entry is the right place for location, access, authority, freshness, fallback, and conflict guidance.

A skill is the right place when source lookup or reconciliation becomes a repeatable workflow.

An MCP server is an access mechanism.

It can let the agent reach external systems. It does not decide which source owns which claim. The source instruction still needs to say what the source can answer and what to do when access or agreement fails.

## Common Mistakes

Treat these as modeling mistakes:

- adding a bare link and assuming the agent will load or trust it correctly
- creating a giant registry of every document in the repository
- creating one source entry per topic when one broader source family is enough
- hiding the active contract entirely in a source
- requiring a private source without access expectations or fallback
- letting one source override claims it does not own
- using a local summary as if it were the current authoritative source
- creating a source-specific always-on instruction when lighter source guidance would be enough
- turning source guidance into another ownership tree

## Official References

- GitHub Docs, Adding repository custom instructions for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- GitHub Docs, Adding agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills>
- GitHub Docs, Copilot customization cheat sheet
  <https://docs.github.com/en/copilot/reference/customization-cheat-sheet>
- GitHub Docs, About Model Context Protocol
  <https://docs.github.com/en/copilot/concepts/context/mcp>
- GitHub Docs, Support for different types of custom instructions  
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>

## Related Docs

- [Operating Model](./operating-model.md)
- [Decision Rules](../rules/decision-rules.md)
- [Follow-Through Triggers](./follow-through-triggers.md)
- [Instruction Conflicts And Precedence](../rules/instruction-conflicts-and-precedence.md)
- [Supporting Source Examples](../examples/supporting-sources/README.md)
