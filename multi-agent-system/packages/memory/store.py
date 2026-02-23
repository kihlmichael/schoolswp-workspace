import json
import os
from datetime import datetime
from pathlib import Path

import aiosqlite

DB_PATH = Path(os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./data/memory.db").replace(
    "sqlite+aiosqlite:///", ""
))


async def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS runs (
                id TEXT PRIMARY KEY,
                task TEXT NOT NULL,
                status TEXT DEFAULT 'running',
                result TEXT,
                created_at TEXT,
                completed_at TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS decisions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                agent TEXT NOT NULL,
                decision TEXT NOT NULL,
                reasoning TEXT,
                confidence REAL DEFAULT 0.5,
                created_at TEXT,
                FOREIGN KEY (run_id) REFERENCES runs(id)
            )
        """)
        await db.execute("""
            CREATE INDEX IF NOT EXISTS idx_decisions_agent
            ON decisions(agent, created_at DESC)
        """)
        await db.commit()


async def save_run(run_id: str, task: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO runs (id, task, status, created_at) VALUES (?, ?, ?, ?)",
            (run_id, task, "running", datetime.utcnow().isoformat()),
        )
        await db.commit()


async def save_decision(
    run_id: str, agent: str, decision: str, reasoning: str, confidence: float
):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """INSERT INTO decisions (run_id, agent, decision, reasoning, confidence, created_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (run_id, agent, decision, reasoning, confidence, datetime.utcnow().isoformat()),
        )
        await db.commit()


async def get_recent_decisions(agent: str, limit: int = 5) -> list[dict]:
    """Récupère les N dernières décisions d'un agent (pour context injection)."""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            """SELECT decision, reasoning, confidence, created_at
               FROM decisions WHERE agent = ?
               ORDER BY created_at DESC LIMIT ?""",
            (agent, limit),
        ) as cursor:
            rows = await cursor.fetchall()
    return [
        {"decision": r[0], "reasoning": r[1], "confidence": r[2], "created_at": r[3]}
        for r in rows
    ]


async def complete_run(run_id: str, result: dict):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE runs SET status = 'done', result = ?, completed_at = ? WHERE id = ?",
            (json.dumps(result, ensure_ascii=False), datetime.utcnow().isoformat(), run_id),
        )
        await db.commit()
