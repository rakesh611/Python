def check_disk_usage(usage):
    if usage >= 90:
        return "CRITICAL"
    elif usage >= 80:
        return "WARNING"
    else:
        return "OK"


status = check_disk_usage (70)
# Now we can reuse the function:
print(check_disk_usage(50))
print(check_disk_usage(75))
print(check_disk_usage(85))
print(check_disk_usage(95))

print("Disk Status:", status)