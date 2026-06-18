"""CLI de test manuel pour le client thruuu.

Usage :
    .venv/Scripts/python -m tools.thruuu-client.cli submit --keyword "tutor lms vs learndash"
    .venv/Scripts/python -m tools.thruuu-client.cli get <serp_id>
    .venv/Scripts/python -m tools.thruuu-client.cli analyze --keyword "fluentcrm avis" --country fr

Pour usage depuis script Python (recommande), importer ThruuuClient directement.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

# tools/thruuu-client/cli.py -> root
_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT))

from tools.thruuu_client import SerpRequest, ThruuuClient, ThruuuError  # noqa: E402


def _print_json(obj: object) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str))


async def _cmd_submit(args: argparse.Namespace) -> int:
    client = ThruuuClient()
    req = SerpRequest(
        keywords=args.keyword,
        country=args.country,
        language=args.language,
        device=args.device,
        num=args.num,
        include_llm=args.llm or [],
    )
    result = await client.submit(req)
    _print_json(result)
    return 0


async def _cmd_get(args: argparse.Namespace) -> int:
    client = ThruuuClient()
    result = await client.get(args.serp_id)
    _print_json(result)
    return 0


async def _cmd_list(args: argparse.Namespace) -> int:
    client = ThruuuClient()
    result = await client.list(page=args.page, per_page=args.per_page)
    _print_json(result)
    return 0


async def _cmd_analyze(args: argparse.Namespace) -> int:
    client = ThruuuClient()
    req = SerpRequest(
        keywords=args.keyword,
        country=args.country,
        language=args.language,
        device=args.device,
        num=args.num,
        include_llm=args.llm or [],
    )
    print(f"[analyze] submit + poll {len(req.keywords)} keyword(s)...", file=sys.stderr)
    results = await client.analyze(req, poll_interval=args.poll_interval, timeout=args.timeout)
    _print_json(results)
    return 0


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="thruuu client CLI - test manuel")
    sub = p.add_subparsers(dest="cmd", required=True)

    def _add_serp_args(parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--keyword", "-k", action="append", required=True, help="repeatable")
        parser.add_argument("--country", default="fr")
        parser.add_argument("--language", default="fr")
        parser.add_argument("--device", default="desktop", choices=["desktop", "mobile"])
        parser.add_argument("--num", type=int, default=10)
        parser.add_argument("--llm", action="append", help="chatgpt|gemini|perplexity|google-ai")

    sp_submit = sub.add_parser("submit", help="POST /serps")
    _add_serp_args(sp_submit)

    sp_get = sub.add_parser("get", help="GET /serps/:id")
    sp_get.add_argument("serp_id")

    sp_list = sub.add_parser("list", help="GET /serps/")
    sp_list.add_argument("--page", type=int, default=1)
    sp_list.add_argument("--per-page", type=int, default=20, dest="per_page")

    sp_analyze = sub.add_parser("analyze", help="submit + poll jusqu'au done")
    _add_serp_args(sp_analyze)
    sp_analyze.add_argument("--poll-interval", type=float, default=5.0, dest="poll_interval")
    sp_analyze.add_argument("--timeout", type=float, default=300.0)

    return p


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    handler = {
        "submit": _cmd_submit,
        "get": _cmd_get,
        "list": _cmd_list,
        "analyze": _cmd_analyze,
    }[args.cmd]
    try:
        return asyncio.run(handler(args))
    except ThruuuError as e:
        print(f"[thruuu error] {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
