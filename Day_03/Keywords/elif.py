# elif
# Means else if.
cpu = 75

if cpu > 90:
    print("Critical")
elif cpu > 70:
    print("Warning")

# Output: Warning

# 2nd Example
status = 503

if status == 200:
    print("Application is healthy")
elif status >= 500:
    print("Application server error")
elif status >= 400:
    print("Client error")
# output: Application server error