# Repositórios-Exemplo

Público: mantenedores que já entendem a arquitetura no abstrato e agora querem ver como um repositório bem implementado pode se parecer.  
Objetivo: mostrar arquétipos genéricos de repositório, a ownership tree que eles usariam e como a arquitetura se comporta em situações do cotidiano.

## Como Usar Esta Pasta

Cada arquivo mostra:

- uma estrutura genérica de repositório
- um layout saudável de ownership tree
- um conjunto pequeno de overlays
- situações cotidianas e quais instructions deveriam importar

Isto não são templates canônicos de repositório.

São exemplos de ensino da arquitetura.

## Arquétipos Incluídos

- [Serviço de API](./01-servico-de-api.md)
  - um backend com rotas, contratos, config, testes e docs
- [Aplicação Web de Produto](./02-aplicacao-web-de-produto.md)
  - uma aplicação frontend com rotas, design system, estado, testes e docs
- [Monorepo de Produto](./03-monorepo-de-produto.md)
  - um monorepo com apps, packages, docs e boundaries de infraestrutura

## O Que Observar

Ao ler os exemplos, foque nestas perguntas:

1. Quais caminhos são boundaries estáveis de ownership?
2. Quais concerns merecem overlays em vez de nós de ownership?
3. Quais mudanças deveriam disparar follow-through para testes, docs, config ou operação?
4. Como a gramática de pastas continua legível quando o repositório cresce?
