---
name: "ownership: docs"
description: "Ownership node for the public architecture documentation under docs/."
applyTo: "docs/**"
---

# Documentation Ownership

The docs tree is the canonical public explanation of the architecture.

- Keep the documentation architecture clear: explanation, model, rules, how-to, and examples.
- Keep overview pages short and route detail into focused pages instead of repeating it.
- Keep repository archetypes inside `examples/repositories/`.
- Favor realistic, selective examples over exhaustive trees that no real repo would maintain.

## Follow-Through Triggers

- If docs structure, page naming, or example layout changes, review both language trees, root READMEs, and `scripts/check_repo.py` for stale references or assumptions.
- If a public architectural claim changes, review starter-kit files, templates, and examples that teach that claim.
