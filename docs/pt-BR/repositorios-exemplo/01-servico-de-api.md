# Serviço de API

## Estrutura do Repositório

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

## Ownership Tree Saudável

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

## Por Que Isto É Bem Implementado

- handlers de rota, serviços de domínio, contratos, config, testes e docs são superfícies diferentes de ownership
- comportamento de admin é tratado como owner mais estreito, e não como uma preocupação global vaga
- testing e observability são overlays porque atravessam várias áreas de ownership
- docs continuam sendo seu próprio owner em vez de virar overlay do código-fonte

## Situações do Cotidiano

### Adicionando Um Novo Campo de Resposta em `src/routes/orders.ts`

Contexto provável de instructions:

- `src/general`
- `src/routes/general`
- `src/routes/orders.ts/contract`
- `src/routes/orders.ts/framework`
- overlay de testing-quality
- overlay de observability se o comportamento operacional mudar

Follow-through provável:

- testes de rota
- testes de contrato
- docs do endpoint
- telemetria se os campos afetarem logs ou dashboards

### Mudando Regras de Billing em `src/services/billing/issue-invoice.ts`

Contexto provável de instructions:

- `src/general`
- `src/services/general`
- `src/services/billing/domain`
- overlay de testing-quality
- overlay de observability se sinais operacionais mudarem

Follow-through provável:

- testes de billing
- docs de invoices ou runbooks financeiros
- contratos se a semântica pública mudar

### Mudando a Precedência de Config em `src/config/load-config.ts`

Contexto provável de instructions:

- `src/general`
- `src/config/general`
- overlay de testing-quality

Follow-through provável:

- arquivos de config de exemplo
- docs
- runbooks de deploy ou operação
- testes que codificam o comportamento de config

### Editando `docs/api/orders.md`

Contexto provável de instructions:

- `docs/general`

Follow-through provável:

- verificar a implementação atual
- verificar se os testes ainda sustentam a afirmação
- verificar se os contratos referenciados estão atuais

## Takeaway de Ensino

Este repositório é fácil de raciocinar porque a ownership tree segue os seams reais do sistema:

- transporte
- domínio
- contratos
- config
- docs

Isso mantém as edições cotidianas locais na maior parte do tempo, sem esconder consequências downstream.
