import shutil

def check_disk_usage(path="C:\\"):
    total, used, free = shutil.disk_usage(path)
    used_percent = (used / total) * 100
    return round(used_percent, 2)

print("Disk Usage:", check_disk_usage(), "%")
