# The Python sys module provides access to variables and functions that interact with the Python interpreter and the operating system environment.
# sys is a built-in Python module, so you don't need to install it using pip.
# import sys
# Example:
import sys

print(sys.version)

# You may have a Jenkins, Ansible, Kubernetes, or Linux automation script that requires Python 3.9+.
import sys

if sys.version_info < (3, 9):
    print("ERROR: Python 3.9 or higher is required")
    sys.exit(1)

print("Python version is supported")

# Important sys functions and attributes
# | Function / Attribute      | Purpose                                                |
# | ------------------------- | ------------------------------------------------------ |
# | `sys.argv`                | Read command-line arguments                            |
# | `sys.exit()`              | Exit a script with a status code                       |
# | `sys.version`             | Python version information                             |
# | `sys.version_info`        | Python version as structured information               |
# | `sys.platform`            | Identify operating platform                            |
# | `sys.executable`          | Path of Python interpreter                             |
# | `sys.path`                | Python module search paths                             |
# | `sys.stdin`               | Standard input                                         |
# | `sys.stdout`              | Standard output                                        |
# | `sys.stderr`              | Standard error                                         |
# | `sys.modules`             | Loaded Python modules                                  |
# | `sys.getsizeof()`         | Approximate memory size of an object                   |
# | `sys.maxsize`             | Maximum value related to Python integer implementation |
# | `sys.prefix`              | Python installation/environment prefix                 |
# | `sys.getrecursionlimit()` | Get recursion limit                                    |
# | `sys.setrecursionlimit()` | Change recursion limit                                 |

##########################################################################################3
# sys.argv — Command-Line Arguments
# sys.argv contains the arguments passed to a Python script.
import sys

if len(sys.argv) < 2:
    print("Usage: python3 server_check.py <server1> <server2> ...")
    sys.exit(1)

for server in sys.argv[1:]:
    print(f"Checking server: {server}")

# Run:
# python3 server_check.py web01 web02 db01
# Output
# Checking server: web01
# Checking server: web02
# Checking server: db01
############################################################################33
# sys.exit() — Exit a Script
# sys.exit() terminates the Python program.
# Example:
import sys

print("Starting deployment")

sys.exit(1)

print("This will not execute")
# Output: Starting deployment
# What does 0 and 1 mean?
# 0 → Success
# non-zero → Failure
# Example:
import sys

deployment_success = True

if deployment_success:
    print("Deployment successful")
    sys.exit(0)
else:
    print("Deployment failed")
    sys.exit(1)

######################################################################
# sys.version
# Returns the Python version and build information.
# Check Python version before running automation:
import sys

print("Python version:")
print(sys.version)

########################################################################
# sys.version_info
# sys.version_info gives structured Python version information.
import sys

if sys.version_info >= (3, 10):
    print("Python version supported")
else:
    print("Python 3.10 or higher required")
    sys.exit(1)

# Imagine your automation requires Python 3.10+:
required_version = (3, 10)

if sys.version_info < required_version:
    print("ERROR: Python 3.10+ required")
    sys.exit(1)

print("Environment validation successful")
#########################################################################
# sys.platform
# Returns information about the operating system/platform.
import sys

if sys.platform.startswith("linux"):
    print("Running on Linux")
elif sys.platform == "win32":
    print("Running on Windows")
elif sys.platform == "darwin":
    print("Running on macOS")
else:
    print("Unknown platform")

#########################################################################
# sys.executable
# Returns the path of the Python interpreter running your script.
# Check which Python interpreter is actually being used:
import sys

print("Python interpreter:")
print(sys.executable)

##########################################################################
# sys.path
# sys.path contains directories where Python searches for modules.
import sys

print(sys.path)
#########################################################################
# sys.stdin
# sys.stdin represents standard input.
# Normally this comes from the terminal.
import sys

name = sys.stdin.readline().strip()

print(f"Hello {name}")
# Run:python3 script.py
# Enter:Rakesh
# Output: Hello Rakesh
# DevOps Example — Read Deployment Environment
import sys

environment = sys.stdin.readline().strip()

if environment == "production":
    print("Production deployment selected")
elif environment == "staging":
    print("Staging deployment selected")
else:
    print("Unknown environment")

####################################################################################
# sys.stdout
# sys.stdout represents standard output.
# Normally:
print("Hello")
# print("Hello")
stdout
# You can directly use:
import sys

sys.stdout.write("Deployment started\n")
# Equivalent to:
print("Deployment started")
# DevOps Example
import sys

sys.stdout.write("[INFO] Deployment started\n")
sys.stdout.write("[INFO] Checking Kubernetes cluster\n")
sys.stdout.write("[INFO] Deployment completed\n")

##############################################################################
# sys.stderr
# sys.stderr is used for error messages.
# Example:
import sys

sys.stderr.write("ERROR: Kubernetes cluster is unavailable\n")
# This is very useful in Jenkins, GitLab CI, shell pipelines, and production automation.

################################################################################
# sys.getsizeof()
# Returns the approximate memory size of an object in bytes.
import sys

name = "Linux"

print(sys.getsizeof(name))
################################################################################
# sys.maxsize
# Returns a large integer related to the platform's integer implementation.
import sys

print(sys.maxsize)
# You can use it when you need a very large sentinel value:
import sys

MAX_VALUE = sys.maxsize

print(MAX_VALUE)
# Example:
import sys

smallest_server_load = sys.maxsize

loads = [80, 30, 50, 20]

for load in loads:
    if load < smallest_server_load:
        smallest_server_load = load

print("Lowest load:", smallest_server_load)

#############################################################################
# sys.modules
# sys.modules contains modules that have already been loaded by Python.
# Example:
import sys

print(sys.modules)
# You will see many modules.
# You can check whether a module has already been loaded:
import sys

if "os" in sys.modules:
    print("os module is already loaded")
else:
    print("os module is not loaded")
# You can inspect whether a required library is loaded:
import sys

if "requests" in sys.modules:
    print("requests is already loaded")
else:
    print("requests is not loaded")
# This is mostly useful for debugging Python runtime behavior rather than normal application code.

####################################################################################
# sys.prefix
# sys.prefix tells you the prefix associated with the Python installation/environment.
import sys

print(sys.prefix)
# DevOps troubleshooting
import sys

print("Python environment:", sys.prefix)
print("Python executable:", sys.executable)
####################################################################################
# sys.getrecursionlimit()
# Python limits recursion depth to avoid uncontrolled recursion.
# Check it:
import sys

print(sys.getrecursionlimit())
####################################################################################
# sys.setrecursionlimit()
# Changes the recursion limit.
import sys

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

###################################################################################
# sys.stdin, stdout, and stderr together
# This is particularly useful for CLI automation.
import sys

sys.stdout.write("[INFO] Starting deployment\n")

environment = sys.stdin.readline().strip()

if environment not in ["dev", "staging", "production"]:
    sys.stderr.write("[ERROR] Invalid environment\n")
    sys.exit(1)

sys.stdout.write(f"[INFO] Deploying to {environment}\n")
# Run:
# echo "production" | python3 deploy.py
# Output:
# [INFO] Starting deployment
# [INFO] Deploying to production