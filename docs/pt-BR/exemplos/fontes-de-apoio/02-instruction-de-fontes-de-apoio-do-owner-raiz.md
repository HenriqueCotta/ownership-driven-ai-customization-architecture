# Instruction de Fontes de Apoio do Owner Raiz

## Situação

Um repositório usa várias fontes:

- docs locais
- um workspace privado de produto
- um board de trabalho
- um repositório de design system
- documentação atual de provider

O time quer um lugar que diga aos agentes onde essas fontes vivem e como tratar conflitos, mas não quer um schema rígido.

## Estrutura do Repositório

```text
<repository-root>/
  .github/
    copilot-instructions.md
    instructions/
      ownership/
        repository/
          supporting-sources.instructions.md
      overlays/
  docs/
  src/
```

A instruction de fontes se aplica globalmente porque guidance de fontes pode ser útil a partir de vários owners.

Ela vive em `ownership/repository/` porque o owner raiz do repositório possui a policy repo-wide de fontes.

Ela continua sendo evidência auxiliar, não outra camada estrutural nem um registro de todo documento.

## Ponte no Baseline

```md
# Repository Baseline

Start from the narrowest relevant owner instruction and apply overlays only when their concern is affected.

When deeper or live evidence could change a decision, use `.github/instructions/ownership/repository/supporting-sources.instructions.md`.

Consult only the source entries that could affect the current claim. Do not list, open, or check every source just because the source instruction exists.
```

## Instruction de Fontes de Apoio

```md
---
applyTo: "**"
---

# Supporting Sources

These entries are not a required schema. They are stable source IDs the repository uses when "check the docs" would be too vague.

Use supporting sources only when they could change the decision, explain a conflict, or prevent unsafe guessing.

## Conflict Handling

When sources diverge, classify the disputed claim first: implementation behavior, product intent, external platform fact, policy, planned work, or design-system contract.

Prefer the source that owns that claim. If the owning source is unavailable and the missing fact could change the result, treat that part as verification-blocked.

Do not let external provider docs override repository product intent, policy constraints, or local security rules. Do not let local mirrors override current provider facts.

## repo-docs

Where: `docs/`
Use for: repository-owned architecture notes, rationale, and local examples.

## product-workspace

Where: product workspace `checkout-product-notes`
Access: product-docs MCP, if available.
Use for: checkout product intent and accepted product decisions.
If unavailable: preserve existing customer-visible behavior and surface missing product intent when it could change the result.

## work-board

Where: board `checkout-work`
Access: project-management MCP, if available.
Use for: planned work, accepted follow-ups, and explicit carry-forward.
Do not use for: current behavior unless linked to merged code or accepted docs.

## design-system

Where: `../design-system/` or `org/design-system`
Access: local checkout first; source-control MCP if needed.
Use for: shared UI component contracts, tokens, accessibility states, and visual interaction rules.
If unavailable: avoid inventing new component behavior; follow existing local UI patterns.

## payment-provider-docs

Where: `https://provider.example/docs`
Access: web or provider-docs MCP, if available.
Use for: provider-owned fields, limits, auth, idempotency, errors, and API behavior.
Freshness: verify current docs before changing provider-specific behavior.
If unavailable: do not introduce behavior that depends on unverified provider support.
If it conflicts: current provider docs own provider facts; local notes may be stale.
```

## Lição do Exemplo

As entradas não usam todas os mesmos campos.

Isso é intencional.

A parte estável é o ID da fonte e a guidance de decisão. O formato Markdown continua pertencendo ao repositório.
