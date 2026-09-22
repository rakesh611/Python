# or
# Requires at least one condition to be true.
cpu = 95
memory = 50

if cpu > 90 or memory > 90:
    print("High resource usage")
else:
    print("Normal resource usage")
# output: High resource usage