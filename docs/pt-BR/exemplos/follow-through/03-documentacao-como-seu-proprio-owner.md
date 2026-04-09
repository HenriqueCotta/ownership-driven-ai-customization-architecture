# Documentação como Seu Próprio Owner

## Cenário

Você edita:

```text
docs/orders.md
```

## Primeiro Palpite Errado

"Documentação sempre deve ser um overlay porque se relaciona com código."

## Classificação Correta

`docs/**/*.md` normalmente é seu próprio nó da ownership tree.

## Por Que

Documentação é sua própria superfície, com suas próprias regras de qualidade:

- clareza,
- source of truth,
- estrutura,
- disciplina de atualização.

Ela se relaciona com código, mas esse relacionamento normalmente é expresso por follow-through, e não por transformar docs em overlay do código-fonte.

## Follow-Through

Se o doc estiver sendo alterado porque o código já mudou, o Copilot deveria verificar:

- a implementação atual,
- os testes relacionados,
- se o doc ainda está correto.
