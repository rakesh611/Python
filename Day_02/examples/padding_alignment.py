# center()
print("Python".center(20, "-"))
# output: -------Python-------

# ljust() and rjust()
print("Python".ljust(20, "-"))
# output: Python--------------

print("Python".rjust(20, "-"))
# output: --------------Python

# zfill()
# Useful for numbers:
print("42".zfill(5))
# output: 00042
print("-42".zfill(5))
# output: -0042