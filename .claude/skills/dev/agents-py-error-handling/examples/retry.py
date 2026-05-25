"""Retry helper avec exponential backoff plus jitter pour les calls LLM et MCP.

A copier dans core/agents-py/retry.py et importer dans les agents qui en ont besoin.

Comportement par defaut : retry uniquement si l'exception est une AgentError avec retryable=True.
Cas particulier : LLMRateLimitError fournit son propre retry_after_seconds, respecte au lieu du backoff calcule.

Port Python du pattern TypeScript du skill source ECC error-handling.
"""

from __future__ import annotations

import asyncio
import logging
import random
from collections.abc import Awaitable, Callable
from typing import TypeVar

from .errors import AgentError, LLMRateLimitError

T = TypeVar("T")
_log = logging.getLogger("agents.retry")


async def with_retry(
    fn: Callable[[], Awaitable[T]],
    *,
    max_attempts: int = 3,
    base_delay_seconds: float = 0.5,
    max_delay_seconds: float = 30.0,
    retry_if: Callable[[Exception], bool] | None = None,
) -> T:
    """Retry une coroutine avec exponential backoff plus jitter.

    Args:
        fn : coroutine sans argument a retry (utiliser lambda ou functools.partial).
        max_attempts : nombre maximum de tentatives (default 3).
        base_delay_seconds : delai de base avant le 2e essai.
        max_delay_seconds : plafond du delai (evite les attentes trop longues).
        retry_if : predicat sur l'exception. Par defaut, retry uniquement si AgentError.retryable est True.

    Returns:
        Le resultat de fn() si une tentative a reussi.

    Raises:
        La derniere exception levee si toutes les tentatives ont echoue, ou si retry_if a renvoye False.
    """
    if retry_if is None:

        def retry_if(e: Exception) -> bool:
            return isinstance(e, AgentError) and e.retryable

    last_exc: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            return await fn()
        except Exception as exc:
            last_exc = exc
            if attempt == max_attempts or not retry_if(exc):
                raise

            if isinstance(exc, LLMRateLimitError):
                delay = exc.retry_after_seconds
            else:
                jitter = random.random() * base_delay_seconds
                delay = min(
                    base_delay_seconds * (2 ** (attempt - 1)) + jitter,
                    max_delay_seconds,
                )

            _log.warning(
                "Retry %d/%d apres %.2fs (raison : %s)",
                attempt,
                max_attempts,
                delay,
                exc,
            )
            await asyncio.sleep(delay)

    if last_exc:
        raise last_exc
    raise RuntimeError("with_retry : execution impossible (max_attempts <= 0 ?)")
