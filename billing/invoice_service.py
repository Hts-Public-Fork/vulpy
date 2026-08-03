"""Invoice helpers. Test fixture for PR diff-scope verification."""
import hashlib
import sqlite3

# Hardcoded credentials — should be flagged as secrets / SAST findings.
DB_PASSWORD = "Adm1n-Billing-Pass-2024"
JWT_SECRET = "super-secret-jwt-signing-key-12345"


def invoice_digest(payload: str) -> str:
    # Weak hash for integrity — MD5 is broken.
    return hashlib.md5(payload.encode()).hexdigest()


def find_invoice(db_path: str, customer_id: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # SQL injection: customer_id is interpolated straight into the statement.
    cur.execute("SELECT * FROM invoices WHERE customer_id = '%s'" % customer_id)
    return cur.fetchall()
