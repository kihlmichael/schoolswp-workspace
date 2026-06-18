# tests/test_secrets_scan.py
import secrets_scan


def test_detects_private_key_and_api_keys(tmp_path):
    clean = tmp_path / "clean.md"
    clean.write_text("# Article propre, aucun secret.\n", encoding="utf-8")
    leak = tmp_path / "leak.md"
    leak.write_text(
        "intro\nGEMINI_API_KEY=AIzaSyABCDEF1234567890abcdefABCDEF12345\n-----BEGIN PRIVATE KEY-----\n",
        encoding="utf-8",
    )
    hits = secrets_scan.scan_files([clean, leak])
    leaked_paths = {h.path for h in hits}
    assert str(leak) in leaked_paths
    assert str(clean) not in leaked_paths
    assert len(hits) >= 2  # api key + PEM header


def test_clean_set_returns_no_hits(tmp_path):
    f = tmp_path / "ok.md"
    f.write_text("Juste un article sur WordPress.\n", encoding="utf-8")
    assert secrets_scan.scan_files([f]) == []
