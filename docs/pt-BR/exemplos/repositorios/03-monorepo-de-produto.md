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

## Um Mapa de Ownership Realista

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

## Por Que Este Mapa É Realista

- `apps/general` dá uma base comum para apps implantáveis
- `apps/admin/` ganha um nó mais estreito porque superfícies admin normalmente têm expectativas mais fortes de autorização e operação
- `packages/contracts/` ganha um nó dedicado porque contratos compartilhados criam blast radius grande em consumidores
- `packages/auth/` ganha um nó dedicado porque comportamento de auth é sensível de segurança
- `infra/terraform/` ganha um nó dedicado porque mudanças de infraestrutura são de alto impacto e alto risco
- `docs/runbooks/` é explícito porque documentação operacional é uma superfície owned real

O que intencionalmente não é mapeado:

- `apps/web/` e `apps/api/` não ganham nós próprios a menos que realmente desviem de `apps/general`
- `packages/ui/` e `packages/analytics/` ficam sob ownership mais ampla até provarem que precisam de guidance local
- `infra/ci/` fica sob prática operacional mais ampla até virar uma área de fricção real
- `docs/product/` e `docs/architecture/` dependem de prática mais ampla de docs e de follow-through

Isto é muito mais sustentável do que tentar espelhar o monorepo inteiro com instructions locais.

## Situações Guiadas por Prompt

### Mudar Um Contrato Compartilhado em `packages/contracts/`

Prompt de exemplo:

```text
Add an optional `customerTier` field to the shared order summary contract and update impacted consumers, tests, and docs.
```

Contexto provável de instructions:

- `packages/contracts/general`
- overlay de testing-quality
- overlay de observability se o campo afetar eventos ou diagnósticos operacionais

Como a arquitetura molda o processo:

1. O nó de contracts mantém o foco em disciplina de schema compartilhado.
2. A prompt naturalmente puxa o impacto em consumidores.
3. O follow-through faz a ponte entre mudança de package compartilhado, apps consumidoras e docs sem criar um nó para cada consumidor.

Follow-through provável:

- consumidores em `apps/web`, `apps/admin` e `apps/api`
- testes de consumidores do contrato
- docs se o campo for externamente visível

### Atualizar Comportamento de Auth em `packages/auth/`

Prompt de exemplo:

```text
Tighten refresh-token reuse detection in the shared auth package and update any tests, runbooks, or app integrations that should move with it.
```

Contexto provável de instructions:

- `packages/auth/security`
- overlay de testing-quality
- overlay de observability se eventos ou diagnósticos de auth mudarem

Como a arquitetura molda o processo:

1. O nó de auth enquadra a mudança como package sensível de segurança.
2. O overlay de observability mantém telemetria e diagnósticos visíveis.
3. O follow-through aponta para integrações e runbooks sem transformar cada consumidor de auth em nó dedicado.

Follow-through provável:

- apps consumidoras
- testes de auth
- runbooks
- docs de produto se o comportamento de sign-in mudar

### Mudar Comportamento de Terraform em `infra/terraform/`

Prompt de exemplo:

```text
Update the Terraform module so queue alerts are created by default in production only. Adjust docs and safety checks as needed.
```

Contexto provável de instructions:

- `infra/terraform/safety`
- overlay de observability

Como a arquitetura molda o processo:

1. O nó de Terraform enquadra a mudança como alteração de infraestrutura sensível.
2. O overlay de observability mantém alerta e monitoramento em vista.
3. O follow-through captura runbooks e docs de ambiente sem exigir um nó para cada pasta de infra.

Follow-through provável:

- runbooks
- docs de ambiente
- checks de validação ou drift
- revisão de ownership de alertas e dashboards

## Takeaway de Ensino

Este monorepo escala com a arquitetura porque mapeia apenas os boundaries de decisão que realmente importam:

- comportamento amplo de apps
- packages compartilhados de alto risco
- infraestrutura de alto risco
- docs operacionais

Isso mantém a árvore entendível mesmo quando o repositório é grande.
