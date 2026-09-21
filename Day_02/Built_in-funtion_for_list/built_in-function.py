# Built-in functions for lists
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(my_list))  # output: 8
print(max(my_list))  # output: 9
print(min(my_list))  # output: 1

# sorted()
# Returns a new sorted list from the elements of any iterable.
sorted_list = sorted(my_list)
print(sorted_list)  # output: [1, 1, 2, 3, 4, 5, 6, 9]

# list()
# Returns a new list containing all items from the iterable.
new_list = list(my_list)
print(new_list)  # output: [3, 1, 4, 1, 5, 9, 2, 6]

# append()
# Adds an item to the end of the list.
my_list.append(7)
print(my_list)  # output: [3, 1, 4, 1, 5, 9, 2, 6, 7]

# extend()
# Extends the list by appending elements from another iterable.
my_list.extend([8, 10])
print(my_list)  # output: [3, 1, 4, 1, 5, 9, 2, 6, 7, 8, 10]

# Difference:
# append() adds a single element to the end of the list.
# extend() adds multiple elements to the end of the list.

# insert()
# Inserts an item at a given position.
my_list.insert(2, 99)  # Insert 99 at index 2
print(my_list)  # output: [3, 1, 99, 4, 1, 5, 9, 2, 6, 7, 8, 10]

# remove()
# Removes the first occurrence of a value.
my_list.remove(1)  # Removes the first occurrence of 1
print(my_list)  # output: [3, 99, 4, 1, 5, 9, 2, 6, 7, 8, 10]

# pop()
# Removes and returns the item at the given position (default is the last item).
last_item = my_list.pop()  # Removes the last item
print(last_item)  # output: 10
print(my_list)  # output: [3, 99, 4, 1, 5, 9, 2, 6, 7, 8]

# clear()
# Removes all items from the list.
my_list.clear()
print(my_list)  # output: []

# index()
# Returns the index of the first occurrence of a value.
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
index = my_list.index(1)  # Returns the index of the first occurrence of 1
print(index)  # output: 1

# count()
# Returns the number of occurrences of a value.
count = my_list.count(1)  # Counts how many times 1 appears in the list
print(count)  # output: 2

# reverse()
# Reverses the elements of the list in place.
my_list.reverse()
print(my_list)  # output: [6, 2, 9, 5, 1, 4, 1, 3]

# sort()
# Sorts the list in place.
my_list.sort()
print(my_list)  # output: [1, 1, 2, 3, 4, 5, 6, 9]

# copy()
# Returns a shallow copy of the list.
new_list = my_list.copy()
print(new_list)  # output: [1, 1, 2, 3, 4, 5, 6, 9]

# Note: The above functions are built-in methods for lists in Python. 
# They provide various functionalities to manipulate and access list elements efficiently.

# Combine list methods + string methods
servers = [" web01 ", " web02 ", " db01 "]

clean_servers = []

for server in servers:
    clean_servers.append(server.strip().upper())

print(clean_servers)
# output: ['WEB01', 'WEB02', 'DB01']

# split() creates a list of strings
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # output: ['apple', 'banana', 'cherry']
# output: ['apple', 'banana', 'cherry']

# join() creates a string from a list of strings
result = " ".join(fruits)
print(result)  # output: apple banana cherry
# output: apple banana cherry

