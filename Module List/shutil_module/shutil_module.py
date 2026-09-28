# Python's shutil (shell utilities) module provides high-level operations for working with files and directories.
# For a DevOps engineer, shutil is especially useful for:
# File and directory backup
# Copying configuration files
# Moving files
# Deleting directories
# Creating deployment packages
# Disk-space monitoring
# Server maintenance scripts
# Log rotation/archiving
# Application deployment
# Infrastructure automation

# Important shutil functions
# copy()
# copy2()
# copyfile()
# copytree()
# move()
# rmtree()
# which()
# disk_usage()
# make_archive()
# unpack_archive()
# chown()
# get_archive_formats()
# get_unpack_formats()

################################################################################
# shutil.copy()
# Purpose
# Copies a file from one location to another.

# Syntax
# shutil.copy(source, destination)

# Example
import shutil

shutil.copy(
    "/etc/hosts",
    "/tmp/hosts"
)

print("File copied successfully")

# Example:2 Backup configuration
# Suppose you want to back up an NGINX configuration before modifying it.
import shutil

source = "/etc/nginx/nginx.conf"
backup = "/backup/nginx.conf"

shutil.copy(source, backup)

print("NGINX configuration backed up")
#######################################################################################
# shutil.copy2()
# copy2() copies a file and attempts to preserve metadata, such as modification time.

# Syntax
# shutil.copy2(source, destination)
# Example:
import shutil

shutil.copy2(
    "/etc/nginx/nginx.conf",
    "/backup/nginx.conf"
)
##########################################################################################
# shutil.copyfile()
# copyfile() copies only the contents of one file to another.

# Syntax
# shutil.copyfile(source, destination)
# Example:
import shutil

shutil.copyfile(
    "application.conf",
    "application.conf.bak"
)
# Important difference
# copyfile() does not preserve metadata such as permissions.

###################################################################################
# shutil.copytree()
# This is extremely useful in DevOps.
# It copies an entire directory tree.

# Syntax
# shutil.copytree(source, destination)
# Example:
import shutil

shutil.copytree(
    "/opt/myapp",
    "/backup/myapp"
)
# Equal to: cp -r /opt/myapp /backup/myapp

# Example: Application backup
import shutil
from datetime import datetime

source = "/opt/myapp"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

destination = f"/backup/myapp_{timestamp}"

shutil.copytree(source, destination)

print(f"Backup created: {destination}")
#####################################################################################
# copytree(..., dirs_exist_ok=True)
# By default, copytree() expects the destination directory not to already exist.
# Modern Python provides:
# dirs_exist_ok=True
import shutil

shutil.copytree(
    "/opt/myapp",
    "/backup/myapp",
    dirs_exist_ok=True
)
########################################################################################
# shutil.move()
# Moves a file or directory.
# Syntax
# shutil.move(source, destination)
# Example:
import shutil

shutil.move(
    "/tmp/application.log",
    "/var/log/application.log"
)
# Equal to: mv /tmp/application.log /var/log/application.log

###############################################################################################
# shutil.which()
# This is very useful for DevOps automation.
# It finds the executable path available in $PATH.

# Syntax
# shutil.which(command)
# Example:
import shutil

path = shutil.which("kubectl")

print(path)

# DevOps example — Check required tools
import shutil

commands = [
    "python",
    "git",
    "kubectl",
    "oc",
    "docker",
    "ansible"
]

for command in commands:
    path = shutil.which(command)

    if path:
        print(f"[OK] {command}: {path}")
    else:
        print(f"[MISSING] {command}")

################################################################################################
# shutil.make_archive()
# Creates an archive such as:
# .tar
# .tar.gz
# .zip
# Syntax
shutil.make_archive(
    base_name,
    format,
    root_dir
)
# Example:
import shutil

shutil.make_archive(
    "/backup/myapp",
    "gztar",
    "/opt/myapp"
)
# Backup application
import shutil
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup_name = f"/backup/myapp_{timestamp}"

shutil.make_archive(
    backup_name,
    "gztar",
    "/opt/myapp"
)

print("Backup created")

########################################################################################
# shutil.unpack_archive()
# Extracts an archive.

# Syntax
shutil.unpack_archive(
    archive,
    destination
)
# Example:
import shutil

shutil.unpack_archive(
    "/backup/myapp.tar.gz",
    "/opt/restore"
)
# Equivalent conceptually to: tar -xzf myapp.tar.gz -C /opt/restore

# backup script
import shutil
import os
from datetime import datetime

SOURCE = "/opt/myapp"
BACKUP_DIR = "/backup"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup_file = os.path.join(
    BACKUP_DIR,
    f"myapp_{timestamp}"
)

# Check source
if not os.path.exists(SOURCE):
    print("ERROR: Application directory does not exist")
    exit(1)

# Create archive
archive = shutil.make_archive(
    backup_file,
    "gztar",
    SOURCE
)

print(f"Backup created: {archive}")

# Check disk
total, used, free = shutil.disk_usage(BACKUP_DIR)

usage = (used / total) * 100

print(f"Backup disk usage: {usage:.2f}%")

if usage >= 90:
    print("WARNING: Backup disk is almost full")
    