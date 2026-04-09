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

## Um Mapa de Ownership Realista

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        features/
          checkout/
            behavior.instructions.md
        design-system/
          tokens/
            consistency.instructions.md
        state/
          auth/
            security.instructions.md
      docs/
        ux/
          general.instructions.md
    overlays/
      quality/
        testing-quality.instructions.md
      consistency/
        code-docs-consistency.instructions.md
```

## Por Que Este Mapa É Realista

- `src/general` carrega expectativas amplas de frontend
- `features/checkout/` ganha um nó local porque checkout costuma ser comportamento crítico e muito visível para o usuário
- `design-system/tokens/` ganha um nó local porque mudanças de token têm blast radius grande de consistência
- `state/auth/` ganha um nó local porque auth state carrega expectativas sensíveis de segurança
- `docs/ux/` é explícito porque documentação de UX é uma superfície owned real

O que intencionalmente fica de fora:

- `features/search/` e `features/notifications/` ficam sob `src/general`
- `app/routes/` não ganha owner local a menos que o shell de rotas tenha regras próprias
- `tests/` continua sendo guiado principalmente por overlays e follow-through
- `lib/api-client/` e `state/cart/` ficam sob guidance mais ampla até provarem que precisam de regras locais

Isso é muito mais realista do que dar instructions para cada pasta de feature.

## Situações Guiadas por Prompt

### Atualizar Validação de Checkout em `src/features/checkout/`

Prompt de exemplo:

```text
Update checkout validation so gift cards cannot be combined with subscription purchases. Adjust tests, user messaging, and analytics if needed.
```

Contexto provável de instructions:

- `src/general`
- `src/features/checkout/behavior`
- overlay de testing-quality
- overlay de code-docs-consistency se copy ou docs de usuário mudarem

Como a arquitetura molda o processo:

1. O nó de checkout mantém o foco em regra de produto e comportamento.
2. O overlay de testing empurra atualizações de cobertura.
3. O overlay de docs-consistency lembra que copy e docs podem precisar andar junto com o código.

Follow-through provável:

- testes unitários e de integração
- docs de checkout ou referências de copy/UX
- analytics se eventos de conversão mudarem

### Mudar Tokens de Design em `src/design-system/tokens/`

Prompt de exemplo:

```text
Rename the old warning color token set to the new semantic alert tokens and update downstream references.
```

Contexto provável de instructions:

- `src/general`
- `src/design-system/tokens/consistency`
- overlay de code-docs-consistency

Como a arquitetura molda o processo:

1. O nó de tokens enquadra a mudança como mudança de consistência, não só como rename.
2. O overlay ajuda a mover docs e referências junto com o código.
3. O follow-through captura screenshots, docs de tokens e snapshots sem precisar de um nó para cada componente.

Follow-through provável:

- docs de tokens
- testes visuais ou snapshots
- referências em componentes que ainda usam os nomes antigos

### Ajustar Auth State em `src/state/auth/`

Prompt de exemplo:

```text
Persist MFA enrollment state across refresh, but keep cache invalidation conservative. Update tests and any related docs.
```

Contexto provável de instructions:

- `src/general`
- `src/state/auth/security`
- overlay de testing-quality

Como a arquitetura molda o processo:

1. O nó de auth empurra o modelo para segurança e semântica de sessão.
2. O overlay de testing puxa cobertura de transições de estado.
3. O follow-through captura guards de rota, fluxo de login e docs sem transformar tudo em nós locais.

Follow-through provável:

- testes de auth
- comportamento de guards de rota
- docs de login ou sessão
- analytics apenas se o fluxo visível para o usuário mudar materialmente

## Takeaway de Ensino

Este repositório funciona bem com a arquitetura porque evita a armadilha de transformar toda feature em owner de instruction:

- só paths de alto valor ou alto risco ganham nós locais
- overlays continuam pequenos e intencionais
- a maior parte do trabalho ainda passa por poucos owners amplos
- o follow-through cuida das superfícies secundárias sem inflar a árvore
