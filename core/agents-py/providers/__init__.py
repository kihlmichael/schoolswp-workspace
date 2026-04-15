"""Factory de résolution de provider LLM.

Usage :
    from agents.providers import resolve_provider
    provider, model_name = resolve_provider("gemini:gemini-2.0-flash")
"""

from __future__ import annotations

import os
from functools import lru_cache

from agents.providers.base import LLMProvider, LLMRequest, LLMResponse

__all__ = ["LLMProvider", "LLMRequest", "LLMResponse", "clear_provider_cache", "resolve_provider"]

# Providers connus avec leur configuration par défaut
_KNOWN_PROVIDERS = {"anthropic", "openai", "gemini", "deepseek", "ollama"}

# Config OpenAI-compatible par provider
_OPENAI_COMPAT_CONFIG: dict[str, dict[str, str]] = {
    "openai": {
        "api_key_env": "OPENAI_API_KEY",
        "base_url_env": "OPENAI_BASE_URL",
        "default_base_url": "https://api.openai.com/v1",
    },
    "gemini": {
        "api_key_env": "GEMINI_API_KEY",
        "base_url_env": "GEMINI_BASE_URL",
        "default_base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
    },
    "deepseek": {
        "api_key_env": "DEEPSEEK_API_KEY",
        "base_url_env": "DEEPSEEK_BASE_URL",
        "default_base_url": "https://api.deepseek.com",
    },
    "ollama": {
        "api_key_env": "",
        "base_url_env": "OLLAMA_BASE_URL",
        "default_base_url": "http://localhost:11434/v1",
    },
}


def _parse_model_string(model_string: str) -> tuple[str, str]:
    """Parse 'provider:model' → (provider, model).

    Split sur le premier ':' uniquement pour supporter les noms
    de modèles contenant ':' (ex: ollama:llama3.3:70b).

    Sans préfixe connu ou modèle commençant par 'claude-' → anthropic.
    """
    if ":" in model_string:
        prefix, _, model_name = model_string.partition(":")
        if prefix in _KNOWN_PROVIDERS:
            return prefix, model_name
    # Pas de préfixe reconnu → Anthropic (rétrocompat)
    return "anthropic", model_string


@lru_cache(maxsize=16)
def _get_anthropic_provider() -> LLMProvider:
    from agents.providers.anthropic import AnthropicProvider

    return AnthropicProvider()


@lru_cache(maxsize=16)
def _get_openai_compat_provider(api_key: str | None, base_url: str) -> LLMProvider:
    from agents.providers.openai_compat import OpenAICompatProvider

    return OpenAICompatProvider(api_key=api_key, base_url=base_url)


def clear_provider_cache() -> None:
    """Vide le cache des providers — utile pour les tests."""
    _get_anthropic_provider.cache_clear()
    _get_openai_compat_provider.cache_clear()


def resolve_provider(model_string: str) -> tuple[LLMProvider, str]:
    """Résout un model string en (provider_instance, model_name_clean).

    Exemples :
        "claude-sonnet-4-6"       → (AnthropicProvider, "claude-sonnet-4-6")
        "openai:gpt-4o"           → (OpenAICompatProvider, "gpt-4o")
        "gemini:gemini-2.0-flash" → (OpenAICompatProvider, "gemini-2.0-flash")
        "ollama:llama3.3:70b"     → (OpenAICompatProvider, "llama3.3:70b")
    """
    provider_name, model_name = _parse_model_string(model_string)

    if provider_name == "anthropic":
        return _get_anthropic_provider(), model_name

    # Provider OpenAI-compatible
    config = _OPENAI_COMPAT_CONFIG[provider_name]
    api_key = os.getenv(config["api_key_env"]) if config["api_key_env"] else "ollama"
    base_url = os.getenv(config["base_url_env"], config["default_base_url"])

    return _get_openai_compat_provider(api_key, base_url), model_name
