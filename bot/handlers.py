import asyncio
import logging

import anthropic
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from bot.claude_client import get_reply
from bot.conversation import ConversationStore

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}! I'm your Claude-powered AI assistant.\n\n"
        "Just send me any message and I'll respond using Claude AI.\n"
        "Type /help to see what I can do."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "<b>Available Commands</b>\n\n"
        "/start — Welcome message\n"
        "/help  — Show this help\n"
        "/reset — Clear your conversation history\n\n"
        "Simply type any message to chat with Claude AI.\n"
        "I remember your conversation context within a session."
    )
    await update.message.reply_html(help_text)


async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    store: ConversationStore = context.bot_data["store"]
    store.reset(update.effective_user.id)
    await update.message.reply_text(
        "Your conversation history has been cleared. Fresh start!"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    store: ConversationStore = context.bot_data["store"]
    user_id = update.effective_user.id
    user_text = update.message.text

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )

    store.add_message(user_id, "user", user_text)

    try:
        reply = await asyncio.to_thread(get_reply, store.get_history(user_id))
        store.add_message(user_id, "assistant", reply)
        await update.message.reply_text(reply)

    except anthropic.RateLimitError:
        logger.warning("Rate limit hit for user %s", user_id)
        await update.message.reply_text(
            "I'm being rate-limited right now. Please try again in a moment."
        )
    except anthropic.APIStatusError as e:
        logger.error("Anthropic API error for user %s: %s", user_id, e)
        await update.message.reply_text(
            "I encountered an error talking to Claude. Please try again."
        )
    except Exception as e:
        logger.exception("Unexpected error for user %s: %s", user_id, e)
        await update.message.reply_text(
            "Something unexpected went wrong. Please try again later."
        )
