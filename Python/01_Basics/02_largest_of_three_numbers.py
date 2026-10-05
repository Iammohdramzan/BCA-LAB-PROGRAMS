# ============================================================
# Program 2: Find the Largest of Three Numbers
# Description: Find the largest among three numbers using
#              conditional statements.
# ============================================================

# Read three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the result
print("\n--- Result ---")
print("Largest number:", largest)

# ------------------------------------------------------------
# Expected Output:
#
# Enter the first number: 25
# Enter the second number: 47
# Enter the third number: 32
#
# --- Result ---
# Largest number: 47.0
# ------------------------------------------------------------
