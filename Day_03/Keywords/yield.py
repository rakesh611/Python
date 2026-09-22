# yield
# Used to create a generator.
# Instead of returning everything at once, yield produces values one at a time.
def servers():
    yield "web01"
    yield "web02"
    yield "db01"

for server in servers():
    print(server)

# This is useful when processing large datasets or logs without loading everything into memory.

# Example
def read_logs(file):

    with open(file) as f:
        for line in f:
            yield line.strip()

for line in read_logs("/var/log/messages"):
    if "ERROR" in line:
        print(line)