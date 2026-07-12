#!/usr/bin/env python3
"""Validate the public Deep Problem Framing package without third-party dependencies."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require_file(relative: str) -> Path:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing required file: {relative}")
    return path


def main() -> int:
    skill = require_file("SKILL.md").read_text(encoding="utf-8")
    require_file("AGENTS.md")
    readme = require_file("README.md").read_text(encoding="utf-8")
    require_file("LICENSE")
    cases = require_file("tests/cases.md").read_text(encoding="utf-8")
    interface = require_file("agents/openai.yaml").read_text(encoding="utf-8")

    frontmatter = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not frontmatter:
        fail("SKILL.md must start with YAML frontmatter")
    metadata = frontmatter.group(1)
    name = re.search(r"^name:\s*([^\n]+)$", metadata, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", metadata, re.MULTILINE)
    if not name or not description:
        fail("SKILL.md frontmatter must contain name and description")
    if name.group(1).strip() != "deep-problem-framing":
        fail("Skill name must be deep-problem-framing")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1).strip()):
        fail("Skill name must be lowercase hyphenated text")
    if not description.group(1).strip().startswith("Use when"):
        fail("Skill description must start with 'Use when'")

    for marker in ("/Users/", "/home/", "\\Users\\", ".env", "api_key", "private key"):
        for relative in ("SKILL.md", "AGENTS.md", "README.md", "agents/openai.yaml", "tests/cases.md"):
            content = (ROOT / relative).read_text(encoding="utf-8").lower()
            if marker.lower() in content:
                fail(f"public artifact contains forbidden marker {marker!r}: {relative}")

    for phrase in ("SKILL.md", "AGENTS.md", "tests/cases.md", "global", "License"):
        if phrase not in readme:
            fail(f"README.md does not explain {phrase}")
    for heading in (
        "## 1. Trivial task",
        "## 2. Ambiguous feature",
        "## 3. Direct-action pressure",
        "## 4. Multi-turn change",
        "## 5. Unsafe or protected action",
    ):
        if heading not in cases:
            fail(f"tests/cases.md is missing {heading}")
    interface_match = re.fullmatch(
        r'interface:\n'
        r'  display_name:\s*"([^"]+)"\n'
        r'  short_description:\s*"([^"]+)"\n'
        r'  default_prompt:\s*"([^"]+)"\n',
        interface,
    )
    if not interface_match or any(not value.strip() for value in interface_match.groups()):
        fail("agents/openai.yaml must contain three non-empty interface strings")

    required_skill_sections = (
        "## Activation",
        "## Trivial tasks",
        "## Non-trivial task frame",
        "## Risk and authorization",
        "## Communication",
        "## Multi-turn recalibration",
    )
    for section in required_skill_sections:
        if section not in skill:
            fail(f"SKILL.md is missing {section}")

    print("PASS: public Skill package is structurally valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
