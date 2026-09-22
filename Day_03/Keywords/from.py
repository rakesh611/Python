# from
# Imports something specific from a module.
from os import path
if path.exists("/etc/passwd"):
    print("File exists")
else:
    print("File not exists")

########
from datetime import datetime

print(datetime.now())