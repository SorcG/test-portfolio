import pytest
from bot.conversation import ConversationStore


def test_add_and_retrieve():
    store = ConversationStore()
    store.add_message(42, "user", "Hello")
    history = store.get_history(42)
    assert len(history) == 1
    assert history[0] == {"role": "user", "content": "Hello"}


def test_reset_clears_history():
    store = ConversationStore()
    store.add_message(1, "user", "Hi")
    store.reset(1)
    assert store.get_history(1) == []


def test_history_is_trimmed():
    from bot.config import MAX_HISTORY_MESSAGES
    store = ConversationStore()
    for i in range(MAX_HISTORY_MESSAGES + 5):
        store.add_message(1, "user", f"msg {i}")
    assert len(store.get_history(1)) == MAX_HISTORY_MESSAGES


def test_isolated_per_user():
    store = ConversationStore()
    store.add_message(1, "user", "User 1 message")
    store.add_message(2, "user", "User 2 message")
    assert len(store.get_history(1)) == 1
    assert store.get_history(1)[0]["content"] == "User 1 message"


def test_user_count():
    store = ConversationStore()
    store.add_message(10, "user", "hi")
    store.add_message(20, "user", "hello")
    assert store.user_count() == 2
