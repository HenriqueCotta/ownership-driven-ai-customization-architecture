# Arquétipos de Repositório

Público: mantenedores que já entendem a arquitetura no abstrato e agora querem arquétipos de repositório mais realistas.
Objetivo: mostrar mapas seletivos de ownership, conjuntos pequenos de overlays e fluxos guiados por prompt que se pareçam com o uso do dia a dia.

## Nesta Página

- [Como Usar Esta Pasta](#como-usar-esta-pasta)
- [Arquétipos Incluídos](#arquétipos-incluídos)
- [O Que Observar](#o-que-observar)

## Como Usar Esta Pasta

Cada arquivo mostra:

- uma estrutura genérica de repositório
- um mapa de ownership realista, e não exaustivo
- um conjunto pequeno de overlays
- situações guiadas por prompt que mostram como a arquitetura ajuda na prática

Isto não são templates canônicos de repositório.

São exemplos de ensino de como um repositório saudável normalmente aplica a arquitetura:

- nem toda pasta vira nó
- nem todo arquivo ganha instruction própria
- muitos caminhos vivem bem com owners amplos, overlays e follow-through

## Arquétipos Incluídos

- [Serviço de API](./01-servico-de-api.md)
  - um backend com rotas, contratos, config, testes e docs
- [Aplicação Web de Produto](./02-aplicacao-web-de-produto.md)
  - uma aplicação frontend com features, design system, estado, testes e docs de UX
- [Monorepo de Produto](./03-monorepo-de-produto.md)
  - um monorepo com apps, packages compartilhados, docs e infraestrutura

## O Que Observar

Ao ler os exemplos, foque nestas perguntas:

1. Quais paths realmente merecem um nó próprio de ownership?
2. Quais paths ficam intencionalmente sob owners mais amplos?
3. Quais overlays são pequenos, mas genuinamente úteis?
4. Como a arquitetura molda a prompt, o processo de implementação e o follow-through?
