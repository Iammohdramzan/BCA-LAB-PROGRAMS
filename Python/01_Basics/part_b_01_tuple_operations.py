# ============================================================
# Part-B Program 1: Tuple Operations
# Description: Create a tuple and demonstrate adding items,
#              len(), checking items, and accessing items.
# ============================================================

# Create a tuple
fruits = ("Apple", "Banana", "Mango", "Orange")

print("Original Tuple:", fruits)

# a) Add items
# Tuples are immutable, so a new tuple is created
fruits = fruits + ("Grapes",)
print("\nAfter adding an item:", fruits)

# b) len() - Find the number of items
print("\nNumber of items:", len(fruits))

# c) Check for an item in the tuple
item = "Mango"

if item in fruits:
    print("\n", item, "is present in the tuple.")
else:
    print("\n", item, "is not present in the tuple.")

# d) Access items
print("\nAccessing items:")
print("First item :", fruits[0])
print("Second item:", fruits[1])
print("Last item  :", fruits[-1])

# ------------------------------------------------------------
# Expected Output:
#
# Original Tuple: ('Apple', 'Banana', 'Mango', 'Orange')
#
# After adding an item: ('Apple', 'Banana', 'Mango', 'Orange', 'Grapes')
#
# Number of items: 5
#
# Mango is present in the tuple.
#
# Accessing items:
# First item : Apple
# Second item: Banana
# Last item  : Grapes
# ------------------------------------------------------------
