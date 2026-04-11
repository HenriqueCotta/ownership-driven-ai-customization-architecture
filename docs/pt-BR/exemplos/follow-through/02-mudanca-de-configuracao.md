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
2. usar o trigger para inspecionar configs de exemplo, testes e docs,
3. se o trabalho downstream for pequeno, atualizar essas superfícies diretamente,
4. se a mudança revelar um drift mais amplo de docs ou operação, reutilizar uma skill genérica de sync de docs ou de review,
5. se o repositório tiver comandos exatos de validação ou checks de rollout, mantenha-os em automação ou runbooks; use skills para o workflow mais amplo de review em volta disso.
