---
name: "overlay: bilingual parity"
description: "Cross-cutting overlay for keeping English and Portuguese documentation structurally mirrored."
applyTo: "README.md, README.pt-BR.md, docs/en/**, docs/pt-BR/**"
---

# Bilingual Parity Overlay

This overlay keeps the English and Portuguese documentation trees aligned.

- Treat English and Portuguese docs as structural mirrors by default.
- Prefer the same section order, file granularity, and link topology in both languages.
- Translate the meaning, but preserve the same documentation architecture.
- If one language intentionally diverges, make the reason explicit instead of letting drift look accidental.

## Follow-Through Triggers

- If a file is added, removed, split, merged, or moved on one side, update the mirrored side and the validation script in the same change.
- If a portal or index changes navigation, review the corresponding portal or index in the other language.
