# The Python subprocess module is one of the most important modules for a DevOps/SRE engineer because it allows Python programs to execute Linux/Unix commands and interact with their output, errors, return codes, and processes.
# subprocess is a Python standard-library module used to:

# Execute Linux commands
# Execute shell commands
# Capture command output
# Capture errors
# Check command exit status
# Pass input to commands
# Run long-running processes
# Chain commands/processes
# Automate DevOps tasks
# Basic example
import subprocess

result = subprocess.run(["hostname"])

print(result)
# For example:
import subprocess

result = subprocess.run(
    ["df", "-h", "/"],
    capture_output=True,
    text=True
)

print(result.stdout)
# Output might be:
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda3       100G   62G   38G  62% /

###############################################################################
# Important functions/classes in subprocess
# | API                             | Purpose                                    |
# | ------------------------------- | ------------------------------------------ |
# | `subprocess.run()`              | Run a command and wait for completion      |
# | `subprocess.Popen()`            | Start and control a process                |
# | `subprocess.call()`             | Run command and return exit code           |
# | `subprocess.check_call()`       | Run command and raise exception on failure |
# | `subprocess.check_output()`     | Run command and return output              |
# | `subprocess.getoutput()`        | Run shell command and return output        |
# | `subprocess.getstatusoutput()`  | Return exit status + output                |
# | `subprocess.PIPE`               | Connect process input/output               |
# | `subprocess.DEVNULL`            | Discard output                             |
# | `subprocess.STDOUT`             | Send stderr to stdout                      |
# | `subprocess.TimeoutExpired`     | Exception for timeout                      |
# | `subprocess.CalledProcessError` | Exception for failed command               |

######################################################################################
# subprocess.run()
# This is the most important function.
# Syntax:
subprocess.run(command)
# Example:
import subprocess

subprocess.run(["hostname"])
# Execute ls
import subprocess

subprocess.run(["ls", "-l"])
# Notice that we pass arguments separately:
# This is generally safer and clearer.

###############################################################################
# Capture command output
# Normally:
subprocess.run(["hostname"])
# prints directly to the terminal.
# If you want Python to capture the output, use:
capture_output=True
# Example:
import subprocess

result = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
)

print("Hostname:", result.stdout)
# Important attributes
# result.stdout
# result.stderr
# result.returncode

#####################################################################################
# stdout
# stdout contains the command's standard output.
import subprocess

result = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
)

print(result.stdout)

######################################################################################
# stderr
# stderr contains error output.
# Example:
import subprocess

result = subprocess.run(
    ["ls", "/does-not-exist"],
    capture_output=True,
    text=True
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
# Possible output:
# STDOUT:
# STDERR: ls: cannot access '/does-not-exist': No such file or directory
# This is extremely useful for RCA and troubleshooting automation.

####################################################################################
# returncode
# Linux commands return an exit code.
# Normally:
# 0 = success
# non-zero = failure
# Example:
import subprocess

result = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
)

print("Return code:", result.returncode)

# service health check
import subprocess

result = subprocess.run(
    ["systemctl", "is-active", "--quiet", "sshd"]
)

if result.returncode == 0:
    print("sshd is running")
else:
    print("sshd is NOT running")

# Equivalent:
# systemctl is-active --quiet sshd
# echo $?
#############################################################################
# text=True
# Without text=True, output is returned as bytes.
import subprocess

result = subprocess.run(
    ["hostname"],
    capture_output=True
)

print(result.stdout)
# Output:b'ocp-svc\n'
# With: text=True
import subprocess

result = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
)

print(result.stdout)
# Output: ocp-svc

##################################################################################
# check=True
# By default, a failed command doesn't automatically raise an exception.
# Example:
import subprocess

result = subprocess.run(
    ["ls", "/does-not-exist"],
    capture_output=True,
    text=True
)

print(result.returncode)
# You get a non-zero return code.
# But:
subprocess.run(
    ["ls", "/does-not-exist"],
    check=True
)
# raises: subprocess.CalledProcessError
# Example:
import subprocess

try:
    subprocess.run(
        ["systemctl", "restart", "sshd"],
        check=True
    )

    print("SSH service restarted successfully")

except subprocess.CalledProcessError:
    print("Failed to restart SSH service")

# This is useful when failure must stop the automation.

#################################################################################
# timeout
# You can prevent a command from running forever.
import subprocess

try:
    result = subprocess.run(
        ["ping", "-c", "4", "8.8.8.8"],
        capture_output=True,
        text=True,
        timeout=10
    )

    print(result.stdout)

except subprocess.TimeoutExpired:
    print("Command timed out")

# Example: server connectivity
import subprocess

server = "192.168.22.211"

try:
    result = subprocess.run(
        ["ping", "-c", "3", server],
        capture_output=True,
        text=True,
        timeout=10
    )

    if result.returncode == 0:
        print(f"{server} is reachable")
    else:
        print(f"{server} is NOT reachable")

except subprocess.TimeoutExpired:
    print(f"{server} ping timed out")

#################################################################################
# check_output()
# check_output() executes a command and returns its output.
# Example:
import subprocess

output = subprocess.check_output(
    ["hostname"],
    text=True
)

print(output)
# Output:ocp-svc

# Important difference
# run()
result = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
)

print(result.stdout)
# check_output()
output = subprocess.check_output(
    ["hostname"],
    text=True
)

print(output)
# check_output() is convenient when you mainly need the output.
# If the command fails, it raises:
# subprocess.CalledProcessError

# Example: Get Kubernetes nodes
import subprocess

output = subprocess.check_output(
    ["kubectl", "get", "nodes"],
    text=True
)

print(output)
# Equivalent:kubectl get nodes
# Example:2
import subprocess

result = subprocess.run(
    ["oc", "get", "nodes"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(result.stdout)
else:
    print("OpenShift command failed")
    print(result.stderr)

############################################################################
# call()
# subprocess.call() executes a command and returns the exit status.
# Example:
import subprocess

return_code = subprocess.call(["hostname"])

print("Return code:", return_code)
# If successful:ocp-svc Return code: 0
# Example:
import subprocess

try:
    subprocess.check_call(
        ["systemctl", "restart", "sshd"]
    )

    print("SSH restarted")

except subprocess.CalledProcessError:
    print("SSH restart failed")

# getoutput()
# getoutput() executes a command through the shell and returns the output as a string.
# Example:
import subprocess

output = subprocess.getoutput("hostname")

print(output)
# Equivalent:hostname
################################################################################
# getstatusoutput()
# This returns:
# (status, output)
# Example: 
import subprocess

status, output = subprocess.getstatusoutput("hostname")

print("Status:", status)
print("Output:", output)

# If command fails:
status, output = subprocess.getstatusoutput(
    "ls /does-not-exist"
)

print("Status:", status)
print("Output:", output)

#############################################################################
# Popen()
# Popen means Process Open.
# It provides more control over a running process.
import subprocess

process = subprocess.Popen(
    ["ping", "-c", "5", "8.8.8.8"]
)

process.wait()

print("Process completed")
# Unlike simple run(), Popen() is designed for more advanced process management.

########################################################################################
# Popen() with output
import subprocess

process = subprocess.Popen(
    ["hostname"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate()

print("Output:", stdout)
print("Error:", stderr)
#############################################################################
# communicate()
# communicate() is used with Popen() to:
# Send input
# Read stdout
# Read stderr
# Wait for process completion

# Example:
import subprocess

process = subprocess.Popen(
    ["cat"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate(
    input="Hello DevOps\n"
)

print(stdout)
# Output:Hello DevOps

###############################################################################
# PIPE
# subprocess.PIPE allows Python to connect to the process's:
# stdin
# stdout
# stderr

# Example:
import subprocess

process = subprocess.Popen(
    ["hostname"],
    stdout=subprocess.PIPE,
    text=True
)

output = process.communicate()[0]

print(output)

######################################################################################
# DEVNULL
# DEVNULL discards output.

# Example:
import subprocess

subprocess.run(
    ["ping", "-c", "3", "8.8.8.8"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

print("Ping completed")
# Useful when you don't need command output.

###################################################################################
# STDOUT
# You can redirect stderr into stdout.
import subprocess

result = subprocess.run(
    ["ls", "/does-not-exist"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

print(result.stdout)
# Now both normal output and errors are available through:

#####################################################################################
# shell=True
# This is an important concept.

# Without shell:
subprocess.run(
    ["ls", "-l"]
)
# With shell:
subprocess.run(
    "ls -l",
    shell=True
)
# The second version asks the system shell to interpret the command.

# Why is shell=True dangerous?
# Never directly put untrusted user input into:
subprocess.run(command, shell=True)
# Example: 
user_input = input("Enter filename: ")

subprocess.run(
    f"cat {user_input}",
    shell=True
)
# If user_input contains shell metacharacters, unintended commands could be executed.
# Prefer argument lists over shell=True.

###############################################################################################
# Environment variables with env
# You can pass environment variables to a process.
import subprocess
import os

env = os.environ.copy()

env["ENVIRONMENT"] = "production"

result = subprocess.run(
    ["bash", "-c", "echo $ENVIRONMENT"],
    env=env,
    capture_output=True,
    text=True
)

print(result.stdout)
# Output:production

# Example: Git branch
import subprocess

result = subprocess.run(
    ["git", "branch", "--show-current"],
    capture_output=True,
    text=True
)

branch = result.stdout.strip()

print("Current branch:", branch)
# Possible output: Current branch: main

# Example: Git status
import subprocess

result = subprocess.run(
    ["git", "status", "--short"],
    capture_output=True,
    text=True
)

if result.stdout.strip():
    print("Working tree contains changes:")
    print(result.stdout)
else:
    print("Working tree is clean")

# Example: Docker status
import subprocess

result = subprocess.run(
    ["docker", "ps"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(result.stdout)
else:
    print("Docker command failed")
    print(result.stderr)

# Example: Kubernetes pods
import subprocess

result = subprocess.run(
    ["kubectl", "get", "pods", "-A"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(result.stdout)
else:
    print("kubectl failed")
    print(result.stderr)

# Example: OpenShift troubleshooting
import subprocess

commands = [
    ["oc", "get", "nodes"],
    ["oc", "get", "pods", "-A"],
    ["oc", "get", "co"],
    ["oc", "get", "events", "-A"]
]

for command in commands:

    print("\n==============================")
    print("Running:", " ".join(command))
    print("==============================")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print("ERROR:")
        print(result.stderr)

# Example: Disk health check
import subprocess

result = subprocess.run(
    ["df", "-h", "/"],
    capture_output=True,
    text=True
)

print(result.stdout)
# You can further process the result:
import subprocess

result = subprocess.run(
    ["df", "-h", "/"],
    capture_output=True,
    text=True
)

lines = result.stdout.splitlines()

for line in lines:
    print(line)

# Example: Check disk usage
import subprocess

result = subprocess.run(
    ["df", "-P", "/"],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print("Unable to check disk usage")
    exit(1)

lines = result.stdout.strip().splitlines()

data = lines[1].split()

usage = data[4]

print("Disk usage:", usage)

percentage = int(usage.rstrip("%"))

if percentage >= 80:
    print("WARNING: Disk usage is high")
else:
    print("Disk usage is normal")

# Example: Check service
import subprocess

def check_service(service):

    result = subprocess.run(
        ["systemctl", "is-active", service],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{service}: RUNNING")
        return True

    print(f"{service}: NOT RUNNING")
    return False


check_service("sshd")
check_service("chronyd")

# Example: Linux health-check
import subprocess


def run_command(command):

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=30
    )

    if result.returncode == 0:
        return result.stdout.strip()

    print("Command failed:")
    print(result.stderr.strip())

    return None


print("===== HOSTNAME =====")
print(run_command(["hostname"]))

print("\n===== KERNEL =====")
print(run_command(["uname", "-r"]))

print("\n===== UPTIME =====")
print(run_command(["uptime"]))

print("\n===== MEMORY =====")
print(run_command(["free", "-m"]))

print("\n===== DISK =====")
print(run_command(["df", "-h", "/"]))

# Example: OpenShift automated health check
import subprocess


def run_oc(command):

    result = subprocess.run(
        ["oc"] + command,
        capture_output=True,
        text=True,
        timeout=60
    )

    if result.returncode != 0:
        print("ERROR:", result.stderr.strip())
        return None

    return result.stdout.strip()


print("===== OPENSHIFT NODES =====")
print(run_oc(["get", "nodes"]))

print("\n===== CLUSTER OPERATORS =====")
print(run_oc(["get", "co"]))

print("\n===== ALL PODS =====")
print(run_oc(["get", "pods", "-A"]))

# subprocess with grep
# Suppose you want:oc get pods -A | grep -i crash
import subprocess

oc = subprocess.Popen(
    ["oc", "get", "pods", "-A"],
    stdout=subprocess.PIPE,
    text=True
)

grep = subprocess.Popen(
    ["grep", "-i", "crash"],
    stdin=oc.stdout,
    stdout=subprocess.PIPE,
    text=True
)

oc.stdout.close()

output, _ = grep.communicate()

print(output)

# Better approach: Python filtering
# For many automation tasks, you don't actually need Linux grep.
# Instead:
import subprocess

result = subprocess.run(
    ["oc", "get", "pods", "-A"],
    capture_output=True,
    text=True
)

for line in result.stdout.splitlines():

    if "CrashLoopBackOff" in line:
        print(line)

# Exception handling
# For production DevOps scripts, handle errors properly.
import subprocess

try:

    result = subprocess.run(
        ["systemctl", "restart", "nginx"],
        capture_output=True,
        text=True,
        check=True
    )

    print("Nginx restarted successfully")

except subprocess.CalledProcessError as e:

    print("Command failed")
    print("Return code:", e.returncode)
    print("Error:", e.stderr)

except subprocess.TimeoutExpired:

    print("Command timed out")

# Example: server_health.py
import subprocess


def run_command(command):

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            print(f"[ERROR] {' '.join(command)}")
            print(result.stderr.strip())
            return None

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] {' '.join(command)}")
        return None


def main():

    print("===== SERVER HEALTH CHECK =====")

    hostname = run_command(["hostname"])
    kernel = run_command(["uname", "-r"])
    uptime = run_command(["uptime"])
    memory = run_command(["free", "-m"])
    disk = run_command(["df", "-h", "/"])

    print("\nHostname:")
    print(hostname)

    print("\nKernel:")
    print(kernel)

    print("\nUptime:")
    print(uptime)

    print("\nMemory:")
    print(memory)

    print("\nDisk:")
    print(disk)


if __name__ == "__main__":
    main()