from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
for name in ("README.md", "LICENSE", "SECURITY.md", "TESTING.md"):
    assert (root / name).is_file(), name
patterns = [r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
            r"gh[pousr]_[A-Za-z0-9]{30,}", r"AIza[A-Za-z0-9_-]{35}"]
for path in root.rglob("*"):
    if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
        continue
    assert path.suffix.lower() not in (".pfx", ".p12", ".key", ".pem", ".log"), path
    text = path.read_text(encoding="utf-8")
    assert not any(re.search(p, text) for p in patterns), path
    if path.suffix == ".sh":
        subprocess.run(["bash", "-n", str(path)], check=True)
print("Repository structure, heuristic secret scan, and Bash syntax passed.")
