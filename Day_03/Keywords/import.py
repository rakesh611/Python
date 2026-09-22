# import
# Imports a Python module.
# Very important for DevOps scripting.
import os
print(os.getcwd())
# Output: current pwd

import subprocess

result = subprocess.run(
    ["systemctl", "is-active", "sshd"],
    capture_output=True,
    text=True
)

print(result.stdout)