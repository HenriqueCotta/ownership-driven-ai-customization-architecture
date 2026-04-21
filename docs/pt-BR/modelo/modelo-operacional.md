# Modelo Operacional

Público: mantenedores que precisam do mapa conceitual da arquitetura antes de escrever regras ou aplicá-la em um repositório.  
Objetivo: definir as partes estruturais do modelo com clareza, sem misturar convenções de layout no disco ou passos de rollout.

## Nesta Página

- [Fórmula Operacional](#fórmula-operacional)
- [O Que a Arquitetura Padroniza](#o-que-a-arquitetura-padroniza)
- [As Partes Estruturais](#as-partes-estruturais)
- [Como o Follow-Through se Encaixa](#como-o-follow-through-se-encaixa)
- [Comportamento em Runtime na Prática](#comportamento-em-runtime-na-prática)
- [Mapa de Relação](#mapa-de-relação)
- [Referências Oficiais](#referências-oficiais)
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
- onde o comportamento downstream de follow-through deve morar

Ela não padroniza o formato interno de prosa de cada instruction.

Os headings, o estilo de escrita e a organização exata em Markdown de cada instruction continuam pertencendo ao repositório ou time adotante.

Ela também não padroniza uma única closure policy universal para todos os repositórios.

Repositórios podem escolher estilos diferentes de follow-through desde que permaneçam estruturalmente claros sobre onde policy, triggers, skills, automação e qualquer superfície explícita opcional de carry-forward pertencem.

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

Mantenha o conjunto de skills pequeno e orientado a outcome.

Casos diferentes de follow-through geralmente devem reutilizar as mesmas poucas skills, como `impact-review`, review de mudança ou debugging, em vez de criar uma skill por trigger.

### Follow-Through Triggers

`Follow-Through Triggers` captura que outras superfícies downstream podem agora precisar de atenção depois de uma mudança relevante.

Não é outro tipo de arquivo.

É a camada de consequência downstream que vive dentro das partes estruturais acima.

A condição do trigger deve ficar ancorada na instruction que consegue observar a mudança de origem.

Um trigger pode revelar trabalho que depois use uma skill genérica, mas o trigger em si não é uma camada de despacho de skills.

Procedimentos exatos e repetíveis se encaixam melhor em scripts, CI ou runbooks do que em prosa geral de trigger.

## Como o Follow-Through se Encaixa

Follow-through saudável geralmente precisa de mais do que triggers sozinhos.

Na prática, repositórios frequentemente precisam compor:

- closure policy do repositório
- triggers ancorados na origem
- skills reutilizáveis
- automação e validação
- quando necessário, uma superfície explícita de carry-forward para follow-through relevante adiado

Isso ainda não é outra camada estrutural.

É apenas a forma prática como repositórios combinam as partes existentes acima.

A policy geral do repositório costuma pertencer ao baseline.
Triggers continuam ancorados na origem em baseline, ownership ou overlays.
Fluxo reutilizável de tarefa pertence a skills.
Checks exatos e repetíveis pertencem à automação.
Quando um repositório carrega adiante um trabalho relevante de forma intencional, muitas vezes é mais saudável preservá-lo em uma superfície explícita do que depender apenas da memória do agente.
Isso é opcional, e não exige um task tracker dedicado.

Use [Follow-Through Triggers](./follow-through-triggers.md) para desenhar triggers, [Regras de Decisão](../regras/regras-de-decisao.md) para dúvidas de posicionamento e [Playbook de Replicação](../playbook-de-replicacao.md) quando for aplicar isso em um repositório real.

## Comportamento em Runtime na Prática

A arquitetura é path-first no disco, mas o valor dela aparece em runtime conforme o escopo do agente se expande.

Na prática:

1. instructions de repositório inteiro fornecem o contexto default amplo
2. quando a tarefa toca um path compatível, as instructions path-specific daquele path também entram em jogo
3. se o trabalho se expandir para novos paths, novas instructions path-specific podem se tornar relevantes também
4. se o tipo de trabalho mudar, o agente pode escolher uma skill just-in-time
5. se existir um check exato e repetível, o agente pode usar scripts, CI ou runbooks em vez de depender só de prosa

É por isso que a arquitetura mantém o contexto local nas ownership instructions e mantém skills orientadas a outcome:

- mudanças de path trazem novo contexto local
- mudanças no workflow podem trazer uma nova skill
- consequências downstream podem revelar mais superfícies sem exigir uma nova camada arquitetural

Esse modelo de runtime combina com o comportamento documentado pelo GitHub:

- instructions de repositório inteiro e instructions path-specific compatíveis são usadas em conjunto quando o path bate
- custom instructions são adicionadas automaticamente às requests e ficam disponíveis assim que o arquivo é salvo
- skills são escolhidas com base na prompt e na descrição da skill
- quando uma skill é escolhida, o `SKILL.md` entra no contexto e recursos dentro da pasta da skill podem ser usados junto com ele

Como diferentes surfaces do Copilot suportam tipos diferentes de instruction, a documentação do repositório deve explicar o modelo como um mapa mental reutilizável, e não como um motor totalmente determinístico de execução.

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
  - consequências downstream de follow-through

A arquitetura continua escalável porque cada parte tem um trabalho estreito.
Os repositórios então compõem policy de fechamento, triggers, skills, automação e tracking ao redor dessas partes, em vez de inventar uma nova camada.

## Referências Oficiais

- GitHub Docs, Adding repository custom instructions for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- GitHub Docs, Adding custom instructions for GitHub Copilot CLI  
  <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions>
- GitHub Docs, Creating agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills>
- GitHub Docs, Comparing GitHub Copilot CLI customization features  
  <https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/copilot-cli/comparing-cli-features>
- GitHub Docs, Support for different types of custom instructions  
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>

## Documentos Relacionados

- [Ownership vs Overlay](./ownership-vs-overlay.md)
- [Follow-Through Triggers](./follow-through-triggers.md)
- [Regras de Decisão](../regras/regras-de-decisao.md)
- [Playbook de Replicação](../playbook-de-replicacao.md)
- [Gramática da Ownership Tree](../regras/gramatica-da-ownership-tree.md)
