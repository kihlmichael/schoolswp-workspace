import os


class Guardrails:
    """
    Garde-fous par run :
    - MAX_ITER : nombre max de passes orchestrateur
    - MAX_TOKENS : budget tokens total estimé par run
    - low_confidence_agents : détecte les agents en dessous du seuil
    - detect_conflicts : détecte les dépendances mutuelles à faible confiance
    """

    def __init__(self):
        self.iterations = 0
        self.total_tokens = 0
        self.MAX_ITER = int(os.getenv("MAX_ITER", 3))
        self.MAX_TOKENS = int(os.getenv("MAX_TOKENS_PER_RUN", 12000))
        self.CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", 0.7))

    def check(self) -> tuple[bool, str]:
        """Retourne (ok, reason). ok=False → stopper l'exécution."""
        if self.iterations >= self.MAX_ITER:
            return False, f"max_iterations ({self.MAX_ITER}) atteint"
        if self.total_tokens >= self.MAX_TOKENS:
            return False, f"budget_tokens ({self.MAX_TOKENS}) épuisé — consommé: {self.total_tokens}"
        return True, ""

    def tick(self, tokens: int = 600):
        self.iterations += 1
        self.total_tokens += tokens

    def low_confidence_agents(self, outputs: dict) -> list[str]:
        return [
            name
            for name, out in outputs.items()
            if isinstance(out, dict) and out.get("confidence", 1.0) < self.CONFIDENCE_THRESHOLD
        ]

    def detect_conflicts(self, outputs: dict) -> list[str]:
        """
        Heuristique simple : si agent A dépend de B ET B a une faible confiance → conflit potentiel.
        Étendre avec une analyse sémantique si besoin.
        """
        conflicts = []
        for agent, out in outputs.items():
            if not isinstance(out, dict):
                continue
            for dep in out.get("depends_on", []):
                # Extraire le nom de l'agent depuis "back_api_schema" → "back"
                dep_agent = dep.split("_")[0] if "_" in dep else dep
                if dep_agent in outputs and dep_agent != agent:
                    dep_conf = outputs[dep_agent].get("confidence", 1.0)
                    own_conf = out.get("confidence", 1.0)
                    if dep_conf < self.CONFIDENCE_THRESHOLD or own_conf < self.CONFIDENCE_THRESHOLD:
                        conflicts.append(
                            f"{agent} dépend de {dep} "
                            f"(confiance {agent}={own_conf:.2f}, {dep_agent}={dep_conf:.2f})"
                        )
        return conflicts

    @property
    def summary(self) -> dict:
        return {
            "iterations": self.iterations,
            "total_tokens_estimated": self.total_tokens,
            "max_iter": self.MAX_ITER,
            "max_tokens": self.MAX_TOKENS,
        }
