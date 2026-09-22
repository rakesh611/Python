# What is a Tuple in Python?
# A tuple is a collection of multiple values stored together in a single variable.
# The main difference from a list is:
# Tuple is immutable — after creating it, you cannot change, add, or remove its elements.
#Example:
servers = ("web01", "web02", "db01")
print(servers)
# output: ('web01', 'web02', 'db01')
# A tuple normally uses parentheses ().
# List vs Tuple
# List
# servers_list = ["web01", "web02", "db01"]
# Tuple
# servers_tuple = ("web01", "web02", "db01")
##########| Feature          | List  | Tuple |
########## | ---------------- | ----- | ----- |
########## | Syntax           | `[]`  | `()`  |
########## | Mutable          | ✅ Yes | ❌ No  |
########## | Add item         | ✅     | ❌     |
########## | Remove item      | ✅     | ❌     |
########## | Change item      | ✅     | ❌     |
########## | Indexing         | ✅     | ✅     |
########## | Duplicate values | ✅     | ✅     |
########## | Ordered          | ✅     | ✅     |

#List can be changed
servers = ["web01", "web02"]
servers[0] = "db01"
print(servers)
# output: ['db01', 'web02']
#Tuple cannot be changed
servers = ("web01", "web02")
# servers[0] = "db01"  # This will raise a TypeError

# 1. Creating a Tuple
servers = ("web01", "web02", "db01")
# we can store different data types:
data = ("Rakesh", 10, 10.5, True)
print(data)

# Single-element Tuple
# This is an important Python concept.
# This is NOT a tuple:
single_element = ("web01")
print(type(single_element))  # output: <class 'str'>

# This is a tuple:
single_element = ("web01",)
print(type(single_element))  # output: <class 'tuple'>
# For a one-element tuple, you need a comma:The comma makes it a tuple.

# 2. Access Tuple Elements
# Tuples support indexing just like lists.
servers = ("web01", "web02", "db01")

print(servers[0])
print(servers[1])
print(servers[2])
# output:
# web01
# web02
# db01

# Negative indexing also works:
print(servers[-1])  # output: db01

# 3. Tuple Slicing
# You can slice tuples just like lists.
servers = ("web01", "web02", "db01", "app01", "app02")
print(servers[1:4])  # output: ('web02', 'db01', 'app01')
print(servers[:3])   # output: ('web01', 'web02', 'db01')
print(servers[2:])   # output: ('db01', 'app01', 'app02')
print(servers[-3:-1])  # output: ('db01', 'app01')

# 4. Tuple Methods
# Tuples have only two built-in methods: count() and index().
servers = ("web01", "web02", "db01", "web01")
# count()
print(servers.count("web01"))  # output: 2
# index()
print(servers.index("db01"))  # output: 2

# 4. len()
# Returns the number of elements
servers = ("web01", "web02", "db01")

print(len(servers))
# output: 3

# 5. max() and min()
# For numbers:
numbers = (10, 5, 8, 20)
print(max(numbers))  # output: 20
print(min(numbers))  # output: 5

# For strings, Python compares them lexicographically:
servers = ("web01", "web02", "db01")

print(max(servers))
print(min(servers))
# output:
# web02
# db01

# 6. sum()
# Works with numeric tuples:
numbers = (10, 5, 8, 20)
print(sum(numbers))  # output: 43

# 7. sorted()
# Returns a sorted list of the tuple's elements.
servers = ("web01", "web02", "db01")
sorted_servers = sorted(servers)
print(sorted_servers)  # output: ['db01', 'web01', 'web02']
# Important
# sorted() returns a list, not a tuple.
# <class 'list'>
# If you want a tuple again:
result = tuple(sorted(servers))

print(result)
# 8. tuple()
# Converts another iterable into a tuple.
# List → Tuple
servers_list = ["web01", "web02", "db01"]

servers_tuple = tuple(servers_list)

print(servers_tuple)
# output: ('web01', 'web02', 'db01')
# String → Tuple
text = "Linux"

print(tuple(text))
# output: ('L', 'i', 'n', 'u', 'x')

# 11. in operator
# You can check whether an item exists:
servers = ("web01", "web02", "db01")
print("web01" in servers)  # output: True
print("app01" in servers)  # output: False

# 12. Loop through a Tuple
servers = ("web01", "web02", "db01")
for server in servers:
    print(server)
# output:
# web01
# web02
# db01

# 13. Tuple Unpacking
# You can unpack a tuple into variables:
servers = ("web01", "web02", "db01")
server1, server2, server3 = servers
print(server1)  # output: web01
print(server2)  # output: web02
print(server3)  # output: db01

# 2nd Example
server = ("web01", "192.168.22.11", 8080)

name, ip, port = server

print(name)
print(ip)
print(port)
# output:
# web01
# 192.168.22.11
# 8080

# 14. Nested Tuples
# Tuples can contain other tuples (or lists, or any other data type):
nested_tuple = (("web01", "192.168.22.11"), ("web02", "192.168.22.12"), ("db01", "192.168.22.13"))
print(nested_tuple)
# output: (('web01', '192.168.22.11'), ('web02', '192.168.22.12'), ('db01', '192.168.22.13'))