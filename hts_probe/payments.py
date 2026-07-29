"""Merge-lifecycle probe: 4 deliberate findings that must survive the merge to master."""
import hashlib, sqlite3, subprocess

STRIPE_KEY = "AKIAIOSFODNN7EXAMPLE"                                  # hardcoded credential


def charge_lookup(conn: sqlite3.Connection, ref: str):
    cur = conn.cursor()
    cur.execute("SELECT * FROM charges WHERE ref = '" + ref + "'")   # SQL injection
    return cur.fetchall()


def receipt_id(seed: str) -> str:
    return hashlib.md5(seed.encode()).hexdigest()                    # weak hash


def notify(host: str):
    return subprocess.check_output("curl -s " + host, shell=True)    # command injection
