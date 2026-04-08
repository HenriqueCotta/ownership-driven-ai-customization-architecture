---
name: "ownership: src general"
description: "Broad ownership guidance for source code."
applyTo: "src/**"
---

This node holds broad rules for source code.
Keep narrower node folders only where a smaller boundary truly needs different guidance.

- Keep boundaries explicit.
- Keep behavior readable and traceable.
- Do not hide important behavior behind generic helpers without clear value.

## Follow-Through Triggers

- If public behavior, contracts, config expectations, or operations change, review tests and docs that encode those expectations.
