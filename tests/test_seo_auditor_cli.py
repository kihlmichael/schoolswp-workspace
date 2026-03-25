"""Tests for seo_auditor CLI argument parsing."""

import pytest

from agents.seo_auditor.cli import build_parser


class TestSeoAuditorParser:
    """Validate argparse config without running the agent."""

    def test_file_mode_minimal(self):
        parser = build_parser()
        args = parser.parse_args(["--file", "article.md", "--keyword", "lms wordpress"])
        assert args.file == "article.md"
        assert args.keyword == "lms wordpress"
        assert args.fix is False
        assert args.threshold == 90
        assert args.intent is None

    def test_text_mode(self):
        parser = build_parser()
        args = parser.parse_args(["--text", "# Mon article", "--keyword", "test keyword"])
        assert args.text == "# Mon article"
        assert args.file is None

    def test_file_and_text_mutually_exclusive(self):
        parser = build_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(["--file", "a.md", "--text", "content", "--keyword", "kw"])

    def test_keyword_required(self):
        parser = build_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(["--file", "a.md"])

    def test_source_required(self):
        parser = build_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(["--keyword", "kw"])

    def test_fix_mode_with_threshold(self):
        parser = build_parser()
        args = parser.parse_args(["--file", "a.md", "--keyword", "kw", "--fix", "--threshold", "85"])
        assert args.fix is True
        assert args.threshold == 85

    def test_valid_intent(self):
        parser = build_parser()
        args = parser.parse_args(["--text", "content", "--keyword", "kw", "--intent", "comparative"])
        assert args.intent == "comparative"

    def test_invalid_intent_rejected(self):
        parser = build_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(["--text", "content", "--keyword", "kw", "--intent", "invalid"])

    def test_save_dir(self):
        parser = build_parser()
        args = parser.parse_args(["--file", "a.md", "--keyword", "kw", "--save-dir", "output/"])
        assert args.save_dir == "output/"

    def test_model_override(self):
        parser = build_parser()
        args = parser.parse_args(["--file", "a.md", "--keyword", "kw", "--model", "claude-opus-4"])
        assert args.model == "claude-opus-4"
