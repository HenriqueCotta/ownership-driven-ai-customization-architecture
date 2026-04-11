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
2. usar o trigger para inspecionar implementações, testes e docs,
3. se o trabalho downstream for pequeno, atualizar essas superfícies diretamente,
4. se a mudança revelar um drift mais amplo de documentação, reutilizar uma skill genérica de sync de docs ou de review,
5. se o repositório tiver scans de compatibilidade ou comandos de validação exatos, mantenha-os em automação ou runbooks; use skills para o workflow mais amplo de review em volta disso.
