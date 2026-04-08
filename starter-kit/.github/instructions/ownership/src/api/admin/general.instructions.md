---
name: "ownership: src api admin general"
description: "Ownership guidance for admin API paths."
applyTo: "src/api/admin/**"
---

This node narrows the API owner for privileged admin surfaces.

- Keep authorization boundaries explicit.
- Keep privileged actions easy to audit.
- Avoid convenience helpers that hide access decisions.

## Follow-Through Triggers

- If access rules, privileged actions, or audit expectations change, review tests, docs, and operational checks.
