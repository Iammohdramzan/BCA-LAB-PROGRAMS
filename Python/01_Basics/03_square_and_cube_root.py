# ============================================================
# Program 3: Find Square Root and Cube Root
# Description: Calculate the square root and cube root of
#              a given number.
# ============================================================

import math

# Read a number from the user
num = float(input("Enter a number: "))

# Calculate square root and cube root
square_root = math.sqrt(num)
cube_root = num ** (1 / 3)

# Display the results
print("\n--- Results ---")
print("Square Root :", square_root)
print("Cube Root   :", cube_root)

# ------------------------------------------------------------
# Expected Output:
#
# Enter a number: 64
#
# --- Results ---
# Square Root : 8.0
# Cube Root   : 3.9999999999999996
# ------------------------------------------------------------
