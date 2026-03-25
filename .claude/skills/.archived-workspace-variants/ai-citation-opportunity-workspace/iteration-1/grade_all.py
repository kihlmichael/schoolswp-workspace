"""Grade all eval outputs for ai-citation-opportunity skill iteration 1."""
import json
import re
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

EVALS = [
    {
        "name": "eval-lms-default",
        "expected_count": 10,
        "expect_proof": True,
        "language": "fr",
        "min_intentions": 5,
        "min_formats": 3,
    },
    {
        "name": "eval-coach-custom",
        "expected_count": 15,
        "expect_proof": True,
        "language": "fr",
        "min_intentions": 5,
        "min_formats": 3,
    },
    {
        "name": "eval-woo-minimal-en",
        "expected_count": 5,
        "expect_proof": False,
        "language": "en",
        "min_intentions": 3,
        "min_formats": 2,
    },
]

VALID_INTENTIONS = {"diagnostic", "comparaison", "how-to", "checklist", "decision"}
VALID_FORMATS = {
    "guide pas-a-pas", "comparatif + tableau", "checklist",
    "template", "stack recommandee", "FAQ structuree",
}


def grade_output(filepath, eval_cfg, is_with_skill):
    """Grade a single output file against assertions."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    results = []

    # A1: Query count
    query_pattern = r"\*\*Requ[eê]te\*\*\s*:|^\d+\.\s+\*\*(?:Query|Requ[eê]te)"
    queries = re.findall(query_pattern, content, re.MULTILINE | re.IGNORECASE)
    if not queries:
        # Fallback: count numbered items that look like queries
        queries = re.findall(r"^\d+\.\s+\*\*", content, re.MULTILINE)
    expected = eval_cfg["expected_count"]
    results.append({
        "text": f"Contains exactly {expected} numbered queries",
        "passed": len(queries) == expected,
        "evidence": f"Found {len(queries)} queries (expected {expected})",
    })

    # A2: Intention coverage
    found_intentions = set()
    for intent in VALID_INTENTIONS:
        if re.search(rf"\*\*Intention\*\*\s*:\s*{intent}", content, re.IGNORECASE):
            found_intentions.add(intent)
    min_req = eval_cfg["min_intentions"]
    results.append({
        "text": f"At least {min_req} intention types represented",
        "passed": len(found_intentions) >= min_req,
        "evidence": f"Found {len(found_intentions)} intentions: {sorted(found_intentions)}",
    })

    # A3: Format variety
    found_formats = set()
    for fmt in VALID_FORMATS:
        if fmt.lower() in content.lower():
            found_formats.add(fmt)
    min_fmt = eval_cfg["min_formats"]
    results.append({
        "text": f"At least {min_fmt} different content formats used",
        "passed": len(found_formats) >= min_fmt,
        "evidence": f"Found {len(found_formats)} formats: {sorted(found_formats)}",
    })

    # A4: 2 constraints per query (heuristic: query lines > 20 words)
    query_lines = re.findall(
        r"\*\*Requ[eê]te\*\*\s*:\s*(.+?)(?:\n|$)", content, re.IGNORECASE
    )
    if not query_lines:
        query_lines = re.findall(r"\*\*Query\*\*\s*:\s*(.+?)(?:\n|$)", content, re.IGNORECASE)
    long_enough = sum(1 for q in query_lines if len(q.split()) >= 12)
    total_q = max(len(query_lines), 1)
    results.append({
        "text": "Each query contains at least 2 explicit constraints (heuristic: >12 words)",
        "passed": long_enough >= total_q * 0.8,
        "evidence": f"{long_enough}/{total_q} queries have 12+ words",
    })

    # A5: Denominators count
    denom_matches = re.findall(r"^\d+\.\s+.+\n\s+-\s+Sous-cat", content, re.MULTILINE)
    results.append({
        "text": "Exactly 5 common denominators listed",
        "passed": len(denom_matches) == 5,
        "evidence": f"Found {len(denom_matches)} denominators with sous-categories",
    })

    # A6: Proof angles (conditional)
    if eval_cfg["expect_proof"]:
        proof_section = "## Angles de preuve" in content or "## Proof" in content
        proof_items = re.findall(r"\*\*(?:Test reel|Critere mesurable|Mini etude de cas)\*\*", content)
        results.append({
            "text": "3 proof angles present in dedicated section",
            "passed": proof_section and len(proof_items) >= 3,
            "evidence": f"Section present: {proof_section}, items found: {len(proof_items)}",
        })
    else:
        has_proof = "## Angles de preuve" in content or "## Proof" in content
        results.append({
            "text": "No proof angles section present (user disabled it)",
            "passed": not has_proof,
            "evidence": f"Proof section found: {has_proof}",
        })

    # A7: Main sections structure
    has_denom = "## Denominateurs communs" in content or "## Common denominators" in content
    has_queries = "## Requ" in content or "## AI Search" in content
    if eval_cfg["expect_proof"]:
        has_proof_section = "## Angles" in content or "## Proof" in content
        results.append({
            "text": "3 main sections present (Denominateurs, Requetes, Angles)",
            "passed": has_denom and has_queries and has_proof_section,
            "evidence": f"Denom: {has_denom}, Queries: {has_queries}, Proof: {has_proof_section}",
        })
    else:
        results.append({
            "text": "2 main sections: Denominateurs and Requetes only",
            "passed": has_denom and has_queries,
            "evidence": f"Denom: {has_denom}, Queries: {has_queries}",
        })

    # A8: Natural language (>10 words per query)
    natural = sum(1 for q in query_lines if len(q.split()) >= 10)
    results.append({
        "text": "All queries are natural language (>10 words each)",
        "passed": natural >= total_q * 0.9,
        "evidence": f"{natural}/{total_q} queries have 10+ words",
    })

    return {
        "expectations": results,
        "summary": f"{sum(1 for r in results if r['passed'])}/{len(results)} assertions passed",
    }


def main():
    for eval_cfg in EVALS:
        for variant in ["with_skill", "without_skill"]:
            result_path = os.path.join(
                WORKSPACE, eval_cfg["name"], variant, "outputs", "result.md"
            )
            if not os.path.exists(result_path):
                print(f"SKIP {eval_cfg['name']}/{variant} - file not found")
                continue

            grading = grade_output(result_path, eval_cfg, variant == "with_skill")
            grading_path = os.path.join(
                WORKSPACE, eval_cfg["name"], variant, "grading.json"
            )
            with open(grading_path, "w", encoding="utf-8") as f:
                json.dump(grading, f, indent=2, ensure_ascii=False)
            print(f"{eval_cfg['name']}/{variant}: {grading['summary']}")


if __name__ == "__main__":
    main()
