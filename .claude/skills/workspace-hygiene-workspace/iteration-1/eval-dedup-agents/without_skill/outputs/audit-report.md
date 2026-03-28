# Deduplication Report: .agent/ vs .agents/

## Findings

`.agent/` and `.agents/` are **100% identical**: same 93 SKILL.md files across 93 subdirectories (gws-*, persona-*, recipe-*), zero diff.

**`.agents/` is the canonical directory** -- it is referenced in:
- `d:/VS Code/CLAUDE CODE/CLAUDE.md` as "Source library -- 42 skills EN d'origine"
- `d:/VS Code/CLAUDE CODE/projects/schoolswp/CLAUDE.md` in the Skills Registry table

**`.agent/` is referenced nowhere** in the project documentation, scripts, or config files. It appears to be an accidental copy (typo missing the "s").

**Recommendation**: Keep `.agents/`, remove `.agent/` via `trash .agent/`. No functional impact.
