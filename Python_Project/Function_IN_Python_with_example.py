# A function is a reusable block of code that performs a specific task.
# '''def function_name(parameters):
#     # logic
#     return result'''

# Example:-

import shutil

def check_disk_usage(path="C:\\"):
    total, used, free, percent = shutil.disk_usage(path)
    used_percent = (used / total) * 100
    return round(used_percent, 2)

print("Disk Usage:", check_disk_usage(), "%")
