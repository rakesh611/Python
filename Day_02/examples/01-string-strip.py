# strip()
# Removes spaces from both sides:
# Example:
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)
################################
# lstrip()
# Removes from left:
# Example:
text = "   Some spaces around   "
left_stripped_text = text.lstrip()
print("Left stripped text:", left_stripped_text)
# Output = Left stripped text: Some spaces around
################################
# rstrip()
# Removes from right:
# Example:
text = "   Some spaces around   "
right_stripped_text = text.rstrip()
print("Right stripped text:", right_stripped_text)
# output = Right stripped text:    Some spaces around
##############################
# We can also remove specific characters:
text = "###Some spaces around###"
stripped_text = text.strip("#")
print("Stripped text:", stripped_text)