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

## Revise a Estrutura Regularmente

Revise a estrutura sempre que uma destas coisas acontecer:

- uma regra aparecer em várias instructions
- uma instruction deixar de mapear para um boundary estável
- uma instruction for majoritariamente workflow e deveria ser uma skill
- uma nova instruction estiver sendo proposta para uma consequência downstream em vez de um boundary de ownership
- mantenedores não conseguirem mais prever quais instructions se aplicam a um arquivo

Quando isso acontecer, revisite:

- [Regras de Decisão](./regras/regras-de-decisao.md)
- [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md)
- [Exemplos e Fluxos](./exemplos-e-fluxos.md)

## Estado Final Saudável

O modelo está saudável quando:

- mantenedores conseguem explicar o mapa de ownership com clareza
- a gramática de pastas pode ser explicada sem introduzir casos especiais
- o conjunto de instructions é pequeno o bastante para ser raciocinável
- consequências downstream são tratadas por `Follow-Through Triggers` em vez de duplicação ad hoc
- a mesma estrutura pode ser reutilizada em outro repositório com um mapa de ownership diferente

## Material Relacionado

- [Modelo Operacional](./modelo/modelo-operacional.md)
- [Regras de Decisão](./regras/regras-de-decisao.md)
- [Gramática da Ownership Tree](./regras/gramatica-da-ownership-tree.md)
- [Exemplos e Fluxos](./exemplos-e-fluxos.md)
