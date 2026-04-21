# Decision Rules

Audience: maintainers who need to place guidance correctly without guessing.  
Goal: provide a compact set of decisions for classifying instructions and recognizing redesign signals.

## On This Page

- [First-Contact Questions](#first-contact-questions)
- [Where Guidance Belongs](#where-guidance-belongs)
- [Quick Classification Checks](#quick-classification-checks)
- [Redesign Signals](#redesign-signals)
- [Related Docs](#related-docs)

## First-Contact Questions

When classifying a path or a proposed instruction, start with these questions:

1. What file or path is changing?
2. Which stable owner is responsible for that path?
3. Which extra concerns also apply there?
4. What else may now be stale because of this change?

Those four questions map directly to:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `Follow-Through Triggers`

## Where Guidance Belongs

Put guidance in the baseline when it is:

- repository-wide
- short
- broadly useful
- unlikely to change often
- the repository's closure policy for how follow-through should usually be handled

Put guidance in ownership when it is:

- tied to a stable path family
- specific to that responsibility boundary
- useful most of the time in that boundary

Put guidance in a cross-cutting overlay when it is:

- relevant across multiple ownership areas
- not owned by one architectural slice
- important enough to load automatically in matching paths

Put guidance in a skill when it is:

- a reusable workflow
- deeper than always-on policy
- not naturally tied to one path

Keep guidance outside the repository map when it is:

- an individual preference that belongs in personal instructions or a personal agent profile
- an organization-level preference that belongs in organization instructions
- mainly an agent tool, MCP, or permission profile rather than repository behavior

Put guidance in automation or a runbook when it is:

- an exact repeatable procedure
- clearer as a script, CI check, or operational checklist than as open-ended prose
- expected to execute deterministically

## Quick Classification Checks

Use these checks when the choice feels unclear:

- if the path is the owner of a kind of logic, it is probably ownership
- if one extra concern spans several owners, it is probably an overlay
- if the main question is "what else may now need downstream follow-through?", it is probably follow-through
- if a node has no distinct downstream consequence worth stating, omit the trigger section instead of filling it with generic repetition
- if a follow-through rule depends on changes outside the instruction's own scope, move it to the instruction that actually observes the originating change, whether that is another owner, a broader owner, an overlay, or the baseline
- if several sibling or nearby nodes would carry almost the same trigger, move the shared rule upward and keep only true local deltas below
- if many downstream cases would reuse the same workflow, prefer one outcome-based skill rather than one skill per trigger
- if the real question is "what is this repository's general stance on closing follow-through now versus carrying it forward?", that is usually baseline policy rather than a trigger or a skill
- if a broader owner still gives honest and useful guidance, stop there for now instead of growing the tree deeper preemptively
- if the content mostly describes a reusable task flow, it is probably a skill
- if the content mainly prescribes exact commands, files, or step order, it probably belongs in automation or a runbook
- if the content mainly defines tools, permissions, or execution profile for a specialized agent, it probably belongs in agent configuration or settings rather than in follow-through prose
- if the only goal is to help readers discover existing guidance, keep that as a small cue inside existing docs or instructions rather than introducing a hint layer

For the conceptual distinction, read [Ownership vs Overlay](../model/ownership-vs-overlay.md).

For downstream consequences, read [Follow-Through Triggers](../model/follow-through-triggers.md).

For how repository policy, reusable skills, automation, and tracking fit around those triggers, use [Operating Model](../model/operating-model.md) and [Replication Playbook](../replication-playbook.md).

## Redesign Signals

Treat these as signs that the map needs redesign:

- the same rule appears in multiple instructions
- near-identical trigger prose appears across sibling or nearby nodes
- a child instruction reverses a parent instead of refining it
- an overlay is named by crossed paths instead of by one coherent concern
- a docs path is treated as an overlay when it should be its own owner
- a new instruction is proposed only because a change has downstream consequences
- the map keeps growing into narrower leaf nodes before broader owners have proved insufficient
- a trigger is being added to almost every instruction whether or not it says anything locally distinct
- a new skill is being proposed for every trigger or ownership node
- exact procedural checklists are living in generic instructions or generic skills
- a new hint layer is being proposed only to connect triggers and skills
- maintainers cannot predict which instructions apply to a given file

## Related Docs

- [Operating Model](../model/operating-model.md)
- [Ownership vs Overlay](../model/ownership-vs-overlay.md)
- [Follow-Through Triggers](../model/follow-through-triggers.md)
- [Replication Playbook](../replication-playbook.md)
- [Ownership Tree Grammar](./ownership-tree-grammar.md)
