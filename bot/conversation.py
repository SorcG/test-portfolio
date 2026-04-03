from collections import defaultdict
from bot.config import MAX_HISTORY_MESSAGES

# Anthropic messages format: {"role": "user"|"assistant", "content": str}
Message = dict[str, str]


class ConversationStore:
    """In-memory store for per-user conversation histories."""

    def __init__(self) -> None:
        self._histories: dict[int, list[Message]] = defaultdict(list)

    def add_message(self, user_id: int, role: str, content: str) -> None:
        history = self._histories[user_id]
        history.append({"role": role, "content": content})
        if len(history) > MAX_HISTORY_MESSAGES:
            self._histories[user_id] = history[-MAX_HISTORY_MESSAGES:]

    def get_history(self, user_id: int) -> list[Message]:
        return list(self._histories[user_id])

    def reset(self, user_id: int) -> None:
        self._histories[user_id] = []

    def user_count(self) -> int:
        return len(self._histories)
