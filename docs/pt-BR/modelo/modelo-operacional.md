# Modelo Operacional

Público: mantenedores que precisam do mapa conceitual da arquitetura antes de escrever regras ou aplicá-la em um repositório.  
Objetivo: definir as partes estruturais do modelo com clareza, sem misturar convenções de layout no disco ou passos de rollout.

## Nesta Página

- [Fórmula Operacional](#fórmula-operacional)
- [O Que a Arquitetura Padroniza](#o-que-a-arquitetura-padroniza)
- [As Partes Estruturais](#as-partes-estruturais)
- [Mapa de Relação](#mapa-de-relação)
- [Documentos Relacionados](#documentos-relacionados)

## Fórmula Operacional

Use esta fórmula:

- `baseline + ownership tree + cross-cutting overlays`

Essa fórmula descreve a parte estrutural da arquitetura.

`Follow-Through Triggers` não é outra camada estrutural.

É uma seção comportamental que pode existir dentro de instructions de baseline, ownership ou overlay.

## O Que a Arquitetura Padroniza

A arquitetura padroniza:

- os papéis estruturais do mapa de instructions
- a espinha dorsal path-first de roteamento
- a distinção entre ownership e concerns transversais
- onde o comportamento downstream de revisão e atualização deve morar

Ela não padroniza o formato interno de prosa de cada instruction.

Os headings, o estilo de escrita e a organização exata em Markdown de cada instruction continuam pertencendo ao repositório ou time adotante.

## As Partes Estruturais

### Baseline

O baseline é a camada curta e geral do repositório.

Ele deve guardar apenas guidance que seja:

- amplamente válida no repositório
- curta o suficiente para continuar legível
- improvável de mudar com frequência
- útil independentemente de qual caminho de ownership esteja ativo

### Ownership Tree

A ownership tree é o mapa path-based de boundaries estáveis de responsabilidade.

Ela responde:

- que parte do sistema é dona deste path
- onde a guidance comportamental local deve morar
- onde refinamento path-based mais estreito é legítimo

### Cross-Cutting Overlays

Um overlay adiciona uma concern extra sobre várias áreas de ownership.

Ele existe para concerns que:

- atravessam vários owners
- ainda se beneficiam de guidance consistente
- não são, por si só, owners arquiteturais estáveis

### Skills

Skills são workflows reutilizáveis.

Use-as para guidance orientada a tarefa que é mais profunda do que instructions always-on e que só deve entrar em contexto quando relevante.

### Follow-Through Triggers

`Follow-Through Triggers` captura o que mais pode agora precisar de revisão depois de uma mudança relevante.

Não é outro tipo de arquivo.

É a camada de consequência downstream que vive dentro das partes estruturais acima.

## Mapa de Relação

Pense no modelo assim:

- `baseline`
  - defaults amplos do repositório
- `ownership tree`
  - comportamento local owned por path
- `cross-cutting overlays`
  - uma lente extra atravessando vários owners
- `skills`
  - workflows reutilizáveis que não devem ficar sempre carregados
- `Follow-Through Triggers`
  - consequências downstream de revisão e atualização

A arquitetura continua escalável porque cada parte tem um trabalho estreito.

## Documentos Relacionados

- [Ownership vs Overlay](./ownership-vs-overlay.md)
- [Follow-Through Triggers](./follow-through-triggers.md)
- [Regras de Decisão](../regras/regras-de-decisao.md)
- [Gramática da Ownership Tree](../regras/gramatica-da-ownership-tree.md)
