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

## Healthy Ownership Tree

```text
.github/
  instructions/
    ownership/
      apps/
        general.instructions.md
        web/
          general.instructions.md
        admin/
          authorization.instructions.md
        api/
          general.instructions.md
      packages/
        general.instructions.md
        ui/
          consistency.instructions.md
        auth/
          security.instructions.md
        contracts/
          general.instructions.md
        analytics/
          instrumentation.instructions.md
      docs/
        general.instructions.md
      infra/
        general.instructions.md
        terraform/
          safety.instructions.md
        ci/
          reliability.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      consistency/
        code-docs-consistency.instructions.md
      operability/
        observability.instructions.md
```

## Why This Is Well-Implemented

- apps, shared packages, docs, and infra are separate top-level ownership surfaces
- admin and auth are narrower owners because they carry special access and security expectations
- contracts are shared-package owners rather than being duplicated across apps
- infra has its own ownership area instead of being treated as a footnote of application code

## Everyday Situations

### Changing A Shared Contract In `packages/contracts/`

Likely instruction context:

- `packages/general`
- `packages/contracts/general`
- testing-quality overlay
- code-docs-consistency overlay

Likely follow-through:

- app consumers in `apps/web`, `apps/admin`, and `apps/api`
- docs
- tests

### Updating Auth Behavior In `packages/auth/`

Likely instruction context:

- `packages/general`
- `packages/auth/security`
- testing-quality overlay
- observability overlay if auth events or diagnostics change

Likely follow-through:

- app consumers
- login and session tests
- runbooks
- product docs if sign-in behavior changes

### Changing CI Rules In `infra/ci/`

Likely instruction context:

- `infra/general`
- `infra/ci/reliability`

Likely follow-through:

- developer docs
- pipeline examples
- workflows that assume the old CI behavior

### Updating Admin UI In `apps/admin/`

Likely instruction context:

- `apps/general`
- `apps/admin/authorization`
- testing-quality overlay
- code-docs-consistency overlay if user-facing admin docs change

Likely follow-through:

- admin tests
- auth or contracts if admin behavior depends on shared packages
- docs and runbooks if operational behavior changes

## Teaching Takeaway

This repository scales because the ownership tree mirrors the monorepo's true decision boundaries:

- deployable apps
- shared packages
- docs
- infrastructure

That makes shared-change blast radius easier to reason about without overloading one monorepo-wide instruction file.
