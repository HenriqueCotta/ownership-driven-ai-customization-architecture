# Conflitos e Precedência de Instruções

Público: mantenedores que precisam desenhar um mapa de instructions seguro e evitar guidance ambígua.  
Objetivo: explicar o que a plataforma garante com clareza, o que ela não garante, e como escrever refinamento com segurança.

## Nesta Página

- [Realidade Operacional](#realidade-operacional)
- [Modelo Mental Seguro](#modelo-mental-seguro)
- [Padrão Seguro de Refinamento](#padrão-seguro-de-refinamento)
- [Regras Práticas de Precedência](#regras-práticas-de-precedência)
- [Sinais de Conflito](#sinais-de-conflito)
- [Como Corrigir um Conflito](#como-corrigir-um-conflito)
- [Documentos Relacionados de Arquitetura](#documentos-relacionados-de-arquitetura)

## Realidade Operacional

Esta seção descreve o modelo prático, não o idealizado.

O que a plataforma deixa claro:

- instructions de repositório inteiro e instructions path-specific compatíveis são fornecidas juntas quando o caminho bate
- fontes de instruction de nível mais alto têm precedência quando há conflito, por exemplo instruções pessoais sobre instruções de repositório, e instruções de repositório sobre instruções de organização

O que a plataforma não garante com clareza:

- um modelo totalmente determinístico de override estilo POO entre vários arquivos de instruction compatíveis do mesmo repositório
- uma regra publicada dizendo que "o caminho mais específico sempre vence" em qualquer caso

Isso significa que você não deve desenhar instructions de repositório como se fossem herança estrita com override garantido.

Use a ownership tree como disciplina de design, não como promessa de resolução automática de conflitos em runtime.

## Modelo Mental Seguro

O modelo mental mais seguro é:

- instructions mais amplas definem defaults
- instructions mais estreitas refinam esses defaults
- overlays adicionam outra lente
- `Follow-Through Triggers` descrevem consequências downstream

Se duas instructions compatíveis realmente se contradizem, o resultado é menos previsível do que herança normal em código.

## Padrão Seguro de Refinamento

Escreva instructions pai e filho como refinamento, não como reversão.

Bom:

- pai: "API handlers devem permanecer finos e delegar trabalho de negócio"
- filho: "Dentro de `src/api/orders/**`, mapeie cedo a entrada HTTP e chame diretamente os services de pedidos"

Ruim:

- pai: "API handlers devem permanecer finos e delegar trabalho de negócio"
- filho: "Dentro de `src/api/orders/**`, coloque validação, regras de negócio, persistência e retries diretamente no handler"

Por que o primeiro é mais seguro:

- o filho estreita o pai dentro de um boundary menor
- o filho adiciona detalhe local sem desfazer a regra maior

Por que o segundo é arriscado:

- o filho tenta reverter o pai
- se as duas instructions entrarem juntas, o modelo recebe guidance conflitante em vez de guidance refinada

## Regras Práticas de Precedência

Quando houver dúvida, use estas regras:

1. Coloque o default amplo no owner mais amplo que realmente for dono dele.
2. Coloque a especialização local no owner mais estreito que realmente precisar dela.
3. Coloque guidance de qualidade transversal em overlays.
4. Coloque regras downstream de follow-through em `Follow-Through Triggers`.
5. Ancore um trigger de follow-through na instruction que consegue observar a mudança de origem.
6. Reutilize um pequeno conjunto de skills orientadas a outcome em vez de criar uma skill por trigger.
7. Mantenha procedimentos exatos e repetíveis em scripts, CI ou runbooks.
8. Mantenha hints de descobribilidade dentro de docs ou instructions existentes em vez de inventar uma camada de hints.
9. Se duas instructions parecerem estar brigando, corrija o mapa de ownership em vez de esperar que a precedência resolva.

Em outras palavras:

- use a estrutura para reduzir conflito
- não dependa de precedência implícita para limpar conflito depois

## Sinais de Conflito

Trate estes pontos como sinais de que o mapa de instructions precisa de redesign:

- a mesma regra aparece em várias instructions
- uma instruction filha tenta reverter a pai em vez de refiná-la
- um overlay é nomeado pelos caminhos cruzados em vez de por uma concern coerente
- um caminho de docs é tratado como overlay quando deveria ser seu próprio owner
- uma nova instruction está sendo proposta apenas porque uma mudança tem consequências downstream
- uma nova skill é proposta para cada trigger ou owner
- passos procedurais exatos estão sendo copiados para instructions ou skills genéricas
- uma camada separada de hints está sendo proposta apenas para conectar triggers e skills

## Como Corrigir um Conflito

Quando houver conflito, comece pelo mapa:

1. Mova defaults amplos para o owner amplo real.
2. Mova especialização local para o owner estreito real.
3. Reescreva guidance filha como refinamento, e não como reversão.
4. Mova concerns realmente transversais para overlays.
5. Mantenha comportamento downstream de follow-through dentro de `Follow-Through Triggers`, em vez de inventar uma nova camada.
6. Mova qualquer regra de follow-through mal posicionada para o escopo de instruction que realmente consegue observar a mudança que a dispara.
7. Consolide variantes de workflow sobrepostas em um pequeno conjunto de skills orientadas a outcome, em vez de uma skill por trigger.
8. Mova passos procedurais exatos para scripts, CI ou runbooks quando a guidance em linguagem natural ficar frágil.
9. Mantenha qualquer texto de descobribilidade como uma pequena dica dentro de docs ou instructions já existentes, em vez de criar uma camada de hints.

Se o mapa estiver limpo, a necessidade de resolução dura de conflito normalmente cai bastante.

## Documentos Relacionados de Arquitetura

- [Ownership vs Overlay](../modelo/ownership-vs-overlay.md)
- [Follow-Through Triggers](../modelo/follow-through-triggers.md)
- [Regras de Decisão](./regras-de-decisao.md)
- [Gramática da Ownership Tree](./gramatica-da-ownership-tree.md)
- [Exemplos](../exemplos/README.md)
