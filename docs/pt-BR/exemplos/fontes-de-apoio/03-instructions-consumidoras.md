# Instructions Consumidoras

## Nesta Página

- [Situação](#situação)
- [Owner de Adapter de Provider](#owner-de-adapter-de-provider)
- [Owner de UI](#owner-de-ui)
- [Overlay de Contrato Público](#overlay-de-contrato-público)
- [Lição do Exemplo](#lição-do-exemplo)

## Situação

Um repositório tem uma instruction de fontes de apoio no owner raiz.

Agora owners e overlays precisam consumir essas fontes sem repetir o mapa inteiro de fontes.

## Owner de Adapter de Provider

```md
---
applyTo: "src/adapters/payment-provider/**"
---

# Payment Provider Adapter

Keep provider-specific behavior isolated in this adapter.

Before changing provider-owned fields, auth behavior, idempotency, rate limits, or error semantics, use supporting source `payment-provider-docs`.

If provider docs are unavailable, do not introduce behavior that depends on unverified provider support.
```

Isso é guidance local, não follow-through.

A mudança atual estaria errada se inventasse comportamento de provider sem suporte.

## Owner de UI

```md
---
applyTo: "src/ui/**"
---

# UI Layer

Prefer existing local components and design tokens.

Use supporting source `design-system` when changing shared component behavior, accessibility states, token usage, or visual interaction patterns.

For ordinary local layout fixes, follow nearby code first. Do not consult the design system unless it could change the decision.
```

Isso mostra uso de fonte só para aprofundamento.

A fonte está disponível, mas deve ser consultada apenas quando puder afetar a claim atual.

## Overlay de Contrato Público

```md
---
applyTo: "src/**"
---

# Public Contract Overlay

If a change affects public API behavior, emitted events, customer-visible errors, or documented response semantics, review the relevant tests and docs before treating the change as complete.

Use supporting source `product-workspace` only for product intent, and `payment-provider-docs` only for provider-owned facts.

If the change reveals broader source divergence, use the repository's source reconciliation workflow instead of resolving it ad hoc.
```

Isso é uma concern transversal porque comportamento de contrato público pode aparecer em vários owners.

O overlay referencia fontes por tipo de claim, não porque toda mudança de contrato público deva consultar todas as fontes.

## Lição do Exemplo

Instructions consumidoras devem responder:

- que contrato local se aplica aqui
- quando evidência de fonte poderia mudar a decisão
- qual ID de fonte possui a claim relevante
- que fallback mantém a mudança segura

Elas não devem copiar a entrada inteira da fonte.
