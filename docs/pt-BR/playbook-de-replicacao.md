# Playbook de Replicação

Público: mantenedores que estão reproduzindo esta arquitetura em outro repositório.
Objetivo: fornecer uma sequência prática para fazer o rollout do modelo sem copiar detalhes acidentais nem reconstruir duplicação.

## Princípio

Replique o modelo, não os nomes de arquivo.

A parte estável é a estrutura:

- baseline
- ownership tree
- a gramática da ownership tree no disco
- cross-cutting overlays
- skills
- checks de higiene que impedem o mapa de derivar

A parte variável é o mapa de ownership do repositório de destino.

## Princípio de Ensino

Ensine o modelo do concreto para o abstrato:

1. mostre um path real
2. mostre quais instructions se aplicam
3. explique por que cada uma se aplica
4. só depois introduza a regra geral

Isso é mais fácil de ensinar e mais fácil de reter do que começar apenas pela taxonomia.

## Ordem Recomendada de Montagem

1. Defina o baseline curto do repositório.
2. Declare a closure policy do repositório no baseline, mantendo-a curta e normalmente limitada a uma regra ou a um conjunto bem pequeno de regras.
3. Identifique os maiores boundaries estáveis de ownership.
4. Adicione apenas as instructions da ownership tree que correspondem a esses boundaries.
5. Adicione cross-cutting overlays reais.
6. Adicione um pequeno conjunto de skills reutilizáveis.
7. Adicione checks que previnam drift, camadas mortas e estruturas legadas.

Use [Regras de Decisão](./regras/regras-de-decisao.md) para classificar a guidance antes de escrevê-la.

Use [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md) para decidir como o mapa de ownership deve parecer no disco.

Use [Modelo Operacional](./modelo/modelo-operacional.md), [Follow-Through Triggers](./modelo/follow-through-triggers.md) e [Regras de Decisão](./regras/regras-de-decisao.md) em conjunto para desenhar como policy, triggers, skills, automação e qualquer superfície explícita opcional de carry-forward devem trabalhar juntos no repositório de destino.

## Use uma Separação Default de Redação

Quando você começar a escrever instructions, use a separação default definida em [Regras de Decisão](./regras/regras-de-decisao.md), a menos que o repositório tenha um motivo para desviar.

Na prática, isso significa manter guidance local, `Follow-Through Triggers`, closure policy e workflow reutilizável claramente separados, sem transformá-los em uma nova camada nem em um template obrigatório de headings.

## Organize Overlays por Família de Concern

Quando overlays passarem de um pequeno conjunto de arquivos, evite uma única pasta plana.

Use subdiretórios dentro de `overlays/` que agrupem overlays por família de concern.

Boas famílias:

- `quality/`
- `operability/`
- `consistency/`
- `workflow/`
- `tooling/`

Agrupe overlays pela concern que eles representam, e não pela combinação exata de paths que eles tocam.

## Faça o Rollout em Passes Pequenos

Comece de forma estreita.

Um primeiro passo saudável costuma ser:

1. um baseline curto
2. dois ou três nós amplos de ownership
3. um ou dois overlays reais
4. validação contra cenários de mudança reais
5. nós mais estreitos adicionados só quando o owner amplo deixa de ser suficiente

Isso mantém o mapa ensinável enquanto o time ainda está aprendendo como os boundaries se comportam.

## Comece Amplo e Cresça Só Quando Houver Necessidade

O ODA foi feito para poder ser adotado em estágios.

Não tente terminar o repositório inteiro em um único pass.

É saudável parar em um owner mais amplo enquanto ele ainda oferece guidance honesta e útil.

Aprofunde apenas quando:

- um subtree realmente precisa de guidance local diferente
- um nó mais estreito remove ambiguidade que o nó amplo não consegue remover
- o detalhe extra produz ganho operacional real, em vez de apenas simetria

Tentar alcançar cada leaf cedo demais costuma criar um mapa grande com pouco valor local.

## Mantenha o Conjunto de Skills Pequeno e Orientado a Outcome

Comece com poucas skills nomeadas pelo outcome do workflow, e não pela mudança que as disparou ou pelo path.

Bons exemplos:

- `impact-review`
- `review-change`
- `debug-behavior`

Isso normalmente escala melhor do que criar variantes como `review-contract-change`, `review-config-change`, `review-api-drift` ou uma skill de docs por trigger.

Triggers diferentes de follow-through normalmente devem reutilizar o mesmo pequeno conjunto de skills, enquanto o contexto local continua vindo da ownership tree e dos overlays.

Adicione uma skill mais específica apenas quando o workflow em si mudar materialmente em evidências, etapas ou saída esperada.

## Não Escreva Triggers em Todo Lugar

Nem toda instruction precisa de uma seção `Follow-Through Triggers`.

Se um nó não tiver nenhuma regra downstream distinta que valha a pena dizer, omita a seção por completo.

Se vários nós irmãos ou próximos repetirem quase o mesmo trigger, mova a parte compartilhada para o owner mais amplo ou para o baseline e deixe abaixo apenas deltas realmente locais.

Enumeração local de triggers é uma fonte comum de duplicação, omissão e drift.

Prefira uma regra compartilhada honesta a várias cópias levemente diferentes.

## Skill Recomendada de Manutenção da Customização do Copilot

Se um repositório mantém ativamente um mapa não trivial de customização do Copilot, considere também carregar uma skill de manutenção do próprio sistema de customização:

- [oda-copilot-customization](../../.github/skills/oda-copilot-customization/SKILL.md)

Ela é opcional, mas recomendada quando mantenedores querem um workflow reutilizável para:

- desenhar ou auditar o próprio mapa de customização
- checar o repositório contra o ODA upstream, e não contra memória local ou cópias stale
- consultar a guidance oficial atual do GitHub Copilot antes de decidir mudanças estruturais
- revisar juntos arquivos de governança, bridges de compatibilidade, mirrors e safeguards de higiene

Use-a como uma meta-skill para a saúde da customização.
Não a transforme em outra camada always-on e não a use como substituto para skills de workflow específicas do repositório, como `impact-review` ou `debug-behavior`.

Se adotantes quiserem usar essa skill em vários repositórios, em vez de deixá-la apenas dentro de um repositório, instale-a em um diretório pessoal de skills suportado ou use o suporte documentado do Copilot CLI para um diretório alternativo de skills.

## Escolha a Closure Policy Deliberadamente

Não deixe o estilo de fechamento do follow-through implícito.

Triggers podem revelar trabalho downstream possível.
Eles não devem, por si só, decidir se o pass atual precisa ampliar escopo agora ou se esse trabalho vira follow-up explícito; isso pertence à closure policy.

No mínimo, decida se o repositório tende a:

- `integrated`
  - impacto downstream claro costuma ser reconciliado no pass atual
- `split`
  - impacto downstream costuma ser carregado como follow-up explícito
- `hybrid`
  - follow-through pequeno e certo é tratado agora, enquanto trabalho mais amplo ou mais arriscado é carregado explicitamente para depois

Mantenha essa policy curta e coloque-a no baseline, normalmente como uma regra ou um conjunto bem pequeno de regras.

A policy deve definir o envelope aceitável do repositório.
Ela não deve reescrever o workflow inteiro de follow-through.

## Use Carry-Forward Explícito Só Quando Isso Ajudar

Nem todo repositório precisa de uma superfície dedicada de carry-forward.

A memória da conversa pode bastar quando o follow-through costuma ser integrado e o trabalho é curto.

Mas, se o repositório adia com frequência follow-through relevante, lida com trabalho longo ou de maior cuidado, ou espera que conversas parem e recomecem, considere preservar esse follow-through em uma superfície explícita que o time já usa.

Essa superfície pode ser um item de board, uma issue, um finding de review, uma nota de handoff ou outro mecanismo equivalente.

O objetivo é ter continuidade fora da memória do agente, e não criar mais uma camada obrigatória.

## Ensine o Modelo de Runtime Explicitamente

Ao documentar ou ensinar esta arquitetura, explique não só o layout de arquivos, mas também o comportamento em runtime que esse layout foi desenhado para suportar.

Na prática, adotantes devem entender que:

- instructions de repositório inteiro fornecem o contexto default
- instructions path-specific podem se tornar relevantes conforme o agente toca novos paths
- follow-through pode expandir o escopo para novas superfícies
- skills genéricas podem ser escolhidas just-in-time quando o tipo de trabalho muda
- checks exatos e repetíveis podem viver em scripts, CI ou runbooks em vez de apenas em prosa
- quando o repositório escolher adiar um follow-through relevante, um item de board, uma issue, um finding de review, uma nota de handoff ou outra superfície explícita de carry-forward pode preservá-lo fora da memória da conversa

Isso ajuda os times a evitarem dois erros comuns:

- esperar que a arquitetura se comporte como um despachante rígido
- esperar uma skill separada para cada trigger ou owner

A documentação do GitHub sustenta esse modelo mental:

- instructions gerais e path-specific compatíveis podem se aplicar juntas
- custom instructions ficam disponíveis automaticamente quando são salvas
- skills são selecionadas com base na prompt e na descrição da skill e entram no contexto quando escolhidas

## Use Automação para Procedimentos Exatos

Se um repositório precisar de comandos exatos, checks determinísticos ou uma sequência rígida de atualização, prefira:

- scripts
- checks de CI
- runbooks

Deixe instructions e skills apontarem para essa automação quando ajudar, mas evite reescrever procedimentos frágeis em instructions gerais ou skills genéricas.

## Revise a Estrutura Regularmente

Revise a estrutura sempre que uma destas coisas acontecer:

- uma regra aparecer em várias instructions
- uma instruction deixar de mapear para um boundary estável
- uma instruction for majoritariamente workflow e deveria ser uma skill
- uma nova instruction estiver sendo proposta para uma consequência downstream em vez de um boundary de ownership
- uma nova skill estiver sendo proposta para cada trigger ou owner
- listas de triggers quase idênticas continuarem aparecendo em nós irmãos ou próximos
- a tree estiver se expandindo até nós leaf antes de owners mais amplos terem provado que são insuficientes
- checklists operacionais exatos estiverem escorrendo para instructions ou skills genéricas
- uma camada separada de hints estiver sendo proposta apenas para conectar triggers e skills
- mantenedores não conseguirem mais prever quais instructions se aplicam a um arquivo

Quando isso acontecer, revisite:

- [Regras de Decisão](./regras/regras-de-decisao.md)
- [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md)
- [Exemplos](./exemplos/README.md)

## Estado Final Saudável

O modelo está saudável quando:

- mantenedores conseguem explicar o mapa de ownership com clareza
- a gramática de pastas pode ser explicada sem introduzir casos especiais
- o conjunto de instructions é pequeno o bastante para ser raciocinável
- consequências downstream são tratadas por `Follow-Through Triggers` em vez de duplicação ad hoc
- o catálogo de skills permanece pequeno e orientado a outcome, em vez de espelhar cada trigger
- procedimentos exatos vivem em automação ou runbooks, e não em prosa frágil
- a mesma estrutura pode ser reutilizada em outro repositório com um mapa de ownership diferente

## Material Relacionado

- [Modelo Operacional](./modelo/modelo-operacional.md)
- [Follow-Through Triggers](./modelo/follow-through-triggers.md)
- [Regras de Decisão](./regras/regras-de-decisao.md)
- [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md)
- [Exemplos](./exemplos/README.md)
- GitHub Docs, Adding custom instructions for GitHub Copilot CLI  
  <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions>
- GitHub Docs, Creating agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills>
