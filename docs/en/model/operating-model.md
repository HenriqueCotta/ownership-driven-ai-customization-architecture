# Operating Model

Audience: maintainers who need the conceptual map of the architecture before writing rules or applying it to a repository.  
Goal: define the structural parts of the model clearly, without mixing in disk-layout conventions or rollout steps.

## On This Page

- [The Operating Formula](#the-operating-formula)
- [What The Architecture Standardizes](#what-the-architecture-standardizes)
- [The Structural Parts](#the-structural-parts)
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

## What The Architecture Standardizes

The architecture standardizes:

- the structural roles in the instruction map
- the path-first routing backbone
- the distinction between ownership and cross-cutting concerns
- where downstream review and update behavior belongs

It does not standardize the internal prose format of each instruction.

The headings, writing style, and exact Markdown organization inside an instruction still belong to the adopting repository or team.

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

Different follow-through cases should often reuse the same few skills, such as change review, docs synchronization, or debugging, rather than creating one skill per trigger.

### Follow-Through Triggers

`Follow-Through Triggers` captures what else may now need review after a meaningful change.

It is not another file type.

It is the downstream consequence layer that sits inside the structural parts above.

The trigger condition should be anchored in the instruction that can observe the originating change.

A trigger may surface work that later uses a generic skill, but the trigger itself is not a skill-dispatch layer.

Exact repeatable procedures belong better in scripts, CI, or runbooks than in general trigger prose.

## Runtime Behavior In Practice

The architecture is path-first on disk, but its value shows up at runtime as the agent's scope expands.

In practical terms:

1. repository-wide instructions provide the broad default context
2. when the current task touches a matching path, path-specific instructions for that path are also in play
3. if the work expands into new paths, newly relevant path-specific instructions may become relevant as well
4. if the type of work changes, the agent may choose a skill just-in-time
5. if an exact repeatable check exists, the agent may use scripts, CI, or runbooks instead of relying on prose alone

This is why the architecture keeps local context in ownership instructions and keeps skills outcome-based:

- path changes bring in new local context
- workflow changes may bring in a new skill
- downstream consequences may reveal more surfaces without requiring a new architectural layer

That runtime model matches GitHub's documented behavior:

- repository-wide and path-specific custom instructions are used together when the path matches
- custom instructions are automatically added to requests and become available as soon as the file is saved
- skills are chosen based on the prompt and the skill description
- when a skill is chosen, its `SKILL.md` is injected into context and resources in the skill directory can be used alongside it

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
  - downstream review and update consequences

The architecture stays scalable because each part has a narrow job.

## Official References

- GitHub Docs, Adding repository custom instructions for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- GitHub Docs, Adding custom instructions for GitHub Copilot CLI  
  <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions>
- GitHub Docs, Creating agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills>
- GitHub Docs, Comparing GitHub Copilot CLI customization features  
  <https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/copilot-cli/comparing-cli-features>
- GitHub Docs, Support for different types of custom instructions  
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>

## Related Docs

- [Ownership vs Overlay](./ownership-vs-overlay.md)
- [Follow-Through Triggers](./follow-through-triggers.md)
- [Decision Rules](../rules/decision-rules.md)
- [Ownership Tree Grammar](../rules/ownership-tree-grammar.md)
