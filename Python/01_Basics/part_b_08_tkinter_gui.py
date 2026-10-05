# ============================================================
# Part-B Program 8: GUI Using Tkinter
# Description: Create a simple Graphical User Interface (GUI)
#              using Python's built-in Tkinter module.
# ============================================================

import tkinter as tk


# Function to display the entered name
def display_message():
    name = name_entry.get()
    message_label.config(text="Welcome, " + name + "!")


# Create the main window
window = tk.Tk()
window.title("Student Information")
window.geometry("400x250")

# Add a heading
heading_label = tk.Label(
    window,
    text="BCA Student Information",
    font=("Arial", 16, "bold")
)
heading_label.pack(pady=20)

# Add name label
name_label = tk.Label(window, text="Enter your name:")
name_label.pack()

# Add name entry box
name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)

# Add button
display_button = tk.Button(
    window,
    text="Display Message",
    command=display_message
)
display_button.pack(pady=10)

# Label to display the message
message_label = tk.Label(
    window,
    text="",
    font=("Arial", 12)
)
message_label.pack(pady=10)

# Start the GUI application
window.mainloop()


# ------------------------------------------------------------
# Expected Output:
#
# A GUI window appears with:
#
#        BCA Student Information
#
#        Enter your name:
#        [______________________]
#
#        [ Display Message ]
#
# After entering "Rahul" and clicking the button:
#
#        Welcome, Rahul!
#
# Note: The output is displayed in a graphical window,
#       not in the Python console.
# ------------------------------------------------------------
