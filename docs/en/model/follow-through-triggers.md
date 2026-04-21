# Follow-Through Triggers

Audience: maintainers who need to model downstream follow-through behavior without inventing extra layers.
Goal: explain what `Follow-Through Triggers` is, why it exists, and where it should live.

## On This Page

- [What Follow-Through Triggers Is](#what-follow-through-triggers-is)
- [Why It Exists](#why-it-exists)
- [Where It Lives](#where-it-lives)
- [Triggers Are Optional](#triggers-are-optional)
- [Source-Anchored Triggers](#source-anchored-triggers)
- [Relationship To Skills And Automation](#relationship-to-skills-and-automation)
- [Relationship To Policy And Tracking](#relationship-to-policy-and-tracking)
- [How Follow-Through Expands Scope](#how-follow-through-expands-scope)
- [Typical Triggers](#typical-triggers)
- [What It Is Not](#what-it-is-not)
- [Official References](#official-references)
- [Related Docs](#related-docs)

## What Follow-Through Triggers Is

`Follow-Through Triggers` describes what other downstream surfaces may now need attention after a meaningful change.

It is a behavioral section inside an instruction.

It is not a separate file type and not another architectural layer.

## Why It Exists

Many important changes have secondary consequences:

- docs may now be stale
- tests may need updates
- configs may need reconciliation
- runbooks, dashboards, or workflows may need adjustment

The model makes those consequences explicit so they are not lost in prompt phrasing or hidden team memory.

## Where It Lives

`Follow-Through Triggers` should live inside the instruction that best understands the origin of the change.

Default placement:

- baseline
  - for short repository-wide downstream rules
- ownership node
  - when the source-side owner best understands the blast radius
- overlay
  - only when the downstream rule is truly owned by that cross-cutting concern

## Triggers Are Optional

An instruction does not need a `Follow-Through Triggers` section just because it exists.

Add one only when that instruction can say something distinct and useful about downstream follow-through from inside its own scope.

If a broader owner already says the downstream rule well enough, do not copy it into narrower children.

If several sibling nodes would carry almost the same trigger with only wording drift or small enumeration differences, move the shared rule upward and keep only truly local deltas below.

An instruction with no trigger is normal when it has no unique downstream consequence worth stating.

## Source-Anchored Triggers

The condition that fires a trigger should come from inside the instruction's own scope.

A follow-through rule may point to paths or surfaces outside the instruction's `applyTo`.

But if the trigger depends on changes that the instruction would not see on its own, the rule is misplaced.

Move it to the instruction scope that can actually observe the originating change.

That may mean moving it upward, sideways, or into a different source-side owner entirely.

For example:

- if a change in `X` should trigger follow-through in `Y`, the trigger belongs with the instruction that sees changes in `X`, not with the instruction for `Y`

Common destinations are:

- the baseline
  - when the originating change may happen anywhere in the repository
- another ownership node
  - when a different source-side owner is the one that actually observes the change
- a broader ownership node
  - when a wider source-side owner better understands the blast radius
- an overlay
  - only when that cross-cutting concern truly owns the downstream rule across matching paths

## Relationship To Skills And Automation

A trigger says what downstream surfaces may need attention, verification, reconciliation, or update.

It does not, by itself, define the workflow for reconciling them.

That distinction matters because many different triggers can reuse the same small set of skills.

For example:

- a contract trigger, a config trigger, and a public-behavior trigger may all reuse the same generic impact-review skill
- if the downstream work is small, no skill is needed; inspect the affected surfaces and update them directly
- if the downstream work requires an exact repeatable sequence, prefer scripts, CI checks, or runbooks over embedding that procedure in the trigger

Do not treat follow-through as a dispatch table from trigger types to matching skills.

If a team wants discoverability help, keep it as a small hint inside existing docs or instructions rather than introducing a separate hint layer.

## Relationship To Policy And Tracking

Triggers are only one part of healthy follow-through.

Repositories still need a way to answer:

- when downstream work should usually be reconciled now
- when it should become explicit follow-up instead
- whether meaningful deferred follow-through should live only in conversation memory or also in an explicit carry-forward surface

That is why healthy repositories often pair triggers with:

- a short repository closure policy in the baseline
- reusable skills for broader decision flow
- automation for exact repeatable checks
- when useful, task tracking or another explicit carry-forward surface

Not every repository needs a dedicated carry-forward mechanism.
But when meaningful follow-through is intentionally deferred, preserving it in an explicit surface outside conversation memory can improve continuity, recoverability, and long-running collaboration.
That surface can still evolve over time; the goal is continuity, not freezing the work.

Those are still not a new architectural layer.
They are the other repository surfaces that can keep follow-through explicit, governable, and recoverable in practice.

Use [Operating Model](./operating-model.md), [Decision Rules](../rules/decision-rules.md), and [Replication Playbook](../replication-playbook.md) together when you need to design that composition in a real repository.

## How Follow-Through Expands Scope

Follow-through often begins in one owner and ends up touching several others.

A typical flow looks like this:

1. the agent starts in the source-side owner where the change originated
2. the matching ownership instructions and overlays shape the first pass
3. a `Follow-Through Triggers` section points to downstream surfaces that may now be stale
4. when the agent opens those new surfaces, path-specific instructions for those paths may now become relevant too
5. if the work turns into a broader review, docs reconciliation, or debugging task, the agent may choose a generic skill just-in-time

This is why follow-through should stay lightweight:

- it expands scope
- it does not replace the ownership tree
- it does not need a one-to-one skill for each trigger

GitHub's documented model supports this reading:

- repository-wide and matching path-specific instructions can both apply
- skills are selected at task time based on the prompt and skill description
- when a skill is selected, its instructions are injected into the agent's context

In other words, follow-through can reveal newly relevant instructions and skills during the work, but it should not be modeled as a rigid dispatch chain.

## Typical Triggers

Typical examples:

- a public contract changes
  - review consumers, docs, and tests
- configuration defaults change
  - review rollout assumptions, docs, and runtime checks
- behavior changes in a public API area
  - review tests, docs, and error handling expectations

## What It Is Not

`Follow-Through Triggers` is not:

- a second ownership tree
- a reason to create new instruction files by itself
- a section that every instruction must contain
- a dispatch table from trigger categories to matching skills
- a procedural checklist for exact commands or file-by-file updates
- a separate architectural hint layer
- a replacement for CI, review, or testing

It is a structured reminder of likely downstream work.

## Official References

- GitHub Docs, Adding repository custom instructions for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- GitHub Docs, Adding custom instructions for GitHub Copilot CLI  
  <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions>
- GitHub Docs, Creating agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills>
- GitHub Docs, Using custom instructions to unlock the power of Copilot code review  
  <https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/use-custom-instructions>
- GitHub Docs, Support for different types of custom instructions  
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>

## Related Docs

- [Operating Model](./operating-model.md)
- [Ownership vs Overlay](./ownership-vs-overlay.md)
- [Decision Rules](../rules/decision-rules.md)
- [Replication Playbook](../replication-playbook.md)
- [Examples](../examples/README.md)
