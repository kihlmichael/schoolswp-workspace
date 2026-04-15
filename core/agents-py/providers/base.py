"""Contrat d'abstraction LLM provider pour schoolsWP agents.

Définit le protocole que chaque provider doit implémenter,
ainsi que les objets de requête/réponse standardisés.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@dataclass
class LLMRequest:
    """Requête standardisée vers un provider LLM.

    Champs obligatoires : model, system, user_message.
    Champs optionnels extensibles sans casser l'API.
    """

    model: str
    system: str
    user_message: str
    max_tokens: int = 4096
    temperature: float | None = None
    stop_sequences: list[str] | None = None


@dataclass
class LLMResponse:
    """Réponse standardisée d'un provider LLM.

    Seul `text` est garanti non-vide. Les champs de métriques
    sont remplis si le provider les expose (0 par défaut).
    """

    text: str
    model: str = ""
    input_tokens: int = 0
    output_tokens: int = 0


@runtime_checkable
class LLMProvider(Protocol):
    """Protocole que chaque provider LLM doit satisfaire."""

    async def complete(self, request: LLMRequest) -> LLMResponse: ...
