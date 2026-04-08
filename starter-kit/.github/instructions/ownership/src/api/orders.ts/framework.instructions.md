---
name: "ownership: src api orders framework"
description: "Framework guidance for the orders API file."
applyTo: "src/api/orders.ts"
---

This file-level node carries framework-facing guidance for `orders.ts`.

- Keep transport and framework glue thin.
- Validate early and keep framework-specific concerns at the edges.
- Avoid coupling business rules to framework lifecycle hooks when plain functions are enough.

## Follow-Through Triggers

- If routing, middleware expectations, or request-handling flow changes, review integration tests and operational signals.
