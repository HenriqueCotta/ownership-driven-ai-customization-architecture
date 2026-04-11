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

When you add skills around those templates, keep the skill set small and outcome-based rather than creating one skill per trigger.

If a process needs exact repeatable commands or checks, prefer scripts, CI, or runbooks over stretching generic instructions or skills.
