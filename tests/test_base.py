"""Tests for agents.base — path traversal protection and agent init."""

import asyncio

import pytest

from agents.base import BaseContentAgent, safe_read_path, safe_write_path


class TestSafeReadPath:
    """safe_read_path must block traversal and reject missing files."""

    def test_valid_path_within_cwd(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        f = tmp_path / "ok.md"
        f.write_text("content")
        result = safe_read_path("ok.md")
        assert result == f.resolve()

    def test_valid_nested_path(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        nested = tmp_path / "sub" / "dir"
        nested.mkdir(parents=True)
        f = nested / "article.md"
        f.write_text("content")
        result = safe_read_path("sub/dir/article.md")
        assert result == f.resolve()

    def test_rejects_path_traversal(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with pytest.raises(ValueError, match="hors du répertoire"):
            safe_read_path("../../etc/passwd")

    def test_rejects_absolute_path_outside_cwd(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        # Use a path that's guaranteed to exist but outside tmp_path
        with pytest.raises(ValueError, match="hors du répertoire"):
            safe_read_path(str(tmp_path.parent / "other.md"))

    def test_raises_on_missing_file(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with pytest.raises(FileNotFoundError, match="introuvable"):
            safe_read_path("nonexistent.md")


class TestSafeWritePath:
    """safe_write_path blocks traversal but doesn't require file to exist."""

    def test_valid_write_path(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        result = safe_write_path("output/report.md")
        assert result.is_relative_to(tmp_path)

    def test_rejects_traversal(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        with pytest.raises(ValueError, match="hors du répertoire"):
            safe_write_path("../../../tmp/evil.md")

    def test_does_not_require_file_existence(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        result = safe_write_path("new-file.md")
        assert not result.exists()
        assert result.is_relative_to(tmp_path)


class TestBaseContentAgent:
    """BaseContentAgent: model resolution and run() contract."""

    def test_default_model(self, fake_env):
        agent = BaseContentAgent()
        assert agent.model == "claude-sonnet-4-6"

    def test_explicit_model_overrides_env(self, fake_env):
        agent = BaseContentAgent(model="claude-opus-4")
        assert agent.model == "claude-opus-4"

    def test_env_model_used_when_no_explicit(self, monkeypatch):
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
        monkeypatch.setenv("MODEL_WRITER", "claude-haiku-4-5")
        agent = BaseContentAgent()
        assert agent.model == "claude-haiku-4-5"

    def test_run_raises_not_implemented(self, fake_env):
        agent = BaseContentAgent()
        with pytest.raises(NotImplementedError, match="base"):
            asyncio.run(agent.run())

    def test_has_provider(self, fake_env):
        agent = BaseContentAgent()
        assert agent._provider is not None
