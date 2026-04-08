# Modelo Central

Público: mantenedores que precisam entender como a arquitetura funciona antes de aplicá-la a um repositório.  
Objetivo: definir o modelo com clareza suficiente para que alguém consiga classificar instructions, desenhar o roteamento e posicionar o follow-through sem depender de adivinhação.

## Fórmula Operacional

Use esta fórmula:

- `baseline + ownership tree + cross-cutting overlays`

Essa fórmula descreve a parte estrutural da arquitetura.

`Follow-Through Triggers` é uma seção comportamental dentro dessas instructions, não uma camada estrutural separada.

## O Que a Arquitetura Não Padroniza

A arquitetura padroniza:

- as camadas estruturais,
- a lógica de roteamento,
- a fronteira entre ownership e overlay,
- onde consequências downstream devem morar.

Ela não define o formato interno de escrita de uma instruction.

A prosa interna, os headings e a estrutura Markdown de uma instruction pertencem ao repositório ou time adotante.

O único bloco arquiteturalmente especial dentro das instructions é:

- `Follow-Through Triggers`

## As Partes Estruturais

### Baseline

O baseline é a camada curta e geral do repositório.

Ele deve guardar apenas regras que sejam:

- amplamente válidas no repositório,
- curtas o suficiente para permanecer legíveis,
- improváveis de mudar com frequência,
- úteis independentemente de qual caminho de ownership esteja ativo.

Conteúdo típico de baseline:

- postura de engenharia,
- expectativas default para mudanças seguras,
- lembretes curtos de follow-through válidos para o repositório,
- guidance concisa sobre como comunicar suposições, validação ou risco.

### Ownership Tree

A ownership tree é a estrutura path-based de boundaries estáveis de responsabilidade.

Pense nela como uma hierarquia de quem é dono de que tipo de lógica:

- owner amplo de código,
- owner mais estreito de subsistema,
- owner mais estreito de feature,
- às vezes um sub-boundary ainda menor se ele realmente precisar de guidance diferente.

Exemplos:

- `src/**/*.ts`
- `src/api/**/*.ts`
- `src/api/orders/**/*.ts`
- `src/billing/invoices/**/*.ts`
- `docs/**/*.md`

Use ownership quando o próprio caminho é dono de um tipo de lógica.

### Layout Canônico dos Nós

Nesta arquitetura, o layout canônico representa todo boundary owned como uma pasta de nó dentro de `.github/instructions/ownership/`.

Isso significa:

- um diretório do repositório vira uma pasta de nó com o mesmo caminho
- um arquivo do repositório também vira uma pasta de nó, como `orders.ts/`
- uma pasta de nó pode conter zero, um ou vários arquivos de instruction
- os nomes dos arquivos de instruction devem descrever a concern que carregam, como `general`, `contract` ou `framework`
- pastas filhas representam boundaries de ownership mais estreitos

Isso mantém a tree ensinável porque nós de pasta e nós de arquivo seguem a mesma gramática visual.

Atalho opcional:

- um nó leaf de arquivo com exatamente uma instruction pode ser escrito diretamente como `orders.ts.instructions.md`
- use isso apenas quando quiser uma tree mais curta para um owner de arquivo simples
- mude para a forma em pasta quando esse owner de arquivo precisar de vários arquivos de instruction

Também mantém a estrutura escalável porque um nó de arquivo pode crescer de uma instruction para várias sem precisar ser renomeado ou "promovido" depois.

Como nomes baseados em concern costumam se repetir, use explicitamente o campo `name` na frontmatter quando quiser rótulos mais claros nas UIs das ferramentas.

Para a convenção completa e exemplos trabalhados, leia [Estrutura da Ownership Tree](./estrutura-da-ownership-tree.md).

### Cross-Cutting Overlays

Um overlay adiciona uma lente extra sobre vários owners.

Use um overlay quando:

- a preocupação atravessa várias áreas de ownership,
- a preocupação se beneficia de guidance consistente,
- a preocupação não é, por si só, um owner arquitetural estável.

Exemplos de concerns boas para overlay:

- qualidade de testes,
- qualidade de linguagem,
- observabilidade,
- diagnósticos de falha,
- consistência entre código e documentação.

Importante:

- overlay diz como pensar,
- ele não diz automaticamente que outra superfície agora precisa mudar.

### Skills

Skills são workflows reutilizáveis.

Use-as para trabalhos mais profundos do que instructions always-on, como:

- debugging,
- revisão,
- planejamento de implementação,
- sincronização de docs,
- brainstorm estruturado.

## Perguntas de Primeiro Contato

Se esta for a primeira vez que você está classificando um caminho de repositório, faça estas quatro perguntas:

1. Que arquivo ou caminho está sendo alterado?
2. Que parte do sistema é dona desse caminho?
3. Que concerns extras também se aplicam ali?
4. O que mais pode ter ficado desatualizado por causa dessa mudança?

Essas perguntas se mapeiam diretamente a:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `Follow-Through Triggers`

## Ownership vs Overlay

Esta é a distinção mais importante do modelo.

Use ownership quando o caminho é dono de um tipo de lógica.

Use overlay quando a mesma preocupação precisa atravessar vários owners diferentes.

Versão curta:

- `overlay` = lente extra
- `follow-through` = consequência downstream

Exemplos:

- `src/api/orders/**/*.ts`
  - nó de ownership
  - aquele subtree é dono da lógica da API de pedidos
- `src/billing/invoices/**/*.ts`
  - nó de ownership
  - aquele subtree é dono da lógica de faturas
- `src/**/*.ts, tests/**/*.ts, scripts/**/*.ts`
  - bom candidato de overlay para qualidade de linguagem ou testing
  - a concern atravessa vários owners
- `src/api/**/*.ts, src/billing/**/*.ts`
  - bom candidato de overlay para observabilidade
  - a concern atravessa vários owners

Regra prática:

- se o recorte existe porque aqueles arquivos são responsáveis por um tipo de lógica, use ownership
- se o recorte existe porque uma concern extra atravessa vários owners, use overlay

`docs/**/*.md` normalmente é seu próprio nó de ownership, não um overlay.

A ligação entre código e docs normalmente vem de follow-through, não de transformar docs em overlay.

## Onde o Follow-Through Deve Ficar

`Follow-Through Triggers` deve morar dentro da instruction que melhor entende a origem da mudança.

Posicionamento default:

- baseline
  - para regras downstream curtas e válidas para o repositório inteiro
- nó de ownership
  - quando o owner da origem entende melhor o blast radius
- overlay
  - apenas quando a regra downstream realmente é owned por aquela concern transversal

Em outras palavras:

- o formato interno do restante do arquivo está fora do escopo da arquitetura
- as consequências downstream ainda devem ser fáceis de encontrar e não devem ser duplicadas arbitrariamente pela árvore

Exemplos:

- contrato mudou
  - follow-through normalmente fica no owner de contrato
- defaults de config mudaram
  - follow-through normalmente fica no owner de config
- comportamento público mudou em `src/**`
  - follow-through normalmente fica no owner relevante do lado de `src` ou no baseline
- overlay de testing-quality
  - ajuda a moldar como testes devem ser escritos
  - não é, por si só, o owner da regra genérica "se `src/**` mudar, revise testes"

## Exemplo Simples de Roteamento

Imagine esta estrutura de repositório:

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

Se o Copilot estiver editando `src/api/orders/create_order.ts`, uma estrutura saudável normalmente se parece com isto:

- baseline
- nós da ownership tree como:
  - `src/**/*.ts`
  - `src/api/**/*.ts`
  - `src/api/orders/**/*.ts`
- cross-cutting overlays como:
  - um overlay de testing-quality
  - um overlay de observabilidade para caminhos operacionais

Exemplos do que esses overlays podem significar:

- overlay de testing-quality
  - preferir testes focados em comportamento
  - manter fixtures pequenas
  - manter nomes de testes explícitos
- overlay de observabilidade
  - registrar eventos operacionais relevantes
  - manter sinais de erro diagnósticáveis
  - preservar contexto útil de telemetria

Depois, se a mudança afetar comportamento público, semântica de contrato, config ou expectativas operacionais, uma seção `Follow-Through Triggers` no owner mais adequado pode instruir o Copilot a inspecionar testes, docs, implementações ou configs.
