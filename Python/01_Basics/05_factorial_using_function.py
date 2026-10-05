# ============================================================
# Program 5: Find Factorial Using a Function
# Description: Calculate the factorial of a given number
#              using a user-defined function.
# ============================================================

# Define a function to calculate factorial
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


# Read a number from the user
num = int(input("Enter a number: "))

# Check for a valid input
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the factorial function
    fact = factorial(num)

    # Display the result
    print("Factorial of", num, "is:", fact)


# ------------------------------------------------------------
# Expected Output:
#
# Enter a number: 5
# Factorial of 5 is: 120
# ------------------------------------------------------------
