# Um Trigger Compartilhado Supera Cópias Locais Repetidas

## Cenário

Um repositório tem nós irmãos de ownership como:

```text
src/domain/orders/
src/domain/payments/
src/domain/invoices/
```

Cada instruction local começa a ganhar sua própria lista de triggers para testes, docs, exemplos e observabilidade.

## Primeiro Palpite Errado

"Todo nó com instruction também deveria ter sua própria lista local de triggers."

## Classificação Correta

Se a regra downstream é basicamente a mesma entre nós irmãos, a parte compartilhada normalmente pertence a um owner de origem mais amplo ou ao baseline.

Os nós mais estreitos devem manter apenas deltas realmente locais, ou nenhum trigger.

## Por Que

Enumeração local repetida entra em drift rapidamente:

- um nó esquece testes
- outro adiciona docs, mas esquece exemplos
- outro usa uma escrita diferente para a mesma ideia

Isso cria duplicação sem cobertura confiável.

## Forma Melhor

Regra compartilhada mais ampla:

- se comportamento público, significado de contrato, defaults ou expectativas operacionais mudaram, revise as superfícies downstream que codificam essas expectativas

Mantenha adições locais apenas quando elas forem realmente diferentes, como:

- um nó de pagamentos que também precisa revisar evidências de compliance
- um nó de invoices que também precisa revisar fixtures gerados de PDF

## Follow-Through

Fluxo esperado:

1. checar se o nó local realmente tem uma consequência downstream única,
2. se não tiver, remover o trigger local repetido e mover a regra compartilhada para cima,
3. manter no nó mais estreito apenas deltas realmente locais,
4. reutilizar o mesmo pequeno conjunto de skills para o review mais amplo em vez de inventar uma skill por trigger local.
