# Um Nó de Arquivo com Dois Arquivos de Instruction

## Cenário

Você tem este path de repositório:

```text
src/api/orders.ts
```

Esse arquivo precisa de dois tipos distintos de guidance:

- guidance de contrato
- guidance de framework

## Primeiro Palpite Errado

"Um arquivo só pode ter uma ownership instruction, então preciso de um workaround especial de nomenclatura."

## Classificação Correta

Isto continua sendo um único nó de ownership.

É um nó de nível de arquivo com dois arquivos de instruction.

## Por Que

O boundary owned continua sendo o próprio arquivo:

- `src/`
- `src/api/`
- `src/api/orders.ts/`

O nó não muda só porque precisa de mais de uma lente de guidance.

Só o conteúdo do nó muda.

## No Disco

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
        api/
          general.instructions.md
          orders.ts/
            contract.instructions.md
            framework.instructions.md
```

## Follow-Through

Se o contrato mudar, a instruction de contrato pode disparar revisão de testes e docs.

Se o fluxo de tratamento da request mudar, a instruction de framework pode disparar checks de integração.
