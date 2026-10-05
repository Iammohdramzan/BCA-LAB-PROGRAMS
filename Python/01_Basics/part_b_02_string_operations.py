# ============================================================
# Part-B Program 2: String Operations
# Description: Demonstrate common string operations using
#              lower(), upper(), find(), replace(), count(),
#              and len().
# ============================================================

# Read a string from the user
text = input("Enter a string: ")

# a) lower() - Convert the string to lowercase
print("\nLowercase:", text.lower())

# b) upper() - Convert the string to uppercase
print("Uppercase:", text.upper())

# c) find() - Find the position of a substring
search_text = input("\nEnter a word to find: ")
print("Position of", search_text, ":", text.find(search_text))

# d) replace() - Replace a substring
old_text = input("\nEnter the word to replace: ")
new_text = input("Enter the new word: ")
print("After replacement:", text.replace(old_text, new_text))

# e) count() - Count occurrences of a substring
count_text = input("\nEnter a word to count: ")
print("Number of occurrences:", text.count(count_text))

# f) len() - Find the length of the string
print("\nLength of the string:", len(text))

# ------------------------------------------------------------
# Expected Output:
#
# Enter a string: Hello Python World
#
# Lowercase: hello python world
# Uppercase: HELLO PYTHON WORLD
#
# Enter a word to find: Python
# Position of Python : 6
#
# Enter the word to replace: Python
# Enter the new word: Programming
# After replacement: Hello Programming World
#
# Enter a word to count: o
# Number of occurrences: 2
#
# Length of the string: 18
# ------------------------------------------------------------
