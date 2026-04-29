# Gramática da Ownership Tree

Público: mantenedores que precisam de uma forma previsível de representar boundaries de ownership no disco.  
Objetivo: definir a gramática canônica da ownership tree para que o mapa seja fácil de ensinar, inspecionar e estender.

## Nesta Página

- [Regra Canônica](#regra-canônica)
- [Gramática Canônica](#gramática-canônica)
- [Owner Raiz do Repositório](#owner-raiz-do-repositório)
- [O Que Uma Pasta de Nó Pode Conter](#o-que-uma-pasta-de-nó-pode-conter)
- [Atalho Opcional Para Um Nó Simples de Arquivo](#atalho-opcional-para-um-nó-simples-de-arquivo)
- [Guidance de Nomes](#guidance-de-nomes)
- [Quando Adicionar Um Nó Mais Estreito](#quando-adicionar-um-nó-mais-estreito)
- [Quando Dividir Um Nó em Vários Arquivos de Instruction](#quando-dividir-um-nó-em-vários-arquivos-de-instruction)
- [Relação com Follow-Through](#relação-com-follow-through)
- [Material Relacionado](#material-relacionado)

## Regra Canônica

Represente o owner raiz do repositório como `.github/instructions/ownership/repository/`.

O nome de pasta `repository/` é literal. Não substitua pelo nome real do checkout do repositório.

Represente todo boundary owned mais estreito como uma pasta de nó filha desse owner raiz.

Essa regra vale tanto quando o boundary owned no repositório é:

- um diretório como `src/api/`
- um arquivo como `src/api/orders.ts`

A pasta é o nó.

Os arquivos de instruction dentro da pasta descrevem a guidance que pertence àquele nó.

## Gramática Canônica

Use estas regras:

1. `repository/` é o owner raiz explícito do repositório.
2. Diretórios do repositório continuam diretórios abaixo de `repository/` na instruction tree.
3. Arquivos do repositório também podem virar pastas de nó, nomeadas com o nome do arquivo.
4. Os arquivos de instruction dentro da pasta de nó são nomeados pela concern ou propósito, e não pelo caminho novamente.
5. Pastas filhas representam boundaries de ownership mais estreitos.

Exemplo canônico mínimo:

```text
.github/
  instructions/
    ownership/
      repository/
        general.instructions.md
        src/
          general.instructions.md
          api/
            general.instructions.md
            orders.ts/
              contract.instructions.md
              framework.instructions.md
```

## Owner Raiz do Repositório

Use `ownership/repository/` quando a guidance pertencer ao boundary raiz do repositório.

Isso é útil para contratos owned pelo repo inteiro, aplicados da raiz para baixo, mas que deixariam o baseline grande ou procedural demais.

Exemplos:

- `ownership/repository/general.instructions.md`
- `ownership/repository/supporting-sources.instructions.md`
- `ownership/repository/repository-structure.instructions.md`

O nó `repository/` é explícito de propósito.

Ele evita que `ownership/` vire uma gaveta ambígua para qualquer regra global.

Ele também evita acoplar a instruction tree ao nome local do clone, ao nome de um fork ou a uma futura renomeação do repositório.

Ele também mantém os owners mais estreitos dentro da mesma árvore: um path top-level real `src/` vira `ownership/repository/src/`, e não um irmão do owner raiz do repositório.

Mantenha o baseline curto e use o owner raiz para guidance owned pelo repo que ainda merece um arquivo de instruction.

Não use o owner raiz como um segundo baseline, um registro de fontes para todo documento ou um lugar para esconder overlays transversais.

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

- `ownership/repository/src/api/orders.ts.instructions.md`

em vez de:

- `ownership/repository/src/api/orders.ts/<concern>.instructions.md`

Use esse atalho apenas para um boundary de arquivo do repositório que precisa de exatamente uma instruction e em que a tree mais curta melhora a legibilidade.

Prefira a forma canônica em pasta quando o nó de arquivo pode crescer, quando ensinabilidade e uniformidade importam mais do que brevidade, ou quando uma segunda representação na mesma área deixaria o mapa mais difícil de ler.

## Guidance de Nomes

Nomeie os arquivos de instruction pela concern ou propósito.

Bons exemplos:

- `general.instructions.md`
- `contract.instructions.md`
- `framework.instructions.md`
- `authorization.instructions.md`
- `diagnostics.instructions.md`

Como nomes como `general.instructions.md` podem se repetir pela árvore, trate o caminho do nó mais o nome do arquivo como a identidade canônica. Mantenha a frontmatter de `.instructions.md` mínima e portável; qualquer metadado extra de UI deve ser opcional e específico de cada surface.

## Quando Adicionar Um Nó Mais Estreito

Cresça a tree de forma incremental.

Não adicione instructions especializadas sem necessidade.

Adicione um nó mais estreito quando:

- o owner mais amplo deixa de oferecer uma guidance honesta o bastante para aquele subtree
- o subtree tem comportamento local, restrições ou terminologia estáveis que merecem guidance própria
- o nó mais estreito reduz ambiguidade em vez de apenas aumentar detalhe

Não adicione um nó mais estreito apenas porque:

- existe mais uma pasta naquele ponto do repositório
- talvez você precise de uma regra ali algum dia
- você quer que todo path tenha sua própria instruction
- você está tentando codificar enumeração de follow-through localmente em vez de reutilizar uma regra mais ampla

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

Ele também é opcional.

Se um nó não tiver nenhuma regra downstream distinta que valha a pena dizer, omita a seção de trigger em vez de copiar prosa genérica de follow-through para baixo.

Esta convenção muda como a tree é organizada no disco.

Ela não cria uma nova camada estrutural.

## Material Relacionado

- [Modelo Operacional](../modelo/modelo-operacional.md)
- [Follow-Through Triggers](../modelo/follow-through-triggers.md)
- [Regras de Decisão](./regras-de-decisao.md)
- [Exemplos](../exemplos/README.md)
- [Repositórios-Exemplo](../exemplos/repositorios/README.md)
