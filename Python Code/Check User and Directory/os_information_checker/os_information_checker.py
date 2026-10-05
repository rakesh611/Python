import platform
import socket
import os
import subprocess

def get_uptime():
    """Get system uptime"""
    try:
        with open("/proc/uptime", "r") as file:
            uptime__seconds = float(file.readline().split()[0])

        days = int(uptime__seconds // 86400)
        hours = int((uptime__seconds % 86400) // 3600)
        minutes = int((uptime__seconds % 3600) // 60)

        return f"{days} days, {hours} hours, {minutes} minutes"
    except FileNotFoundError:
        return "Not Available"

def get_os_release():
    """Read linux os information from /etc/os-release."""
    os_info ={}

    try:
        with open("/etc/os-release", "r") as file:
            for line in file:
                line = line.strip()

                if "=" in line:
                    key, value = line.split("=", 1)
                    os_info[key] = value.strip('"')

    except FileNotFoundError:
        pass
    return os_info

def get_ip_address():
    """Get IP address..."""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception:
        return "Not Available"

def main():

    print("=" * 60)
    print("             OS INFORMATION CHECKER")
    print("=" * 60)

    # Operating System
    print(f"Operating System : {platform.system()}")

    # Distribution
    os_info = get_os_release()

    print(f"Distribution     : {os_info.get('PRETTY_NAME', 'Not Available')}")

    # Kernel
    print(f"Kernel Version   : {platform.release()}")

    # Architecture
    print(f"Architecture     : {platform.machine()}")

    # Hostname
    print(f"Hostname         : {socket.gethostname()}")

    # IP Address
    print(f"IP Address       : {get_ip_address()}")

    # CPU
    print(f"CPU Count        : {os.cpu_count()}")

    # Uptime
    print(f"System Uptime    : {get_uptime()}")

    print("=" * 60)

main()