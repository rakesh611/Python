# continue
# Skips the current iteration and moves to the next one.
servers = ["web01", "db01", "web02"]

for server in servers:

    if server == "db01":
        continue

    print("Checking:", server)

# Output:
# Checking: web01
# Checking: web02
# Useful when you want to skip certain servers.