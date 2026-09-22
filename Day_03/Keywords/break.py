# break
# Immediately exits a loop.
servers = ["web01", "web02", "db01"]

for server in servers:
    if server == "db01":
        break

    print(server)

# Output: 
# web01
# web02