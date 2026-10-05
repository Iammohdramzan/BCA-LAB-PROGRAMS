# ============================================================
# Part-B Program 7: Simple and Multiple Inheritance
# Description: Demonstrate simple inheritance and multiple
#              inheritance using Python classes.
# ============================================================


# ------------------------------------------------------------
# a) Simple Inheritance
# ------------------------------------------------------------

# Parent class
class Person:
    def display_person(self):
        print("This is the Person class.")


# Child class inherits from Person
class Student(Person):
    def display_student(self):
        print("This is the Student class.")


# Create object of child class
student = Student()

print("--- Simple Inheritance ---")
student.display_person()
student.display_student()


# ------------------------------------------------------------
# b) Multiple Inheritance
# ------------------------------------------------------------

# First parent class
class Father:
    def father_method(self):
        print("This method belongs to Father class.")


# Second parent class
class Mother:
    def mother_method(self):
        print("This method belongs to Mother class.")


# Child class inherits from both Father and Mother
class Child(Father, Mother):
    def child_method(self):
        print("This method belongs to Child class.")


# Create object of child class
child = Child()

print("\n--- Multiple Inheritance ---")
child.father_method()
child.mother_method()
child.child_method()


# ------------------------------------------------------------
# Expected Output:
#
# --- Simple Inheritance ---
# This is the Person class.
# This is the Student class.
#
# --- Multiple Inheritance ---
# This method belongs to Father class.
# This method belongs to Mother class.
# This method belongs to Child class.
# ------------------------------------------------------------
