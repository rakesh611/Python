# *args allows a function to accept multiple positional arguments.
def check_servers(*servers):
    for server in servers:
        print("Checking:", server)


check_servers(
    "web01",
    "web02",
    "db01",
    "db02"
)
# This can be useful when the number of servers is not fixed.