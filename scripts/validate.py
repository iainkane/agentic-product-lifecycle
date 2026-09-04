#!/usr/bin/env python3
"""Perform dependency-free structural checks for the lifecycle repository."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TEMPLATES = {
    "intake.yaml",
    "intent.yaml",
    "requirements.yaml",
    "handoff.yaml",
    "project-overlay.yaml",
    "capability-assessment.yaml",
}


def main() -> int:
    errors: list[str] = []

    schema_paths = sorted((ROOT / "schemas").glob("*.json"))
    if not schema_paths:
        errors.append("no JSON schemas found")
    for path in schema_paths:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid schema {path.relative_to(ROOT)}: {exc}")

    present_templates = {path.name for path in (ROOT / "templates").glob("*.yaml")}
    for missing in sorted(REQUIRED_TEMPLATES - present_templates):
        errors.append(f"missing template templates/{missing}")

    skill_paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skill_paths:
        errors.append("no skills found")
    for path in skill_paths:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            errors.append(f"missing frontmatter: {path.relative_to(ROOT)}")
            continue
        frontmatter = match.group(1)
        for field in ("name:", "description:"):
            if field not in frontmatter:
                errors.append(f"missing {field[:-1]}: {path.relative_to(ROOT)}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Validation passed: {len(schema_paths)} schema(s), "
        f"{len(present_templates)} template(s), {len(skill_paths)} skill(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
