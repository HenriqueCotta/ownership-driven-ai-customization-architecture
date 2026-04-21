# Follow-Through Triggers

Público: mantenedores que precisam modelar follow-through downstream sem inventar camadas extras.
Objetivo: explicar o que `Follow-Through Triggers` é, por que existe e onde deve morar.

## Nesta Página

- [O Que Follow-Through Triggers É](#o-que-follow-through-triggers-é)
- [Por Que Existe](#por-que-existe)
- [Onde Mora](#onde-mora)
- [Triggers São Opcionais](#triggers-são-opcionais)
- [Triggers Ancorados na Origem](#triggers-ancorados-na-origem)
- [Relação com Skills e Automação](#relação-com-skills-e-automação)
- [Relação com Policy e Tracking](#relação-com-policy-e-tracking)
- [Como o Follow-Through Expande o Escopo](#como-o-follow-through-expande-o-escopo)
- [Triggers Típicos](#triggers-típicos)
- [O Que Não É](#o-que-não-é)
- [Referências Oficiais](#referências-oficiais)
- [Documentos Relacionados](#documentos-relacionados)

## O Que Follow-Through Triggers É

`Follow-Through Triggers` descreve que outras superfícies downstream podem agora precisar de atenção depois de uma mudança relevante.

É uma seção comportamental dentro de uma instruction.

Não é um tipo de arquivo separado nem outra camada arquitetural.

## Por Que Existe

Muitas mudanças importantes têm consequências secundárias:

- docs podem ter ficado desatualizadas
- testes podem precisar de atualização
- configs podem precisar de reconciliação
- runbooks, dashboards ou workflows podem precisar de ajuste

O modelo torna essas consequências explícitas para que elas não dependam só do jeito como a prompt foi escrita ou da memória do time.

## Onde Mora

`Follow-Through Triggers` deve morar dentro da instruction que melhor entende a origem da mudança.

Posicionamento default:

- baseline
  - para regras downstream curtas e válidas para o repositório inteiro
- nó de ownership
  - quando o owner da origem entende melhor o blast radius
- overlay
  - apenas quando a regra downstream realmente é owned por aquela concern transversal

## Triggers São Opcionais

Uma instruction não precisa ter uma seção `Follow-Through Triggers` só porque ela existe.

Adicione essa seção apenas quando aquela instruction conseguir dizer algo distinto e útil sobre follow-through downstream a partir do seu próprio escopo.

Se um owner mais amplo já disser bem a regra downstream, não a copie para filhos mais estreitos.

Se vários nós irmãos carregariam quase o mesmo trigger, mudando só a escrita ou pequenos itens de enumeração, mova a parte compartilhada para cima e deixe abaixo apenas deltas realmente locais.

Uma instruction sem trigger é normal quando ela não tem nenhuma consequência downstream única que valha a pena explicitar.

## Triggers Ancorados na Origem

A condição que dispara o trigger deve nascer de dentro do domínio onde aquela instruction é carregada.

Uma regra de follow-through pode apontar para paths ou superfícies fora do `applyTo` da instruction.

Mas, se o trigger depender de mudanças que aquela instruction não veria sozinha, a regra está mal posicionada.

Mova a regra para o escopo de instruction que realmente consegue observar a mudança de origem.

Isso pode significar mover a regra para cima, para o lado, ou até para outro owner de origem.

Por exemplo:

- se uma mudança em `X` deve disparar follow-through em `Y`, o trigger pertence à instruction que enxerga mudanças em `X`, e não à instruction de `Y`

Destinos comuns são:

- o baseline
  - quando a mudança de origem pode acontecer em qualquer lugar do repositório
- outro nó de ownership
  - quando um owner de origem diferente é quem realmente observa a mudança
- um nó de ownership mais amplo
  - quando um owner de origem mais amplo entende melhor o blast radius
- um overlay
  - apenas quando aquela concern transversal realmente é dona da regra downstream nos paths compatíveis

## Relação com Skills e Automação

Um trigger diz quais superfícies downstream podem precisar de atenção, verificação, reconciliação ou atualização.

Ele não define, por si só, o workflow para reconciliá-las.

Essa distinção importa porque muitos triggers diferentes podem reutilizar o mesmo pequeno conjunto de skills.

Por exemplo:

- um trigger de contrato, um trigger de configuração e um trigger de comportamento público podem reutilizar a mesma skill genérica de impact-review
- se o trabalho downstream for pequeno, nenhuma skill é necessária; inspecione as superfícies afetadas e atualize-as diretamente
- se o trabalho downstream exigir uma sequência exata e repetível, prefira scripts, checks de CI ou runbooks em vez de embutir esse procedimento no trigger

Não trate follow-through como uma tabela de despacho de tipos de trigger para skills correspondentes.

Se o time quiser ajuda de descobribilidade, mantenha isso como uma dica curta dentro de docs ou instructions existentes, em vez de introduzir uma camada separada de hints.

## Relação com Policy e Tracking

Triggers são apenas uma parte de um follow-through saudável.

Repositórios ainda precisam de uma forma de responder:

- quando trabalho downstream normalmente deve ser reconciliado agora
- quando ele deve virar follow-up explícito
- se um follow-through relevante adiado deve viver só na memória da conversa ou também em uma superfície explícita de carry-forward

É por isso que repositórios saudáveis frequentemente combinam triggers com:

- uma closure policy curta no baseline
- skills reutilizáveis para fluxo de decisão mais amplo
- automação para checks exatos e repetíveis
- quando fizer sentido, task tracking ou outra superfície explícita de carry-forward

Nem todo repositório precisa de um mecanismo dedicado de carry-forward.
Mas, quando um follow-through relevante é adiado intencionalmente, preservá-lo em uma superfície explícita fora da memória da conversa pode melhorar continuidade, recuperabilidade e colaboração de longo prazo.
Essa superfície ainda pode evoluir com o tempo; o objetivo é preservar continuidade, e não congelar o trabalho.

Esses elementos ainda não formam uma nova camada arquitetural.
Eles são apenas as outras superfícies do repositório que podem manter o follow-through explícito, governável e recuperável na prática.

Use [Modelo Operacional](./modelo-operacional.md), [Regras de Decisão](../regras/regras-de-decisao.md) e [Playbook de Replicação](../playbook-de-replicacao.md) em conjunto quando precisar desenhar essa composição em um repositório real.

## Como o Follow-Through Expande o Escopo

Follow-through normalmente começa em um owner e termina tocando vários outros.

Um fluxo típico se parece com isto:

1. o agente começa no owner de origem onde a mudança aconteceu
2. as ownership instructions e overlays compatíveis moldam a primeira análise
3. uma seção `Follow-Through Triggers` aponta para superfícies downstream que podem ter ficado stale
4. quando o agente abre essas novas superfícies, instructions path-specific desses paths também podem se tornar relevantes
5. se o trabalho virar um review mais amplo, uma reconciliação de docs ou um debugging mais profundo, o agente pode escolher uma skill genérica just-in-time

É por isso que follow-through deve continuar leve:

- ele expande o escopo
- ele não substitui a ownership tree
- ele não precisa de uma skill dedicada para cada trigger

O modelo documentado pelo GitHub sustenta essa leitura:

- instructions de repositório inteiro e instructions path-specific compatíveis podem se aplicar juntas
- skills são selecionadas em tempo de tarefa com base na prompt e na descrição da skill
- quando uma skill é selecionada, suas instruções entram no contexto do agente

Em outras palavras, follow-through pode revelar novas instructions e novas skills durante o trabalho, mas não deve ser modelado como uma cadeia rígida de despacho.

## Triggers Típicos

Exemplos típicos:

- um contrato público muda
  - revise consumers, docs e testes
- defaults de configuração mudam
  - revise pressupostos de rollout, docs e checks de runtime
- um comportamento muda em uma API pública
  - revise testes, docs e expectativas de tratamento de erro

## O Que Não É

`Follow-Through Triggers` não é:

- uma segunda ownership tree
- um motivo para criar novos arquivos de instruction por si só
- uma seção que toda instruction precisa conter
- uma tabela de despacho de categorias de trigger para skills correspondentes
- um checklist procedural de comandos exatos ou atualizações arquivo por arquivo
- uma camada arquitetural separada de hints
- um substituto para CI, review ou testes

É um lembrete estruturado de trabalho downstream provável.

## Referências Oficiais

- GitHub Docs, Adding repository custom instructions for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- GitHub Docs, Adding custom instructions for GitHub Copilot CLI  
  <https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions>
- GitHub Docs, Creating agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills>
- GitHub Docs, Using custom instructions to unlock the power of Copilot code review  
  <https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/use-custom-instructions>
- GitHub Docs, Support for different types of custom instructions  
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>

## Documentos Relacionados

- [Modelo Operacional](./modelo-operacional.md)
- [Ownership vs Overlay](./ownership-vs-overlay.md)
- [Regras de Decisão](../regras/regras-de-decisao.md)
- [Playbook de Replicação](../playbook-de-replicacao.md)
- [Exemplos](../exemplos/README.md)
