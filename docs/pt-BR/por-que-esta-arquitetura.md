# Por Que Esta Arquitetura

Público: mantenedores, times de plataforma e lideranças de engenharia avaliando se vale a pena adotar este padrão.  
Objetivo: explicar o caso de negócio, a justificativa técnica, os ganhos esperados, os limites e o alinhamento com guidance oficial.

## Ir Para

- [Resumo Executivo](#resumo-executivo)
- [Por Que o Modelo Faz Sentido](#por-que-o-modelo-faz-sentido)
- [Por Que o Baseline Fica Intencionalmente Curto](#por-que-o-baseline-fica-intencionalmente-curto)
- [Por Que o Modelo É Path-First](#por-que-o-modelo-é-path-first)
- [Por Que a Ownership Tree Usa Uma Única Gramática de Pastas](#por-que-a-ownership-tree-usa-uma-única-gramática-de-pastas)
- [Por Que Skills Ficam Opcionais e Seletivas](#por-que-skills-ficam-opcionais-e-seletivas)
- [Ganhos Esperados](#ganhos-esperados)
- [Por Que Isto Escala](#por-que-isto-escala)
- [Por Que Isto É Mais Seguro do Que Customização Ad Hoc](#por-que-isto-é-mais-seguro-do-que-customização-ad-hoc)
- [Realidade de Suporte e Portabilidade](#realidade-de-suporte-e-portabilidade)
- [Limites e Não-Objetivos](#limites-e-não-objetivos)
- [Alinhamento com Guidance Oficial](#alinhamento-com-guidance-oficial)
- [Notas de Design da Documentação](#notas-de-design-da-documentação)
- [Referências](#referências)

## Resumo Executivo

`Ownership-Driven AI Customization Architecture` existe para resolver um problema prático:

- instruções customizadas de repositório normalmente começam pequenas
- depois colapsam em um único arquivo geral muito grande ou em várias regras sobrepostas
- e acabam ficando difíceis de confiar, difíceis de evoluir e difíceis de reutilizar entre repositórios

Esta arquitetura responde a isso com um conjunto pequeno de decisões estruturais estáveis:

- manter a guidance geral do repositório curta
- rotear a maior parte do comportamento por caminhos de ownership estáveis
- adicionar overlays apenas para concerns que realmente atravessam vários owners
- manter o comportamento downstream de revisão e atualização explícito com `Follow-Through Triggers`
- usar skills apenas para workflows mais profundos que não devem ficar sempre ativos

## Por Que o Modelo Faz Sentido

Este modelo segue a forma como a customização do GitHub Copilot funciona hoje.

A documentação do GitHub recomenda instruções curtas e autocontidas, e documenta que instruções gerais do repositório e instruções path-specific compatíveis são usadas juntas. O GitHub também nota que conflitos devem ser evitados porque a escolha do Copilot entre orientações conflitantes é não determinística.

Essa combinação leva a uma conclusão prática de design:

- manter o baseline curto
- usar ownership path-based como mecanismo principal de roteamento
- manter overlays estreitos e com propósito claro
- reduzir duplicação antes que ela chegue ao modelo

Skills seguem a mesma lógica. O GitHub recomenda custom instructions para orientações simples e relevantes para quase toda tarefa, e skills para guidance mais detalhada que o Copilot deve acessar apenas quando for relevante.

## Por Que o Baseline Fica Intencionalmente Curto

Esta arquitetura é intencionalmente cética com arquivos gerais de instrução grandes demais.

Isso não é apenas preferência de estilo.

Vem diretamente da plataforma:

- o GitHub recomenda instruções curtas e autocontidas
- o GitHub recomenda instruções path-specific para evitar sobrecarregar a camada geral do repositório com guidance que só vale para certos arquivos
- o GitHub documenta que o Copilot code review lê apenas uma parte limitada de cada arquivo de custom instruction

Essas restrições tornam um baseline grande estruturalmente fraco:

- ele fica mais difícil de manter
- aumenta o risco de conflito
- e parte dele pode nem estar visível em superfícies importantes, como code review

## Por Que o Modelo É Path-First

Esta arquitetura trata paths estáveis como a espinha dorsal principal de roteamento.

Essa escolha é prática, não ideológica.

Tanto o GitHub quanto o VS Code suportam instruções path-specific em `.github/instructions/**/*.instructions.md`, e o VS Code documenta que esses arquivos podem ser organizados recursivamente em subdiretórios.

Isso dá aos times uma unidade concreta e escalável de organização:

- owners amplos
- owners mais estreitos
- overlays só quando uma concern realmente atravessa esses boundaries de ownership

Roteamento path-first é mais fácil de entender do que roteamento por temas abstratos porque ele fica ancorado na estrutura real do repositório.

## Por Que a Ownership Tree Usa Uma Única Gramática de Pastas

A arquitetura não para em "usar paths".

Ela também recomenda um layout canônico no disco para os nós de ownership:

- todo boundary owned vira uma pasta de nó
- diretórios do repositório continuam diretórios
- arquivos do repositório também podem virar pastas de nó
- os arquivos de instruction dentro do nó são nomeados pela concern

Essa escolha importa porque sistemas mistos de nomenclatura normalmente criam atrito:

- alguns nós parecem arquivos e outros parecem pastas
- owners de arquivo precisam ser renomeados depois quando ganham uma segunda instruction
- novos mantenedores precisam aprender exceções antes de conseguirem ler a árvore com confiança

Uma gramática única de pastas evita esses problemas.

Ela é mais ensinável porque a explicação vira:

1. encontre o caminho no repositório
2. caminhe pelo mesmo caminho dentro de `ownership/`
3. leia os arquivos de instruction nas pastas de nó correspondentes

Ela é mais escalável porque:

- um arquivo pode ter um ou vários arquivos de instruction sem mudar de identidade
- filhos mistos são naturais
- nomes baseados em concern continuam fazendo sentido quando paths evoluem
- os times conseguem estender a árvore sem redesenhar a convenção de nomes

## Por Que Skills Ficam Opcionais e Seletivas

A arquitetura inclui skills, mas evita transformá-las no mecanismo principal de roteamento.

Isso também é apoiado por guidance oficial:

- o GitHub recomenda skills para instruções mais detalhadas que só devem ser acessadas quando relevantes
- a documentação do Copilot CLI diz explicitamente que, se o comportamento é necessário apenas em um workflow, uma skill é a melhor escolha
- a mesma documentação alerta para não sobrecarregar a janela de contexto do Copilot com instruções que não são relevantes para a tarefa atual

É por isso que skills aparecem aqui como extensões de workflow, e não como fundação do modelo.

## Ganhos Esperados

### Menor Atrito de Prompt

Os times deixam de repetir o mesmo contexto do repositório em toda prompt.

### Melhor Disciplina de Roteamento

O contexto relevante fica preso a paths e concerns estáveis, em vez de ficar espalhado em um único arquivo enorme.

### Menos Duplicação e Conflito

Os nós de ownership carregam a guidance comportamental local. Os overlays adicionam lentes transversais. Essa separação reduz a chance de a mesma regra aparecer em vários lugares com pequenas variações.

### Melhor Escalabilidade Entre Repositórios

O modelo é reutilizável porque depende de poucas ideias estruturais, e não da linguagem de domínio de um único projeto.

### Melhor Higiene Downstream

`Follow-Through Triggers` deixa visível o trabalho secundário:

- docs que podem ter ficado desatualizadas
- testes que podem precisar de atualização
- configs que podem precisar de revisão
- artefatos de workflow que podem precisar de ajuste

### Melhor Disciplina de Custo

A arquitetura mantém o contexto always-on pequeno de propósito e empurra workflows mais profundos para skills opcionais.

## Por Que Isto Escala

O modelo escala porque cada parte tem um trabalho estreito:

- `baseline`
  - apenas defaults amplos
- `ownership tree`
  - guidance comportamental owned por path
- `cross-cutting overlays`
  - uma lente extra atravessando vários owners
- `Follow-Through Triggers`
  - consequências downstream de revisão e atualização
- `skills`
  - workflows reutilizáveis que não devem ficar sempre carregados

Essa separação facilita controlar o crescimento:

- novos owners são adicionados por path
- novos overlays só aparecem quando uma concern realmente atravessa vários owners
- novos workflows viram skills apenas quando instructions always-on seriam a ferramenta errada

A gramática de pastas da ownership tree reforça essa escalabilidade:

- a árvore pode crescer sem mudar a forma como leitores a interpretam
- nós de arquivo e nós de diretório usam a mesma forma
- nós com várias instructions não exigem uma segunda representação
- mantenedores conseguem inspecionar a estrutura caminhando pelas pastas, em vez de decodificar casos especiais

## Por Que Isto É Mais Seguro do Que Customização Ad Hoc

A arquitetura não torna o Copilot determinístico.

Ela torna o mapa de instruções menos ambíguo.

Isso importa porque o GitHub nota explicitamente que o Copilot pode não seguir as custom instructions exatamente da mesma forma toda vez, e que conflitos devem ser evitados. A resposta mais segura não é adicionar mais política abstrata. A resposta mais segura é reduzir ambiguidade no grafo de instruções.

## Realidade de Suporte e Portabilidade

Diferentes surfaces do Copilot não suportam os mesmos mecanismos de customização da mesma forma.

A matriz oficial de suporte do GitHub mostra que instruções gerais do repositório, instruções path-specific, skills, instruções organizacionais e arquivos ligados a agents não têm suporte idêntico entre GitHub.com, VS Code, Visual Studio, JetBrains e CLI.

Isso importa para arquitetura.

Um modelo reutilizável deve se apoiar primeiro nos mecanismos de repositório mais amplamente documentados e tratar mecanismos mais especializados como extensões opcionais.

Essa é uma das razões pelas quais esta arquitetura concentra o peso principal em:

- instruções gerais do repositório
- instruções path-specific
- uso criterioso de skills

## Limites e Não-Objetivos

Esta arquitetura não:

- garante que o Copilot sempre obedecerá todas as instruções
- substitui code review, CI, testes ou controles de segurança
- prescreve o formato interno de escrita de cada instruction
- elimina a necessidade de julgamento ao mapear ownership ou overlays
- transforma skills em um motor determinístico de orquestração

Ela é uma estrutura para reduzir confusão e melhorar reuso, não um motor formal de execução.

## Alinhamento com Guidance Oficial

Este projeto é intencionalmente alinhado ao modelo oficial de customização do GitHub Copilot:

- instruções gerais do repositório em `.github/copilot-instructions.md`
- instruções path-specific em `.github/instructions/**/*.instructions.md`
- roteamento com `applyTo` nas instructions path-specific
- skills em `.github/skills/<skill-name>/SKILL.md`
- prevenção de conflitos quando múltiplas fontes de instruction se aplicam

Ele também segue guidance comum de documentação:

- manter páginas de visão geral curtas
- separar explicação de docs de modelo, regras, how-to e exemplos
- usar diagramas textuais fáceis de manter junto com código e docs

## Notas de Design da Documentação

Este conjunto de docs foi organizado para que cada documento tenha um trabalho principal:

- `README`
  - portal, trilhas de leitura e mapa da documentação
- `Por Que Esta Arquitetura`
  - caso de negócio, ganhos, limites e alinhamento com padrões
- `Modelo Operacional`
  - vocabulário estrutural
- `Ownership vs Overlay`
  - a principal distinção conceitual do modelo
- `Follow-Through Triggers`
  - comportamento downstream de revisão e atualização
- `Regras de Decisão`
  - classificação da guidance e posicionamento de follow-through
- `Gramática da Ownership Tree`
  - gramática canônica no disco e política de atalho
- `Conflitos e Precedência de Instruções`
  - ambiguidade, refinamento e não determinismo
- `Exemplos e Fluxos`
  - aprendizado por cenários
- `Playbook de Replicação`
  - rollout e manutenção

Essa divisão é influenciada pelo Diátaxis, que separa explicação, docs de modelo e de regras, how-to e necessidades mais próximas de tutorial.

## Referências

- GitHub Docs, About customizing GitHub Copilot responses  
  <https://docs.github.com/en/copilot/concepts/prompting/response-customization>
- GitHub Docs, Adding repository custom instructions for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- GitHub Docs, Support for different types of custom instructions  
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>
- GitHub Docs, Using custom instructions to unlock the power of Copilot code review  
  <https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/use-custom-instructions>
- GitHub Docs, Creating agent skills for GitHub Copilot  
  <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills>
- GitHub Docs, Comparing GitHub Copilot CLI customization features  
  <https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/agents/copilot-cli/comparing-cli-features>
- VS Code Docs, Use custom instructions in VS Code  
  <https://code.visualstudio.com/docs/copilot/customization/custom-instructions>
- GitHub Docs, Best practices for repositories  
  <https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories>
