# Arquitetura de Personalização de IA Orientada a Ownership

Público: mantenedores que estão desenhando um modelo escalável de personalização do Copilot para um ou vários repositórios.  
Objetivo: definir uma estrutura reutilizável, previsível, enxuta e fácil de manter.

## O Que Esta Pasta Documenta

Esta pasta é agnóstica ao repositório.

Ela documenta uma arquitetura reutilizável para organizar:

- instruções gerais do repositório,
- instructions baseadas em ownership por caminho,
- overlays transversais,
- skills reutilizáveis,
- comportamento downstream de revisão e atualização.

Nome formal:

- `Arquitetura de Personalização de IA Orientada a Ownership`

Atalho operacional:

- `baseline + ownership tree + cross-cutting overlays`

## Arquitetura em Uma Visão

A arquitetura tem quatro partes estruturais:

- `baseline`
  - a camada curta e geral do repositório
- `ownership tree`
  - instructions ligadas a boundaries estáveis de responsabilidade por caminho
- `cross-cutting overlays`
  - instructions para concerns que atravessam vários owners
- `skills`
  - workflows reutilizáveis mais profundos do que instructions always-on

`Follow-Through Triggers` não é outro tipo de arquivo.

É uma seção que pode existir dentro de instructions de baseline, ownership-tree ou overlay para descrever o que mais pode precisar de revisão depois de uma mudança relevante.

## Quando Esta Arquitetura Faz Sentido

Use esta arquitetura quando você quiser:

- um modelo path-based de personalização que escale entre vários repositórios,
- roteamento previsível sem transformar toda preocupação em agent,
- separação clara entre ownership e concerns transversais,
- uma estrutura legível tanto para quem está chegando agora quanto para quem vai manter por muito tempo.

## Mapa da Documentação

- [Por Que Esta Arquitetura](./por-que-esta-arquitetura.md)
  - caso de negócio, ganhos esperados, não-objetivos e alinhamento com guidance oficial
- [Modelo Central](./modelo-central.md)
  - o modelo conceitual, os termos centrais, a lógica de roteamento e onde o follow-through deve morar
- [Conflitos e Precedência de Instruções](./conflitos-e-precedencia-de-instrucoes.md)
  - o que a plataforma realmente garante, como refinamento deve funcionar e como evitar mapas ambíguos
- [Exemplos e Fluxos](./exemplos-e-fluxos.md)
  - exemplos trabalhados que ensinam o modelo por cenário
- [Playbook de Replicação](./playbook-de-replicacao.md)
  - como reproduzir a arquitetura em outros repositórios

## Trilhas Sugeridas de Leitura

Se este for seu primeiro contato com a arquitetura:

1. Leia este arquivo.
2. Leia [Por Que Esta Arquitetura](./por-que-esta-arquitetura.md).
3. Leia [Modelo Central](./modelo-central.md).
4. Leia [Exemplos e Fluxos](./exemplos-e-fluxos.md).

Se você estiver desenhando um novo repositório:

1. Leia este arquivo.
2. Leia [Por Que Esta Arquitetura](./por-que-esta-arquitetura.md).
3. Leia [Modelo Central](./modelo-central.md).
4. Leia [Playbook de Replicação](./playbook-de-replicacao.md).

Se você estiver investigando ambiguidade ou conflito entre instructions:

1. Leia este arquivo.
2. Leia [Conflitos e Precedência de Instruções](./conflitos-e-precedencia-de-instrucoes.md).
3. Leia [Modelo Central](./modelo-central.md).
4. Leia [Exemplos e Fluxos](./exemplos-e-fluxos.md).

## Regras Centrais de Design

- Comece por boundaries estáveis de ownership, não por temas abstratos.
- Use overlays apenas para concerns que realmente atravessam vários owners.
- Mantenha a lógica downstream de revisão e atualização em `Follow-Through Triggers`, e não em novos tipos de arquivo.
- Trate instructions mais estreitas como refinamentos das mais amplas, e não como reversões arbitrárias.
- Mantenha a visão geral curta e empurre o detalhamento para documentos de referência dedicados.
