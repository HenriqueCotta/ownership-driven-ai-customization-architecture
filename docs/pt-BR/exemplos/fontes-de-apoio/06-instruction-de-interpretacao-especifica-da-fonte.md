# Instruction de Interpretação Específica da Fonte

## Nesta Página

- [Situação](#situação)
- [Default Preferido](#default-preferido)
- [Quando a Instruction Extra Vale a Pena](#quando-a-instruction-extra-vale-a-pena)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Entrada de Fonte de Apoio](#entrada-de-fonte-de-apoio)
- [Instruction de Interpretação Específica da Fonte](#instruction-de-interpretação-específica-da-fonte-1)
- [O Que Fica Fora](#o-que-fica-fora)
- [Lição do Exemplo](#lição-do-exemplo)

## Situação

Um repositório usa um board de trabalho para acompanhar trabalho planejado, follow-through adiado, coordenação de release e follow-ups aceitos.

A instruction de fontes de apoio já tem uma entrada compacta `work-board`.

Essa entrada basta para a maioria das tarefas.

O time também tem algumas regras owned pelo repo sobre como interpretar o estado do board. Essas regras são importantes, mas detalhadas demais para o mapa central de fontes.

## Default Preferido

Evite criar uma instruction por fonte.

A maioria das fontes deve continuar como entradas compactas:

```md
## work-board

Where: board `checkout-work`
Access: project-management MCP, if available.
Use for: planned work, accepted follow-ups, and explicit carry-forward.
Do not use for: current behavior unless linked to merged code, tests, or accepted docs.
If unavailable: do not invent board state; surface missing planning context when it could change the result.
```

Isso mantém o mapa de fontes fácil de escanear.

## Quando a Instruction Extra Vale a Pena

Crie uma instruction de interpretação específica por fonte apenas quando a fonte tiver policy de interpretação owned pelo repo que guidance de fonte mais leve não consegue carregar com segurança, e o valor dessa policy justificar contexto always-on.

Esse último ponto importa.

As path-specific instructions atuais roteiam por path de arquivo. Se a interpretação do board pode se aplicar em qualquer lugar do repositório, a instruction normalmente precisa de `applyTo: "**"`, o que significa que ela pode ficar em contexto sempre que a surface suportar instructions compatíveis.

## Estrutura do Repositório

```text
<repository-root>/
  .github/
    copilot-instructions.md
    instructions/
      ownership/
        repository/
          supporting-sources.instructions.md
          work-board.instructions.md
      overlays/
```

## Entrada de Fonte de Apoio

```md
## work-board

Where: board `checkout-work`
Access: project-management MCP, if available.
Use for: planned work, accepted follow-ups, and explicit carry-forward.
Do not use for: current behavior unless linked to merged code, tests, or accepted docs.
Details: use `ownership/repository/work-board.instructions.md` only when board interpretation could change the decision.
```

## Instruction de Interpretação Específica da Fonte

```md
---
applyTo: "**"
---

# Work Board Interpretation

Use this instruction only when the task involves planned work, deferred follow-through, issue status, release coordination, or board-backed decisions.

The board owns planning state and explicit carry-forward. It does not prove current implementation behavior unless linked to merged code, tests, or accepted docs.

If board state conflicts with code, tests, or accepted docs, classify the disputed claim first. Code and tests own current implementation behavior. Accepted docs own documented behavior. The board owns planned or deferred work.

Do not create, move, close, or rewrite board items unless the user asks for board changes or the repository closure policy requires explicit carry-forward.
```

## O Que Fica Fora

Não coloque operações exatas do board nesta instruction.

Mudanças operacionais no board pertencem a uma superfície procedural explícita.

## Lição do Exemplo

Uma instruction de interpretação específica por fonte é útil quando o repositório precisa de policy durável de interpretação para uma fonte.

Ela não é o formato default de fonte.

Use com cuidado porque instructions repo-wide de interpretação específica por fonte costumam ser contexto always-on.
