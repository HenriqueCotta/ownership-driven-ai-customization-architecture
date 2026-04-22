---
name: "ownership: templates"
description: "Ownership node for reusable templates distributed by this repository."
applyTo: "templates/**"
---

# Templates Ownership

Templates should express the architecture cleanly without dragging in repo-specific assumptions.

- Keep templates generic, scaffold-first, and aligned with the documented model.
- Point adopters to the starter kit when they want a copyable minimal implementation.
- Prefer template wording that makes required adaptation obvious instead of hiding it.
- Do not let templates drift away from the starter kit they are meant to support.

## Follow-Through Triggers

- If a template changes, review the starter kit and the docs that position templates as scaffolds rather than copyable implementations.
- If the documented architecture changes, review whether each template still teaches the current model.
