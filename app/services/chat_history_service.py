import sqlite3
from pathlib import Path

from langchain_core.messages import HumanMessage, AIMessage


DB_PATH = Path("data/chat_history.db")


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    return sqlite3.connect(DB_PATH)


def initialize_database():

    with get_connection() as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """)


def save_message(session_id, role, content):

    with get_connection() as conn:

        conn.execute("""
            INSERT INTO chat_history
            (session_id, role, content)
            VALUES (?, ?, ?)
        """, (session_id, role, content))


def load_chat_history(session_id):

    with get_connection() as conn:

        rows = conn.execute("""
            SELECT role, content
            FROM chat_history
            WHERE session_id = ?
            ORDER BY id
        """, (session_id,)).fetchall()

    messages = []

    for role, content in rows:

        if role == "human":
            messages.append(HumanMessage(content=content))

        elif role == "ai":
            messages.append(AIMessage(content=content))

    return messages