import pathlib
import re
import sys

BASE = pathlib.Path(__file__).resolve().parents[2] / ".claude" / "skills"

CANONICAL = [
    ["objectif", "dev definition"],
    ["architecture", "formule"],
    ["sorties obligatoires"],
    ["donnees d entree", "entrees", "variables"],
    ["prompt principal"],
    ["workflow recommande", "implementation pattern"],
    ["failure modes / optimization", "failure mode / optimization", "failure modes"],
    ["exemple entree / sortie"],
    ["regles", "regles de redaction", "regles de contexte"],
    ["checklist (5 points)"],
    ["actions suivantes", "plan d execution"],
]

REQUIRED = {"exemple entree / sortie", "checklist (5 points)"}


def normalize(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def extract_headers(text):
    return [normalize(m.group(1)) for m in re.finditer(r"(?m)^##\s+(.+)$", text)]


def canonical_index(header):
    for idx, variants in enumerate(CANONICAL):
        if header in variants:
            return idx
    return None


def validate_file(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    headers = extract_headers(text)

    issues = []

    missing = [h for h in REQUIRED if h not in headers]
    if missing:
        issues.append(f"missing sections: {', '.join(sorted(missing))}")

    # order check (only for known sections)
    indices = []
    for h in headers:
        idx = canonical_index(h)
        if idx is not None:
            indices.append(idx)
    if indices != sorted(indices):
        issues.append("sections out of canonical order")

    return issues


def main():
    if not BASE.exists():
        print(f"[skills-validator] directory not found: {BASE}")
        return 1

    skills = [p for p in BASE.iterdir() if p.is_dir() and (p / "SKILL.md").exists()]
    errors = 0

    for skill in sorted(skills):
        path = skill / "SKILL.md"
        issues = validate_file(path)
        if issues:
            errors += 1
            print(f"[FAIL] {path}")
            for issue in issues:
                print(f"  - {issue}")

    if errors:
        print(f"[skills-validator] {errors} file(s) failed")
        return 1

    print("[skills-validator] OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
