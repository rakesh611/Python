# int()
# Convert a string/float to integer:
x = int("10")
y = int(3.14)
print(x)  # output: 10
print(y)  # output: 3

# abs()
# Get the absolute value of a number:
x = abs(-10)
y = abs(3.14)
print(x)  # output: 10
print(y)  # output: 3.14

# pow()
# Raise a number to a power:
x = pow(2, 3)
y = pow(4, 0.5)
print(x)  # output: 8
print(y)  # output: 2.0

# round()
# Round a number to the nearest integer:
x = round(3.14)
y = round(3.75)
print(x)  # output: 3
print(y)  # output: 4

# min() and max()
x = min(5, 10, 2)
y = max(5, 10, 2)
print(x)  # output: 2
print(y)  # output: 10

# sum()
# Calculate the sum of a list of numbers:
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)  # output: 15

# divmod()
# Return the quotient and remainder of a division:
x = divmod(10, 3)
print(x)  # output: (3, 1)

# 2. Integer operators
a = 10
b = 3

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor division
print(a % b)    # Remainder
print(a ** b)   # Power

# 3. Type checking
print(type(a))  # output: <class 'int'>
print(type(b))  # output: <class 'int'>

# Or:
print(isinstance(a, int))