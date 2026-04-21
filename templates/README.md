# Templates

These templates are meant to reduce blank-page friction.

Use them as starting points, not as fixed doctrine.

Included templates:

- [copilot-instructions.md.template](./copilot-instructions.md.template)
- [ownership-node.instructions.md.template](./ownership-node.instructions.md.template)
- [cross-cutting-overlay.instructions.md.template](./cross-cutting-overlay.instructions.md.template)

Adapt the wording to your repository's ownership map and operating model.

For ownership instructions, place the template inside the node folder that represents the owned boundary.

Examples:

- `ownership/src/general.instructions.md`
- `ownership/src/api/orders.ts/contract.instructions.md`
- `ownership/docs/general.instructions.md`

Optional shortcut for a simple file node:

- `ownership/src/api/orders.ts.instructions.md`

In the canonical tree convention, the folder identifies the owned path and the filename identifies the concern.

If you use the shortcut, the file path itself identifies the owned file and the single instruction file carries the whole node.

If filenames such as `general.instructions.md` repeat across the tree, set the frontmatter `name` field explicitly for clearer UI labels.

These templates do not prescribe an internal writing format.

The architecture standardizes the structural role of the instruction and `Follow-Through Triggers`, not the prose or Markdown shape inside the file.

If a repository needs a consistent closure stance for follow-through, state that briefly in the baseline instead of trying to encode it through many triggers or through one generic skill alone.

Not every instruction needs a `Follow-Through Triggers` section.

If a node or overlay has no distinct downstream rule worth stating, omit that section entirely.

If several nearby nodes would repeat almost the same trigger, move the shared part upward to the broader owner or baseline instead of copying it downward.

When you add skills around those templates, keep the skill set small and outcome-based rather than creating one skill per trigger.

If the repository also needs a reusable workflow for shaping or auditing its Copilot customization itself, consider copying the optional [oda-copilot-customization skill](../.github/skills/oda-copilot-customization/SKILL.md) from this repository.

If you want to reuse that skill across multiple repositories, add this repository's `.github/skills` directory as an alternative skills location in Copilot CLI or copy the skill into the personal skills location your tooling supports.

If a process needs exact repeatable commands or checks, prefer scripts, CI, or runbooks over stretching generic instructions or skills.
