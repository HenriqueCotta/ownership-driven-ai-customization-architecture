# Estrutura da Ownership Tree

Público: mantenedores que precisam de uma forma simples e ensinável de organizar no disco as instructions da ownership tree.  
Objetivo: definir uma gramática canônica de pastas, mais um pequeno atalho opcional, que suporte owners de diretório, owners de arquivo, filhos mistos e múltiplas instructions por nó sem confusão.

## A Regra em Uma Frase

Represente todo boundary owned como uma pasta de nó dentro de `.github/instructions/ownership/`.

Essa regra vale tanto quando o boundary owned no repositório é:

- um diretório como `src/api/`
- um arquivo como `src/api/orders.ts`

A pasta é o nó.

Os arquivos de instruction dentro da pasta descrevem a guidance que pertence àquele nó.

## Por Que Esta Convenção Existe

Sem um layout canônico, ownership trees normalmente viram misturas confusas, como:

- alguns nós representados por arquivos
- alguns nós representados por pastas
- nós de arquivo que precisam ser renomeados depois quando uma instruction vira várias
- regras de nome fáceis de lembrar para o autor original, mas difíceis de ensinar para o resto do time

Esta convenção remove esses problemas usando uma gramática única em toda a árvore.

## A Gramática Canônica

Use estas regras:

1. Todo boundary de ownership vira uma pasta de nó.
2. Diretórios do repositório continuam diretórios na instruction tree.
3. Arquivos do repositório também viram pastas de nó, nomeadas com o nome do arquivo.
4. Os arquivos de instruction dentro de uma pasta de nó são nomeados pela concern ou propósito, e não pelo caminho outra vez.
5. Pastas filhas representam boundaries de ownership mais estreitos.

Exemplos de nomes baseados em concern:

- `general.instructions.md`
- `contract.instructions.md`
- `framework.instructions.md`
- `authorization.instructions.md`
- `diagnostics.instructions.md`

## O Que Uma Pasta de Nó Pode Conter

Uma pasta de nó pode conter:

- nenhum arquivo de instruction ainda
- um arquivo de instruction
- vários arquivos de instruction
- nós filhos mais estreitos
- arquivos de instruction e nós filhos mais estreitos ao mesmo tempo

Não existe arquivo "main" nem `_self` obrigatório.

Se uma instruction basta, mantenha uma.

Se concerns realmente distintas pertencem ao mesmo boundary, divida em vários arquivos.

Para exemplos trabalhados e fluxos de ensino, leia [Exemplos e Fluxos](./exemplos-e-fluxos.md).

## Atalho Opcional Para Um Nó Simples de Arquivo

Se um arquivo do repositório for um nó leaf e precisar de exatamente uma instruction, você pode usar a forma curta:

- `src/api/orders.ts.instructions.md`

em vez de:

- `src/api/orders.ts/<concern>.instructions.md`

Use esse atalho apenas quando tudo abaixo for verdade:

- o boundary owned é um arquivo do repositório, não um diretório
- esse nó de arquivo precisa de exatamente uma instruction
- você está otimizando por uma tree mais curta

Prefira a forma canônica em pasta quando:

- você espera que esse nó de arquivo cresça,
- você quer a gramática mais ensinável e uniforme,
- ou quer evitar introduzir uma segunda representação na mesma área.

Se esse nó de arquivo depois precisar de uma segunda instruction, mude para a forma canônica em pasta.

## Exemplo Simples

Estrutura do repositório:

```text
repo/
  src/
    api/
      orders.ts
  docs/
    orders.md
```

Estrutura das instructions:

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        api/
          general.instructions.md
          orders.ts/
            contract.instructions.md
            framework.instructions.md
      docs/
        general.instructions.md
```

Como ler isso:

- `src/` é um nó amplo de ownership
- `src/api/` é um nó mais estreito de ownership
- `src/api/orders.ts/` é um nó de ownership em nível de arquivo
- `orders.ts/` tem dois arquivos de instruction porque aquele arquivo precisa de dois tipos distintos de guidance

## Exemplo com Filhos Mistos

Um mesmo pai pode conter nós de diretório mais estreitos e nós de arquivo ao mesmo tempo.

Estrutura do repositório:

```text
repo/
  src/
    routes/
      health.ts
      orders.ts
      admin/
        users.ts
```

Estrutura das instructions:

```text
.github/
  instructions/
    ownership/
      src/
        routes/
          general.instructions.md
          health.ts/
            diagnostics.instructions.md
          orders.ts/
            contract.instructions.md
            framework.instructions.md
          admin/
            authorization.instructions.md
            users.ts/
              validation.instructions.md
```

Isto é válido e intencional:

- `health.ts/` é um nó de arquivo
- `orders.ts/` é outro nó de arquivo
- `admin/` é um nó de diretório mais estreito
- os três ficam lado a lado porque todos são filhos do boundary `routes/`

## Por Que Isto É Mais Fácil de Ensinar

O roteiro de ensino fica muito simples:

1. Encontre o caminho no repositório.
2. Caminhe pelo mesmo caminho dentro de `ownership/`.
3. Trate cada pasta desse caminho como um possível nó de ownership.
4. Leia os arquivos de instruction que vivem nas pastas de nó correspondentes.
5. Só adicione overlays depois que o ownership estiver claro.

Isso é muito mais fácil de explicar do que ensinar uma regra para nós de pasta e outra para nós de arquivo.

## Por Que Isto Escala

Este layout escala bem porque:

- a árvore pode crescer sem trocar de gramática
- um arquivo pode ganhar uma segunda instruction sem forçar mudança de estratégia de nome
- irmãos mistos não precisam de truques especiais de nomenclatura
- nomes baseados em concern continuam fazendo sentido quando caminhos são reorganizados
- novos mantenedores conseguem inspecionar a árvore caminhando pelos diretórios, em vez de decodificar convenções

Em resumo:

- a pasta diz o que é owned
- o arquivo de instruction diz que tipo de guidance mora ali

## Guidance de Nomes

Como nomes como `general.instructions.md` podem se repetir bastante pela árvore, prefira definir um `name` claro na frontmatter para melhorar os rótulos nas ferramentas e UIs.

Exemplo:

```md
---
name: "ownership: src api orders contract"
description: "Guidance de contrato para o arquivo da API de orders."
applyTo: "src/api/orders.ts"
---
```

O nome repetido do arquivo não é um problema.

O campo `name` é o que deixa o rótulo da UI mais amigável para humanos.

Se você usar o atalho de arquivo único, o mesmo conselho continua valendo:

```md
---
name: "ownership: src api orders"
description: "Guidance geral para o arquivo da API de orders."
applyTo: "src/api/orders.ts"
---
```

## Quando Dividir Um Nó em Vários Arquivos de Instruction

Divida apenas quando o mesmo boundary owned realmente precisar de lentes de guidance diferentes.

Bons motivos para dividir:

- um arquivo precisa ao mesmo tempo de guidance de contrato e de framework
- um subtree precisa ao mesmo tempo de guidance de arquitetura e de autorização
- um boundary tem um conjunto estável de regras gerais mais uma concern operacional mais estreita

Maus motivos para dividir:

- você está tentando codificar consequências downstream em arquivos separados
- você está duplicando o mesmo conselho com pequenas variações de texto
- o arquivo extra existe só porque o esquema de nomes parece esperto

## Relação com Follow-Through

`Follow-Through Triggers` continua morando dentro do arquivo de instruction mais relevante.

Esta convenção muda como a tree é organizada no disco.

Ela não cria uma nova camada estrutural.
