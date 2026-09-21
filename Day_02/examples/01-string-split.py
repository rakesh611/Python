text = "Python is awesome"
words = text.split()
print("Words:", words)

# 2nd example
linux = "Linux is an open-source operating system"
words = linux.split()
new_words = words[3].split("-")
print("new_words:", new_words)
length = len(words[0])
print("Length of the words:", length)
uppercase = words[0].upper()
print("Uppercase of the words:", uppercase)
