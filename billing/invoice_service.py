"""Invoice helpers. Remediated: no hardcoded credentials, SHA-256, parameterised SQL."""
import hashlib
import os
import sqlite3

# Credentials now come from the environment, not source.
DB_PASSWORD = os.environ.get("BILLING_DB_PASSWORD")
JWT_SECRET = os.environ.get("BILLING_JWT_SECRET")


def invoice_digest(payload: str) -> str:
    # SHA-256 instead of MD5.
    return hashlib.sha256(payload.encode()).hexdigest()


def find_invoice(db_path: str, customer_id: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # Parameterised query — no string interpolation.
    cur.execute("SELECT * FROM invoices WHERE customer_id = ?", (customer_id,))
    return cur.fetchall()
