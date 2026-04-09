# Gramática da Ownership Tree

Público: mantenedores que precisam de uma forma previsível de representar boundaries de ownership no disco.  
Objetivo: definir a gramática canônica da ownership tree para que o mapa seja fácil de ensinar, inspecionar e estender.

## Nesta Página

- [Regra Canônica](#regra-canônica)
- [Gramática Canônica](#gramática-canônica)
- [O Que Uma Pasta de Nó Pode Conter](#o-que-uma-pasta-de-nó-pode-conter)
- [Atalho Opcional Para Um Nó Simples de Arquivo](#atalho-opcional-para-um-nó-simples-de-arquivo)
- [Guidance de Nomes](#guidance-de-nomes)
- [Quando Dividir Um Nó em Vários Arquivos de Instruction](#quando-dividir-um-nó-em-vários-arquivos-de-instruction)
- [Relação com Follow-Through](#relação-com-follow-through)
- [Material Relacionado](#material-relacionado)

## Regra Canônica

Represente todo boundary owned como uma pasta de nó dentro de `.github/instructions/ownership/`.

Essa regra vale tanto quando o boundary owned no repositório é:

- um diretório como `src/api/`
- um arquivo como `src/api/orders.ts`

A pasta é o nó.

Os arquivos de instruction dentro da pasta descrevem a guidance que pertence àquele nó.

## Gramática Canônica

Use estas regras:

1. Todo boundary de ownership vira uma pasta de nó.
2. Diretórios do repositório continuam diretórios na instruction tree.
3. Arquivos do repositório também podem virar pastas de nó, nomeadas com o nome do arquivo.
4. Os arquivos de instruction dentro da pasta de nó são nomeados pela concern ou propósito, e não pelo caminho novamente.
5. Pastas filhas representam boundaries de ownership mais estreitos.

Exemplo canônico mínimo:

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
```

## O Que Uma Pasta de Nó Pode Conter

Uma pasta de nó pode conter:

- nenhum arquivo de instruction ainda
- um arquivo de instruction
- vários arquivos de instruction
- nós filhos mais estreitos
- arquivos de instruction e nós filhos mais estreitos ao mesmo tempo

Filhos mistos são normais.

Não existe arquivo "main" nem `_self` obrigatório.

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

- você espera que esse nó de arquivo cresça
- você quer a gramática mais ensinável e uniforme
- você quer evitar uma segunda representação na mesma área

## Guidance de Nomes

Nomeie os arquivos de instruction pela concern ou propósito.

Bons exemplos:

- `general.instructions.md`
- `contract.instructions.md`
- `framework.instructions.md`
- `authorization.instructions.md`
- `diagnostics.instructions.md`

Como nomes como `general.instructions.md` podem se repetir pela árvore, prefira definir um `name` claro na frontmatter para melhorar os rótulos nas ferramentas e UIs.

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

## Material Relacionado

- [Modelo Operacional](../modelo/modelo-operacional.md)
- [Follow-Through Triggers](../modelo/follow-through-triggers.md)
- [Regras de Decisão](./regras-de-decisao.md)
- [Exemplos](../exemplos/README.md)
- [Repositórios-Exemplo](../exemplos/repositorios/README.md)
