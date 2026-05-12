"""Skoatch REST API client.

Wraps https://skoatch.com/api endpoints with Laravel Sanctum bearer auth.
All responses are returned as parsed JSON dicts. HTTP errors raise SkoatchError
with status_code, message and raw body.
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass
from typing import Any

import requests

DEFAULT_BASE_URL = "https://skoatch.com/api"
DEFAULT_TIMEOUT = 60

TERMINAL_SUCCESS = 20
TERMINAL_ERRORS = {30, 31, 33, 35, 36}
TERMINAL_STATUSES = {TERMINAL_SUCCESS, *TERMINAL_ERRORS}

JOB_STATUS_LABELS = {
    1: "En attente",
    2: "Generation en cours",
    4: "Etape intermediaire (post-fetch?)",  # observed 2026-05-11 articles 1196078/1196166/1196181
    6: "Images demandees",
    9: "Images recuperees",
    13: "Images in-content demandees",
    14: "Images in-content recuperees",
    16: "Etape intermediaire (pre-finalisation?)",  # observed 2026-05-11 articles 1196078/1196166/1196181
    17: "Etape intermediaire (post-generation?)",  # observed 2026-05-11 article 1196181
    20: "Termine",
    21: "Publie",
    22: "Archive",
    30: "Erreur technique",
    31: "Erreur fetch URL",
    32: "Erreur images (1)",
    33: "Erreur images max",
    34: "Erreur images (2)",
    35: "Erreur images max",
    36: "Retry max atteint",
    40: "Retry automatique",
}


log = logging.getLogger("skoatch")


class SkoatchError(RuntimeError):
    """Raised when the API returns a non-2xx response."""

    def __init__(self, status_code: int, message: str, body: Any = None):
        super().__init__(f"HTTP {status_code}: {message}")
        self.status_code = status_code
        self.body = body


@dataclass
class SkoatchClient:
    token: str
    base_url: str = DEFAULT_BASE_URL
    timeout: int = DEFAULT_TIMEOUT

    def __post_init__(self) -> None:
        if not self.token:
            raise SkoatchError(0, "Missing Skoatch bearer token")
        self.base_url = self.base_url.rstrip("/")
        self._session = requests.Session()
        self._session.headers.update(
            {
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "schoolswp-skoatch-client/0.1",
            }
        )

    # ------------------------------------------------------------------ HTTP
    def _request(self, method: str, path: str, *, json_body: Any = None, params: dict | None = None) -> dict:
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            resp = self._session.request(
                method,
                url,
                json=json_body,
                params=params,
                timeout=self.timeout,
            )
        except requests.RequestException as exc:
            raise SkoatchError(0, f"Network error: {exc}") from exc

        if resp.status_code >= 400:
            try:
                body = resp.json()
                message = body.get("message") or body.get("error") or resp.text[:200]
            except ValueError:
                body = resp.text
                message = resp.text[:200] or resp.reason
            raise SkoatchError(resp.status_code, message, body)

        if not resp.content:
            return {}
        try:
            return resp.json()
        except ValueError as exc:
            raise SkoatchError(resp.status_code, f"Invalid JSON in response: {exc}", resp.text) from exc

    # ------------------------------------------------------------------ Auth
    @classmethod
    def login(
        cls,
        email: str,
        password: str,
        device_name: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> str:
        """POST /api/sanctum/token. Returns the raw bearer token string.

        Only works for accounts with a password set (not Google-only accounts).
        """
        url = f"{base_url.rstrip('/')}/sanctum/token"
        resp = requests.post(
            url,
            json={"email": email, "password": password, "device_name": device_name},
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            timeout=timeout,
        )
        if resp.status_code >= 400:
            try:
                body = resp.json()
                msg = body.get("message", resp.text[:200])
            except ValueError:
                body = resp.text
                msg = resp.text[:200]
            raise SkoatchError(resp.status_code, msg, body)
        token = resp.text.strip().strip('"')
        if not token or " " in token:
            raise SkoatchError(0, f"Unexpected token response: {resp.text[:120]!r}")
        return token

    # --------------------------------------------------------------- Credits
    def get_credits(self) -> dict:
        return self._request("GET", "credits")

    # --------------------------------------------------------------- Helpers
    def form_data(self) -> dict:
        """Returns sites, languages, statuses, video positions, prompts, image styles."""
        return self._request("GET", "single-posts/form-data")

    def generate_title(self, input_text: str, language_id: int) -> dict:
        return self._request(
            "POST",
            "single-posts/generate-title",
            json_body={"input": input_text, "language_id": language_id},
        )

    def generate_structure(self, input_text: str, language_id: int, title: str | None = None) -> dict:
        body: dict[str, Any] = {"input": input_text, "language_id": language_id}
        if title:
            body["title"] = title
        return self._request("POST", "single-posts/generate-structure", json_body=body)

    # ------------------------------------------------------------- Articles
    def create_article(self, payload: dict) -> dict:
        """POST /api/single-posts. Returns immediately with the article id.

        At least one of `input` or `title` must be in payload.
        With is_auto_generated: true (default), generation starts asynchronously.
        Poll get_article(id) until job_status_id reaches a terminal value.
        """
        if not payload.get("input") and not payload.get("title"):
            raise SkoatchError(0, "Either 'input' or 'title' is required")
        if "language_id" not in payload:
            raise SkoatchError(0, "'language_id' is required")
        return self._request("POST", "single-posts", json_body=payload)

    def get_article(self, post_id: int) -> dict:
        return self._request("GET", f"single-posts/{post_id}")

    def list_articles(self, per_page: int = 15, page: int = 1) -> dict:
        return self._request("GET", "single-posts", params={"per_page": per_page, "page": page})

    def update_article(self, post_id: int, title: str, content: str, **extra: Any) -> dict:
        body = {"title": title, "content": content, **extra}
        return self._request("PUT", f"single-posts/{post_id}", json_body=body)

    def publish_article(self, post_id: int) -> dict:
        return self._request("POST", f"single-posts/{post_id}/publish")

    def mark_single_post_published(self, post_id: int, wordpress_url: str | None = None) -> dict:
        body = {"wordpress_url": wordpress_url} if wordpress_url else None
        return self._request("POST", f"single-posts/{post_id}/mark-as-published", json_body=body)

    def delete_article(self, post_id: int) -> dict:
        return self._request("DELETE", f"single-posts/{post_id}")

    # --------------------------------------------------------------- Projects
    def list_projects(self) -> dict:
        return self._request("GET", "projects")

    def list_project_posts(self, project_id: int, per_page: int = 15, page: int = 1) -> dict:
        return self._request(
            "GET",
            f"projects/{project_id}/posts",
            params={"per_page": per_page, "page": page},
        )

    def mark_project_post_published(self, post_id: int, wordpress_url: str | None = None) -> dict:
        body = {"wordpress_url": wordpress_url} if wordpress_url else None
        return self._request("POST", f"posts/{post_id}/mark-as-published", json_body=body)

    def mark_project_post_completed(self, post_id: int) -> dict:
        return self._request("POST", f"posts/{post_id}/mark-as-completed")

    # --------------------------------------------------------------- Polling
    def poll_until_done(
        self,
        post_id: int,
        *,
        on_tick=None,
        fast_interval: int = 30,
        slow_interval: int = 180,
        switch_after: int = 1800,
        max_wait: int = 7200,
    ) -> dict:
        """Polls GET /single-posts/{id} until a terminal job_status_id is reached.

        Strategy: every `fast_interval`s during the first `switch_after` seconds,
        then every `slow_interval`s up to `max_wait` seconds total. Beyond
        `max_wait`, raises SkoatchError(408) — the post is not lost, callers can
        resume with `get_article(id)` later.

        `on_tick(article)` is called after every poll (useful for CLI progress).
        Returns the final article payload.
        """
        start = time.monotonic()
        while True:
            resp = self.get_article(post_id)
            article = resp.get("data") if "data" in resp else resp
            if on_tick:
                try:
                    on_tick(article)
                except Exception:  # noqa: BLE001 - never let a callback kill the poll
                    log.exception("on_tick callback failed")
            status = article.get("job_status_id")
            if status in TERMINAL_STATUSES:
                return resp
            elapsed = time.monotonic() - start
            if elapsed > max_wait:
                raise SkoatchError(
                    408,
                    f"Polling timeout after {int(elapsed)}s — article {post_id} still at status {status}. "
                    "Call get_article(id) later to resume.",
                )
            interval = fast_interval if elapsed < switch_after else slow_interval
            time.sleep(interval)


def status_label(status_id: int | None) -> str:
    if status_id is None:
        return "?"
    return JOB_STATUS_LABELS.get(status_id, f"status {status_id}")


def pretty(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)
