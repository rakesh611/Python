#  Function for Linux Service Check
import subprocess

def check_service(service):
    result = subprocess.run(
        ["systemctl", "is-active", service],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()


status_sshd = check_service("sshd")
status_docker = check_service("docker")
status_nginx = check_service("nginx")

print("SSH Service:", status_sshd)
print("Docker Service:", status_docker)
print("Nginx Service:", status_nginx)