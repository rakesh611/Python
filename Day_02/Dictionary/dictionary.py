# Dictionary (dict) in Python
# A dictionary is a Python data structure that stores data as key-value pairs.
# Think of it like:
# Key: Value
# For example:
# "name": "Alice"
# "age": 30
# 2nd example:
server = {
    "name": "web01",
    "ip": "192.168.22.11",
    "port": 8080,
    "status": "running"
}
# You can access the values in a dictionary using their keys:
print(server["name"])  # output: web01
print(server["ip"])    # output: 192.168.22.11
print(server["port"])  # output: 8080
print(server["status"])  # output: running

# 2. get() — safely get a value
# Instead of:
print(server["status"])
# You can use get() to avoid KeyError if the key doesn't exist:
print(server.get("status"))  # output: running
print(server.get("location", "Not Found"))  # output: Not Found
# This is very useful in DevOps scripts, where some JSON/API data may not contain every field.

# 3. Add a new key-value pair
server["location"] = "Data Center 1"
print(server)
# output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080, 'status': 'running', 'location': 'Data Center 1'}

# 4. Modify/update an existing value
server["status"] = "stopped"
print(server)
# output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080, 'status': 'stopped', 'location': 'Data Center 1'}

# 5. Delete a key-value pair
del server["location"]
print(server)
# output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080, 'status': 'stopped'}

# pop()
# Removes a key-value pair and returns the value.
status = server.pop("status")
print(status)  # output: stopped
print(server)  # output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080}

# keys()
# Returns a view of the dictionary's keys.
keys = server.keys()
print(keys)  # output: dict_keys(['name', 'ip', 'port'])

# You can loop through them:
for key in server.keys():
    print(key)
# output:
# name
# ip
# port

# loop through values:
for value in server.values():
    print(value)
# output:
# web01
# 192.168.22.11
# 8080

# items()
# Returns a view of the dictionary's key-value pairs.
items = server.items()
print(items)  # output: dict_items([('name', 'web01'), ('ip', '192.168.22.11'), ('port', 8080)])

# loop through items:
for key, value in server.items():
    print(f"{key}: {value}")
# output:
# name: web01
# ip: 192.168.22.11
# port: 8080

# 7. update()
# Updates the dictionary with key-value pairs from another dictionary or iterable.
server.update({"status": "running", "location": "Data Center 1", "environment": "production"})
print(server)
# output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080, 'status': 'running', 'location': 'Data Center 1', 'environment': 'production'}

# pop()
# Removes a key-value pair and returns the value.
status = server.pop("status")
print(status)  # output: running
print(server)  # output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080, 'location': 'Data Center 1', 'environment': 'production'}

# popitem()
# Removes and returns the last inserted key-value pair as a tuple.
last_item = server.popitem()
print(last_item)  # output: ('environment', 'production')
print(server)  # output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080, 'status': 'running', 'location': 'Data Center 1'}

# clear()
# Removes all items from the dictionary.
server.clear()
print(server)  # output: {}

# copy()
# Returns a shallow copy of the dictionary.
server_copy = server.copy()
print(server_copy)  # output: {}

# setdefault()
# Returns the value of a key if it exists, otherwise inserts the key with a default value.
default_value = server.setdefault("status", "unknown")
print(default_value)  # output: unknown
print(server)  # output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080, 'status': 'unknown'}
# If status already exists:
server["status"] = "running"
print(server)  # output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080, 'status': 'running'}
# it doesn't overwrite the existing value.

# 13. Built-in functions that work with dictionaries
# len() — Returns the number of key-value pairs in the dictionary.
print(len(server))  # output: 4

# type() — Returns the type of the object.
print(type(server))  # output: <class 'dict'>

# dict() — Creates a new dictionary.
new_dict = dict(name="web02", ip="192.168.22.12", port=8080)
print(new_dict)  # output: {'name': 'web02', 'ip': '192.168.22.12', 'port': 8080}

# 14. Check whether a key exists
# use in operator:
print("name" in server)  # output: True
print("location" in server)  # output: False
# Important: in checks keys, not values.

# 15. Dictionary with different data types
# A dictionary can have keys and values of different data types:
mixed_dict = {
    "name": "web01",  # string
    "ip": "192.168.22.11",  # string
    "port": 8080,  # integer
    "is_active": True,  # boolean
    "packages": ["nginx", "curl", "vim"],  # list
    "cpu": 75.5,  # float
}
print(mixed_dict)  # output: {'name': 'web01', 'ip': '192.168.22.11', 'port': 8080, 'is_active': True, 'packages': ['nginx', 'curl', 'vim'], 'cpu': 75.5}
# Access the list:
print(mixed_dict["packages"])  # output: ['nginx', 'curl', 'vim']
# Access an item inside that list:
print(mixed_dict["packages"][0])  # output: nginx

# 16. Nested dictionaries
# A dictionary can contain another dictionary as a value:
nested_dict = {
    "server1": {
        "name": "web01",
        "ip": "192.168.22.11",
        "port": 8080
    },
    "server2": {
        "name": "web02",
        "ip": "192.168.22.12",
        "port": 8080
    }
}
# Accessing nested dictionary values:
# Access server1's IP:
print(nested_dict["server1"]["ip"])  # output: 192.168.22.11
# Access server2's name:
print(nested_dict["server2"]["name"])  # output: web02

# loop through nested dictionaries:
for server_key, server_info in nested_dict.items():
    print(f"{server_key}:")
    for key, value in server_info.items():
        print(f"  {key}: {value}")
# output:
# server1:
#   name: web01
#   ip: 192.168.22.11
#   port: 8080
# server2:
#   name: web02
#   ip: 192.168.22.12
#   port: 8080
