# A conditional statement is used to make a decision in a Python program.
# "If this condition is true, do this; otherwise, do something else."

# if Statement
# The if statement executes a block of code only when the condition is True.
# Syntax
# if condition:
#     statement
# Example:
cpu_usage = 85

if cpu_usage > 80:
    print("WARNING: CPU usage is high")


##########################

# if-else Statement
# Sometimes you want to perform one action when the condition is true and another action when it is false.
# For this, use if-else.
# Syntax
# if condition:
#     statement_if_true
# else:
#     statement_if_false

# Example:
pod_status = "Running"

if pod_status == "Running":
    print("Pod is healthy")
else:
    print("Pod is not healthy")


###########################

# if-elif-else Statement
# elif means:
# else if
# It is used when you have multiple conditions.
# Syntax
# if condition1:
#     statement
# elif condition2:
#     statement
# elif condition3:
#     statement
# else:
#     statement
# Python checks the conditions from top to bottom.
# Example:
memory_usage = 92

if memory_usage >= 90:
    print("CRITICAL: Memory usage is very high")
elif memory_usage >= 80:
    print("WARNING: Memory usage is high")
elif memory_usage >= 60:
    print("INFO: Memory usage is moderate")
else:
    print("OK: Memory usage is normal")

# Output: CRITICAL: Memory usage is very high

######################

# Multiple Conditions Using and
# and means both conditions must be True.
# Example:
pod_status = "Running"
restart_count = 5

if pod_status == "Running" and restart_count > 3:
    print("Pod is running but restarting frequently")

# Output: Pod is running but restarting frequently

####################################

# Multiple Conditions Using or
# or means at least one condition must be True.
# Example:
cpu = 50
disk = 95

if cpu > 90 or disk > 90:
    print("Alert: Server resource usage is critical")

# Output: Alert: Server resource usage is critical

##################################

# not Operator
# not reverses the result of a condition.
# True  → False
# False → True
# Example:
pod_ready = False

if not pod_ready:
    print("Pod is not ready")

# Output: Pod is not ready

################################

# Nested if
# A nested if means an if statement inside another if statement.
# Example:
pod_status = "Running"
restart_count = 5

if pod_status == "Running":

    if restart_count > 3:
        print("Pod is running but unstable")
    else:
        print("Pod is healthy")
else:
    print("Pod is not running")

# Output: Pod is running but unstable

#######################################

# Nested if-else
# You can also put if-else inside another if.
# Example:
environment = "production"
deployment_status = "failed"

if environment == "production":

    if deployment_status == "success":
        print("Production deployment successful")
    else:
        print("Production deployment failed")

else:
    print("Non-production environment")

# Output: Production deployment failed