# Filhos Mistos sob um Mesmo Pai

## Cenário

Você tem esta estrutura de repositório:

```text
src/routes/
  health.ts
  orders.ts
  admin/
    users.ts
```

## Primeiro Palpite Errado

"A tree fica confusa aqui porque alguns filhos são arquivos e um filho é uma pasta."

## Classificação Correta

Isto é uma forma normal da ownership tree.

Um mesmo pai pode conter:

- nós de arquivo
- nós de diretório mais estreitos
- arquivos de instruction para o próprio pai

## Por Que

Todos estes são filhos do mesmo boundary owned:

- `src/routes/health.ts`
- `src/routes/orders.ts`
- `src/routes/admin/`

A gramática por pastas lida com isso naturalmente porque tanto arquivos quanto diretórios do repositório são representados como pastas de nó.

## No Disco

```text
.github/
  instructions/
    ownership/
      src/
        routes/
          general.instructions.md
          health.ts/
            diagnostics.instructions.md
          orders.ts/
            contract.instructions.md
            framework.instructions.md
          admin/
            authorization.instructions.md
            users.ts/
              validation.instructions.md
```

## Follow-Through

O nó pai pode carregar guidance ampla de rotas.

Cada nó filho pode carregar comportamento mais estreito sem forçar uma segunda gramática de tree.
