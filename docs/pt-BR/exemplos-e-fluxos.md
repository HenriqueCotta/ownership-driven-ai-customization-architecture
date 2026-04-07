# Exemplos e Fluxos

Público: mantenedores que querem entender a arquitetura por exemplos antes de desenhar sua própria estrutura.
Objetivo: ensinar a `Arquitetura de Personalização de IA Orientada a Ownership` com cenários simples e reutilizáveis de programação, e não com terminologia específica de um repositório.

## Como Usar Este Arquivo

Leia os exemplos em ordem.

Eles vão da distinção mais simples para fluxos mais realistas:

1. identificar o owner de um caminho,
2. identificar um overlay,
3. identificar uma consequência downstream,
4. decidir se outra superfície precisa ser revisada ou atualizada.

Cada exemplo segue o mesmo padrão de ensino:

- cenário
- primeiro palpite errado
- classificação correta
- por que ela está correta
- follow-through

## Exemplo 1: Um Caminho, Um Owner

### Cenário

Você tem este caminho:

```text
src/api/orders/create_order.ts
```

### Primeiro Palpite Errado

"Isto precisa ser um overlay porque é importante."

### Classificação Correta

Isto é um problema de ownership tree.

Nós prováveis de ownership:

- `src/**/*.ts`
- `src/api/**/*.ts`
- `src/api/orders/**/*.ts`

### Por Que

O caminho pertence a um boundary claro de responsabilidade:

- código,
- depois código de API,
- depois código da API de pedidos.

Isto é hierarquia por ownership, não uma preocupação transversal.

### Follow-Through

Nenhuma revisão downstream é necessária a menos que a mudança afete comportamento, contratos, config ou documentação.

## Exemplo 2: Um Overlay de Verdade

### Cenário

Você quer uma lente única de qualidade de testes que se aplique de forma transversal ao código de produção e aos testes:

```text
src/**/*.ts
tests/**/*.ts
```

### Primeiro Palpite Errado

"Testing deveria ser mais um nó de ownership embaixo de `src`."

### Classificação Correta

Isto é um cross-cutting overlay.

### Por Que

Testing não é owned por um único slice arquitetural como `api`, `billing` ou `docs`.

Ele atravessa vários slices e acrescenta uma lente extra:

- preferir testes focados em comportamento, e não em detalhes de implementação,
- manter fixtures pequenos e legíveis,
- cobrir casos de sucesso, falha e borda realmente relevantes,
- deixar claro no nome do teste qual comportamento está sendo validado.

É por isso que testing pode ser um overlay: ele adiciona uma lente de qualidade de testes sobre vários owners.

O que **não** faz testing virar overlay, por si só, é uma regra como:

- "se a lógica mudou em `src/**`, revise ou atualize os testes"

Isso normalmente é uma consequência de follow-through, não a definição do overlay.

### Follow-Through

Se uma mudança de comportamento acontecer em `src/api/orders/create_order.ts`, o trigger para revisar testes normalmente pertence ao owner do lado de `src` ou ao baseline, porque é ali que a mudança é melhor entendida.

Depois, quando o Copilot abrir os arquivos de teste, o overlay de testing ajuda a aplicar padrões específicos de testes.

Então o fluxo normalmente é:

1. um owner do lado de `src` diz que o comportamento mudou e que testes podem precisar de revisão,
2. o Copilot abre os arquivos de teste relevantes,
3. o overlay de testing ajuda a moldar como esses testes devem ser escritos ou revisados.

Superfícies típicas de teste:

- `tests/api/orders/create_order.test.ts`
- testes de integração,
- fixtures,
- helpers de teste

## Exemplo 3: Owner Mais Estreito vs Overlay

### Cenário

Você tem estes caminhos:

```text
src/api/orders/**/*.ts
src/billing/invoices/**/*.ts
```

### Primeiro Palpite Errado

"Estes são dois casos especiais, então deveriam ser overlays."

### Classificação Correta

Estes são nós mais estreitos da ownership tree.

### Por Que

Eles são diferentes porque cada subtree é dono de um tipo diferente de lógica:

- lógica da API de pedidos
- lógica de faturas

Isto é ownership.

Um overlay seria algo como:

```text
src/api/**/*.ts
src/billing/**/*.ts
```

para uma preocupação compartilhada, como observabilidade, retries ou error reporting.

### Follow-Through

Se você adicionar um novo estado ao ciclo de vida de uma fatura, talvez precise de:

- testes de billing
- docs de billing
- revisão de telemetria

Mas a decisão de ownership continua vindo primeiro: a lógica de faturas é owned pelo subtree de faturas.

## Exemplo 4: Mudança de Contrato

### Cenário

Você muda uma interface pública:

```text
src/contracts/payment_gateway.ts
```

### Primeiro Palpite Errado

"Só o arquivo de contrato mudou, então a mudança é local."

### Classificação Correta

Contexto principal de instruction:

- baseline
- instruction de qualidade de linguagem, se o repo usar uma
- nó da ownership tree para contratos

### Por Que

Contratos costumam ser arquivos pequenos com blast radius grande.

Mesmo que a edição seja local, o significado da mudança não é.

### Follow-Through

Uma seção `Follow-Through Triggers` na instruction de contrato pode dizer:

- se campos, defaults, semântica de retorno ou expectativas de compatibilidade mudarem, revise implementações, testes e docs de referência

Fluxo esperado:

1. mudar o contrato,
2. inspecionar implementações,
3. inspecionar testes,
4. inspecionar docs,
5. atualizar ou justificar explicitamente que não houve mudança downstream.

## Exemplo 5: Mudança de Configuração

### Cenário

Você muda o carregamento de config ou os defaults:

```text
src/config/load_config.ts
```

### Primeiro Palpite Errado

"Isto é plumbing interno, então só o arquivo de config importa."

### Classificação Correta

Contexto principal de instruction:

- baseline
- nó da ownership tree para configuração

Possíveis superfícies downstream:

- docs
- arquivos de exemplo de config
- testes

### Por Que

Mudanças de configuração frequentemente afetam o que usuários digitam, o que operadores esperam e o que os testes codificam.

### Follow-Through

Uma seção `Follow-Through Triggers` pode dizer:

- se precedência, defaults, regras de source of truth ou validação mudarem, revise exemplos, docs e testes

Fluxo esperado:

1. mudar o comportamento de config,
2. inspecionar configs de exemplo,
3. inspecionar testes,
4. inspecionar docs,
5. atualizar ou justificar no-op.

## Exemplo 6: Documentação Como Seu Próprio Owner

### Cenário

Você edita:

```text
docs/orders.md
```

### Primeiro Palpite Errado

"Documentação sempre deve ser um overlay porque se relaciona com código."

### Classificação Correta

`docs/**/*.md` normalmente é seu próprio nó da ownership tree.

### Por Que

Documentação é sua própria superfície, com suas próprias regras de qualidade:

- clareza,
- source of truth,
- estrutura,
- disciplina de atualização.

Ela se relaciona com código, mas esse relacionamento normalmente é expresso por follow-through, não transformando docs em overlay do código-fonte.

### Follow-Through

Se o doc estiver sendo alterado porque o código já mudou, o Copilot deveria verificar:

- a implementação atual,
- os testes relacionados,
- se o doc ainda está correto.

## Exemplo 7: Follow-Through de Board ou Task

### Cenário

Você termina uma implementação e percebe que o escopo mudou:

- um critério de aceitação não está mais correto
- um novo item de follow-up foi descoberto

### Primeiro Palpite Errado

"Task tracking deveria ser mais um owner embaixo de `src`."

### Classificação Correta

Task tracking normalmente é um cross-cutting overlay.

### Por Que

Ele atravessa muitos tipos de trabalho:

- código,
- docs,
- design,
- operação,
- rollout.

### Follow-Through

Uma seção `Follow-Through Triggers` pode dizer:

- se escopo, status, critérios de aceitação ou follow-up work mudarem materialmente, revise task tracking

Fluxo esperado:

1. reavaliar o que mudou,
2. decidir se a task ficou desatualizada,
3. atualizá-la se o workflow suportar isso,
4. caso contrário, explicar exatamente o que precisa ser atualizado.

## Exemplo 8: Nenhum Follow-Through Necessário

### Cenário

Você renomeia variáveis e simplifica um helper sem mudar comportamento:

```text
src/api/orders/normalize_input.ts
```

### Primeiro Palpite Errado

"Toda mudança deve forçar revisão de docs, testes e board."

### Classificação Correta

Isto continua sendo uma edição da ownership tree, mas pode não disparar trabalho downstream.

### Por Que

Nem toda mudança é mudança de comportamento.

Se nada público, contratual, operacional ou user-facing mudou, forçar follow-through cria ruído.

### Follow-Through

Um bom resultado é:

1. confirmar que a mudança preserva comportamento,
2. evitar edições downstream desnecessárias,
3. deixar essa decisão explícita na explicação.

## Checklist Rápido de Revisão

Depois de uma mudança relevante, pergunte:

1. Qual caminho é o owner primário deste arquivo?
2. Que nós mais amplos ou mais estreitos da ownership tree também se aplicam?
3. Há aqui uma preocupação transversal real, ou estou rotulando ownership como overlay por engano?
4. Uma seção existente de `Follow-Through Triggers` já descreve o que mais pode ter ficado desatualizado?
5. Se não, essa guidance deveria ser adicionada a uma instruction existente em vez de criar um novo arquivo?
