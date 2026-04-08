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

## Healthy Ownership Tree

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        routes/
          general.instructions.md
          orders.ts/
            contract.instructions.md
            framework.instructions.md
          admin/
            authorization.instructions.md
        services/
          general.instructions.md
          orders/
            domain.instructions.md
          billing/
            domain.instructions.md
        contracts/
          general.instructions.md
        config/
          general.instructions.md
      tests/
        general.instructions.md
      docs/
        general.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      operability/
        observability.instructions.md
```

## Why This Is Well-Implemented

- route handlers, domain services, contracts, config, tests, and docs are separate ownership surfaces
- admin behavior is treated as a narrower owner, not as a vague global concern
- testing and observability are overlays because they span several ownership areas
- docs stay their own owner instead of becoming an overlay for source code

## Everyday Situations

### Adding A New Response Field In `src/routes/orders.ts`

Likely instruction context:

- `src/general`
- `src/routes/general`
- `src/routes/orders.ts/contract`
- `src/routes/orders.ts/framework`
- testing-quality overlay
- observability overlay if operational behavior changes

Likely follow-through:

- route tests
- contract tests
- docs for the endpoint
- telemetry if fields affect logs or dashboards

### Changing Billing Rules In `src/services/billing/issue-invoice.ts`

Likely instruction context:

- `src/general`
- `src/services/general`
- `src/services/billing/domain`
- testing-quality overlay
- observability overlay if operational signals change

Likely follow-through:

- billing tests
- invoices docs or finance runbooks
- contracts if public semantics changed

### Changing Config Precedence In `src/config/load-config.ts`

Likely instruction context:

- `src/general`
- `src/config/general`
- testing-quality overlay

Likely follow-through:

- example config files
- docs
- deployment or operator runbooks
- tests that encode config behavior

### Editing `docs/api/orders.md`

Likely instruction context:

- `docs/general`

Likely follow-through:

- verify the current implementation
- verify tests still support the claim
- verify referenced contracts are current

## Teaching Takeaway

This repository is easy to reason about because the ownership tree follows the system's real seams:

- transport
- domain
- contracts
- config
- docs

That keeps day-to-day edits local most of the time, while still making downstream consequences visible.
