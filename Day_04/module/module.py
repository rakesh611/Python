# A module in Python is a .py file that contains reusable Python code such as:
# Variables
# Functions
# Classes
# Constants
# Logic

# The main purpose of a module is code reusability.

# As a DevOps engineer, you can think of a Python module like a reusable automation component. Instead of writing the same code in every script, you write it once in a module and import it wherever required.

# Simple definition
# Module = A Python .py file containing reusable code that can be imported into another Python program.

# For example:
# devops/
# ├── server.py
# └── main.py
# If server.py contains functions for checking servers, main.py can import and use those functions.

# Put the reusable function inside server_utils.py.
# server_utils.py

import subprocess

def check_server(ip):
    result = subprocess.run(
        ["ping", "-c", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        return True
    else:
        return False
# Now other scripts can reuse it.
# monitor.py

from server_utils import check_server

ip = "192.168.1.10"

if check_server(ip):
    print(f"{ip} is UP")
else:
    print(f"{ip} is DOWN")