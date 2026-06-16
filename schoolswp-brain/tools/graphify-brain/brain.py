"""graphify-brain CLI: the guardrail wrapper. graphify maps; schoolsWP decides."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import changes
import config
import cost
import graphify_runner
import logbook
import md_local_index
import secrets_scan

DEFAULT_ALLOWLIST = Path(__file__).resolve().parent / "allowlist.yml"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _head(repo: Path) -> str:
    out = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, check=True)
    return out.stdout.strip()


def _state_file(cfg: config.BrainConfig) -> Path:
    return cfg.repo_path / "schoolswp-brain" / "07_graph" / ".brain-state.json"


def _log_dir(cfg: config.BrainConfig) -> Path:
    return cfg.repo_path / "schoolswp-brain" / "07_graph" / "logs"


def _dry_run(cfg: config.BrainConfig, env: dict, *, show_files: bool = False):
    since = logbook.read_state(_state_file(cfg)).get("last_indexed_commit")
    delta = changes.changed_files(cfg.repo_path, since, cfg.roots, cfg.exclude)
    _, egress_changed = changes.split_local_vs_egress(delta, cfg.roots)
    egress = changes.gemini_corpus(cfg.repo_path, cfg.roots, cfg.exclude)
    est = cost.estimate([cfg.repo_path / p for p in egress], cfg.gemini_model)
    print("=== DRY-RUN (nothing is sent) ===")
    print(
        f"changed since last index: {len(delta.new)} new, {len(delta.modified)} modified "
        f"({len(egress_changed)} Gemini-bound markdown)"
    )
    print(
        f"a --gemini refresh re-processes the FULL Gemini corpus: {len(egress)} "
        f"markdown file(s) under gemini roots -> {cfg.gemini_model}"
    )
    print("code + markdown structure stay LOCAL (always offline)")
    print(f"est. tokens: {est.est_tokens}  est. cost: ${est.est_usd}")
    if show_files:
        for p in egress:
            print(f"  -> {p}")
    return egress, est


def cmd_refresh(args, cfg: config.BrainConfig, env: dict) -> int:
    if args.dry_run:
        _dry_run(cfg, env, show_files=args.changed)
        return 0

    if args.local:
        # Couche 1: code AST offline. Couche 2: local markdown structural index (no LLM).
        ignore = config.compile_graphifyignore(cfg, mode="code-only")
        (cfg.repo_path / ".graphifyignore").write_text(ignore, encoding="utf-8")
        oenv = graphify_runner.offline_env(env)
        graphify_runner.run_extract(cfg.repo_path, cfg.output_path, oenv)
        graphify_runner.run_cluster(cfg.output_path, oenv, label=False, backend=None, model=None)
        docs = []
        for r in cfg.roots:
            root_dir = cfg.repo_path / r.path
            if root_dir.exists():
                docs.extend(md_local_index.scan_tree(root_dir, cfg.exclude))
        cfg.output_path.mkdir(parents=True, exist_ok=True)
        (cfg.output_path / "md-local-index.json").write_text(
            json.dumps([asdict(d) for d in docs], ensure_ascii=False, indent=2), encoding="utf-8"
        )
        commit = _head(cfg.repo_path)
        logbook.write_state(_state_file(cfg), commit)
        logbook.append_log(
            _log_dir(cfg),
            logbook.RefreshLogEntry(
                date=_now(),
                command="refresh --local",
                files_analyzed=len(docs),
                files_sent=0,
                model=None,
                est_cost_usd=0.0,
                real_cost_usd=0.0,
                result="ok",
            ),
        )
        print(f"refresh --local done (offline, 0 egress; {len(docs)} md docs structurally indexed).")
        return 0

    if args.gemini:
        egress, est = _dry_run(cfg, env, show_files=True)
        if not args.yes:
            print(
                "\nREFUSED: refresh --gemini requires explicit --yes after reviewing the dry-run.",
                file=sys.stderr,
            )
            return 2
        hits = secrets_scan.scan_files([cfg.repo_path / p for p in egress])
        if hits:
            for h in hits:
                print(f"SECRET? {h.path}:{h.line} [{h.pattern}]", file=sys.stderr)
            print("ABORTED: secret-looking content in the egress set.", file=sys.stderr)
            return 3
        ignore = config.compile_graphifyignore(cfg, mode="full")
        (cfg.repo_path / ".graphifyignore").write_text(ignore, encoding="utf-8")
        genv = graphify_runner.gemini_env(env)
        graphify_runner.run_extract(cfg.repo_path, cfg.output_path, genv)
        graphify_runner.run_cluster(cfg.output_path, genv, label=True, backend="gemini", model=cfg.gemini_model)
        commit = _head(cfg.repo_path)
        logbook.write_state(_state_file(cfg), commit)
        logbook.append_log(
            _log_dir(cfg),
            logbook.RefreshLogEntry(
                date=_now(),
                command="refresh --gemini",
                files_analyzed=len(egress),
                files_sent=len(egress),
                model=cfg.gemini_model,
                est_cost_usd=est.est_usd,
                real_cost_usd=None,
                result="ok",
            ),
        )
        print(f"refresh --gemini done ({len(egress)} file(s) processed by {cfg.gemini_model}).")
        return 0

    print("nothing to do: pass --local, --changed --dry-run, or --gemini --yes", file=sys.stderr)
    return 1


def _graph_path(cfg: config.BrainConfig) -> Path:
    return cfg.output_path / "graphify-out" / "graph.json"


def cmd_query(args, cfg, env):
    print(graphify_runner.run_query(_graph_path(cfg), args.question, env))
    return 0


def cmd_explain(args, cfg, env):
    print(graphify_runner.run_explain(_graph_path(cfg), args.node, env))
    return 0


def cmd_path(args, cfg, env):
    print(graphify_runner.run_path(_graph_path(cfg), args.a, args.b, env))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="brain", description="schoolsWP second brain (graphify wrapper)")
    sub = p.add_subparsers(dest="cmd", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--allowlist", default=str(DEFAULT_ALLOWLIST))

    r = sub.add_parser("refresh", parents=[common])
    r.add_argument("--local", action="store_true")
    r.add_argument("--changed", action="store_true")
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("--gemini", action="store_true")
    r.add_argument("--yes", action="store_true")
    r.set_defaults(func=cmd_refresh)

    q = sub.add_parser("query", parents=[common])
    q.add_argument("question")
    q.set_defaults(func=cmd_query)
    e = sub.add_parser("explain", parents=[common])
    e.add_argument("node")
    e.set_defaults(func=cmd_explain)
    pa = sub.add_parser("path", parents=[common])
    pa.add_argument("a")
    pa.add_argument("b")
    pa.set_defaults(func=cmd_path)
    return p


def main(argv: list[str] | None = None, env: dict | None = None) -> int:
    env = dict(env if env is not None else os.environ)
    args = build_parser().parse_args(argv)
    cfg = config.load_config(Path(args.allowlist), env)
    return args.func(args, cfg, env)


if __name__ == "__main__":
    raise SystemExit(main())
