# Monorepo de Produto

## Estrutura do Repositório

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

## Ownership Tree Saudável

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

## Por Que Isto É Bem Implementado

- apps, packages compartilhados, docs e infra são superfícies separadas de ownership
- admin e auth são owners mais estreitos porque carregam expectativas especiais de acesso e segurança
- contracts são owners de packages compartilhados, em vez de serem duplicados em cada app
- infra tem sua própria área de ownership, em vez de ser tratada como detalhe do código de aplicação

## Situações do Cotidiano

### Mudando Um Contrato Compartilhado em `packages/contracts/`

Contexto provável de instructions:

- `packages/general`
- `packages/contracts/general`
- overlay de testing-quality
- overlay de code-docs-consistency

Follow-through provável:

- consumidores em `apps/web`, `apps/admin` e `apps/api`
- docs
- testes

### Atualizando Comportamento de Auth em `packages/auth/`

Contexto provável de instructions:

- `packages/general`
- `packages/auth/security`
- overlay de testing-quality
- overlay de observability se eventos ou diagnósticos de auth mudarem

Follow-through provável:

- apps consumidoras
- testes de login e sessão
- runbooks
- docs de produto se o comportamento de sign-in mudar

### Mudando Regras de CI em `infra/ci/`

Contexto provável de instructions:

- `infra/general`
- `infra/ci/reliability`

Follow-through provável:

- docs de desenvolvimento
- exemplos de pipeline
- workflows que assumem o comportamento antigo de CI

### Atualizando Admin UI em `apps/admin/`

Contexto provável de instructions:

- `apps/general`
- `apps/admin/authorization`
- overlay de testing-quality
- overlay de code-docs-consistency se docs de admin mudarem

Follow-through provável:

- testes de admin
- auth ou contracts se o comportamento depender de packages compartilhados
- docs e runbooks se o comportamento operacional mudar

## Takeaway de Ensino

Este repositório escala porque a ownership tree espelha os verdadeiros boundaries de decisão do monorepo:

- apps implantáveis
- packages compartilhados
- docs
- infraestrutura

Isso torna o blast radius de mudanças compartilhadas mais fácil de entender, sem sobrecarregar um único arquivo monolítico de instruções do monorepo.
