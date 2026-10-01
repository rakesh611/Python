# The Python yaml module is used to read, write, parse, and modify YAML files.
# In DevOps, YAML is extremely important because many tools use YAML for configuration:
# Kubernetes / OpenShift manifests
# Ansible playbooks
# Docker Compose
# GitLab CI/CD
# Argo CD
# Helm values
# CI/CD pipelines
# Application configuration

# Python does not provide YAML support in its standard library, so the most commonly used library is PyYAML.
# Install PyYAML
pip install PyYAML
# Verify:
python3 -c "import yaml; print(yaml.__version__)"
# Import it in Python:
import yaml

#########################################################################################################################
# Important PyYAML functions
# The most important functions are:
# | Function               | Purpose                                           |
# | ---------------------- | ------------------------------------------------- |
# | `yaml.safe_load()`     | YAML → Python object                              |
# | `yaml.safe_load_all()` | Multiple YAML documents → Python objects          |
# | `yaml.safe_dump()`     | Python object → YAML                              |
# | `yaml.safe_dump_all()` | Multiple Python objects → multiple YAML documents |
# | `yaml.load()`          | Load YAML with a loader                           |
# | `yaml.dump()`          | Python object → YAML                              |
# | `yaml.full_load()`     | Load YAML using FullLoader                        |
# | `yaml.full_load_all()` | Load multiple YAML documents                      |
# | `yaml.scan()`          | Generate YAML tokens                              |
# | `yaml.parse()`         | Generate YAML parsing events                      |

##############################################################################################################################
# yaml.safe_load()
# This is probably the most important YAML function for DevOps.
# It converts YAML into a Python object.
# YAML file
# deployment.yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: nginx

spec:
  replicas: 3

  selector:
    matchLabels:
      app: nginx
# Python:
import yaml

with open("deployment.yaml", "r") as file:
    data = yaml.safe_load(file)

print(data)

# Output:
{
    'apiVersion': 'apps/v1',
    'kind': 'Deployment',
    'metadata': {
        'name': 'nginx'
    },
    'spec': {
        'replicas': 3,
        'selector': {
            'matchLabels': {
                'app': 'nginx'
            }
        }
    }
}
# YAML becomes a Python dictionary.
# Access YAML values
# After using:
data = yaml.safe_load(file)

# you can access values like a normal Python dictionary.
print(data["apiVersion"])
print(data["kind"])
print(data["metadata"]["name"])
print(data["spec"]["replicas"])
# Output:
# apps/v1
# Deployment
# nginx
# 3

# Example — Check Kubernetes replicas
# Suppose:   replicas: 3
import yaml

with open("deployment.yaml") as file:
    deployment = yaml.safe_load(file)

replicas = deployment["spec"]["replicas"]

print("Current replicas:", replicas)

if replicas < 3:
    print("WARNING: Replica count is too low")
else:
    print("Replica count is OK")

# Output: 
# Current replicas: 3
# Replica count is OK
# This is useful for configuration validation.

########################################################################################################################################
# yaml.safe_dump()
# safe_dump() converts a Python object into YAML.

# Example:
import yaml

data = {
    "name": "nginx",
    "replicas": 3,
    "image": "nginx:1.27"
}

yaml_output = yaml.safe_dump(data)

print(yaml_output)
# Output:
image: nginx:1.27
name: nginx
replicas: 3

############################################################################################################################################
# Write YAML to a file
import yaml

data = {
    "name": "nginx",
    "replicas": 3,
    "image": "nginx:1.27"
}

with open("deployment.yaml", "w") as file:
    yaml.safe_dump(data, file)

# Now: cat deployment.yaml
# Output:
image: nginx:1.27
name: nginx
replicas: 3

# Example — Generate Kubernetes YAML
import yaml

deployment = {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
        "name": "nginx"
    },
    "spec": {
        "replicas": 3,
        "selector": {
            "matchLabels": {
                "app": "nginx"
            }
        }
    }
}

with open("nginx-deployment.yaml", "w") as file:
    yaml.safe_dump(deployment, file, sort_keys=False)

print("Kubernetes YAML generated successfully")
# Generated YAML:
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
# Notice: sort_keys=False
# This preserves the dictionary's insertion order, making generated Kubernetes YAML easier to read.
##########################################################################################################################################
# Modify an existing Kubernetes YAML
# This is one of the most useful real-world DevOps examples.
# Original:
apiVersion: apps/v1
kind: Deployment

metadata:
  name: nginx

spec:
  replicas: 3

# Python:
import yaml

with open("deployment.yaml") as file:
    data = yaml.safe_load(file)

print("Old replicas:", data["spec"]["replicas"])

data["spec"]["replicas"] = 5

with open("deployment.yaml", "w") as file:
    yaml.safe_dump(data, file, sort_keys=False)

print("New replicas:", data["spec"]["replicas"])

# Output:
# Old replicas: 3
# New replicas: 5

############################################################################################################################################
# yaml.safe_load() with a YAML string
# You don't always need a file.
# You can parse a YAML string:
import yaml

yaml_data = """
name: nginx
replicas: 3
environment: production
"""

data = yaml.safe_load(yaml_data)

print(data)
# Output:
{
    'name': 'nginx',
    'replicas': 3,
    'environment': 'production'
}
##########################################################################################################################################
# Convert YAML string to Python
import yaml

yaml_data = """
server:
  hostname: web01
  ip: 192.168.22.20
  port: 8080
"""

data = yaml.safe_load(yaml_data)

print(data["server"]["hostname"])
print(data["server"]["ip"])
print(data["server"]["port"])
# Output:
# web01
# 192.168.22.20
# 8080

############################################################################################################################################
# yaml.safe_dump() with string output
# You can also create YAML without writing immediately to a file.
import yaml

data = {
    "server": {
        "hostname": "web01",
        "ip": "192.168.22.20",
        "port": 8080
    }
}

yaml_string = yaml.safe_dump(data, sort_keys=False)

print(yaml_string)
# Output:
server:
  hostname: web01
  ip: 192.168.22.20
  port: 8080

##############################################################################################################################################
# yaml.safe_load_all()
# This is extremely important for Kubernetes/OpenShift.
# A Kubernetes YAML file often contains multiple resources separated by ---.

# Example:
apiVersion: v1
kind: Service
metadata:
  name: nginx
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
# This is called a multi-document YAML file.
import yaml

with open("resources.yaml") as file:
    resources = yaml.safe_load_all(file)

for resource in resources:
    print(resource["kind"])
# Output:
Service
Deployment

# Example — Find all Kubernetes resources
import yaml

with open("resources.yaml") as file:
    resources = yaml.safe_load_all(file)

for resource in resources:
    print(
        "Kind:",
        resource["kind"],
        "Name:",
        resource["metadata"]["name"]
    )
# Output:
Kind: Service Name: nginx
Kind: Deployment Name: nginx
#################################################################################################################################################
# yaml.safe_dump_all()
# The opposite of safe_load_all().
# It converts multiple Python dictionaries into multiple YAML documents.

# Example:
import yaml

service = {
    "apiVersion": "v1",
    "kind": "Service",
    "metadata": {
        "name": "nginx"
    }
}

deployment = {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
        "name": "nginx"
    }
}

resources = [
    service,
    deployment
]

with open("resources.yaml", "w") as file:
    yaml.safe_dump_all(
        resources,
        file,
        sort_keys=False
    )
# Generated:
apiVersion: v1
kind: Service
metadata:
  name: nginx
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
# However, for normal DevOps configuration processing, prefer:
yaml.safe_load()
# rather than using an unsafe loader.

#######################################################################################################33
# yaml.full_load()
# full_load() loads YAML using FullLoader.

# Example:
import yaml

with open("config.yaml") as file:
    data = yaml.full_load(file)

print(data)
# For ordinary Kubernetes/OpenShift configuration automation, you will normally have little reason to use it instead of:yaml.safe_load()

################################################################################################################
# yaml.full_load_all()
# Used when the YAML contains multiple documents.
import yaml

with open("resources.yaml") as file:
    resources = yaml.full_load_all(file)

for resource in resources:
    print(resource)
# Again, for ordinary DevOps YAML processing, safe_load_all() is usually the better default.

#################################################################################################################
# Example — Worker node configuration
# Suppose:
workers:
  - name: ocp-w-1
    ip: 192.168.22.211
    cpu: 8

  - name: ocp-w-2
    ip: 192.168.22.212
    cpu: 8

  - name: ocp-w-3
    ip: 192.168.22.213
    cpu: 8

# Python:
import yaml

with open("workers.yaml") as file:
    data = yaml.safe_load(file)

for worker in data["workers"]:
    print(
        f"Node: {worker['name']} "
        f"IP: {worker['ip']} "
        f"CPU: {worker['cpu']}"
    )
# Output:
Node: ocp-w-1 IP: 192.168.22.211 CPU: 8
Node: ocp-w-2 IP: 192.168.22.212 CPU: 8
Node: ocp-w-3 IP: 192.168.22.213 CPU: 8

##########################################################################################################
# Modify an image tag
# YAML is often used for application configuration.
# Suppose:
spec:
  template:
    spec:
      containers:
        - name: nginx
          image: nginx:1.27

# Python:
import yaml

with open("deployment.yaml") as file:
    data = yaml.safe_load(file)

data["spec"]["template"]["spec"]["containers"][0]["image"] = "nginx:1.28"

with open("deployment.yaml", "w") as file:
    yaml.safe_dump(data, file, sort_keys=False)

########################################################################################################
# Modify multiple containers
containers:
  - name: nginx
    image: nginx:1.27

  - name: sidecar
    image: busybox:1.36

# Python
import yaml

with open("deployment.yaml") as file:
    data = yaml.safe_load(file)

containers = data["spec"]["template"]["spec"]["containers"]

for container in containers:
    print(
        container["name"],
        container["image"]
    )
# Output:
nginx nginx:1.27
sidecar busybox:1.36

#Find a specific container
import yaml

with open("deployment.yaml") as file:
    data = yaml.safe_load(file)

containers = data["spec"]["template"]["spec"]["containers"]

for container in containers:

    if container["name"] == "nginx":
        print("Current image:", container["image"])

# Update image automatically
import yaml

NEW_IMAGE = "nginx:1.28"

with open("deployment.yaml") as file:
    data = yaml.safe_load(file)

containers = data["spec"]["template"]["spec"]["containers"]

for container in containers:

    if container["name"] == "nginx":
        container["image"] = NEW_IMAGE

with open("deployment.yaml", "w") as file:
    yaml.safe_dump(
        data,
        file,
        sort_keys=False
    )

print("Image updated successfully")

# YAML validation using Python
import yaml

try:

    with open("deployment.yaml") as file:
        data = yaml.safe_load(file)

    print("YAML syntax is valid")

except yaml.YAMLError as error:

    print("Invalid YAML")
    print(error)

# CI/CD YAML validation
import yaml
import sys

file_name = "deployment.yaml"

try:

    with open(file_name) as file:
        yaml.safe_load(file)

    print(f"{file_name}: YAML is valid")

except yaml.YAMLError as error:

    print(f"{file_name}: YAML is invalid")
    print(error)

    sys.exit(1)

# Validate Kubernetes resource kind
# You can combine Python and YAML.
import yaml
import sys

with open("deployment.yaml") as file:
    data = yaml.safe_load(file)

if data.get("kind") != "Deployment":
    print("ERROR: Resource is not a Deployment")
    sys.exit(1)

print("Deployment YAML detected")

# Validate required fields
import yaml
import sys

with open("deployment.yaml") as file:
    data = yaml.safe_load(file)

required_fields = [
    "apiVersion",
    "kind",
    "metadata",
    "spec"
]

for field in required_fields:

    if field not in data:
        print(f"ERROR: Missing field: {field}")
        sys.exit(1)

print("Required fields are present")

# Generate YAML and apply it
import yaml
import subprocess

deployment = {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
        "name": "nginx"
    },
    "spec": {
        "replicas": 3
    }
}

with open("generated.yaml", "w") as file:
    yaml.safe_dump(
        deployment,
        file,
        sort_keys=False
    )

subprocess.run(
    ["oc", "apply", "-f", "generated.yaml"],
    check=True
)

print("Deployment applied successfully")

#############################################################################################################
# Complete DevOps Project Example
# Suppose you have:
apiVersion: apps/v1
kind: Deployment

metadata:
  name: nginx

spec:
  replicas: 2

  selector:
    matchLabels:
      app: nginx

  template:
    metadata:
      labels:
        app: nginx

    spec:
      containers:
        - name: nginx
          image: nginx:1.27
          ports:
            - containerPort: 80

# Create:update_deployment.py
import yaml
import sys

FILE = "deployment.yaml"
NEW_REPLICAS = 5
NEW_IMAGE = "nginx:1.28"


try:

    # Read YAML
    with open(FILE, "r") as file:
        deployment = yaml.safe_load(file)

except FileNotFoundError:

    print(f"ERROR: File not found: {FILE}")
    sys.exit(1)

except yaml.YAMLError as error:

    print("ERROR: Invalid YAML")
    print(error)
    sys.exit(1)


# Validate resource
if deployment.get("kind") != "Deployment":

    print("ERROR: YAML is not a Deployment")
    sys.exit(1)


# Update replicas
deployment["spec"]["replicas"] = NEW_REPLICAS


# Update container image
containers = deployment["spec"]["template"]["spec"]["containers"]

for container in containers:

    if container["name"] == "nginx":

        container["image"] = NEW_IMAGE


# Write YAML
with open(FILE, "w") as file:

    yaml.safe_dump(
        deployment,
        file,
        sort_keys=False
    )


print("Deployment updated successfully")
print("Replicas:", NEW_REPLICAS)
print("Image:", NEW_IMAGE)

# Run:python3 update_deployment.py

# Result:
spec:
  replicas: 5

  template:
    spec:
      containers:
        - name: nginx
          image: nginx:1.28