# Exemplos

Público: mantenedores que querem aprender a arquitetura por cenários concretos em vez de começar pela teoria.
Objetivo: fornecer exemplos curtos e linkáveis que ensinem classificação, follow-through e layout da ownership tree sem obrigar o leitor a passar por um arquivo longo demais.

## Nesta Página

- [Como Usar Esta Pasta](#como-usar-esta-pasta)
- [Classificação](#classificação)
- [Follow-Through](#follow-through)
- [Ownership Tree](#ownership-tree)
- [Arquétipos de Repositório](#arquétipos-de-repositório)
- [Checklist Rápido de Revisão](#checklist-rápido-de-revisão)

## Como Usar Esta Pasta

Leia os exemplos por tema:

- `classification/`
  - como distinguir ownership de overlays
- `follow-through/`
  - como a lógica downstream de revisão e atualização deve funcionar
- `ownership-tree/`
  - como a ownership tree deve aparecer no disco
- `repositorios/`
  - como a arquitetura aparece em arquétipos de repositório mais realistas e em prompts do dia a dia

Se esta for sua primeira leitura, siga esta ordem:

1. [Um Caminho, Um Owner](./classification/01-um-caminho-um-owner.md)
2. [Um Overlay de Verdade](./classification/02-um-overlay-de-verdade.md)
3. [Owner Mais Estreito vs Overlay](./classification/03-owner-mais-estreito-vs-overlay.md)
4. [Mudança de Contrato](./follow-through/01-mudanca-de-contrato.md)
5. [Mudança de Configuração](./follow-through/02-mudanca-de-configuracao.md)
6. [Um Nó de Arquivo com Dois Arquivos de Instruction](./ownership-tree/01-um-no-de-arquivo-com-dois-arquivos-de-instruction.md)
7. [Filhos Mistos sob um Mesmo Pai](./ownership-tree/02-filhos-mistos-sob-um-mesmo-pai.md)

## Classificação

- [Um Caminho, Um Owner](./classification/01-um-caminho-um-owner.md)
- [Um Overlay de Verdade](./classification/02-um-overlay-de-verdade.md)
- [Owner Mais Estreito vs Overlay](./classification/03-owner-mais-estreito-vs-overlay.md)

## Follow-Through

- [Mudança de Contrato](./follow-through/01-mudanca-de-contrato.md)
- [Mudança de Configuração](./follow-through/02-mudanca-de-configuracao.md)
- [Documentação como Seu Próprio Owner](./follow-through/03-documentacao-como-seu-proprio-owner.md)
- [Follow-Through de Board ou Task](./follow-through/04-follow-through-de-board-ou-task.md)
- [Nenhum Follow-Through Necessário](./follow-through/05-nenhum-follow-through-necessario.md)

## Ownership Tree

- [Um Nó de Arquivo com Dois Arquivos de Instruction](./ownership-tree/01-um-no-de-arquivo-com-dois-arquivos-de-instruction.md)
- [Filhos Mistos sob um Mesmo Pai](./ownership-tree/02-filhos-mistos-sob-um-mesmo-pai.md)
- [Por Que uma Gramática de Pastas é Mais Fácil de Ensinar](./ownership-tree/03-por-que-uma-gramatica-de-pastas-e-mais-facil-de-ensinar.md)

## Arquétipos de Repositório

- [Índice de Arquétipos de Repositório](./repositorios/README.md)
- [Serviço de API](./repositorios/01-servico-de-api.md)
- [Aplicação Web de Produto](./repositorios/02-aplicacao-web-de-produto.md)
- [Monorepo de Produto](./repositorios/03-monorepo-de-produto.md)

## Checklist Rápido de Revisão

Depois de uma mudança relevante, pergunte:

1. Qual path é o owner primário deste arquivo?
2. Quais nós mais amplos ou mais estreitos da ownership tree também se aplicam?
3. Há aqui uma preocupação transversal real, ou estou rotulando ownership como overlay por engano?
4. Uma seção existente de `Follow-Through Triggers` já descreve o que mais pode ter ficado desatualizado?
5. Se não, essa guidance deveria ser adicionada a uma instruction existente em vez de criar um novo arquivo?
6. O trabalho downstream é pequeno o bastante para ser feito diretamente, ou ele justifica uma skill existente orientada a outcome?
7. Algum check exato e repetível ficaria mais claro como automação ou runbook?
8. Estou inventando uma nova camada de hints ou uma skill por trigger quando o mapa existente já é suficiente?
