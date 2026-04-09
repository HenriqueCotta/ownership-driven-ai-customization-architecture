# Um Overlay de Verdade

## Cenário

Você quer uma lente compartilhada de qualidade de testes que se aplique tanto ao código de produção quanto aos testes:

```text
src/**/*.ts
tests/**/*.ts
```

## Primeiro Palpite Errado

"Testing deveria ser mais um nó de ownership em `src`."

## Classificação Correta

Isto é um overlay transversal.

## Por Que

Testing não é owned por um único slice arquitetural como `api`, `billing` ou `docs`.

Ele atravessa vários slices e adiciona uma lente extra:

- preferir testes focados em comportamento, e não em detalhes de implementação,
- manter fixtures pequenos e legíveis,
- cobrir casos de sucesso, falha e borda realmente relevantes,
- manter nomes de testes claros sobre qual comportamento está sendo validado.

É por isso que testing pode ser um overlay: ele adiciona uma lente de testes sobre vários owners.

O que **não** faz testing virar overlay, por si só, é uma regra como:

- "se a lógica mudar em `src/**`, revise ou atualize os testes"

Isto normalmente é uma consequência de follow-through, e não a definição do overlay.

## Follow-Through

Se uma mudança de comportamento acontecer em `src/api/orders/create_order.ts`, o trigger para revisar testes normalmente pertence ao owner do lado de `src` ou ao baseline, porque é ali que a mudança é melhor entendida.

Depois, quando o Copilot abrir arquivos de teste, o overlay de testing ajuda a aplicar padrões específicos de testes.

Isto significa que o fluxo normalmente é:

1. um owner do lado de `src` diz que o comportamento mudou, então os testes podem precisar de revisão,
2. o Copilot abre os arquivos de teste relevantes,
3. o overlay de testing ajuda a moldar como esses testes devem ser escritos ou revisados.

Superfícies típicas de teste:

- `tests/api/orders/create_order.test.ts`
- testes de integração,
- fixtures,
- helpers de teste
