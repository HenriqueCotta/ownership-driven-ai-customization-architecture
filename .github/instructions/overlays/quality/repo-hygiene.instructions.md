---
name: "overlay: repo hygiene"
description: "Cross-cutting overlay for avoiding stale links, stale validation rules, and architecture drift across docs and support surfaces."
applyTo: ".github/**, docs/**, starter-kit/**, templates/**, scripts/**, README.md, README.pt-BR.md"
---

# Repo Hygiene Overlay

This overlay adds a maintenance lens across the repository's public and support surfaces.

- Treat broken links, orphaned examples, and stale validation assumptions as real defects.
- Keep the repo's own `.github` implementation consistent with the architecture it publishes.
- When moving content, update indices, portals, and validation in the same change.
- Prefer one coherent source of truth over repeated near-copies.

## Follow-Through Triggers

- If structure changes, review READMEs, docs indices, `scripts/check_repo.py`, and `.github/workflows/docs-hygiene.yml`.
- If the repo starts teaching a new rule, review whether that rule belongs in baseline, ownership, or an overlay inside `.github/instructions`.
