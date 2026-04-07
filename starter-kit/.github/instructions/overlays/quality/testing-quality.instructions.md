---
description: "Cross-cutting overlay for testing quality."
applyTo: "src/**, tests/**"
---

- Prefer behavior-focused tests.
- Keep fixtures small.
- Cover meaningful success, failure, and edge cases.

## Follow-Through Triggers

- If shared test fixtures or helpers change, review the tests that depend on them.
