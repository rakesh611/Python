import sys
import subprocess


if len(sys.argv) != 2:
    print("Usage: python3 server_validate.py <service>")
    sys.exit(1)


service = sys.argv[1]

print(f"Checking service: {service}")


result = subprocess.run(
    ["systemctl", "is-active", service],
    capture_output=True,
    text=True
)


if result.returncode == 0:

    print(f"SUCCESS: {service} is running")

    sys.exit(0)

else:

    sys.stderr.write(
        f"ERROR: {service} is not running\n"
    )

    sys.exit(1)

# Run:
# python3 server_validate.py sshd
# Possible Output:
# Checking service: sshd
# SUCCESS: sshd is running