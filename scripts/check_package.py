#!/usr/bin/env python3
"""Check a research skill release. No dependencies beyond Python's stdlib."""

from pathlib import Path
import json
import re
import sys


EXPECTED = {
    "research-guide",
    "research-field-map",
    "research-foundations",
    "research-question",
    "research-test-design",
    "research-paper-library",
    "research-review",
    "research-papers",
}
REQUIRED = ("README.md", "LICENSE", ".gitignore", "evals/scenarios.md",
            "evals/validation.md")
PRIVATE_DIRECTORIES = {"research", "outputs", "backups", "work", "private", "project-data"}
PRIVATE_PATTERNS = {
    "absolute Windows path": re.compile(r"\b[A-Za-z]:[\\/]"),
    "absolute personal Unix path": re.compile(r"/(?:Users|home)/[^\s/]+/"),
    "email address": re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"),
    "UUID-like identifier": re.compile(
        r"\b[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\b", re.I),
    "common credential prefix": re.compile(
        r"\b(?:ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,})\b"),
}


def check(root):
    errors = []
    if not root.is_dir():
        return [f"Directory does not exist: {root}"], 0
    for name in sorted(PRIVATE_DIRECTORIES):
        if (root / name).exists():
            errors.append(f"Private working directory must not enter the release: {name}")
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing release file: {name}")
    skill_root = root / "skills"
    actual = {p.name for p in skill_root.iterdir() if p.is_dir()} if skill_root.exists() else set()
    if actual != EXPECTED:
        errors.append(f"Skill folders differ: {sorted(actual ^ EXPECTED)}")
    for name in sorted(EXPECTED):
        folder = skill_root / name
        entry = folder / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        content = entry.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not frontmatter:
            errors.append(f"{name}: missing YAML frontmatter")
        else:
            # Restrict this release to simple scalar name/description fields.
            fields = dict(re.findall(r"^([a-z-]+):[ \t]*(.+)$",
                                     frontmatter.group(1), re.M))
            if fields.get("name", "").strip("\"'") != name:
                errors.append(f"{name}: frontmatter name mismatch")
            if not fields.get("description", "").strip("\"' "):
                errors.append(f"{name}: empty description")
        ui = folder / "agents" / "openai.yaml"
        if not ui.is_file():
            errors.append(f"{name}: missing UI metadata")
        elif ("$" + name) not in ui.read_text(encoding="utf-8"):
            errors.append(f"{name}: default prompt does not invoke the skill")

    files = [p for p in root.rglob("*") if p.is_file()
             and ".git" not in p.relative_to(root).parts
             and "__pycache__" not in p.relative_to(root).parts]
    for path in files:
        rel = path.relative_to(root).as_posix()
        if path.suffix not in {".md", ".yaml", ".py", ".json"} and path.name not in {
                "LICENSE", ".gitignore"}:
            errors.append(f"{rel}: unexpected distribution file type")
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            errors.append(f"{rel}: unreadable or non-text release file")
            continue
        for label, pattern in PRIVATE_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"{rel}: review possible {label}")
        if path.suffix == ".json":
            try:
                record = json.loads(content)
                if path.name == "workflow-state.example.json":
                    expected_stages = ["subfield", "questions", "library", "review"]
                    if [s.get("id") for s in record.get("stages", [])] != expected_stages:
                        errors.append(f"{rel}: missing or reordered workflow stages")
                    if any(s.get("acceptance") is not None or s.get("status") != "not_started"
                           for s in record.get("stages", [])):
                        errors.append(f"{rel}: template must not contain accepted work")
                    preferences = record.get("reasoning_preferences", {})
                    if any(preferences.get(key) is not None for key in (
                            "creation_authorization", "followup_authorization",
                            "work_codex_substitution_authorization")):
                        errors.append(f"{rel}: template must not contain user authorization")
                    if record.get("handoffs"):
                        errors.append(f"{rel}: template must not contain live consultations")
            except (ValueError, TypeError, AttributeError):
                errors.append(f"{rel}: invalid JSON or workflow template")
        if re.search(r"\[TODO:|\bFIXME\b", content):
            # The checker necessarily contains its own marker patterns.
            if path.name != "check_package.py":
                errors.append(f"{rel}: unfinished scaffold")
        if path.suffix == ".md":
            for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content):
                target = target.strip("<>").split("#", 1)[0]
                if not target or re.match(r"https?://", target):
                    continue
                if re.match(r"[A-Za-z]+:", target):
                    errors.append(f"{rel}: unsupported link scheme")
                    continue
                destination = (path.parent / target).resolve()
                if not destination.is_relative_to(root):
                    errors.append(f"{rel}: link escapes package: {target}")
                elif not destination.exists():
                    errors.append(f"{rel}: broken local link: {target}")
    return errors, len(files)


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors, count = check(root)
    if errors:
        print("\n".join(f"FAIL: {error}" for error in errors))
        return 1
    print(f"PASS: {len(EXPECTED)} skills, {count} text files; structure, "
          "local links, and configured privacy patterns checked.")
    print("Manual content review and behavioral evaluation are still needed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
