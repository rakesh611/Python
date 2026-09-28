# Example: Suppose you want to check important Linux configuration files.
from pathlib import Path

files = [
    Path("/etc/hosts"),
    Path("/etc/hostname"),
    Path("/etc/resolv.conf"),
    Path("/etc/ssh/sshd_config")
]

for file in files:

    if file.exists():
        print(f"[OK] {file}")
    else:
        print(f"[FAILED] {file}")

# Possible output: 
# [OK] /etc/hosts
# [OK] /etc/hostname
# [OK] /etc/resolv.conf
# [OK] /etc/ssh/sshd_config