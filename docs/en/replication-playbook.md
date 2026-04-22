# Replication Playbook

Audience: maintainers reproducing this architecture in another repository.
Goal: provide a practical sequence for rolling the model out without copying accidental details or rebuilding duplication.

## Principle

Replicate the model, not the filenames.

The stable part is the structure:

- baseline
- ownership tree
- the ownership-tree disk grammar
- cross-cutting overlays
- skills
- hygiene checks that keep the map from drifting

The variable part is the ownership map of the target repository.

## Teaching Principle

Teach the model from concrete to abstract:

1. show one real path
2. show which instructions apply
3. explain why each one applies
4. only then introduce the general rule

This is easier to teach and easier to retain than starting with taxonomy alone.

## Recommended Build Order

1. Define the short repository-wide baseline.
2. State the repository's closure policy in the baseline, keeping it short and usually limited to one rule or a very small set of rules.
3. Identify the largest stable ownership boundaries.
4. Add only the ownership-tree instructions that match those boundaries.
5. Add true cross-cutting overlays.
6. Add a small set of reusable skills.
7. Add checks that prevent drift, dead layers, and legacy structures.

Use [Decision Rules](./rules/decision-rules.md) to classify guidance before you write it.

Use [Ownership Tree Grammar](./rules/ownership-tree-grammar.md) to decide how the ownership map should look on disk.

Use [Operating Model](./model/operating-model.md), [Follow-Through Triggers](./model/follow-through-triggers.md), and [Decision Rules](./rules/decision-rules.md) together to design how policy, triggers, skills, automation, and any optional explicit carry-forward surface should work together in the target repository.

## Use A Default Authoring Split

When you start writing instructions, use the default split from [Decision Rules](./rules/decision-rules.md) unless the repository has a reason to deviate.

In practice, that means keeping local guidance, `Follow-Through Triggers`, closure policy, and reusable workflow clearly separated without turning them into a new layer or a required heading template.

## Organize Overlays By Concern Family

Once overlays grow beyond a handful of files, avoid one flat directory.

Use subdirectories under `overlays/` that group overlays by concern family.

Good families:

- `quality/`
- `operability/`
- `consistency/`
- `workflow/`
- `tooling/`

Group overlays by the concern they represent, not by the exact path combination they happen to touch.

## Roll Out In Small Passes

Start narrow.

A healthy first pass is usually:

1. one short baseline
2. two or three broad ownership nodes
3. one or two true overlays
4. validation against real change scenarios
5. narrower nodes added only where the broad owner stops being enough

This keeps the map teachable while the team is still learning how the boundaries behave.

## Start Broad And Grow Only When Needed

ODA is meant to be adoptable in stages.

Do not try to finish the whole repository in one pass.

It is healthy to stop at a broader owner while it still gives guidance that is honest and useful.

Go deeper only when:

- a subtree clearly needs different local guidance
- a narrower node removes ambiguity that the broader node cannot
- the added detail produces real operational value instead of symmetry for its own sake

Trying to reach every leaf too early usually creates a large map with weak local value.

## Keep The Skill Set Small And Outcome-Based

Start with a few skills named by workflow outcome, not by triggering change or path.

Good examples:

- `impact-review`
- `review-change`
- `debug-behavior`

That usually scales better than creating variants such as `review-contract-change`, `review-config-change`, `review-api-drift`, or one docs-update skill per trigger.

Different follow-through triggers should usually reuse the same small skill set, with local context coming from the ownership tree and overlays.

Add a more specific skill only when the workflow itself materially differs in evidence, steps, or expected output.

## Do Not Write Triggers Everywhere

Not every instruction needs a `Follow-Through Triggers` section.

If a node has no distinct downstream rule worth stating, omit the section entirely.

If several sibling or nearby nodes would repeat almost the same trigger, move the shared part upward to the broader owner or baseline and keep only real local deltas below.

Local trigger enumeration is a common source of duplication, omission, and drift.

Prefer one honest shared rule over many slightly different copies.

## Recommended Maintenance Skill For Copilot Customization

If a repository actively maintains a non-trivial Copilot customization map, consider also carrying one repository-maintenance skill for the customization itself:

- [oda-copilot-customization](../../.github/skills/oda-copilot-customization/SKILL.md)

This is optional, but recommended when maintainers want a reusable workflow for:

- shaping or auditing the customization map itself
- checking the repository against upstream ODA rather than local memory or stale copies
- checking the current official GitHub Copilot guidance before deciding on structural changes
- reviewing governance files, compatibility bridges, mirrors, and hygiene safeguards together

Use it as a meta-skill for customization health.
Do not turn it into another always-on layer, and do not use it as a substitute for repository-specific workflow skills such as `impact-review` or `debug-behavior`.

If adopters want to use that skill across repositories instead of only inside one repository, install it into a supported personal skills directory or use Copilot CLI's documented alternative skills location support.

## Choose The Closure Policy Deliberately

Do not leave follow-through closure style implicit.

Triggers can reveal possible downstream work.
They should not, by themselves, decide whether the current pass must widen now or whether that work becomes explicit follow-up; that belongs to the closure policy.

At minimum, decide whether the repository leans:

- `integrated`
  - clear downstream impact is usually reconciled in the current pass
- `split`
  - downstream impact is usually carried forward as explicit follow-up work
- `hybrid`
  - small and certain follow-through is handled now, broader or riskier work is carried forward explicitly

Keep that policy short and put it in the baseline, usually as one rule or a very small set of rules.

The policy should define the repository's acceptable envelope.
It should not restate the whole follow-through workflow.

## Use Explicit Carry-Forward Only When It Helps

Not every repository needs a dedicated carry-forward surface.

Conversation memory may be enough when follow-through is usually integrated and the work is short-lived.

But if the repository often defers meaningful follow-through, handles long-running or high-care work, or expects conversations to stop and resume, consider preserving that follow-through in an explicit surface the team already uses.

That surface may be a board item, issue, review finding, handoff note, or another equivalent mechanism.

The goal is continuity outside agent memory, not another required layer.

## Teach The Runtime Model Explicitly

When you document or teach this architecture, explain not only the file layout but also the runtime behavior the layout is meant to support.

In practice, adopters should understand that:

- repository-wide instructions provide default context
- path-specific instructions can become relevant as the agent touches new paths
- follow-through can expand the scope into new surfaces
- generic skills can be chosen just-in-time when the type of work changes
- exact repeatable checks may live in scripts, CI, or runbooks rather than in prose alone
- when a repository chooses to defer meaningful follow-through, a board item, issue, review finding, handoff note, or another explicit carry-forward surface may preserve it outside conversation memory

This helps teams avoid two common mistakes:

- expecting the architecture to behave like a rigid dispatcher
- expecting a separate skill for every trigger or ownership node

GitHub's documentation supports this mental model:

- matching repository-wide and path-specific instructions can both apply
- custom instructions become available automatically when saved
- skills are selected based on prompt plus skill description and injected into context when chosen

## Use Automation For Exact Procedures

If a repository needs exact commands, deterministic checks, or a rigid update sequence, prefer:

- scripts
- CI checks
- runbooks

Let instructions and skills point to that automation when helpful, but avoid restating brittle procedures in general instructions or generic skills.

## Review The Structure Regularly

Review the structure whenever one of these happens:

- a rule appears in multiple instructions
- an instruction no longer maps to a stable boundary
- an instruction is mostly workflow and should be a skill
- a new instruction is being proposed for a downstream consequence rather than an ownership boundary
- a new skill is being proposed for every trigger or ownership node
- near-identical trigger lists keep appearing across sibling or nearby nodes
- the tree is expanding to leaf nodes before broader owners have proved insufficient
- exact operational checklists are drifting into generic instructions or skills
- a separate hint layer is being proposed just to connect triggers and skills
- maintainers can no longer predict which instructions apply to a given file

When that happens, revisit:

- [Decision Rules](./rules/decision-rules.md)
- [Ownership Tree Grammar](./rules/ownership-tree-grammar.md)
- [Examples](./examples/README.md)

## Healthy End State

The model is healthy when:

- maintainers can explain the ownership map clearly
- the folder grammar can be explained without introducing special cases
- the instruction set is small enough to reason about
- downstream consequences are handled through `Follow-Through Triggers` instead of ad hoc duplication
- the skill catalog stays small and outcome-based rather than mirroring every trigger
- exact procedures live in automation or runbooks instead of brittle prose
- the same structure can be reused in another repository with a different ownership map

## Related Material

- [Operating Model](./model/operating-model.md)
- [Follow-Through Triggers](./model/follow-through-triggers.md)
- [Decision Rules](./rules/decision-rules.md)
- [Ownership Tree Grammar](./rules/ownership-tree-grammar.md)
- [Examples](./examples/README.md)
- GitHub Docs, Adding custom instructions for GitHub Copilot CLI  
  <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions>
- GitHub Docs, Creating agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills>
