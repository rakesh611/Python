# Check Environment
import os

environment = os.getenv(
    "ENVIRONMENT",
    "development"
)

app_name = os.getenv(
    "APP_NAME",
    "unknown"
)

hostname = os.getenv(
    "HOSTNAME",
    "unknown"
)

print("Application :", app_name)
print("Environment :", environment)
print("Hostname    :", hostname)