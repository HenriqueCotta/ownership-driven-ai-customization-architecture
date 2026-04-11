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
2. Identifique os maiores boundaries estáveis de ownership.
3. Adicione apenas as instructions da ownership tree que correspondem a esses boundaries.
4. Adicione cross-cutting overlays reais.
5. Adicione um pequeno conjunto de skills reutilizáveis.
6. Adicione checks que previnam drift, camadas mortas e estruturas legadas.

Use [Regras de Decisão](./regras/regras-de-decisao.md) para classificar a guidance antes de escrevê-la.

Use [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md) para decidir como o mapa de ownership deve parecer no disco.

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

## Mantenha o Conjunto de Skills Pequeno e Orientado a Outcome

Comece com poucas skills nomeadas pelo outcome do workflow, e não pela mudança que as disparou ou pelo path.

Bons exemplos:

- `review-change`
- `sync-docs`
- `debug-behavior`

Isso normalmente escala melhor do que criar variantes como `review-contract-change`, `review-config-change` ou `review-api-drift`.

Triggers diferentes de follow-through normalmente devem reutilizar o mesmo pequeno conjunto de skills, enquanto o contexto local continua vindo da ownership tree e dos overlays.

Adicione uma skill mais específica apenas quando o workflow em si mudar materialmente em evidências, etapas ou saída esperada.

## Ensine o Modelo de Runtime Explicitamente

Ao documentar ou ensinar esta arquitetura, explique não só o layout de arquivos, mas também o comportamento em runtime que esse layout foi desenhado para suportar.

Na prática, adotantes devem entender que:

- instructions de repositório inteiro fornecem o contexto default
- instructions path-specific podem se tornar relevantes conforme o agente toca novos paths
- follow-through pode expandir o escopo para novas superfícies
- skills genéricas podem ser escolhidas just-in-time quando o tipo de trabalho muda
- checks exatos e repetíveis podem viver em scripts, CI ou runbooks em vez de apenas em prosa

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
- [Regras de Decisão](./regras/regras-de-decisao.md)
- [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md)
- [Exemplos](./exemplos/README.md)
- GitHub Docs, Adding custom instructions for GitHub Copilot CLI  
  <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions>
- GitHub Docs, Creating agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills>
