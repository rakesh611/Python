# Python `logging` Module — Complete DevOps Guide

## 1. What is the `logging` module?

Python's built-in `logging` module is used to record events that happen while a program or automation script is running.

For a DevOps engineer, logging is useful for:

- Deployment automation
- Linux server monitoring
- Kubernetes/OpenShift automation
- CI/CD pipelines
- Backup scripts
- Docker operations
- API automation
- Troubleshooting and RCA
- Monitoring infrastructure health

Instead of using only:

```python
print("Deployment started")
```

we can use:

```python
import logging

logging.info("Deployment started")
```

Logging provides additional capabilities such as:

- Severity levels
- Timestamps
- Log files
- Log rotation
- Exception tracebacks
- Multiple output destinations
- Named loggers
- Structured logging

---

# 2. Why use logging instead of `print()`?

## Using `print()`

```python
print("Deployment started")
print("Deployment failed")
```

Problems with `print()`:

- No standard severity level
- No automatic timestamp
- Difficult to manage large applications
- No built-in log rotation
- Exception information is not automatically captured
- Difficult to send different messages to different destinations

## Using `logging`

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

logging.info("Deployment started")
logging.error("Deployment failed")
```

Example:

```text
2026-10-05 08:30:10,123 INFO: Deployment started
2026-10-05 08:30:15,456 ERROR: Deployment failed
```

---

# 3. Logging architecture

The basic logging architecture is:

```text
Python Application
       |
       v
     Logger
       |
       v
   Log Record
       |
       v
    Handler
       |
       +-------------------+
       |                   |
       v                   v
    Console              File
       |                   |
       v                   v
 stdout/stderr       application.log
```

The important components are:

| Component | Purpose |
|---|---|
| Logger | Application/module creates log messages |
| Log level | Defines severity |
| Handler | Decides where the log goes |
| Formatter | Defines log message format |
| Filter | Allows or blocks selected log records |
| LogRecord | Internal object containing event information |

---

# 4. Logging levels

Python provides five commonly used logging levels:

| Level | Value | Purpose |
|---|---:|---|
| `DEBUG` | 10 | Detailed troubleshooting information |
| `INFO` | 20 | Normal operational information |
| `WARNING` | 30 | Potential problem |
| `ERROR` | 40 | Operation failed |
| `CRITICAL` | 50 | Very serious failure |

The hierarchy is:

```text
DEBUG
  |
  v
INFO
  |
  v
WARNING
  |
  v
ERROR
  |
  v
CRITICAL
```

If the logger is configured with:

```python
level=logging.INFO
```

then `DEBUG` messages are normally not displayed.

---

# 5. `logging.debug()`

`debug()` is used for detailed troubleshooting information.

```python
import logging

logging.basicConfig(level=logging.DEBUG)

server = "web01"
cpu_usage = 72

logging.debug(
    "Checking server=%s CPU=%s%%",
    server,
    cpu_usage
)
```

Typical DevOps use cases:

- Debugging deployment scripts
- Displaying command output
- Printing variables during troubleshooting
- Debugging API requests
- Investigating Kubernetes problems

Example:

```python
logging.debug("kubectl command: %s", command)
logging.debug("API response: %s", response)
```

Do not normally enable very verbose debug logs in production unless troubleshooting.

---

# 6. `logging.info()`

`info()` is used for normal operational events.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Deployment started")
logging.info("Docker image pulled")
logging.info("Deployment completed successfully")
```

Typical DevOps messages:

```text
INFO - Backup started
INFO - Kubernetes deployment created
INFO - Health check passed
INFO - Docker image pulled successfully
```

---

# 7. `logging.warning()`

`warning()` is used when something requires attention but is not necessarily a failure.

```python
import logging

logging.basicConfig(level=logging.INFO)

disk_usage = 85

if disk_usage > 80:
    logging.warning(
        "Disk usage is high: %s%%",
        disk_usage
    )
```

Output:

```text
WARNING - Disk usage is high: 85%
```

DevOps examples:

- Disk usage above 80%
- Memory usage is high
- TLS certificate is nearing expiry
- Kubernetes replicas are below desired count
- Backup storage is almost full

---

# 8. `logging.error()`

`error()` is used when an operation fails.

```python
import logging

logging.basicConfig(level=logging.INFO)

try:
    open("/tmp/missing-file.txt")
except FileNotFoundError:
    logging.error(
        "Required configuration file was not found"
    )
```

Output:

```text
ERROR - Required configuration file was not found
```

DevOps examples:

```python
logging.error("Deployment failed")
logging.error("Database connection failed")
logging.error("Backup failed")
```

---

# 9. `logging.critical()`

`critical()` is used for very serious failures.

```python
import logging

logging.basicConfig(level=logging.INFO)

database_available = False

if not database_available:
    logging.critical(
        "Database is completely unavailable"
    )
```

Typical DevOps situations:

- Production database unavailable
- Kubernetes control plane unavailable
- Filesystem critically full
- Disaster recovery failure
- Critical configuration missing

---

# 10. `logging.exception()`

`exception()` is extremely important for DevOps troubleshooting.

It logs:

1. Your error message
2. Exception type
3. Full traceback

Use it inside an `except` block.

```python
import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s: %(message)s"
)

try:
    result = 10 / 0

except ZeroDivisionError:
    logging.exception(
        "Failed to calculate deployment percentage"
    )
```

Example output:

```text
ERROR Failed to calculate deployment percentage
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
```

Compare:

```python
logging.error("Deployment failed")
```

with:

```python
logging.exception("Deployment failed")
```

The second one gives you the traceback, which is much more useful for RCA.

---

# 11. `logging.log()`

`log()` allows you to select the log level dynamically.

```python
import logging

logging.basicConfig(level=logging.INFO)

level = logging.WARNING

logging.log(
    level,
    "Disk usage is high"
)
```

This is useful when the logging level is stored in a variable.

Equivalent example:

```python
logging.warning("Disk usage is high")
```

---

# 12. `logging.basicConfig()`

`basicConfig()` is used to configure the basic logging system.

Example:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

logging.info("Automation started")
```

Important arguments:

| Argument | Purpose |
|---|---|
| `level` | Minimum logging level |
| `format` | Log message format |
| `filename` | Log file path |
| `filemode` | File mode |
| `datefmt` | Timestamp format |
| `handlers` | Logging handlers |
| `encoding` | File encoding |

---

# 13. Logging to a file

For DevOps automation, persistent logs are often required.

```python
import logging

logging.basicConfig(
    filename="/tmp/deployment.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

logging.info("Deployment started")
logging.info("Image pulled successfully")
logging.info("Deployment completed")
```

View the log:

```bash
cat /tmp/deployment.log
```

Follow the log:

```bash
tail -f /tmp/deployment.log
```

---

# 14. `filemode`

By default, logs are generally appended to the file.

```python
import logging

logging.basicConfig(
    filename="/tmp/deployment.log",
    level=logging.INFO,
    filemode="a"
)

logging.info("New deployment started")
```

`a` means append.

To overwrite the file:

```python
logging.basicConfig(
    filename="/tmp/deployment.log",
    level=logging.INFO,
    filemode="w"
)
```

For operational logs, append mode is normally preferred.

---

# 15. Log formatting

A useful DevOps format is:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)

logging.info("Server health check passed")
```

Example:

```text
2026-10-05 08:35:10,123 INFO root: Server health check passed
```

Important format fields:

| Format | Meaning |
|---|---|
| `%(asctime)s` | Date/time |
| `%(levelname)s` | Logging level |
| `%(name)s` | Logger name |
| `%(message)s` | Message |
| `%(filename)s` | Source filename |
| `%(module)s` | Module name |
| `%(funcName)s` | Function name |
| `%(lineno)d` | Source line |
| `%(process)d` | Process ID |
| `%(thread)d` | Thread ID |

Example:

```python
logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s %(levelname)s "
        "%(filename)s:%(lineno)d "
        "%(message)s"
    )
)
```

---

# 16. Use variables safely in log messages

Prefer:

```python
deployment = "nginx"

logging.info(
    "Deployment %s started",
    deployment
)
```

instead of:

```python
logging.info(
    f"Deployment {deployment} started"
)
```

The logging module can avoid unnecessary string formatting when the message will not be emitted because of the configured log level.

---

# 17. `logging.getLogger()`

For real projects, create a named logger.

```python
import logging

logger = logging.getLogger(__name__)
```

Then:

```python
logger.info("Deployment started")
logger.warning("Disk usage is high")
logger.error("Deployment failed")
```

Using:

```python
logging.getLogger(__name__)
```

is a common best practice in multi-module Python applications.

Example:

```text
INFO deployment: Deployment started
INFO monitoring: Health check started
```

The logger name helps identify which module generated the message.

---

# 18. Logger methods

After:

```python
logger = logging.getLogger(__name__)
```

you can use:

```python
logger.debug()
logger.info()
logger.warning()
logger.error()
logger.critical()
logger.exception()
logger.log()
```

Example:

```python
logger.info("Starting backup")
logger.warning("Backup directory is almost full")
logger.error("Backup failed")
```

---

# 19. `setLevel()`

`setLevel()` sets the minimum level.

```python
logger.setLevel(logging.DEBUG)
```

Example:

```python
logger.setLevel(logging.INFO)
```

This means:

```text
DEBUG      -> ignored
INFO       -> logged
WARNING    -> logged
ERROR      -> logged
CRITICAL   -> logged
```

---

# 20. Handlers

A Handler decides where logs are sent.

Common handlers:

| Handler | Purpose |
|---|---|
| `StreamHandler` | Console/stdout/stderr |
| `FileHandler` | Log file |
| `RotatingFileHandler` | Size-based rotation |
| `TimedRotatingFileHandler` | Time-based rotation |
| `NullHandler` | Discards logs |

---

# 21. `StreamHandler`

`StreamHandler` sends logs to a stream, commonly the console.

```python
import logging

logger = logging.getLogger("openshift")
logger.setLevel(logging.INFO)

console = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s"
)

console.setFormatter(formatter)
logger.addHandler(console)

logger.info("Checking OpenShift cluster")
```

This is particularly useful for:

- Jenkins
- GitLab CI/CD
- GitHub Actions
- Docker
- Kubernetes
- OpenShift

Container platforms can collect stdout/stderr and forward the logs to centralized logging systems.

---

# 22. `FileHandler`

`FileHandler` writes logs to a file.

```python
import logging

logger = logging.getLogger("backup")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    "/tmp/backup.log"
)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s: %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("Backup started")
logger.info("Backup completed")
```

---

# 23. Multiple handlers

A logger can send logs to multiple destinations.

```python
import logging

logger = logging.getLogger("deployment")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
file_handler = logging.FileHandler(
    "/tmp/deployment.log"
)

console.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s: %(message)s"
)

console.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file_handler)

logger.debug("kubectl command prepared")
logger.info("Deployment started")
logger.error("Deployment failed")
```

Conceptually:

```text
                 +--> Console
                 |
Logger ----------+
                 |
                 +--> deployment.log
```

Here:

```text
Console -> INFO and above
File    -> DEBUG and above
```

---

# 24. `RotatingFileHandler`

This is very useful for production DevOps automation.

Without log rotation:

```text
deployment.log
```

could grow indefinitely.

Use:

```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("deployment")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "/tmp/deployment.log",
    maxBytes=5 * 1024 * 1024,
    backupCount=3
)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Deployment started")
```

When the log reaches approximately 5 MB, it rotates:

```text
deployment.log
deployment.log.1
deployment.log.2
deployment.log.3
```

---

# 25. `TimedRotatingFileHandler`

Use this when logs should rotate based on time.

```python
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("backup")
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(
    "/tmp/backup.log",
    when="midnight",
    interval=1,
    backupCount=7
)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Backup completed")
```

This can maintain approximately seven days of rotated logs.

Useful for:

- Daily backup jobs
- Daily reports
- Infrastructure monitoring
- Scheduled automation

---

# 26. `Formatter`

`Formatter` controls the appearance of log messages.

```python
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s: %(message)s"
)
```

Attach it to a handler:

```python
handler.setFormatter(formatter)
```

Example output:

```text
2026-10-05 08:40:10 INFO backup: Backup completed
```

---

# 27. `addHandler()`

Adds a handler to a logger.

```python
logger.addHandler(file_handler)
logger.addHandler(console_handler)
```

---

# 28. `removeHandler()`

Removes a handler.

```python
logger.removeHandler(file_handler)
```

This is useful when logging destinations need to be changed dynamically.

---

# 29. Exception logging with `exc_info`

You can explicitly include exception information.

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    value = int("abc")

except ValueError:
    logging.error(
        "Invalid number received",
        exc_info=True
    )
```

However, inside an `except` block, this is usually simpler:

```python
except ValueError:
    logging.exception("Invalid number received")
```

---

# 30. DevOps Example: Linux disk monitoring

A practical infrastructure monitoring script:

```python
import logging
import shutil

logging.basicConfig(
    filename="/tmp/disk_monitor.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

path = "/"

try:
    total, used, free = shutil.disk_usage(path)

    usage_percent = (used / total) * 100

    logging.info(
        "Disk usage for %s: %.2f%%",
        path,
        usage_percent
    )

    if usage_percent >= 90:
        logging.critical(
            "Disk usage is critical: %.2f%%",
            usage_percent
        )

    elif usage_percent >= 80:
        logging.warning(
            "Disk usage is high: %.2f%%",
            usage_percent
        )

    else:
        logging.info(
            "Disk usage is healthy"
        )

except Exception:
    logging.exception(
        "Disk monitoring failed"
    )
```

Run:

```bash
python3 disk_monitor.py
```

View:

```bash
tail -f /tmp/disk_monitor.log
```

---

# 31. DevOps Example: Kubernetes deployment monitoring

```python
import logging
import subprocess

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)


def check_deployment(namespace, deployment):

    logging.info(
        "Checking deployment %s in namespace %s",
        deployment,
        namespace
    )

    try:

        result = subprocess.run(
            [
                "kubectl",
                "get",
                "deployment",
                deployment,
                "-n",
                namespace
            ],
            capture_output=True,
            text=True,
            check=True
        )

        logging.info(
            "Deployment check successful"
        )

        logging.debug(
            "kubectl output: %s",
            result.stdout.strip()
        )

    except FileNotFoundError:

        logging.error(
            "kubectl command was not found"
        )

    except subprocess.CalledProcessError:

        logging.exception(
            "Failed to check deployment %s",
            deployment
        )


check_deployment(
    "production",
    "nginx"
)
```

This pattern is useful for Kubernetes/OpenShift automation.

---

# 32. DevOps Example: OpenShift health check

```python
import logging
import subprocess

logger = logging.getLogger("openshift")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)


def oc_health_check():

    logger.info(
        "Starting OpenShift health check"
    )

    try:

        result = subprocess.run(
            ["oc", "get", "clusterversion"],
            capture_output=True,
            text=True,
            check=True
        )

        logger.info(
            "OpenShift cluster is reachable"
        )

        logger.debug(
            "oc output: %s",
            result.stdout.strip()
        )

    except FileNotFoundError:

        logger.error(
            "oc command is not installed"
        )

    except subprocess.CalledProcessError:

        logger.exception(
            "OpenShift health check failed"
        )


oc_health_check()
```

---

# 33. DevOps Example: Docker image pull

```python
import logging
import subprocess

logger = logging.getLogger("docker")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)

image = "nginx:latest"

logger.info(
    "Pulling Docker image: %s",
    image
)

try:

    subprocess.run(
        ["docker", "pull", image],
        check=True
    )

    logger.info(
        "Docker image pulled successfully: %s",
        image
    )

except subprocess.CalledProcessError:

    logger.exception(
        "Docker image pull failed: %s",
        image
    )
```

---

# 34. DevOps Example: Backup script

```python
import logging
import shutil
from pathlib import Path

logger = logging.getLogger("backup")

logging.basicConfig(
    filename="/tmp/backup.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)

source = Path("/etc")
destination = Path("/tmp/etc-backup")

logger.info("Backup started")
logger.info("Source: %s", source)
logger.info("Destination: %s", destination)

try:

    shutil.copytree(
        source,
        destination,
        dirs_exist_ok=True
    )

    logger.info(
        "Backup completed successfully"
    )

except Exception:

    logger.exception(
        "Backup failed"
    )
```

---

# 35. DevOps Example: CI/CD deployment

```python
import logging
import subprocess
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)


def run_command(command):

    logging.info(
        "Executing command: %s",
        " ".join(command)
    )

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        logging.info(
            "Command completed successfully"
        )

        if result.stdout:

            logging.debug(
                "Command output: %s",
                result.stdout.strip()
            )

        return result.stdout

    except subprocess.CalledProcessError as exc:

        logging.error(
            "Command failed with return code %s",
            exc.returncode
        )

        logging.error(
            "stderr: %s",
            exc.stderr.strip()
        )

        return None


logging.info(
    "CI/CD deployment started"
)

result = run_command(
    [
        "kubectl",
        "apply",
        "-f",
        "deployment.yaml"
    ]
)

if result is None:

    logging.error(
        "Deployment failed"
    )

    sys.exit(1)

logging.info(
    "CI/CD deployment completed"
)
```

This pattern can be used in:

```text
Jenkins
GitLab CI/CD
GitHub Actions
Kubernetes automation
OpenShift automation
Ansible helper scripts
```

---

# 36. Logging sensitive information

Never log passwords, tokens, private keys, or API secrets.

Bad:

```python
password = "SuperSecret123"

logging.info(
    "Connecting with password=%s",
    password
)
```

This can expose the password in:

- Jenkins logs
- GitLab job logs
- Kubernetes logs
- OpenShift logs
- Centralized logging systems
- SIEM systems

Better:

```python
logging.info(
    "Connecting to database"
)
```

For tokens:

```python
logging.info(
    "Authentication token loaded successfully"
)
```

Do not print the token itself.

---

# 37. Logging Kubernetes/OpenShift container applications

For containerized applications, writing logs to stdout/stderr is usually preferred.

```python
import logging
import sys

logger = logging.getLogger("app")

handler = logging.StreamHandler(
    sys.stdout
)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info(
    "Application started"
)
```

Then:

```bash
kubectl logs pod/my-app
```

or:

```bash
oc logs pod/my-app
```

This fits a container-native logging architecture.

---

# 38. Structured logging

Modern DevOps platforms often prefer structured logs.

A simple approach is JSON:

```python
import json
import logging

logging.basicConfig(
    level=logging.INFO
)

event = {
    "event": "deployment",
    "application": "nginx",
    "namespace": "production",
    "status": "success"
}

logging.info(
    json.dumps(event)
)
```

Example:

```text
INFO {"event": "deployment", "application": "nginx", "namespace": "production", "status": "success"}
```

Structured logs are easier for systems such as:

```text
Elasticsearch
OpenSearch
Splunk
Loki
SIEM platforms
Cloud logging systems
```

to search and process.

---

# 39. Logging in a multi-module DevOps project

Project:

```text
devops_tool/
├── main.py
├── deployment.py
└── monitoring.py
```

## deployment.py

```python
import logging

logger = logging.getLogger(__name__)


def deploy():

    logger.info(
        "Deployment started"
    )
```

## monitoring.py

```python
import logging

logger = logging.getLogger(__name__)


def health_check():

    logger.info(
        "Health check started"
    )
```

## main.py

```python
import logging

from deployment import deploy
from monitoring import health_check


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(name)s: "
        "%(message)s"
    )
)


deploy()
health_check()
```

Possible output:

```text
INFO deployment: Deployment started
INFO monitoring: Health check started
```

This is why:

```python
logging.getLogger(__name__)
```

is useful in large automation projects.

---

# 40. Avoid duplicate log messages

A common mistake is repeatedly adding handlers.

Bad:

```python
def get_logger():

    logger = logging.getLogger("app")

    handler = logging.StreamHandler()

    logger.addHandler(handler)

    return logger
```

If the function is called many times, the same logger can have multiple handlers.

A safer approach:

```python
def get_logger():

    logger = logging.getLogger("app")

    if not logger.handlers:

        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

    logger.setLevel(logging.INFO)

    return logger
```

---

# 41. `logging.disable()`

Logging can be temporarily disabled.

```python
import logging

logging.disable(logging.INFO)
```

This can suppress messages at or below the specified level.

Use carefully in production because disabling logging can make troubleshooting difficult.

---

# 42. Important `LogRecord` fields

A log record can contain:

```python
%(asctime)s
%(created)f
%(filename)s
%(funcName)s
%(levelname)s
%(levelno)d
%(lineno)d
%(module)s
%(name)s
%(pathname)s
%(process)d
%(thread)d
%(message)s
```

Example:

```python
logging.basicConfig(
    format=(
        "%(asctime)s "
        "PID=%(process)d "
        "%(levelname)s "
        "%(name)s "
        "%(filename)s:%(lineno)d "
        "%(message)s"
    )
)
```

This can be useful when troubleshooting automation running across multiple processes.

---

# 43. Complete production-style DevOps logging example

Project:

```text
devops-monitor/
├── main.py
└── logs/
```

`main.py`:

```python
import logging
import shutil
import subprocess
from logging.handlers import RotatingFileHandler


def configure_logging():

    logger = logging.getLogger(
        "devops-monitor"
    )

    logger.setLevel(
        logging.DEBUG
    )

    formatter = logging.Formatter(
        "%(asctime)s "
        "%(levelname)s "
        "%(name)s: "
        "%(message)s"
    )

    console = logging.StreamHandler()

    console.setLevel(
        logging.INFO
    )

    console.setFormatter(
        formatter
    )

    file_handler = RotatingFileHandler(
        "logs/devops-monitor.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )

    file_handler.setLevel(
        logging.DEBUG
    )

    file_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        console
    )

    logger.addHandler(
        file_handler
    )

    return logger


logger = configure_logging()


def check_disk():

    logger.info(
        "Checking disk usage"
    )

    try:

        total, used, free = (
            shutil.disk_usage("/")
        )

        usage = used / total * 100

        logger.info(
            "Root filesystem usage: %.2f%%",
            usage
        )

        if usage >= 90:

            logger.critical(
                "Root filesystem usage is critical: %.2f%%",
                usage
            )

        elif usage >= 80:

            logger.warning(
                "Root filesystem usage is high: %.2f%%",
                usage
            )

    except Exception:

        logger.exception(
            "Disk check failed"
        )


def check_kubernetes():

    logger.info(
        "Checking Kubernetes cluster"
    )

    try:

        result = subprocess.run(
            ["kubectl", "get", "nodes"],
            capture_output=True,
            text=True,
            check=True
        )

        logger.info(
            "Kubernetes API is reachable"
        )

        logger.debug(
            "Node output:\n%s",
            result.stdout
        )

    except FileNotFoundError:

        logger.error(
            "kubectl command not found"
        )

    except subprocess.CalledProcessError:

        logger.exception(
            "Kubernetes health check failed"
        )


def main():

    logger.info(
        "DevOps monitoring started"
    )

    check_disk()
    check_kubernetes()

    logger.info(
        "DevOps monitoring completed"
    )


if __name__ == "__main__":

    main()
```

Run:

```bash
mkdir -p logs

python3 main.py
```

View the persistent log:

```bash
tail -f logs/devops-monitor.log
```

---

# 44. Most important functions/classes cheat sheet

## Module-level functions

```python
logging.basicConfig()
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
logging.exception()
logging.log()
logging.getLogger()
logging.disable()
```

## Logger methods

```python
logger.debug()
logger.info()
logger.warning()
logger.error()
logger.critical()
logger.exception()
logger.log()
logger.setLevel()
logger.addHandler()
logger.removeHandler()
```

## Important classes

```python
logging.Logger
logging.Handler
logging.StreamHandler
logging.FileHandler
logging.Formatter
```

From:

```python
logging.handlers
```

Important classes:

```python
RotatingFileHandler
TimedRotatingFileHandler
```

---

# 45. Recommended logging levels for DevOps

```text
DEBUG
 |
 +-- kubectl output
 +-- API response details
 +-- variable values
 +-- troubleshooting information

INFO
 |
 +-- Deployment started
 +-- Deployment completed
 +-- Backup started
 +-- Health check passed

WARNING
 |
 +-- Disk usage > 80%
 +-- Certificate nearing expiry
 +-- Replica count below expected value

ERROR
 |
 +-- Deployment failed
 +-- Backup failed
 +-- API request failed

CRITICAL
 |
 +-- Cluster unavailable
 +-- Filesystem critically full
 +-- Recovery failure
```

---

# 46. DevOps best practices

## 1. Use a named logger

```python
logger = logging.getLogger(__name__)
```

## 2. Use the correct severity

Correct:

```python
logger.info(
    "Deployment started"
)
```

Incorrect:

```python
logger.error(
    "Deployment started"
)
```

## 3. Include timestamps

```python
"%(asctime)s"
```

## 4. Include logger name

```python
"%(name)s"
```

## 5. Include traceback for exceptions

```python
logger.exception(
    "Deployment failed"
)
```

## 6. Rotate persistent logs

Use:

```python
RotatingFileHandler
```

or:

```python
TimedRotatingFileHandler
```

## 7. Never log secrets

Never log:

```text
Passwords
API keys
Tokens
Private keys
Database credentials
Kubernetes secrets
```

## 8. Use stdout/stderr in containers

This allows Kubernetes/OpenShift and container log collectors to collect application logs.

## 9. Use DEBUG for troubleshooting

Do not flood normal production logs with unnecessary debug information.

## 10. Prefer structured logs for large environments

JSON/structured logs make centralized searching and alerting easier.

---

# 47. Interview questions

## Q1. Why use logging instead of print()?

`logging` provides:

- Severity levels
- Timestamps
- File output
- Multiple handlers
- Log rotation
- Exception traceback
- Named loggers
- Centralized logging integration

---

## Q2. What are the standard logging levels?

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

## Q3. Difference between `error()` and `exception()`?

`error()` logs an error message:

```python
logger.error(
    "Deployment failed"
)
```

`exception()` logs the message plus traceback:

```python
try:
    deploy()

except Exception:
    logger.exception(
        "Deployment failed"
    )
```

Use `exception()` inside an exception handler when you need RCA information.

---

## Q4. What is a Handler?

A Handler determines where the log record is sent.

Examples:

```text
StreamHandler
FileHandler
RotatingFileHandler
TimedRotatingFileHandler
```

---

## Q5. What is a Formatter?

A Formatter controls the structure of a log message.

Example:

```python
logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s: %(message)s"
)
```

---

## Q6. What is log rotation?

Log rotation prevents a log file from growing indefinitely.

Size-based:

```python
RotatingFileHandler
```

Time-based:

```python
TimedRotatingFileHandler
```

---

## Q7. Difference between logger level and handler level?

The logger level controls which records the logger allows.

The handler level controls which records that particular handler emits.

Example:

```python
logger.setLevel(
    logging.DEBUG
)

console.setLevel(
    logging.INFO
)

file_handler.setLevel(
    logging.DEBUG
)
```

Result:

```text
Console -> INFO and above
File    -> DEBUG and above
```

---

## Q8. Why use `logging.getLogger(__name__)`?

It creates a logger associated with the current module.

```python
logger = logging.getLogger(__name__)
```

This helps identify which module generated a message.

---

# 48. Quick reference example

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(name)s: "
        "%(message)s"
    )
)

logger = logging.getLogger(__name__)

logger.debug(
    "Detailed troubleshooting information"
)

logger.info(
    "Normal operational information"
)

logger.warning(
    "Potential problem"
)

logger.error(
    "Operation failed"
)

logger.critical(
    "Critical failure"
)

try:

    1 / 0

except Exception:

    logger.exception(
        "Unexpected exception"
    )
```

---

# 49. Final mental model

Remember this simple DevOps model:

```text
                 Python Automation
                        |
                        v
                     Logger
                        |
                        v
                   Log Record
                        |
                        v
                    Handler
                   /       \
                  /         \
                 v           v
             Console        File
                |             |
                v             v
             stdout      Rotated logs
                |
                v
       Kubernetes/OpenShift
                |
                v
       Centralized Logging
                |
        +-------+-------+
        |               |
        v               v
    OpenSearch        Loki
    /Elastic          /Grafana
```

The key rule is:

> **Logger creates the event, Level defines its severity, Handler decides where it goes, and Formatter decides how it looks.**

For a DevOps engineer, first master these:

```python
logging.getLogger()
logging.basicConfig()

logger.debug()
logger.info()
logger.warning()
logger.error()
logger.critical()
logger.exception()

logging.Formatter
logging.StreamHandler
logging.FileHandler

RotatingFileHandler
TimedRotatingFileHandler

logger.setLevel()
logger.addHandler()
logger.removeHandler()
```

These concepts are enough to build reliable logging into Linux, Kubernetes, OpenShift, Docker, CI/CD, backup, and infrastructure automation scripts.