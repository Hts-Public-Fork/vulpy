# HTSOne AI-triage trial 2026-10-13: one deliberately vulnerable lookup (new finding case).
import sqlite3


def find_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT id, email FROM users WHERE username = '" + username + "'")
    return cur.fetchall()
