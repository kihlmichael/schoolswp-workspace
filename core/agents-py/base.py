import logging
import logging.handlers
import os
from pathlib import Path

from anthropic import AsyncAnthropic


def _setup_logging() -> None:
    """Configure le logging centralisé avec rotation automatique.

    - Fichier : logs/agents.log (10 MB max, 5 fichiers conservés)
    - Console : WARNING et plus seulement
    - Format  : timestamp | niveau | logger | message
    """
    log_dir = Path(__file__).resolve().parent.parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)

    root = logging.getLogger("agents")
    if root.handlers:
        return  # déjà configuré (import multiple)

    root.setLevel(logging.DEBUG)

    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    # Handler fichier rotatif — 10 MB × 5 = 50 MB max
    fh = logging.handlers.RotatingFileHandler(
        log_dir / "agents.log",
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    # Handler console — WARNING+ uniquement (ne pollue pas le stdout des CLIs)
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)
    ch.setFormatter(fmt)

    root.addHandler(fh)
    root.addHandler(ch)


# Charge automatiquement ANTHROPIC_API_KEY depuis les .env connus
# (priorité : agents/.env > racine workspace > multi-agent-system/.env)
def _load_env() -> None:
    if os.getenv("ANTHROPIC_API_KEY"):
        return  # déjà défini — pas besoin de charger
    try:
        from dotenv import load_dotenv  # type: ignore[import-untyped]

        # core/agents-py/base.py → project root = parent.parent.parent
        _root = Path(__file__).resolve().parent.parent.parent
        for candidate in [
            _root / "agents" / ".env",
            _root / ".env",
            _root / "multi-agent-system" / ".env",
        ]:
            if candidate.exists():
                load_dotenv(candidate, override=False)
                if os.getenv("ANTHROPIC_API_KEY"):
                    break
    except ImportError:
        pass  # python-dotenv absent — l'utilisateur doit exporter la variable manuellement


_load_env()
_setup_logging()

_logger = logging.getLogger("agents")


def safe_read_path(file_arg: str) -> Path:
    """Résout et valide un chemin de lecture — protection path traversal.

    Lève ValueError si le chemin sort du répertoire de travail courant.
    """
    p = Path(file_arg).resolve()
    cwd = Path.cwd().resolve()
    if not p.is_relative_to(cwd):
        raise ValueError(f"Accès refusé : '{file_arg}' est hors du répertoire de travail ({cwd})")
    if not p.exists():
        raise FileNotFoundError(f"Fichier introuvable : {p}")
    return p


def safe_write_path(path_arg: str) -> Path:
    """Résout et valide un chemin d'écriture — protection path traversal.

    Lève ValueError si le chemin sort du répertoire de travail courant.
    """
    p = Path(path_arg).resolve()
    cwd = Path.cwd().resolve()
    if not p.is_relative_to(cwd):
        raise ValueError(f"Accès refusé : '{path_arg}' est hors du répertoire de travail ({cwd})")
    return p


class BaseContentAgent:
    """
    Agent de base pour la génération de contenu schoolsWP.

    Trois catégories d'agents héritent de cette classe :

    1. Agents simples (retournent str) — ex: SeoWriterAgent, WpTeacherAgent
       → Utiliser ``call_llm(user_message)`` dans run()

    2. Agents audit (retournent une dataclass parsée) — ex: SeoAuditorAgent
       → Utiliser ``call_llm(user_message)`` puis ``ResultClass.parse(raw)``

    3. Agents orchestrateurs (délèguent à des sous-agents) — ex: PublishReadyAgent
       → Instancier les sous-agents et les appeler directement

    Attributs de classe :
        name          : identifiant kebab-case (ex: "seo-writer")
        system_prompt : prompt système LLM
        max_tokens    : limite de tokens par défaut (4096, surcharger si besoin)
    """

    name: str = "base"
    system_prompt: str = ""
    max_tokens: int = 4096

    def __init__(self, model: str | None = None) -> None:
        self.model = model or os.getenv("MODEL_WRITER", "claude-sonnet-4-6")
        self._client = AsyncAnthropic()
        self._log = logging.getLogger(f"agents.{self.name}")

    async def call_llm(self, user_message: str, *, max_tokens: int | None = None) -> str:
        """Appel LLM standardisé — élimine le boilerplate des 30 agents.

        Args:
            user_message : message utilisateur à envoyer
            max_tokens   : override ponctuel (sinon utilise self.max_tokens)

        Returns:
            Texte brut de la réponse LLM.
        """
        self._log.debug("call_llm → %s (%d tokens max)", self.name, max_tokens or self.max_tokens)
        response = await self._client.messages.create(
            model=self.model,
            max_tokens=max_tokens or self.max_tokens,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        text = response.content[0].text
        self._log.debug("call_llm ← %s (%d chars)", self.name, len(text))
        return text

    async def run(self, **kwargs) -> str:
        raise NotImplementedError(f"L'agent '{self.name}' doit implémenter run()")
