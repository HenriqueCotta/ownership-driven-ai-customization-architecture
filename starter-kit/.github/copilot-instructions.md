---
description: "Starter-kit baseline for an Ownership-Driven Copilot setup."
---

# Repository Baseline

- Keep this file short and let ownership-tree instructions do most of the routing work.
- Use ownership nodes for path-owned logic and overlays for truly cross-cutting concerns.
- Keep downstream review/update behavior inside `Follow-Through Triggers`.
- Put a follow-through rule here only when the triggering change may originate anywhere in the repository.
- Use skills only for reusable workflows that would bloat always-on instructions.
- Keep skills outcome-based and reusable rather than creating one skill per trigger.
- Prefer scripts, CI checks, or runbooks for exact repeatable procedures.
- Keep code, tests, docs, config, and operational behavior aligned.
