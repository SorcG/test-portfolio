import anthropic
from bot.config import ANTHROPIC_API_KEY, CLAUDE_MODEL, SYSTEM_PROMPT
from bot.conversation import Message

_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def get_reply(history: list[Message]) -> str:
    """Send conversation history to Claude and return the assistant's reply."""
    response = _client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=history,
    )
    return response.content[0].text
