"""Thin subprocess wrappers around the graphify CLI, with explicit egress control."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Mapping

LLM_KEYS = (
    "GEMINI_API_KEY",
    "GOOGLE_API_KEY",
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "DEEPSEEK_API_KEY",
    "KIMI_API_KEY",
    "MOONSHOT_API_KEY",
    "OLLAMA_HOST",
    "OPENAI_BASE_URL",
    "ANTHROPIC_BASE_URL",
)


def offline_env(base: Mapping[str, str]) -> dict:
    env = dict(base)
    for k in LLM_KEYS:
        env.pop(k, None)
    return env


def gemini_env(base: Mapping[str, str]) -> dict:
    return dict(base)


def _run(args: list[str], env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(args, env=env, capture_output=True, text=True)


def run_extract(repo: Path, out: Path, env: dict) -> subprocess.CompletedProcess:
    return _run(["graphify", "extract", str(repo), "--out", str(out)], env)


def run_cluster(
    out: Path,
    env: dict,
    *,
    label: bool,
    backend: str | None,
    model: str | None,
) -> subprocess.CompletedProcess:
    args = ["graphify", "cluster-only", str(out)]
    if not label:
        args.append("--no-label")
    if backend:
        args.append(f"--backend={backend}")
    if model:
        args.append(f"--model={model}")
    return _run(args, env)


def run_query(graph: Path, question: str, env: dict) -> str:
    return _run(["graphify", "query", question, "--graph", str(graph)], env).stdout


def run_explain(graph: Path, node: str, env: dict) -> str:
    return _run(["graphify", "explain", node, "--graph", str(graph)], env).stdout


def run_path(graph: Path, a: str, b: str, env: dict) -> str:
    return _run(["graphify", "path", a, b, "--graph", str(graph)], env).stdout
