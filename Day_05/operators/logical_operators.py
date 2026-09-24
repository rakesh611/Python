# Logical operators combine conditions.
# There are three: and, or, not

# and
# Both conditions must be True.
node_ready = True
disk_usage = 95

if node_ready and disk_usage > 90:
    print("Node is Ready but disk usage is critical")

# Output: Node is Ready but disk usage is critical

#############################

# or
# At least one condition must be True.
cpu = 90
disk = 70

if cpu > 90 or disk > 90:
    print("Alert")
else:
    print("Normal")

# Output: Normal

################################

# not
# Reverses a Boolean value.
pod_ready = False

if not pod_ready:
    print("Pod is not ready")
# Output: Pod is not ready
