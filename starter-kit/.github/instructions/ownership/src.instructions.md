---
description: "Ownership node for broad source-code behavior."
applyTo: "src/**"
---

This node holds broad rules for source code.
Keep local specialization in narrower ownership nodes.

- Keep boundaries explicit.
- Keep behavior readable and traceable.
- Do not hide important behavior behind generic helpers without clear value.

## Follow-Through Triggers

- If public behavior, contracts, config expectations, or operations change, review tests and docs that encode those expectations.
