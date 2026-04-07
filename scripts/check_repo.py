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
    "docs/pt-BR",
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
        "README.md",
        "core-model.md",
        "why-this-architecture.md",
        "instruction-conflicts-and-precedence.md",
        "examples-and-flows.md",
        "replication-playbook.md",
    }
    portuguese = {
        "README.md",
        "modelo-central.md",
        "por-que-esta-arquitetura.md",
        "conflitos-e-precedencia-de-instrucoes.md",
        "exemplos-e-fluxos.md",
        "playbook-de-replicacao.md",
    }

    english_files = {path.name for path in (ROOT / "docs/en").glob("*.md")}
    portuguese_files = {path.name for path in (ROOT / "docs/pt-BR").glob("*.md")}

    missing_en = english - english_files
    missing_pt = portuguese - portuguese_files

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
