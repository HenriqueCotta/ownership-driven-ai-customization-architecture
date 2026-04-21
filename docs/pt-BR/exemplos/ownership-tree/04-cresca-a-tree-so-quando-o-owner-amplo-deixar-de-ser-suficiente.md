# Cresça a Tree Só Quando o Owner Amplo Deixar de Ser Suficiente

## Cenário

Um time começa a adoção do ODA em:

```text
src/app/
```

e quer criar instructions imediatamente para:

```text
src/app/
src/app/checkout/
src/app/checkout/forms/
src/app/checkout/forms/address/
src/app/checkout/forms/payment/
```

## Primeiro Palpite Errado

"Se não mapearmos todos os níveis agora, então não estamos aplicando ODA de verdade."

## Classificação Correta

Comece pelo owner mais amplo que ainda fornece guidance honesta e útil.

Adicione nós mais estreitos apenas depois que um subtree provar que precisa de guidance local diferente.

## Por Que

Trees profundas cedo demais costumam criar:

- conjuntos longos de instructions com pouco valor local
- escrita repetida entre nós próximos
- falsa precisão antes de o time entender onde os boundaries reais estão

O ODA foi feito para crescer, e não para ser finalizado todo de uma vez.

## Melhor Primeiro Pass

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
      src/app/
        general.instructions.md
```

Depois, se checkout realmente precisar de guidance distinta:

```text
.github/
  instructions/
    ownership/
      src/
        general.instructions.md
      src/app/
        general.instructions.md
        checkout/
          general.instructions.md
```

## Follow-Through

Fluxo esperado:

1. começar pelo owner amplo,
2. validar trabalho real contra esse owner,
3. adicionar um nó mais estreito apenas quando o nó amplo deixar de bastar,
4. evitar criar instructions de nós leaf só para espelhar a tree do repositório.
