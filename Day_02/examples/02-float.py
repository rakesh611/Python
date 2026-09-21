# 1. float()
# Converts a value into a floating-point number.
x = float("3.14")
y = float(10)
print(x)  # output: 3.14
print(y)  # output: 10.0

# int()
# Converts float to integer by removing the decimal part.
z = int(3.14)
print(z)  # output: 3

# round()
# Used for rounding decimal values.
result = round(3.14159, 2)
result2 = round(3.14159, 3)
print(result)  # output: 3.14
print(result2)  # output: 3.142

# abs()
# Returns the positive/absolute value.
x = abs(-3.14)
print(x)  # output: 3.14

# min() and max()
# Returns the minimum and maximum values from a list of numbers.
numbers = [3.14, 2.71, 1.41, 4.67]
minimum = min(numbers)
maximum = max(numbers)
print(minimum)  # output: 1.41
print(maximum)  # output: 4.67

# sum()
# Calculates the sum of a list of numbers.
numbers = [1.5, 2.5, 3.5]
total = sum(numbers)
print(total)  # output: 7.5

# divmod()
# Returns the quotient and remainder of a division.
quotient, remainder = divmod(10, 3)
print(quotient)  # output: 3
print(remainder)  # output: 1

# 2. Float operators
a = 3.14
b = 2.71
c = a + b  # Addition
d = a - b  # Subtraction
e = a * b  # Multiplication
f = a / b  # Division
g = a % b  # Modulus
h = a ** b  # Exponentiation

# 3. Type checking
print(type(a))  # output: <class 'float'>

# 4. Type conversion
# Convert float to int
int_value = int(a)
print(int_value)  # output: 3

# Convert float to string
str_value = str(a)
print(str_value)  # output: '3.14'

# Convert float to complex
complex_value = complex(a)
print(complex_value)  # output: (3.14+0j)

# 5. Comparison operators
x = 3.14
y = 2.71
print(x > y)   # output: True
print(x < y)   # output: False
print(x == y)  # output: False

# 6. Built-in functions
# round()
rounded_value = round(3.14159, 2)
print(rounded_value)  # output: 3.14
