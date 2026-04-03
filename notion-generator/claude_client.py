import os
from dotenv import load_dotenv
import anthropic
from prompts import get_prompt

load_dotenv()

_client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
MODEL = "claude-haiku-4-5-20251001"


def generate_content(topic: str, content_type: str) -> str:
    """Generate structured Markdown content using Claude."""
    prompt = get_prompt(topic, content_type)
    response = _client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text
