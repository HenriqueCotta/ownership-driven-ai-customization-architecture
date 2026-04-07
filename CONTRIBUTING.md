# Contributing

Thanks for helping improve this project.

## Before You Open A Pull Request

- Read [README.md](./README.md).
- Read the architecture docs in [docs/en](./docs/en/README.md) or [docs/pt-BR](./docs/pt-BR/README.md).
- For larger changes, open an issue first so the direction can be discussed before the structure drifts.

## What Good Contributions Look Like

- the change improves clarity, adoption, or maintainability
- the change keeps the architecture repository-agnostic
- the change avoids adding unnecessary layers, agents, or special cases
- the change includes docs updates when terminology, structure, or starter-kit behavior changes

## Documentation Rules

- Keep English and Portuguese public docs aligned when the core model changes.
- If exact same-day parity is not possible, state the mismatch clearly in the pull request.
- Do not add repository-specific examples to the canonical architecture docs unless they are clearly labeled as examples.

## Starter Kit Rules

- Keep the starter kit small enough to understand quickly.
- Favor copyable defaults over exhaustive coverage.
- If the starter kit structure changes, update the templates and docs that explain it.

## Validation

Before opening a pull request, run:

```bash
python scripts/check_repo.py
```

## Pull Request Checklist

- The change has a clear reason.
- Public-facing docs were updated when needed.
- Starter kit and templates remain coherent.
- English and Portuguese navigation still works.
- `python scripts/check_repo.py` passes.
