# ============================================================
# Program 6: Operations on Lists
# Description: Demonstrate creating, accessing, updating,
#              and deleting elements in a Python list.
# ============================================================

# a) Create a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:", fruits)

# b) Access list
print("\nAccessing the list:")
print("First item :", fruits[0])
print("Second item:", fruits[1])

# c) Update list - Add an item
fruits.append("Grapes")
print("\nAfter adding an item:", fruits)

# Update list - Remove an item
fruits.remove("Banana")
print("After removing an item:", fruits)

# d) Delete list
del fruits

print("\nList deleted successfully.")

# ------------------------------------------------------------
# Expected Output:
#
# Original List: ['Apple', 'Banana', 'Mango', 'Orange']
#
# Accessing the list:
# First item : Apple
# Second item: Banana
#
# After adding an item: ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes']
# After removing an item: ['Apple', 'Mango', 'Orange', 'Grapes']
#
# List deleted successfully.
# ------------------------------------------------------------
