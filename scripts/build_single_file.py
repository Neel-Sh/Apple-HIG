#!/usr/bin/env python3
"""Build or check the optional single-file copy from the installable skill."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "apple-hig"
OUTPUT = ROOT / "apple-hig.md"
FILES = (
    "SKILL.md",
    "getting-started.md",
    "iphone-duo.md",
    "foundations.md",
    "patterns.md",
    "components-content-layout.md",
    "components-menus-navigation.md",
    "components-presentation-input.md",
    "components-status-system.md",
    "inputs.md",
    "technologies.md",
    "catalog.md",
)


def render() -> str:
    sections = [
        "# Apple Human Interface Guidelines skill\n\n"
        "Generated from `apple-hig/` by `scripts/build_single_file.py`. "
        "Install the directory for skill-aware agents; this file is for agents "
        "that need one document. Relative reference links resolve in `apple-hig/`.\n\n"
        "Official source: https://developer.apple.com/design/human-interface-guidelines\n"
    ]
    for name in FILES:
        path = SKILL / name
        body = path.read_text(encoding="utf-8").strip()
        sections.append(f"\n\n<!-- source: {name} -->\n\n{body}\n")
    return "".join(sections)


def check_local_links() -> list[str]:
    errors = []
    documents = [(SKILL / name, SKILL) for name in FILES]
    documents.append((ROOT / "README.md", ROOT))
    for path, base in documents:
        body = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", body):
            local = target.split("#", 1)[0]
            if local and not re.match(r"^[a-z][a-z0-9+.-]*:", local, re.I):
                if not (base / local).exists():
                    errors.append(f"{path.relative_to(ROOT)}: missing local link {target}")
    return errors


def check_manifest() -> list[str]:
    body = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", body, re.S)
    if not match:
        return ["SKILL.md: missing YAML frontmatter"]
    frontmatter = match.group(1)
    errors = []
    if not re.search(r"^name: apple-hig$", frontmatter, re.M):
        errors.append("SKILL.md: expected name: apple-hig")
    if not re.search(r"^description: (?:>|\S)", frontmatter, re.M):
        errors.append("SKILL.md: missing description")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify generated output and links")
    args = parser.parse_args()

    errors = check_manifest() + check_local_links()
    if errors:
        print("\n".join(errors))
        return 1

    expected = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != expected:
            print("apple-hig.md is out of date; run scripts/build_single_file.py")
            return 1
        print(f"OK: manifest, {len(FILES)} source files, local links, and apple-hig.md")
    else:
        OUTPUT.write_text(expected, encoding="utf-8")
        print(f"Wrote {OUTPUT.name} from {len(FILES)} source files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
