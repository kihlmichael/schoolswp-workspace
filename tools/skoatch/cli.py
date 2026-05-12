"""Skoatch CLI — wraps tools.skoatch.client for shell use.

Usage:
    .venv/Scripts/python -m tools.skoatch.cli env-check
    .venv/Scripts/python -m tools.skoatch.cli login --email x --password y --device-name z
    .venv/Scripts/python -m tools.skoatch.cli credits
    .venv/Scripts/python -m tools.skoatch.cli form-data
    .venv/Scripts/python -m tools.skoatch.cli generate-title --input "..." --language-id 1
    .venv/Scripts/python -m tools.skoatch.cli generate-structure --input "..." --language-id 1
    .venv/Scripts/python -m tools.skoatch.cli create --input "..." --language-id 1 [--payload payload.json] [--wait]
    .venv/Scripts/python -m tools.skoatch.cli status --id 42
    .venv/Scripts/python -m tools.skoatch.cli wait --id 42
    .venv/Scripts/python -m tools.skoatch.cli list [--per-page 15] [--page 1]
    .venv/Scripts/python -m tools.skoatch.cli update --id 42 --title "..." --content-file body.html
    .venv/Scripts/python -m tools.skoatch.cli publish --id 42
    .venv/Scripts/python -m tools.skoatch.cli mark-published --id 42 [--wordpress-url ...]
    .venv/Scripts/python -m tools.skoatch.cli delete --id 42
    .venv/Scripts/python -m tools.skoatch.cli projects
    .venv/Scripts/python -m tools.skoatch.cli project-posts --project-id 10
    .venv/Scripts/python -m tools.skoatch.cli mark-project-published --id 42

Token lookup order:
    1) --token CLI flag
    2) SKOATCH_TOKEN env var
    3) .env file in tools/skoatch/, then in the project root
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

from .client import (
    DEFAULT_BASE_URL,
    SkoatchClient,
    SkoatchError,
    pretty,
    status_label,
)

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parents[1]


def _load_env_file(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        out[key.strip()] = val.strip().strip('"').strip("'")
    return out


def resolve_token(cli_token: str | None) -> str:
    """Resolution order: --token > SKOATCH_TOKEN > tools/skoatch/.env > project .env.

    .env values override os.environ (per project convention: see
    memory/feedback_env_priority_over_os_environ.md).
    """
    if cli_token:
        return cli_token
    for env_path in (ROOT / ".env", PROJECT_ROOT / ".env"):
        env = _load_env_file(env_path)
        if env.get("SKOATCH_TOKEN"):
            return env["SKOATCH_TOKEN"]
    return os.environ.get("SKOATCH_TOKEN", "")


def _make_client(args: argparse.Namespace) -> SkoatchClient:
    token = resolve_token(getattr(args, "token", None))
    if not token:
        sys.stderr.write(
            "ERR: no Skoatch token found. Pass --token, set SKOATCH_TOKEN env var, "
            "or add SKOATCH_TOKEN=... to tools/skoatch/.env or the project .env.\n"
        )
        sys.exit(2)
    return SkoatchClient(token=token, base_url=args.base_url)


def _emit(payload: Any) -> None:
    sys.stdout.write(pretty(payload) + "\n")


def _ticker_factory():
    last_status: dict[str, Any] = {"id": None}

    def _on_tick(article: dict) -> None:
        status = article.get("job_status_id")
        if status != last_status["id"]:
            last_status["id"] = status
            sys.stderr.write(f"  [poll] status_id={status} ({status_label(status)})\n")
            sys.stderr.flush()

    return _on_tick


# ----------------------------------------------------------------- Commands


def cmd_env_check(args: argparse.Namespace) -> int:
    token = resolve_token(getattr(args, "token", None))
    sys.stdout.write(f"base_url:  {args.base_url}\n")
    sys.stdout.write(f"token:     {'OK (hidden)' if token else 'MISSING'}\n")
    if not token:
        return 2
    client = SkoatchClient(token=token, base_url=args.base_url)
    try:
        credits = client.get_credits()
    except SkoatchError as exc:
        sys.stdout.write(f"connection: FAIL ({exc})\n")
        return 1
    bal = credits.get("data", {}).get("credit_balance", "?")
    sys.stdout.write("connection: OK\n")
    sys.stdout.write(f"credits:    {bal}\n")
    return 0


def cmd_login(args: argparse.Namespace) -> int:
    token = SkoatchClient.login(
        email=args.email,
        password=args.password,
        device_name=args.device_name,
        base_url=args.base_url,
    )
    sys.stderr.write(
        "Token generated. Copy it into SKOATCH_TOKEN in your .env (or tools/skoatch/.env). Skoatch displays it once.\n"
    )
    sys.stdout.write(token + "\n")
    return 0


def cmd_credits(args: argparse.Namespace) -> int:
    _emit(_make_client(args).get_credits())
    return 0


def cmd_form_data(args: argparse.Namespace) -> int:
    _emit(_make_client(args).form_data())
    return 0


def cmd_generate_title(args: argparse.Namespace) -> int:
    _emit(_make_client(args).generate_title(args.input, args.language_id))
    return 0


def cmd_generate_structure(args: argparse.Namespace) -> int:
    _emit(_make_client(args).generate_structure(args.input, args.language_id, title=args.title))
    return 0


def _load_payload_file(path: str | None) -> dict:
    if not path:
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def cmd_create(args: argparse.Namespace) -> int:
    payload = _load_payload_file(args.payload)
    # CLI flags merge on top of the payload file
    if args.input:
        payload["input"] = args.input
    if args.title:
        payload["title"] = args.title
    if args.language_id is not None:
        payload["language_id"] = args.language_id
    if args.no_auto_generate:
        payload["is_auto_generated"] = False
    client = _make_client(args)
    response = client.create_article(payload)
    article = response.get("data") if "data" in response else response
    article_id = article.get("id")
    sys.stderr.write(f"Article created: id={article_id} status_id={article.get('job_status_id')}\n")
    if args.wait and article_id is not None and payload.get("is_auto_generated", True) is not False:
        sys.stderr.write("Waiting for completion (polling 30s / backoff 3min after 30min)...\n")
        final = client.poll_until_done(article_id, on_tick=_ticker_factory())
        _emit(final)
    else:
        _emit(response)
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    _emit(_make_client(args).get_article(args.id))
    return 0


def cmd_wait(args: argparse.Namespace) -> int:
    client = _make_client(args)
    final = client.poll_until_done(
        args.id,
        on_tick=_ticker_factory(),
        max_wait=args.max_wait,
    )
    _emit(final)
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    _emit(_make_client(args).list_articles(per_page=args.per_page, page=args.page))
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    content = Path(args.content_file).read_text(encoding="utf-8") if args.content_file else args.content
    if not content:
        sys.stderr.write("ERR: provide --content or --content-file\n")
        return 2
    extra = _load_payload_file(args.extra)
    _emit(_make_client(args).update_article(args.id, args.title, content, **extra))
    return 0


def cmd_publish(args: argparse.Namespace) -> int:
    _emit(_make_client(args).publish_article(args.id))
    return 0


def cmd_mark_published(args: argparse.Namespace) -> int:
    _emit(_make_client(args).mark_single_post_published(args.id, wordpress_url=args.wordpress_url))
    return 0


def cmd_delete(args: argparse.Namespace) -> int:
    _emit(_make_client(args).delete_article(args.id))
    return 0


def cmd_projects(args: argparse.Namespace) -> int:
    _emit(_make_client(args).list_projects())
    return 0


def cmd_project_posts(args: argparse.Namespace) -> int:
    _emit(_make_client(args).list_project_posts(args.project_id, per_page=args.per_page, page=args.page))
    return 0


def cmd_mark_project_published(args: argparse.Namespace) -> int:
    _emit(_make_client(args).mark_project_post_published(args.id, wordpress_url=args.wordpress_url))
    return 0


def cmd_mark_project_completed(args: argparse.Namespace) -> int:
    _emit(_make_client(args).mark_project_post_completed(args.id))
    return 0


# ----------------------------------------------------------------- argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="skoatch", description="Skoatch API CLI")
    p.add_argument("--base-url", default=DEFAULT_BASE_URL, help="API base URL (default: %(default)s)")
    p.add_argument("--token", default=None, help="Bearer token (overrides env)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("env-check", help="Verify token + reachability + balance").set_defaults(func=cmd_env_check)

    login = sub.add_parser("login", help="POST /sanctum/token (password accounts only)")
    login.add_argument("--email", required=True)
    login.add_argument("--password", required=True)
    login.add_argument("--device-name", required=True)
    login.set_defaults(func=cmd_login)

    sub.add_parser("credits", help="GET /credits").set_defaults(func=cmd_credits)
    sub.add_parser("form-data", help="GET /single-posts/form-data").set_defaults(func=cmd_form_data)

    gt = sub.add_parser("generate-title", help="POST /single-posts/generate-title (costs credits)")
    gt.add_argument("--input", required=True)
    gt.add_argument("--language-id", required=True, type=int)
    gt.set_defaults(func=cmd_generate_title)

    gs = sub.add_parser("generate-structure", help="POST /single-posts/generate-structure (costs credits)")
    gs.add_argument("--input", required=True)
    gs.add_argument("--language-id", required=True, type=int)
    gs.add_argument("--title", default=None)
    gs.set_defaults(func=cmd_generate_structure)

    cr = sub.add_parser("create", help="POST /single-posts — start generation")
    cr.add_argument("--input", default=None)
    cr.add_argument("--title", default=None)
    cr.add_argument("--language-id", type=int, default=None)
    cr.add_argument("--payload", default=None, help="JSON file with the full body (merged with CLI flags)")
    cr.add_argument("--no-auto-generate", action="store_true", help="Set is_auto_generated=false")
    cr.add_argument("--wait", action="store_true", help="Poll until terminal status")
    cr.set_defaults(func=cmd_create)

    st = sub.add_parser("status", help="GET /single-posts/{id}")
    st.add_argument("--id", required=True, type=int)
    st.set_defaults(func=cmd_status)

    wt = sub.add_parser("wait", help="Poll /single-posts/{id} until terminal")
    wt.add_argument("--id", required=True, type=int)
    wt.add_argument("--max-wait", type=int, default=7200, help="Max wait in seconds (default 2h)")
    wt.set_defaults(func=cmd_wait)

    ls = sub.add_parser("list", help="GET /single-posts (paginated)")
    ls.add_argument("--per-page", type=int, default=15)
    ls.add_argument("--page", type=int, default=1)
    ls.set_defaults(func=cmd_list)

    up = sub.add_parser("update", help="PUT /single-posts/{id}")
    up.add_argument("--id", required=True, type=int)
    up.add_argument("--title", required=True)
    up.add_argument("--content", default=None)
    up.add_argument("--content-file", default=None)
    up.add_argument("--extra", default=None, help="JSON file with extra fields")
    up.set_defaults(func=cmd_update)

    pb = sub.add_parser("publish", help="POST /single-posts/{id}/publish")
    pb.add_argument("--id", required=True, type=int)
    pb.set_defaults(func=cmd_publish)

    mp = sub.add_parser("mark-published", help="POST /single-posts/{id}/mark-as-published")
    mp.add_argument("--id", required=True, type=int)
    mp.add_argument("--wordpress-url", default=None)
    mp.set_defaults(func=cmd_mark_published)

    dl = sub.add_parser("delete", help="DELETE /single-posts/{id}")
    dl.add_argument("--id", required=True, type=int)
    dl.set_defaults(func=cmd_delete)

    sub.add_parser("projects", help="GET /projects").set_defaults(func=cmd_projects)

    pp = sub.add_parser("project-posts", help="GET /projects/{id}/posts")
    pp.add_argument("--project-id", required=True, type=int)
    pp.add_argument("--per-page", type=int, default=15)
    pp.add_argument("--page", type=int, default=1)
    pp.set_defaults(func=cmd_project_posts)

    mpp = sub.add_parser("mark-project-published", help="POST /posts/{id}/mark-as-published")
    mpp.add_argument("--id", required=True, type=int)
    mpp.add_argument("--wordpress-url", default=None)
    mpp.set_defaults(func=cmd_mark_project_published)

    mpc = sub.add_parser("mark-project-completed", help="POST /posts/{id}/mark-as-completed (status 21 -> 20)")
    mpc.add_argument("--id", required=True, type=int)
    mpc.set_defaults(func=cmd_mark_project_completed)

    return p


def _force_utf8_stdio() -> None:
    """Reconfigure stdout/stderr to UTF-8.

    Windows Python defaults to cp1252 which crashes on non-Latin1 chars
    (em-dash, arrows, etc.) when the CLI emits JSON containing them. We
    set errors="replace" so a stray unmappable char never aborts the run.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main(argv: list[str] | None = None) -> int:
    _force_utf8_stdio()
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except SkoatchError as exc:
        sys.stderr.write(f"ERR HTTP {exc.status_code}: {exc.args[0]}\n")
        if exc.body and isinstance(exc.body, (dict, list)):
            sys.stderr.write(pretty(exc.body) + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
