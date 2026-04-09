---
name: "ownership: scripts"
description: "Ownership node for repository automation and validation scripts."
applyTo: "scripts/**"
---

# Scripts Ownership

Scripts are maintenance surfaces that should encode the current repository contract, not stale historical assumptions.

- Keep validation rules explicit, easy to inspect, and easy to update.
- Prefer actionable failures over silent drift.
- Treat broken links, stale structure assumptions, and language-mirror drift as real hygiene defects.
- Keep script logic aligned with the actual docs, starter-kit, templates, and `.github` tree.

## Follow-Through Triggers

- If docs, examples, starter-kit, templates, or `.github` structure changes, update the relevant validation logic in the same change.
- If a script changes what the repo considers valid, review the workflow that runs it and the docs that describe the expected structure.
