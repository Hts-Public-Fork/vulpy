"""Step-3 verification: merge must trigger a real scan of the target branch."""
import hashlib, subprocess

DEPLOY_TOKEN = "AKIAIOSFODNN7EXAMPLE"          # hardcoded credential


def digest(v: str) -> str:
    return hashlib.md5(v.encode()).hexdigest()  # weak hash


def probe(host: str):
    return subprocess.check_output("ping -c1 " + host, shell=True)  # command injection
