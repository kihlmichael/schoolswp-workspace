"""Grade all 6 runs against 10 assertions for iteration 2."""

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

FORBIDDEN_PATTERNS = [
    r"en \d+ secondes",
    r"en moins de \d+ secondes",
    r"en moins de \d+ minutes?",
    r"sans aucune compétence",
    r"aucun prérequis",
    r"compatible avec tou[st]e?s? les",
    r"c.est terminé",
    r"c.est fini",
    r"tu n.auras plus jamais",
    r"révolutionnaire",
    r"game.?changer",
    r"disruptif",
    r"powered by AI",
    r"magie de l.IA",
    r"100\s*%\s*automati",
    r"entièrement automatisé",
    r"copy de qualité à chaque fois",
]

TECH_JARGON = [r"\bMCP\b", r"\bAPI\b", r"\bSDK\b", r"\bWebSocket\b"]


def read_output(eval_name, config):
    path = os.path.join(ITER_DIR, eval_name, config, "outputs", "positionnement.md")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def get_messages_section(text):
    """Extract the messages finaux section (section 9 or last major section)."""
    match = re.search(r"(?i)##\s*(?:9|7|8)\.?\s*Messages?\s+finau?x?.*?\n(.*)", text, re.DOTALL)
    if match:
        return match.group(1)
    # Fallback: everything after "Post LinkedIn"
    match = re.search(r"(?i)Post\s+LinkedIn.*?\n(.*)", text, re.DOTALL)
    return match.group(1) if match else text[-3000:]


def check_a1_structure_9(text):
    """9 sections present."""
    sections_found = 0
    for i in range(1, 10):
        if re.search(rf"##\s*{i}\.", text):
            sections_found += 1
    return sections_found >= 9, f"{sections_found}/9 sections found"


def check_a2_promesse_transformation(text):
    """Promise is about business transformation, not just time savings."""
    match = re.search(r"##\s*1\.[^\n]*\n+(.*?)(?=\n##|\n---|\Z)", text, re.DOTALL)
    if not match:
        return False, "Section 1 not found"
    content = match.group(1).strip()
    content = re.sub(r"\*\*", "", content)
    # Business transformation indicators
    biz_words = [
        r"business",
        r"client",
        r"factur",
        r"revenue",
        r"prestation",
        r"valoris",
        r"standardis",
        r"assurance",
        r"crédibi",
        r"professionnel",
        r"proposes?",
        r"soutien",
        r"relation",
        r"converti",
        r"monétis",
    ]
    # Pure time/speed indicators
    time_words = [r"en \d+", r"secondes?", r"minutes?", r"rapide", r"vite", r"gagn.*temps"]
    biz_count = sum(1 for w in biz_words if re.search(w, content, re.IGNORECASE))
    time_count = sum(1 for w in time_words if re.search(w, content, re.IGNORECASE))
    passed = biz_count >= 1
    return passed, f"business_indicators={biz_count}, time_indicators={time_count}"


def check_a3_tableau_3col(text):
    """Table with 3+ columns present."""
    table_rows = re.findall(r"^\|.+\|.+\|.+\|", text, re.MULTILINE)
    has_table = len(table_rows) >= 3
    return has_table, f"{len(table_rows)} rows with 3+ columns"


def check_a4_three_messages(text):
    has_linkedin = bool(re.search(r"(?i)(post\s+)?linkedin|### A\.", text))
    has_landing = bool(re.search(r"(?i)landing\s+page|### B\.", text))
    has_pitch = bool(re.search(r"(?i)pitch\s+produit|### C\.", text))
    count = sum([has_linkedin, has_landing, has_pitch])
    return count == 3, f"LinkedIn={has_linkedin}, Landing={has_landing}, Pitch={has_pitch}"


def check_a5_tutoiement(text):
    has_tu = bool(re.search(r"\btu\b|\bton\b|\bta\b|\btes\b", text, re.IGNORECASE))
    has_vous = bool(re.search(r"\bvous\b|\bvotre\b|\bvos\b", text, re.IGNORECASE))
    has_utilisateur = bool(re.search(r"l.utilisateur", text, re.IGNORECASE))
    passed = has_tu and not has_vous and not has_utilisateur
    return passed, f"tu={has_tu}, vous={has_vous}, l'utilisateur={has_utilisateur}"


def check_a6_zero_forbidden(text):
    found = []
    for fp in FORBIDDEN_PATTERNS:
        matches = re.findall(fp, text, re.IGNORECASE)
        if matches:
            found.extend(matches[:2])
    return len(found) == 0, f"forbidden found: {found}" if found else "no forbidden patterns"


def check_a7_credibilite(text):
    """Section crédibilité/limites present with substantive content."""
    has_section = bool(re.search(r"(?i)(crédibi|limite|##\s*8\.)", text))
    has_limit = bool(re.search(r"(?i)(ne remplace pas|limite|prérequis|ce que ça ne fait pas|reste à faire)", text))
    passed = has_section and has_limit
    return passed, f"section={has_section}, limits_mentioned={has_limit}"


def check_a8_cible(text):
    """Precise target section present (not just 'agences et consultants')."""
    has_section = bool(re.search(r"(?i)(##\s*2\.\s*Cible|cible précise|persona|profil)", text))
    # Check for specificity indicators
    specifics = [
        r"\d+\s*(à|et)\s*\d+",
        r"freelance",
        r"solo",
        r"agence.*\d",
        r"blogueur",
        r"consultant.*acqui",
        r"moment de douleur",
        r"profil\s+(principal|type)",
    ]
    spec_count = sum(1 for s in specifics if re.search(s, text, re.IGNORECASE))
    passed = has_section and spec_count >= 2
    return passed, f"section={has_section}, specificity_markers={spec_count}"


def check_a9_linkedin(text):
    match = re.search(
        r"(?i)(?:###?\s*A\.?\s*)?(?:Post\s+)?LinkedIn[^\n]*\n+(.*?)(?=\n###|\n---|\n##[^#]|\Z)", text, re.DOTALL
    )
    if not match:
        return False, "LinkedIn section not found"
    linkedin = match.group(1).strip()
    if len(linkedin) < 50:
        return False, "LinkedIn section too short"
    lines = [l for l in linkedin.split("\n") if l.strip()]
    has_accroche = len(lines) >= 1 and (lines[0].strip().endswith("?") or len(lines[0].strip()) < 100)
    cta_patterns = [
        r"commentaire",
        r"\bDM\b",
        r"message",
        r"lien",
        r"découvr",
        r"partag",
        r"dis.le",
        r"dis.moi",
        r"commente",
        r"réponds",
    ]
    has_cta = any(re.search(p, linkedin, re.IGNORECASE) for p in cta_patterns)
    has_body = len(linkedin) > 200
    passed = has_accroche and has_cta and has_body
    return passed, f"accroche={has_accroche}, cta={has_cta}, body_length={len(linkedin)}"


def check_a10_no_jargon_messages(text):
    """No MCP/API/SDK in the messages section."""
    messages = get_messages_section(text)
    found = []
    for tj in TECH_JARGON:
        if re.search(tj, messages):
            found.append(tj)
    return len(found) == 0, f"jargon in messages: {found}" if found else "no tech jargon in messages"


ASSERTIONS = [
    ("A1", "structure-9-sections", check_a1_structure_9),
    ("A2", "promesse-transformation-business", check_a2_promesse_transformation),
    ("A3", "tableau-3-colonnes", check_a3_tableau_3col),
    ("A4", "3-messages-distincts", check_a4_three_messages),
    ("A5", "tutoiement-consistant", check_a5_tutoiement),
    ("A6", "zero-formulations-interdites", check_a6_zero_forbidden),
    ("A7", "section-credibilite-limites", check_a7_credibilite),
    ("A8", "cible-precise", check_a8_cible),
    ("A9", "linkedin-structure", check_a9_linkedin),
    ("A10", "zero-jargon-technique-messages", check_a10_no_jargon_messages),
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

    print("\n\n=== SUMMARY ===")
    print(f"{'Run':<50} {'Pass Rate':>10}")
    print("-" * 62)
    for run_id, data in all_grades.items():
        print(f"{run_id:<50} {data['pass_rate']:.0%}")


if __name__ == "__main__":
    main()
