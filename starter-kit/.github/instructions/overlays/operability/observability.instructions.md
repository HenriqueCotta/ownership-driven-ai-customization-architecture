---
applyTo: "src/**, docs/operations/**, docs/reference/observability/**"
---

- Prefer actionable telemetry.
- Keep error signals diagnosable.
- Preserve stable signal names and meanings.

## Follow-Through Triggers

- If runtime failure behavior changes, review telemetry docs, dashboards, and tests that depend on those signals.
