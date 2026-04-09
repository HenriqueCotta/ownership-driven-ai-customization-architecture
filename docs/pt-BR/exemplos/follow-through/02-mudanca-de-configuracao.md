# Mudança de Configuração

## Cenário

Você muda o carregamento de config ou os defaults:

```text
src/config/load_config.ts
```

## Primeiro Palpite Errado

"Isto é plumbing interno, então só o arquivo de config importa."

## Classificação Correta

Contexto primário de instruction:

- baseline
- nó da ownership tree para configuração

Possíveis superfícies downstream:

- docs
- arquivos de exemplo de config
- testes

## Por Que

Mudanças de configuração frequentemente afetam o que usuários digitam, o que operadores esperam e o que os testes codificam.

## Follow-Through

Uma seção `Follow-Through Triggers` pode dizer:

- se precedência, defaults, regras de source of truth ou validação mudaram, revise exemplos, docs e testes

Fluxo esperado:

1. mudar o comportamento de config,
2. inspecionar configs de exemplo,
3. inspecionar testes,
4. inspecionar docs,
5. atualizar ou justificar no-op.
