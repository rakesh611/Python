# return
# Returns a value from a function.
def check_service(status):
    if status == "active":
        return True
    else:
        return False

result = check_service("active")

print(result)
# Output: True