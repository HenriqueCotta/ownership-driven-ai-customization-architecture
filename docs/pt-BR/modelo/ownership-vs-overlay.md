# Ownership vs Overlay

Público: mantenedores que precisam entender a distinção conceitual mais importante da arquitetura.  
Objetivo: explicar a diferença entre comportamento owned por path e concerns transversais antes da escrita das regras.

## Nesta Página

- [A Distinção Central](#a-distinção-central)
- [Use Ownership Quando](#use-ownership-quando)
- [Use Overlay Quando](#use-overlay-quando)
- [Exemplos](#exemplos)
- [Erros Comuns](#erros-comuns)
- [Documentos Relacionados](#documentos-relacionados)

## A Distinção Central

Use ownership quando o path é dono de um tipo de lógica.

Use overlay quando uma concern extra atravessa vários owners diferentes.

Versão curta:

- `ownership`
  - quem é dono desse path e do comportamento local dele
- `overlay`
  - que lente extra deve se aplicar sobre vários owners

## Use Ownership Quando

Escolha ownership quando:

- o path existe porque aquela parte do repositório é dona de um tipo específico de lógica
- mantenedores naturalmente explicariam a área como subsistema, slice ou boundary de responsabilidade
- a guidance é útil na maior parte do tempo dentro daquele path

Ownership fala de responsabilidade estável, não de agrupamento por conveniência.

## Use Overlay Quando

Escolha overlay quando:

- a concern atravessa várias áreas de ownership
- a concern é importante o bastante para ser carregada automaticamente nos paths compatíveis
- a concern não é, por si só, um owner arquitetural estável

Overlay é uma lente extra, não uma segunda ownership tree.

## Exemplos

- `src/api/orders/**/*.ts`
  - nó de ownership
  - aquele subtree é dono da lógica da API de pedidos
- `src/billing/invoices/**/*.ts`
  - nó de ownership
  - aquele subtree é dono da lógica de faturas
- `src/**/*.ts, tests/**/*.ts, scripts/**/*.ts`
  - bom candidato de overlay para qualidade de linguagem ou testing quality
- `src/api/**/*.ts, src/billing/**/*.ts`
  - bom candidato de overlay para observabilidade

`docs/**/*.md` normalmente é seu próprio nó de ownership, e não um overlay.

A relação entre código e docs normalmente vem de follow-through, não de transformar docs em uma camada transversal.

## Erros Comuns

Trate estes pontos como erros de modelagem:

- usar overlays para representar owners mais estreitos
- nomear overlays pelos paths cruzados em vez de por uma concern coerente
- tratar documentação como concern transversal quando ela é uma superfície owned
- criar um novo nó de ownership apenas porque uma mudança tem consequências downstream

## Documentos Relacionados

- [Modelo Operacional](./modelo-operacional.md)
- [Follow-Through Triggers](./follow-through-triggers.md)
- [Regras de Decisão](../regras/regras-de-decisao.md)
- [Exemplos](../exemplos/README.md)
