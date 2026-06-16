# tests/test_md_local_index.py
import md_local_index as mli

SAMPLE = """---
tags: [seo, api]
---

# Titre principal

Voir [[autre-note]] et [[cluster-securite]].

## Sous-section

Texte avec #wordpress et #seo.
"""


def test_scan_markdown_file_extracts_structure(tmp_path):
    f = tmp_path / "note.md"
    f.write_text(SAMPLE, encoding="utf-8")
    doc = mli.scan_markdown_file(f)
    assert doc.title == "Titre principal"
    assert "Sous-section" in doc.headings
    assert "autre-note" in doc.wikilinks
    assert "cluster-securite" in doc.wikilinks
    assert "wordpress" in doc.tags
    assert doc.frontmatter.get("tags") == ["seo", "api"]


def test_scan_tree_respects_exclude(tmp_path):
    (tmp_path / "keep.md").write_text("# Keep", encoding="utf-8")
    drafts = tmp_path / "_drafts"
    drafts.mkdir()
    (drafts / "skip.md").write_text("# Skip", encoding="utf-8")
    docs = mli.scan_tree(tmp_path, exclude=["**/_drafts/**"])
    paths = [d.path for d in docs]
    assert any(p.endswith("keep.md") for p in paths)
    assert not any("skip.md" in p for p in paths)
