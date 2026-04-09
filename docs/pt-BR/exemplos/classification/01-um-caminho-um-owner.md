# Um Caminho, Um Owner

## Cenário

Você tem este path:

```text
src/api/orders/create_order.ts
```

## Primeiro Palpite Errado

"Isto precisa ser um overlay porque é importante."

## Classificação Correta

Isto é um problema de ownership tree.

Nós prováveis de ownership:

- `src/**/*.ts`
- `src/api/**/*.ts`
- `src/api/orders/**/*.ts`

## Por Que

O path pertence a um boundary claro de responsabilidade:

- código,
- depois código de API,
- depois código da API de pedidos.

Isto é hierarquia por ownership, e não uma preocupação transversal.

## Follow-Through

Nenhuma revisão downstream é necessária, a menos que a mudança afete comportamento, contratos, config ou documentação.
