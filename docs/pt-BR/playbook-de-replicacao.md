# Playbook de Replicação

Público: mantenedores que estão desenhando esta arquitetura para outros repositórios.
Objetivo: fornecer um método conciso para construir e manter a estrutura sem overfitting a uma única codebase.

## Princípio

Replique o modelo, não os nomes de arquivo.

Replique a `Arquitetura de Personalização de IA Orientada a Ownership`, não os nomes exatos de um repositório específico.

A parte estável é a estrutura:

- baseline,
- ownership tree,
- cross-cutting overlays,
- skills,
- checks de higiene.

A parte variável é o mapa de ownership do repositório de destino.

## Não Padronize Demais a Escrita das Instructions

Padronize a arquitetura, não o formato interno de prosa de cada instruction.

A arquitetura deve padronizar:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `Follow-Through Triggers`
- o critério de quando usar skills

O formato interno de escrita das instructions pertence ao repositório ou time adotante e está fora do escopo desta arquitetura.

## Princípio de Ensino

Quando você ensinar ou documentar esse modelo, vá do concreto para o abstrato:

1. mostre um caminho de arquivo,
2. mostre quais instructions se aplicam,
3. explique por que cada uma se aplica,
4. só depois introduza as regras gerais.

Isso é mais fácil de entender do que começar apenas pela taxonomia.

## Ordem Recomendada de Montagem

1. Defina o baseline geral do repositório.
2. Identifique os maiores boundaries estáveis de ownership.
3. Adicione apenas as instructions da ownership tree que correspondem a esses boundaries.
4. Adicione os cross-cutting overlays que realmente atravessam várias áreas de ownership.
5. Adicione um pequeno conjunto de skills reutilizáveis.
6. Adicione checks que previnam drift, camadas mortas e estruturas legadas.

## Como Identificar Nós da Ownership Tree

Comece por boundaries estáveis de responsabilidade na estrutura de caminhos, não por tópicos abstratos.

Boas fontes de boundaries de ownership:

- slices arquiteturais,
- boundaries de deploy,
- boundaries de contrato,
- boundaries de camada,
- boundaries de subsistema.

Bons exemplos:

- `src/**/*.ts`
- `src/api/**/*.ts`
- `src/api/orders/**/*.ts`
- `src/billing/invoices/**/*.ts`
- `docs/**/*.md`

Fontes ruins:

- temas vagos de qualidade,
- tarefas temporárias,
- iniciativas pontuais.

Se um boundary muda a forma como o Copilot deve pensar sobre os arquivos daquele caminho, ele pode merecer uma instruction da ownership tree.

A árvore só deve ficar mais específica quando o subtree mais estreito realmente precisar de guidance diferente.

## Como Identificar Cross-Cutting Overlays

Um cross-cutting overlay é apropriado quando:

1. a preocupação atravessa várias áreas de ownership,
2. a preocupação ainda se beneficia de guidance consistente,
3. a preocupação não é, por si só, um owner arquitetural estável.

Overlays típicos:

- testing,
- documentation,
- configuration,
- observability,
- task tracking.

Não exemplo:

- `src/api/orders/**/*.ts` e `src/billing/invoices/**/*.ts`

Se esses caminhos são diferentes porque cada subtree é dono de um tipo diferente de lógica, eles pertencem à ownership tree.

Eles não são overlays só porque são mais estreitos do que `src/**/*.ts`.

## Como Organizar Arquivos de Overlay

Quando overlays passarem de um pequeno conjunto de arquivos, evite manter tudo em uma única pasta plana.

Use subdiretórios dentro de `overlays/` que agrupem overlays por família de concern.

Boas famílias:

- `quality/`
- `operability/`
- `consistency/`
- `workflow/`
- `tooling/`

Exemplo:

```text
.github/instructions/
  overlays/
    quality/
      testing-quality.instructions.md
      language-quality.instructions.md
    operability/
      observability.instructions.md
      failure-diagnostics.instructions.md
    consistency/
      code-docs-consistency.instructions.md
```

Não agrupe overlays pela combinação exata de caminhos que eles tocam.

Agrupe-os pela preocupação que eles representam.

## Exemplo Mínimo de Ensino

Comece com uma estrutura pequena:

```text
repo/
  src/
    api/
      orders/
        create_order.ts
    billing/
      invoices/
        issue_invoice.ts
  tests/
    api/
      orders/
        create_order.test.ts
  docs/
    orders.md
```

Depois explique nesta ordem:

1. `baseline`
   - se aplica em todo lugar
2. `src/**/*.ts`
   - owner amplo de código
3. `src/api/**/*.ts`
   - owner de API
4. `src/api/orders/**/*.ts`
   - owner mais estreito para endpoints de pedidos
5. `src/**/*.ts, tests/**/*.ts`
   - overlay de qualidade de testes ou de qualidade de linguagem
6. `docs/**/*.md`
   - owner de documentação, não overlay

Por fim, adicione a regra downstream:

- se `create_order.ts` mudar comportamento público, uma seção `Follow-Through Triggers` pode orientar o Copilot a revisar testes e docs

Distinção importante:

- o passo 5 fala da lente extra de qualidade que se aplica quando esses arquivos entram em escopo
- a regra downstream final fala do que mais pode precisar de revisão depois de uma mudança relevante

## Matriz de Decisão

Coloque guidance no baseline quando ela for:

- válida para o repositório inteiro,
- curta,
- amplamente útil,
- improvável de mudar com frequência.

Coloque guidance em uma instruction da ownership tree quando ela for:

- ligada a uma família estável de caminhos,
- específica daquele boundary de responsabilidade,
- útil na maior parte do tempo naquele caminho.

Coloque guidance em um cross-cutting overlay quando ela for:

- relevante em várias áreas de ownership,
- não owned por um único slice arquitetural,
- importante o bastante para ser carregada automaticamente nos caminhos compatíveis.

Coloque guidance em uma skill quando ela for:

- um workflow reutilizável,
- mais profundo do que política always-on,
- não naturalmente preso a um único caminho.

Considere um agent apenas quando:

- o time for usá-lo como modo explícito,
- o modo tiver um papel ou boundary de ferramentas distinto,
- uma skill não for suficiente.

## Regra para Consequências Downstream

Não crie um novo arquivo de instruction só porque uma mudança tem consequências downstream.

Em vez disso:

- adicione ou refine uma seção `Follow-Through Triggers` na instruction existente de baseline, ownership-tree ou cross-cutting que já é dona daquela preocupação.

## Guidance de Pai e Filho

Trate nós mais estreitos de ownership como refinamentos de nós mais amplos.

Bom refinamento:

- pai: "API handlers devem permanecer finos e delegar o trabalho de negócio"
- filho: "dentro de `src/api/orders/**`, mapeie cedo a entrada HTTP e chame diretamente os services de pedidos"

Ruim refinamento:

- pai: "API handlers devem permanecer finos e delegar o trabalho de negócio"
- filho: "dentro de `src/api/orders/**`, coloque validação, regras de negócio, persistência e retries diretamente no handler"

O objetivo não é override arbitrário.

O objetivo é especialização controlada para um boundary de caminho menor.

## Checks Anti-Bloat

Revise a estrutura sempre que uma destas coisas acontecer:

- uma regra aparecer em várias instructions,
- uma instruction deixar de mapear para um boundary estável,
- uma instruction for majoritariamente workflow e deveria ser uma skill,
- uma nova instruction estiver sendo proposta para uma consequência downstream em vez de um boundary de ownership,
- mantenedores não conseguirem mais prever quais instructions se aplicam a um arquivo.

## Estado Final Saudável

O modelo está saudável quando:

- mantenedores conseguem explicar o mapa de ownership com clareza,
- o conjunto de instructions é pequeno o bastante para ser raciocinável,
- consequências downstream são tratadas por seções `Follow-Through Triggers` em vez de duplicação ad hoc,
- a mesma estrutura pode ser reutilizada em outro repositório com um mapa de ownership diferente.
