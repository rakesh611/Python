# Python `re` Module — Complete Guide for DevOps Engineers

## 1. What is the `re` Module?

Python's built-in `re` module provides support for **Regular Expressions (Regex)**.

Regular expressions are patterns used to:

- Search text
- Extract information
- Validate input
- Replace text
- Split text
- Parse logs
- Analyze command output
- Detect errors and warnings
- Process configuration files
- Extract IP addresses, ports, versions, URLs, etc.

Import it with:

```python
import re
```

The `re` module is part of Python's standard library, so no `pip install` is required.

---

# 2. Why Regex is Important for DevOps

DevOps engineers frequently work with unstructured text:

```text
Linux logs
Command output
Application logs
Monitoring output
Configuration files
CI/CD output
Ansible output
OpenShift/Kubernetes output
```

For example:

```text
Server IP is 192.168.22.10
```

To extract the IP:

```python
import re

text = "Server IP is 192.168.22.10"

result = re.search(r"\d+\.\d+\.\d+\.\d+", text)

if result:
    print(result.group())
```

Output:

```text
192.168.22.10
```

---

# 3. What is Regular Expression?

A regular expression is a pattern used to identify specific text.

Example:

```python
r"\d+\.\d+\.\d+\.\d+"
```

Breakdown:

| Regex | Meaning |
|---|---|
| `\d` | Any digit from 0-9 |
| `+` | One or more occurrences |
| `\.` | Literal dot |
| `r""` | Python raw string |

Therefore:

```text
\d+\.\d+\.\d+\.\d+
```

can match:

```text
192.168.22.10
10.0.0.1
172.30.0.10
```

---

# 4. Important `re` Functions

The most important functions for DevOps automation are:

```text
re.search()
re.match()
re.fullmatch()
re.findall()
re.finditer()
re.split()
re.sub()
re.subn()
re.compile()
re.escape()
```

Important regex flags include:

```text
re.IGNORECASE
re.MULTILINE
re.DOTALL
re.VERBOSE
```

---

# 5. `re.search()`

## Purpose

Searches the entire string and returns the **first matching occurrence**.

### Syntax

```python
re.search(pattern, string)
```

### Example

```python
import re

text = "Kubernetes cluster version is v1.33.6"

result = re.search(r"v\d+\.\d+\.\d+", text)

if result:
    print(result.group())
```

Output:

```text
v1.33.6
```

## DevOps Example — Find an IP Address

```python
import re

output = """
Server: ocp-svc
IP Address: 192.168.22.1
Gateway: 192.168.22.254
"""

result = re.search(
    r"\d+\.\d+\.\d+\.\d+",
    output
)

if result:
    print("IP:", result.group())
```

Output:

```text
IP: 192.168.22.1
```

### Important

`search()` returns only the **first match**.

---

# 6. `re.match()`

## Purpose

`re.match()` checks whether the pattern matches from the **beginning of the string**.

### Example

```python
import re

text = "ERROR: Kubernetes pod failed"

result = re.match(r"ERROR", text)

if result:
    print("Error found")
```

Output:

```text
Error found
```

But:

```python
import re

text = "Kubernetes ERROR: pod failed"

result = re.match(r"ERROR", text)

print(result)
```

Output:

```text
None
```

Because `ERROR` is not at the beginning.

## DevOps Example — Detect Error Lines

```python
import re

logs = [
    "ERROR: Pod nginx failed",
    "INFO: Pod nginx started",
    "WARNING: Disk usage high"
]

for line in logs:
    if re.match(r"ERROR", line):
        print("Error:", line)
```

Output:

```text
Error: ERROR: Pod nginx failed
```

---

# 7. `re.fullmatch()`

## Purpose

`fullmatch()` requires the **entire string** to match the pattern.

It is useful for validation.

### Example

```python
import re

value = "sonarqube-prod"

pattern = r"[a-z0-9-]+"

if re.fullmatch(pattern, value):
    print("Valid namespace format")
else:
    print("Invalid namespace")
```

Output:

```text
Valid namespace format
```

If:

```python
value = "SonarQube-Prod"
```

the pattern will not match because uppercase characters are not allowed.

## DevOps Use Cases

`fullmatch()` is useful for validating:

- Namespace names
- Hostname formats
- Environment names
- Version formats
- User input
- Configuration values

---

# 8. `re.findall()`

## Purpose

Returns **all matching values** as a list.

This is one of the most useful `re` functions for DevOps.

### Example

```python
import re

text = """
Server1: 192.168.22.10
Server2: 192.168.22.11
Server3: 192.168.22.12
"""

ips = re.findall(
    r"\d+\.\d+\.\d+\.\d+",
    text
)

print(ips)
```

Output:

```text
['192.168.22.10', '192.168.22.11', '192.168.22.12']
```

## DevOps Example — Extract IPs from Command Output

```python
import subprocess
import re

output = subprocess.check_output(
    ["ip", "addr"],
    text=True
)

ips = re.findall(
    r"\b\d{1,3}(?:\.\d{1,3}){3}\b",
    output
)

for ip in ips:
    print(ip)
```

This can be used in Linux automation scripts.

> Note: This regex checks the shape of an IPv4 address, not whether every octet is between 0 and 255. For strict IP validation, Python's `ipaddress` module is preferable.

---

# 9. `re.finditer()`

## Purpose

`finditer()` returns an iterator containing **match objects**.

Use it when you need:

- Matched value
- Start position
- End position
- Capturing groups

### Example

```python
import re

text = "node1=192.168.22.11 node2=192.168.22.12"

for match in re.finditer(
    r"\d+\.\d+\.\d+\.\d+",
    text
):
    print("IP:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
```

Example output:

```text
IP: 192.168.22.11
Start: 6
End: 19

IP: 192.168.22.12
Start: 26
End: 39
```

### Difference

```text
findall()  -> matching values
finditer() -> match objects
```

---

# 10. `match.group()`

`group()` is a method of the match object.

Example:

```python
import re

text = "Pod nginx-abc123 is Running"

result = re.search(
    r"Pod (\S+)",
    text
)

if result:
    print(result.group())
    print(result.group(1))
```

Output:

```text
Pod nginx-abc123
nginx-abc123
```

- `group()` or `group(0)` = complete match
- `group(1)` = first capturing group
- `group(2)` = second capturing group

---

# 11. Capturing Groups `()`

Parentheses create capturing groups.

Example:

```python
import re

text = "CPU=75% MEMORY=82%"

pattern = r"CPU=(\d+)% MEMORY=(\d+)%"

result = re.search(pattern, text)

if result:
    print("CPU:", result.group(1))
    print("Memory:", result.group(2))
```

Output:

```text
CPU: 75
Memory: 82
```

## DevOps Example — Parse Pod Information

```python
import re

text = "nginx-abc123   1/1   Running   0   2h"

pattern = r"(\S+)\s+\d+/\d+\s+(\S+)\s+\d+\s+(\S+)"

result = re.search(pattern, text)

if result:
    pod = result.group(1)
    status = result.group(2)
    age = result.group(3)

    print("Pod:", pod)
    print("Status:", status)
    print("Age:", age)
```

For production Kubernetes/OpenShift automation, structured JSON from `kubectl`/`oc` is generally safer than parsing table output with regex.

---

# 12. Named Capturing Groups

Instead of:

```python
group(1)
group(2)
```

you can give groups names.

### Example

```python
import re

text = "CPU=75% MEMORY=82%"

pattern = (
    r"CPU=(?P<cpu>\d+)% "
    r"MEMORY=(?P<memory>\d+)%"
)

result = re.search(pattern, text)

if result:
    print("CPU:", result.group("cpu"))
    print("Memory:", result.group("memory"))
```

Output:

```text
CPU: 75
Memory: 82
```

Named groups make automation scripts easier to read.

---

# 13. `groupdict()`

When named groups are used, `groupdict()` returns a dictionary.

```python
import re

text = "server=web01 ip=192.168.22.10"

pattern = (
    r"server=(?P<server>\S+)\s+"
    r"ip=(?P<ip>\S+)"
)

match = re.search(pattern, text)

if match:
    print(match.groupdict())
```

Output:

```text
{'server': 'web01', 'ip': '192.168.22.10'}
```

This is useful when converting parsed text into structured data.

---

# 14. `re.split()`

## Purpose

Splits a string using a regex pattern.

### Example

```python
import re

text = "linux,kubernetes;openshift docker"

items = re.split(
    r"[,; ]+",
    text
)

print(items)
```

Output:

```text
['linux', 'kubernetes', 'openshift', 'docker']
```

## DevOps Example

```python
import re

servers = "web01,web02;web03 web04"

server_list = re.split(
    r"[,; ]+",
    servers
)

for server in server_list:
    print(server)
```

Output:

```text
web01
web02
web03
web04
```

---

# 15. `re.sub()`

## Purpose

Replaces matching text.

### Syntax

```python
re.sub(pattern, replacement, string)
```

### Example

```python
import re

text = "server01.example.com"

result = re.sub(
    r"\.example\.com",
    "",
    text
)

print(result)
```

Output:

```text
server01
```

---

# 16. DevOps Example — Mask Passwords

Suppose a configuration contains:

```text
username=admin
password=MySecret123
```

We should avoid exposing the password in logs.

```python
import re

config = """
username=admin
password=MySecret123
"""

safe_config = re.sub(
    r"(?i)(password\s*=\s*)\S+",
    r"\1********",
    config
)

print(safe_config)
```

Output:

```text
username=admin
password=********
```

This technique can be used when sanitizing command output or configuration data before logging it.

---

# 17. `re.subn()`

`subn()` works like `sub()`, but also returns the number of replacements.

### Example

```python
import re

text = "ERROR ERROR ERROR"

result, count = re.subn(
    r"ERROR",
    "WARNING",
    text
)

print(result)
print("Replacements:", count)
```

Output:

```text
WARNING WARNING WARNING
Replacements: 3
```

## DevOps Use

Useful when modifying configuration files and verifying how many replacements were performed.

---

# 18. `re.compile()`

## Purpose

`compile()` creates a reusable regex pattern.

Instead of repeatedly writing:

```python
re.search(pattern, text1)
re.search(pattern, text2)
re.search(pattern, text3)
```

compile it once:

```python
import re

ip_pattern = re.compile(
    r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
)

print(ip_pattern.findall("Server 192.168.22.10"))
print(ip_pattern.findall("Server 192.168.22.11"))
print(ip_pattern.findall("Server 192.168.22.12"))
```

## DevOps Example — Process Many Log Lines

```python
import re

ip_pattern = re.compile(
    r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
)

logs = [
    "Connection from 192.168.22.10",
    "Connection from 192.168.22.11",
    "Connection from 192.168.22.12"
]

for log in logs:
    ips = ip_pattern.findall(log)
    print(ips)
```

`compile()` is particularly useful when the same pattern is reused repeatedly.

---

# 19. `re.escape()`

## Purpose

Escapes regex metacharacters so that a string can be treated as literal text.

### Example

```python
import re

text = "server.example.com"

pattern = re.escape(text)

print(pattern)
```

Output:

```text
server\.example\.com
```

This is useful when a pattern contains text supplied by a user or configuration and that text should be matched literally.

---

# 20. Important Regex Character Classes

## `[abc]`

Matches one character from `a`, `b`, or `c`.

```python
import re

print(re.findall(r"[abc]", "kubernetes"))
```

---

## `[0-9]`

Matches a digit.

```python
import re

print(re.findall(r"[0-9]+", "node123 worker456"))
```

Output:

```text
['123', '456']
```

---

## `[a-z]`

Matches lowercase letters.

```python
r"[a-z]+"
```

---

## `[A-Z]`

Matches uppercase letters.

```python
r"[A-Z]+"
```

---

## `[a-zA-Z]`

Matches English letters.

```python
r"[a-zA-Z]+"
```

---

# 21. Important Regex Metacharacters

| Regex | Meaning |
|---|---|
| `.` | Any character except newline by default |
| `^` | Beginning of string/line |
| `$` | End of string/line |
| `*` | Zero or more |
| `+` | One or more |
| `?` | Zero or one |
| `{n}` | Exactly n |
| `{n,m}` | Between n and m |
| `[]` | Character class |
| `()` | Capturing group |
| `|` | OR |
| `\d` | Digit |
| `\D` | Not a digit |
| `\w` | Word character |
| `\W` | Not a word character |
| `\s` | Whitespace |
| `\S` | Non-whitespace |
| `\b` | Word boundary |

---

# 22. `\d`

Matches digits.

```python
import re

text = "CPU 75%"

print(re.findall(r"\d+", text))
```

Output:

```text
['75']
```

---

# 23. `\w`

Matches word characters.

Generally includes:

```text
letters
digits
underscore
```

Example:

```python
import re

text = "node_01 worker_02"

print(re.findall(r"\w+", text))
```

Output:

```text
['node_01', 'worker_02']
```

---

# 24. `\s`

Matches whitespace.

```python
import re

text = "hello     world"

print(re.split(r"\s+", text))
```

Output:

```text
['hello', 'world']
```

---

# 25. `\S`

Matches non-whitespace characters.

```python
import re

text = "Pod nginx Running"

print(re.findall(r"\S+", text))
```

Output:

```text
['Pod', 'nginx', 'Running']
```

---

# 26. `\b` — Word Boundary

Useful when searching logs.

```python
import re

text = "ERROR ERROR123 MYERROR ERROR"

errors = re.findall(
    r"\bERROR\b",
    text
)

print(errors)
```

Output:

```text
['ERROR', 'ERROR']
```

It does not match:

```text
ERROR123
MYERROR
```

---

# 27. `^` — Beginning

```python
import re

text = "ERROR: Pod failed"

if re.search(r"^ERROR", text):
    print("Error line")
```

---

# 28. `$` — End

```python
import re

text = "Pod status: Running"

if re.search(r"Running$", text):
    print("Pod is running")
```

---

# 29. `.` — Any Character

```python
import re

text = "cat cot cut"

print(re.findall(r"c.t", text))
```

Output:

```text
['cat', 'cot', 'cut']
```

---

# 30. `*` — Zero or More

```python
r"ab*"
```

Can match:

```text
a
ab
abb
abbb
```

Example:

```python
import re

text = "a ab abb abbb"

print(re.findall(r"ab*", text))
```

---

# 31. `+` — One or More

```python
r"ab+"
```

Can match:

```text
ab
abb
abbb
```

but not:

```text
a
```

---

# 32. `?` — Zero or One

Example:

```python
import re

pattern = r"https?"

print(re.findall(pattern, "http https ftp"))
```

Output:

```text
['http', 'https']
```

---

# 33. `{n}` — Exactly n

```python
import re

text = "123 1234 12345"

print(re.findall(r"\d{4}", text))
```

Output:

```text
['1234', '1234']
```

---

# 34. `{n,m}` — Between n and m

```python
import re

text = "1 12 123 1234 12345"

print(re.findall(r"\d{2,4}", text))
```

---

# 35. `|` — OR

```python
import re

text = "ERROR WARNING INFO ERROR"

result = re.findall(
    r"ERROR|WARNING",
    text
)

print(result)
```

Output:

```text
['ERROR', 'WARNING', 'ERROR']
```

A DevOps log filter can use:

```python
r"ERROR|FAILED|CRITICAL"
```

---

# 36. Raw Strings `r""`

You will frequently see:

```python
r"\d+\.\d+\.\d+\.\d+"
```

instead of:

```python
"\\d+\\.\\d+\\.\\d+\\.\\d+"
```

Raw strings make regex patterns easier to read because backslashes are handled more conveniently by Python's string syntax.

For regex, prefer:

```python
r"\d+"
```

---

# 37. DevOps Example — Extract IP Addresses

A common IPv4-shaped regex is:

```python
r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
```

Example:

```python
import re

text = """
API Server: 192.168.22.10
Worker1: 192.168.22.211
Worker2: 192.168.22.212
"""

ips = re.findall(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    text
)

for ip in ips:
    print(ip)
```

Output:

```text
192.168.22.10
192.168.22.211
192.168.22.212
```

For strict IP validation, prefer:

```python
import ipaddress

ipaddress.ip_address("192.168.22.10")
```

---

# 38. DevOps Example — Extract Port Numbers

```python
import re

text = """
nginx listening on port 80
https listening on port 443
kubernetes API port 6443
"""

ports = re.findall(
    r"\bport\s+(\d+)",
    text,
    re.IGNORECASE
)

print(ports)
```

Output:

```text
['80', '443', '6443']
```

---

# 39. DevOps Example — Extract Kubernetes/OpenShift Versions

```python
import re

text = """
Kubernetes v1.33.6
OpenShift 4.20.13
"""

versions = re.findall(
    r"\bv?\d+\.\d+\.\d+\b",
    text
)

print(versions)
```

Output:

```text
['v1.33.6', '4.20.13']
```

---

# 40. `re.IGNORECASE`

Makes matching case-insensitive.

```python
import re

text = "error ERROR Error eRrOr"

result = re.findall(
    r"error",
    text,
    re.IGNORECASE
)

print(result)
```

Output:

```text
['error', 'ERROR', 'Error', 'eRrOr']
```

---

# 41. `re.MULTILINE`

Changes `^` and `$` so they can match individual lines in multiline text.

```python
import re

text = """ERROR Pod failed
INFO Pod started
ERROR Service failed
"""

errors = re.findall(
    r"^ERROR.*$",
    text,
    re.MULTILINE
)

print(errors)
```

Output:

```text
['ERROR Pod failed', 'ERROR Service failed']
```

This is extremely useful for log files.

---

# 42. `re.DOTALL`

Normally `.` does not match newline characters.

With `re.DOTALL`, it does.

```python
import re

text = """START
line1
line2
END"""

result = re.search(
    r"START.*END",
    text,
    re.DOTALL
)

if result:
    print(result.group())
```

Output:

```text
START
line1
line2
END
```

---

# 43. Combining Regex Flags

Flags can be combined using `|`.

```python
import re

pattern = re.compile(
    r"^error.*$",
    re.IGNORECASE | re.MULTILINE
)
```

---

# 44. DevOps Example — Parse `df -h`

Suppose command output is:

```text
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   40G   10G  80% /
/dev/sdb1       100G   95G    5G  95% /data
```

We want to identify filesystems at or above 90%.

```python
import re

output = """
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   40G   10G  80% /
/dev/sdb1       100G   95G    5G  95% /data
"""

pattern = (
    r"(\S+)\s+\S+\s+\S+\s+\S+"
    r"\s+(\d+)%\s+(\S+)"
)

for match in re.finditer(pattern, output):

    filesystem = match.group(1)
    usage = int(match.group(2))
    mount = match.group(3)

    if usage >= 90:
        print(
            f"ALERT: {filesystem} "
            f"{usage}% used on {mount}"
        )
```

Output:

```text
ALERT: /dev/sdb1 95% used on /data
```

---

# 45. DevOps Example — Parse `systemctl`

Suppose:

```text
● nginx.service - nginx
   Loaded: loaded
   Active: active (running)
```

Python:

```python
import re

output = """
● nginx.service - nginx
   Loaded: loaded
   Active: active (running)
"""

match = re.search(
    r"Active:\s+(\S+)",
    output
)

if match:
    status = match.group(1)
    print("Service status:", status)
```

Output:

```text
Service status: active
```

---

# 46. DevOps Example — Parse `oc get nodes`

Suppose:

```text
NAME       STATUS     ROLES
ocp-cp-1   Ready      master
ocp-cp-2   Ready      master
ocp-w-1    Ready      worker
ocp-w-2    NotReady   worker
```

Detect `NotReady` nodes:

```python
import re

output = """
ocp-cp-1   Ready      master
ocp-cp-2   Ready      master
ocp-w-1    Ready      worker
ocp-w-2    NotReady   worker
"""

pattern = r"^(\S+)\s+NotReady\b.*$"

for match in re.finditer(
    pattern,
    output,
    re.MULTILINE
):
    print("Problem node:", match.group(1))
```

Output:

```text
Problem node: ocp-w-2
```

For production OpenShift automation, prefer:

```bash
oc get nodes -o json
```

and parse JSON with Python's `json` module instead of relying on table formatting.

---

# 47. DevOps Example — Extract URLs

```python
import re

text = """
Jenkins: https://jenkins.example.com
GitLab: https://gitlab.example.com
Registry: http://registry.example.com
"""

urls = re.findall(
    r"https?://[^\s]+",
    text
)

for url in urls:
    print(url)
```

Output:

```text
https://jenkins.example.com
https://gitlab.example.com
http://registry.example.com
```

---

# 48. DevOps Example — Extract Email Addresses

```python
import re

text = """
Contact devops@example.com
Support support@example.org
"""

emails = re.findall(
    r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b",
    text
)

print(emails)
```

Output:

```text
['devops@example.com', 'support@example.org']
```

---

# 49. DevOps Example — Detect Errors in Logs

```python
import re

logs = """
INFO Pod started
INFO Service created
ERROR Connection refused
WARNING Disk usage high
CRITICAL Database unavailable
"""

pattern = re.compile(
    r"\b(ERROR|WARNING|CRITICAL)\b"
)

for line in logs.splitlines():

    match = pattern.search(line)

    if match:
        print(
            match.group(1),
            "=>",
            line
        )
```

Output:

```text
ERROR => ERROR Connection refused
WARNING => WARNING Disk usage high
CRITICAL => CRITICAL Database unavailable
```

---

# 50. DevOps Example — Extract Error Lines

```python
import re

log_file = """
INFO Starting application
ERROR Database connection failed
INFO Retrying
ERROR Connection timeout
INFO Application stopped
"""

errors = re.findall(
    r"(?im)^ERROR.*$",
    log_file
)

for error in errors:
    print(error)
```

Output:

```text
ERROR Database connection failed
ERROR Connection timeout
```

Here:

```text
(?i) = case-insensitive
(?m) = multiline
^    = beginning of line
$    = end of line
```

---

# 51. DevOps Example — Regex + `subprocess`

Regex becomes especially useful when combined with command execution.

```python
import subprocess
import re

result = subprocess.run(
    ["systemctl", "status", "sshd"],
    capture_output=True,
    text=True
)

output = result.stdout + result.stderr

match = re.search(
    r"Active:\s+(\S+)",
    output
)

if match:
    status = match.group(1)

    if status == "active":
        print("SSH service is running")
    else:
        print("SSH service is NOT running")
```

Concept:

```text
subprocess
    |
    v
Command output
    |
    v
re module
    |
    v
Extract information
    |
    v
Automation decision
```

---

# 52. DevOps Example — Regex + Log File

```python
import re

with open("/var/log/messages") as file:

    for line in file:

        if re.search(
            r"\b(ERROR|CRITICAL|FAILED)\b",
            line,
            re.IGNORECASE
        ):
            print(line.strip())
```

This can be used as a simple log-monitoring script.

---

# 53. DevOps Example — Parse Ansible Output

Suppose:

```text
changed=3
failed=1
unreachable=0
```

Extract values:

```python
import re

output = """
changed=3
failed=1
unreachable=0
"""

changed = re.search(
    r"changed=(\d+)",
    output
).group(1)

failed = re.search(
    r"failed=(\d+)",
    output
).group(1)

print("Changed:", changed)
print("Failed:", failed)
```

Output:

```text
Changed: 3
Failed: 1
```

---

# 54. Better Approach — Named Groups

```python
import re

text = "changed=3 failed=1 unreachable=0"

pattern = re.compile(
    r"changed=(?P<changed>\d+)\s+"
    r"failed=(?P<failed>\d+)\s+"
    r"unreachable=(?P<unreachable>\d+)"
)

match = pattern.search(text)

if match:
    data = match.groupdict()
    print(data)
```

Output:

```text
{
    'changed': '3',
    'failed': '1',
    'unreachable': '0'
}
```

This is easier to maintain than relying heavily on numeric group indexes.

---

# 55. Greedy vs Non-Greedy Matching

Regex quantifiers such as `*` and `+` are normally greedy.

Example:

```python
import re

text = "<start>hello</start><start>world</start>"

result = re.search(
    r"<start>.*</start>",
    text
)

print(result.group())
```

A greedy `.*` can consume from the first `<start>` to the last `</start>`.

For non-greedy matching, use `.*?`:

```python
import re

results = re.findall(
    r"<start>(.*?)</start>",
    text
)

print(results)
```

Output:

```text
['hello', 'world']
```

---

# 56. Realistic DevOps Log Parser

Input:

```text
2026-10-01 10:20:30 ERROR nginx 192.168.22.10 Connection refused
2026-10-01 10:21:30 INFO nginx 192.168.22.11 Request successful
```

Python:

```python
import re

logs = """
2026-10-01 10:20:30 ERROR nginx 192.168.22.10 Connection refused
2026-10-01 10:21:30 INFO nginx 192.168.22.11 Request successful
"""

pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>\w+)\s+"
    r"(?P<service>\S+)\s+"
    r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+"
    r"(?P<message>.*)"
)

for line in logs.splitlines():

    match = pattern.search(line)

    if match:
        data = match.groupdict()

        print("Date:", data["date"])
        print("Time:", data["time"])
        print("Level:", data["level"])
        print("Service:", data["service"])
        print("IP:", data["ip"])
        print("Message:", data["message"])
        print("---")
```

This demonstrates a common DevOps pattern:

```text
Raw log
   |
   v
Regex pattern
   |
   v
Named groups
   |
   v
Dictionary
   |
   v
Automation / alert / report
```

---

# 57. Important `re` Functions Cheat Sheet

| Function | Purpose | DevOps Example |
|---|---|---|
| `re.search()` | First match anywhere | Find IP/error/version |
| `re.match()` | Match from beginning | Check log prefix |
| `re.fullmatch()` | Entire string | Validate names |
| `re.findall()` | All matching values | Extract IPs/ports |
| `re.finditer()` | Match objects | Value + position |
| `re.split()` | Regex-based split | Parse lists/config |
| `re.sub()` | Replace matches | Sanitize secrets |
| `re.subn()` | Replace + count | Verify replacements |
| `re.compile()` | Reusable regex | Large log processing |
| `re.escape()` | Escape literal text | Dynamic patterns |

---

# 58. Important Regex Patterns for DevOps

```python
# IPv4-shaped address
r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

# Number
r"\d+"

# Word
r"\w+"

# Non-whitespace
r"\S+"

# Whitespace
r"\s+"

# Email
r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"

# URL
r"https?://[^\s]+"

# Version
r"\bv?\d+\.\d+\.\d+\b"

# Error / warning / critical
r"\b(ERROR|FAILED|CRITICAL)\b"

# Line beginning with ERROR
r"^ERROR.*$"

# key=value
r"(\w+)=(\S+)"

# Kubernetes/OpenShift-style DNS label
r"[a-z0-9]([-a-z0-9]*[a-z0-9])?"
```

These patterns should be adapted to the exact data format rather than blindly reused for every situation.

---

# 59. `match()` vs `search()` vs `fullmatch()`

This is an important interview topic.

| Function | Matching behavior |
|---|---|
| `re.match()` | Beginning of string |
| `re.search()` | Anywhere in string |
| `re.fullmatch()` | Entire string |

Example:

```python
text = "Hello ERROR World"
```

### `match()`

```python
re.match(r"ERROR", text)
```

Result:

```text
None
```

### `search()`

```python
re.search(r"ERROR", text)
```

Finds:

```text
ERROR
```

### `fullmatch()`

```python
re.fullmatch(r"ERROR", text)
```

Result:

```text
None
```

because the complete string is not exactly `ERROR`.

---

# 60. `findall()` vs `finditer()`

## `findall()`

```python
import re

text = "IP 192.168.1.1 IP 192.168.1.2"

result = re.findall(
    r"\d+\.\d+\.\d+\.\d+",
    text
)

print(result)
```

Output:

```text
['192.168.1.1', '192.168.1.2']
```

## `finditer()`

```python
for match in re.finditer(
    r"\d+\.\d+\.\d+\.\d+",
    text
):
    print(match.group())
```

Use `finditer()` when you need match metadata such as:

```text
start()
end()
group()
groups()
groupdict()
```

---

# 61. Regex + Structured Data: Important DevOps Rule

Regex is powerful, but it should not be used for everything.

Prefer structured parsers when the source is structured.

| Data | Prefer |
|---|---|
| JSON | `json` module |
| YAML | `yaml` module |
| XML | XML parser |
| IP address | `ipaddress` module |
| URLs | Appropriate URL parser |
| Kubernetes/OpenShift | `oc/kubectl -o json` + `json` |
| Unstructured logs | `re` |
| Legacy command output | `re` when necessary |

For example, instead of parsing:

```bash
oc get pods
```

with regex, prefer:

```bash
oc get pods -o json
```

and then:

```python
import json
```

This is usually more reliable because table formatting can change.

---

# 62. Complete DevOps Example

The following script combines:

- `subprocess`
- `re`
- Log/error detection
- IP extraction
- Version extraction
- Named groups

```python
import subprocess
import re


def run_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return result.stdout + result.stderr


output = run_command(["ip", "addr"])

ip_pattern = re.compile(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
)

ips = ip_pattern.findall(output)

print("Detected IP addresses:")

for ip in ips:
    print(ip)


log_text = """
2026-10-01 10:20:30 ERROR nginx 192.168.22.10 Connection refused
2026-10-01 10:21:30 INFO nginx 192.168.22.11 Request successful
"""

log_pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>\w+)\s+"
    r"(?P<service>\S+)\s+"
    r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+"
    r"(?P<message>.*)"
)

for line in log_text.splitlines():

    match = log_pattern.search(line)

    if not match:
        continue

    data = match.groupdict()

    if data["level"] in {"ERROR", "CRITICAL"}:
        print(
            f"ALERT: {data['service']} "
            f"on {data['ip']} - "
            f"{data['message']}"
        )
```

---

# 63. Recommended Learning Order

For a DevOps engineer, learn regex in this order:

## Level 1 — Basic

Learn:

```text
\d
\w
\s
\S
.
+
*
?
```

## Level 2 — Position

Learn:

```text
^
$
\b
```

## Level 3 — Groups

Learn:

```text
()
(?P<name>...)
group()
group(1)
groupdict()
```

## Level 4 — `re` Functions

Master:

```text
search()
match()
fullmatch()
findall()
finditer()
split()
sub()
subn()
compile()
```

## Level 5 — Flags

Learn:

```text
re.IGNORECASE
re.MULTILINE
re.DOTALL
re.VERBOSE
```

## Level 6 — DevOps Automation

Practice with:

```text
Linux logs
df -h
systemctl
ip addr
ss -lntp
Ansible output
Jenkins output
OpenShift output
Kubernetes logs
configuration files
monitoring output
```

---

# 64. Interview Questions

## Q1. What is the `re` module?

**Answer:**

The Python `re` module provides regular-expression functionality for searching, extracting, validating, replacing, and splitting text. In DevOps automation, it is commonly used for log parsing, command-output processing, configuration processing, and extracting information such as IP addresses, versions, and errors.

---

## Q2. Difference between `match()` and `search()`?

```text
re.match()
    |
    +-- checks from beginning

re.search()
    |
    +-- searches anywhere
```

---

## Q3. Difference between `findall()` and `finditer()`?

```text
findall()
    -> returns matching values

finditer()
    -> returns match objects
```

Use `finditer()` when you need positions or additional match metadata.

---

## Q4. Why use `re.compile()`?

`re.compile()` creates a reusable regex pattern.

It is useful when the same regex pattern is applied repeatedly, especially in log-processing or automation scripts.

---

## Q5. What is a capturing group?

Parentheses create a capturing group:

```python
r"IP=(\S+)"
```

Then:

```python
match.group(1)
```

returns the captured value.

---

## Q6. What is a named group?

Example:

```python
r"IP=(?P<ip>\S+)"
```

Then:

```python
match.group("ip")
```

can retrieve the value.

---

## Q7. Why use raw strings in regex?

Instead of:

```python
"\\d+"
```

we can write:

```python
r"\d+"
```

which makes regex patterns easier to read and maintain.

---

# 65. Final DevOps Cheat Sheet

```python
import re

# Search
re.search(pattern, text)

# Match from beginning
re.match(pattern, text)

# Match entire string
re.fullmatch(pattern, text)

# Find all matches
re.findall(pattern, text)

# Iterate over matches
re.finditer(pattern, text)

# Split
re.split(pattern, text)

# Replace
re.sub(pattern, replacement, text)

# Replace and count
re.subn(pattern, replacement, text)

# Compile reusable pattern
re.compile(pattern)

# Escape literal text
re.escape(text)
```

Most important regex symbols:

```text
\d      digit
\D      non-digit
\w      word character
\W      non-word character
\s      whitespace
\S      non-whitespace
\b      word boundary

.       any character
^       beginning
$       end

*       zero or more
+       one or more
?       zero or one
{n}     exactly n
{n,m}   n to m

[]      character class
()      capturing group
|       OR
```

---

# 66. Key Takeaway for DevOps

Think about the `re` module like this:

```text
                 Logs / Command Output
                          |
                          v
                    Python re
                          |
             +------------+------------+
             |            |            |
             v            v            v
          Search       Extract       Replace
             |            |            |
          search()     findall()     sub()
          match()      finditer()    subn()
          fullmatch()
             |            |            |
             +------------+------------+
                          |
                          v
                  Automation Logic
                          |
              +-----------+-----------+
              |           |           |
              v           v           v
            Alert       Report       Action
```

For DevOps automation, focus first on:

```python
re.search()
re.match()
re.fullmatch()
re.findall()
re.finditer()
re.split()
re.sub()
re.compile()
```

and master:

```text
\d  \w  \s  \S  \b
.   *   +   ?   {}
[]  ()  ^   $   |
```

Once these are comfortable, practice them against real Linux logs, `systemctl`, `df -h`, `ip addr`, Ansible/Jenkins output, Kubernetes/OpenShift logs, and configuration files.