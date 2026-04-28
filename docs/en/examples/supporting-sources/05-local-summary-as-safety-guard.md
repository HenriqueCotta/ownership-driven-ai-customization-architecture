# Local Summary As Safety Guard

## Situation

A repository depends on an external policy source for billing constraints.

The policy source is authoritative, but access sometimes fails in local environments.

The team wants the agent to avoid unsafe changes when the source is unavailable.

## Source Entry

```md
## finance-policy

Where: policy workspace `billing-policy`
Access: policy-docs MCP, if available.
Use for: tax, invoice, refund, and compliance constraints.
Freshness: verify before changing invoice or refund behavior.
If unavailable: do not relax existing finance constraints; mark policy verification blocked.
If it conflicts: owns finance compliance constraints.
```

## Owner Instruction

```md
---
applyTo: "src/billing/**"
---

# Billing

Invoices must remain tax-inclusive at display boundaries.

Local safety summary: existing invoice displays are tax-inclusive. If supporting source `finance-policy` is unavailable, this summary may preserve current behavior, but it must not justify a new tax rule.

Before changing invoice or refund semantics, use supporting source `finance-policy`.
```

## Why This Duplication Is Acceptable

The duplicated sentence is short, stable, and defensive.

It prevents the agent from relaxing an important invariant when the source cannot be reached.

It does not copy detailed rates, regional exceptions, or procedural policy text.

## Bad Version

```md
# Billing

The current tax rate is 17.5%. Region A uses exception X. Region B uses exception Y. Discounts use policy rule ABC. Refund timing follows the current finance spreadsheet.
```

This turns the instruction into a stale mirror.

If those facts matter, the agent needs the current authoritative source.

## Teaching Takeaway

Duplicate durable guardrails sparingly.

Use them to preserve safety when access fails, not to avoid checking the source before making a policy-dependent change.
