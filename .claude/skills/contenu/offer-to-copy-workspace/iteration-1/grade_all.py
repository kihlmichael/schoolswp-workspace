"""Grade all 6 runs against 8 assertions programmatically."""

import json
import re
import os

ITER_DIR = os.path.dirname(os.path.abspath(__file__))

EVALS = [
    ("eval-1-google-ads-skill", "with_skill"),
    ("eval-1-google-ads-skill", "without_skill"),
    ("eval-2-plugin-landing-page", "with_skill"),
    ("eval-2-plugin-landing-page", "without_skill"),
    ("eval-3-formation-fluentcrm", "with_skill"),
    ("eval-3-formation-fluentcrm", "without_skill"),
]

HYPE_WORDS = [
    r"r[ée]volutionnaire",
    r"game.?changer",
    r"magie de l.IA",
    r"powered by AI",
    r"disrupts?",
    r"cutting.?edge",
]


def read_output(eval_name, config):
    path = os.path.join(ITER_DIR, eval_name, config, "outputs", "positionnement.md")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def check_a1_structure(text):
    """7 sections numbered 1-7 present."""
    sections_found = 0
    patterns = [
        r"##\s*1\.",
        r"##\s*2\.",
        r"##\s*3\.",
        r"##\s*4\.",
        r"##\s*5\.",
        r"##\s*6\.",
        r"##\s*7\.",
    ]
    for p in patterns:
        if re.search(p, text):
            sections_found += 1
    return sections_found >= 7, f"{sections_found}/7 sections found"


def check_a2_promesse_une_phrase(text):
    """Promise section has one sentence (no intermediate period followed by capital)."""
    match = re.search(r"##\s*1\.[^\n]*\n+(.*?)(?=\n##|\n---|\Z)", text, re.DOTALL)
    if not match:
        return False, "Section 1 not found"
    content = match.group(1).strip()
    # Remove markdown bold markers
    content = re.sub(r"\*\*", "", content)
    # Remove blank lines, keep only text
    lines = [
        l.strip()
        for l in content.split("\n")
        if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("---")
    ]
    text_block = " ".join(lines)
    # Count sentences (period followed by space and capital or end)
    sentences = re.split(r"\.\s+(?=[A-ZÀ-Ü])", text_block)
    return len(sentences) <= 2, f"{len(sentences)} sentence(s) detected"


def check_a3_tableau(text):
    """Markdown table with 2+ columns present (pipe-separated)."""
    table_rows = re.findall(r"^\|.+\|.+\|", text, re.MULTILINE)
    # At least header + separator + 1 data row
    has_table = len(table_rows) >= 3
    # Check it's a feature/benefit style table (2 content columns)
    return has_table, f"{len(table_rows)} table rows found"


def check_a4_three_messages(text):
    """3 distinct message versions: LinkedIn, landing page, pitch."""
    has_linkedin = bool(re.search(r"(?i)(post\s+)?linkedin|### A\.", text))
    has_landing = bool(re.search(r"(?i)landing\s+page|### B\.", text))
    has_pitch = bool(re.search(r"(?i)pitch\s+produit|### C\.", text))
    count = sum([has_linkedin, has_landing, has_pitch])
    return count == 3, f"LinkedIn={has_linkedin}, Landing={has_landing}, Pitch={has_pitch}"


def check_a5_tutoiement(text):
    """Uses tu/ton/ta/tes consistently, no vous or 'l'utilisateur'."""
    has_tu = bool(re.search(r"\btu\b|\bton\b|\bta\b|\btes\b", text, re.IGNORECASE))
    has_vous = bool(re.search(r"\bvous\b|\bvotre\b|\bvos\b", text, re.IGNORECASE))
    has_utilisateur = bool(re.search(r"l.utilisateur", text, re.IGNORECASE))
    passed = has_tu and not has_vous and not has_utilisateur
    evidence = f"tu={has_tu}, vous={has_vous}, l'utilisateur={has_utilisateur}"
    return passed, evidence


def check_a6_zero_hype(text):
    """No hype AI terms."""
    found = []
    for hw in HYPE_WORDS:
        if re.search(hw, text, re.IGNORECASE):
            found.append(hw)
    return len(found) == 0, f"hype words found: {found}" if found else "no hype words"


def check_a7_benefice_avant_technique(text):
    """In section 4 (solution), first substantive sentence is benefit-oriented."""
    match = re.search(r"##\s*4\.[^\n]*\n+(.*?)(?=\n##|\Z)", text, re.DOTALL)
    if not match:
        # Try alternate structure
        match = re.search(r"(?i)(?:la\s+)?solution[^\n]*\n+(.*?)(?=\n##|\n---|\Z)", text, re.DOTALL)
    if not match:
        return False, "Section 4 / solution not found"
    content = match.group(1).strip()
    lines = [
        l.strip()
        for l in content.split("\n")
        if l.strip()
        and not l.strip().startswith("#")
        and not l.strip().startswith("---")
        and not l.strip().startswith("|")
    ]
    if not lines:
        return False, "No content in solution section"
    first_line = lines[0]
    # Technical indicators: mentions specific tech stack, protocols, code
    tech_indicators = [r"\bMCP\b", r"\bAPI\b", r"\bHTML\b", r"\bCSV\b", r"\bJSON\b", r"\bscrape\b", r"\bwebsocket\b"]
    # Benefit indicators: tu, résultat, gagn, temps, simple, rapide, sans
    benefit_indicators = [
        r"\btu\b",
        r"\br[ée]sultat",
        r"\bgagn",
        r"\btemps\b",
        r"\bsimple\b",
        r"\brapide",
        r"\bsans\b",
        r"\bplus besoin\b",
        r"\bfini\b",
    ]
    tech_count = sum(1 for t in tech_indicators if re.search(t, first_line, re.IGNORECASE))
    benefit_count = sum(1 for b in benefit_indicators if re.search(b, first_line, re.IGNORECASE))
    passed = benefit_count >= tech_count
    return passed, f"first line: '{first_line[:80]}...' tech={tech_count} benefit={benefit_count}"


def check_a8_linkedin_structure(text):
    """LinkedIn post has identifiable accroche + problème + solution + CTA."""
    # Find LinkedIn section
    match = re.search(
        r"(?i)(?:###?\s*A\.?\s*)?(?:Post\s+)?LinkedIn[^\n]*\n+(.*?)(?=\n###|\n---|\n##[^#]|\Z)", text, re.DOTALL
    )
    if not match:
        return False, "LinkedIn section not found"
    linkedin = match.group(1).strip()
    if len(linkedin) < 50:
        return False, "LinkedIn section too short"
    # Check for question or hook at start (accroche)
    lines = [l for l in linkedin.split("\n") if l.strip()]
    has_accroche = len(lines) >= 1 and (lines[0].strip().endswith("?") or len(lines[0].strip()) < 100)
    # Check for CTA indicators
    cta_patterns = [r"commentaire", r"\bDM\b", r"message", r"lien", r"d[ée]couvr", r"partag", r"dis.le", r"dis.moi"]
    has_cta = any(re.search(p, linkedin, re.IGNORECASE) for p in cta_patterns)
    # Minimum length check as proxy for problem+solution
    has_body = len(linkedin) > 200
    passed = has_accroche and has_cta and has_body
    return passed, f"accroche={has_accroche}, cta={has_cta}, body_length={len(linkedin)}"


ASSERTIONS = [
    ("A1", "structure-7-sections", check_a1_structure),
    ("A2", "promesse-une-phrase", check_a2_promesse_une_phrase),
    ("A3", "tableau-fonctionnalites-benefices", check_a3_tableau),
    ("A4", "3-messages-distincts", check_a4_three_messages),
    ("A5", "tutoiement-consistant", check_a5_tutoiement),
    ("A6", "zero-hype-ia", check_a6_zero_hype),
    ("A7", "benefices-avant-technique", check_a7_benefice_avant_technique),
    ("A8", "linkedin-structure", check_a8_linkedin_structure),
]


def grade_run(eval_name, config):
    text = read_output(eval_name, config)
    results = []
    for aid, aname, check_fn in ASSERTIONS:
        passed, evidence = check_fn(text)
        results.append(
            {
                "text": f"[{aid}] {aname}",
                "passed": passed,
                "evidence": evidence,
            }
        )
    return results


def main():
    all_grades = {}
    for eval_name, config in EVALS:
        run_id = f"{eval_name}/{config}"
        print(f"\n=== Grading {run_id} ===")
        results = grade_run(eval_name, config)
        passed_count = sum(1 for r in results if r["passed"])
        print(f"  Score: {passed_count}/{len(results)}")
        for r in results:
            status = "PASS" if r["passed"] else "FAIL"
            print(f"  [{status}] {r['text']} — {r['evidence']}")

        # Save grading.json
        grading_path = os.path.join(ITER_DIR, eval_name, config, "grading.json")
        grading_data = {
            "eval_name": eval_name,
            "config": config,
            "pass_rate": passed_count / len(results),
            "expectations": results,
        }
        with open(grading_path, "w", encoding="utf-8") as f:
            json.dump(grading_data, f, indent=2, ensure_ascii=False)
        all_grades[run_id] = grading_data

    # Print summary
    print("\n\n=== SUMMARY ===")
    print(f"{'Run':<50} {'Pass Rate':>10}")
    print("-" * 62)
    for run_id, data in all_grades.items():
        print(f"{run_id:<50} {data['pass_rate']:.0%}")


if __name__ == "__main__":
    main()
