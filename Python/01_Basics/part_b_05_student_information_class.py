# ============================================================
# Part-B Program 5: Student Information Using Class
# Description: Demonstrate the use of a class and object
#              to store and display student information.
# ============================================================

# Define a Student class
class Student:

    # Constructor to initialize student details
    def __init__(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    # Method to display student information
    def display(self):
        print("\n--- Student Information ---")
        print("Name    :", self.name)
        print("Roll No :", self.roll_no)
        print("Course  :", self.course)
        print("Marks   :", self.marks)


# Create a Student object
student1 = Student("Rahul", 101, "BCA", 85)

# Display student information
student1.display()

# ------------------------------------------------------------
# Expected Output:
#
# --- Student Information ---
# Name    : Rahul
# Roll No : 101
# Course  : BCA
# Marks   : 85
# ------------------------------------------------------------
