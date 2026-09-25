# A loop in Python is used to execute the same block of code repeatedly.
# Python mainly provides two types of loops:
# for loop
# while loop
# There are also important loop-control statements:
# break
# continue
# pass
# else with loops
#############################################

# for Loop
# A for loop is used when you want to iterate over a sequence or collection of items.
# Basic syntax
# for variable in sequence:
#     # code to execute
servers = ["web01", "web02", "db01"]

for server in servers:
    print(server)
# Output: 
# web01
# web02
# db01

#####################################################

# for Loop with Numbers
# You can use range() to execute a loop a specific number of times.
for i in range(5):
    print(i)
# output: 0 1 2 3 4 

########################################################

# for Loop with IP Addresses
# This is more realistic for DevOps automation.
ips = [
    "192.168.22.211",
    "192.168.22.212",
    "192.168.22.213"
]

for ip in ips:
    print(f"Checking server: {ip}")
# Output:
# Checking server: 192.168.22.211
# Checking server: 192.168.22.212
# Checking server: 192.168.22.213

#####################################################

# for Loop with Dictionary
# DevOps scripts frequently work with dictionaries containing configuration.
server = {
    "hostname": "web01",
    "ip": "192.168.22.211",
    "environment": "production"
}

for key, value in server.items():
    print(key, "=", value)
# Output:
# hostname = web01
# ip = 192.168.22.211
# environment = production

# Why .items()?
# .items() gives both:
# key value

#################################################

# Nested for Loop
# A loop inside another loop is called a nested loop.
environments = ["dev", "stage", "prod"]
services = ["nginx", "redis", "postgres"]

for env in environments:
    for service in services:
        print(f"{env} -> {service}")
# Output:
# dev -> nginx
# dev -> redis
# dev -> postgres

# stage -> nginx
# stage -> redis
# stage -> postgres

# prod -> nginx
# prod -> redis
# prod -> postgres

#####################################################

# while Loop
# A while loop executes code as long as a condition is true.
# Syntax
# while condition:
#     # code
# Example:
count = 1

while count <= 5:
    print(count)
    count += 1
# Output: 1 2 3 4 5 

####################################################

# A while loop is particularly useful for retry logic.
# Suppose a service may take several attempts to become available:
service_ready = False
attempt = 1

while not service_ready and attempt <= 5:

    print(f"Checking service, attempt {attempt}")

    # Imagine health check here
    if attempt == 3:
        service_ready = True

    attempt += 1

if service_ready:
    print("Service is ready")
else:
    print("Service is not ready")

# Output:
# Checking service, attempt 1
# Checking service, attempt 2
# Checking service, attempt 3
# Service is ready

##################################################

# break
# break immediately stops the loop.
# Example:
pods = [
    "nginx-abc",
    "redis-xyz",
    "postgres-123"
]

for pod in pods:

    print(f"Checking {pod}")

    if "postgres" in pod:
        print("PostgreSQL pod found")
        break
# Output:
# Checking nginx-abc
# Checking redis-xyz
# Checking postgres-123
# PostgreSQL pod found

###################################################3
# continue
# continue skips the current iteration and moves to the next iteration.
# Example:
pods = [
    ("nginx", "Running"),
    ("redis", "Pending"),
    ("postgres", "Running")
]

for pod, status in pods:

    if status != "Running":
        continue

    print(f"Processing {pod}")
# Output:
# Processing nginx
# Processing postgres

########################################################
# pass
# pass does nothing.
# It is used when Python requires a statement but you don't want to execute anything yet.
servers = ["web01", "web02"]

for server in servers:

    if server == "web01":
        pass

    print(server)
# Output:
# web01
# web02