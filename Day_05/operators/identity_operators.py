# Identity operators: They check whether two variables refer to the same object, not merely whether their values are equal.
# is
# is not

# is
# Example:
result = None

if result is None:
    print("Command did not return a result")

# Output: Command did not return a result

################

# is not
result = "Running"

if result is not None:
    print("Result is available")

# Output: Result is available