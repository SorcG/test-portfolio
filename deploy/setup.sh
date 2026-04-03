#!/bin/bash
set -e

REPO_DIR="/root/test-portfolio"
BRANCH="claude/first-portfolio-project-CTvTE"
SERVICE="claude-bot"

echo "=== Claude Bot Setup ==="

# 1. System packages
apt-get update -y
apt-get install -y python3 python3-pip python3-venv git curl

# 2. Clone or update repo
if [ -d "$REPO_DIR/.git" ]; then
    echo "Repo already exists, pulling latest..."
    git -C "$REPO_DIR" fetch origin
    git -C "$REPO_DIR" checkout "$BRANCH"
    git -C "$REPO_DIR" pull origin "$BRANCH"
else
    git clone https://github.com/SorcG/test-portfolio.git "$REPO_DIR"
    git -C "$REPO_DIR" checkout "$BRANCH"
fi

# 3. Python virtual environment
python3 -m venv "$REPO_DIR/.venv"
"$REPO_DIR/.venv/bin/pip" install --upgrade pip
"$REPO_DIR/.venv/bin/pip" install -r "$REPO_DIR/requirements.txt"

# 4. Install and enable systemd service
cp "$REPO_DIR/deploy/claude-bot.service" /etc/systemd/system/${SERVICE}.service
systemctl daemon-reload
systemctl enable "$SERVICE"

echo ""
echo "=== Setup complete! ==="
echo ""
echo "Next: create your .env file with your API keys:"
echo ""
echo "  nano $REPO_DIR/.env"
echo ""
echo "Paste the following and fill in your keys:"
echo "  TELEGRAM_BOT_TOKEN=your_token_here"
echo "  ANTHROPIC_API_KEY=your_key_here"
echo ""
echo "Then start the bot:"
echo "  systemctl start $SERVICE"
echo "  systemctl status $SERVICE"
echo ""
echo "Useful commands:"
echo "  journalctl -u $SERVICE -f     # live logs"
echo "  systemctl restart $SERVICE    # restart after code updates"
echo "  systemctl stop $SERVICE       # stop the bot"
