# lambda
# Creates a small anonymous function.
# Example:
square = lambda x: x * x

print(square(5))
# Output: 25

servers = [
    {"name": "web01", "cpu": 80},
    {"name": "web02", "cpu": 50},
    {"name": "db01", "cpu": 90}
]

servers.sort(key=lambda server: server["cpu"])

print(servers)

# Very useful when processing infrastructure data.