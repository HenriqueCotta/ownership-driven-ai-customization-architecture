# Why This Architecture

Audience: maintainers, platform teams, and engineering leaders evaluating whether this pattern is worth adopting.  
Goal: explain the business case, technical rationale, expected gains, limits, and standards alignment behind the model.

## Executive Summary

`Ownership-Driven AI Customization Architecture` exists to solve a practical problem:

- repository custom instructions often start small,
- then collapse into one large baseline file or a pile of overlapping rules,
- and eventually become hard to trust, hard to change, and hard to reuse across repositories.

This architecture answers that problem with a small set of stable structural decisions:

- keep repository-wide guidance short,
- route most behavior through stable ownership paths,
- add overlays only for concerns that truly span multiple owners,
- keep downstream review/update behavior explicit through `Follow-Through Triggers`,
- use skills only for deeper workflows that should not stay always-on.

## Why The Model Makes Sense

This model follows the grain of how GitHub Copilot customization works today.

GitHub's documentation recommends short, self-contained custom instructions and documents that repository-wide instructions and matching path-specific instructions are used together. GitHub also notes that conflicting instructions should be avoided because Copilot's choice between conflicting guidance is non-deterministic.

That combination leads to a practical design conclusion:

- keep the baseline short,
- use path-based ownership as the main routing mechanism,
- keep overlays narrow and purposeful,
- reduce duplication before it reaches the model.

Skills fit the same logic. GitHub recommends custom instructions for simple guidance that is relevant to almost every task, and skills for more detailed guidance that Copilot should access only when relevant.

## Why The Baseline Stays Intentionally Short

This architecture is intentionally skeptical of oversized repository-wide instruction files.

That is not just a stylistic preference.

It follows directly from the platform:

- GitHub recommends short, self-contained instruction statements.
- GitHub recommends path-specific instructions so repository-wide instructions do not become overloaded with guidance that only applies to certain files.
- GitHub documents that Copilot code review reads only a limited portion of each custom instruction file.

Those constraints make a long baseline structurally weak:

- it becomes harder to maintain,
- it increases conflict risk,
- and part of it may not even be visible in important surfaces such as code review.

## Why The Model Is Path-First

This architecture treats stable paths as the main routing backbone.

That choice is practical rather than ideological.

GitHub and VS Code both support path-specific instructions under `.github/instructions/**/*.instructions.md`, and VS Code documents that instruction files can be organized recursively in subdirectories.

That gives teams a concrete and scalable unit for organization:

- broad owners,
- narrower owners,
- overlays only where a concern truly crosses those ownership boundaries.

Path-first routing is easier to reason about than theme-first routing because it stays tied to the repository's actual structure.

## Why The Ownership Tree Uses One Folder Grammar

The architecture does not stop at "use paths."

It also recommends one canonical disk layout for ownership nodes:

- every owned boundary becomes a folder node
- repository directories stay directories
- repository files also become folder nodes
- instruction files inside the node are named by concern

That choice matters because mixed naming systems usually create friction:

- some nodes look like files and some look like folders
- file-level owners need to be renamed later when they gain a second instruction
- new maintainers have to learn exceptions before they can read the tree confidently

One folder grammar avoids those problems.

It is more teachable because the explanation becomes:

1. find the repository path,
2. walk the same path inside `ownership/`,
3. read the instruction files in the matching node folders.

It is more scalable because:

- one file can have one or many instruction files without changing its identity,
- mixed children are natural,
- concern-based filenames remain meaningful when paths evolve,
- teams can extend the tree without redesigning the naming convention.

## Why Skills Stay Optional And Selective

The architecture includes skills, but deliberately avoids making them the main routing mechanism.

This is also grounded in official guidance:

- GitHub recommends skills for more detailed instructions that should only be accessed when relevant.
- GitHub's CLI documentation explicitly says that if behavior is only needed in one workflow, a skill is the better fit.
- The same documentation warns against overloading Copilot's context window with instructions that are not relevant to the current task.

That is why skills appear here as workflow extensions rather than as the foundation of the model.

## Expected Gains

### Lower Prompt Friction

Teams stop re-explaining the same repository context in every prompt.

### Better Routing Discipline

Relevant context is tied to stable paths and stable concerns instead of being spread across one oversized file.

### Less Duplication And Conflict

Ownership-tree nodes carry local behavioral guidance. Overlays add cross-cutting lenses. That separation reduces the chance that the same rule is repeated in multiple places with slightly different wording.

### Better Scalability Across Repositories

The model is reusable because it depends on a small number of structural ideas, not on one repository's domain language.

### Stronger Downstream Hygiene

`Follow-Through Triggers` make secondary work visible:

- docs that may now be stale,
- tests that may need updates,
- configs that may need review,
- workflow artifacts that may need adjustment.

### Better Cost Discipline

The architecture intentionally keeps always-on context small and pushes deeper workflows into optional skills.

## Why This Is Scalable

The model scales because each part has a narrow job:

- `baseline`
  - broad defaults only
- `ownership tree`
  - path-owned behavioral guidance
- `cross-cutting overlays`
  - one extra lens across several owners
- `Follow-Through Triggers`
  - downstream review/update consequences
- `skills`
  - reusable workflows that should not always be loaded

That separation makes growth easier to control:

- new owners are added by path,
- new overlays are added only when a concern truly spans multiple owners,
- new workflows become skills only when always-on instructions would be the wrong tool.

The ownership-tree folder grammar reinforces that scalability:

- the tree can grow without changing how readers interpret it,
- file-level nodes and directory-level nodes use the same shape,
- multi-instruction nodes do not require a second representation,
- maintainers can inspect the structure by walking folders instead of decoding special cases.

## Why This Is Safer Than Ad Hoc Customization

The architecture does not make Copilot deterministic.

It does make the instruction map less ambiguous.

That matters because GitHub explicitly notes that Copilot may not follow custom instructions in exactly the same way every time, and that conflicting instructions should be avoided. The safest response is not to add more abstract policy. The safest response is to reduce ambiguity in the instruction graph.

## Support And Portability Reality

Different Copilot surfaces do not support the same customization features in the same way.

GitHub's support matrix shows that repository-wide instructions, path-specific instructions, skills, organization instructions, and agent-related files do not all have identical support across GitHub.com, VS Code, Visual Studio, JetBrains, and CLI surfaces.

That matters for architecture.

A reusable model should anchor itself in the most broadly documented repository-level mechanisms and treat more specialized mechanisms as optional extensions.

That is one reason this architecture puts the main weight on:

- repository-wide instructions,
- path-specific instructions,
- and careful use of skills.

## Limits And Non-Goals

This architecture does not:

- guarantee that Copilot will always obey every instruction,
- replace code review, CI, testing, or security controls,
- prescribe the internal prose format of each instruction,
- eliminate the need for judgment when mapping ownership or overlays,
- turn skills into a deterministic orchestration engine.

It is a structure for reducing confusion and improving reuse, not a formal execution engine.

## Alignment With Official Guidance

This project is intentionally aligned with the official GitHub Copilot customization model:

- repository-wide custom instructions in `.github/copilot-instructions.md`
- path-specific instructions in `.github/instructions/**/*.instructions.md`
- `applyTo`-based routing for path-specific instructions
- skills in `.github/skills/<skill-name>/SKILL.md`
- conflict avoidance when multiple instruction sources apply

It also follows common documentation guidance:

- keep overview pages short,
- split explanation from examples and replication guidance,
- use text-based diagrams that are easy to maintain alongside code and docs.

## Documentation Design Notes

This documentation set is organized to support both fast onboarding and deeper evaluation:

- `README`
  - quick overview and reading paths
- `Why This Architecture`
  - business case, gains, and limits
- `Core Model`
  - conceptual structure and routing logic
- `Instruction Conflicts And Precedence`
  - ambiguity, refinement, and non-determinism
- `Examples`
  - scenario-based learning
- `Replication Playbook`
  - rollout and maintenance guidance

This split is influenced by Diataxis, which distinguishes explanation, reference, how-to guidance, and tutorial-style needs.

## References

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
