# Product Monorepo

## Repository Shape

```text
repo/
  apps/
    web/
    admin/
    api/
  packages/
    ui/
    auth/
    contracts/
    analytics/
  docs/
    architecture/
    product/
    runbooks/
  infra/
    terraform/
    ci/
```

## A Realistic Ownership Map

```text
.github/
  instructions/
    ownership/
      apps/
        general.instructions.md
        admin/
          authorization.instructions.md
      packages/
        contracts/
          general.instructions.md
        auth/
          security.instructions.md
      infra/
        terraform/
          safety.instructions.md
      docs/
        runbooks/
          general.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      operability/
        observability.instructions.md
```

## Why This Map Is Realistic

- `apps/general` gives deployable apps one shared application-level baseline
- `apps/admin/` gets a narrower node because admin surfaces usually have stronger authorization and operational expectations
- `packages/contracts/` gets a dedicated node because shared contracts create wide consumer blast radius
- `packages/auth/` gets a dedicated node because auth behavior is security-sensitive across consumers
- `infra/terraform/` gets a dedicated node because infrastructure changes are high-impact and safety-sensitive
- `docs/runbooks/` is explicit because operational documentation is a real owned surface

What is intentionally not mapped:

- `apps/web/` and `apps/api/` do not get their own nodes unless they truly diverge from `apps/general`
- `packages/ui/` and `packages/analytics/` stay under broader ownership until they prove they need local rules
- `infra/ci/` stays under broader operational practice unless CI itself becomes a high-friction area
- `docs/product/` and `docs/architecture/` rely on broader docs practice and follow-through

That is much closer to what a real monorepo can sustain over time.

## Prompt-Driven Situations

### Change A Shared Contract In `packages/contracts/`

Example prompt:

```text
Add an optional `customerTier` field to the shared order summary contract and update impacted consumers, tests, and docs.
```

Likely instruction context:

- `packages/contracts/general`
- testing-quality overlay
- observability overlay if the field affects events or operational diagnostics

How the architecture shapes the process:

1. The contracts node keeps the model focused on shared schema discipline.
2. The prompt naturally pulls consumer impact into scope.
3. Follow-through bridges from shared package change to app consumers and docs without creating nodes for every consumer path.

Likely follow-through:

- `apps/web`, `apps/admin`, and `apps/api` consumers
- tests for contract consumers
- docs if the field is externally visible

### Update Auth Behavior In `packages/auth/`

Example prompt:

```text
Tighten refresh-token reuse detection in the shared auth package and update any tests, runbooks, or app integrations that should move with it.
```

Likely instruction context:

- `packages/auth/security`
- testing-quality overlay
- observability overlay if auth events or diagnostics change

How the architecture shapes the process:

1. The auth node keeps the change framed as a security-sensitive package change.
2. The observability overlay catches auth telemetry and operational diagnostics.
3. Follow-through points to app integrations and runbooks without turning every auth consumer into a dedicated node.

Likely follow-through:

- app consumers
- auth tests
- runbooks
- product docs if sign-in behavior changes

### Change Terraform Behavior In `infra/terraform/`

Example prompt:

```text
Update the Terraform module so queue alerts are created by default in production only. Adjust docs and safety checks as needed.
```

Likely instruction context:

- `infra/terraform/safety`
- observability overlay

How the architecture shapes the process:

1. The Terraform node frames the change as a safety-sensitive infra change.
2. The observability overlay keeps alerting and monitoring implications visible.
3. Follow-through catches runbooks and environment docs without requiring a node for every infra subfolder.

Likely follow-through:

- runbooks
- environment docs
- validation or drift checks
- dashboard and alert ownership review

## Teaching Takeaway

This monorepo scales with the architecture because it maps only the decision boundaries that really matter:

- broad app behavior
- high-risk shared packages
- high-risk infrastructure
- operational docs

That keeps the tree understandable even when the repository itself is large.
