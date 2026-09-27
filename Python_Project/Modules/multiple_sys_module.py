import sys
import platform


# --------------------------------------------------
# 1. Check command-line arguments
# --------------------------------------------------

if len(sys.argv) != 2:
    print("Usage: python3 deploy_check.py <environment>")
    print("Example: python3 deploy_check.py production")
    sys.exit(1)


environment = sys.argv[1]


# --------------------------------------------------
# 2. Validate environment
# --------------------------------------------------

allowed_environments = ["dev", "staging", "production"]

if environment not in allowed_environments:
    sys.stderr.write(
        f"ERROR: Invalid environment: {environment}\n"
    )
    sys.exit(1)


# --------------------------------------------------
# 3. Display Python information
# --------------------------------------------------

print("========== Environment Information ==========")

print("Python version:")
print(sys.version)

print("Python executable:")
print(sys.executable)

print("Platform:")
print(sys.platform)

print("Operating system:")
print(platform.system())

print("Python prefix:")
print(sys.prefix)


# --------------------------------------------------
# 4. Deployment information
# --------------------------------------------------

print("\n========== Deployment ==========")

print(f"Target environment: {environment}")

print("Deployment validation successful")

sys.exit(0)

# Run:python3 deploy_check.py production
# Possible output:
# ========== Environment Information ==========

# Python version:
# 3.12.4 ...

# Python executable:
# /usr/bin/python3

# Platform:
# linux

# Operating system:
# Linux

# Python prefix:
# /usr

# ========== Deployment ==========

# Target environment: production

# Deployment validation successful