# Python can execute Linux commands using subprocess.
import subprocess

def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout


hostname = run_command("hostname")
uptime = run_command("uptime")
file_system_space = run_command("df -h")
free_space = run_command("free -m")
                     
# Now the same function can execute different commands:
print(uptime)
print(file_system_space)
print(free_space)
print(hostname)