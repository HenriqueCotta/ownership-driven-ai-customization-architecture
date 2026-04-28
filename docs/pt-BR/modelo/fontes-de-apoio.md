# Fontes de Apoio

Público: mantenedores cujos repositórios às vezes precisam de docs locais, docs externas, sistemas privados ou outras evidências fora das instructions ativas.  
Objetivo: definir a menor forma útil de tornar essas fontes localizáveis, governáveis e seguras de usar sem transformá-las em outra camada do ODA.

## Nesta Página

- [Regra Central](#regra-central)
- [Onde a Guidance de Fontes Mora](#onde-a-guidance-de-fontes-mora)
- [Entradas de Fonte São Flexíveis](#entradas-de-fonte-são-flexíveis)
- [Como Instructions Consumidoras Referenciam Fontes](#como-instructions-consumidoras-referenciam-fontes)
- [Quando Uma Fonte Precisa da Própria Instruction](#quando-uma-fonte-precisa-da-própria-instruction)
- [Quando Uma Fonte Basta](#quando-uma-fonte-basta)
- [Quando Várias Fontes São Necessárias](#quando-várias-fontes-são-necessárias)
- [Como Duplicar Conhecimento de Fonte com Segurança](#como-duplicar-conhecimento-de-fonte-com-segurança)
- [Tratamento de Conflitos](#tratamento-de-conflitos)
- [Relação com Triggers, Skills e MCP](#relação-com-triggers-skills-e-mcp)
- [Erros Comuns](#erros-comuns)
- [Referências Oficiais](#referências-oficiais)
- [Documentos Relacionados](#documentos-relacionados)

## Regra Central

Fontes de apoio são evidência auxiliar opcional.

Elas não são uma quarta camada estrutural na fórmula do ODA.

A fórmula estrutural continua:

- `baseline + ownership tree + cross-cutting overlays`

Instructions carregam o contrato ativo.

Fontes de apoio explicam onde vive a evidência mais profunda ou viva, como acessá-la, que tipo de claim ela pode responder e o que fazer quando acesso ou concordância entre fontes falhar.

Use fontes de apoio apenas quando guidance vaga como "verifique os docs" for fraca demais.

## Onde a Guidance de Fontes Mora

O ODA não exige um único nome de arquivo.

### Padrão Preferido

O padrão local mais comum em repositórios é uma instruction de fontes de apoio owned pelo owner raiz do repositório:

```text
.github/
  copilot-instructions.md
  instructions/
    ownership/
      repository/
        supporting-sources.instructions.md
```

```md
---
applyTo: "**"
---

# Supporting Sources

Use these sources only when they could change the decision.
```

Mantenha o baseline pequeno. Ele pode apontar para a instruction de fontes com uma regra curta:

```md
When deeper or live evidence could change a decision, use the repository supporting-source instructions.
```

### Owner Raiz do Repositório

Use `ownership/repository/` quando a guidance de fontes pertencer ao owner raiz do repositório.

Coloque ali quando ela fizer parte do contrato do owner raiz: o mapa repo-wide de evidência mais profunda, autoridade das fontes, fallback e tratamento de conflito.

Este é um nó raiz real. Outros owners top-level do repositório, como `docs/` ou `src/`, ficam abaixo de `ownership/repository/`, e não ao lado dele.

O nome de pasta `repository/` é uma convenção literal, não o nome real do repositório.

Não use `ownership/` em si como gaveta para qualquer regra global.

Guidance de fontes continua sendo evidência auxiliar.

Ela não deve virar um segundo baseline, um registro de fontes para todo documento ou outra ownership tree.

### Outras Superfícies

Para policy de fontes voltada ao agente, prefira uma instruction do Copilot.

Outras superfícies podem guardar informações de fonte, mas elas não têm a mesma garantia de carregamento por si só.

Elas são saudáveis apenas quando guidance ativa aponta explicitamente para elas e explica quando consultá-las.

A superfície exata é menos importante do que tornar a fonte alcançável sem fingir que ela é carregada automaticamente.

Evite colocar um `.github/sources.md` solto no repositório como se o Copilot fosse carregá-lo automaticamente.

Uma nota de fontes fora de instruction ainda pode ser útil, mas tem menor garantia a menos que uma instruction ou workflow carregado faça o agente consultá-la.

Escolha o lugar mais leve que torne a fonte fácil de encontrar e difícil de usar mal, e seja honesto sobre quão confiavelmente esse lugar entra em contexto.

## Entradas de Fonte São Flexíveis

Uma entrada de fonte não é um schema obrigatório.

Ela pode ser uma linha, um card compacto, uma linha de tabela ou uma nota mais rica.

Prefira um ID estável de fonte para que instructions consumidoras possam apontar para ele com clareza:

```md
## product-docs

Where: `docs/product/`
Use for: product intent and user-facing semantics.
```

Instructions consumidoras devem referenciar o ID:

```md
Use supporting source `product-docs`.
```

Use apenas os campos que importam para a fonte.

Campos úteis costumam incluir:

- onde a fonte vive
- como ela pode ser acessada
- que tipo de claim ela pode responder
- se verificação atual importa
- o que fazer se o acesso falhar
- como lidar com conflito com código, docs, testes, instructions ou intenção do usuário

Não exija que toda entrada de fonte carregue todos os campos.

O objetivo é guidance suficiente para o nível de risco do repositório, não um formulário para preencher.

## Como Instructions Consumidoras Referenciam Fontes

Instructions consumidoras devem manter visível o contrato local ativo.

Elas devem referenciar uma fonte de apoio apenas quando a evidência da fonte puder mudar a decisão.

Bom:

```md
# Payment Provider Adapter

Keep provider-specific behavior isolated in this adapter.

Before changing provider-owned fields, auth behavior, idempotency, rate limits, or error semantics, use supporting source `payment-provider-docs`.

If provider docs are unavailable, do not introduce behavior that depends on unverified provider support.
```

Arriscado:

```md
Follow the current provider docs.
```

A versão arriscada esconde o contrato local atrás de um ponteiro vago.

A versão saudável diz o que pertence ao adapter e usa a fonte apenas para fatos owned pelo provider.

## Quando Uma Fonte Precisa da Própria Instruction

Evite instructions de interpretação específica por fonte por default.

A maioria das fontes deve continuar como entradas compactas na instruction de fontes de apoio do repositório.

Isso mantém o mapa de fontes fácil de escanear e evita manter detalhe específico de uma fonte no contexto de toda tarefa.

Crie uma instruction separada de interpretação específica por fonte apenas quando a guidance for policy de interpretação owned pelo repo, guidance de fonte mais leve não conseguir carregá-la com segurança, e mantê-la na instruction central de fontes deixaria o mapa de fontes mais difícil de escanear.

Se a guidance for principalmente procedural, mantenha-a fora de instructions always-on e aponte para a superfície de workflow que possui o procedimento.

Coloque interpretação repo-wide específica de fonte no owner raiz do repositório:

```text
.github/
  instructions/
    ownership/
      repository/
        supporting-sources.instructions.md
        work-board.instructions.md
```

Tenha cuidado com `applyTo: "**"`.

As custom instructions atuais do Copilot são roteadas principalmente por repositório e path. Se uma interpretação específica de fonte pode se aplicar em qualquer lugar, `applyTo: "**"` pode ser o formato portável disponível, mas isso também significa que a guidance fica efetivamente sempre ligada nas surfaces que suportam path-specific instructions.

Use esse custo de propósito.

Prefira guidance ativa de fonte mais leve quando isso bastar.

Boa instruction de interpretação específica por fonte:

```md
---
applyTo: "**"
---

# Work Board Interpretation

Use this instruction only when the task involves planned work, deferred follow-through, issue status, release coordination, or board-backed decisions.

The board owns planning state and explicit carry-forward. It does not prove current implementation behavior unless linked to merged code, tests, or accepted docs.

Do not create, move, close, or rewrite board items unless the user asks for board changes or the repository closure policy requires explicit carry-forward.
```

A entrada correspondente de fonte pode continuar compacta:

```md
## work-board

Where: board `checkout-work`
Access: project-management MCP, if available.
Use for: planned work, accepted follow-ups, and explicit carry-forward.
Details: use `ownership/repository/work-board.instructions.md` only when board interpretation could change the decision.
```

Se a fonte exigir operações exatas, use uma superfície procedural explícita em vez de esticar uma instruction always-on.

## Quando Uma Fonte Basta

Alguns repositórios precisam de uma só fonte local.

Isso pode continuar simples:

```md
## product-docs

Where: `docs/product/`
Use for: user-facing behavior and product wording.
If unavailable: preserve existing behavior and surface the missing product context when it could change the result.
```

Um owner pode consumi-la diretamente:

```md
If a change alters customer-visible behavior, use supporting source `product-docs` before treating the change as complete.
```

Nenhum workflow extra de fontes é necessário quando a fonte é local e óbvia.

## Quando Várias Fontes São Necessárias

Mudanças mais complexas podem precisar de várias fontes porque claims diferentes têm owners diferentes.

```md
Before changing invoice tax behavior, use supporting source `finance-policy` for compliance constraints and `product-docs` for customer-facing semantics.

Use supporting source `payment-provider-docs` only for provider-owned fields, limits, and API behavior.
```

Isso não é enumeração por si só.

É uma forma de impedir que uma fonte vire a verdade inteira para claims que ela não possui.

## Como Duplicar Conhecimento de Fonte com Segurança

Às vezes um pequeno resumo local deve aparecer em uma instruction de owner mesmo quando a fonte autoritativa vive em outro lugar.

Isso é útil quando perder acesso à fonte poderia levar o agente a relaxar um invariante importante.

Bom:

```md
Invoices must remain tax-inclusive at display boundaries.

Local safety summary: existing invoice displays are tax-inclusive. If supporting source `finance-policy` is unavailable, this summary may preserve current behavior, but it must not justify a new tax rule.
```

Arriscado:

```md
Tax is 17.5%. Discounts use rule ABC. Regional exceptions are listed below...
```

Não copie detalhes longos, voláteis ou owned por policy para instructions locais.

Um resumo local deve atuar como guarda contra mudança insegura, não como espelho stale da fonte autoritativa.

## Tratamento de Conflitos

Coloque a regra geral de conflito onde as entradas de fonte vivem.

Depois adicione notas de conflito por fonte apenas quando uma fonte precisar de refinamento local.

Exemplo:

```md
## Conflict Handling

When sources diverge, classify the disputed claim first: implementation behavior, product intent, external platform fact, policy, planned work, or design-system contract.

Prefer the source that owns that claim. If the owning source is unavailable and the missing fact could change the result, treat that part as verification-blocked.

Do not let external provider docs override repository product intent, policy constraints, or local security rules. Do not let local mirrors override current provider facts.
```

Notas específicas de fonte podem refinar isso:

```md
## payment-provider-docs

Where: `https://provider.example/docs`
Use for: provider-owned fields, limits, auth, errors, and API behavior.
If it conflicts: current provider docs own provider facts; local notes may be stale.
```

## Relação com Triggers, Skills e MCP

Uma consulta de fonte pertence à instruction consumidora quando a fonte é necessária para fazer a mudança atual corretamente.

Uma seção `Follow-Through Triggers` é o lugar certo quando uma mudança pode deixar outra superfície stale.

Uma entrada de fonte de apoio é o lugar certo para localização, acesso, autoridade, frescor, fallback e guidance de conflito.

Uma skill é o lugar certo quando consulta ou reconciliação de fontes vira um workflow repetível.

Um servidor MCP é um mecanismo de acesso.

Ele pode permitir que o agente acesse sistemas externos. Ele não decide que fonte possui que claim. A instruction de fontes ainda precisa dizer o que a fonte pode responder e o que fazer quando acesso ou concordância falhar.

## Erros Comuns

Trate estes pontos como erros de modelagem:

- adicionar um link solto e assumir que o agente vai carregá-lo ou confiá-lo corretamente
- criar um registro gigante de todos os documentos do repositório
- criar uma entrada de fonte por tópico quando uma família de fontes mais ampla basta
- esconder o contrato ativo inteiro dentro de uma fonte
- exigir uma fonte privada sem expectativa de acesso ou fallback
- deixar uma fonte sobrescrever claims que ela não possui
- usar um resumo local como se ele fosse a fonte autoritativa atual
- criar uma instruction always-on específica por fonte quando guidance de fonte mais leve bastaria
- transformar guidance de fontes em outra ownership tree

## Referências Oficiais

- GitHub Docs, Adding repository custom instructions for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- GitHub Docs, Adding agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills>
- GitHub Docs, Copilot customization cheat sheet
  <https://docs.github.com/en/copilot/reference/customization-cheat-sheet>
- GitHub Docs, About Model Context Protocol
  <https://docs.github.com/en/copilot/concepts/context/mcp>
- GitHub Docs, Support for different types of custom instructions  
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>

## Documentos Relacionados

- [Modelo Operacional](./modelo-operacional.md)
- [Regras de Decisão](../regras/regras-de-decisao.md)
- [Follow-Through Triggers](./follow-through-triggers.md)
- [Conflitos e Precedência de Instruções](../regras/conflitos-e-precedencia-de-instrucoes.md)
- [Exemplos de Fontes de Apoio](../exemplos/fontes-de-apoio/README.md)
