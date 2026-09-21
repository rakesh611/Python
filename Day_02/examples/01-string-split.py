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

# 3. split("-") — Split using -
python = "Python is a high-level programming language"
words = python.split()
new_words = words[3].split("-")
print("words:", words[0], words[1], words[2], new_words[0], new_words[1], words[4], words[5])

# 4. rsplit() — Split from the right side
language = "Python is a high-level programming language"
new_language = language.rsplit(" ", 1)
new_language1 = language.rsplit(" ", 2)
print("new_language:", new_language)
print("new_language1:", new_language1)