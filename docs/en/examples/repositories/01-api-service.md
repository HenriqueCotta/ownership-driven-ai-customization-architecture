# API Service

## Repository Shape

```text
repo/
  src/
    routes/
      health.ts
      orders.ts
      admin/
        users.ts
    services/
      orders/
        create-order.ts
      billing/
        issue-invoice.ts
    contracts/
      orders.ts
      billing.ts
    config/
      load-config.ts
  tests/
    routes/
    services/
    contracts/
  docs/
    api/
    runbooks/
```

## A Realistic Ownership Map

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        routes/
          orders.ts/
            contract.instructions.md
            framework.instructions.md
        services/
          billing/
            domain.instructions.md
        contracts/
          general.instructions.md
        config/
          general.instructions.md
      docs/
        api/
          general.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      operability/
        observability.instructions.md
```

## Why This Map Is Realistic

- `src/general` carries broad backend expectations for the service
- `src/routes/orders.ts/` gets its own node because it combines public contract concerns and route-framework concerns
- `src/services/billing/` gets a narrower node because financial logic usually deserves tighter domain guidance
- `src/contracts/` and `src/config/` are separate owners because contract changes and config changes have clear downstream blast radius
- `docs/api/` is explicit because endpoint documentation is a real owned surface

Just as important, this map is selective:

- `routes/health.ts` does not get its own node
- `services/orders/` does not get its own node
- `tests/` does not get a separate ownership node here
- `docs/runbooks/` stays under broader operational follow-through rather than getting its own branch

That is usually what a mature repository looks like. Most paths rely on broader owners, overlays, and follow-through instead of bespoke local instructions.

## Prompt-Driven Situations

### Add A Response Field To `src/routes/orders.ts`

Example prompt:

```text
Add `customerTier` to the orders response. Update the route, contract, tests, and docs if needed.
```

Likely instruction context:

- `src/general`
- `src/routes/orders.ts/contract`
- `src/routes/orders.ts/framework`
- `src/contracts/general`
- testing-quality overlay
- observability overlay if response shape affects logs, metrics, or dashboards

How the architecture shapes the process:

1. The route-specific node pushes attention to HTTP mapping and response semantics.
2. The contracts owner keeps the shared schema honest.
3. The testing overlay reminds Copilot to update route and contract coverage.
4. Follow-through brings `docs/api/` into scope without requiring a docs overlay.

Likely follow-through:

- route tests
- contract tests
- endpoint docs
- telemetry review if downstream consumers depend on the field

### Change Billing Rules In `src/services/billing/issue-invoice.ts`

Example prompt:

```text
Change invoice issuance so failed retries are marked as recoverable instead of terminal. Update anything else that should move with that rule.
```

Likely instruction context:

- `src/general`
- `src/services/billing/domain`
- testing-quality overlay
- observability overlay if failure classification changes operational signals

How the architecture shapes the process:

1. The billing node keeps the model focused on domain semantics instead of route mechanics.
2. The observability overlay catches the operational side of failure-state changes.
3. Follow-through points to finance docs, tests, and runbooks without creating a separate node for each one.

Likely follow-through:

- billing tests
- finance-facing docs or runbooks
- alerting and dashboards if error classification changes
- contracts if public semantics changed

### Change Config Precedence In `src/config/load-config.ts`

Example prompt:

```text
Make environment variables override file-based config only for production and staging. Update the surrounding docs and checks.
```

Likely instruction context:

- `src/general`
- `src/config/general`
- testing-quality overlay

How the architecture shapes the process:

1. The config owner keeps the change framed as a configuration-semantics change, not just a code edit.
2. The testing overlay pushes toward scenario coverage for precedence rules.
3. Follow-through brings docs and operational guidance into scope even though they are not modeled as separate local nodes.

Likely follow-through:

- precedence tests
- example config docs
- deployment or operator runbooks
- startup diagnostics if the new behavior changes support expectations

## Teaching Takeaway

This repository works well with the architecture because the map is selective:

- broad source behavior sits in `src/general`
- only high-value local exceptions get narrower nodes
- overlays stay small
- downstream work is handled through follow-through instead of by growing a giant ownership tree
