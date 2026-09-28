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

#####################################################################################################################
# rmdir()
# Removes an empty directory.

from pathlib import Path

directory = Path("/tmp/test")

directory.rmdir()
# Important: rmdir() cannot remove a directory containing files.
# This will fail: directory.rmdir()
# For recursive deletion, Python also provides shutil.rmtree().
#################################################################################################################
# touch()
# Creates an empty file.
from pathlib import Path

file = Path("/tmp/test.txt")

file.touch()
# Example:2
from pathlib import Path

health_file = Path("/tmp/application_healthy")

health_file.touch()

print("Health marker created")
###################################################################################################################
# unlink()
# Deletes a file.
from pathlib import Path

file = Path("/tmp/test.txt")

file.unlink()
# Safe version
from pathlib import Path

file = Path("/tmp/test.txt")

if file.exists():
    file.unlink()
    print("File deleted")
else:
    print("File does not exist")

# Remove an old deployment marker:
from pathlib import Path

marker = Path("/opt/app/deployment_failed")

if marker.exists():
    marker.unlink()
    print("Old deployment marker removed")

########################################################################################################################
# write_text()
# Writes text into a file.
from pathlib import Path

file = Path("/tmp/app.txt")

file.write_text("Application started\n")
# Read it: 
print(file.read_text())
# Output: Application started

#######################################################################################################################
# read_text()
# Reads text from a file.
from pathlib import Path

config = Path("/etc/hostname")

hostname = config.read_text()

print(hostname)
# Read an application configuration:
from pathlib import Path

config = Path("/opt/myapp/config/app.conf")

if config.exists():
    content = config.read_text()

    print(content)

#######################################################################################################################
# write_bytes()
# Writes binary data.
from pathlib import Path

file = Path("/tmp/data.bin")

file.write_bytes(b"Hello")
# Useful for:
# Binary files
# Certificates
# Images
# Compressed data

# For normal configuration/log files, use:
write_text()

#######################################################################################################################
# read_bytes()
# Reads binary data.
from pathlib import Path

file = Path("/tmp/data.bin")

data = file.read_bytes()

print(data)
# Output: b'Hello'
###################################################################################################################
# open()
# Path.open() works similarly to Python's built-in open().
from pathlib import Path

log_file = Path("/var/log/application.log")

with log_file.open("r") as file:
    data = file.read()

print(data)
# Read line by line
from pathlib import Path

log_file = Path("/var/log/application.log")

with log_file.open("r") as file:
    for line in file:
        print(line.strip())
# This is useful for large log files because you don't need to load the entire file into memory.
# name
# Returns the filename.
from pathlib import Path

path = Path("/var/log/application.log")

print(path.name)
# Output: application.log
# Example: 
from pathlib import Path

config = Path("/etc/nginx/nginx.conf")

print("File:", config.name)
# Output: File: nginx.conf

#############################################################################################################################
# stem
# Returns the filename without extension.
from pathlib import Path

file = Path("/var/log/application.log")

print(file.stem)
# Output: application
# Useful when generating backup names.
from pathlib import Path

log = Path("/var/log/application.log")

backup = log.parent / f"{log.stem}.backup{log.suffix}"

print(backup)
# Output: /var/log/application.backup.log
######################################################################################################################
# suffix
# Returns the file extension.
from pathlib import Path

file = Path("/etc/nginx/nginx.conf")

print(file.suffix)
# Output: .conf
# Another example:
file = Path("/tmp/application.log")

print(file.suffix)
# Output: .log
##############################################################################################################################
# suffixes
# Returns multiple extensions.
from pathlib import Path

file = Path("/backup/app.tar.gz")

print(file.suffixes)
# Output: ['.tar', '.gz']
# Useful for compressed backup files.

#############################################################################################################################
# parent
# Returns the parent directory.
from pathlib import Path

file = Path("/var/log/application/app.log")

print(file.parent)
# Output: /var/log/application
# Example: 
from pathlib import Path

config = Path("/etc/nginx/nginx.conf")

print("Configuration directory:", config.parent)
################################################################################################################################
# parents
# Returns all parent directories.
from pathlib import Path

path = Path("/opt/application/config/app.yaml")

print(list(path.parents))
# Example:
# /opt/application/config
# /opt/application
# /opt
# /

#####################################################################################################################################
# absolute()
# Returns an absolute path.
from pathlib import Path

path = Path("app/config.yaml")

print(path.absolute())
# Example: /home/rakesh/app/config.yaml
#######################################################################################################################################
# resolve()
# Resolves the path to its absolute/canonical form.
from pathlib import Path

path = Path("../app/config.yaml")

print(path.resolve())
# Example:
from pathlib import Path

config = Path("../config/app.yaml")

real_path = config.resolve()

print("Real path:", real_path)

##########################################################################################################################################
# relative_to()
# Finds a path relative to another path.
from pathlib import Path

base = Path("/opt/application")

file = Path("/opt/application/config/app.yaml")

print(file.relative_to(base))
# Output: config/app.yaml
###########################################################################################################################################
# with_name()
# Changes the filename while keeping the same directory.
from pathlib import Path

file = Path("/etc/nginx/nginx.conf")

new_file = file.with_name("nginx.conf.backup")

print(new_file)

# Output: /etc/nginx/nginx.conf.backup
###########################################################################################################################################
# with_suffix()
# Changes the file extension.
from pathlib import Path

file = Path("/tmp/application.txt")

new_file = file.with_suffix(".backup")

print(new_file)
# Output: /tmp/application.backup
# Example:2
from pathlib import Path

config = Path("/etc/nginx/nginx.conf")

backup = config.with_suffix(".conf.backup")

print(backup)
###########################################################################################
# iterdir()
# Lists files and directories inside a directory.
from pathlib import Path

directory = Path("/var/log")

for item in directory.iterdir():
    print(item)
# Possible Output:
# /var/log/messages
# /var/log/secure
# /var/log/httpd
# /var/log/audit
