# with
# Used with context managers.
# Extremely useful for file handling.
# Instead of:
# file = open("/tmp/test.txt")
# data = file.read()
# file.close()
# use:
with open("/tmp/test.txt") as file:
    data = file.read()

# Python automatically handles closing the file.