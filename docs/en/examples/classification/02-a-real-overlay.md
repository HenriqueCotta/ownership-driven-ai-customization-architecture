# A Real Overlay

## Scenario

You want one shared testing-quality lens to apply across both production code and tests:

```text
src/**/*.ts
tests/**/*.ts
```

## Wrong First Guess

"Testing should be another ownership node under `src`."

## Correct Classification

This is a cross-cutting overlay.

## Why

Testing is not owned by one architectural slice such as `api`, `billing`, or `docs`.

It spans multiple slices and gives one extra lens:

- prefer behavior-focused tests over implementation-detail tests,
- keep fixtures small and readable,
- cover meaningful success, failure, and edge cases,
- keep test names clear about what behavior is being validated.

That is why testing can be an overlay: it adds one testing lens across many owners.

What does **not** make testing an overlay by itself is a rule like:

- "if logic changes in `src/**`, review or update tests"

That is usually a follow-through consequence, not the definition of the overlay.

## Follow-Through

If a behavior change happens in `src/api/orders/create_order.ts`, the trigger to review tests usually belongs in the source-side owner or in the baseline, because that is where the change is best understood.

Then, when Copilot opens test files, the testing overlay helps it apply testing-specific standards.

That means the flow is usually:

1. a source-side owner says behavior changed, so tests may need review,
2. Copilot opens the relevant test files,
3. the testing overlay helps shape how those tests should be written or revised.

Typical test surfaces:

- `tests/api/orders/create_order.test.ts`
- integration tests,
- fixtures,
- test helpers
