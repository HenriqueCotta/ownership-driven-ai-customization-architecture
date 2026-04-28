---
applyTo: ".github/**"
---

# Repo Automation Ownership

This is the broad fallback owner for `.github/` surfaces that do not already have a narrower owner or overlay.

- Keep internal instructions aligned with the public architecture we document.
- Prefer narrower owners plus small overlays over growing this file into a monolith.
- If a maintenance rule keeps returning in review, encode it here instead of relying on memory.
- Keep workflow, template, and instruction changes predictable for contributors.

## Follow-Through Triggers

- If `.github/instructions/**` changes shape, review whether docs or the validation script assume the old structure.
- If `.github/` grows a new stable concern family, add a narrower owner or overlay instead of stretching this file to cover everything.
- If contributor workflow changes, review issue templates, pull request templates, and contributor-facing policy docs together.
