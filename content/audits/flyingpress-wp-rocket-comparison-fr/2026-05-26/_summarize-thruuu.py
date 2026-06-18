"""Summarize thruuu raw JSON into focused markdown blocks per language."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
raw = json.loads((OUT / "_thruuu-raw.json").read_text(encoding="utf-8"))


def docx_overview(d: dict, label: str) -> str:
    lines = [f"=== {label} ==="]
    lines.append(f"  paragraphs: {d['n_paragraphs']}, tables: {d['n_tables']}")
    # All paragraphs
    for p in d["paragraphs"]:
        lines.append(f"  [{p['style']}] {p['text']}")
    # Tables (full)
    for ti, t in enumerate(d["tables"]):
        lines.append(f"\n  TABLE #{ti} ({len(t)} rows x {len(t[0]) if t else 0} cols):")
        for ri, row in enumerate(t):
            cells = " | ".join(c.replace("\n", " ").strip() for c in row)
            lines.append(f"    row {ri}: {cells}")
    return "\n".join(lines)


def xlsx_keysheets(x: dict, label: str, sheets_to_dump: list[str]) -> str:
    lines = [f"=== {label} ==="]
    for sname in sheets_to_dump:
        sdata = x.get(sname)
        if not sdata:
            continue
        lines.append(f"\n  SHEET '{sname}' ({sdata['n_rows']} rows):")
        for ri, row in enumerate(sdata["rows"]):
            lines.append(f"    r{ri}: {' | '.join(c[:200] for c in row[:10])}")
    return "\n".join(lines)


buf = []
buf.append(docx_overview(raw["docx"]["audit_fr"], "DOCX AUDIT FR"))
buf.append("\n\n" + "#" * 70 + "\n\n")
buf.append(docx_overview(raw["docx"]["audit_de"], "DOCX AUDIT DE"))
buf.append("\n\n" + "#" * 70 + "\n\n")

# Critical sheets to dump from each xlsx
SHEETS_PRIORITY = [
    "Info",
    "SERP Overview",
    "Search Volume",
    "Monthly Search Volume",
    "SERP Organic Title",
    "Heading 1 (Organic page only)",
    "Heading 2 (Organic page only)",
    "Frequent Questions",
    "FAQ",
    "Topic",
    "Related Search",
]

buf.append(xlsx_keysheets(raw["xlsx"]["serp_main"], "XLSX SERP_MAIN", SHEETS_PRIORITY))
buf.append("\n\n" + "#" * 70 + "\n\n")
buf.append(xlsx_keysheets(raw["xlsx"]["serp_dup"], "XLSX SERP_DUP", SHEETS_PRIORITY))

out_md = OUT / "_thruuu-summary.txt"
out_md.write_text("\n".join(buf), encoding="utf-8")
print(f"WROTE {out_md} ({out_md.stat().st_size} bytes, {len(buf)} blocks)")
