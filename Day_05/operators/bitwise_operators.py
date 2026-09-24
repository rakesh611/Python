# Bitwise operators work at the binary/bit level.
# Operators:
# &     AND
# |     OR
# ^     XOR
# ~     NOT
# <<    Left shift
# >>    Right shift

################################

# Bitwise &
# Performs binary AND.
a = 5
b = 3

print(a & b)
# Binary:
# 5 = 101
# 3 = 011

#     101
# AND 011
# ---------
#     001
# Output: 1

#####################

# Bitwise |
# Binary OR.
a = 5
b = 3

print(a | b)
# 101
# 011
# ---
# 111
# Output: 7

##################################
# Bitwise ^
# XOR.
a = 5
b = 3

print(a ^ b)

# 101
# 011
# ---
# 110
# Output: 6
# XOR returns 1 when the bits are different.

####################################

# Bitwise ~
# Bitwise NOT.
a = 5

print(~a)