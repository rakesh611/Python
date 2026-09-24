# Comparison operators compare two values.
# They return:True or False
# Important comparision operators.
# ==    Equal
# !=    Not equal
# >     Greater than
# <     Less than
# >=    Greater than or equal
# <=    Less than or equal

######################

# == Equal To
# Checks whether two values are equal.
status = "Running"

if status == "Running":
    print("Pod is running")

# Output: Pod is running

####################

# != Not Equal
# Checks whether two values are different.
status = "Failed"

if status != "Running":
    print("Pod is not running")

# Output: Pod is not running
# This is very useful in troubleshooting scripts.

##########################

# > Greater Than
disk_usage = 92

if disk_usage > 90:
    print("WARNING: Disk usage is high")
# Output: WARNING: Disk usage is high

#######################

# < Less Than
memory = 20

if memory < 30:
    print("Low memory")
# Output: Low memory

#################

# >= Greater Than or Equal
cpu = 80

if cpu >= 80:
    print("High CPU usage")
# Output: High CPU usage

#########################

# <= Less Than or Equal
disk_usage = 80

if disk_usage <= 80:
    print("Disk usage is acceptable")

# Output: Disk usage is acceptable