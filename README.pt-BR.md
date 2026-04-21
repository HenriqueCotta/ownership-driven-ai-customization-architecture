<p align="center">
  <img src="./docs/assets/branding/oda_lockup.svg?v=20260413" alt="Lockup ODA" height="200">
</p>

<p align="center">
  <a href="./docs/en/README.md">
    <img alt="Docs EN" src="https://img.shields.io/badge/docs-EN-2563eb?style=for-the-badge">
  </a>
  <a href="./docs/pt-BR/README.md">
    <img alt="Docs PT-BR" src="https://img.shields.io/badge/docs-PT--BR-16a34a?style=for-the-badge">
  </a>
  <a href="./starter-kit/README.md">
    <img alt="Starter Kit" src="https://img.shields.io/badge/starter--kit-ready-f59e0b?style=for-the-badge">
  </a>
  <a href="./templates/README.md">
    <img alt="Templates" src="https://img.shields.io/badge/templates-copyable-7c3aed?style=for-the-badge">
  </a>
  <a href="./LICENSE">
    <img alt="Licença MIT" src="https://img.shields.io/badge/license-MIT-111827?style=for-the-badge">
  </a>
  <a href="https://github.com/HenriqueCotta/ownership-driven-ai-customization-architecture/releases">
    <img alt="Latest Release" src="https://img.shields.io/github/v/release/HenriqueCotta/ownership-driven-ai-customization-architecture?style=for-the-badge">
  </a>
</p>

# Ownership-Driven Architecture (ODA)

Uma arquitetura escalável para GitHub Copilot custom instructions, path-specific instructions, skills e AGENTS.md em repositórios grandes e monorepos.

Ela ajuda times a organizar `baseline`, `ownership tree`, `cross-cutting overlays`, `Follow-Through Triggers` e `skills` sem transformar tudo em custom agents.

Nome formal da arquitetura:

- `Ownership-Driven Architecture`

Versão em inglês:

- [README.md](./README.md)

## Nesta Página

- [Ownership-Driven Architecture (ODA)](#ownership-driven-architecture-oda)
  - [Nesta Página](#nesta-página)
  - [Para Quem É](#para-quem-é)
  - [Visão Rápida da Arquitetura](#visão-rápida-da-arquitetura)
  - [Por Que Este Repositório Existe](#por-que-este-repositório-existe)
  - [O Que Você Encontra Aqui](#o-que-você-encontra-aqui)
  - [Começo Rápido](#começo-rápido)
  - [Mapa do Repositório](#mapa-do-repositório)
  - [Princípios](#princípios)
  - [Intenção Open Source](#intenção-open-source)
  - [Licença](#licença)

## Para Quem É

Este repositório é para times que precisam escalar a customização do GitHub Copilot em:

- repositórios grandes
- monorepos
- mapas de instruction path-specific
- skills compartilhadas
- compatibilidade com AGENTS.md
- codebases de longa vida com múltiplos boundaries de ownership

## Visão Rápida da Arquitetura

Em alto nível, o modelo separa:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `skills`

Mantenha a visão geral do repositório curta aqui.

Coloque o layout canônico da ownership tree, as regras de nome e os atalhos em [docs/pt-BR/regras/gramatica-da-ownership-tree.md](./docs/pt-BR/regras/gramatica-da-ownership-tree.md).

Coloque cenários trabalhados e arquétipos de repositório em [docs/pt-BR/exemplos/README.md](./docs/pt-BR/exemplos/README.md).

## Por Que Este Repositório Existe

Muitos setups de Copilot crescem sempre para a mesma direção ruim:

- um único arquivo gigante de instruções gerais do repositório
- regras duplicadas em vários arquivos
- boundaries de responsabilidade pouco claros
- custom agents criados para assuntos que deveriam ser instructions ou skills
- docs e templates desatualizados e fora do modelo real de roteamento

Este projeto propõe um modelo operacional mais simples:

- manter o baseline curto
- ligar a maior parte do comportamento a boundaries de ownership
- usar overlays apenas para concerns realmente transversais
- manter comportamento downstream de revisão e atualização em `Follow-Through Triggers`
- usar skills apenas para workflows reutilizáveis que inchariam instructions always-on

## O Que Você Encontra Aqui

- documentação da arquitetura em inglês e português do Brasil
- uma justificativa clara de por que esse modelo existe e onde ele faz sentido
- um starter kit copiável para outro repositório
- templates de baseline, ownership nodes e overlays
- uma skill recomendada de manutenção do repositório para desenhar e auditar a própria customização do Copilot
- um script auxiliar para instalar skills do repositório em diretórios pessoais suportados
- arquivos de comunidade para operar isso como projeto open source

## Começo Rápido

1. Leia a arquitetura em [docs/pt-BR](./docs/pt-BR/README.md).
2. Leia [Por Que Esta Arquitetura](./docs/pt-BR/por-que-esta-arquitetura.md), [Modelo Operacional](./docs/pt-BR/modelo/modelo-operacional.md), [Regras de Decisão](./docs/pt-BR/regras/regras-de-decisao.md) e [Gramática da Ownership Tree](./docs/pt-BR/regras/gramatica-da-ownership-tree.md).
3. Copie o [starter-kit](./starter-kit/README.md) para um repositório de teste.
4. Adapte o mapa de ownership aos seus caminhos reais.
5. Adicione apenas os overlays que realmente atravessam vários owners.
6. Mantenha workflows em skills, e não em instructions always-on.
7. Se precisar desenhar ou auditar o próprio mapa de customização, reutilize a skill opcional [oda-copilot-customization](./.github/skills/oda-copilot-customization/SKILL.md).

## Instale a Skill Recomendada

As docs atuais do GitHub Copilot descrevem skills de repositório em `.github/skills` e skills pessoais em `~/.copilot/skills`, `~/.claude/skills` ou `~/.agents/skills`.

Este repositório mantém a fonte canônica em [`.github/skills/oda-copilot-customization`](./.github/skills/oda-copilot-customization/SKILL.md).

Se você estiver usando Copilot CLI e quiser usar este próprio repositório como fonte de skills sem copiar arquivos, o GitHub também documenta a adição de um diretório alternativo de skills com `/skills add`. Nesse modelo, aponte o Copilot para a pasta `.github/skills` deste repositório e recarregue as skills.

## Mapa do Repositório

- [docs/en](./docs/en/README.md)
  - documentação em inglês
- [docs/pt-BR](./docs/pt-BR/README.md)
  - documentação em português do Brasil
- [starter-kit](./starter-kit/README.md)
  - um exemplo copiável de `.github`
- [templates](./templates/README.md)
  - templates reutilizáveis
- [CONTRIBUTING.md](./CONTRIBUTING.md)
  - regras de contribuição
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
  - expectativas da comunidade
- [SECURITY.md](./SECURITY.md)
  - como reportar problemas com responsabilidade

## Princípios

- Preferir previsibilidade a roteamento esperto demais.
- Preferir ownership a abstração excessiva.
- Preferir refinamento a reversão.
- Preferir workflows reutilizáveis a instructions gigantes.
- Preferir exemplos públicos a convenções escondidas.

## Intenção Open Source

Este projeto foi feito para ser melhorado em público.

Se você adotar a arquitetura em outro repositório, abra uma issue ou pull request contando:

- o que funcionou
- o que ficou confuso
- o que se quebrou em escala
- que decisões de nomenclatura ou roteamento melhoraram o modelo

## Licença

Este repositório é distribuído sob a [Licença MIT](./LICENSE).
