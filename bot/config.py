import os
from dotenv import load_dotenv

load_dotenv()


def _require(key: str) -> str:
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Missing required environment variable: {key}")
    return value


TELEGRAM_BOT_TOKEN: str = _require("TELEGRAM_BOT_TOKEN")
ANTHROPIC_API_KEY: str = _require("ANTHROPIC_API_KEY")

CLAUDE_MODEL: str = "claude-haiku-4-5-20251001"
MAX_HISTORY_MESSAGES: int = 20
SYSTEM_PROMPT: str = (
    "You are a helpful, friendly AI assistant. "
    "Keep responses concise and conversational. "
    "You are running inside a Telegram bot."
)
