import shutil
import psutil

def get_disk_usage(path="C:\\"):
    total, used, free = shutil.disk_usage(path)
    return round((used / total) * 100, 2)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def system_health_check():
    disk = get_disk_usage("C:\\")
    memory = get_memory_usage()
    cpu = get_cpu_usage()

    print(f"Disk Usage: {disk}%")
    print(f"Memory Usage: {memory}%")
    print(f"CPU Usage: {cpu}%")

    if disk > 80:
        print(f"Disk Usage: {disk}%")
    elif memory > 80:
        print(f"Memory Usage: {memory}%")
    elif cpu > 80:
        print(f"CPU Usage: {cpu}%")
    else:
        print("System Health: OK")

system_health_check()
