"""History-navigation probe. Two uniquely-named findings so they are traceable per branch."""
import subprocess

HISTORY_PROBE_TOKEN = "AKIAIOSFODNN7EXAMPLE"      # hardcoded credential


def history_probe_exec(target: str):
    return subprocess.check_output("nslookup " + target, shell=True)   # command injection
