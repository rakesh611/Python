print("Hello World")
# Hella world is string
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello World"
print(a)
# Multiline Strings
# We can assign a multiline string to a variable by using three quotes:
a = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Get the character at position 1 (remember that the first character has the position 0):
# Also get the character from reverse we can use -1 if get last position
a = "Hello World"
print(a[1])
print(a[-1])
# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
    print(x)
# String Length
# To get the length of a string, use the len() function.
a = "Hello World"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
#example
# Check if "free" and "look" is present in the following text:
txt = "the best thing is my life is i am free from debt"
print("free" in txt)
print("look" in txt)
# Check if NOT
txt = "the best thing is my life is i am free from debt"
if "loan" not in txt:
    print("No, 'loan' is NOT present." )

# Slicing Strings
# You can return a range of characters by using the slice syntax.
# example:- Get the characters from position 2 to position 5 (not included):
a = "hello world"
print(a[2:5])

# Slice From the Start
# Example:- Get the characters from the start to position 5 (not included):
a = "hello world"
print(a[:5])

# Slice To the End
# example:- Get the characters from position 2, and all the way to the end:
a = "hello world"
print(a[2:])

# Modify Strings
# Upper Case
# example:- The upper() method returns the string in upper case:
a = "hello world"
print(a.upper())
# Lower Case
# example:- The lower() method returns the string in Lower case:
a = "HELLO WORLD"
print(a.lower())

# Remove Whitespace
# Example :- The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World   "
print(a.strip())

# Replace String
# example:- The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String:- The split() method returns a list where the text between the specified separator becomes the list items.
# example:- The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Format:- As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# Example:-
age = 36
#This will produce an error:
txt = "My name is John, I am " + str(age)
print(txt)
# But we can combine strings and numbers by using f-strings or the format() method!
# F-Strings:- F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
#
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
#example:-Create an f-string:
age = 36
txt = f"My name is john, I am {age}"
print(txt)
