# ============================================================
# Program 8: Dictionary Operations and Methods
# Description: Create a dictionary and demonstrate printing
#              items, accessing items, get(), changing values,
#              and len().
# ============================================================

# Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA",
    "marks": 85
}

# a) Print the dictionary items
print("Dictionary Items:")
print(student)

# b) Access items
print("\nAccessing Items:")
print("Name  :", student["name"])
print("Course:", student["course"])

# c) Use get()
print("\nUsing get():")
print("Age:", student.get("age"))

# d) Change values
student["marks"] = 90
print("\nAfter changing marks:")
print(student)

# e) Use len()
print("\nNumber of items in dictionary:", len(student))

# ------------------------------------------------------------
# Expected Output:
#
# Dictionary Items:
# {'name': 'Rahul', 'age': 20, 'course': 'BCA', 'marks': 85}
#
# Accessing Items:
# Name  : Rahul
# Course: BCA
#
# Using get():
# Age: 20
#
# After changing marks:
# {'name': 'Rahul', 'age': 20, 'course': 'BCA', 'marks': 90}
#
# Number of items in dictionary: 4
# ------------------------------------------------------------
