# Follow-Through Triggers

Público: mantenedores que precisam modelar guidance downstream de revisão e atualização sem inventar camadas extras.  
Objetivo: explicar o que `Follow-Through Triggers` é, por que existe e onde deve morar.

## Nesta Página

- [O Que Follow-Through Triggers É](#o-que-follow-through-triggers-é)
- [Por Que Existe](#por-que-existe)
- [Onde Mora](#onde-mora)
- [Triggers Típicos](#triggers-típicos)
- [O Que Não É](#o-que-não-é)
- [Documentos Relacionados](#documentos-relacionados)

## O Que Follow-Through Triggers É

`Follow-Through Triggers` descreve o que mais pode agora precisar de revisão depois de uma mudança relevante.

É uma seção comportamental dentro de uma instruction.

Não é um tipo de arquivo separado nem outra camada arquitetural.

## Por Que Existe

Muitas mudanças importantes têm consequências secundárias:

- docs podem ter ficado desatualizadas
- testes podem precisar de atualização
- configs podem precisar de revisão
- runbooks, dashboards ou workflows podem precisar de ajuste

O modelo torna essas consequências explícitas para que elas não dependam só do jeito como a prompt foi escrita ou da memória do time.

## Onde Mora

`Follow-Through Triggers` deve morar dentro da instruction que melhor entende a origem da mudança.

Posicionamento default:

- baseline
  - para regras downstream curtas e válidas para o repositório inteiro
- nó de ownership
  - quando o owner da origem entende melhor o blast radius
- overlay
  - apenas quando a regra downstream realmente é owned por aquela concern transversal

## Triggers Típicos

Exemplos típicos:

- um contrato público muda
  - revise consumers, docs e testes
- defaults de configuração mudam
  - revise pressupostos de rollout, docs e checks de runtime
- um comportamento muda em uma API pública
  - revise testes, docs e expectativas de tratamento de erro

## O Que Não É

`Follow-Through Triggers` não é:

- uma segunda ownership tree
- um motivo para criar novos arquivos de instruction por si só
- um substituto para CI, review ou testes

É um lembrete estruturado de trabalho downstream provável.

## Documentos Relacionados

- [Modelo Operacional](./modelo-operacional.md)
- [Ownership vs Overlay](./ownership-vs-overlay.md)
- [Regras de Decisão](../regras/regras-de-decisao.md)
- [Exemplos](../exemplos/README.md)
