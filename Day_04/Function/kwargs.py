# **kwargs allows multiple keyword arguments.
def server_info(**details):
    for key, value in details.items():
        print(key, ":", value)


server_info(
    hostname="web01",
    ip="192.168.1.10",
    environment="production",
    os="RHEL"
)
