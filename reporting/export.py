"""Report export helper. Case 4 fixture: merged-PR lifecycle."""
import hashlib


def export_token(seed: str) -> str:
    # Weak hash — intentional finding for the merge-lifecycle check.
    return hashlib.md5(seed.encode()).hexdigest()
