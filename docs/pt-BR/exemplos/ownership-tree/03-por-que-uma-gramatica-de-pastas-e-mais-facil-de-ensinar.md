# Por Que uma Gramática de Pastas é Mais Fácil de Ensinar

## Cenário

Um novo mantenedor precisa entender quais ownership instructions se aplicam a:

```text
src/api/orders.ts
```

## Primeiro Palpite Errado

"Precisamos de uma explicação especial para owners de diretório e outra explicação para owners de arquivo."

## Classificação Correta

O mesmo roteiro de ensino funciona para ambos:

1. encontre o path do repositório,
2. percorra o mesmo path dentro de `ownership/`,
3. leia os arquivos de instruction nas pastas de nó correspondentes.

## Por Que

Esse roteiro funciona porque a pasta é sempre o nó.

O leitor não precisa memorizar:

- exceções de nó de arquivo
- regras de promoção
- significados escondidos em nomes de arquivo

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
```

## Follow-Through

Quando o leitor entende quais nós de ownership se aplicam, ele pode avaliar overlays e follow-through da forma usual.
