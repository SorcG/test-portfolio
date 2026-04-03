# Claude → Notion Generator

A Streamlit web app that generates structured content using the Anthropic Claude API and saves it directly as a formatted Notion page — with one click.

## Features

- Generate **Blog Articles**, **Project Plans**, and **Research Summaries** via Claude AI
- Live preview of generated content before saving
- One-click export to a formatted Notion page
- Clean, minimal web interface

## Tech Stack

| Component    | Library          |
|--------------|------------------|
| Web UI       | Streamlit        |
| AI Backend   | Anthropic Claude |
| Notion API   | notion-client    |
| Config       | python-dotenv    |

## Project Structure

```
notion-generator/
├── app.py              # Streamlit UI and orchestration
├── claude_client.py    # Claude content generation
├── notion_wrapper.py   # Notion API: Markdown → page blocks
└── prompts.py          # Prompt templates per content type
```

## Getting Started

### Prerequisites
- Python 3.11+
- An [Anthropic API Key](https://console.anthropic.com/)
- A Notion account with an Integration Token

### Notion Setup

1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click **New integration** → give it a name → copy the **Internal Integration Token**
3. Open a Notion page where generated content should be saved
4. Click **Share** (top right) → find your integration → click **Invite**
5. Copy the page ID from the URL: `notion.so/<page-id>?v=...`

### Installation

```bash
cd notion-generator
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Fill in your three keys in .env
```

### Running

```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

## How It Works

1. Enter a topic and select a content type
2. Claude generates structured Markdown content using a tailored prompt
3. The app previews the result
4. Click **Save to Notion** — the Markdown is parsed into Notion block objects and a new page is created under your chosen parent page

## License

MIT
