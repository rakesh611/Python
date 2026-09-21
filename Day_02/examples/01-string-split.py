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

# 3rd example
python = "Python is a high-level programming language"
words = python.split()
new_words = words[3].split("-")
print("words:", words[0], words[1], words[2], new_words[0], new_words[1], words[4], words[5])
