# Ownership-Driven AI Customization

Uma arquitetura reutilizável para escalar a personalização do GitHub Copilot com:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `Follow-Through Triggers`
- `skills` como extensões opcionais de workflow

Nome formal da arquitetura:

- `Ownership-Driven AI Customization Architecture`

Versão em inglês:

- [README.md](./README.md)

## Por Que Este Repositório Existe

Muitos setups de Copilot crescem sempre para a mesma direção ruim:

- um único arquivo gigante de instruções gerais do repositório,
- regras duplicadas em vários arquivos,
- boundaries de responsabilidade pouco claros,
- custom agents criados para assuntos que deveriam ser instructions ou skills,
- docs e templates desatualizados e fora do modelo real de roteamento.

Este projeto propõe um modelo operacional mais simples:

- manter o baseline curto,
- ligar a maior parte do comportamento a boundaries de ownership,
- usar overlays apenas para concerns realmente transversais,
- manter comportamento downstream de revisão e atualização em `Follow-Through Triggers`,
- usar skills apenas para workflows reutilizáveis que inchariam instructions always-on.

## O Que Você Encontra Aqui

- documentação da arquitetura em inglês e português do Brasil
- uma justificativa clara de por que esse modelo existe e onde ele faz sentido
- um starter kit copiável para outro repositório
- templates de baseline, ownership nodes e overlays
- arquivos de comunidade para operar isso como projeto open source

## Começo Rápido

1. Leia a arquitetura em [docs/pt-BR](./docs/pt-BR/README.md).
2. Leia [Por Que Esta Arquitetura](./docs/pt-BR/por-que-esta-arquitetura.md) e [Modelo Central](./docs/pt-BR/modelo-central.md).
3. Copie o [starter-kit](./starter-kit/README.md) para um repositório de teste.
4. Adapte o mapa de ownership aos seus caminhos reais.
5. Adicione apenas os overlays que realmente atravessam vários owners.
6. Mantenha workflows em skills, e não em instructions always-on.

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

- o que funcionou,
- o que ficou confuso,
- o que se quebrou em escala,
- que decisões de nomenclatura ou roteamento melhoraram o modelo.

## Licença

Este repositório é distribuído sob a [Licença MIT](./LICENSE).
