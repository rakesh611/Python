# Python `socket`, `ssl`, and `http.client` Modules for DevOps Engineers

## 1. Introduction

Python provides several standard-library modules that are extremely useful for DevOps and infrastructure automation.

Three important modules are:

| Module | Main Purpose | Typical DevOps Use |
|---|---|---|
| `socket` | Low-level network communication | Port checks, DNS lookup, TCP connectivity |
| `ssl` | TLS/SSL communication and certificate handling | HTTPS checks, certificate inspection, TLS validation |
| `http.client` | Low-level HTTP/HTTPS client | REST API health checks, HTTP status validation |

These modules are especially useful when you want to build lightweight monitoring or troubleshooting scripts without installing third-party packages.

---

# 2. `socket` Module

## 2.1 What is `socket`?

The Python `socket` module provides access to the operating system's network socket interface.

A socket is an endpoint used for communication between two systems or processes.

For example:

```text
Python Script
     |
     | TCP connection
     v
192.168.22.10:389
     |
     v
LDAP Server
```

A DevOps engineer can use sockets to:

- Check whether a TCP port is reachable
- Resolve hostnames
- Test network connectivity
- Create TCP/UDP clients
- Build simple network services
- Troubleshoot firewall/network problems

---

## 2.2 Importing the module

```python
import socket
```

---

# 3. Important `socket` Functions and Classes

## 3.1 `socket.gethostname()`

Returns the hostname of the local machine.

### Example

```python
import socket

hostname = socket.gethostname()

print("Hostname:", hostname)
```

Possible output:

```text
Hostname: ocp-svc.lab.ocp.lan
```

### DevOps use

Useful when generating host-specific logs or monitoring information.

---

## 3.2 `socket.getfqdn()`

Returns the fully qualified domain name.

```python
import socket

print(socket.getfqdn())
```

Possible output:

```text
ocp-svc.lab.ocp.lan
```

This is useful in infrastructure scripts where FQDN information matters.

---

## 3.3 `socket.gethostbyname()`

Resolves a hostname to an IPv4 address.

```python
import socket

ip = socket.gethostbyname("ldap.lab.ocp.lan")

print("IP:", ip)
```

Possible output:

```text
IP: 192.168.22.10
```

### DevOps use

Useful for:

- DNS troubleshooting
- Service discovery checks
- Validating internal DNS
- Checking application endpoints

---

## 3.4 `socket.gethostbyname_ex()`

Returns hostname, aliases, and IP addresses.

```python
import socket

result = socket.gethostbyname_ex("localhost")

print("Hostname:", result[0])
print("Aliases:", result[1])
print("Addresses:", result[2])
```

---

## 3.5 `socket.getaddrinfo()`

One of the most useful functions for DevOps network troubleshooting.

It returns address information for a hostname/service.

```python
import socket

results = socket.getaddrinfo(
    "google.com",
    443,
    type=socket.SOCK_STREAM
)

for result in results:
    print(result)
```

It can provide information about:

- Address family
- Socket type
- Protocol
- Canonical name
- Socket address

---

# 4. Checking TCP Port Connectivity

This is one of the most useful DevOps applications of `socket`.

## 4.1 `socket.create_connection()`

Creates a TCP connection to a host and port.

```python
import socket

host = "192.168.22.10"
port = 389

try:
    sock = socket.create_connection((host, port), timeout=5)
    print(f"{host}:{port} is reachable")
    sock.close()

except socket.timeout:
    print(f"{host}:{port} connection timed out")

except OSError as e:
    print(f"{host}:{port} is not reachable: {e}")
```

### DevOps troubleshooting

Suppose LDAP is expected on:

```text
192.168.22.10:389
```

This test tells you whether a TCP connection can be established.

It does **not** prove that LDAP itself is healthy. It only proves TCP connectivity.

---

# 5. `socket.socket()`

The `socket.socket()` class creates a socket object.

Basic TCP socket:

```python
import socket

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

sock.connect(("192.168.22.10", 389))

print("Connected")

sock.close()
```

### Important parameters

```python
socket.socket(
    family,
    type,
    proto=0
)
```

Common values:

| Constant | Meaning |
|---|---|
| `AF_INET` | IPv4 |
| `AF_INET6` | IPv6 |
| `SOCK_STREAM` | TCP |
| `SOCK_DGRAM` | UDP |

---

# 6. `socket.settimeout()`

Sets a timeout for socket operations.

```python
import socket

sock = socket.socket()

sock.settimeout(3)

try:
    sock.connect(("192.168.22.10", 389))
    print("Connected")
except socket.timeout:
    print("Connection timed out")
finally:
    sock.close()
```

### Why timeout matters in DevOps

Without a timeout, a network automation script can potentially wait for a long time.

Always consider timeouts for network checks.

---

# 7. `socket.close()`

Closes the socket.

```python
sock.close()
```

Prefer a context manager where possible:

```python
import socket

with socket.create_connection(("192.168.22.10", 389), timeout=5) as sock:
    print("Connected")
```

The socket is automatically closed when the `with` block finishes.

---

# 8. `socket.send()` and `socket.recv()`

These are used for sending and receiving data through a connected socket.

Example:

```python
import socket

with socket.create_connection(("example.com", 80), timeout=5) as sock:

    request = b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"

    sock.send(request)

    response = sock.recv(4096)

    print(response.decode(errors="ignore"))
```

This demonstrates what an HTTP client does at a lower level.

---

# 9. DevOps Example: Multi-Port Checker

A common DevOps task is checking whether required infrastructure ports are reachable.

```python
import socket

servers = {
    "LDAP": ("192.168.22.10", 389),
    "HTTPS": ("192.168.22.1", 443),
    "Kubernetes API": ("192.168.22.201", 6443),
    "DNS": ("192.168.22.1", 53),
}

for service, (host, port) in servers.items():

    try:
        with socket.create_connection((host, port), timeout=3):
            print(f"[OK]   {service}: {host}:{port}")

    except socket.timeout:
        print(f"[TIMEOUT] {service}: {host}:{port}")

    except OSError as e:
        print(f"[FAILED] {service}: {host}:{port} - {e}")
```

Possible output:

```text
[OK]   LDAP: 192.168.22.10:389
[OK]   HTTPS: 192.168.22.1:443
[OK]   Kubernetes API: 192.168.22.201:6443
[TIMEOUT] DNS: 192.168.22.1:53
```

---

# 10. `ssl` Module

## 10.1 What is `ssl`?

Python's `ssl` module provides TLS/SSL support.

It is commonly used to secure network communication.

Example:

```text
Python
  |
  | TLS
  v
HTTPS Server
  |
  +-- Certificate
  +-- Encryption
  +-- Authentication
```

DevOps engineers commonly use it for:

- HTTPS testing
- TLS certificate inspection
- Certificate expiry monitoring
- TLS version validation
- Secure socket connections
- mTLS/client certificate testing

---

# 11. Importing `ssl`

```python
import ssl
```

---

# 12. `ssl.create_default_context()`

This is one of the most important functions in the module.

```python
import ssl

context = ssl.create_default_context()

print(context)
```

It creates a secure TLS context with appropriate default certificate verification settings.

For production automation, prefer secure defaults instead of disabling certificate verification.

---

# 13. `ssl.create_connection()`

`ssl.create_connection()` can establish a TLS connection.

Example:

```python
import ssl

context = ssl.create_default_context()

with context.wrap_socket(
    socket.socket(),
    server_hostname="example.com"
) as sock:

    sock.settimeout(5)
    sock.connect(("example.com", 443))

    print("TLS connection established")
```

A simpler and often preferable pattern is:

```python
import socket
import ssl

context = ssl.create_default_context()

with socket.create_connection(("example.com", 443), timeout=5) as raw_sock:
    with context.wrap_socket(
        raw_sock,
        server_hostname="example.com"
    ) as tls_sock:

        print("TLS version:", tls_sock.version())
        print("Cipher:", tls_sock.cipher())
```

---

# 14. `SSLContext`

`SSLContext` is the central object for configuring TLS behavior.

Example:

```python
import ssl

context = ssl.create_default_context()

print("Minimum TLS version:", context.minimum_version)
print("Maximum TLS version:", context.maximum_version)
```

You can configure a TLS version when required:

```python
context.minimum_version = ssl.TLSVersion.TLSv1_2
```

For example, a DevOps policy may require TLS 1.2 or newer.

---

# 15. `ssl.PROTOCOL_TLS_CLIENT`

You may also explicitly create a client TLS context:

```python
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

context.load_default_certs()
```

For normal HTTPS clients, `ssl.create_default_context()` is usually more convenient.

---

# 16. `SSLContext.wrap_socket()`

Wraps a normal socket with TLS.

```python
import socket
import ssl

context = ssl.create_default_context()

with socket.create_connection(("example.com", 443), timeout=5) as raw_socket:

    with context.wrap_socket(
        raw_socket,
        server_hostname="example.com"
    ) as tls_socket:

        print("Connected using:", tls_socket.version())
```

---

# 17. `SSLSocket.version()`

Returns the negotiated TLS version.

```python
print(tls_socket.version())
```

Possible output:

```text
TLSv1.3
```

### DevOps use

Useful when validating TLS hardening.

For example:

```text
Expected: TLS 1.2 or TLS 1.3
Actual:   TLS 1.3
Result:   PASS
```

---

# 18. `SSLSocket.cipher()`

Returns information about the negotiated cipher.

```python
print(tls_socket.cipher())
```

Possible output:

```text
('TLS_AES_256_GCM_SHA384', 'TLSv1.3', 256)
```

---

# 19. `SSLSocket.getpeercert()`

Returns information about the peer certificate.

```python
certificate = tls_socket.getpeercert()

print(certificate)
```

Example fields may include:

```text
subject
issuer
version
serialNumber
notBefore
notAfter
subjectAltName
```

---

# 20. DevOps Example: Check HTTPS TLS Certificate

```python
import socket
import ssl
from datetime import datetime

hostname = "example.com"
port = 443

context = ssl.create_default_context()

with socket.create_connection((hostname, port), timeout=5) as raw_socket:

    with context.wrap_socket(
        raw_socket,
        server_hostname=hostname
    ) as tls_socket:

        certificate = tls_socket.getpeercert()

        print("TLS version:", tls_socket.version())
        print("Cipher:", tls_socket.cipher())
        print("Certificate subject:", certificate.get("subject"))
        print("Certificate issuer:", certificate.get("issuer"))
        print("Valid from:", certificate.get("notBefore"))
        print("Valid until:", certificate.get("notAfter"))
```

---

# 21. Certificate Expiry Monitoring

A practical DevOps requirement is checking whether an HTTPS certificate will expire soon.

```python
import socket
import ssl
from datetime import datetime, timezone

hostname = "example.com"

context = ssl.create_default_context()

with socket.create_connection((hostname, 443), timeout=5) as raw_socket:

    with context.wrap_socket(
        raw_socket,
        server_hostname=hostname
    ) as tls_socket:

        cert = tls_socket.getpeercert()

        expiry = datetime.strptime(
            cert["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        ).replace(tzinfo=timezone.utc)

        remaining = expiry - datetime.now(timezone.utc)

        print("Certificate expires:", expiry)
        print("Remaining:", remaining.days, "days")

        if remaining.days < 30:
            print("WARNING: Certificate expires in less than 30 days")
        else:
            print("Certificate is OK")
```

This type of script can be integrated into:

- Cron
- Jenkins
- GitLab CI/CD
- Ansible workflows
- Monitoring systems

---

# 22. `ssl.get_server_certificate()`

Returns the PEM certificate presented by a server.

```python
import ssl

certificate = ssl.get_server_certificate(
    ("example.com", 443)
)

print(certificate)
```

The result looks similar to:

```text
-----BEGIN CERTIFICATE-----
MIIF...
...
-----END CERTIFICATE-----
```

This is useful when you need to retrieve a server certificate for inspection.

---

# 23. `ssl.match_hostname()`

Checks whether a certificate matches a hostname.

Conceptually:

```python
ssl.match_hostname(cert, "example.com")
```

However, modern TLS clients should normally rely on an appropriately configured `SSLContext` rather than manually implementing certificate hostname verification.

---

# 24. TLS Troubleshooting Example

Suppose your OpenShift/LDAP environment has:

```text
LDAP FQDN: ldap.lab.ocp.lan
Port:      636
Protocol:  LDAPS
```

You can test the TLS handshake:

```python
import socket
import ssl

hostname = "ldap.lab.ocp.lan"
port = 636

context = ssl.create_default_context()

try:
    with socket.create_connection(
        (hostname, port),
        timeout=5
    ) as raw_socket:

        with context.wrap_socket(
            raw_socket,
            server_hostname=hostname
        ) as tls_socket:

            print("[OK] TLS handshake successful")
            print("TLS version:", tls_socket.version())
            print("Cipher:", tls_socket.cipher())

except ssl.SSLCertVerificationError as e:
    print("[CERTIFICATE ERROR]", e)

except ssl.SSLError as e:
    print("[TLS ERROR]", e)

except OSError as e:
    print("[NETWORK ERROR]", e)
```

This helps distinguish:

```text
DNS problem
   |
   +--> TCP problem
           |
           +--> TLS handshake problem
                    |
                    +--> Certificate validation problem
```

---

# 25. `http.client` Module

## 25.1 What is `http.client`?

`http.client` is Python's low-level HTTP client module.

It can communicate with HTTP and HTTPS servers without requiring external libraries such as `requests`.

Example:

```text
Python Script
     |
     | HTTP/HTTPS
     v
Web Server / REST API
```

DevOps uses include:

- API health checks
- HTTP status validation
- Kubernetes/OpenShift API testing
- Web application checks
- Internal service testing
- Automation scripts

---

# 26. Importing `http.client`

```python
import http.client
```

---

# 27. `HTTPConnection`

Used for HTTP connections.

```python
import http.client

connection = http.client.HTTPConnection(
    "example.com",
    80,
    timeout=5
)

connection.request("GET", "/")

response = connection.getresponse()

print(response.status)
print(response.reason)

connection.close()
```

Possible output:

```text
200
OK
```

---

# 28. `HTTPSConnection`

Used for HTTPS connections.

```python
import http.client

connection = http.client.HTTPSConnection(
    "example.com",
    443,
    timeout=5
)

connection.request("GET", "/")

response = connection.getresponse()

print("Status:", response.status)
print("Reason:", response.reason)

connection.close()
```

---

# 29. `HTTPConnection.request()`

Sends an HTTP request.

Syntax:

```python
connection.request(
    method,
    url,
    body=None,
    headers={}
)
```

Example:

```python
connection.request(
    "GET",
    "/health"
)
```

POST example:

```python
import http.client

connection = http.client.HTTPConnection(
    "localhost",
    8080,
    timeout=5
)

body = '{"status": "check"}'

headers = {
    "Content-Type": "application/json"
}

connection.request(
    "POST",
    "/api/check",
    body=body,
    headers=headers
)

response = connection.getresponse()

print(response.status)
print(response.read().decode())

connection.close()
```

---

# 30. `getresponse()`

Returns the HTTP response.

```python
response = connection.getresponse()
```

You can then inspect:

```python
response.status
response.reason
response.headers
response.read()
```

---

# 31. `HTTPResponse.status`

Returns the HTTP status code.

```python
print(response.status)
```

Examples:

| Status | Meaning |
|---|---|
| `200` | OK |
| `201` | Created |
| `204` | No Content |
| `301` | Redirect |
| `302` | Redirect |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Not Found |
| `500` | Internal Server Error |
| `502` | Bad Gateway |
| `503` | Service Unavailable |

---

# 32. `HTTPResponse.reason`

Returns the status description.

```python
print(response.reason)
```

Example:

```text
200 OK
```

---

# 33. `HTTPResponse.read()`

Reads the response body.

```python
body = response.read()

print(body.decode())
```

For JSON APIs:

```python
import json

data = json.loads(response.read().decode())

print(data)
```

---

# 34. `HTTPResponse.getheaders()`

Returns response headers.

```python
headers = response.getheaders()

for key, value in headers:
    print(key, ":", value)
```

---

# 35. `HTTPResponse.getheader()`

Gets a specific header.

```python
content_type = response.getheader("Content-Type")

print(content_type)
```

---

# 36. DevOps Example: HTTP Health Check

A simple health-check script:

```python
import http.client

host = "localhost"
port = 8080
path = "/health"

try:
    connection = http.client.HTTPConnection(
        host,
        port,
        timeout=5
    )

    connection.request("GET", path)

    response = connection.getresponse()

    if response.status == 200:
        print("[OK] Application is healthy")
    else:
        print(
            f"[FAILED] HTTP status: "
            f"{response.status} {response.reason}"
        )

    connection.close()

except OSError as e:
    print("[ERROR] Could not connect:", e)
```

---

# 37. DevOps Example: HTTPS Health Check

```python
import http.client
import ssl

hostname = "example.com"

context = ssl.create_default_context()

try:
    connection = http.client.HTTPSConnection(
        hostname,
        443,
        timeout=5,
        context=context
    )

    connection.request("GET", "/")

    response = connection.getresponse()

    print("HTTP status:", response.status)
    print("HTTP reason:", response.reason)

    if 200 <= response.status < 400:
        print("[PASS] HTTPS endpoint is healthy")
    else:
        print("[FAIL] HTTPS endpoint returned an error")

    connection.close()

except ssl.SSLError as e:
    print("[TLS ERROR]", e)

except OSError as e:
    print("[NETWORK ERROR]", e)
```

---

# 38. Sending HTTP Headers

Headers are frequently required by APIs.

```python
import http.client

connection = http.client.HTTPConnection(
    "localhost",
    8080,
    timeout=5
)

headers = {
    "Accept": "application/json",
    "User-Agent": "DevOps-Health-Checker/1.0"
}

connection.request(
    "GET",
    "/api/health",
    headers=headers
)

response = connection.getresponse()

print("Status:", response.status)
print("Body:", response.read().decode())

connection.close()
```

---

# 39. Sending JSON POST Requests

```python
import http.client
import json

host = "localhost"
port = 8080

payload = {
    "service": "sonarqube",
    "environment": "lab",
    "check": "health"
}

body = json.dumps(payload)

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

connection = http.client.HTTPConnection(
    host,
    port,
    timeout=5
)

connection.request(
    "POST",
    "/api/health",
    body=body,
    headers=headers
)

response = connection.getresponse()

print("Status:", response.status)

response_body = response.read().decode()

print("Response:", response_body)

connection.close()
```

---

# 40. OpenShift/Kubernetes API Example

The Kubernetes/OpenShift API commonly uses HTTPS.

For example:

```text
https://api.ocp.lan:6443
```

A basic connectivity check can be performed with `HTTPSConnection`.

```python
import http.client
import ssl

host = "api.ocp.lan"
port = 6443

context = ssl.create_default_context()

try:
    connection = http.client.HTTPSConnection(
        host,
        port,
        timeout=5,
        context=context
    )

    connection.request("GET", "/version")

    response = connection.getresponse()

    print("HTTP status:", response.status)
    print("Reason:", response.reason)

    body = response.read().decode()

    print("Response:")
    print(body)

    connection.close()

except Exception as e:
    print("API check failed:", e)
```

> In a real OpenShift/Kubernetes environment, authentication and the cluster CA must be handled correctly. A simple `/version` request is mainly useful for connectivity/API troubleshooting.

---

# 41. Combining `socket`, `ssl`, and `http.client`

These three modules become particularly useful when combined.

A typical troubleshooting flow is:

```text
1. DNS
   |
   v
socket.gethostbyname()
   |
   v
2. TCP connectivity
   |
   v
socket.create_connection()
   |
   v
3. TLS handshake
   |
   v
ssl.SSLContext / wrap_socket()
   |
   v
4. HTTP request
   |
   v
http.client.HTTPSConnection()
   |
   v
5. HTTP status
   |
   v
200 / 401 / 403 / 404 / 500 / 503
```

This is very useful for L2/L3 infrastructure troubleshooting.

---

# 42. Complete DevOps Endpoint Checker

The following script checks:

1. DNS resolution
2. TCP port connectivity
3. TLS connectivity
4. HTTP response

```python
import socket
import ssl
import http.client


def check_endpoint(host, port=443, path="/"):
    print("=" * 60)
    print(f"Checking: {host}:{port}{path}")
    print("=" * 60)

    # 1. DNS
    try:
        ip = socket.gethostbyname(host)
        print(f"[OK] DNS: {host} -> {ip}")

    except socket.gaierror as e:
        print(f"[FAIL] DNS resolution failed: {e}")
        return

    # 2. TCP
    try:
        with socket.create_connection(
            (host, port),
            timeout=5
        ):
            print(f"[OK] TCP: {host}:{port}")

    except socket.timeout:
        print(f"[FAIL] TCP timeout: {host}:{port}")
        return

    except OSError as e:
        print(f"[FAIL] TCP connection failed: {e}")
        return

    # 3. TLS
    if port == 443:

        context = ssl.create_default_context()

        try:
            with socket.create_connection(
                (host, port),
                timeout=5
            ) as raw_socket:

                with context.wrap_socket(
                    raw_socket,
                    server_hostname=host
                ) as tls_socket:

                    print(
                        f"[OK] TLS: "
                        f"{tls_socket.version()}"
                    )

                    print(
                        f"[OK] Cipher: "
                        f"{tls_socket.cipher()[0]}"
                    )

        except ssl.SSLError as e:
            print(f"[FAIL] TLS: {e}")
            return

    # 4. HTTP
    try:
        context = ssl.create_default_context()

        connection = http.client.HTTPSConnection(
            host,
            port,
            timeout=5,
            context=context
        )

        connection.request("GET", path)

        response = connection.getresponse()

        print(
            f"[HTTP] "
            f"{response.status} "
            f"{response.reason}"
        )

        if 200 <= response.status < 400:
            print("[PASS] Endpoint is healthy")
        else:
            print("[FAIL] Endpoint returned error")

        connection.close()

    except Exception as e:
        print(f"[FAIL] HTTP request failed: {e}")


check_endpoint(
    "example.com",
    443,
    "/"
)
```

---

# 43. Better Production Version with Exception Handling

For DevOps automation, catch specific exceptions where possible.

```python
import socket
import ssl
import http.client


def health_check(host, port, path="/"):

    try:
        ip = socket.gethostbyname(host)
        print(f"DNS OK: {ip}")

    except socket.gaierror:
        print("DNS FAILED")
        return False

    try:
        with socket.create_connection(
            (host, port),
            timeout=5
        ):
            print("TCP OK")

    except socket.timeout:
        print("TCP TIMEOUT")
        return False

    except OSError as e:
        print(f"TCP FAILED: {e}")
        return False

    context = ssl.create_default_context()

    try:
        connection = http.client.HTTPSConnection(
            host,
            port,
            timeout=5,
            context=context
        )

        connection.request("GET", path)

        response = connection.getresponse()

        print(
            f"HTTP: "
            f"{response.status} "
            f"{response.reason}"
        )

        connection.close()

        return 200 <= response.status < 400

    except ssl.SSLError as e:
        print(f"TLS FAILED: {e}")
        return False

    except OSError as e:
        print(f"HTTP CONNECTION FAILED: {e}")
        return False


if health_check("example.com", 443):
    print("FINAL RESULT: PASS")
else:
    print("FINAL RESULT: FAIL")
```

---

# 44. Important Functions/Classes Cheat Sheet

## `socket`

| Function/Class | Purpose |
|---|---|
| `socket.socket()` | Create socket |
| `socket.create_connection()` | Create TCP connection |
| `socket.gethostname()` | Get local hostname |
| `socket.getfqdn()` | Get FQDN |
| `socket.gethostbyname()` | Resolve hostname to IPv4 |
| `socket.gethostbyname_ex()` | Detailed hostname resolution |
| `socket.getaddrinfo()` | Resolve address/service information |
| `socket.settimeout()` | Configure timeout |
| `socket.send()` | Send bytes |
| `socket.recv()` | Receive bytes |
| `socket.close()` | Close socket |

## `ssl`

| Function/Class | Purpose |
|---|---|
| `ssl.create_default_context()` | Create secure TLS context |
| `ssl.SSLContext()` | Create/configure TLS context |
| `SSLContext.wrap_socket()` | Add TLS to a socket |
| `ssl.get_server_certificate()` | Retrieve server certificate |
| `SSLSocket.version()` | Get negotiated TLS version |
| `SSLSocket.cipher()` | Get negotiated cipher |
| `SSLSocket.getpeercert()` | Get peer certificate |
| `ssl.TLSVersion` | Specify TLS versions |
| `ssl.SSLCertVerificationError` | Certificate validation error |
| `ssl.SSLError` | TLS/SSL error |

## `http.client`

| Function/Class | Purpose |
|---|---|
| `HTTPConnection` | HTTP connection |
| `HTTPSConnection` | HTTPS connection |
| `request()` | Send HTTP request |
| `getresponse()` | Receive HTTP response |
| `HTTPResponse.status` | HTTP status code |
| `HTTPResponse.reason` | HTTP status reason |
| `HTTPResponse.read()` | Read response body |
| `HTTPResponse.getheaders()` | Get all headers |
| `HTTPResponse.getheader()` | Get specific header |

---

# 45. When Should a DevOps Engineer Use Each Module?

## Use `socket` when:

You need to answer:

```text
Can I resolve this hostname?
Can I reach this IP?
Is TCP port 6443 open?
Is port 389 reachable?
Is the service accepting TCP connections?
```

Example:

```python
socket.create_connection(("api.ocp.lan", 6443), timeout=5)
```

---

## Use `ssl` when:

You need to answer:

```text
Is TLS working?
Which TLS version was negotiated?
What certificate is being presented?
When does the certificate expire?
Does the certificate validate?
Which cipher is being used?
```

Example:

```python
context.wrap_socket(
    raw_socket,
    server_hostname="api.ocp.lan"
)
```

---

## Use `http.client` when:

You need to answer:

```text
Is the web application responding?
What HTTP status is returned?
What does the API return?
Is /health returning 200?
Does the API require authentication?
```

Example:

```python
connection.request("GET", "/health")
```

---

# 46. Real DevOps Troubleshooting Scenario

Suppose users report:

```text
OpenShift API is not accessible.
```

Do not immediately assume that Kubernetes is broken.

Use a layered troubleshooting approach.

## Step 1: DNS

```python
import socket

print(socket.gethostbyname("api.ocp.lan"))
```

If this fails:

```text
DNS problem
```

---

## Step 2: TCP

```python
import socket

with socket.create_connection(
    ("api.ocp.lan", 6443),
    timeout=5
):
    print("TCP connection successful")
```

If this fails:

```text
Firewall/network/load balancer/listener problem
```

---

## Step 3: TLS

```python
import socket
import ssl

context = ssl.create_default_context()

with socket.create_connection(
    ("api.ocp.lan", 6443),
    timeout=5
) as raw:

    with context.wrap_socket(
        raw,
        server_hostname="api.ocp.lan"
    ) as tls:

        print(tls.version())
        print(tls.cipher())
```

If this fails:

```text
TLS/certificate/CA/SNI problem
```

---

## Step 4: HTTP

```python
import http.client
import ssl

context = ssl.create_default_context()

connection = http.client.HTTPSConnection(
    "api.ocp.lan",
    6443,
    timeout=5,
    context=context
)

connection.request("GET", "/version")

response = connection.getresponse()

print(response.status)
print(response.reason)

connection.close()
```

If you get:

```text
200
```

or another valid API response, then:

```text
DNS       -> OK
TCP       -> OK
TLS       -> OK
HTTP/API  -> Responding
```

This greatly narrows the troubleshooting scope.

---

# 47. `socket` vs `ssl` vs `http.client`

Think of the modules as different layers.

```text
Application
    |
    | HTTP
    v
http.client
    |
    | HTTPS/TLS
    v
ssl
    |
    | TCP
    v
socket
    |
    | IP
    v
Network
```

### Simple memory trick

```text
socket   = Can I connect?
ssl      = Can I establish secure TLS?
http     = Does the application respond?
```

---

# 48. Important DevOps Best Practices

## 1. Always use timeouts

Bad:

```python
socket.create_connection(("server", 443))
```

Better:

```python
socket.create_connection(
    ("server", 443),
    timeout=5
)
```

---

## 2. Do not disable TLS verification in production

Avoid:

```python
context = ssl._create_unverified_context()
```

unless you have a specific controlled lab/testing reason.

Prefer:

```python
context = ssl.create_default_context()
```

---

## 3. Use FQDNs for TLS

Prefer:

```python
server_hostname="api.ocp.lan"
```

rather than only using an IP address.

TLS certificates commonly contain DNS names in their SAN entries.

---

## 4. Close connections

Use:

```python
with socket.create_connection(...) as sock:
    ...
```

or explicitly:

```python
connection.close()
```

---

## 5. Catch useful exceptions

Examples:

```python
socket.gaierror
socket.timeout
OSError
ssl.SSLError
ssl.SSLCertVerificationError
```

This makes troubleshooting output much more useful.

---

# 49. Mini Project: Infrastructure Endpoint Monitor

Create:

```text
endpoint_monitor.py
```

Example:

```python
import socket
import ssl
import http.client


ENDPOINTS = [
    {
        "name": "OpenShift API",
        "host": "api.ocp.lan",
        "port": 6443,
        "path": "/version",
    },
    {
        "name": "LDAP LDAPS",
        "host": "ldap.lab.ocp.lan",
        "port": 636,
        "path": None,
    },
]


def check_tcp(host, port):
    try:
        with socket.create_connection(
            (host, port),
            timeout=5
        ):
            return True
    except OSError:
        return False


def check_tls(host, port):
    context = ssl.create_default_context()

    try:
        with socket.create_connection(
            (host, port),
            timeout=5
        ) as raw:

            with context.wrap_socket(
                raw,
                server_hostname=host
            ) as tls:

                print(
                    f"TLS={tls.version()} "
                    f"Cipher={tls.cipher()[0]}"
                )

                return True

    except ssl.SSLError as e:
        print(f"TLS error: {e}")
        return False


def check_http(host, port, path):

    context = ssl.create_default_context()

    try:
        connection = http.client.HTTPSConnection(
            host,
            port,
            timeout=5,
            context=context
        )

        connection.request("GET", path)

        response = connection.getresponse()

        status = response.status

        connection.close()

        return status

    except Exception as e:
        print(f"HTTP error: {e}")
        return None


for endpoint in ENDPOINTS:

    print("\n" + "=" * 50)
    print(endpoint["name"])
    print("=" * 50)

    host = endpoint["host"]
    port = endpoint["port"]

    try:
        ip = socket.gethostbyname(host)
        print(f"DNS: PASS ({ip})")
    except socket.gaierror:
        print("DNS: FAIL")
        continue

    if check_tcp(host, port):
        print(f"TCP {port}: PASS")
    else:
        print(f"TCP {port}: FAIL")
        continue

    if check_tls(host, port):
        print("TLS: PASS")
    else:
        print("TLS: FAIL")
        continue

    if endpoint["path"]:
        status = check_http(
            host,
            port,
            endpoint["path"]
        )

        print(f"HTTP status: {status}")
```

This is a good foundation for a real infrastructure-monitoring project.

---

# 50. Summary

For a DevOps engineer, remember these three modules as follows:

```text
socket
   |
   +-- DNS
   +-- TCP
   +-- UDP
   +-- Port checks
   +-- Network connectivity

ssl
   |
   +-- TLS
   +-- Certificates
   +-- TLS versions
   +-- Ciphers
   +-- Secure sockets

http.client
   |
   +-- HTTP
   +-- HTTPS
   +-- REST APIs
   +-- Health checks
   +-- HTTP status codes
```

The most important practical functions/classes to learn first are:

```python
# socket
socket.gethostbyname()
socket.getaddrinfo()
socket.create_connection()
socket.socket()

# ssl
ssl.create_default_context()
ssl.SSLContext
SSLContext.wrap_socket()
ssl.get_server_certificate()
SSLSocket.version()
SSLSocket.cipher()
SSLSocket.getpeercert()

# http.client
HTTPConnection
HTTPSConnection
request()
getresponse()
response.status
response.reason
response.read()
response.getheaders()
response.getheader()
```

For DevOps interviews, a strong way to explain the relationship is:

> **`socket` is used for low-level network connectivity, `ssl` adds TLS security and certificate handling, and `http.client` works at the HTTP/HTTPS application layer.**
