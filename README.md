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

### Running (local)

```bash
python -m bot.main
```

### Deployment on a VPS (Ubuntu 24.04)

To run the bot permanently on a server (auto-start on boot, auto-restart on crash):

**1. Connect to your server via SSH**
```bash
ssh root@<your-server-ip>
```

**2. Run the setup script**
```bash
bash <(curl -s https://raw.githubusercontent.com/SorcG/test-portfolio/claude/first-portfolio-project-CTvTE/deploy/setup.sh)
```

**3. Create your `.env` file on the server**
```bash
nano /root/test-portfolio/.env
# Add your keys, save with Ctrl+X → Y → Enter
```

**4. Start the bot**
```bash
systemctl start claude-bot
systemctl status claude-bot
```

**Useful management commands:**
```bash
journalctl -u claude-bot -f     # Live logs
systemctl restart claude-bot    # Restart after code updates
systemctl stop claude-bot       # Stop the bot
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
