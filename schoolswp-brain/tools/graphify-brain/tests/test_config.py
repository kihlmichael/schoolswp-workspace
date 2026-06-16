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
