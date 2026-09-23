# Python Function
# A function in Python is a reusable block of code that performs a specific task.
# Instead of writing the same code again and again, we put it inside a function and call the function whenever we need it.

# Simple definition
# def function_name():
#     # code
# Example:
def hello():
    print("Hello DevOps Engineer")

hello()

# Here:
# def → keyword used to create a function
# hello → function name
# () → parameters go here
# : → starts the function body
# indented code → function body
# hello() → calls the function

# 2. Basic Function
def check_server():
    print("Checking server...")
    print("Server is UP")

check_server()

# 3. Function with a Parameter
# A parameter allows us to pass data into a function.
# Example:
def check_server(server):
    print("Checking server:", server)

check_server("server01")
check_server("server02")
check_server("server03")
# Output:
# Checking server: server01
# Checking server: server02
# Checking server: server03
# Here: server is the parameter
# And:"server01" is the argument

# 4. Multiple Parameters
# A function can accept multiple parameters.
def server_info(server, ip, environment):
    print("Server:", server)
    print("IP:", ip)
    print("Environment:", environment)

server_info("web01", "192.168.1.10", "production")
# Another call:
server_info("web02", "192.168.1.11", "development")
# Output:
# Server: web01
# IP: 192.168.1.10
# Environment: production

# 5. Function with return
# This is very important for DevOps automation.
# return sends a value back from the function.

# Example:
def check_disk():
    usage = 75
    return usage

disk_usage = check_disk()

print("Disk usage:", disk_usage, "%")
# Output: Disk usage: 75 %

# 6. print() vs return
# Using print()
def check_disk():
    print(80)

check_disk()
# The function displays:
# Output: 80
# But it doesn't give the value back for further processing.

# Using return
def check_disk():
    return 80

usage = check_disk()

if usage > 80:
    print("Disk is almost full")

# Now the returned value can be used by another part of the program.
# For DevOps automation, return is usually more useful than simply printing the result.