#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.pt-BR.md",
    "LICENSE",
    "scripts/check_repo.py",
    ".github/copilot-instructions.md",
    ".github/workflows/docs-hygiene.yml",
    ".github/instructions/ownership/.github/general.instructions.md",
    ".github/instructions/ownership/docs/general.instructions.md",
    ".github/instructions/ownership/starter-kit/general.instructions.md",
    ".github/instructions/ownership/templates/general.instructions.md",
    ".github/instructions/ownership/scripts/general.instructions.md",
    ".github/instructions/ownership/README.md.instructions.md",
    ".github/instructions/ownership/README.pt-BR.md.instructions.md",
    ".github/instructions/overlays/quality/markdown-quality.instructions.md",
    ".github/instructions/overlays/quality/bilingual-parity.instructions.md",
    ".github/instructions/overlays/quality/repo-hygiene.instructions.md",
    ".github/instructions/overlays/workflow/community-health.instructions.md",
    "docs/en/README.md",
    "docs/pt-BR/README.md",
    "starter-kit/README.md",
    "starter-kit/.github/copilot-instructions.md",
    "templates/README.md",
]

REQUIRED_DIRS = [
    ".github/instructions/ownership",
    ".github/instructions/overlays",
    "docs/en",
    "docs/en/model",
    "docs/en/rules",
    "docs/en/examples",
    "docs/en/examples/classification",
    "docs/en/examples/follow-through",
    "docs/en/examples/ownership-tree",
    "docs/en/examples/repositories",
    "docs/pt-BR",
    "docs/pt-BR/exemplos",
    "docs/pt-BR/exemplos/classification",
    "docs/pt-BR/exemplos/follow-through",
    "docs/pt-BR/exemplos/ownership-tree",
    "docs/pt-BR/exemplos/repositorios",
    "docs/pt-BR/modelo",
    "docs/pt-BR/regras",
    "starter-kit/.github/instructions/ownership",
    "starter-kit/.github/instructions/overlays",
    "templates",
]

MARKDOWN_LINK_RE = re.compile(r"(?<!\!)\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def ensure_required_paths() -> None:
    for rel_path in REQUIRED_DIRS:
        path = ROOT / rel_path
        if not path.is_dir():
            fail(f"Required directory missing: {rel_path}")

    for rel_path in REQUIRED_FILES:
        path = ROOT / rel_path
        if not path.is_file():
            fail(f"Required file missing: {rel_path}")


def ensure_instruction_tree_layout() -> None:
    for rel_root in [".github/instructions", "starter-kit/.github/instructions"]:
        root = ROOT / rel_root
        flat_files = list(root.glob("*.instructions.md"))
        if flat_files:
            fail(
                f"Flat instruction files found under {rel_root}: "
                + ", ".join(path.name for path in flat_files)
            )


def ensure_instruction_sets_have_content() -> None:
    required_instruction_sets = [
        ".github/instructions/ownership",
        ".github/instructions/overlays",
        "starter-kit/.github/instructions/ownership",
        "starter-kit/.github/instructions/overlays",
    ]

    for rel_root in required_instruction_sets:
        root = ROOT / rel_root
        matches = list(root.rglob("*.instructions.md"))
        if not matches:
            fail(f"No instruction files found under: {rel_root}")


def ensure_optional_skill_layout() -> None:
    skill_roots = [
        "starter-kit/.github/skills",
        ".github/skills",
    ]

    for rel_root in skill_roots:
        root = ROOT / rel_root
        if not root.exists():
            continue

        skill_dirs = [path for path in root.iterdir() if path.is_dir()]
        for skill_dir in skill_dirs:
            if not (skill_dir / "SKILL.md").is_file():
                fail(
                    f"Skill directory missing SKILL.md: "
                    f"{skill_dir.relative_to(ROOT)}"
                )


def ensure_templates_have_content() -> None:
    template_files = list((ROOT / "templates").glob("*.template"))
    if not template_files:
        fail("No template files found under: templates")


def resolve_link(source: Path, target: str) -> Path | None:
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if target.startswith("<") and target.endswith(">"):
        return None

    clean_target = target.split("#", 1)[0].strip()
    if not clean_target:
        return None

    resolved = (source.parent / clean_target).resolve()
    if resolved.exists():
        return resolved

    if resolved.is_dir():
        return resolved

    readme_resolved = resolved / "README.md"
    if readme_resolved.exists():
        return readme_resolved

    return resolved


def ensure_markdown_links() -> None:
    markdown_files = list(ROOT.rglob("*.md"))
    for md_file in markdown_files:
        text = md_file.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            resolved = resolve_link(md_file, target)
            if resolved is None:
                continue
            if not resolved.exists():
                fail(
                    f"Broken markdown link in {md_file.relative_to(ROOT)} -> {target}"
                )


def ensure_language_doc_sets() -> None:
    english = {
        "docs/en/README.md",
        "docs/en/why-this-architecture.md",
        "docs/en/replication-playbook.md",
        "docs/en/model/operating-model.md",
        "docs/en/model/ownership-vs-overlay.md",
        "docs/en/model/follow-through-triggers.md",
        "docs/en/rules/decision-rules.md",
        "docs/en/rules/ownership-tree-grammar.md",
        "docs/en/rules/instruction-conflicts-and-precedence.md",
        "docs/en/examples/README.md",
        "docs/en/examples/classification/01-one-path-one-owner.md",
        "docs/en/examples/classification/02-a-real-overlay.md",
        "docs/en/examples/classification/03-narrower-owner-vs-overlay.md",
        "docs/en/examples/follow-through/01-contract-change.md",
        "docs/en/examples/follow-through/02-configuration-change.md",
        "docs/en/examples/follow-through/03-documentation-as-its-own-owner.md",
        "docs/en/examples/follow-through/04-board-or-task-follow-through.md",
        "docs/en/examples/follow-through/05-no-follow-through-needed.md",
        "docs/en/examples/ownership-tree/01-one-file-node-with-two-instruction-files.md",
        "docs/en/examples/ownership-tree/02-mixed-children-under-one-parent.md",
        "docs/en/examples/ownership-tree/03-why-a-folder-grammar-is-easier-to-teach.md",
        "docs/en/examples/repositories/README.md",
        "docs/en/examples/repositories/01-api-service.md",
        "docs/en/examples/repositories/02-web-product-app.md",
        "docs/en/examples/repositories/03-product-monorepo.md",
    }
    portuguese = {
        "docs/pt-BR/README.md",
        "docs/pt-BR/por-que-esta-arquitetura.md",
        "docs/pt-BR/playbook-de-replicacao.md",
        "docs/pt-BR/modelo/modelo-operacional.md",
        "docs/pt-BR/modelo/ownership-vs-overlay.md",
        "docs/pt-BR/modelo/follow-through-triggers.md",
        "docs/pt-BR/regras/regras-de-decisao.md",
        "docs/pt-BR/regras/gramatica-da-ownership-tree.md",
        "docs/pt-BR/regras/conflitos-e-precedencia-de-instrucoes.md",
        "docs/pt-BR/exemplos/README.md",
        "docs/pt-BR/exemplos/classification/01-um-caminho-um-owner.md",
        "docs/pt-BR/exemplos/classification/02-um-overlay-de-verdade.md",
        "docs/pt-BR/exemplos/classification/03-owner-mais-estreito-vs-overlay.md",
        "docs/pt-BR/exemplos/follow-through/01-mudanca-de-contrato.md",
        "docs/pt-BR/exemplos/follow-through/02-mudanca-de-configuracao.md",
        "docs/pt-BR/exemplos/follow-through/03-documentacao-como-seu-proprio-owner.md",
        "docs/pt-BR/exemplos/follow-through/04-follow-through-de-board-ou-task.md",
        "docs/pt-BR/exemplos/follow-through/05-nenhum-follow-through-necessario.md",
        "docs/pt-BR/exemplos/ownership-tree/01-um-no-de-arquivo-com-dois-arquivos-de-instruction.md",
        "docs/pt-BR/exemplos/ownership-tree/02-filhos-mistos-sob-um-mesmo-pai.md",
        "docs/pt-BR/exemplos/ownership-tree/03-por-que-uma-gramatica-de-pastas-e-mais-facil-de-ensinar.md",
        "docs/pt-BR/exemplos/repositorios/README.md",
        "docs/pt-BR/exemplos/repositorios/01-servico-de-api.md",
        "docs/pt-BR/exemplos/repositorios/02-aplicacao-web-de-produto.md",
        "docs/pt-BR/exemplos/repositorios/03-monorepo-de-produto.md",
    }

    missing_en = {
        rel_path for rel_path in english if not (ROOT / rel_path).is_file()
    }
    missing_pt = {
        rel_path for rel_path in portuguese if not (ROOT / rel_path).is_file()
    }

    if missing_en:
        fail("Missing English docs: " + ", ".join(sorted(missing_en)))
    if missing_pt:
        fail("Missing Portuguese docs: " + ", ".join(sorted(missing_pt)))


def main() -> int:
    ensure_required_paths()
    ensure_instruction_tree_layout()
    ensure_instruction_sets_have_content()
    ensure_optional_skill_layout()
    ensure_templates_have_content()
    ensure_language_doc_sets()
    ensure_markdown_links()
    print("ownership-driven-ai-customization hygiene: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
