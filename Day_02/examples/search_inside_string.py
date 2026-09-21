# find()
# Returns the position of the text.
text = "Hello, welcome to my tutorial"
position = text.find("welcome")
print("Position of 'welcome':", position)
# If not found:
print("Position of 'Python':", text.find("Python"))  # Output: -1

# index()
# Similar to find(), but raises an error if not found.
text = "Hello Python"
print(text.index("Python"))
# print(text.index("Java"))  # This will raise a ValueError

# count()
# Counts occurrences:
text = "hello hello python"
print(text.count("hello"))