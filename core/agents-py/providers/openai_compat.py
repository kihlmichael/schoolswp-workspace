"""Provider OpenAI-compatible — couvre GPT-4o, Gemini, DeepSeek, Ollama.

Utilise le SDK `openai` (AsyncOpenAI) avec des base_url configurables.
Import conditionnel : si le SDK n'est pas installé, une erreur claire est levée.
"""

from __future__ import annotations

from agents.providers.base import LLMRequest, LLMResponse

try:
    from openai import AsyncOpenAI
except ImportError:
    AsyncOpenAI = None  # type: ignore[assignment,misc]

_INSTALL_MSG = (
    "Le SDK openai est requis pour les providers non-Anthropic. "
    "Installe-le avec : uv pip install 'schoolswp-agents[multi-provider]' "
    "ou : pip install openai>=1.0.0"
)


class OpenAICompatProvider:
    """Provider pour toute API compatible OpenAI Chat Completions.

    Fonctionne avec : OpenAI, Gemini (via endpoint compatible), DeepSeek, Ollama.
    """

    def __init__(self, *, api_key: str | None = None, base_url: str | None = None) -> None:
        if AsyncOpenAI is None:
            raise ImportError(_INSTALL_MSG)
        kwargs: dict = {}
        if api_key is not None:
            kwargs["api_key"] = api_key
        if base_url is not None:
            kwargs["base_url"] = base_url
        self._client = AsyncOpenAI(**kwargs)

    async def complete(self, request: LLMRequest) -> LLMResponse:
        messages: list[dict] = []
        if request.system:
            messages.append({"role": "system", "content": request.system})
        messages.append({"role": "user", "content": request.user_message})

        kwargs: dict = {
            "model": request.model,
            "max_tokens": request.max_tokens,
            "messages": messages,
        }
        if request.temperature is not None:
            kwargs["temperature"] = request.temperature
        if request.stop_sequences is not None:
            kwargs["stop"] = request.stop_sequences

        response = await self._client.chat.completions.create(**kwargs)

        choice = response.choices[0]
        usage = getattr(response, "usage", None)
        return LLMResponse(
            text=choice.message.content or "",
            model=getattr(response, "model", request.model) or request.model,
            input_tokens=getattr(usage, "prompt_tokens", 0) if usage else 0,
            output_tokens=getattr(usage, "completion_tokens", 0) if usage else 0,
        )
