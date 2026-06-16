# tests/test_graphify_runner.py
import graphify_runner as gr

LLM_KEYS = ["GEMINI_API_KEY", "GOOGLE_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "OLLAMA_HOST"]


def test_offline_env_strips_all_llm_keys():
    base = {k: "secret" for k in LLM_KEYS} | {"PATH": "/usr/bin"}
    env = gr.offline_env(base)
    for k in LLM_KEYS:
        assert k not in env
    assert env["PATH"] == "/usr/bin"


def test_gemini_env_keeps_key():
    base = {"GEMINI_API_KEY": "secret", "PATH": "/usr/bin"}
    env = gr.gemini_env(base)
    assert env["GEMINI_API_KEY"] == "secret"
