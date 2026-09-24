# Arithmetic Operators
# Arithmetic operators perform mathematical calculations.
# +     Addition
# -     Subtraction
# *     Multiplication
# /     Division
# //    Floor division
# %     Modulus
# **    Power

# + Addition
# Adds two values.
# Suppose you have CPU usage from two processes:
nginx_cpu = 35
docker_cpu = 25

total_cpu = nginx_cpu + docker_cpu

print("Total CPU:", total_cpu)
# Output: Total CPU: 60

# + can also concatenate strings:
server = "ocp"
node = "-worker1"

name = server + node

print(name)
# Output: ocp-worker1

################################

# - Subtraction
# Subtracts one value from another.
total_memory = 32
used_memory = 20

free_memory = total_memory - used_memory

print("Free memory:", free_memory, "GB")
# Output: Free memory: 12 GB

####################################

# * Multiplication
# Multiplies values.
workers = 5
cpu_per_worker = 8

total_cpu = workers * cpu_per_worker

print("Total CPU:", total_cpu)
# Output: Total CPU: 40

#######################################

# / Division
# Performs normal division.
used_disk = 750
total_disk = 1000

disk_usage = (used_disk / total_disk) * 100

print("Disk Usage:", disk_usage, "%")
# output: Disk Usage: 75.0 %

#####################################
# // Floor Division
# Returns the integer part of division.
# Suppose you have 100 pods and want to distribute them across 6 nodes:
pods = 100
nodes = 6

pods_per_node = pods // nodes

print(pods_per_node)
# Output: 16

#######################################3

# % Modulus
# Returns the remainder.
# Check whether a number is even:
pod_number = 10

if pod_number % 2 == 0:
    print("Even pod number")
else:
    print("Odd pod number")
# Output: Even pod number

######################################

# ** Exponentiation
# Raises a number to a power.
base = 2
power = 10

result = base ** power

print(result)
# Output: 1024