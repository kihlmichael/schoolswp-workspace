"""Circuit breaker pour proteger les calls MCP externes contre les downtimes prolonges.

A copier dans core/agents-py/circuit_breaker.py et importer dans les wrappers MCP.

Pattern 3 etats :
- CLOSED : normal, requetes passent.
- OPEN : trop d'echecs consecutifs, requetes bloquees pendant cooldown_seconds.
- HALF_OPEN : apres le cooldown, un seul appel autorise. Si OK -> CLOSED, si KO -> OPEN.

Une instance par MCP cible (Novamira, n8n, DataForSEO).
Combine avec with_retry : retry gere les transients d'un meme call, circuit gere le downtime global.

Note : ECC error-handling mentionne circuit breaker dans la description du skill source mais
ne l'implemente pas. Cette implementation comble ce trou pour le contexte schoolsWP.
"""

from __future__ import annotations

import asyncio
import logging
import time
from collections.abc import Awaitable, Callable
from enum import Enum
from typing import TypeVar

T = TypeVar("T")
_log = logging.getLogger("agents.circuit_breaker")


class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitBreakerOpen(Exception):
    """Le circuit est ouvert, requete refusee sans tenter l'appel."""

    def __init__(self, name: str, reopen_in_seconds: float) -> None:
        super().__init__(f"Circuit '{name}' ouvert, reessayer dans {reopen_in_seconds:.1f}s")
        self.name = name
        self.reopen_in_seconds = reopen_in_seconds


class CircuitBreaker:
    """Circuit breaker simple pour proteger les calls MCP externes.

    Args:
        name : identifiant du circuit (utilise dans les logs).
        failure_threshold : nombre d'echecs consecutifs avant ouverture (default 5).
        cooldown_seconds : duree d'attente avant test HALF_OPEN (default 60).
    """

    def __init__(
        self,
        name: str,
        *,
        failure_threshold: int = 5,
        cooldown_seconds: float = 60.0,
    ) -> None:
        self.name = name
        self.failure_threshold = failure_threshold
        self.cooldown_seconds = cooldown_seconds

        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._opened_at: float | None = None
        self._lock = asyncio.Lock()

    async def call(self, fn: Callable[[], Awaitable[T]]) -> T:
        """Execute fn() a travers le circuit breaker.

        Raises:
            CircuitBreakerOpen : si le circuit est ouvert et que le cooldown n'est pas ecoule.
            L'exception originale de fn() en cas d'echec.
        """
        async with self._lock:
            now = time.monotonic()

            if self._state == CircuitState.OPEN:
                elapsed = now - (self._opened_at or now)
                if elapsed < self.cooldown_seconds:
                    raise CircuitBreakerOpen(self.name, self.cooldown_seconds - elapsed)
                _log.info("Circuit '%s' passe HALF_OPEN apres cooldown", self.name)
                self._state = CircuitState.HALF_OPEN

        try:
            result = await fn()
        except Exception:
            async with self._lock:
                self._failure_count += 1
                should_open = self._state == CircuitState.HALF_OPEN or self._failure_count >= self.failure_threshold
                if should_open:
                    self._state = CircuitState.OPEN
                    self._opened_at = time.monotonic()
                    _log.warning(
                        "Circuit '%s' OUVERT apres %d echecs (cooldown %.0fs)",
                        self.name,
                        self._failure_count,
                        self.cooldown_seconds,
                    )
            raise

        async with self._lock:
            if self._state == CircuitState.HALF_OPEN:
                _log.info("Circuit '%s' referme apres test HALF_OPEN reussi", self.name)
            self._state = CircuitState.CLOSED
            self._failure_count = 0
            self._opened_at = None

        return result

    def reset(self) -> None:
        """Reset force du circuit a l'etat CLOSED. A utiliser apres incident manuel."""
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._opened_at = None
        _log.info("Circuit '%s' reset manuellement", self.name)
