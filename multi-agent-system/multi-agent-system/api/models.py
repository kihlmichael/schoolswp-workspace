from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime


class RunStatus(str, Enum):
    QUEUED = "queued"
    ROUTING = "routing"
    RUNNING = "running"
    SYNTHESIZING = "synthesizing"
    DONE = "done"
    ERROR = "error"


class RunRequest(BaseModel):
    task: str
    callback_url: Optional[str] = None  # n8n webhook URL pour le mode async
    agents: Optional[list[str]] = None  # Force des agents spécifiques
    context: Optional[dict] = {}


class RunResponse(BaseModel):
    run_id: str
    status: RunStatus
    stream_url: str


class AgentOutput(BaseModel):
    domain: str
    confidence: float
    recommendations: list[str]
    warnings: list[str]
    depends_on: list[str] = []
    tool_calls_made: list[str] = []


class SynthesisOutput(BaseModel):
    summary: str
    priority_actions: list[dict]
    conflicts: list[str]
    cross_domain_insights: list[str]
    next_steps: list[str]


class RunResult(BaseModel):
    run_id: str
    status: RunStatus
    task: str
    agent_outputs: dict = {}
    synthesis: dict = {}
    meta: dict = {}
    created_at: Optional[str] = None
    completed_at: Optional[str] = None
