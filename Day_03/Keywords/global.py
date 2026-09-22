# global
# Used to modify a global variable from inside a function.
count = 0

def increase_count():
    global count
    count += 1

increase_count()

print(count)

# Output: 1
# Generally, avoid excessive use of global because it can make automation scripts harder to maintain.