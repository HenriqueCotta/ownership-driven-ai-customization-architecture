# Aplicação Web de Produto

## Estrutura do Repositório

```text
repo/
  src/
    app/
      routes/
        dashboard/
        settings/
      layout/
    features/
      checkout/
      search/
      notifications/
    design-system/
      components/
      tokens/
    state/
      auth/
      cart/
    lib/
      analytics/
      api-client/
  tests/
    e2e/
    integration/
    unit/
  docs/
    ux/
    product/
```

## Ownership Tree Saudável

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        app/
          general.instructions.md
          routes/
            general.instructions.md
        features/
          general.instructions.md
          checkout/
            behavior.instructions.md
          search/
            behavior.instructions.md
        design-system/
          general.instructions.md
          tokens/
            consistency.instructions.md
        state/
          general.instructions.md
          auth/
            security.instructions.md
        lib/
          analytics/
            instrumentation.instructions.md
      tests/
        general.instructions.md
      docs/
        general.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      consistency/
        code-docs-consistency.instructions.md
```

## Por Que Isto É Bem Implementado

- app shell, features, design system, estado e bibliotecas compartilhadas são boundaries separados de ownership
- checkout e search são owners de feature mais estreitos porque o comportamento realmente difere
- auth state é um owner mais estreito porque carrega expectativas sensíveis de segurança
- code-docs consistency é overlay porque docs de produto e UX atravessam vários owners do código

## Situações do Cotidiano

### Atualizando Validação de Checkout em `src/features/checkout/`

Contexto provável de instructions:

- `src/general`
- `src/features/general`
- `src/features/checkout/behavior`
- overlay de testing-quality
- overlay de code-docs-consistency se a mensagem para usuário mudar

Follow-through provável:

- testes unitários e de integração
- docs de checkout ou referências de copy/UX
- analytics se eventos de conversão mudarem

### Mudando Tokens de Design em `src/design-system/tokens/`

Contexto provável de instructions:

- `src/general`
- `src/design-system/general`
- `src/design-system/tokens/consistency`
- overlay de code-docs-consistency se houver docs dos tokens

Follow-through provável:

- testes visuais
- docs de componentes
- screenshots ou specs de referência

### Ajustando Auth State em `src/state/auth/`

Contexto provável de instructions:

- `src/general`
- `src/state/general`
- `src/state/auth/security`
- overlay de testing-quality

Follow-through provável:

- testes de autenticação
- guards de rota
- docs de sessão ou login
- analytics se o funnel de login mudar

### Editando `docs/ux/search.md`

Contexto provável de instructions:

- `docs/general`
- overlay de code-docs-consistency se código e docs precisarem ficar alinhados

Follow-through provável:

- verificar o comportamento atual da feature
- verificar screenshots ou exemplos
- verificar se os testes ainda codificam o comportamento descrito

## Takeaway de Ensino

Este repositório funciona bem com a arquitetura porque o ownership segue seams reais de produto e engenharia:

- app shell
- features
- design system
- estado
- bibliotecas compartilhadas

Isso impede que trabalho de UI, design system e comportamento de produto colapsem em uma única instruction gigante de frontend.
