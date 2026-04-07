# Examples And Flows

Audience: maintainers who want to understand the architecture by example before designing their own structure.
Goal: teach the `Ownership-Driven AI Customization Architecture` using simple, reusable programming scenarios rather than repository-specific terminology.

## How To Use This File

Read the examples in order.

They move from the simplest distinction to more realistic flows:

1. identify the owner of a path,
2. identify an overlay,
3. identify a downstream consequence,
4. decide whether another surface must be reviewed or updated.

Each example follows the same teaching pattern:

- scenario
- wrong first guess
- correct classification
- why it is correct
- follow-through

## Example 1: One Path, One Owner

### Scenario

You have this path:

```text
src/api/orders/create_order.ts
```

### Wrong First Guess

"This needs an overlay because it is important."

### Correct Classification

This is an ownership-tree problem.

Likely ownership nodes:

- `src/**/*.ts`
- `src/api/**/*.ts`
- `src/api/orders/**/*.ts`

### Why

The path belongs to a clear responsibility boundary:

- code,
- then API code,
- then order API code.

That is hierarchy by ownership, not a cross-cutting concern.

### Follow-Through

No downstream review is required unless the change affects behavior, contracts, config, or documentation.

## Example 2: A Real Overlay

### Scenario

You want one shared testing-quality lens to apply across both production code and tests:

```text
src/**/*.ts
tests/**/*.ts
```

### Wrong First Guess

"Testing should be another ownership node under `src`."

### Correct Classification

This is a cross-cutting overlay.

### Why

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

### Follow-Through

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

## Example 3: Narrower Owner vs Overlay

### Scenario

You have these paths:

```text
src/api/orders/**/*.ts
src/billing/invoices/**/*.ts
```

### Wrong First Guess

"These are two special cases, so they should be overlays."

### Correct Classification

These are narrower ownership-tree nodes.

### Why

They are different because each subtree owns a different kind of logic:

- order API logic
- invoice logic

That is ownership.

An overlay would be something like:

```text
src/api/**/*.ts
src/billing/**/*.ts
```

for one shared concern such as observability, retries, or error reporting.

### Follow-Through

If you add a new invoice lifecycle state, you may need:

- billing tests
- billing docs
- telemetry review

But the ownership decision still comes first: invoice logic is owned by the invoice subtree.

## Example 4: Contract Change

### Scenario

You change a public interface:

```text
src/contracts/payment_gateway.ts
```

### Wrong First Guess

"Only the contract file changed, so the change is local."

### Correct Classification

Primary instruction context:

- baseline
- language-quality instruction if the repo uses one
- ownership-tree node for contracts

### Why

Contracts are usually small files with large blast radius.

Even if the edit is local, the meaning of the change is not.

### Follow-Through

A `Follow-Through Triggers` section in the contract instruction may say:

- if fields, defaults, return semantics, or compatibility expectations changed, review implementations, tests, and reference docs

Expected flow:

1. change the contract,
2. inspect implementations,
3. inspect tests,
4. inspect docs,
5. update or explicitly justify no downstream change.

## Example 5: Configuration Change

### Scenario

You change config loading or defaults:

```text
src/config/load_config.ts
```

### Wrong First Guess

"This is internal plumbing, so only the config file matters."

### Correct Classification

Primary instruction context:

- baseline
- ownership-tree node for configuration

Possible downstream surfaces:

- docs
- sample config files
- tests

### Why

Configuration changes often affect what users type, what operators expect, and what tests encode.

### Follow-Through

A `Follow-Through Triggers` section may say:

- if precedence, defaults, source-of-truth rules, or validation changed, review examples, docs, and tests

Expected flow:

1. change config behavior,
2. inspect sample configs,
3. inspect tests,
4. inspect docs,
5. update or justify no-op.

## Example 6: Documentation As Its Own Owner

### Scenario

You edit:

```text
docs/orders.md
```

### Wrong First Guess

"Documentation must always be an overlay because it relates to code."

### Correct Classification

`docs/**/*.md` is usually its own ownership-tree node.

### Why

Documentation is its own surface with its own quality rules:

- clarity,
- source of truth,
- structure,
- update discipline.

It is related to code, but that relationship is usually expressed through follow-through, not by turning docs into an overlay for source code.

### Follow-Through

If the doc is being changed because code already changed, Copilot should verify:

- the current implementation,
- the related tests,
- whether the doc is still accurate.

## Example 7: Board Or Task Follow-Through

### Scenario

You finish an implementation and realize the scope changed:

- one acceptance criterion is no longer correct
- a new follow-up item was discovered

### Wrong First Guess

"Task tracking should be another owner under `src`."

### Correct Classification

Task tracking is usually a cross-cutting overlay.

### Why

It spans many kinds of work:

- code,
- docs,
- design,
- operations,
- rollout.

### Follow-Through

A `Follow-Through Triggers` section may say:

- if scope, status, acceptance criteria, or follow-up work changed materially, review task tracking

Expected flow:

1. reassess what changed,
2. decide whether the task is now stale,
3. update it if the workflow supports that,
4. otherwise explain exactly what needs updating.

## Example 8: No Follow-Through Needed

### Scenario

You rename variables and simplify a helper without changing behavior:

```text
src/api/orders/normalize_input.ts
```

### Wrong First Guess

"Every change should force docs, tests, and board review."

### Correct Classification

This is still an ownership-tree edit, but it may not trigger downstream work.

### Why

Not every change is behavior change.

If nothing public, contractual, operational, or user-facing changed, forcing follow-through creates noise.

### Follow-Through

A good outcome is:

1. confirm the change is behavior-preserving,
2. avoid unnecessary downstream edits,
3. make that decision explicit in the explanation.

## Quick Review Checklist

After a meaningful change, ask:

1. Which path is the primary owner of this file?
2. Which broader or narrower ownership-tree nodes also apply?
3. Is there a real cross-cutting concern here, or am I mislabeling ownership as an overlay?
4. Does an existing `Follow-Through Triggers` section describe what else may now be stale?
5. If not, should that guidance be added to an existing instruction rather than a new file?
