import os
import re
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

_notion = Client(auth=os.environ["NOTION_TOKEN"])
PARENT_PAGE_ID = os.environ["NOTION_PARENT_PAGE_ID"]


def markdown_to_blocks(markdown: str) -> tuple[str, list]:
    """Parse Markdown into a page title and list of Notion block objects."""
    lines = markdown.strip().split("\n")
    title = "Untitled"
    blocks = []

    for line in lines:
        line = line.rstrip()

        if not line:
            continue

        if line.startswith("# "):
            title = line[2:].strip()

        elif line.startswith("## "):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": line[3:].strip()}}]
                },
            })

        elif line.startswith("### "):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": line[4:].strip()}}]
                },
            })

        elif re.match(r"^[-*] ", line):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:].strip()}}]
                },
            })

        else:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": line}}]
                },
            })

    return title, blocks


def create_page(markdown: str) -> str:
    """Create a Notion page from Markdown content. Returns the page URL."""
    title, blocks = markdown_to_blocks(markdown)

    # Notion API limit: max 100 blocks per request
    response = _notion.pages.create(
        parent={"page_id": PARENT_PAGE_ID},
        properties={
            "title": [{"type": "text", "text": {"content": title}}]
        },
        children=blocks[:100],
    )

    page_id = response["id"]
    return f"https://notion.so/{page_id.replace('-', '')}"
