# Operating Model

Audience: maintainers who need the conceptual map of the architecture before writing rules or applying it to a repository.  
Goal: define the structural parts of the model clearly, without mixing in disk-layout conventions or rollout steps.

## On This Page

- [The Operating Formula](#the-operating-formula)
- [What The Architecture Standardizes](#what-the-architecture-standardizes)
- [The Structural Parts](#the-structural-parts)
- [How Follow-Through Fits](#how-follow-through-fits)
- [How Supporting Sources Fit](#how-supporting-sources-fit)
- [Runtime Behavior In Practice](#runtime-behavior-in-practice)
- [Relationship Map](#relationship-map)
- [Official References](#official-references)
- [Related Docs](#related-docs)

## The Operating Formula

Use this formula:

- `baseline + ownership tree + cross-cutting overlays`

That formula describes the structural part of the architecture.

`Follow-Through Triggers` is not another structural layer.

It is a behavioral section that may live inside baseline, ownership, or overlay instructions.

Supporting sources are also not another structural layer.

They are auxiliary evidence that can help an agent locate and handle deeper, live, private, or conflicting sources when those sources could change the decision.

## What The Architecture Standardizes

The architecture standardizes:

- the structural roles in the instruction map
- the path-first routing backbone
- the distinction between ownership and cross-cutting concerns
- where downstream follow-through behavior belongs

It does not standardize the internal prose format of each instruction.

The headings, writing style, and exact Markdown organization inside an instruction still belong to the adopting repository or team.

It also does not standardize one universal closure policy for every repository.

Repositories may choose different follow-through styles as long as they stay structurally clear about where policy, triggers, skills, automation, and any optional explicit carry-forward surface belong.

## The Structural Parts

### Baseline

The baseline is the short repository-wide operating layer.

It should hold only guidance that is:

- broadly valid across the repository
- short enough to remain readable
- unlikely to change often
- useful no matter which ownership path is active

### Ownership Tree

The ownership tree is the path-based map of stable responsibility boundaries.

It answers:

- which part of the system owns this path
- where local behavioral guidance should live
- where narrower path-based refinement is legitimate

### Cross-Cutting Overlays

An overlay adds one extra concern across multiple ownership areas.

It exists for concerns that:

- span several owners
- still benefit from consistent guidance
- are not themselves stable architectural owners

### Skills

Skills are reusable workflows.

Use them for task-shaped guidance that is deeper than always-on instructions and should only be pulled in when relevant.

Keep the skill set small and outcome-based.

Different follow-through cases should often reuse the same few skills, such as `impact-review`, change review, or debugging, rather than creating one skill per trigger.

### Follow-Through Triggers

`Follow-Through Triggers` captures what other downstream surfaces may now need attention after a meaningful change.

It is not another file type.

It is the downstream consequence layer that sits inside the structural parts above.

The trigger condition should be anchored in the instruction that can observe the originating change.

A trigger may surface work that later uses a generic skill, but the trigger itself is not a skill-dispatch layer.

Exact repeatable procedures belong better in scripts, CI, or runbooks than in general trigger prose.

## How Follow-Through Fits

Healthy follow-through usually needs more than triggers alone.

In practice, repositories often need to compose:

- repository closure policy
- origin-anchored follow-through triggers
- supporting sources
- reusable skills
- automation and validation
- when needed, an explicit carry-forward surface for meaningful deferred follow-through

That still is not another structural layer.

It is simply the practical way repositories combine the existing parts above.

Repositories often keep local guidance, `Follow-Through Triggers`, closure policy, and reusable workflow distinct.
Treat that as a classification heuristic, not as another structural layer and not as a required heading template.
Use [Decision Rules](../rules/decision-rules.md) for the canonical version of that heuristic.

The repository-wide policy usually belongs in the baseline.
Triggers stay anchored at the originating change in baseline, ownership, or overlays.
Agent-facing supporting-source policy normally belongs in a small source instruction owned by the repository root.
A non-instruction source surface is healthy only when active guidance points to it and explains how it should be used.
Reusable task flow belongs in skills.
Exact repeatable checks belong in automation.
When a repository intentionally carries meaningful work forward, it is often healthier to preserve it in an explicit surface rather than in agent memory alone.
That is optional, and it does not require a dedicated task tracker.

Use [Follow-Through Triggers](./follow-through-triggers.md) for trigger design, [Supporting Sources](./supporting-sources.md) for source guidance, [Decision Rules](../rules/decision-rules.md) for placement questions, and [Replication Playbook](../replication-playbook.md) when rolling this out in a real repository.

## How Supporting Sources Fit

Some repositories need deeper or more current evidence than always-on instructions should carry.

Supporting sources handle that depth.

They can be local or external, public or private, static or live. What matters is whether they provide evidence that could change the decision.

Instructions still carry the compact active contract.

Supporting-source guidance tells the agent where relevant evidence lives, how to access it, what kind of claim it can answer, how fresh it must be, what to do if it is unavailable, and how to handle conflict.

The source format is intentionally flexible, but the reliability of each surface is not the same. A repository may use `.github/instructions/ownership/repository/supporting-sources.instructions.md` for agent-facing source policy, or another maintained source surface when active guidance explicitly points to it.

Some sources may need deeper source-specific interpretation guidance.

Treat that as an exception, not the default.

Because current path-specific instructions are routed by file paths, repo-wide source-specific interpretation instructions usually need `applyTo: "**"` and therefore stay effectively always on in surfaces that support them.

Use a separate repository-root instruction only when the source's interpretation policy is important enough to justify that always-on context. Use an explicit procedural workflow surface for procedural source operations.

What matters is that source use stays auxiliary:

- a consumer instruction names a source only when it could change the decision
- conflict handling is visible where source entries are defined
- source-specific interpretation instructions are added only when lighter source guidance is not enough
- sources do not become another ownership tree or a giant document registry
- skills are used only when source lookup or reconciliation becomes a repeatable workflow

Use [Supporting Sources](./supporting-sources.md) for the canonical guidance.

## Runtime Behavior In Practice

The architecture is path-first on disk, but its value shows up at runtime as the agent's scope expands.

In practical terms:

1. repository-wide instructions provide the broad default context
2. when the current task touches a matching path, path-specific instructions for that path are also in play
3. if the work expands into new paths, newly relevant path-specific instructions may become relevant as well
4. if the type of work changes, the agent may choose a skill just-in-time
5. if the task needs deeper or live evidence, the agent may use supporting-source guidance to locate and handle it
6. if an exact repeatable check exists, the agent may use scripts, CI, or runbooks instead of relying on prose alone

This is why the architecture keeps local context in ownership instructions and keeps skills outcome-based:

- path changes bring in new local context
- workflow changes may bring in a new skill
- downstream consequences may reveal more surfaces without requiring a new architectural layer
- supporting sources may bring in deeper evidence without bloating always-on instructions

That runtime model matches GitHub's documented behavior:

- repository-wide and path-specific custom instructions are used together when the path matches
- custom instructions are automatically added to requests and become available as soon as the file is saved
- skills are chosen based on the prompt and the skill description
- when a skill is chosen, its `SKILL.md` is injected into context and resources in the skill directory can be used alongside it
- MCP servers can provide access to external systems, but access does not replace source authority and conflict guidance

Different Copilot surfaces support different instruction types, so repository documentation should explain the model as a reusable mental map rather than as a fully deterministic execution engine.

## Relationship Map

Think of the model like this:

- `baseline`
  - broad repository defaults
- `ownership tree`
  - path-owned local behavior
- `cross-cutting overlays`
  - one extra lens across several owners
- `skills`
  - reusable workflows that should not always be loaded
- `Follow-Through Triggers`
  - downstream follow-through consequences
- `supporting sources`
  - optional auxiliary evidence, normally governed by a repository-root source instruction or explicitly reached through another maintained source surface named by active guidance

The architecture stays scalable because each part has a narrow job.
Repositories then compose closure policy, triggers, supporting sources, skills, automation, and tracking around those parts instead of inventing a new layer.

## Official References

- GitHub Docs, Adding repository custom instructions for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- GitHub Docs, Adding custom instructions for GitHub Copilot CLI  
  <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions>
- GitHub Docs, Adding agent skills for GitHub Copilot
  <https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills>
- GitHub Docs, Comparing GitHub Copilot CLI customization features  
  <https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/copilot-cli/comparing-cli-features>
- GitHub Docs, Copilot customization cheat sheet
  <https://docs.github.com/en/copilot/reference/customization-cheat-sheet>
- GitHub Docs, About Model Context Protocol
  <https://docs.github.com/en/copilot/concepts/context/mcp>
- GitHub Docs, Support for different types of custom instructions  
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>

## Related Docs

- [Ownership vs Overlay](./ownership-vs-overlay.md)
- [Follow-Through Triggers](./follow-through-triggers.md)
- [Supporting Sources](./supporting-sources.md)
- [Decision Rules](../rules/decision-rules.md)
- [Replication Playbook](../replication-playbook.md)
- [Ownership Tree Grammar](../rules/ownership-tree-grammar.md)
