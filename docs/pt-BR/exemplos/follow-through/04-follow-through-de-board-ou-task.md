# Follow-Through de Board ou Task

## Cenário

Você termina uma implementação e percebe que o escopo mudou:

- um critério de aceitação não está mais correto
- um novo item de follow-up foi descoberto

## Primeiro Palpite Errado

"Task tracking deveria ser mais um owner em `src`."

## Classificação Correta

Se o repositório mantiver task tracking ou estado de planejamento dentro do mapa do repositório, isso normalmente é um overlay transversal.

Se essa superfície de carry-forward viver fora do repositório, ela permanece fora do mapa do repositório.

## Por Que

Quando um repositório decide preservar follow-through fora da memória da conversa, essa superfície de planejamento pode atravessar muitos tipos de trabalho:

- código,
- docs,
- design,
- operação,
- rollout.

## Follow-Through

Uma seção `Follow-Through Triggers` pode dizer:

- se escopo, status, critérios de aceitação ou follow-up work mudaram materialmente, revise a superfície explícita de carry-forward do repositório quando ela existir

Fluxo esperado:

1. reavaliar o que mudou,
2. usar o trigger para inspecionar o board, a task ou a superfície equivalente de carry-forward, se o repositório mantiver uma,
3. se a atualização for direta, fazê-la ali mesmo,
4. se o repositório usar um workflow mais amplo de planejamento ou review, reutilizar essa skill genérica em vez de criar uma skill específica para este trigger,
5. se o repositório tiver automações exatas de board, mantenha-as em scripts ou regras da própria plataforma; use skills para o workflow mais amplo de review ou planejamento em volta disso.
