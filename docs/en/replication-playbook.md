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
2. Identify the largest stable ownership boundaries.
3. Add only the ownership-tree instructions that match those boundaries.
4. Add true cross-cutting overlays.
5. Add a small set of reusable skills.
6. Add checks that prevent drift, dead layers, and legacy structures.

Use [Decision Rules](./rules/decision-rules.md) to classify guidance before you write it.

Use [Ownership Tree Grammar](./rules/ownership-tree-grammar.md) to decide how the ownership map should look on disk.

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

## Keep The Skill Set Small And Outcome-Based

Start with a few skills named by workflow outcome, not by triggering change or path.

Good examples:

- `review-change`
- `sync-docs`
- `debug-behavior`

That usually scales better than creating variants such as `review-contract-change`, `review-config-change`, or `review-api-drift`.

Different follow-through triggers should usually reuse the same small skill set, with local context coming from the ownership tree and overlays.

Add a more specific skill only when the workflow itself materially differs in evidence, steps, or expected output.

## Teach The Runtime Model Explicitly

When you document or teach this architecture, explain not only the file layout but also the runtime behavior the layout is meant to support.

In practice, adopters should understand that:

- repository-wide instructions provide default context
- path-specific instructions can become relevant as the agent touches new paths
- follow-through can expand the scope into new surfaces
- generic skills can be chosen just-in-time when the type of work changes
- exact repeatable checks may live in scripts, CI, or runbooks rather than in prose alone

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
- [Decision Rules](./rules/decision-rules.md)
- [Ownership Tree Grammar](./rules/ownership-tree-grammar.md)
- [Examples](./examples/README.md)
- GitHub Docs, Adding custom instructions for GitHub Copilot CLI  
  <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions>
- GitHub Docs, Creating agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills>
