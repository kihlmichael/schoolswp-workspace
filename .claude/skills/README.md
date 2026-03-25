# Canonical SKILL Structure (schoolsWP)

This document defines the standard section order for all project-only skills.
Keep sections short, explicit, and action-oriented.

## Canonical order (H2)
1) Objectif / Dev definition
2) Architecture / Formule (if applicable)
3) Sorties obligatoires
4) Donnees d entree / Entrees / Variables
5) Prompt principal
6) Workflow recommande / Implementation pattern
7) Failure modes / optimization (if applicable)
8) Exemple entree / sortie
9) Regles / Regles de redaction
10) Checklist (5 points)
11) Actions suivantes / Plan d execution

## Notes
- Prefer ASCII text.
- Keep examples minimal and deterministic.
- If a section is not relevant, omit it.
- Validator: `tools/scripts/validate_skills.py` (runs in pre-commit when SKILL.md changes).
