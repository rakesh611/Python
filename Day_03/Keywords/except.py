# except
# Handles an exception.
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

# Output: Cannot divide by zero

try:
    with sp.open("/etc/hosts") as file:
        data = file.read()

except FileNotFoundError:
    print("File not found")