# The Python os module is one of the most important standard-library modules for a DevOps engineer.
# It allows Python programs to interact with the Linux/Unix operating system, including:

# Files and directories
# Environment variables
# Processes
# File permissions
# Current working directory
# Operating-system information
# Path-related operations
# Running shell commands

# You don't need to install it separately.
# import os

# As a DevOps engineer, you frequently perform tasks such as:
# Check whether a file exists
# Create backup directory
# Read environment variables
# Check disk/log directories
# Change file permissions
# Execute Linux commands
# Automate repetitive administration
##########################################

# Important os functions for DevOps
# | Function             | Purpose                          | DevOps Usage          |
# | -------------------- | -------------------------------- | --------------------- |
# | `os.getcwd()`        | Get current directory            | Automation scripts    |
# | `os.chdir()`         | Change directory                 | Script navigation     |
# | `os.listdir()`       | List files/directories           | Log/file inspection   |
# | `os.mkdir()`         | Create directory                 | Automation            |
# | `os.makedirs()`      | Create nested directories        | Backup/deployment     |
# | `os.remove()`        | Delete file                      | Cleanup               |
# | `os.rmdir()`         | Delete empty directory           | Cleanup               |
# | `os.rename()`        | Rename/move file                 | Log rotation          |
# | `os.environ`         | Access environment variables     | CI/CD                 |
# | `os.getenv()`        | Get environment variable         | Secrets/config        |
# | `os.putenv()`        | Set environment variable         | Runtime configuration |
# | `os.path.exists()`   | Check path                       | Validation            |
# | `os.path.isfile()`   | Check file                       | File validation       |
# | `os.path.isdir()`    | Check directory                  | Directory validation  |
# | `os.path.join()`     | Build path                       | Portable scripts      |
# | `os.path.basename()` | Get filename                     | Log processing        |
# | `os.path.dirname()`  | Get directory                    | Path processing       |
# | `os.path.abspath()`  | Get absolute path                | Automation            |
# | `os.path.getsize()`  | Get file size                    | Log monitoring        |
# | `os.stat()`          | File metadata                    | Permissions/ownership |
# | `os.chmod()`         | Change permissions               | Linux administration  |
# | `os.system()`        | Execute shell command            | Simple automation     |
# | `os.getpid()`        | Get process ID                   | Process monitoring    |
# | `os.cpu_count()`     | Get CPU count                    | System information    |
# | `os.getuid()`        | Get user ID                      | Linux scripts         |
# | `os.getgid()`        | Get group ID                     | Linux scripts         |
# | `os.walk()`          | Recursively traverse directories | Log/file scanning     |

##################################################################################

# os.getcwd() — Get Current working Directory
# Example:
import os

current_dir = os.getcwd()

print("Current directory:", current_dir)
# Output: it gives current working directory

#####################################################################################
# os.chdir() — Change Directory
import os

os.chdir("/var/log")

print(os.getcwd())
# Output: /var/log

# Example:
import os

os.chdir("/var/log")

files = os.listdir()

print("Log files:")
for file in files:
    print(file)
####################################################

# os.listdir() — List Files
import os

log_dir = "/var/log"

for file in os.listdir(log_dir):

    if file.endswith(".log"):
        print("Log file:", file)

######################################################
# os.mkdir() — Create Directory
import os

if not os.path.exists("/backup"):
    os.mkdir("/backup")

print("Backup directory ready")

#######################################################
# os.makedirs() — Create Nested Directories
import os

os.makedirs(
    "/backup/nginx/2026/september",
    exist_ok=True
)

# exist_ok=True means:
# Don't generate an error if the directory already exists.

########################################################
# os.remove() — Delete File
import os

file = "/tmp/test.log"

if os.path.exists(file):
    os.remove(file)
    print("File deleted")
else:
    print("File does not exist")

#######################################################
# os.rmdir() — Delete Empty Directory
import os

os.rmdir("/tmp/test")
# only removes empty directory.
#########################################################
# os.rename() — Rename/Move
import os

old_log = "/var/log/application.log"
backup_log = "/var/log/application.log.old"

if os.path.exists(old_log):
    os.rename(old_log, backup_log)

print("Log rotated")
############################################################
# os.path.exists() — Check Whether Path Exists
# This is extremely important in automation.
import os

config = "/etc/kubernetes/kubelet.conf"

if os.path.exists(config):
    print("Configuration exists")
else:
    print("Configuration missing")

##############################################################
# os.path.isfile() — Check File
import os

log_file = "/var/log/messages"

if os.path.isfile(log_file):
    print("Log file exists")
else:
    print("Log file missing")

###############################################################
# os.path.isdir() — Check Directory
import os

log_dir = "/var/log"

if os.path.isdir(log_dir):
    print("Starting log collection...")
else:
    print("Log directory not found")

################################################################
# os.path.join() — Join Paths
# This is one of the most important functions for writing portable scripts.
import os

base_dir = "/backup"
server = "web01"
log_file = "nginx.log"

path = os.path.join(
    base_dir,
    server,
    log_file
)

print(path)
# Output: /backup/web01/nginx.log
##############################################################################
# os.path.basename() — Get Filename
import os

path = "/var/log/nginx/access.log"

filename = os.path.basename(path)

print(filename)

#############################################################################
# os.path.dirname() — Get Directory
import os

path = "/var/log/nginx/access.log"

directory = os.path.dirname(path)

print(directory)
# Output: /var/log/nginx
################################################################################
# os.path.abspath() — Absolute Path
import os

path = "deploy.yaml"

absolute_path = os.path.abspath(path)

print(absolute_path)

################################################################################
# os.path.getsize() — File Size
import os

file = "/var/log/messages"

size = os.path.getsize(file)

print("Size:", size, "bytes")

# Convert to MB
import os

file = "/var/log/messages"

size = os.path.getsize(file)

size_mb = size / (1024 * 1024)

print(f"Size: {size_mb:.2f} MB")

# Example:
import os

log_file = "/var/log/application.log"

if os.path.exists(log_file):

    size_mb = os.path.getsize(log_file) / (1024 * 1024)

    if size_mb > 500:
        print("WARNING: Log file is larger than 500 MB")
    else:
        print("Log size is normal")

################################################################################
# os.environ — Environment Variables
# Linux
# export ENV=production
import os

print(os.environ["ENV"])
# Output: production
################################################################################
# os.getenv() — Get Environment Variable
# I recommend using getenv() when the variable might not exist.
import os

env = os.getenv("ENV")

print(env)
# If it doesn't exist:
None

# You can provide a default:
import os

env = os.getenv("ENV", "development")

print(env)
# If ENV isn't defined:
# development

###############################################################################
# Set Environment Variable
# You can set an environment variable for the current Python process:
import os

os.environ["ENVIRONMENT"] = "production"

print(os.getenv("ENVIRONMENT"))
# Output: production

#############################################################################
# os.cpu_count() — Number of CPUs
import os

cpu = os.cpu_count()

if cpu >= 8:
    print("Node has sufficient CPU")
else:
    print("Node has low CPU capacity")
###############################################################################
# os.getpid() — Process ID
import os

print("PID:", os.getpid())
##############################################################################
# os.getuid() — User ID
import os

print("UID:", os.getuid())
# Example:
import os

if os.getuid() == 0:
    print("Running as root")
else:
    print("Not running as root")
################################################################################
# os.getgid() — Group ID
import os

print("GID:", os.getgid())
##############################################################################
# os.chmod() — Change File Permissions
import os

os.chmod(
    "deploy.sh",
    0o755
)
# The 0o indicates an octal number.
# Example:
import os

script = "/opt/scripts/deploy.sh"

if os.path.exists(script):
    os.chmod(script, 0o755)
    print("Deployment script is executable")

################################################################
# os.stat() — File Information
# os.stat() provides metadata about a file.
import os

info = os.stat("/var/log/messages")

print(info)
# You can access specific information:
import os

info = os.stat("/var/log/messages")

print("Size:", info.st_size)
print("UID:", info.st_uid)
print("GID:", info.st_gid)
print("Mode:", info.st_mode)
# This is useful for Linux administration and troubleshooting.

#################################################################################
# os.walk() — Recursively Search Directories
import os

for root, directories, files in os.walk("/opt/application"):

    print("Directory:", root)

    for file in files:
        print("File:", file)

# Example: Find All .log Files
import os

for root, directories, files in os.walk("/var/log"):

    for file in files:

        if file.endswith(".log"):

            full_path = os.path.join(root, file)

            print(full_path)
# Example: Find Large Log Files
import os

log_directory = "/var/log"

for root, directories, files in os.walk(log_directory):

    for file in files:

        full_path = os.path.join(root, file)

        if os.path.isfile(full_path):

            size_mb = os.path.getsize(full_path) / (1024 * 1024)

            if size_mb > 100:
                print(
                    f"Large log: {full_path} "
                    f"Size: {size_mb:.2f} MB"
                )