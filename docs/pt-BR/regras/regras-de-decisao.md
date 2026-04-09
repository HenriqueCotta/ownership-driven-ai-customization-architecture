# Regras de Decisão

Público: mantenedores que precisam posicionar guidance corretamente sem adivinhação.  
Objetivo: fornecer um conjunto compacto de decisões para classificar instructions e reconhecer sinais de redesign.

## Nesta Página

- [Perguntas de Primeiro Contato](#perguntas-de-primeiro-contato)
- [Onde Cada Guidance Deve Morar](#onde-cada-guidance-deve-morar)
- [Checks Rápidos de Classificação](#checks-rápidos-de-classificação)
- [Sinais de Redesign](#sinais-de-redesign)
- [Documentos Relacionados](#documentos-relacionados)

## Perguntas de Primeiro Contato

Ao classificar um path ou uma instruction proposta, comece com estas perguntas:

1. Que arquivo ou path está mudando?
2. Que owner estável é responsável por esse path?
3. Que concerns extras também se aplicam ali?
4. O que mais pode agora ter ficado desatualizado por causa dessa mudança?

Essas quatro perguntas se mapeiam diretamente a:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `Follow-Through Triggers`

## Onde Cada Guidance Deve Morar

Coloque guidance no baseline quando ela for:

- válida para o repositório inteiro
- curta
- amplamente útil
- improvável de mudar com frequência

Coloque guidance em ownership quando ela for:

- ligada a uma família estável de paths
- específica daquele boundary de responsabilidade
- útil na maior parte do tempo naquele boundary

Coloque guidance em um cross-cutting overlay quando ela for:

- relevante em várias áreas de ownership
- não owned por um único slice arquitetural
- importante o bastante para ser carregada automaticamente nos paths compatíveis

Coloque guidance em uma skill quando ela for:

- um workflow reutilizável
- mais profunda do que política always-on
- não naturalmente presa a um único path

## Checks Rápidos de Classificação

Use estes checks quando a escolha parecer nebulosa:

- se o path é dono de um tipo de lógica, provavelmente é ownership
- se uma concern extra atravessa vários owners, provavelmente é overlay
- se a pergunta principal é "o que mais pode agora precisar de revisão?", provavelmente é follow-through
- se o conteúdo descreve principalmente um fluxo reutilizável de trabalho, provavelmente é skill

Para a distinção conceitual, leia [Ownership vs Overlay](../modelo/ownership-vs-overlay.md).

Para consequências downstream, leia [Follow-Through Triggers](../modelo/follow-through-triggers.md).

## Sinais de Redesign

Trate estes pontos como sinais de que o mapa precisa de redesign:

- a mesma regra aparece em várias instructions
- uma instruction filha reverte a pai em vez de refiná-la
- um overlay é nomeado pelos paths cruzados em vez de por uma concern coerente
- um path de docs é tratado como overlay quando deveria ser seu próprio owner
- uma nova instruction é proposta apenas porque uma mudança tem consequências downstream
- mantenedores não conseguem prever quais instructions se aplicam a um arquivo

## Documentos Relacionados

- [Modelo Operacional](../modelo/modelo-operacional.md)
- [Ownership vs Overlay](../modelo/ownership-vs-overlay.md)
- [Follow-Through Triggers](../modelo/follow-through-triggers.md)
- [Gramática da Ownership Tree](./gramatica-da-ownership-tree.md)
