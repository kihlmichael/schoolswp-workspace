"""Exemple d'agent schoolsWP qui combine retry, parsing strict, et PipelineError.

Pattern type pour un agent qui :
1. Appelle un LLM en tolerant les transients (rate limit, 5xx)
2. Valide strictement le format de sortie
3. Re-raise en PipelineError typee si l'echec est permanent
4. Log le contexte avant de raise

A adapter aux 28 agents existants dans core/agents-py/ qui ont besoin de robustesse.

Note : ce fichier est un exemple pedagogique. Pour l'integration reelle, copier la logique
dans l'agent concret (article_pipeline, content_factory, etc.).
"""

from __future__ import annotations

from agents.base import BaseContentAgent

from .errors import LLMParseError, PipelineError
from .retry import with_retry


class MonAgentRobuste(BaseContentAgent):
    """Agent demonstratif avec retry plus parsing strict plus PipelineError.

    Sequence :
    - with_retry envelope call_llm pour gerer les rate limit et 5xx du provider
    - _parse_output valide strictement le markdown attendu
    - Si parse echec apres retry : PipelineError pour signaler echec permanent a l'orchestrateur

    Le markdown de sortie ne contient JAMAIS d'erreur brute visible par l'utilisateur final.
    Les details d'exception vivent dans logs/agents.log via self._log.
    """

    name = "mon-agent-robuste"
    system_prompt = "Tu es un assistant qui repond en markdown commencant par un H1."

    async def run(self, *, topic: str, **kwargs) -> str:
        """Genere un markdown sur le topic avec retry plus parsing strict.

        Args:
            topic : sujet a traiter.

        Returns:
            Markdown valide commencant par un H1.

        Raises:
            PipelineError : si le LLM ne fournit pas de markdown parsable apres retry.
        """
        try:
            raw = await with_retry(
                lambda: self.call_llm(topic),
                max_attempts=3,
                base_delay_seconds=1.0,
            )
            return self._parse_output(raw)
        except LLMParseError as exc:
            self._log.error(
                "Parse impossible apres retry dans %s : %s",
                self.name,
                exc.context,
            )
            raise PipelineError(
                stage=self.name,
                message="Output LLM non parsable apres 3 tentatives",
                retryable=False,
            ) from exc

    def _parse_output(self, raw: str) -> str:
        """Validation stricte du markdown attendu.

        Raises:
            LLMParseError : si le format n'est pas conforme.
        """
        stripped = raw.strip()
        if not stripped.startswith("# "):
            raise LLMParseError(
                expected="Markdown commencant par un H1 (ligne '# ...')",
                raw_excerpt=raw[:200],
            )
        return stripped
