# ============================================================
# Part-B Program 6: try, except and finally
# Description: Demonstrate the use of try, except, and
#              finally blocks for exception handling.
# ============================================================

try:
    # Read two numbers from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform division
    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    # Handle division by zero error
    print("Error: Cannot divide by zero.")

except ValueError:
    # Handle invalid input
    print("Error: Please enter valid numbers.")

finally:
    # This block always executes
    print("Finally block executed.")

# ------------------------------------------------------------
# Expected Output:
#
# Enter the first number: 20
# Enter the second number: 5
# Result: 4.0
# Finally block executed.
#
# ------------------------------------------------------------
# Another Expected Output:
#
# Enter the first number: 20
# Enter the second number: 0
# Error: Cannot divide by zero.
# Finally block executed.
# ------------------------------------------------------------
