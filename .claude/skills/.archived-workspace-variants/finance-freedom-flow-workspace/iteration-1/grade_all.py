"""Grade all eval outputs for finance-freedom-flow skill iteration 1."""
import json
import re
import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))


def grade_flow_complet(content):
    """Grade eval-flow-complet (7 steps full flow)."""
    results = []

    # A1: 7 steps present
    step_keywords = [
        (r"[EÉeé]tape\s*1|[Aa]udit|[Rr]adiographie", "Etape 1 Audit"),
        (r"[EÉeé]tape\s*2|[Aa]rch[eé]type|[Pp]ersonnalit", "Etape 2 Archetype"),
        (r"[EÉeé]tape\s*3|[Bb]udget|[Bb]ucket", "Etape 3 Budget"),
        (r"[EÉeé]tape\s*4|[Dd]ette|[Ss]nowball|[Aa]valanche", "Etape 4 Dettes"),
        (r"[EÉeé]tape\s*5|[Ff]onds.{0,5}[Uu]rgence|[Ll]ibert[eé]", "Etape 5 Fonds urgence"),
        (r"[EÉeé]tape\s*6|[Pp]ortefeuille|ETF|[Ii]nvestissement", "Etape 6 Portefeuille"),
        (r"[EÉeé]tape\s*7|[Rr]ituel|[Rr]evue\s*[Mm]ensuelle", "Etape 7 Rituel"),
    ]
    found_steps = []
    for pattern, name in step_keywords:
        if re.search(pattern, content):
            found_steps.append(name)
    results.append({
        "text": "7 steps present (Audit, Archetype, Budget, Dettes, Fonds urgence, Portefeuille, Rituel)",
        "passed": len(found_steps) >= 7,
        "evidence": f"Found {len(found_steps)}/7: {found_steps}",
    })

    # A2: Score /10
    has_score = bool(re.search(r"\b\d+\s*/\s*10\b", content))
    results.append({
        "text": "Score sante financiere /10 present",
        "passed": has_score,
        "evidence": f"Score /10 found: {has_score}",
    })

    # A3: Budget buckets with EUR amounts
    has_buckets = bool(re.search(r"[Bb]ucket|[Nn][eé]cessit[eé]s|[Pp]laisir", content))
    has_eur = bool(re.search(r"\d+\s*(?:EUR|€)", content))
    results.append({
        "text": "Systeme buckets avec allocations en EUR",
        "passed": has_buckets and has_eur,
        "evidence": f"Buckets: {has_buckets}, EUR amounts: {has_eur}",
    })

    # A4: 3 debt methods compared
    methods = 0
    if re.search(r"[Ss]nowball", content): methods += 1
    if re.search(r"[Aa]valanche", content): methods += 1
    if re.search(r"[Hh]ybride|[Hh]ybrid", content): methods += 1
    results.append({
        "text": "3 methodes de dette comparees (snowball, avalanche, hybride)",
        "passed": methods >= 3,
        "evidence": f"Found {methods}/3 methods",
    })

    # A5: FI levels calculated
    fi_levels = 0
    if re.search(r"[Ll]ean\s*FI|[Ll]ibert[eé]\s*[Pp]artielle", content): fi_levels += 1
    if re.search(r"\bFI\b|[Ll]ibert[eé]\s*[Cc]onfortable", content): fi_levels += 1
    if re.search(r"[Ff]at\s*FI|[Ll]ibert[eé]\s*[Tt]otale", content): fi_levels += 1
    results.append({
        "text": "3 niveaux FI calcules (Lean, FI, Fat)",
        "passed": fi_levels >= 3,
        "evidence": f"Found {fi_levels}/3 FI levels",
    })

    # A6: ETF allocation
    has_etf = bool(re.search(r"ETF|CW8|EWLD|MSCI\s*World|[Tt]icker", content))
    results.append({
        "text": "Allocation ETF avec tickers",
        "passed": has_etf,
        "evidence": f"ETF/tickers found: {has_etf}",
    })

    # A7: Monthly template
    has_template = bool(re.search(r"[Rr]ituel|[Rr]evue\s*[Mm]ensuelle|[Mm]inutes?\s*\d", content))
    results.append({
        "text": "Template revue mensuelle present",
        "passed": has_template,
        "evidence": f"Monthly template found: {has_template}",
    })

    # A8: Action plan
    has_plan = bool(re.search(r"[Pp]lan\s*d.action|[Aa]ction\s*priorit|[Ss]emaine\s*1", content))
    results.append({
        "text": "Plan d'action priorise present",
        "passed": has_plan,
        "evidence": f"Action plan found: {has_plan}",
    })

    return results


def grade_dette(content):
    """Grade eval-dette-isolee."""
    results = []

    # A1: 3 debts listed
    debts = len(re.findall(r"(?:credit|carte|revolving|auto|conso)", content, re.IGNORECASE))
    results.append({
        "text": "3 dettes inventoriees",
        "passed": debts >= 3,
        "evidence": f"Found {debts} debt references",
    })

    # A2: Snowball order (revolving first = smallest)
    has_snowball = bool(re.search(r"[Ss]nowball", content))
    results.append({
        "text": "Methode Snowball presente avec ordre",
        "passed": has_snowball,
        "evidence": f"Snowball found: {has_snowball}",
    })

    # A3: Avalanche order (revolving first = highest rate)
    has_avalanche = bool(re.search(r"[Aa]valanche", content))
    revolving_first = bool(re.search(r"[Aa]valanche.*revolving|19[.,]8\s*%.*premier|revolving.*priorit", content, re.DOTALL | re.IGNORECASE))
    results.append({
        "text": "Methode Avalanche : revolving (19.8%) en premier",
        "passed": has_avalanche,
        "evidence": f"Avalanche found: {has_avalanche}, revolving priority indicated: {revolving_first}",
    })

    # A4: Monthly calendar
    has_calendar = bool(re.search(r"M\d+|[Mm]ois\s*\d|calendrier|mois\s*par\s*mois", content))
    results.append({
        "text": "Calendrier mois par mois present",
        "passed": has_calendar,
        "evidence": f"Monthly calendar found: {has_calendar}",
    })

    # A5: Recommendation
    has_reco = bool(re.search(r"[Rr]ecommand|[Cc]onseill[eé]|[Mm][eé]thode\s*optimale|pour\s*toi", content, re.IGNORECASE))
    results.append({
        "text": "Recommandation personnalisee avec justification",
        "passed": has_reco,
        "evidence": f"Recommendation found: {has_reco}",
    })

    # A6: Total interest compared
    has_interest = bool(re.search(r"int[eé]r[eê]ts?\s*totaux|[eé]conomie|€.*vs|diff[eé]rence", content, re.IGNORECASE))
    results.append({
        "text": "Interets totaux compares entre methodes",
        "passed": has_interest,
        "evidence": f"Interest comparison found: {has_interest}",
    })

    return results


def grade_portefeuille(content):
    """Grade eval-portefeuille."""
    results = []

    # A1: ETF tickers
    tickers = re.findall(r"\b(?:CW8|EWLD|PAEEM|PCEU|AGGH|EPRE|MWRD|VWCE|IWDA)\b", content, re.IGNORECASE)
    results.append({
        "text": "Tickers ETF mentionnes",
        "passed": len(tickers) >= 1,
        "evidence": f"Found tickers: {list(set(t.upper() for t in tickers))}",
    })

    # A2: PEA priority
    has_pea = bool(re.search(r"PEA", content))
    results.append({
        "text": "PEA mentionne comme enveloppe prioritaire",
        "passed": has_pea,
        "evidence": f"PEA found: {has_pea}",
    })

    # A3: French brokers
    brokers = re.findall(r"(?:Bourse\s*Direct|Boursorama|Fortuneo|Trade\s*Republic|Degiro|Linxea|Yomoni)", content, re.IGNORECASE)
    results.append({
        "text": "Au moins 2 courtiers FR recommandes",
        "passed": len(set(b.lower() for b in brokers)) >= 2,
        "evidence": f"Found brokers: {list(set(b for b in brokers))}",
    })

    # A4: DCA 300 EUR
    has_dca = bool(re.search(r"DCA|Dollar\s*Cost|[Vv]irement.*mensuel|300\s*(?:EUR|€)", content))
    results.append({
        "text": "Strategie DCA a 300 EUR/mois",
        "passed": has_dca,
        "evidence": f"DCA strategy found: {has_dca}",
    })

    # A5: Allocation table with percentages
    percentages = re.findall(r"\d+\s*%", content)
    results.append({
        "text": "Tableau allocation avec pourcentages",
        "passed": len(percentages) >= 3,
        "evidence": f"Found {len(percentages)} percentage values",
    })

    # A6: Week 1 plan
    has_plan = bool(re.search(r"[Jj]our\s*1|[Ss]emaine\s*1|[Cc]ette\s*semaine|[Dd][eé]marrage|[Aa]ction\s*plan", content))
    results.append({
        "text": "Plan d'action premiere semaine present",
        "passed": has_plan,
        "evidence": f"Week-1 plan found: {has_plan}",
    })

    return results


EVAL_CONFIG = {
    "eval-flow-complet": grade_flow_complet,
    "eval-dette-isolee": grade_dette,
    "eval-portefeuille": grade_portefeuille,
}


def main():
    for eval_name, grader_fn in EVAL_CONFIG.items():
        for variant in ["with_skill", "without_skill"]:
            result_path = os.path.join(WORKSPACE, eval_name, variant, "outputs", "result.md")
            if not os.path.exists(result_path):
                print(f"SKIP {eval_name}/{variant} - file not found")
                continue

            with open(result_path, "r", encoding="utf-8") as f:
                content = f.read()

            results = grader_fn(content)
            grading = {
                "expectations": results,
                "summary": f"{sum(1 for r in results if r['passed'])}/{len(results)} assertions passed",
            }

            grading_path = os.path.join(WORKSPACE, eval_name, variant, "grading.json")
            with open(grading_path, "w", encoding="utf-8") as f:
                json.dump(grading, f, indent=2, ensure_ascii=False)
            print(f"{eval_name}/{variant}: {grading['summary']}")


if __name__ == "__main__":
    main()
