# Ownership-Driven Architecture (ODA)

Público: mantenedores que estão desenhando um modelo escalável de personalização do Copilot para um ou vários repositórios.  
Objetivo: fornecer um portal de documentação que deixe a arquitetura fácil de aprender, consultar e reutilizar.

## O Que Esta Pasta Documenta

Esta pasta é agnóstica ao repositório.

Ela documenta uma arquitetura reutilizável para organizar:

- instruções gerais do repositório
- instructions baseadas em ownership por caminho
- overlays transversais
- skills reutilizáveis
- comportamento downstream de revisão e atualização

Nome formal:

- `Ownership-Driven Architecture`

Atalho operacional:

- `baseline + ownership tree + cross-cutting overlays`

## Nesta Página

- [O Que Esta Pasta Documenta](#o-que-esta-pasta-documenta)
- [Estrutura da Documentação](#estrutura-da-documentação)
- [Mapa da Documentação](#mapa-da-documentação)
- [Trilhas Sugeridas de Leitura](#trilhas-sugeridas-de-leitura)
- [Regras Centrais de Design](#regras-centrais-de-design)

## Estrutura da Documentação

Este conjunto de docs é organizado pela intenção de leitura:

- explicação
  - por que a arquitetura existe
- modelo
  - o que o sistema é e como suas partes se relacionam
- regras
  - as convenções e fronteiras de decisão consultadas durante o desenho do mapa
- how-to
  - como fazer rollout do modelo em um repositório real
- exemplos
  - como o modelo se comporta em situações concretas

Cada documento deve ter um trabalho principal.

Se uma página começa a repetir outra, normalmente ela deve linkar em vez de restatar.

## Mapa da Documentação

### Explicação

- [Por Que Esta Arquitetura](./por-que-esta-arquitetura.md)
  - caso de negócio, ganhos esperados, não-objetivos e alinhamento com padrões

### Modelo

- [Modelo Operacional](./modelo/modelo-operacional.md)
  - o vocabulário estrutural da arquitetura
- [Ownership vs Overlay](./modelo/ownership-vs-overlay.md)
  - a distinção conceitual mais importante do modelo
- [Follow-Through Triggers](./modelo/follow-through-triggers.md)
  - para que serve a guidance downstream de revisão e atualização

### Regras

- [Regras de Decisão](./regras/regras-de-decisao.md)
  - onde cada guidance deve morar e o que fazer quando a classificação estiver nebulosa
- [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md)
  - a gramática canônica no disco, as regras de nome e a política de atalho
- [Conflitos e Precedência de Instruções](./regras/conflitos-e-precedencia-de-instrucoes.md)
  - o que a plataforma garante com clareza e como evitar mapas ambíguos

### How-To

- [Playbook de Replicação](./playbook-de-replicacao.md)
  - como reproduzir a arquitetura em outro repositório

### Exemplos Trabalhados

- [Exemplos](./exemplos/README.md)
  - exemplos curtos por cenário e arquétipos de repositório na mesma pasta

## Trilhas Sugeridas de Leitura

Se este for seu primeiro contato com a arquitetura:

1. Leia este arquivo.
2. Leia [Por Que Esta Arquitetura](./por-que-esta-arquitetura.md).
3. Leia [Modelo Operacional](./modelo/modelo-operacional.md).
4. Leia [Ownership vs Overlay](./modelo/ownership-vs-overlay.md).
5. Leia [Follow-Through Triggers](./modelo/follow-through-triggers.md).
6. Leia [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md).
7. Leia [Exemplos](./exemplos/README.md).

Se você estiver desenhando um novo repositório:

1. Leia este arquivo.
2. Leia [Por Que Esta Arquitetura](./por-que-esta-arquitetura.md).
3. Leia [Modelo Operacional](./modelo/modelo-operacional.md).
4. Leia [Regras de Decisão](./regras/regras-de-decisao.md).
5. Leia [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md).
6. Leia [Playbook de Replicação](./playbook-de-replicacao.md).
7. Leia [Exemplos](./exemplos/README.md).

Se você estiver investigando ambiguidade ou conflito entre instructions:

1. Leia este arquivo.
2. Leia [Conflitos e Precedência de Instruções](./regras/conflitos-e-precedencia-de-instrucoes.md).
3. Leia [Ownership vs Overlay](./modelo/ownership-vs-overlay.md).
4. Leia [Follow-Through Triggers](./modelo/follow-through-triggers.md).
5. Leia [Exemplos](./exemplos/README.md).

## Regras Centrais de Design

- Comece por boundaries estáveis de ownership, não por temas abstratos.
- Represente boundaries de ownership com uma tree fácil de ler antes de tentar otimizá-la.
- Use overlays apenas para concerns que realmente atravessam vários owners.
- Mantenha a lógica downstream de revisão e atualização em `Follow-Through Triggers`, e não em novos tipos de arquivo.
- Trate instructions mais estreitas como refinamentos das mais amplas, e não como reversões arbitrárias.
- Mantenha páginas de visão geral curtas e mova o detalhamento para documentos focados de modelo e de regras.
