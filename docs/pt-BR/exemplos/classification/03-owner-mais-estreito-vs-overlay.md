# Owner Mais Estreito vs Overlay

## Cenário

Você tem estes paths:

```text
src/api/orders/**/*.ts
src/billing/invoices/**/*.ts
```

## Primeiro Palpite Errado

"Estes são dois casos especiais, então deveriam ser overlays."

## Classificação Correta

Estes são nós mais estreitos da ownership tree.

## Por Que

Eles são diferentes porque cada subtree é dona de um tipo diferente de lógica:

- lógica da API de pedidos
- lógica de faturas

Isto é ownership.

Um overlay seria algo como:

```text
src/api/**/*.ts
src/billing/**/*.ts
```

para uma preocupação compartilhada, como observabilidade, retries ou error reporting.

## Follow-Through

Se você adicionar um novo estado ao ciclo de vida de uma fatura, talvez precise de:

- testes de billing
- docs de billing
- revisão de telemetria

Mas a decisão de ownership continua vindo primeiro: a lógica de faturas é owned pelo subtree de faturas.
