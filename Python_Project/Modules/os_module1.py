# Requirement

# Check a server's application directory:

# Does /opt/app exist?
# List files.
# Find log files.
# Check their size.
# Create a backup directory.
import os

app_dir = "/opt/app"
backup_dir = "/opt/app_backup"

# 1. Check application directory
if not os.path.isdir(app_dir):

    print("Application directory does not exist")

else:

    print("Application directory exists")

    # 2. List files
    for file in os.listdir(app_dir):

        full_path = os.path.join(app_dir, file)

        print("Found:", full_path)

        # 3. Check log files
        if os.path.isfile(full_path) and file.endswith(".log"):

            # 4. Check size
            size_mb = os.path.getsize(full_path) / (1024 * 1024)

            print(
                f"Log: {file}, "
                f"Size: {size_mb:.2f} MB"
            )

# 5. Create backup directory
os.makedirs(backup_dir, exist_ok=True)

print("Backup directory ready")