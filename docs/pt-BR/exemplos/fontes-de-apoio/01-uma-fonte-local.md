# Uma Fonte Local

## Situação

Um serviço pequeno mantém notas de comportamento de produto visíveis ao cliente em `docs/product/`.

O repositório também tem outros docs em `docs/`, mas eles não fazem parte desta fonte.

Não há sistemas privados, docs vivas de provider nem método especial de acesso.

O time quer que agentes saibam quando `docs/product/` deve ser usado como evidência de intenção de produto, sem fazer toda tarefa abrir a pasta de docs.

## Estrutura do Repositório

```text
<repository-root>/
  .github/
    copilot-instructions.md
    instructions/
      ownership/
        repository/
          supporting-sources.instructions.md
          docs/
            general.instructions.md
          src/
            notifications/
              general.instructions.md
  docs/
    product/
      notifications.md
    runbooks/
      deploy.md
  src/
    notifications/
```

O owner `docs/` e a fonte `product-docs` têm trabalhos diferentes.

O owner `docs/` explica como editar arquivos de documentação.

A fonte `product-docs` diz a outras instructions quando `docs/product/` é evidência de intenção de produto.

## Instruction de Fonte de Apoio

```md
---
applyTo: "**"
---

# Supporting Sources

Use these sources only when they could change the decision.

Do not open docs by reflex.

## product-docs

Where: `docs/product/`
Scope: product behavior notes only; this does not mean every file under `docs/`.
Use for: customer-visible behavior, product wording, and product intent.
Do not use for: deployment runbooks, architecture notes, or current implementation behavior.
If unavailable: preserve existing behavior and surface the missing product context when it could change the result.
If it conflicts: product docs own intended customer semantics, but implementation and tests may reveal drift.
```

## Instruction Consumidora

```md
---
applyTo: "src/notifications/**"
---

# Customer Notifications

Notification behavior should stay understandable from the customer's point of view.

If a change alters customer-visible wording, delivery timing, opt-out behavior, or customer-facing defaults, use supporting source `product-docs` before treating the change as complete.

Do not consult `product-docs` for internal refactors that preserve customer-visible behavior.
```

## Instruction do Owner de Docs

```md
---
applyTo: "docs/**"
---

# Documentation

Keep docs concise, current, and organized by reader need.

When editing `docs/product/`, preserve product intent and customer-facing semantics unless the task explicitly changes them.

This owner instruction governs how documentation files are edited. It does not make all docs a supporting source for code changes.
```

## Dúvidas Comuns

### A Fonte é `docs/` Ou `docs/product/`?

Neste exemplo, a fonte é `docs/product/`.

Essa fonte mais estreita é intencional.

O repositório pode conter runbooks, notas de arquitetura, docs de onboarding e notas de release em `docs/`. Tratar todo `docs/` como uma única fonte faria o agente adivinhar quais docs possuem intenção de produto.

### Uma Instruction do Owner de Docs Conflita Com Uma Fonte de Docs?

Não.

Elas respondem perguntas diferentes.

A instruction do owner `docs/` fica ativa quando o agente edita paths de documentação.

A fonte `product-docs` é consultada por outra instruction quando evidência de produto pode mudar uma decisão.

### Por Que Não Só Dizer "Verifique Os Docs"?

"Verifique os docs" é vago.

Isso não diz quais docs importam, quando consultá-los, que claim eles possuem, nem o que fazer se estiverem ausentes ou stale.

Uma pequena entrada de fonte dá estrutura suficiente ao agente sem criar um registro grande.

### Quando A Fonte Deve Ser Usada?

Use `product-docs` quando uma mudança puder alterar o que clientes veem, entendem, recebem, aceitam ou recusam.

Não use para limpeza interna, formatação, updates de dependência ou testes que preservam comportamento visível ao cliente.

### Uma Skill é Necessária?

Não.

A fonte é local e a consulta é simples.

Uma skill só ficaria útil se a consulta de fontes virasse um workflow repetível, como comparar vários documentos de produto, reconciliar docs stale ou preparar um relatório estruturado de impacto em produto.

## Por Que Isso Basta

A fonte é local, estreita e estável.

A entrada de fonte nomeia a pasta exata que possui a claim relevante.

A instruction consumidora explica quando a fonte importa.

A instruction do owner de docs continua livre para governar edições de documentação sem virar um mapa de fontes.
