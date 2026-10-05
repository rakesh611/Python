import os
import subprocess
import sys

def ensure_root():
    if os.getuid() == 0:
        print("OK: Running as Root")

    else:
        print("ERROR: Script is not running as root")
        print("INFO: Re-running script with sudo...")

        subprocess.run(
            ["sudo", sys.executable, os.path.abspath(__file__)],
            check=True
        )
        sys.exit(0)

def ensure_root_directory():
    current_dir = os.getcwd()
    if current_dir == "/":
        print("OK: Current directory is /")
        return
    print(f"Current directory is {current_dir}")
    print("Changing directory to /")

    os.chdir("/")
    print(f"OK: Current directory is now {os.getcwd()}")

def main():
    print("Starting environment validation....")
    ensure_root()
    ensure_root_directory()
    print("Environment validation completed....")

main()