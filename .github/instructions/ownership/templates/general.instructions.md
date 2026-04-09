---
name: "ownership: templates"
description: "Ownership node for reusable templates distributed by this repository."
applyTo: "templates/**"
---

# Templates Ownership

Templates should express the architecture cleanly without dragging in repo-specific assumptions.

- Keep templates generic, copyable, and aligned with the documented model.
- Prefer template wording that teaches the structure instead of hiding it.
- Do not let templates drift away from the starter kit they are meant to support.

## Follow-Through Triggers

- If a template changes, review the starter kit and docs that depend on that template shape.
- If the documented architecture changes, review whether each template still teaches the current model.
