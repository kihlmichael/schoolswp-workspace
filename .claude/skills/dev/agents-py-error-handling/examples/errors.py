"""Hierarchie d'exceptions schoolsWP.

A copier dans core/agents-py/errors.py et importer dans les agents qui en ont besoin.

Toutes les classes derivent d'AgentError qui porte :
- code : identifiant string pour mapping et logs
- retryable : flag qui guide le retry helper
- context : dict avec details (provider, operation, excerpt)
"""

from __future__ import annotations


class AgentError(Exception):
    """Base error pour tous les agents schoolsWP."""

    def __init__(
        self,
        message: str,
        code: str,
        *,
        retryable: bool = False,
        context: dict | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.retryable = retryable
        self.context = context or {}


class LLMProviderError(AgentError):
    """Erreur d'appel a un provider LLM (Anthropic, OpenAI, Gemini, DeepSeek, Ollama)."""

    def __init__(
        self,
        provider: str,
        message: str,
        *,
        retryable: bool = True,
        context: dict | None = None,
    ) -> None:
        super().__init__(
            f"[{provider}] {message}",
            code="LLM_PROVIDER_ERROR",
            retryable=retryable,
            context={"provider": provider, **(context or {})},
        )


class LLMRateLimitError(LLMProviderError):
    """Rate limit hit sur un provider LLM. Retryable apres delai."""

    def __init__(self, provider: str, retry_after_seconds: float = 15.0) -> None:
        super().__init__(
            provider,
            f"Rate limit hit, retry apres {retry_after_seconds}s",
            retryable=True,
            context={"retry_after_seconds": retry_after_seconds},
        )
        self.retry_after_seconds = retry_after_seconds


class MCPCallError(AgentError):
    """Erreur d'appel a un MCP externe (Novamira, n8n, DataForSEO)."""

    def __init__(
        self,
        server: str,
        operation: str,
        message: str,
        *,
        retryable: bool = True,
    ) -> None:
        super().__init__(
            f"[MCP:{server}] {operation} a echoue : {message}",
            code="MCP_CALL_ERROR",
            retryable=retryable,
            context={"server": server, "operation": operation},
        )


class LLMParseError(AgentError):
    """La sortie LLM n'a pas pu etre parsee (JSON malforme, structure attendue absente)."""

    def __init__(self, expected: str, raw_excerpt: str) -> None:
        super().__init__(
            f"Parse echec : attendu {expected}, recu : {raw_excerpt[:120]}",
            code="LLM_PARSE_ERROR",
            retryable=False,
            context={"expected": expected, "excerpt": raw_excerpt[:500]},
        )


class PipelineError(AgentError):
    """Erreur dans un pipeline multi-etapes. Identifie l'etape qui a echoue."""

    def __init__(self, stage: str, message: str, *, retryable: bool = False) -> None:
        super().__init__(
            f"Pipeline stage '{stage}' : {message}",
            code="PIPELINE_ERROR",
            retryable=retryable,
            context={"stage": stage},
        )


class ConfigurationError(AgentError):
    """Erreur de configuration (env var manquante, fichier .env invalide, model unknown)."""

    def __init__(self, message: str) -> None:
        super().__init__(message, code="CONFIGURATION_ERROR", retryable=False)
