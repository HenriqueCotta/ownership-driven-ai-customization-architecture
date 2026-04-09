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

## Um Mapa de Ownership Realista

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        routes/
          orders.ts/
            contract.instructions.md
            framework.instructions.md
        services/
          billing/
            domain.instructions.md
        contracts/
          general.instructions.md
        config/
          general.instructions.md
      docs/
        api/
          general.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      operability/
        observability.instructions.md
```

## Por Que Este Mapa É Realista

- `src/general` carrega as expectativas amplas de backend do serviço
- `src/routes/orders.ts/` ganha um nó próprio porque combina preocupação de contrato público com preocupação de framework de rota
- `src/services/billing/` ganha um nó mais estreito porque lógica financeira normalmente merece guidance de domínio mais forte
- `src/contracts/` e `src/config/` são owners separados porque mudanças de contrato e mudanças de config têm blast radius downstream claro
- `docs/api/` é explícito porque documentação de endpoint é uma superfície owned de verdade

Igualmente importante, este mapa é seletivo:

- `routes/health.ts` não ganha nó próprio
- `services/orders/` não ganha nó próprio
- `tests/` não ganha um nó separado de ownership aqui
- `docs/runbooks/` fica sob follow-through operacional mais amplo, em vez de ganhar um branch próprio

É assim que um repositório maduro normalmente se parece. A maior parte dos paths vive bem com owners amplos, overlays e follow-through.

## Situações Guiadas por Prompt

### Adicionar Um Campo de Resposta em `src/routes/orders.ts`

Prompt de exemplo:

```text
Add `customerTier` to the orders response. Update the route, contract, tests, and docs if needed.
```

Contexto provável de instructions:

- `src/general`
- `src/routes/orders.ts/contract`
- `src/routes/orders.ts/framework`
- `src/contracts/general`
- overlay de testing-quality
- overlay de observability se a resposta afetar logs, métricas ou dashboards

Como a arquitetura molda o processo:

1. O nó específico da rota puxa a atenção para semântica de resposta e mapeamento HTTP.
2. O owner de contratos mantém o schema compartilhado honesto.
3. O overlay de testing lembra o Copilot de atualizar cobertura de rota e contrato.
4. O follow-through traz `docs/api/` para o escopo sem exigir um overlay de docs.

Follow-through provável:

- testes de rota
- testes de contrato
- docs do endpoint
- revisão de telemetria se consumidores downstream dependerem do campo

### Mudar Regras de Billing em `src/services/billing/issue-invoice.ts`

Prompt de exemplo:

```text
Change invoice issuance so failed retries are marked as recoverable instead of terminal. Update anything else that should move with that rule.
```

Contexto provável de instructions:

- `src/general`
- `src/services/billing/domain`
- overlay de testing-quality
- overlay de observability se a classificação de falha mudar sinais operacionais

Como a arquitetura molda o processo:

1. O nó de billing mantém o modelo focado em semântica de domínio, e não em mecânica de rota.
2. O overlay de observability captura o lado operacional da mudança.
3. O follow-through aponta para docs financeiros, testes e runbooks sem criar um nó para cada superfície.

Follow-through provável:

- testes de billing
- docs ou runbooks financeiros
- alertas e dashboards se a classificação de erro mudar
- contratos se a semântica pública mudar

### Mudar Precedência de Config em `src/config/load-config.ts`

Prompt de exemplo:

```text
Make environment variables override file-based config only for production and staging. Update the surrounding docs and checks.
```

Contexto provável de instructions:

- `src/general`
- `src/config/general`
- overlay de testing-quality

Como a arquitetura molda o processo:

1. O owner de config enquadra a mudança como semântica de configuração, e não só como edição de código.
2. O overlay de testing empurra o trabalho para cobertura de cenários de precedência.
3. O follow-through traz docs e guidance operacional para perto mesmo sem nós próprios para cada subárea.

Follow-through provável:

- testes de precedência
- docs de config de exemplo
- runbooks de deploy ou operação
- diagnósticos de startup se o comportamento novo mudar expectativas de suporte

## Takeaway de Ensino

Este repositório funciona bem com a arquitetura porque o mapa é seletivo:

- comportamento amplo de código fica em `src/general`
- só exceções locais de alto valor ganham nós mais estreitos
- overlays continuam pequenos
- trabalho downstream é tratado por follow-through, e não por uma ownership tree gigante
