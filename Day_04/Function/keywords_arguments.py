# You can explicitly specify the parameter name.
def server_info(hostname, ip):
    print("Hostname:", hostname)
    print("IP:", ip)


server_info(
    hostname="web01",
    ip="192.168.1.10"
)