# ============================================================
# Part-B Program 4: Display Month and Year
# Description: Display the current month and year using
#              Python's built-in datetime module.
# ============================================================

from datetime import datetime

# Get the current date and time
current_date = datetime.now()

# Display the current month and year
print("Current Month:", current_date.strftime("%B"))
print("Current Year :", current_date.strftime("%Y"))

# ------------------------------------------------------------
# Expected Output:
#
# Current Month: October
# Current Year : 2026
#
# Note: The output will change according to the current
#       month and year when the program is executed.
# ------------------------------------------------------------
