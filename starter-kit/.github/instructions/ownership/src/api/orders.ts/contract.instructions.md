---
applyTo: "src/api/orders.ts"
---

This file-level node carries contract guidance for `orders.ts`.

- Keep request and response contracts explicit.
- Preserve field meaning, defaults, and compatibility expectations.
- Call out contract-risky changes early.

## Follow-Through Triggers

- If fields, defaults, return semantics, or compatibility expectations change, review implementations, tests, and reference docs.
