# Múltiplas Fontes e Conflitos

## Situação

Um repositório muda comportamento de assinatura e cobrança.

A mudança pode envolver intenção de produto, policy financeira, comportamento de provider, testes, docs e trabalho planejado de follow-up.

Nenhuma fonte sozinha possui todas essas claims.

## Trecho da Fonte de Apoio

```md
## Conflict Handling

When sources diverge, classify the disputed claim first: implementation behavior, product intent, external platform fact, policy, planned work, or design-system contract.

Prefer the source that owns that claim. If the owning source is unavailable and the missing fact could change the result, treat that part as verification-blocked.

## product-workspace

Where: product workspace `subscription-product-notes`
Access: product-docs MCP, if available.
Use for: subscription product intent and accepted product decisions.
If it conflicts: owns intended customer semantics; code/tests may reveal implementation drift.

## finance-policy

Where: policy workspace `billing-policy`
Access: policy-docs MCP, if available.
Use for: tax, invoice, refund, and compliance constraints.
Freshness: verify before changing invoice or refund behavior.
If unavailable: do not relax existing finance constraints; mark policy verification blocked.
If it conflicts: owns finance compliance constraints.

## payment-provider-docs

Where: `https://provider.example/docs`
Use for: provider-owned fields, limits, auth, errors, and API behavior.
Freshness: verify current docs before changing provider-specific behavior.
If it conflicts: current provider docs own provider facts; local mirrors may be stale.

## work-board

Where: board `subscription-work`
Use for: accepted follow-ups and explicit carry-forward.
Do not use for: current behavior unless linked to merged code or accepted docs.
```

## Instruction de Owner

```md
---
applyTo: "src/subscriptions/**"
---

# Subscriptions

Subscription state changes must keep customer-visible entitlement, billing, and cancellation behavior consistent.

Before changing invoice, refund, or cancellation semantics, use supporting source `product-workspace` for product intent and `finance-policy` for policy constraints.

Use supporting source `payment-provider-docs` only for provider-owned fields, limits, and API behavior.

## Follow-Through Triggers

If subscription behavior changes, review product docs, subscription tests, customer-facing examples, and accepted carry-forward work in supporting source `work-board` when the current pass intentionally defers meaningful follow-through.
```

## Skill Opcional

```md
---
name: source-reconciliation
description: Reconcile conflicting repository, product, provider, policy, work-board, and design-system sources. Use when a task requires comparing multiple sources or classifying source divergence.
---

Start by identifying the disputed claim type: implementation behavior, product intent, external platform fact, policy, planned work, or design-system contract.

Use the supporting-source instruction to locate only the sources that can own that claim.

Return: sources checked, conflict classification, chosen authority, blocked verification, and follow-through needed.
```

## Fluxo Guiado por Prompt

Prompt:

```text
Change cancellation so customers keep access until the paid period ends, and update anything else that should move with it.
```

Fluxo provável:

1. O owner de subscriptions fornece o contrato local.
2. A intenção de produto vem de `product-workspace`.
3. Restrições de refund e invoice vêm de `finance-policy`.
4. Comportamento de provider é checado apenas se campos owned pelo provider ou comportamento de API mudarem.
5. O trigger revela docs, testes, exemplos e trabalho aceito de carry-forward.
6. Se as fontes divergirem, a skill de reconciliação se torna útil porque o workflow ficou maior do que uma consulta.

## Lição do Exemplo

Múltiplas fontes são saudáveis quando evitam confusão de autoridade.

Elas se tornam problemáticas quando a instruction força o agente a enumerar toda fonte antes de toda mudança.
