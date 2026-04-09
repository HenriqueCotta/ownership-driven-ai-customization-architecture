# Mudança de Contrato

## Cenário

Você muda uma interface pública:

```text
src/contracts/payment_gateway.ts
```

## Primeiro Palpite Errado

"Só o arquivo de contrato mudou, então a mudança é local."

## Classificação Correta

Contexto primário de instruction:

- baseline
- instruction de qualidade de linguagem, se o repo usar uma
- nó da ownership tree para contratos

## Por Que

Contratos costumam ser arquivos pequenos com blast radius grande.

Mesmo que a edição seja local, o significado da mudança não é.

## Follow-Through

Uma seção `Follow-Through Triggers` na instruction de contrato pode dizer:

- se campos, defaults, semântica de retorno ou expectativas de compatibilidade mudaram, revise implementações, testes e docs de referência

Fluxo esperado:

1. mudar o contrato,
2. inspecionar implementações,
3. inspecionar testes,
4. inspecionar docs,
5. atualizar ou justificar explicitamente que não houve mudança downstream.
