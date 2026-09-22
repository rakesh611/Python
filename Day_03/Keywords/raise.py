# raise
# Manually generates an exception.
disk_usage = 95

if disk_usage > 90:
    raise Exception("Disk usage is critical")
