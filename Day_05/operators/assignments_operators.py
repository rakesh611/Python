# Assignment operators assign or update values.

# = Assignment
server_count = 5

print(server_count)
# Output: 5

###################

# +=
# Adds a value and assigns the result back.
successful_servers = 0

successful_servers += 1
successful_servers += 1
successful_servers += 1

print(successful_servers)
# Output: 3

########################
# -=
# Subtracts and assigns.
disk = 100

disk -= 20

print(disk)
# Output: 80

###########################
# *=
# Multiplies and assigns.
replicas = 2

replicas *= 3

print(replicas)
# Output: 6

###################

# /=
# Divides and assigns.
memory = 32

memory /= 2

print(memory)
# Output: 16.0


#################

# //=
# Floor divides and assigns.
pods = 100

pods //= 6

print(pods)
# Output: 16

#######################

# %=
# Modulus and assignment.
number = 10

number %= 3

print(number)
# Output: 1

#######################
# **=
# Exponentiation and assignment.
number = 2

number **= 3

print(number)
# Output: 8