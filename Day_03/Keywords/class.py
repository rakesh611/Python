# class
# Defines a class.
# Classes are used in object-oriented programming.
class Server:

    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

server = Server("web01", "192.168.1.10")

print(server.hostname)
print(server.ip)