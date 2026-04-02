# Claude AI Telegram Bot

A conversational Telegram bot powered by the Anthropic Claude API, built with Python's async ecosystem. Maintains per-user conversation context and handles errors gracefully.

## Features

- Context-aware conversations using Claude Haiku
- Per-user conversation history with automatic trimming
- Typing indicator while Claude generates a response
- `/start`, `/help`, `/reset` commands
- Structured error handling for API failures and rate limits
- Clean async architecture with python-telegram-bot v21

## Tech Stack

| Component      | Library                  |
|----------------|--------------------------|
| Telegram Layer | python-telegram-bot v21  |
| AI Backend     | anthropic SDK            |
| Config         | python-dotenv            |

## Project Structure

```
bot/
├── main.py            # Entry point, wires handlers to Application
├── config.py          # Env var loading with fail-fast validation
├── claude_client.py   # Thin Anthropic SDK wrapper
├── conversation.py    # In-memory per-user history store
└── handlers.py        # Command and message handlers
```

## Getting Started

### Prerequisites
- Python 3.11+
- A Telegram Bot Token (get one from [@BotFather](https://t.me/BotFather))
- An [Anthropic API Key](https://console.anthropic.com/)

### Installation

```bash
git clone <repo-url>
cd test-portfolio
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and fill in your credentials
```

### Running

```bash
python -m bot.main
```

### Tests

```bash
pytest tests/
```

## Getting a Telegram Bot Token

1. Open Telegram and search for `@BotFather`
2. Send `/newbot`
3. Follow the prompts to choose a name and username
4. Copy the token into your `.env` file as `TELEGRAM_BOT_TOKEN=...`

## Architecture Notes

The Anthropic SDK is synchronous. To avoid blocking the async Telegram event loop, all Claude API calls are dispatched via `asyncio.to_thread()`. Conversation history is stored as a plain in-memory dict keyed by Telegram user ID — simple and fast without requiring a database. For a production deployment, this would be replaced with Redis or SQLite.

## License

MIT
