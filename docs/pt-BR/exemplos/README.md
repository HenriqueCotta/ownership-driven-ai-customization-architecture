# Exemplos

Público: mantenedores que querem aprender a arquitetura por cenários concretos em vez de começar pela teoria.
Objetivo: fornecer exemplos curtos e linkáveis que ensinem classificação, follow-through e layout da ownership tree sem obrigar o leitor a passar por um arquivo longo demais.

## Nesta Página

- [Como Usar Esta Pasta](#como-usar-esta-pasta)
- [Classificação](#classificação)
- [Follow-Through](#follow-through)
- [Ownership Tree](#ownership-tree)
- [Fontes de Apoio](#fontes-de-apoio)
- [Arquétipos de Repositório](#arquétipos-de-repositório)
- [Checklist Rápido de Revisão](#checklist-rápido-de-revisão)

## Como Usar Esta Pasta

Leia os exemplos por tema:

- `classification/`
  - como distinguir ownership de overlays
- `follow-through/`
  - como a lógica downstream de follow-through deve funcionar
- `ownership-tree/`
  - como a ownership tree deve aparecer no disco
- `fontes-de-apoio/`
  - como guidance de fontes, instructions consumidoras, conflitos e workflows de fonte se encaixam
- `repositorios/`
  - como a arquitetura aparece em arquétipos de repositório mais realistas e em prompts do dia a dia

Se esta for sua primeira leitura, siga esta ordem:

1. [Um Caminho, Um Owner](./classification/01-um-caminho-um-owner.md)
2. [Um Overlay de Verdade](./classification/02-um-overlay-de-verdade.md)
3. [Owner Mais Estreito vs Overlay](./classification/03-owner-mais-estreito-vs-overlay.md)
4. [Mudança de Contrato](./follow-through/01-mudanca-de-contrato.md)
5. [Mudança de Configuração](./follow-through/02-mudanca-de-configuracao.md)
6. [Um Trigger Compartilhado Supera Cópias Locais Repetidas](./follow-through/06-um-trigger-compartilhado-supera-copias-locais-repetidas.md)
7. [Um Nó de Arquivo com Dois Arquivos de Instruction](./ownership-tree/01-um-no-de-arquivo-com-dois-arquivos-de-instruction.md)
8. [Cresça a Tree Só Quando o Owner Amplo Deixar de Ser Suficiente](./ownership-tree/04-cresca-a-tree-so-quando-o-owner-amplo-deixar-de-ser-suficiente.md)
9. [Instruction de Fontes de Apoio do Owner Raiz](./fontes-de-apoio/02-instruction-de-fontes-de-apoio-do-owner-raiz.md)
10. [Instructions Consumidoras](./fontes-de-apoio/03-instructions-consumidoras.md)

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
- [Um Trigger Compartilhado Supera Cópias Locais Repetidas](./follow-through/06-um-trigger-compartilhado-supera-copias-locais-repetidas.md)

## Ownership Tree

- [Um Nó de Arquivo com Dois Arquivos de Instruction](./ownership-tree/01-um-no-de-arquivo-com-dois-arquivos-de-instruction.md)
- [Filhos Mistos sob um Mesmo Pai](./ownership-tree/02-filhos-mistos-sob-um-mesmo-pai.md)
- [Por Que uma Gramática de Pastas é Mais Fácil de Ensinar](./ownership-tree/03-por-que-uma-gramatica-de-pastas-e-mais-facil-de-ensinar.md)
- [Cresça a Tree Só Quando o Owner Amplo Deixar de Ser Suficiente](./ownership-tree/04-cresca-a-tree-so-quando-o-owner-amplo-deixar-de-ser-suficiente.md)

## Fontes de Apoio

- [Índice de Exemplos de Fontes de Apoio](./fontes-de-apoio/README.md)
- [Uma Fonte Local](./fontes-de-apoio/01-uma-fonte-local.md)
- [Instruction de Fontes de Apoio do Owner Raiz](./fontes-de-apoio/02-instruction-de-fontes-de-apoio-do-owner-raiz.md)
- [Instructions Consumidoras](./fontes-de-apoio/03-instructions-consumidoras.md)
- [Múltiplas Fontes e Conflitos](./fontes-de-apoio/04-multiplas-fontes-e-conflitos.md)
- [Resumo Local Como Guarda de Segurança](./fontes-de-apoio/05-resumo-local-como-guarda-de-seguranca.md)
- [Instruction de Interpretação Específica da Fonte](./fontes-de-apoio/06-instruction-de-interpretacao-especifica-da-fonte.md)

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
5. Se não, essa guidance deveria ser adicionada a uma instruction mais ampla já existente em vez de ser copiada em vários lugares?
6. Esta instruction realmente precisa de um trigger, ou estou adicionando um por reflexo?
7. O trabalho downstream é pequeno o bastante para ser feito diretamente, ou ele justifica uma skill existente orientada a outcome?
8. Algum check exato e repetível ficaria mais claro como automação ou runbook?
9. Se evidência mais profunda ou viva importa, localização, acesso, fallback e conflito de fontes estão claros?
10. Estou inventando uma nova camada de hints, um registro de fontes ou uma skill por trigger quando o mapa existente já é suficiente?
11. Estou aprofundando a tree antes de o owner mais amplo realmente provar que não basta?
