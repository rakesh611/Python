# nonlocal
# Used inside nested functions to modify a variable from the enclosing function.
def outer():

    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()

    print(count)

outer()
# Output: 1
# This is less common in typical DevOps scripts.