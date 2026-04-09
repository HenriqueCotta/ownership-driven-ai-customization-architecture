---
name: "ownership: repo automation"
description: "Ownership node for this repository's own .github surfaces, internal instructions, and contributor workflow wiring."
applyTo: ".github/**"
---

# Repo Automation Ownership

This repository should use its own Ownership-Driven architecture inside `.github/`.

- Keep internal instructions aligned with the public architecture we document.
- Prefer broad ownership nodes plus small overlays over monolithic instruction files.
- If a maintenance rule keeps returning in review, encode it here instead of relying on memory.
- Keep workflow, template, and instruction changes predictable for contributors.

## Follow-Through Triggers

- If `.github/instructions/**` changes shape, review whether docs or the validation script assume the old structure.
- If contributor workflow changes, review issue templates, pull request templates, and contributor-facing policy docs together.
