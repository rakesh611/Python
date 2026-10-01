# Python `argparse` Module for DevOps Engineers

## 1. What is `argparse`?

`argparse` is a **built-in Python module** used to create command-line interfaces (CLI).

It allows a Python script to accept arguments such as:

```bash
python deploy.py --environment prod --version 1.2.5
```

Instead of hard-coding values inside the script, we can pass them from the command line.

### Why is `argparse` useful for DevOps?

DevOps engineers frequently write automation scripts for:

- Deployment
- Server health checks
- Backup and restore
- Log analysis
- Kubernetes/OpenShift operations
- Docker automation
- File cleanup
- Service management
- Monitoring
- Configuration management
- CI/CD pipelines

For example:

```bash
python deploy.py --environment production --version 2.5.1
```

The same script can be reused for different environments without changing the source code.

---

# 2. Basic Syntax

The basic structure is:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name")

args = parser.parse_args()

print(args.name)
```

Run:

```bash
python script.py --name rakesh
```

Output:

```text
rakesh
```

---

# 3. How `argparse` Works

The normal flow is:

```text
Command line
     |
     v
argparse.ArgumentParser()
     |
     v
add_argument()
     |
     v
parse_args()
     |
     v
args.variable
     |
     v
Python automation logic
```

Example:

```bash
python server_check.py --host 192.168.22.10
```

Python:

```python
args.host
```

returns:

```text
192.168.22.10
```

---

# 4. Important `argparse` Functions and Methods

The most important components for DevOps scripts are:

| Function / Method | Purpose |
|---|---|
| `argparse.ArgumentParser()` | Creates the argument parser |
| `parser.add_argument()` | Defines a CLI argument |
| `parser.parse_args()` | Parses command-line arguments |
| `parser.parse_known_args()` | Parses known arguments and leaves unknown ones |
| `parser.add_subparsers()` | Creates subcommands |
| `parser.set_defaults()` | Sets default values or functions |
| `parser.error()` | Displays an argument error |
| `parser.print_help()` | Displays help |
| `parser.print_usage()` | Displays usage information |
| `argparse.FileType()` | Opens files passed as arguments |
| `argparse.ArgumentDefaultsHelpFormatter` | Shows default values in help |
| `argparse.RawDescriptionHelpFormatter` | Preserves formatting in descriptions |

The most important one is:

```python
parser.add_argument()
```

because it defines how users interact with your CLI.

---

# 5. `ArgumentParser()`

## Purpose

`ArgumentParser()` creates the main CLI parser.

Syntax:

```python
parser = argparse.ArgumentParser()
```

Example:

```python
import argparse

parser = argparse.ArgumentParser(
    description="Linux server health check tool"
)

args = parser.parse_args()
```

Run:

```bash
python health_check.py --help
```

Output will contain:

```text
usage: health_check.py [-h]

Linux server health check tool
```

---

# 6. `description`

The `description` parameter explains what your script does.

Example:

```python
import argparse

parser = argparse.ArgumentParser(
    description="Deploy application to Kubernetes cluster"
)

args = parser.parse_args()
```

Run:

```bash
python deploy.py --help
```

The description appears in the help output.

---

# 7. `add_argument()`

This is the most important `argparse` method.

It defines a command-line argument.

Example:

```python
parser.add_argument("--environment")
```

Run:

```bash
python deploy.py --environment production
```

Access it:

```python
print(args.environment)
```

Output:

```text
production
```

---

# 8. Positional Arguments

A positional argument does not require `--`.

Example:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("environment")

args = parser.parse_args()

print(args.environment)
```

Run:

```bash
python deploy.py production
```

Output:

```text
production
```

Another example:

```python
parser.add_argument("application")
parser.add_argument("version")
```

Run:

```bash
python deploy.py nginx 1.27
```

Access:

```python
args.application
args.version
```

---

# 9. Optional Arguments

Optional arguments normally start with `--`.

Example:

```python
parser.add_argument("--environment")
```

Run:

```bash
python deploy.py --environment production
```

Access:

```python
args.environment
```

---

# 10. Short and Long Options

You can provide both short and long forms.

```python
parser.add_argument(
    "-e",
    "--environment"
)
```

Both commands work:

```bash
python deploy.py -e production
```

or:

```bash
python deploy.py --environment production
```

This is common in DevOps CLI tools.

---

# 11. `required=True`

By default, optional arguments are not mandatory.

Example:

```python
parser.add_argument(
    "--environment",
    required=True
)
```

Now this will fail:

```bash
python deploy.py
```

The user must provide:

```bash
python deploy.py --environment production
```

Example:

```python
parser.add_argument(
    "-e",
    "--environment",
    required=True,
    help="Deployment environment"
)
```

---

# 12. `default`

`default` specifies a value when the user does not provide an argument.

Example:

```python
parser.add_argument(
    "--namespace",
    default="default"
)
```

Run:

```bash
python deploy.py
```

Then:

```python
args.namespace
```

returns:

```text
default
```

This is very useful for Kubernetes/OpenShift scripts.

---

# 13. `type`

`type` converts the CLI input into a Python data type.

Without `type`:

```python
parser.add_argument("--replicas")
```

The value is a string.

With:

```python
parser.add_argument(
    "--replicas",
    type=int
)
```

the value becomes an integer.

Example:

```python
print(type(args.replicas))
```

Output:

```text
<class 'int'>
```

---

# 14. Common `type` Values

You can use:

```python
type=str
```

```python
type=int
```

```python
type=float
```

```python
type=bool
```

However, `type=bool` is usually **not recommended** for CLI flags.

For flags, use:

```python
action="store_true"
```

instead.

---

# 15. `choices`

`choices` restricts the allowed values.

Example:

```python
parser.add_argument(
    "--environment",
    choices=["dev", "qa", "prod"]
)
```

Valid:

```bash
python deploy.py --environment dev
```

Valid:

```bash
python deploy.py --environment prod
```

Invalid:

```bash
python deploy.py --environment testing
```

The parser reports an invalid choice.

This is very useful for deployment automation.

---

# 16. `help`

`help` explains an argument.

Example:

```python
parser.add_argument(
    "-e",
    "--environment",
    help="Target deployment environment"
)
```

Run:

```bash
python deploy.py --help
```

You will see the help text.

---

# 17. `metavar`

`metavar` controls how an argument is displayed in help.

Example:

```python
parser.add_argument(
    "--environment",
    metavar="ENV"
)
```

Help may show:

```text
--environment ENV
```

instead of:

```text
--environment ENVIRONMENT
```

This is useful for making CLI help cleaner.

---

# 18. `action="store_true"`

This is one of the most useful options for DevOps flags.

Example:

```python
parser.add_argument(
    "--dry-run",
    action="store_true"
)
```

Run:

```bash
python deploy.py --dry-run
```

Then:

```python
args.dry_run
```

returns:

```python
True
```

Without the flag:

```bash
python deploy.py
```

returns:

```python
False
```

This is ideal for options such as:

```text
--dry-run
--verbose
--force
--debug
--cleanup
```

---

# 19. `action="store_false"`

The opposite behavior can be implemented using:

```python
parser.add_argument(
    "--no-check",
    action="store_false",
    dest="check"
)
```

If:

```bash
python script.py
```

the default can be `True`.

If:

```bash
python script.py --no-check
```

then:

```python
args.check
```

becomes:

```text
False
```

---

# 20. `action="append"`

`append` allows the user to provide the same option multiple times.

Example:

```python
parser.add_argument(
    "--host",
    action="append"
)
```

Run:

```bash
python check.py \
    --host 192.168.22.10 \
    --host 192.168.22.11 \
    --host 192.168.22.12
```

Then:

```python
args.host
```

returns:

```python
[
    "192.168.22.10",
    "192.168.22.11",
    "192.168.22.12"
]
```

Useful for:

- Multiple servers
- Multiple namespaces
- Multiple Kubernetes resources
- Multiple files

---

# 21. `nargs`

`nargs` controls how many values an argument accepts.

## One value

Default:

```python
parser.add_argument("--host")
```

## Multiple values

```python
parser.add_argument(
    "--hosts",
    nargs="+"
)
```

Run:

```bash
python check.py \
    --hosts 192.168.22.10 192.168.22.11 192.168.22.12
```

Result:

```python
args.hosts
```

is:

```python
[
    "192.168.22.10",
    "192.168.22.11",
    "192.168.22.12"
]
```

### Common `nargs`

| Value | Meaning |
|---|---|
| `1` | Exactly one |
| `?` | Zero or one |
| `*` | Zero or more |
| `+` | One or more |

---

# 22. `dest`

`dest` controls the attribute name stored in the parsed result.

Example:

```python
parser.add_argument(
    "--target-node",
    dest="node"
)
```

Run:

```bash
python script.py --target-node ocp-w-1
```

Access:

```python
args.node
```

instead of:

```python
args.target_node
```

---

# 23. `version`

You can provide a version option.

Example:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--version",
    action="version",
    version="1.0.0"
)

args = parser.parse_args()
```

Run:

```bash
python script.py --version
```

Output:

```text
1.0.0
```

---

# 24. `parse_args()`

`parse_args()` reads the command-line arguments and converts them into a Namespace object.

Example:

```python
args = parser.parse_args()
```

Given:

```bash
python deploy.py --environment prod --replicas 3
```

you can access:

```python
args.environment
args.replicas
```

Example:

```python
print(args)
```

Output:

```text
Namespace(environment='prod', replicas=3)
```

---

# 25. `parse_known_args()`

Sometimes a script should process known arguments while allowing additional unknown arguments.

Example:

```python
args, unknown = parser.parse_known_args()

print(args)
print(unknown)
```

If the command is:

```bash
python script.py --environment prod --extra-value test
```

then the known arguments are parsed while the unknown arguments are returned separately.

This can be useful when integrating a Python wrapper with another CLI tool.

---

# 26. `print_help()`

Displays the complete help message.

Example:

```python
parser.print_help()
```

You can also trigger help automatically with:

```bash
python script.py --help
```

---

# 27. `print_usage()`

Displays only the usage section.

Example:

```python
parser.print_usage()
```

This is useful when writing custom validation.

---

# 28. `parser.error()`

Used to display an argument-related error.

Example:

```python
if args.environment == "prod" and args.replicas < 2:
    parser.error(
        "Production requires at least 2 replicas"
    )
```

This is useful for enforcing operational rules in automation scripts.

---

# 29. `FileType`

`argparse.FileType()` can open files passed through CLI arguments.

Example:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--config",
    type=argparse.FileType("r")
)

args = parser.parse_args()

content = args.config.read()

print(content)
```

Run:

```bash
python script.py --config deployment.yaml
```

For simple scripts, `pathlib.Path` is often more flexible, but `FileType` is useful when you want `argparse` to handle opening the file.

---

# 30. `ArgumentDefaultsHelpFormatter`

This formatter displays default values in help output.

Example:

```python
import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "--namespace",
    default="default"
)

parser.add_argument(
    "--replicas",
    type=int,
    default=2
)

args = parser.parse_args()
```

Run:

```bash
python script.py --help
```

The help output includes the defaults.

---

# 31. `RawDescriptionHelpFormatter`

This formatter preserves newlines in the description.

Example:

```python
import argparse

description = """
Kubernetes deployment utility.

Examples:
  python deploy.py --environment dev
  python deploy.py --environment prod
"""

parser = argparse.ArgumentParser(
    description=description,
    formatter_class=argparse.RawDescriptionHelpFormatter
)
```

Useful when creating professional internal DevOps tools.

---

# 32. Complete DevOps Example 1: Kubernetes Deployment

Consider a deployment script:

```python
#!/usr/bin/env python3

import argparse
import subprocess


parser = argparse.ArgumentParser(
    description="Deploy application to Kubernetes"
)

parser.add_argument(
    "-e",
    "--environment",
    required=True,
    choices=["dev", "qa", "prod"],
    help="Target environment"
)

parser.add_argument(
    "-n",
    "--namespace",
    default="default",
    help="Kubernetes namespace"
)

parser.add_argument(
    "-r",
    "--replicas",
    type=int,
    default=2,
    help="Number of replicas"
)

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Show command without executing it"
)

args = parser.parse_args()


command = [
    "kubectl",
    "scale",
    "deployment",
    "web",
    "--replicas",
    str(args.replicas),
    "-n",
    args.namespace
]

print("Environment:", args.environment)
print("Namespace:", args.namespace)
print("Replicas:", args.replicas)

if args.dry_run:
    print("DRY RUN:")
    print(" ".join(command))
else:
    subprocess.run(command, check=True)
```

Run:

```bash
python deploy.py \
    --environment prod \
    --namespace production \
    --replicas 4
```

Dry run:

```bash
python deploy.py \
    --environment prod \
    --namespace production \
    --replicas 4 \
    --dry-run
```

Expected output:

```text
Environment: prod
Namespace: production
Replicas: 4
DRY RUN:
kubectl scale deployment web --replicas 4 -n production
```

---

# 33. Complete DevOps Example 2: Linux Server Health Check

```python
#!/usr/bin/env python3

import argparse
import subprocess


parser = argparse.ArgumentParser(
    description="Linux server health check"
)

parser.add_argument(
    "-H",
    "--host",
    required=True,
    help="Remote Linux server"
)

parser.add_argument(
    "-u",
    "--user",
    default="root",
    help="SSH user"
)

parser.add_argument(
    "--port",
    type=int,
    default=22,
    help="SSH port"
)

parser.add_argument(
    "--command",
    default="uptime",
    help="Command to execute remotely"
)

args = parser.parse_args()


ssh_command = [
    "ssh",
    "-p",
    str(args.port),
    f"{args.user}@{args.host}",
    args.command
]

print("Executing:")
print(" ".join(ssh_command))

subprocess.run(ssh_command, check=True)
```

Run:

```bash
python health_check.py \
    --host 192.168.22.10 \
    --user root \
    --command "uptime"
```

Another example:

```bash
python health_check.py \
    --host 192.168.22.10 \
    --user root \
    --command "df -h"
```

---

# 34. Complete DevOps Example 3: Log Analyzer

Suppose you want to analyze an application log.

```python
#!/usr/bin/env python3

import argparse
from pathlib import Path


parser = argparse.ArgumentParser(
    description="Analyze application log file"
)

parser.add_argument(
    "-f",
    "--file",
    type=Path,
    required=True,
    help="Path to log file"
)

parser.add_argument(
    "--keyword",
    default="ERROR",
    help="Keyword to search"
)

args = parser.parse_args()


if not args.file.exists():
    parser.error(f"Log file does not exist: {args.file}")


count = 0

with args.file.open() as logfile:
    for line in logfile:
        if args.keyword in line:
            count += 1


print(f"Keyword: {args.keyword}")
print(f"Matches: {count}")
```

Run:

```bash
python log_analyzer.py \
    --file /var/log/app/application.log \
    --keyword ERROR
```

Output:

```text
Keyword: ERROR
Matches: 37
```

You can also search for:

```bash
python log_analyzer.py \
    --file application.log \
    --keyword WARNING
```

---

# 35. Complete DevOps Example 4: OpenShift Pod Checker

```python
#!/usr/bin/env python3

import argparse
import subprocess


parser = argparse.ArgumentParser(
    description="Check OpenShift pod status"
)

parser.add_argument(
    "-n",
    "--namespace",
    required=True,
    help="OpenShift project/namespace"
)

parser.add_argument(
    "--selector",
    help="Label selector"
)

args = parser.parse_args()


command = [
    "oc",
    "get",
    "pods",
    "-n",
    args.namespace
]

if args.selector:
    command.extend([
        "-l",
        args.selector
    ])

subprocess.run(command, check=True)
```

Run:

```bash
python pod_check.py \
    --namespace sonarqube
```

Using a selector:

```bash
python pod_check.py \
    --namespace sonarqube \
    --selector app=sonarqube
```

This is a practical pattern for OpenShift automation.

---

# 36. Complete DevOps Example 5: Multiple Kubernetes Namespaces

Using `nargs="+"`:

```python
#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser(
    description="Process multiple Kubernetes namespaces"
)

parser.add_argument(
    "--namespaces",
    nargs="+",
    required=True,
    help="Namespaces to process"
)

args = parser.parse_args()


for namespace in args.namespaces:
    print(f"Checking namespace: {namespace}")
```

Run:

```bash
python check.py \
    --namespaces default sonarqube logging monitoring
```

Output:

```text
Checking namespace: default
Checking namespace: sonarqube
Checking namespace: logging
Checking namespace: monitoring
```

---

# 37. Complete DevOps Example 6: Multiple Servers

Using `action="append"`:

```python
#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser(
    description="Check multiple Linux servers"
)

parser.add_argument(
    "--host",
    action="append",
    required=True,
    help="Server IP or hostname; can be specified multiple times"
)

args = parser.parse_args()


for host in args.host:
    print(f"Checking server: {host}")
```

Run:

```bash
python check.py \
    --host 192.168.22.10 \
    --host 192.168.22.11 \
    --host 192.168.22.12
```

Output:

```text
Checking server: 192.168.22.10
Checking server: 192.168.22.11
Checking server: 192.168.22.12
```

---

# 38. Subcommands with `add_subparsers()`

Professional CLI tools often use subcommands.

For example:

```bash
python infra.py server check
python infra.py server restart
python infra.py k8s pods
python infra.py k8s deploy
```

This can be implemented with `add_subparsers()`.

Example:

```python
import argparse


parser = argparse.ArgumentParser(
    description="Infrastructure automation CLI"
)

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)


server_parser = subparsers.add_parser(
    "server",
    help="Server operations"
)

server_parser.add_argument(
    "action",
    choices=["check", "restart"]
)


k8s_parser = subparsers.add_parser(
    "k8s",
    help="Kubernetes operations"
)

k8s_parser.add_argument(
    "action",
    choices=["pods", "deploy"]
)


args = parser.parse_args()

print(args)
```

Run:

```bash
python infra.py server check
```

or:

```bash
python infra.py k8s pods
```

This approach is useful when building a larger internal DevOps CLI.

---

# 39. `set_defaults()`

`set_defaults()` can associate a function with a subcommand.

Example:

```python
import argparse


def server_check(args):
    print(f"Checking server: {args.host}")


def k8s_pods(args):
    print(f"Checking pods in: {args.namespace}")


parser = argparse.ArgumentParser(
    description="DevOps CLI"
)

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)


server = subparsers.add_parser("server")
server.add_argument("--host", required=True)
server.set_defaults(func=server_check)


k8s = subparsers.add_parser("k8s")
k8s.add_argument("--namespace", required=True)
k8s.set_defaults(func=k8s_pods)


args = parser.parse_args()

args.func(args)
```

Run:

```bash
python infra.py server --host 192.168.22.10
```

Output:

```text
Checking server: 192.168.22.10
```

Run:

```bash
python infra.py k8s --namespace sonarqube
```

Output:

```text
Checking pods in: sonarqube
```

This pattern is useful for larger automation frameworks.

---

# 40. Argument Validation

`argparse` performs basic validation automatically.

Example:

```python
parser.add_argument(
    "--replicas",
    type=int
)
```

This command:

```bash
python deploy.py --replicas abc
```

will fail because `abc` cannot be converted to an integer.

You can also implement custom validation.

Example:

```python
if args.replicas < 1:
    parser.error("--replicas must be greater than 0")
```

---

# 41. DevOps Example: Production Validation

A common requirement is to protect production deployments.

Example:

```python
import argparse


parser = argparse.ArgumentParser()

parser.add_argument(
    "--environment",
    choices=["dev", "qa", "prod"],
    required=True
)

parser.add_argument(
    "--version",
    required=True
)

parser.add_argument(
    "--force",
    action="store_true"
)

args = parser.parse_args()


if args.environment == "prod" and not args.force:
    parser.error(
        "Production deployment requires --force"
    )

print(
    f"Deploying version {args.version} "
    f"to {args.environment}"
)
```

Run:

```bash
python deploy.py \
    --environment prod \
    --version 2.5.1
```

The script rejects the operation.

Run:

```bash
python deploy.py \
    --environment prod \
    --version 2.5.1 \
    --force
```

Now the validation succeeds.

> In a real production environment, additional authorization, approval, and safety controls should be implemented rather than relying only on a CLI flag.

---

# 42. `argparse` + Environment Variables

`argparse` can be combined with environment variables.

Example:

```python
import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument(
    "--namespace",
    default=os.getenv("K8S_NAMESPACE", "default")
)

args = parser.parse_args()

print("Namespace:", args.namespace)
```

If:

```bash
export K8S_NAMESPACE=sonarqube
```

then:

```bash
python script.py
```

produces:

```text
Namespace: sonarqube
```

A CLI argument can override the environment variable:

```bash
python script.py --namespace logging
```

Output:

```text
Namespace: logging
```

This pattern is very useful in CI/CD pipelines.

---

# 43. `argparse` in Jenkins/GitLab CI

A Python deployment script might contain:

```python
parser.add_argument(
    "--environment",
    required=True,
    choices=["dev", "qa", "prod"]
)

parser.add_argument(
    "--version",
    required=True
)
```

Jenkins can execute:

```bash
python deploy.py \
    --environment "$ENVIRONMENT" \
    --version "$APP_VERSION"
```

GitLab CI can execute:

```bash
python deploy.py \
    --environment "$DEPLOY_ENV" \
    --version "$CI_COMMIT_TAG"
```

This makes the same Python script reusable across pipelines.

---

# 44. `argparse` + Docker

Example:

```python
import argparse
import subprocess


parser = argparse.ArgumentParser(
    description="Docker image build utility"
)

parser.add_argument(
    "--image",
    required=True
)

parser.add_argument(
    "--tag",
    default="latest"
)

parser.add_argument(
    "--no-cache",
    action="store_true"
)

args = parser.parse_args()


command = [
    "docker",
    "build",
    "-t",
    f"{args.image}:{args.tag}"
]

if args.no_cache:
    command.append("--no-cache")

command.append(".")


print(" ".join(command))

subprocess.run(command, check=True)
```

Run:

```bash
python build.py \
    --image myapp \
    --tag 1.0.0 \
    --no-cache
```

---

# 45. `argparse` + Ansible

You can use `argparse` to select an Ansible inventory.

```python
import argparse
import subprocess


parser = argparse.ArgumentParser(
    description="Run Ansible playbook"
)

parser.add_argument(
    "--inventory",
    required=True
)

parser.add_argument(
    "--playbook",
    required=True
)

parser.add_argument(
    "--limit"
)

args = parser.parse_args()


command = [
    "ansible-playbook",
    "-i",
    args.inventory,
    args.playbook
]

if args.limit:
    command.extend([
        "--limit",
        args.limit
    ])

subprocess.run(command, check=True)
```

Run:

```bash
python ansible_run.py \
    --inventory inventory/prod \
    --playbook site.yml \
    --limit webservers
```

---

# 46. A Professional DevOps CLI Example

Here is a more complete example combining several concepts.

```python
#!/usr/bin/env python3

import argparse
import subprocess
import sys


def create_parser():
    parser = argparse.ArgumentParser(
        description="DevOps Kubernetes deployment utility"
    )

    parser.add_argument(
        "-e",
        "--environment",
        required=True,
        choices=["dev", "qa", "prod"],
        help="Target environment"
    )

    parser.add_argument(
        "-n",
        "--namespace",
        default="default",
        help="Kubernetes namespace"
    )

    parser.add_argument(
        "-r",
        "--replicas",
        type=int,
        default=2,
        help="Number of replicas"
    )

    parser.add_argument(
        "--image",
        required=True,
        help="Container image"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print command without executing"
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.replicas < 1:
        parser.error("--replicas must be >= 1")

    command = [
        "kubectl",
        "set",
        "image",
        "deployment/web",
        f"web={args.image}",
        "-n",
        args.namespace
    ]

    print(f"Environment : {args.environment}")
    print(f"Namespace   : {args.namespace}")
    print(f"Replicas    : {args.replicas}")
    print(f"Image       : {args.image}")

    if args.dry_run:
        print("\nDRY RUN:")
        print(" ".join(command))
        return

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as exc:
        print(
            f"Deployment failed with exit code {exc.returncode}",
            file=sys.stderr
        )
        sys.exit(exc.returncode)


if __name__ == "__main__":
    main()
```

Run:

```bash
python deploy.py \
    --environment prod \
    --namespace production \
    --replicas 3 \
    --image registry.example.com/web:2.5.1 \
    --dry-run
```

---

# 47. `if __name__ == "__main__"` with `argparse`

You will commonly see:

```python
if __name__ == "__main__":
    main()
```

This ensures that the CLI code executes when the Python file is run directly.

Example:

```python
def main():
    parser = argparse.ArgumentParser()
    ...
    args = parser.parse_args()


if __name__ == "__main__":
    main()
```

This is considered a clean structure for reusable automation scripts.

---

# 48. Complete Command-Line Example

Suppose the file is:

```text
deploy.py
```

Run:

```bash
python deploy.py --help
```

Possible output:

```text
usage: deploy.py [-h] -e {dev,qa,prod} [-n NAMESPACE]
                 [-r REPLICAS] --image IMAGE [--dry-run]

DevOps Kubernetes deployment utility

options:
  -h, --help
  -e {dev,qa,prod}, --environment {dev,qa,prod}
                        Target environment
  -n NAMESPACE, --namespace NAMESPACE
                        Kubernetes namespace
  -r REPLICAS, --replicas REPLICAS
                        Number of replicas
  --image IMAGE         Container image
  --dry-run             Print command without executing
```

This is one of the biggest advantages of `argparse`: it automatically generates a useful CLI help interface.

---

# 49. Important `argparse` Parameters Cheat Sheet

## `ArgumentParser()`

```python
argparse.ArgumentParser(
    description="Description",
    epilog="Additional information",
    formatter_class=...
)
```

## `add_argument()`

Common parameters:

```python
parser.add_argument(
    "--name",
    type=str,
    default="value",
    required=False,
    choices=["a", "b"],
    help="Description",
    metavar="NAME",
    dest="variable",
    nargs="+",
    action="store_true"
)
```

---

# 50. Most Important `action` Values

| Action | Purpose |
|---|---|
| `store` | Store the supplied value; this is the default |
| `store_true` | Set value to `True` when flag is present |
| `store_false` | Set value to `False` when flag is present |
| `append` | Append repeated values to a list |
| `count` | Count repeated occurrences |
| `version` | Display version and exit |
| `help` | Display help |

Example:

```python
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true"
)
```

Example:

```bash
python script.py --verbose
```

---

# 51. `action="count"`

Useful for verbosity levels.

```python
parser.add_argument(
    "-v",
    "--verbose",
    action="count",
    default=0
)
```

Run:

```bash
python script.py -v
```

Result:

```text
1
```

Run:

```bash
python script.py -vv
```

Result:

```text
2
```

Run:

```bash
python script.py -vvv
```

Result:

```text
3
```

This can be used to implement:

```text
-v    normal verbose
-vv   detailed debugging
-vvv  very detailed debugging
```

---

# 52. Best Practices for DevOps Scripts

## 1. Always provide `--help`

Use meaningful descriptions:

```python
help="Kubernetes namespace"
```

## 2. Use `choices` where possible

Instead of:

```python
--environment anything
```

use:

```python
choices=["dev", "qa", "prod"]
```

## 3. Use `type=int` for numeric values

Good:

```python
type=int
```

Avoid manually converting:

```python
int(args.replicas)
```

when `argparse` can do it.

## 4. Use `store_true` for boolean flags

Good:

```python
action="store_true"
```

Avoid:

```python
type=bool
```

for normal CLI flags.

## 5. Provide safe defaults

Example:

```python
default="default"
```

## 6. Validate dangerous operations

For production operations, validate:

```python
if args.environment == "prod":
    ...
```

## 7. Add dry-run functionality

A useful automation pattern is:

```bash
--dry-run
```

This allows engineers to verify commands before execution.

## 8. Return proper exit codes

Use:

```python
sys.exit(1)
```

or:

```python
subprocess.run(command, check=True)
```

This is important because CI/CD systems use exit codes to determine success or failure.

---

# 53. Common Mistakes

## Mistake 1: Forgetting `parse_args()`

Incorrect:

```python
parser.add_argument("--name")

print(args.name)
```

Correct:

```python
parser.add_argument("--name")

args = parser.parse_args()

print(args.name)
```

---

## Mistake 2: Using `type=bool` for normal flags

Avoid:

```python
parser.add_argument(
    "--dry-run",
    type=bool
)
```

Prefer:

```python
parser.add_argument(
    "--dry-run",
    action="store_true"
)
```

---

## Mistake 3: Not validating choices

Instead of:

```python
parser.add_argument("--environment")
```

consider:

```python
parser.add_argument(
    "--environment",
    choices=["dev", "qa", "prod"]
)
```

---

## Mistake 4: Hard-coding environment values

Avoid:

```python
environment = "prod"
```

Better:

```python
parser.add_argument(
    "--environment",
    required=True
)
```

Then:

```bash
python deploy.py --environment prod
```

---

# 54. `argparse` vs `sys.argv`

Without `argparse`, you could use:

```python
import sys

print(sys.argv)
```

Run:

```bash
python script.py prod 3
```

You might receive:

```python
[
    "script.py",
    "prod",
    "3"
]
```

But you would need to manually handle:

- Argument positions
- Missing arguments
- Type conversion
- Help
- Validation
- Error messages

With `argparse`:

```python
parser.add_argument(
    "--environment",
    choices=["dev", "qa", "prod"]
)

parser.add_argument(
    "--replicas",
    type=int
)
```

Python handles much of this automatically.

---

# 55. `argparse` vs Environment Variables

### CLI

```bash
python deploy.py --environment prod
```

Advantages:

- Explicit
- Easy to test
- Good for interactive use

### Environment variable

```bash
export ENVIRONMENT=prod
python deploy.py
```

Advantages:

- Good for CI/CD
- Useful for pipeline configuration
- Avoids long command lines

### Practical DevOps approach

Use both:

```python
default=os.getenv("ENVIRONMENT", "dev")
```

and allow CLI arguments to override defaults.

---

# 56. Interview Questions

## Q1. What is `argparse`?

`argparse` is a Python standard-library module used to create command-line interfaces and parse command-line arguments.

---

## Q2. Why is `argparse` useful in DevOps?

It allows automation scripts to accept runtime parameters such as:

```text
environment
namespace
server
image
version
replicas
file
```

This makes scripts reusable across environments.

---

## Q3. What does `parse_args()` do?

It reads command-line arguments and converts them into a Python `Namespace`.

Example:

```python
args = parser.parse_args()
```

---

## Q4. Difference between positional and optional arguments?

Positional:

```python
parser.add_argument("environment")
```

Usage:

```bash
python deploy.py prod
```

Optional:

```python
parser.add_argument("--environment")
```

Usage:

```bash
python deploy.py --environment prod
```

---

## Q5. How do you create a boolean flag?

Use:

```python
action="store_true"
```

Example:

```python
parser.add_argument(
    "--dry-run",
    action="store_true"
)
```

---

## Q6. How do you restrict argument values?

Use:

```python
choices=["dev", "qa", "prod"]
```

Example:

```python
parser.add_argument(
    "--environment",
    choices=["dev", "qa", "prod"]
)
```

---

## Q7. How do you make an argument mandatory?

Use:

```python
required=True
```

Example:

```python
parser.add_argument(
    "--image",
    required=True
)
```

---

## Q8. How do you set a default value?

Use:

```python
default="default"
```

Example:

```python
parser.add_argument(
    "--namespace",
    default="default"
)
```

---

## Q9. How do you accept multiple values?

Use:

```python
nargs="+"
```

Example:

```python
parser.add_argument(
    "--hosts",
    nargs="+"
)
```

---

## Q10. How do you accept the same option multiple times?

Use:

```python
action="append"
```

Example:

```python
parser.add_argument(
    "--host",
    action="append"
)
```

---

# 57. Real DevOps CLI Design Pattern

A good DevOps Python script often follows this structure:

```text
script.py
   |
   +-- ArgumentParser
   |
   +-- add_argument
   |
   +-- parse_args
   |
   +-- validate arguments
   |
   +-- execute automation
   |
   +-- error handling
   |
   +-- exit code
```

Example:

```python
def main():

    parser = argparse.ArgumentParser(
        description="DevOps automation tool"
    )

    parser.add_argument(
        "--environment",
        required=True,
        choices=["dev", "qa", "prod"]
    )

    parser.add_argument(
        "--dry-run",
        action="store_true"
    )

    args = parser.parse_args()

    # Validation
    # Automation
    # Error handling


if __name__ == "__main__":
    main()
```

This structure is clean, reusable, and suitable for CI/CD automation.

---

# 58. Quick Reference

```python
import argparse

parser = argparse.ArgumentParser(
    description="DevOps automation tool"
)

parser.add_argument(
    "-e",
    "--environment",
    required=True,
    choices=["dev", "qa", "prod"],
    help="Target environment"
)

parser.add_argument(
    "-n",
    "--namespace",
    default="default",
    help="Kubernetes namespace"
)

parser.add_argument(
    "-r",
    "--replicas",
    type=int,
    default=2,
    help="Number of replicas"
)

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Do not execute changes"
)

args = parser.parse_args()

print(args.environment)
print(args.namespace)
print(args.replicas)
print(args.dry_run)
```

Example:

```bash
python deploy.py \
    --environment prod \
    --namespace production \
    --replicas 3 \
    --dry-run
```

---

# 59. Important Functions/Methods to Remember

For a DevOps engineer, remember these first:

```text
argparse.ArgumentParser()
        ↓
parser.add_argument()
        ↓
parser.parse_args()
        ↓
args.argument
```

Then learn:

```text
required=True
default=
type=
choices=
help=
action=
nargs=
dest=
```

After that, learn:

```text
add_subparsers()
set_defaults()
parse_known_args()
parser.error()
parser.print_help()
parser.print_usage()
```

---

# 60. Final DevOps Perspective

`argparse` is especially valuable because it turns a simple Python script into a reusable CLI automation tool.

For example, instead of creating separate scripts:

```text
deploy_dev.py
deploy_qa.py
deploy_prod.py
```

you can create one script:

```text
deploy.py
```

and execute:

```bash
python deploy.py --environment dev
```

```bash
python deploy.py --environment qa
```

```bash
python deploy.py --environment prod
```

Similarly, one OpenShift/Kubernetes automation script can accept:

```bash
python ocp.py \
    --namespace sonarqube \
    --replicas 3 \
    --image sonarqube:2026.1 \
    --dry-run
```

This makes `argparse` a useful building block for **DevOps automation, CI/CD tools, Linux administration scripts, Kubernetes/OpenShift utilities, and internal command-line tools**.