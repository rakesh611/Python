# The Python pathlib module is used to work with files and directories.
# For a DevOps engineer, pathlib is very useful for:
# Checking whether files/directories exist
# Creating directories
# Creating, reading, and writing files
# Finding log/config files
# Managing backup directories
# Searching files recursively
# Getting file size and metadata
# Building Linux paths safely
# Automating deployment and cleanup tasks

# The biggest advantage is that pathlib provides an object-oriented way of handling paths, instead of manually manipulating strings.
# Import pathlib
from pathlib import Path
# Example:
from pathlib import Path

path = Path("/var/log/messages")

print(path)
# Output:
# /var/log/messages
###########################################################################################################
# Why use pathlib?
# Traditional approach:
log_file = "/var/log/app/app.log"

if os.path.exists(log_file):
    print("File exists")
# Using pathlib:
from pathlib import Path

log_file = Path("/var/log/app/app.log")

if log_file.exists():
    print("File exists")
# pathlib makes filesystem automation cleaner and easier to read.
#########################################################################################################
# Important pathlib Classes
# The most important class is:
# Path
# Import:
from pathlib import Path
#########################################################################################################
# Path.cwd()
# cwd() means Current Working Directory.
from pathlib import Path

current_dir = Path.cwd()

print(current_dir)
# Example output:/home/rakesh/devops
# example:
from pathlib import Path

workspace = Path.cwd()

print("Deployment workspace:", workspace)

#########################################################################################################
# Path.home()
# Returns the user's home directory.
from pathlib import Path

home = Path.home()

print(home)
# Output:/home/rakesh

# Example: Find the user's SSH directory:
from pathlib import Path

ssh_dir = Path.home() / ".ssh"

print(ssh_dir)
# Output:/home/rakesh/.ssh
# This is one of the most useful features of pathlib.

##############################################################################################################
# Path joining using /
# You can join paths using /.
from pathlib import Path

base = Path("/opt/application")

config = base / "config" / "app.conf"

print(config)
# Output:/opt/application/config/app.conf
# Instead of:  config = "/opt/application/" + "config/" + "app.conf"
# Use:  config = Path("/opt/application") / "config" / "app.conf"

# Example: 
from pathlib import Path

app_dir = Path("/opt/myapp")

config_file = app_dir / "config" / "application.yaml"
log_file = app_dir / "logs" / "application.log"

print("Config:", config_file)
print("Log:", log_file)

##################################################################################################################
# exists()
# Checks whether a file or directory exists.
from pathlib import Path

path = Path("/etc/hosts")

if path.exists():
    print("Path exists")
else:
    print("Path does not exist")

# Example: 2
from pathlib import Path

kubeconfig = Path.home() / ".kube" / "config"

if kubeconfig.exists():
    print("Kubeconfig exists")
else:
    print("Kubeconfig not found")

#####################################################################################################################
# is_file()
# Checks whether the path is a regular file.
from pathlib import Path

path = Path("/etc/hosts")

if path.is_file():
    print("It is a file")
# Example:2
from pathlib import Path

config = Path("/etc/ssh/sshd_config")

if config.is_file():
    print("SSH configuration file exists")
else:
    print("SSH configuration file missing")

#####################################################################################################################
# is_dir()
# Checks whether the path is a directory.
from pathlib import Path

path = Path("/var/log")

if path.is_dir():
    print("It is a directory")
# Example:2
from pathlib import Path

backup = Path("/backup")

if backup.is_dir():
    print("Backup directory exists")
else:
    print("Backup directory missing")

#####################################################################################################################
# mkdir()
# Creates a directory.
from pathlib import Path

path = Path("/tmp/devops")

path.mkdir()
# Directory:/tmp/devops is created
# Problem If the parent directory doesn't exist:Path("/tmp/devops/logs").mkdir() may fail.
# Use:Path("/tmp/devops/logs").mkdir(parents=True)

#####################################################################################################################
# mkdir(parents=True)
# Creates parent directories automatically.
from pathlib import Path

log_dir = Path("/tmp/devops/application/logs")

log_dir.mkdir(parents=True, exist_ok=True)
# Example: 
from pathlib import Path

backup_dir = Path("/backup/application/2026/09/28")

backup_dir.mkdir(
    parents=True,
    exist_ok=True
)

print("Backup directory ready")
