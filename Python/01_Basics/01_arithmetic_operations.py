# ============================================================
# Program 1: Arithmetic Operations
# Description: Perform basic arithmetic operations on two numbers
# ============================================================

# Read two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
remainder = num1 % num2
power = num1 ** num2

# Display the results
print("\n--- Arithmetic Operations ---")
print("Addition        :", addition)
print("Subtraction     :", subtraction)
print("Multiplication  :", multiplication)
print("Division        :", division)
print("Floor Division  :", floor_division)
print("Remainder       :", remainder)
print("Power           :", power)

# ------------------------------------------------------------
# Expected Output:
#
# Enter the first number: 10
# Enter the second number: 3
#
# --- Arithmetic Operations ---
# Addition        : 13.0
# Subtraction     : 7.0
# Multiplication  : 30.0
# Division        : 3.3333333333333335
# Floor Division  : 3.0
# Remainder       : 1.0
# Power           : 1000.0
# ------------------------------------------------------------
