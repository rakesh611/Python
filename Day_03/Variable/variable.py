# Python Variables
# In Python, a variable is a name/reference used to store or point to a value.
# Think of a variable like a label attached to data.
# Example:
server_ip = "192.168.22.10"
server_port = 6443
server_count = 3
# Here:
# server_ip → variable
# "192.168.22.10" → string value
# server_port → variable
# 6443 → integer value
# server_count → variable
# 3 → integer value
# Python determines the variable's type automatically.


#  How to Create a Variable
# Python does not require you to declare the datatype.
port = 6443
# Python automatically understands that port is an integer.

# 2. Important Python Variable/Data Types

# 3. String Variable — str
# A string stores text.
# Example:
server_name = "ocp-worker-1"
server_ip = "192.168.22.211"

print(server_name)
print(server_ip)
# Output:
# ocp-worker-1
# 192.168.22.211

# 4. Integer Variable — int
# An integer stores a whole number.
port = 6443
replicas = 3
timeout = 60

print(port)
print(type(port))
# Output: 
# 6443
# <class 'int'>

# 5. Float Variable — float
# A float stores decimal numbers.
cpu_usage = 75.5
memory_usage = 82.3

print(cpu_usage)
print(type(cpu_usage))
# Output:
# 75.5
# <class 'float'>

# 6. Boolean Variable — bool
# Boolean contains only two values:
service_running = True
server_down = False
if service_running:
    print("Service is running")
else:
    print("Service is stopped")

# Output: Service is running
# This is extremely important for automation scripts.

# 7. List Variable — list
# A list stores multiple values.
servers = [
    "ocp-master-1",
    "ocp-master-2",
    "ocp-master-3"
]

print(servers)
# Output: ['ocp-master-1', 'ocp-master-2', 'ocp-master-3']

# 8. Tuple Variable — tuple
# A tuple is similar to a list, but normally used for fixed/immutable data.
cluster_nodes = (
    "master",
    "worker",
    "infra"
)

print(cluster_nodes)
# Output: ('master', 'worker', 'infra')

# 9. Dictionary Variable — dict
# A dictionary stores data as:
server = {
    "hostname": "ocp-worker-1",
    "ip": "192.168.22.211",
    "role": "worker",
    "status": "Running"
}
# Access values:
print(server["hostname"])
print(server["ip"])
print(server["status"])
# Output:
# ocp-worker-1
# 192.168.22.211
# Running

# 10. Set Variable — set
# A set stores unique values.
# Example:
servers = {
    "web01",
    "web02",
    "web01",
    "web03"
}

print(servers)
# Output: {'web02', 'web03', 'web01'}

# 11. None Variable
# None means there is currently no value
# Example:
pod_ip = None

if pod_ip is None:
    print("Pod IP is not assigned")

# Output: Pod IP is not assigned

# 12. Checking Variable Type
# Use type().
hostname = "ocp-worker-1"
port = 6443
cpu = 75.5
running = True
servers = ["web01", "web02"]

print(type(hostname))
print(type(port))
print(type(cpu))
print(type(running))
print(type(servers))

# Output: 
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'list'>


# 13. Multiple Variables
# Python allows multiple assignments.
server1, server2, server3 = "web01", "web02", "web03"

print(server1)
print(server2)
print(server3)
# You can also assign the same value:
server1 = server2 = server3 = "Running"
print(server1)
# Output:
# web01
# web02
# web03
# Running

# 14. Variable Reassignment
# A variable can point to a different value.
status = "Running"

print(status)

status = "Stopped"

print(status)
# Output:
# Running
# Stopped

# 17. Local Variable
# A variable created inside a function is generally local to that function.
def check_server():
    server_name = "ocp-worker-1"
    print(server_name)

check_server()
# server_name belongs to that function's local scope.

# 18. Global Variable
# A variable created outside functions can be accessed from functions.
server_name = "ocp-worker-1"

def check_server():
    print(server_name)

check_server()
# For automation, avoid excessive global variables because they can make large scripts difficult to maintai