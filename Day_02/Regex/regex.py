# Regex in Python
# Regex means Regular Expression.
# It is a pattern used to search, match, extract, validate, replace, or split text.
# In Python, regex functionality is provided mainly by the built-in re module.
# import re

# Example
log = "ERROR: Server web01 is down"
# Find the word ERROR:
import re
result = re.search("ERROR", log)
print(result)
# output: <re.Match object; span=(0, 5), match='ERROR'>

# 1. Important Regex Functions in Python
# re.search()
# Searches for a pattern anywhere in the string.
import re
text = "Linux OpenShift Kubernetes"
result = re.search("OpenShift", text)
print(result)
# output: <re.Match object; span=(6, 15), match='OpenShift'>

# A better way to check:
if re.search("OpenShift", text):
    print("OpenShift found")

# output: OpenShift found

# re.match()
# Checks for a match only at the beginning of the string.
import re
text = "Linux OpenShift Kubernetes"
result = re.match("Linux", text)
print(result)
# output: <re.Match object; span=(0, 5), match='Linux'

# A better way to check:
if re.match("Linux", text):
    print("Linux found")
else:
    print("Linux not found")

# output: Linux found

# re.fullmatch()
# Checks for a match only if the entire string matches the pattern.
import re
text = "Linux OpenShift Kubernetes"
if re.fullmatch("Linux OpenShift Kubernetes", text):
    print("Full match found")
else:
    print("Full match not found")

# output: Full match found

# re.findall()
# Returns a list of all occurrences of the pattern in the string.
# It returns all matching values as a list.
import re

text = "web01 web02 db01 app01"
servers = re.findall(r"\w+", text)

print(servers)
# output ['web01', 'web02', 'db01', 'app01']

# Find IP addresses
import re

text = """
server1 192.168.22.11
server2 192.168.22.12
server3 192.168.22.13
"""

ips = re.findall(r"\d+\.\d+\.\d+\.\d+", text)

print(ips)
# output : ['192.168.22.11', '192.168.22.12', '192.168.22.13']

# re.finditer()
# Similar to findall(), but returns match objects.
import re

text = "web01 web02 db01"

for match in re.finditer(r"\w+", text):
    print(match.group())

# output : 
# web01
# web02
# db01

# You can also get positions:
for match in re.finditer(r"\w+", text):
    print(match.group(), match.start(), match.end())

# output:
# web01 0 5
# web02 6 11
# db01 12 16

# re.sub()
# Used to replace matching text.
import re

text = "Linux Linux Linux"

result = re.sub("Linux", "OpenShift", text)

print(result)
# Output: OpenShift OpenShift OpenShift

# re.split()
# Splits a string using a regex pattern.
# For example, split using comma or semicolon:
import re

text = "Linux,OpenShift;Kubernetes,Docker"

result = re.split(r"[,;]", text)

print(result)
# output: ['Linux', 'OpenShift', 'Kubernetes', 'Docker']

# This is more powerful than normal:
# text.split(",")
# because regex can handle multiple separators.

# re.compile()
# Used when you want to reuse the same regex pattern multiple times.
import re

pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")

text1 = "Server IP: 192.168.22.11"
text2 = "Server IP: 192.168.22.12"

print(pattern.findall(text1))
print(pattern.findall(text2))
# output:
# ['192.168.22.11']
# ['192.168.22.12']

# re.escape()
# Escapes characters that have special meaning in regex.
import re

text = "server.example.com"

pattern = re.escape(text)

print(pattern)
# output: server\.example\.com
# This is useful when you want to search for literal text rather than interpret regex characters.


# Important Regex Patterns
# Now the most important part: regex syntax.
# \d — Digit
# Matches numbers 0-9.
import re

text = "Server123"

print(re.findall(r"\d", text))
# output: ['1', '2', '3']

# \D — Not a digit
re.findall(r"\D", "abc123")
# output: ['a', 'b', 'c']

# \w — Word character
# Generally matches:
re.findall(r"\w+", "web01 db01 app01")
# output: ['web01', 'db01', 'app01']

# \s — Whitespace
# Matches spaces, tabs, newlines, etc.
re.findall(r"\s", "Linux Python")

# +
# Means one or more.
# r"\d+"
text = "CPU 75% MEM 80%"

print(re.findall(r"\d+", text))
# output : ['75', '80']

# *
# Means zero or more.
# a*
# can match:
# "a"
# "aa"
# "aaa"
# ?
# Means zero or one.
# colou?r
# matches both:
# color
# colour
# {n}
# Exactly n occurrences.
# r"\d{4}"
# matches:
# 2026
# 1234
# 9999

# Example:
text = "Year 2026"

print(re.findall(r"\d{4}", text))
# output: ['2026']

# {n,m}
# Between n and m occurrences.
# r"\d{2,4}"
# Can match:
# 12
# 123
# 1234

# .
# Dot means any character except newline by default.
# r"web."
# Can match:
# web1
# web2
# webA
# web-

# ^
# Means beginning of string.
# r"^ERROR"
# Matches:
# ERROR: server failed
# but not:
# INFO: ERROR server failed


# $
# Means end of string.
# r"failed$"
# Matches:
# Server failed


# []
# Character set.
# r"[aeiou]"
# Matches vowels.
# Example:
text = "Linux"

print(re.findall(r"[aeiou]", text))
# output: ['i', 'u']

# |
# Means OR.
# r"ERROR|WARNING"
# example:
text = "WARNING: disk usage high"

if re.search(r"ERROR|WARNING", text):
    print("Important log found")
# output: Important log found


# Groups ()
# Groups part of a pattern.
# Example:
text = "CPU: 75%"

result = re.search(r"CPU:\s*(\d+)%", text)

print(result.group(1))
# Output:75
# This is very useful when extracting specific information from logs.
