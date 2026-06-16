# tests/test_config.py
from pathlib import Path

import config


def _write_allowlist(tmp_path: Path) -> Path:
    f = tmp_path / "allowlist.yml"
    f.write_text(
        "roots:\n"
        "  - { path: core/, type: code, backend: offline }\n"
        "  - { path: docs/, type: content, backend: gemini }\n"
        "exclude:\n"
        '  - "**/.env*"\n'
        'gemini_model: "gemini-2.5-flash"\n',
        encoding="utf-8",
    )
    return f


def test_load_config_parses_roots_and_env(tmp_path):
    allow = _write_allowlist(tmp_path)
    env = {
        "SCHOOLSWP_REPO_PATH": str(tmp_path),
        "OBSIDIAN_BRIDGE_PATH": str(tmp_path / "obsidian-bridge"),
        "GRAPHIFY_OUTPUT_PATH": str(tmp_path / "schoolswp-brain" / ".graphify"),
    }
    cfg = config.load_config(allow, env)
    assert cfg.repo_path == tmp_path
    assert cfg.output_path == tmp_path / "schoolswp-brain" / ".graphify"
    assert [r.path for r in cfg.roots] == ["core/", "docs/"]
    assert cfg.roots[0].backend == "offline"
    assert cfg.gemini_model == "gemini-2.5-flash"
    assert "**/.env*" in cfg.exclude


def test_load_config_defaults_output_under_repo(tmp_path):
    allow = _write_allowlist(tmp_path)
    env = {"SCHOOLSWP_REPO_PATH": str(tmp_path)}  # no output/obsidian set
    cfg = config.load_config(allow, env)
    assert cfg.output_path == tmp_path / "schoolswp-brain" / ".graphify"
    assert cfg.obsidian_bridge_path == tmp_path / "obsidian-bridge"


def test_compile_graphifyignore_whitelists_roots_and_excludes(tmp_path):
    allow = _write_allowlist(tmp_path)
    cfg = config.load_config(allow, {"SCHOOLSWP_REPO_PATH": str(tmp_path)})
    full = config.compile_graphifyignore(cfg, mode="full")
    lines = full.splitlines()
    assert "*" in lines  # ignore-all anchor present (whitelist style)
    assert "!core/" in lines and "!core/**" in lines
    assert "!docs/" in lines and "!docs/**" in lines
    assert "**/.env*" in lines  # exclude re-applied after the whitelist


def test_compile_graphifyignore_code_only_excludes_markdown(tmp_path):
    allow = _write_allowlist(tmp_path)
    cfg = config.load_config(allow, {"SCHOOLSWP_REPO_PATH": str(tmp_path)})
    code = config.compile_graphifyignore(cfg, mode="code-only")
    assert "*.md" in code
    assert "*.pdf" in code


def test_compile_graphifyignore_code_only_excludes_non_code_assets(tmp_path):
    # graphify routes images/data/office/media to LLM semantic extraction; offline
    # mode must re-ignore them all so a code-only corpus needs no API key.
    allow = _write_allowlist(tmp_path)
    cfg = config.load_config(allow, {"SCHOOLSWP_REPO_PATH": str(tmp_path)})
    code = config.compile_graphifyignore(cfg, mode="code-only").splitlines()
    for glob in ("*.png", "*.jpg", "*.svg", "*.json", "*.csv", "*.html", "*.xlsx", "*.docx", "*.mp4", "*.yaml"):
        assert glob in code, f"{glob} must be re-ignored in code-only mode"
    # the full (gemini) mode keeps them so semantic extraction can run
    full = config.compile_graphifyignore(cfg, mode="full").splitlines()
    assert "*.png" not in full
    assert "*.json" not in full
