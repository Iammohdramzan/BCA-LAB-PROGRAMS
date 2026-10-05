# ============================================================
# Program 7: Demonstrate List Methods
# Description: Create a list and demonstrate the use of
#              insert(), remove(), append(), len(), pop(),
#              and clear() methods.
# ============================================================

# Create a list
numbers = [10, 20, 30, 40]

print("Original List:", numbers)

# a) insert() - Add an item at a specific position
numbers.insert(2, 25)
print("\nAfter insert(2, 25):", numbers)

# b) remove() - Remove a specific item
numbers.remove(25)
print("After remove(25):", numbers)

# c) append() - Add an item at the end
numbers.append(50)
print("After append(50):", numbers)

# d) len() - Find the number of items
print("Length of the list:", len(numbers))

# e) pop() - Remove the last item
removed_item = numbers.pop()
print("Removed item using pop():", removed_item)
print("List after pop():", numbers)

# f) clear() - Remove all items from the list
numbers.clear()
print("List after clear():", numbers)

# ------------------------------------------------------------
# Expected Output:
#
# Original List: [10, 20, 30, 40]
#
# After insert(2, 25): [10, 20, 25, 30, 40]
# After remove(25): [10, 20, 30, 40]
# After append(50): [10, 20, 30, 40, 50]
# Length of the list: 5
# Removed item using pop(): 50
# List after pop(): [10, 20, 30, 40]
# List after clear(): []
# ------------------------------------------------------------
