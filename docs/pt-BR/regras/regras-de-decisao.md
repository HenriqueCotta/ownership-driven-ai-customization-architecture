# Regras de Decisão

Público: mantenedores que precisam posicionar guidance corretamente sem adivinhação.  
Objetivo: fornecer um conjunto compacto de decisões para classificar instructions e reconhecer sinais de redesign.

## Nesta Página

- [Perguntas de Primeiro Contato](#perguntas-de-primeiro-contato)
- [Onde Cada Guidance Deve Morar](#onde-cada-guidance-deve-morar)
- [Separação Default Recomendada](#separação-default-recomendada)
- [Checks Rápidos de Classificação](#checks-rápidos-de-classificação)
- [Sinais de Redesign](#sinais-de-redesign)
- [Documentos Relacionados](#documentos-relacionados)

## Perguntas de Primeiro Contato

Ao classificar um path ou uma instruction proposta, comece com estas perguntas:

1. Que arquivo ou path está mudando?
2. Que owner estável é responsável por esse path?
3. Que concerns extras também se aplicam ali?
4. O que mais pode agora ter ficado desatualizado por causa dessa mudança?

Essas quatro perguntas se mapeiam diretamente a:

- `baseline`
- `ownership tree`
- `cross-cutting overlays`
- `Follow-Through Triggers`

## Onde Cada Guidance Deve Morar

Coloque guidance no baseline quando ela for:

- válida para o repositório inteiro
- curta
- amplamente útil
- improvável de mudar com frequência
- a closure policy do repositório para como o follow-through normalmente deve ser tratado

Coloque guidance em ownership quando ela for:

- ligada a uma família estável de paths
- específica daquele boundary de responsabilidade
- útil na maior parte do tempo naquele boundary

Coloque guidance em um cross-cutting overlay quando ela for:

- relevante em várias áreas de ownership
- não owned por um único slice arquitetural
- importante o bastante para ser carregada automaticamente nos paths compatíveis

Coloque guidance em uma skill quando ela for:

- um workflow reutilizável
- mais profunda do que política always-on
- não naturalmente presa a um único path

Mantenha guidance fora da ownership e overlay quando ela for:

- uma preferência individual que pertence a personal instructions ou a um perfil pessoal de agent
- uma preferência organizacional que pertence a organization instructions
- principalmente um perfil de tools, MCP ou permissões de agent, e não comportamento do repositório

Coloque guidance em automação ou em um runbook quando ela for:

- um procedimento exato e repetível
- mais clara como script, check de CI ou checklist operacional do que como prosa aberta
- esperada para executar de forma determinística

## Separação Default Recomendada

Quando mantenedores não souberem se uma regra é guidance local, follow-through, policy ou workflow, use esta interpretação default recomendada.

Ela não é uma nova camada arquitetural nem um template obrigatório de arquivo.
É apenas uma forma prática de classificar guidance dentro do modelo existente.

- se ignorar a regra deixaria a mudança errada dentro do escopo atual, ela normalmente é guidance local no baseline, no nó de ownership ou no overlay ativo
- se a mudança atual ainda pode estar correta por si só, mas pode deixar outras superfícies stale, isso normalmente é `Follow-Through Triggers`
- se a pergunta real for se esse trabalho downstream revelado normalmente deve ser reconciliado agora ou carregado adiante explicitamente, isso normalmente é closure policy de baseline
- se o conteúdo descreve principalmente um workflow reutilizável ou um procedimento exato para tratar esse trabalho, isso normalmente pertence a uma skill, automação ou runbook

## Checks Rápidos de Classificação

Use estes checks quando a escolha parecer nebulosa:

- se o path é dono de um tipo de lógica, provavelmente é ownership
- se uma concern extra atravessa vários owners, provavelmente é overlay
- se ignorar uma regra deixaria a mudança errada dentro do próprio escopo, ela provavelmente é guidance local no baseline, owner ou overlay ativo, e não follow-through
- se a mudança atual ainda pode estar correta por si só, mas pode deixar outras superfícies stale, provavelmente é follow-through
- se a pergunta principal é "o que mais pode agora precisar de follow-through downstream?", provavelmente é follow-through
- se um nó não tem nenhuma consequência downstream distinta que valha a pena explicar, omita a seção de trigger em vez de preenchê-la com repetição genérica
- se uma regra de follow-through depende de mudanças fora do escopo da própria instruction, mova-a para a instruction que realmente observa a mudança de origem, seja ela outro owner, um owner mais amplo, um overlay ou o baseline
- se vários nós irmãos ou próximos carregariam quase o mesmo trigger, mova a regra compartilhada para cima e deixe abaixo apenas deltas realmente locais
- se muitos casos downstream reutilizariam o mesmo workflow, prefira uma skill orientada a outcome em vez de uma skill por trigger
- se a pergunta real é "qual é a postura geral deste repositório sobre fechar follow-through agora versus carregá-lo para depois?", isto normalmente é policy de baseline, e não trigger nem skill
- se um owner mais amplo ainda entrega guidance honesta e útil, pare nele por agora em vez de aprofundar a tree preventivamente
- se o conteúdo descreve principalmente um fluxo reutilizável de trabalho, provavelmente é skill
- se o conteúdo prescreve principalmente comandos, arquivos ou ordem exata de etapas, provavelmente pertence à automação ou a um runbook
- se o conteúdo define principalmente tools, permissões ou perfil de execução de um agent especializado, provavelmente pertence à configuração do agent ou a settings, e não à prosa de follow-through
- se o único objetivo é ajudar leitores a descobrir guidance existente, mantenha isso como uma pequena dica dentro de docs ou instructions já existentes, em vez de introduzir uma camada de hints

Para a distinção conceitual, leia [Ownership vs Overlay](../modelo/ownership-vs-overlay.md).

Para consequências downstream, leia [Follow-Through Triggers](../modelo/follow-through-triggers.md).

Para entender como policy do repositório, skills reutilizáveis, automação e tracking se encaixam ao redor desses triggers, use [Modelo Operacional](../modelo/modelo-operacional.md) e [Playbook de Replicação](../playbook-de-replicacao.md).

## Sinais de Redesign

Trate estes pontos como sinais de que o mapa precisa de redesign:

- a mesma regra aparece em várias instructions
- uma prosa de trigger quase idêntica aparece em vários nós irmãos ou próximos
- uma instruction filha reverte a pai em vez de refiná-la
- um overlay é nomeado pelos paths cruzados em vez de por uma concern coerente
- um path de docs é tratado como overlay quando deveria ser seu próprio owner
- uma nova instruction é proposta apenas porque uma mudança tem consequências downstream
- o mapa continua crescendo até nós leaf mais estreitos antes de owners mais amplos terem provado que são insuficientes
- um trigger está sendo adicionado a quase toda instruction mesmo quando ele não diz nada localmente distinto
- uma nova skill está sendo proposta para cada trigger ou owner
- checklists procedurais exatos estão vivendo em instructions genéricas ou skills genéricas
- uma nova camada de hints está sendo proposta apenas para conectar triggers e skills
- mantenedores não conseguem prever quais instructions se aplicam a um arquivo

## Documentos Relacionados

- [Modelo Operacional](../modelo/modelo-operacional.md)
- [Ownership vs Overlay](../modelo/ownership-vs-overlay.md)
- [Follow-Through Triggers](../modelo/follow-through-triggers.md)
- [Playbook de Replicação](../playbook-de-replicacao.md)
- [Gramática da Ownership Tree](./gramatica-da-ownership-tree.md)
