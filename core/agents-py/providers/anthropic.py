"""Provider Anthropic — wrapper AsyncAnthropic.

Comportement identique à l'ancien call_llm() de BaseContentAgent.
"""

from __future__ import annotations

from anthropic import AsyncAnthropic

from agents.providers.base import LLMRequest, LLMResponse


class AnthropicProvider:
    """Provider pour les modèles Claude via l'API Anthropic."""

    def __init__(self) -> None:
        self._client = AsyncAnthropic()

    async def complete(self, request: LLMRequest) -> LLMResponse:
        kwargs: dict = {
            "model": request.model,
            "max_tokens": request.max_tokens,
            "system": request.system,
            "messages": [{"role": "user", "content": request.user_message}],
        }
        if request.temperature is not None:
            kwargs["temperature"] = request.temperature
        if request.stop_sequences is not None:
            kwargs["stop_sequences"] = request.stop_sequences

        response = await self._client.messages.create(**kwargs)

        usage = getattr(response, "usage", None)
        return LLMResponse(
            text=response.content[0].text,
            model=getattr(response, "model", request.model),
            input_tokens=getattr(usage, "input_tokens", 0) if usage else 0,
            output_tokens=getattr(usage, "output_tokens", 0) if usage else 0,
        )
