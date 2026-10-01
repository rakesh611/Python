# The Python json module is used to work with JSON (JavaScript Object Notation) data.
# As a DevOps engineer, you will use JSON very frequently for:
# REST API responses
# Kubernetes/OpenShift API data
# AWS/Azure/GCP APIs
# Configuration files
# Ansible output
# Docker metadata
# CI/CD pipelines
# Monitoring data
# Infrastructure automation
# Reading/writing structured configuration

# What is JSON?
# JSON = JavaScript Object Notation
# It is a lightweight format for storing and exchanging structured data.

# Example:
# {
#     "name": "web-server",
#     "ip": "192.168.22.211",
#     "status": "running",
#     "port": 8080
# }

# JSON ↔ Python
# | JSON        | Python          |
# | ----------- | --------------- |
# | object `{}` | `dict`          |
# | array `[]`  | `list`          |
# | string      | `str`           |
# | number      | `int` / `float` |
# | `true`      | `True`          |
# | `false`     | `False`         |
# | `null`      | `None`          |

##################################################################################
# json.dumps()
# Purpose
# json.dumps() converts a Python object into a JSON string.
# Example: 
# Suppose an automation script generates server information:
import json

server = {
    "hostname": "ocp-w-1",
    "ip": "192.168.22.211",
    "role": "worker",
    "status": "Ready"
}

json_data = json.dumps(server)

print(json_data)
# Output: {"hostname": "ocp-w-1", "ip": "192.168.22.211", "role": "worker", "status": "Ready"}
# You can then send this JSON to:
# REST API
# monitoring system
# logging system
# CI/CD system
# another automation script

###########################################################################################################
# json.dumps() with indent
# Without formatting:
import json

server = {
    "hostname": "ocp-w-1",
    "ip": "192.168.22.211",
    "status": "Ready",
    "labels": {
        "workload": "sonarqube"
    }
}

print(json.dumps(server))
# Output: {"hostname": "ocp-w-1", "ip": "192.168.22.211", "status": "Ready", "labels": {"workload": "sonarqube"}}

# For readable output:
print(json.dumps(server, indent=4))

# Output:
# {
#     "hostname": "ocp-w-1",
#     "ip": "192.168.22.211",
#     "status": "Ready",
#     "labels": {
#         "workload": "sonarqube"
#     }
# }
# This is very useful while troubleshooting API responses.

##############################################################################################
# json.dumps() with sort_keys=True
# Suppose:
import json

server = {
    "status": "Ready",
    "hostname": "ocp-w-1",
    "ip": "192.168.22.211"
}

print(json.dumps(server, indent=4, sort_keys=True))
# Output:
{
    "hostname": "ocp-w-1",
    "ip": "192.168.22.211",
    "status": "Ready"
}

# sort_keys=True sorts dictionary keys alphabetically.
# This is useful when:
# comparing JSON output
# debugging configuration
# generating predictable files
# Git version control

#############################################################################################
# json.loads()
# This is the reverse of dumps().
# Example:
import json

data = '{"hostname": "ocp-w-1", "status": "Ready"}'

server = json.loads(data)

print(server)
print(type(server))

# Output: {'hostname': 'ocp-w-1', 'status': 'Ready'}
# <class 'dict'>
# Now you can access individual values:
print(server["hostname"])
print(server["status"])
# Output:
# ocp-w-1
# Ready

######################################################################################################
# DevOps Example — API Response
# This is one of the most important real-world use cases.
# Suppose an OpenShift/Kubernetes API returns:
api_response = '''
{
    "kind": "Pod",
    "metadata": {
        "name": "nginx-abc123"
    },
    "status": {
        "phase": "Running"
    }
}
'''
# Convert it to Python:
import json

data = json.loads(api_response)

pod_name = data["metadata"]["name"]
pod_status = data["status"]["phase"]

print("Pod:", pod_name)
print("Status:", pod_status)
# Output:
# Pod: nginx-abc123
# Status: Running

##########################################################################################################
# json.dump()
# Now we have an important difference:
# dumps()
# Python → JSON string
# dump()
# Python → JSON file
# Example:
import json

server = {
    "hostname": "ocp-w-1",
    "ip": "192.168.22.211",
    "status": "Ready"
}

with open("server.json", "w") as file:
    json.dump(server, file, indent=4)

# This creates: server.json
# Contents:
# {
#     "hostname": "ocp-w-1",
#     "ip": "192.168.22.211",
#     "status": "Ready"
# }

# Example — Generate Server Inventory
import json

servers = [
    {
        "hostname": "ocp-cp-1",
        "ip": "192.168.22.201",
        "role": "control-plane"
    },
    {
        "hostname": "ocp-w-1",
        "ip": "192.168.22.211",
        "role": "worker"
    },
    {
        "hostname": "ocp-w-2",
        "ip": "192.168.22.212",
        "role": "worker"
    }
]

with open("inventory.json", "w") as file:
    json.dump(servers, file, indent=4)

# Generated file:
[
    {
        "hostname": "ocp-cp-1",
        "ip": "192.168.22.201",
        "role": "control-plane"
    },
    {
        "hostname": "ocp-w-1",
        "ip": "192.168.22.211",
        "role": "worker"
    },
    {
        "hostname": "ocp-w-2",
        "ip": "192.168.22.212",
        "role": "worker"
    }
]
# This could be consumed by another automation process.

##########################################################################################################
# json.load()
# This is the reverse of dump().
# JSON file → Python object
# Suppose inventory.json contains:
{
    "hostname": "ocp-w-1",
    "ip": "192.168.22.211",
    "role": "worker"
}
# Python:
import json

with open("inventory.json", "r") as file:
    server = json.load(file)

print(server)
print(server["hostname"])
print(server["ip"])
# Output:
# {'hostname': 'ocp-w-1', 'ip': '192.168.22.211', 'role': 'worker'}
# ocp-w-1
# 192.168.22.211

# Difference Between load() and loads()
# This is a very important interview question.
# | Function       | Input         | Output        |
# | -------------- | ------------- | ------------- |
# | `json.load()`  | JSON file     | Python object |
# | `json.loads()` | JSON string   | Python object |
# | `json.dump()`  | Python object | JSON file     |
# | `json.dumps()` | Python object | JSON string   |

########################################################################################################
# Working With Lists
# JSON can contain arrays.

# Python:
import json

pods = [
    "nginx-1",
    "nginx-2",
    "nginx-3"
]

data = json.dumps(pods)

print(data)
# Output: ["nginx-1", "nginx-2", "nginx-3"]
# Convert back:
pods = json.loads(data)

print(pods)
print(pods[0]) 
# Output:
# ['nginx-1', 'nginx-2', 'nginx-3']
# nginx-1

#########################################################################################################
# Nested JSON
# DevOps APIs frequently return nested JSON.

# Example:
import json

data = '''
{
    "cluster": {
        "name": "lab-cluster",
        "version": "4.20.13"
    },
    "nodes": {
        "control_plane": 3,
        "workers": 3
    }
}
'''

cluster = json.loads(data)

print(cluster["cluster"]["name"])
print(cluster["cluster"]["version"])

print(cluster["nodes"]["workers"])

# Output:
# lab-cluster
# 4.20.13
# 3
############################################################################################################
# Real DevOps Example — Kubernetes Pod JSON
# Suppose you run:
# oc get pods -o json
# You could save it:oc get pods -o json > pods.json
# Then process it using Python:
import json

with open("pods.json") as file:
    data = json.load(file)

for pod in data["items"]:
    name = pod["metadata"]["name"]
    namespace = pod["metadata"]["namespace"]

    print(f"{namespace}: {name}")

# Possible Output:
# default: nginx-1
# default: nginx-2 

#################################################################################################
# Get Pod Status
# You can extend the previous example:
import json

with open("pods.json") as file:
    data = json.load(file)

for pod in data["items"]:

    name = pod["metadata"]["name"]

    status = pod.get("status", {}).get("phase", "Unknown")

    print(f"{name} --> {status}")
# Possible Output:
# nginx-1 --> Running
# nginx-2 --> Pending
# nginx-3 --> Running
# Notice this:
# pod.get("status", {}).get("phase", "Unknown")
# It prevents a KeyError if a field doesn't exist.

#########################################################################################################
# get() vs Direct JSON Access
# Direct access:
status = pod["status"]["phase"]
# If phase doesn't exist:
# KeyError: 'phase'
# Safer:
status = pod.get("status", {}).get("phase", "Unknown")
# This is preferable for automation scripts where API responses may vary.

########################################################################################################
# Example — Find Failed Pods
import json

with open("pods.json") as file:
    data = json.load(file)

for pod in data["items"]:

    name = pod["metadata"]["name"]
    status = pod.get("status", {}).get("phase", "Unknown")

    if status != "Running":
        print(f"WARNING: {name} is {status}")
# Example:
# WARNING: redis-0 is Pending
# WARNING: nginx-1 is Failed
# You could then integrate this script into a CI/CD health check.

#########################################################################################################
# JSON Boolean Values
# JSON:
{
    "enabled": true,
    "debug": false
}
# Python:
import json
data = {
    "enabled": True,
    "debug": False
}
# Convert:
import json

print(json.dumps(data))
# Output: {"enabled": true, "debug": false}

#########################################################################################################
# JSON null
# JSON:
{
    "node": "worker-1",
    "ip": null
}
# Python:
data = {
    "node": "worker-1",
    "ip": None
}
# Convert:
import json
print(json.dumps(data))
# Output: {"node": "worker-1", "ip": null}

#########################################################################################################
# JSON Error Handling
# Production DevOps scripts should handle invalid JSON.

# Example:
import json

data = '{"hostname": "ocp-w-1", "status": }'

try:
    server = json.loads(data)
    print(server)

except json.JSONDecodeError as e:
    print("Invalid JSON")
    print("Error:", e)
# Possible output:
# Invalid JSON
# Error: Expecting value: line 1 column 31 (char 30)
##########################################################################################################
# Example — Validate API Response
import json

api_response = '{"status": "Ready", "node": "ocp-w-1"}'

try:
    data = json.loads(api_response)

    status = data.get("status")

    if status == "Ready":
        print("Node is healthy")
    else:
        print("Node is not ready")

except json.JSONDecodeError:
    print("ERROR: API returned invalid JSON")
# Possible output:
# Node is healthy
##########################################################################################################
# JSON Configuration File
# You can use JSON as a configuration file.

# config.json
{
    "environment": "production",
    "namespace": "sonarqube",
    "replicas": 3,
    "image": "sonarqube:2026.1-community",
    "port": 9000
}
# Python:
import json

with open("config.json") as file:
    config = json.load(file)

print("Environment:", config["environment"])
print("Namespace:", config["namespace"])
print("Replicas:", config["replicas"])
print("Image:", config["image"])
print("Port:", config["port"])
# Output:
# Environment: production
# Namespace: sonarqube
# Replicas: 3
# Image: sonarqube:2026.1-community
# Port: 9000

# Modify JSON Configuration
# You can also modify configuration programmatically.
import json

with open("config.json") as file:
    config = json.load(file)

config["replicas"] = 5

with open("config.json", "w") as file:
    json.dump(config, file, indent=4)

# Now:
{
    "environment": "production",
    "namespace": "sonarqube",
    "replicas": 5,
    "image": "sonarqube:2026.1-community",
    "port": 9000
}

#########################################################################################
# JSON + Environment Variables
# JSON configuration
#         +
# Environment variables
#         ↓
# Automation script
import json
import os

with open("config.json") as file:
    config = json.load(file)

namespace = os.getenv("NAMESPACE", config["namespace"])

print("Namespace:", namespace)
# If:
# export NAMESPACE=production
# then:
# Namespace: production
# Otherwise it uses:
# "namespace": "sonarqube"

###############################################################################################
# JSON + Subprocess + OpenShift
# Run: oc get nodes -o json
# from Python.
import subprocess
import json

result = subprocess.run(
    ["oc", "get", "nodes", "-o", "json"],
    capture_output=True,
    text=True,
    check=True
)

data = json.loads(result.stdout)

for node in data["items"]:

    name = node["metadata"]["name"]

    conditions = node.get("status", {}).get("conditions", [])

    ready = "Unknown"

    for condition in conditions:
        if condition["type"] == "Ready":
            ready = condition["status"]

    print(f"{name}: Ready={ready}")
# Possible Output:
# ocp-cp-1: Ready=True
# ocp-cp-2: Ready=True
# ocp-cp-3: Ready=True

##################################################################################
# JSON + REST API
import json
import requests

response = requests.get(
    "https://example.com/api/status"
)

data = response.json()

print(data["status"])
# response.json() is a convenient method that automatically parses the JSON response and returns a Python object.
